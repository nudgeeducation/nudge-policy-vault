---
title: Tag Taxonomy
audience: internal
groups: [slt-directors, all-staff]
provision: all
type: meta
status: live
---
Every policy in this vault carries the following YAML frontmatter. Tags drive the audience views, the commissioner pack, and the Nudge platform sign-off integration.

```yaml
---
title: <Policy Title>
audience: internal | external | both
groups: [list of groups this policy is relevant to]
provision: nudge-education | neo | haven | all
type: core | addendum | standalone-neo | inactive-neo
status: live | draft | archive
version: <e.g. Dec 2025 or v04.26>
owner_role: <role responsible — DSL, DPO, Director, etc.>
source_file: <original filename for audit>
neo_addendum: true | false
last_reviewed: YYYY-MM-DD
---
```

## Field reference

### audience
- **internal** — staff only; not surfaced on the public Quartz site
- **external** — commissioners, parents, carers, learners; surfaced publicly
- **both** — surfaced publicly with internal supplementary detail visible to staff via Nudge platform

### groups
- `all-staff` — every Nudge Education employee
- `practitioners` — named practitioner / mentor role across all provisions
- `qualified-teachers` — subject-specialist teachers (NEO live lessons)
- `dsl-safeguarding` — DSL, DDSL, and named safeguarding team
- `slt-directors` — Senior Leadership Team and Directors
- `office-staff` — finance, admin, HR, operational support
- `commissioners` — Local Authority commissioning officers
- `schools` — school-based commissioners, school DSLs, AP coordinators
- `parents-carers` — families of learners
- `learners` — learners themselves

### provision
- `nudge-education` — applies to Nudge Education Ltd parent operations
- `neo` — applies to Nudge Education Online specifically
- `haven` — applies to Haven (rare in this vault — Haven has its own)
- `all` — applies across all Nudge Education-operated provisions

### type
- `core` — canonical Nudge Education policy
- `addendum` — NEO online overlay added to a core policy (lives within the core file as a section)
- `standalone-neo` — NEO-only policy (no parent equivalent)
- `inactive-neo` — Nudge Education policy explicitly not applicable to NEO online provision
- `meta` — vault meta documents (taxonomy, indexes, change logs)

### status
- `live` — current, signed-off
- `draft` — in progress, awaiting sign-off (typically DSL for safeguarding)
- `archive` — superseded version retained for audit

### neo_addendum
- `true` — this core policy contains an NEO Online Addendum section
- `false` — no NEO addendum (NEO inherits unchanged, or NEO has a standalone)
