/**
 * Generate a PDF for every content page in the built Quartz site.
 *
 * Runs AFTER `npx quartz build`, reading from ./public and writing to
 * ./public/pdf/<slug>.pdf, so the PDFs deploy as ordinary static files.
 *
 * Usage:  node scripts/generate-pdfs.mjs
 * Requires: playwright (chromium) — installed in CI via
 *   npx playwright install --with-deps chromium
 */
import { chromium } from "playwright"
import { createServer } from "node:http"
import { readFile, mkdir, readdir, stat } from "node:fs/promises"
import { join, dirname, extname, relative } from "node:path"

const PUBLIC = "public"
const OUT = join(PUBLIC, "pdf")
const PORT = 8931

// Pages that get no PDF: list/index pages, tag pages, redirects, 404.
const SKIP = (slug) =>
  slug === "404" ||
  slug === "index" ||
  slug.endsWith("/index") ||
  slug.startsWith("tags/") ||
  slug === "tags"

const MIME = {
  ".html": "text/html",
  ".css": "text/css",
  ".js": "application/javascript",
  ".svg": "image/svg+xml",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".woff2": "font/woff2",
  ".json": "application/json",
  ".xml": "application/xml",
}

async function* walk(dir) {
  for (const entry of await readdir(dir)) {
    const p = join(dir, entry)
    if ((await stat(p)).isDirectory()) yield* walk(p)
    else yield p
  }
}

// Tiny static server so relative asset URLs resolve exactly as deployed.
const server = createServer(async (req, res) => {
  try {
    let path = decodeURIComponent(new URL(req.url, `http://localhost:${PORT}`).pathname)
    if (path.endsWith("/")) path += "index.html"
    let file = join(PUBLIC, path)
    try {
      if ((await stat(file)).isDirectory()) file = join(file, "index.html")
    } catch {
      if (!extname(file)) file += ".html"
    }
    const body = await readFile(file)
    res.writeHead(200, { "content-type": MIME[extname(file)] ?? "application/octet-stream" })
    res.end(body)
  } catch {
    res.writeHead(404)
    res.end()
  }
})

await new Promise((r) => server.listen(PORT, r))

const browser = await chromium.launch({
  executablePath: process.env.PW_CHROMIUM_PATH || undefined,
})
const page = await browser.newPage()

// Hide site chrome in the PDF: nav, sidebars, search, graph, backlinks, the
// PDF button itself. Keep the article, title, meta and tables.
const PRINT_CSS = `
  header, footer, .sidebar, .search, .darkmode, .reader-mode, .graph,
  .backlinks, .toc, .explorer, .breadcrumb-container, a.download-pdf,
  .tags, #quartz-announcement { display: none !important; }
  .page, .page > #quartz-body .center { max-width: 168mm !important; width: 100% ; margin: 0; padding: 0; }
  body { background: #ffffff !important; }
  article, h1.article-title { max-width: 168mm !important; overflow-wrap: break-word; }
  a.internal { color: inherit !important; text-decoration: none; }
`

let count = 0
const failures = []
for await (const file of walk(PUBLIC)) {
  if (extname(file) !== ".html") continue
  const slug = relative(PUBLIC, file).replace(/\.html$/, "").replaceAll("\\", "/")
  if (SKIP(slug)) continue
  const out = join(OUT, `${slug}.pdf`)
  try {
    await mkdir(dirname(out), { recursive: true })
    await page.goto(`http://localhost:${PORT}/${slug}`, { waitUntil: "networkidle" })
    await page.emulateMedia({ media: "print" })
    await page.addStyleTag({ content: PRINT_CSS })
    await page.pdf({
      path: out,
      format: "A4",
      margin: { top: "20mm", bottom: "20mm", left: "18mm", right: "18mm" },
      displayHeaderFooter: true,
      headerTemplate: `<div style="font-size:7pt; color:#6b7b8d; width:100%; text-align:right; padding-right:18mm; font-family: Arial, sans-serif;">Nudge Education Policy Library &middot; policies.nudgeeducation.online</div>`,
      footerTemplate: `<div style="font-size:7pt; color:#6b7b8d; width:100%; text-align:center; font-family: Arial, sans-serif;">Page <span class="pageNumber"></span> of <span class="totalPages"></span> &middot; Printed from the live Policy Library &mdash; the website is the controlled version</div>`,
    })
    count++
  } catch (e) {
    failures.push(`${slug}: ${e.message}`)
  }
}

await browser.close()
server.close()

console.log(`Generated ${count} PDFs into ${OUT}`)
if (failures.length) {
  console.error(`FAILED (${failures.length}):\n` + failures.join("\n"))
  process.exit(1)
}
