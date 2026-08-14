import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"
import { joinSegments, pathToRoot } from "../util/path"

/**
 * "Download as PDF" link for policy pages.
 *
 * PDFs are generated at build time by scripts/generate-pdfs.mjs into
 * public/pdf/<slug>.pdf. This component renders a link to the matching PDF
 * on every content page (skipping index/list pages, where a single-page PDF
 * makes no sense).
 */
const DownloadPdf: QuartzComponent = ({ fileData, displayClass }: QuartzComponentProps) => {
  const slug = fileData.slug
  if (!slug || slug === "index" || slug.endsWith("/index")) {
    return null
  }
  const baseDir = pathToRoot(slug)
  const pdfHref = joinSegments(baseDir, "pdf", `${slug}.pdf`)
  return (
    <a
      href={pdfHref}
      class={classNames(displayClass, "download-pdf")}
      download
      title="Download this policy as a PDF"
    >
      Download as PDF
    </a>
  )
}

DownloadPdf.css = `
a.download-pdf {
  display: inline-block;
  margin: 0.2rem 0 0.8rem 0;
  padding: 0.25rem 0.75rem;
  border: 1px solid var(--secondary);
  border-radius: 4px;
  font-size: 0.8rem;
  text-decoration: none;
  color: var(--secondary);
}
a.download-pdf:hover {
  background-color: var(--secondary);
  color: var(--light);
}
`

export default (() => DownloadPdf) satisfies QuartzComponentConstructor
