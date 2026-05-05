# Nudge Education Policy Vault

The unified policy library operated by **Nudge Education Ltd** (Company Number 10192753), covering both face-to-face interventions and the online provision **Nudge Education Online (NEO)**.

🔗 **Live site:** https://policies.nudgeeducation.online/

## Architecture

Where Nudge Education already holds a canonical policy and NEO requires online-specific provisions, those provisions appear as an **NEO Online Addendum** block at the end of the canonical policy. Genuinely online-specific policies live in `content/neo-only/`. See [`SETUP.md`](SETUP.md) for local development and [`content/00-index/about.md`](content/00-index/about.md) for the architecture overview.

## Provisions covered

- **Nudge Education Ltd** — face-to-face interventions across the UK
- **Nudge Education Online (NEO)** — fully online alternative provision, launching September 2026

## Stack

Built with [Quartz 4](https://quartz.jzhao.xyz/) on top of an Obsidian-format markdown vault. Auto-deploys to GitHub Pages via `.github/workflows/deploy.yml` on every push to `main`.
EOF
```

If you keep the upstream Quartz README, that's fine too — just be aware it'll be the public-facing description of the repo.

### 3. Initialise git locally

```bash
git init -b main
git add .
git commit -m "Initial commit: Nudge Education + NEO unified policy vault

- 78 markdown files: 13 core+addendum, 5 NEO standalone, 23 inherited
  unchanged, 5 new addendums (DRAFT), 5 inactive-NEO, plus indexes,
  audience MOCs, and procurement pack
- Quartz 4.5.2 configured with Nudge brand (navy/teal/cream, Fraunces+Inter)
- en-GB locale, Pages workflow at .github/workflows/deploy.yml
- DRAFT status preserved on NEO Safeguarding (pending DSL sign-off) and
  the 5 newly authored NEO addendums (pending policy-owner review)"
```

### 4. Create the GitHub repo and push

Using GitHub CLI (recommended):

```bash
gh repo create nudgeeducation/policy-vault \
  --public \
  --source=. \
  --push \
  --description "Nudge Education Ltd + NEO unified policy vault. Built with Obsidian + Quartz."
```

That command creates the repo under the `nudgeeducation` org, sets the remote, and pushes `main` in one step.

If `gh` prompts you to confirm the org, choose `nudgeeducation`.

### 5. Enable GitHub Pages

GitHub Pages needs to be set to "GitHub Actions" as the source so the deploy workflow at `.github/workflows/deploy.yml` runs.

Via CLI:

```bash
gh api -X PUT repos/nudgeeducation/policy-vault/pages \
  -f 'build_type=workflow' \
  -f 'source[branch]=main' \
  -f 'source[path]=/'
```

Or via the web:

1. Go to <https://github.com/nudgeeducation/policy-vault/settings/pages>
2. Under "Build and deployment" → "Source", select **GitHub Actions**
3. Save

### 6. Watch the first deploy

The deploy workflow triggers automatically on push to `main`. Watch it run:

```bash
gh run watch
```

Or via the web at <https://github.com/nudgeeducation/policy-vault/actions>.

First build takes ~2–3 minutes (npm install + Quartz build + Pages deploy).

### 7. Visit the live site

Once the workflow completes:

<https://nudgeeducation.github.io/policy-vault/>

## What to do if the deploy fails

The most common first-push failure is GitHub Pages not yet being enabled in the repo settings (step 4). If you see an error like "Get Pages site failed", complete step 4 then re-run the workflow:

```bash
gh workflow run deploy.yml
```

## Future updates

Once initial push is done, future updates are simply:

```bash
git add .
git commit -m "Update <describe what changed>"
git push
```

The deploy workflow re-runs on every push to `main`.

## Working in Obsidian alongside git

You can edit any policy in Obsidian (open the `content/` folder as a vault), and the markdown changes are tracked by git like any other text file. Recommended flow:

1. Edit in Obsidian (or any markdown editor)
2. Build locally with `npx quartz build --serve` to preview at <http://localhost:8080/>
3. Once happy, `git add . && git commit -m "..." && git push`
4. The Pages site rebuilds automatically

## Useful repo-management commands

| Task | Command |
|---|---|
| See workflow runs | `gh run list` |
| Re-trigger latest workflow | `gh workflow run deploy.yml` |
| View the live site | `gh browse` (opens repo) or visit Pages URL |
| Open repo in browser | `gh repo view --web` |
| Toggle to private (if needed) | `gh repo edit --visibility private` |
