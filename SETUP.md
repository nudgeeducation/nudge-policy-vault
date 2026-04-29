# Local setup — Nudge Education Policy Vault

This vault uses [Quartz](https://quartz.jzhao.xyz/) to publish the Obsidian-formatted markdown content as a static site.

## Prerequisites

- Node.js 22 or newer
- npm 10.9.2 or newer

Check with:

```bash
node --version
npm --version
```

## First-time setup

From the vault root (`/Users/kirstinstevens/Documents/Claude/Projects/Nudge Education/nudge-policy-vault/`):

```bash
npm install
```

This installs Quartz and its dependencies into `node_modules/`. Takes ~1–2 minutes.

## Build the static site

```bash
npx quartz build
```

Output goes to `public/`. You can open `public/index.html` directly in a browser.

## Preview locally with live reload

```bash
npx quartz build --serve
```

Site is then visible at `http://localhost:8080/`. Edits to any file in `content/` reload the browser automatically. Great for content review.

## Open the vault in Obsidian

1. Launch Obsidian
2. Open vault → select the `content/` folder of this repo
3. Edit any `.md` file as normal — Quartz reads the same files

## Folder layout

```
nudge-policy-vault/
├── content/                  Vault content (Obsidian + Quartz read this)
│   ├── 00-index/             Vault meta (taxonomy, change log, about)
│   ├── 01-all-company/       Whole-company policies
│   ├── 02-hr-employee-relations/
│   ├── 03-service-delivery/
│   ├── 04-office/
│   ├── 05-commissioning-pack/  External commissioner-facing
│   ├── 06-management-executive/
│   ├── 07-intervention-safety/
│   ├── neo-only/             NEO standalone policies
│   ├── audience/             Audience-specific MOC pages
│   └── archive/              Superseded versions
├── quartz/                   Quartz framework code
├── quartz.config.ts          Site configuration (brand, baseUrl, plugins)
├── quartz.layout.ts          Page layout config
├── package.json
└── public/                   Build output (don't commit)
```

## Brand configuration

Brand colours, fonts, and metadata are in `quartz.config.ts`. The Nudge Education palette:

| Token | Hex | Use |
|---|---|---|
| Navy | `#1A2E3B` | Primary dark / headers / links |
| Teal | `#2AB3A0` | Accent / hover / highlight |
| Cream | `#F7F7F5` | Page background |
| Charcoal | `#2D3436` | Body text |

Typography: **Fraunces** (display) + **Inter** (body) + **IBM Plex Mono** (code). Loaded from Google Fonts.

## Editing content

Each policy is a single `.md` file with YAML frontmatter at the top. The frontmatter schema:

```yaml
---
title: Policy Title
audience: internal | external | both
groups: [all-staff, commissioners, ...]
provision: nudge-education | neo | haven | all
type: core | addendum | standalone-neo | inactive-neo
status: live | draft | archive
version: Dec 2025
owner_role: Director of Operations
source_file: path/to/original.pdf
neo_addendum: true | false
---
```

See [[content/00-index/tag-taxonomy|Tag Taxonomy]] for the full reference.

## Adding a new policy

1. Create a new `.md` file in the appropriate category folder under `content/`
2. Add frontmatter at the top
3. Write the body in markdown
4. Add a link to it from the relevant index pages and audience MOCs
5. Run `npx quartz build --serve` to preview

## Deploying to GitHub Pages

When ready to publish, push this repo to the `nudgeeducation` GitHub org. The deploy workflow at `.github/workflows/deploy.yml` (to be added during the push step) handles the build and Pages publishing automatically.
