---
title: About this Vault
audience: both
groups: [all-staff, commissioners, slt-directors]
provision: all
type: meta
status: live
---

# About the Nudge Education Policy Vault

The single source of truth for all policies operated by **Nudge Education Ltd**, including the online provision **Nudge Education Online (NEO)**.

This site is built from an Obsidian vault published with [Quartz](https://quartz.jzhao.xyz/). Every policy is authored in markdown with structured frontmatter, then rendered as a connected, searchable website.

## Provisions covered

- **Nudge Education Ltd** (Company Number 10192753) — the parent company, operating face-to-face interventions across the UK
- **Nudge Education Online (NEO)** — the fully online alternative provision, launching September 2026

Haven, a separate hyflex provision, maintains its own [policy site](https://thenovacene.github.io/haven-policy-site/) and is not covered by this vault.

## Architecture

Where Nudge Education already holds a canonical policy and NEO requires online-specific provisions, those provisions appear as an **NEO Online Addendum** block at the end of the canonical policy — not as a duplicate document. This means:

- **One canonical policy** per topic
- **One approval trail** per topic
- **One version** for LAs to verify
- **NEO-specific online content** clearly marked but not separated

Genuinely online-specific policies (where Nudge Education has no parent equivalent — Online Safety, AI Policy, Home-School Agreement, Teaching & Learning, Behaviour & Regulation) live in the [[../neo-only/index|NEO Online section]].

## Browse

- [[../index|Home]] — start here
- [[../audience/commissioner-pack|Commissioner Pack]] — for LA commissioning officers
- [[../audience/parents-carers-pack|Parents & Carers Pack]] — for families
- [[tag-taxonomy|Tag Taxonomy]] — how policies are classified
- [[change-log|Change Log]] — vault build history

## Tag taxonomy in brief

Every policy carries frontmatter with these fields:

| Field | Purpose |
|---|---|
| `audience` | internal / external / both — drives public vs internal visibility |
| `groups` | which staff/audience groups need this policy (drives induction packs) |
| `provision` | nudge-education / neo / haven / all |
| `type` | core / addendum / standalone-neo / inactive-neo |
| `status` | live / draft / archive |
| `version` | current version marker |
| `owner_role` | role responsible for the policy |
| `source_file` | original document path for audit trail |

See [[tag-taxonomy|the full taxonomy]] for details.

## Status

Vault built April 2026. See the [[change-log|change log]] for ongoing work.
