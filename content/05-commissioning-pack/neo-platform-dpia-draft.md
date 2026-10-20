---
title: NEO Platform DPIA (draft for DPO completion)
audience: internal
groups: [slt-directors]
provision: neo
type: core
status: draft
version: 0.1-draft
owner_role: Data Protection Officer
neo_addendum: false
source_file: Drafted from neo-architecture (solutions-architecture.md, setting-up-neo.md, agentic-platform), the NEO Data Protection, Confidentiality and Privacy Policy v04.26, and the canonical DPIA Form template.
---
> **Operated by:** Nudge Education Ltd (Company No. 10192753) · **Owner:** Data Protection Officer (function held by the Director, NEO & Head of School during the initial period) · **Status:** DRAFT for DPO completion and sign-off

## How to read this draft

This is a **populated draft**, not a completed DPIA. It uses the canonical Nudge Education DPIA Form structure (`dpia-form.md`) and fills the sections that can be sourced from NEO's committed architecture and policy documents. Three things to hold in mind:

1. **Whole-platform scope.** This is a platform-level "master" DPIA for NEO. It does **not** discharge the requirement for processing-specific DPIAs that *Setting up NEO* §15.3 and the architecture §12 already mandate: the intake/enrolment agent, the Claude Developer Platform, the filtering & monitoring tool selection, and any Gemini for Workspace enablement each need their own DPIA (or an addendum to this one). This document is the parent they hang off.

2. **Marked placeholders are the DPO's to complete.** Anything tagged **`[DPO TO COMPLETE]`** or **`[DPO TO CONFIRM]`** is a lawful-basis, necessity, risk-scoring, consultation or sign-off judgement that must not be inferred from architecture. Filling these from memory would be worse than leaving them blank.

3. **Category-level only.** This document describes data *categories*, never named learners or real incidents, consistent with NEO's role-only-naming and children's-data discipline. Keep it that way.

**Source documents:** NEO Solutions Architecture (v0.2-draft, 30 Apr 2026); Setting up NEO — Systems Account Set Up (v2.0, 22 Apr 2026); Agentic Platform authorisation paperwork (Claude Developer Platform, 26 May 2026); NEO Data Protection, Confidentiality and Privacy Policy (v04.26); Data Protection and Information Security Policy (Dec 2025); and the DPO review meeting of 23 June 2026 with the retained data-protection consultancy (Data Protection People Ltd).

> **Review status:** The retained DP consultancy (Data Protection People Ltd) is reviewing this DPIA and will return comments. A Record of Processing Activities (ROPA) is being maintained in parallel by the company DPO and the consultancy; this DPIA should be cross-referenced against it. The actions surfaced in the 23 June review are consolidated in the box below.

## Actions identified at the DPO review (23 June 2026)

These are open items, not yet closed. They are the priority work before the September 2026 launch.

1. **Learner / platform privacy notice does not yet exist.** NEO currently has privacy notices for web users and commissioners only. A learner-facing privacy notice — child-friendly (11–13 and 14–18 registers), covering AI use and **lesson transcription** specifically — must be drafted, surfaced before sign-up/sign-in, and linked in the footer of both the NEO and Nudge websites. Consent from parents/carers is gathered before learners use the platform.
2. **No executed Data Processing Agreement / due-diligence record for Google or Anthropic.** Due-diligence questionnaires and DPAs are outstanding for both. The retained consultancy is providing templates. NEO uses Google Workspace **Business** (not Google for Education — an alternative provision does not qualify), so education-grade lockdowns are configured manually; the allow/disallow decisions are documented in *Setting up NEO*.
3. **Launch cohort is 13+** — see the scope note below; reconcile against the committed architecture, which states 11–18.
4. **Map the in-provision data flows**, not just intake: Google Classroom chat, Google Meet transcripts, and homework/assignment artifact submissions — where each is stored, how, and for how long.
5. **Legitimate-interest assessments (LIAs)** and any public-interest assessments will be needed in due course; the consultancy has parked these behind the DPIA to avoid overload.

---

# Part 1 — DPIA Screening

## Background

**Project / processing:** Nudge Education Online (NEO) — a fully online alternative provision operated by Nudge Education Ltd, launching September 2026. **Launch cohort: learners aged 13–18** (NEO opens to over-13s at launch; processing children's data below 13 is deliberately deferred to reduce the additional Children's Code consent burden). The documented provision range in the architecture and policy is 11–18; **this inconsistency must be reconciled** — if under-13s are admitted later, the under-13 parental-consent and age-appropriate provisions in §11 of the policy and the Children's Code apply and this DPIA must be revisited. This DPIA covers the NEO platform as a whole: the NOOMA operations platform (identity, enrolment, timetabling, risk-assessment generation, audit), the Google Workspace delivery layer (Classroom, Meet, Calendar, Drive, Groups), the GitHub-hosted knowledge layer (RA verse library and policy vault — institutional data only), and the public-facing marketing, policy and curriculum surfaces.

**New or variation:** New processing. NEO is a new provision; the platform brings together new systems and new data flows, including children's special-category data processed at scale across digital platforms, and agentic-AI components in the operational path. This meets the UK GDPR Article 35 threshold for a mandatory DPIA.

**Objectives of the processing:** to deliver online education and pastoral support; to maintain safeguarding; to individualise provision through structured learner pen portraits; to meet statutory and OEAS-accreditation obligations; and to provide commissioners (local authorities and schools) with attendance, progress and safeguarding assurance.

## Screening questions

A DPIA is **required**. The following criteria are met:

- ☑ **Processing of special-category / highly personal data** — SEND, EHCP, health, safeguarding records, behavioural and pastoral notes, EBSNA history.
- ☑ **Processing concerning vulnerable data subjects** — children (13–18 at launch), many with significant additional vulnerability; the defining population of an alternative provision.
- ☑ **Systematic monitoring** — filtering and monitoring of learner accounts for online-safety/harm indicators (tool under selection per *Setting up NEO* §10.5).
- ☑ **Evaluation or scoring / profiling** — structured pen-portrait flags drive individualised risk-assessment controls; attendance and engagement tracking.
- ☑ **Innovative technology** — agentic-AI components (NOOMA agents invoking the Claude Developer Platform) in the operational workflow.
- ☑ **Matching / combining datasets** — NOOMA reconciles its own records with Google Workspace data and with commissioner-supplied referral data.
- ☑ **Data that could risk physical harm in the event of a breach** — safeguarding records relating to at-risk children.

**Screening result:** Full DPIA required. Proceed to Part 3.

---

# Part 2 — Guidance Notes

The standard ICO guidance notes on what constitutes "likely to result in high risk" (evaluation/scoring, automated decision-making, systematic monitoring, sensitive data, large-scale processing, dataset matching, vulnerable subjects, innovative technology, denial of service/contract) apply unchanged from the canonical `dpia-form.md`. They are not reproduced here; refer to the template. The screening above identifies which of these criteria NEO meets and why.

---

# Part 3 — DPIA

## About the processing

### What data is being processed?

Sourced from the NEO Data Protection Policy v04.26 §5 and the Solutions Architecture data model §5.

**Learner data (LEARNER_PROFILE, PEN_PORTRAIT, ENROLMENT, ATTENDANCE):**

- Name, date of birth, address, contact details.
- SEND information, EHCP documentation, health and medical needs *(special category — Art. 9)*.
- Attendance, engagement and academic-progress records.
- Safeguarding records and referrals *(special category / sensitive — risk of physical harm)*.
- Behavioural logs and pastoral notes.
- EBSNA history and context shared at admission.
- Session recordings — primarily the educator/lesson feed; learner voice/image captured only incidentally (see §17 of the policy and the lesson-recordings rule).
- **Lesson transcripts** — the principal AI-touchpoint in live delivery. Transcription captures spoken classroom interaction and can support (or be used to infer) reading age, language ability and engagement. This is rich, sometimes very personal, learning-conversation data; its storage location, access controls, retention (one academic term unless required for safeguarding) and any inferences drawn from it must be tightly controlled. *Potentially special-category by inference.*
- **Google Classroom chat** and learner–educator communication.
- **Homework / assignment artifact submissions** posted to Google Classroom (learner-created work and any personal content within it).
- Structured pen-portrait flags used for individualisation *(may encode health/SEND — special category)*.

**Parent / carer data (GUARDIAN_CONTACT, GUARDIAN_LINK):** name, contact details, relationship to learner, emergency contacts, consent records, billing/invoicing data where fees are family-paid.

**Staff / practitioner / contractor data (STAFF_PROFILE, EDUCATOR_PROFILE):** name, contact details, qualifications, employment history, DBS outcomes and Single Central Record entries *(criminal-offence data — Art. 10)*, payroll/contractual data, training and performance records.

**Commissioner data (COMMISSIONER, COMMISSIONER_CONTACT):** commissioning-body and contact details; commission records linking a commissioner to a learner.

**System / audit data (AUDIT_EVENT):** append-only log of auth events, role/permission changes, RA generations and certifications, policy lookups, Google API calls, break-glass invocations and bulk exports.

**Special-category and criminal-offence summary:** health, SEND/EHCP, safeguarding, ethnicity (where processed), and DBS/criminal-offence data are all in scope. Processing relies on an Article 9 condition (and Article 10 / DPA 2018 Schedule 1 condition for DBS data). **`[DPO TO COMPLETE]` — cite the specific Article 9 condition(s) and the DPA 2018 Schedule 1 paragraph(s), and confirm an Appropriate Policy Document is in place (DPA 2018 Sch 1 Pts 3–4).**

### Who is the data about?

- ☑ Learners (children aged 11–18) — vulnerable data subjects; the core population.
- ☑ Parents / carers.
- ☑ Members of staff, practitioners, contractors, volunteers (and prospective).
- ☑ Commissioner contacts (LA / school staff).

**Reasonable expectations:** learners and families would expect an education provider to hold and process the categories above to deliver education and discharge safeguarding duties. Processing that may exceed default expectation — agentic-AI components and filtering/monitoring of learner accounts — is addressed through transparency measures (age-appropriate privacy notices, §11 of the policy) and the human-in-the-loop safety contract (architecture §2.5). **`[DPO TO CONFIRM]` — that privacy notices for learners (11–13 and 14–18 versions), parents and commissioners are published and cover AI use and monitoring.**

### Purpose of the processing

To deliver online education and individualised pastoral support to learners aged 11–18; to maintain safeguarding; to generate and certify risk assessments tied to each learner's pen portrait; to meet statutory duties (KCSIE 2025, Online Safety Act 2023, education law) and OEAS-accreditation evidence obligations; and to provide commissioners with proportionate attendance, progress and safeguarding assurance.

### Nature and context of the processing

NEO operates within a single legal entity (Nudge Education Ltd) across two Google Workspace tenants (`nudgeeducation.co.uk` for the face-to-face parent business; `nudgeeducation.online` for NEO). NOOMA is the source of truth for identity, enrolment, timetabling, RAs and audit; Google Workspace is the live-delivery layer; two GitHub repositories hold institutional knowledge only (no learner data). Processing is continuous through term time, large-scale relative to the learner population, and concerns a uniquely vulnerable group.

**Novel elements:** (a) agentic-AI components — NOOMA constructs prompts and invokes the Claude Developer Platform for synthesis steps, with humans certifying every output; practitioners never hand-prompt the model; (b) systematic filtering/monitoring of learner accounts (tool under selection); (c) structured individualisation driving generated risk-assessment controls. Each carries its own DPIA or addendum per Part 1 note 1.

## Users and uses of the information

### Disclosures and sharing

- **Commissioners (LAs / schools):** attendance, safeguarding and progress data shared securely and proportionately. The commissioner may be controller, joint controller, or NEO may be processor, depending on context (policy §12). **`[DPO TO CONFIRM]` — data-sharing / data-processing agreements in place per commissioner.**
- **Safeguarding partners / statutory bodies:** information shared on a need-to-know basis where necessary to protect a child (DfE *Information Sharing* 2018; Caldicott principles), defided by the DSL who records the rationale and lawful basis.
- **Processors:** see below.

### Data processors

| Processor | Processing | Notes / status |
|---|---|---|
| Google (Workspace **Business**, Classroom, Meet, Calendar, Drive, Groups) | Live delivery; document, message, assignment and recording/transcript storage; guardian-summary email | Managed accounts. **GAP (23 Jun review): no executed DPA or completed due-diligence questionnaire yet** — consultancy providing templates. NEO uses Google Workspace Business, not Google for Education (AP does not qualify), so feature lockdowns are configured manually and documented in *Setting up NEO*. |
| Google Gemini / NotebookLM / custom "gems" (within the Google Workspace) | Generic lesson-plan generation via custom gems (no identifiable learner data); staff productivity | Gemini OFF by default for all OUs; enabled **per-OU for staff (teachers/SLT) only** under documented authorisation; **never default-on for learners**. Custom gems standardise lesson-plan output; inputs are generic, not learner-identifiable. |
| Anthropic, PBC (Claude Developer Platform — API, Agent SDK, Claude Code) | Synthesis steps in NOOMA agents; build-phase developer tooling (accessed from a Nudge-managed device/account) | Receives institutional / pseudonymised data only; no learner names, DOB, addresses, contact details, safeguarding content or lesson recordings (agentic-platform §2). API data not used for training by default. **GAP (23 Jun review): formal due-diligence record / DPA outstanding.** EU-region endpoint pinning and sub-processor list **`[DPO TO CONFIRM]` at sign-off and quarterly**; US-based processor — confirm transfer mechanism. |
| GitHub (knowledge layer + public sites) | Hosts institutional verse/policy repos and public-facing Quartz sites | Institutional data only; no personal data |
| Filtering & monitoring vendor (under selection: Smoothwall / Senso / Securly UK / Lightspeed) | Systematic monitoring of learner accounts for harm indicators | **Not yet selected**; selection requires its own DPIA before learner onboarding (*Setting up NEO* §10.5) |
| Off-site backup provider | Encrypted off-site backup (AES-256, SSL) | Per Data Protection & Information Security Policy |

**`[DPO TO COMPLETE]` — confirm the full processor list, that a written DPA is in place for each, and the international-transfer position for any non-UK processor (notably Anthropic — US-based; confirm transfer mechanism and residency posture).**

### IT systems

NOOMA (operations platform); Google Workspace; GitHub (private repos + Pages); the agentic layer (Claude Developer Platform via API/SDK); secure cloud storage for safeguarding/EHCP evidence; encrypted off-site backup. Data flows are documented in the Solutions Architecture §3 (system context), §5 (data model), §6 (Google integration) and §7 (knowledge layer) — those Mermaid diagrams should be attached as the visual data-flow record this section requires.

### Responsibility / beneficiaries

**Process owner / responsibility:** Director, NEO & Head of School, holding the DPO function during the initial period (policy §7). Proprietor (Diego Melo) is the named accountable person under the OEAS framework. Company DPO / Information Security: Brian Mair, Director of Operations. System Architect: Felipe Lyra.

**Beneficiaries / intended effects:** learners benefit from individualised, safer online provision; families gain transparency and safeguarding assurance; commissioners receive proportionate evidence. Intended effect on individuals is positive; the assessment below addresses the risks.

## Consultation process

**`[DPO TO COMPLETE]`** — Describe the consultation undertaken or planned with: learners and families (age-appropriately); staff/practitioners; the DSL (termly joint DSL/DPO review per policy §6/§19); commissioners; and, where residual high risk cannot be mitigated, the ICO (prior consultation under Art. 36). State who else internally is consulted to ensure all risks are understood. *Not inferable from architecture — this is a record of activity that must actually happen.*

## Assessing the processing's necessity and proportionality

The processing is necessary to deliver online alternative provision and discharge safeguarding and statutory duties; there is no materially lower-risk alternative that still delivers individualised, safeguarded online education. Proportionality is supported architecturally by least-privilege-by-default, capabilities-not-roles, relationship-based access, absolute domain walls (safeguarding/finance/HR/governance), time-bounded access, and data minimisation in the AI path (pseudonymised references; no learner names to the model; no lesson recordings ever sent externally).

**`[DPO TO COMPLETE]`** — Confirm the necessity-and-proportionality judgement for each high-risk element (monitoring, agentic AI, profiling) and that less-intrusive alternatives were considered and recorded.

## Rights

Responsibility for responding to data-subject rights requests sits with the DPO (`neo@nudgeeducation.co.uk`); NEO responds within one calendar month (policy §13). SARs touching safeguarding records are handled with the DSL to avoid compromising a child's safety. Rights covered: be informed, access, rectification, erasure, restriction, portability, object, and rights relating to automated decision-making/profiling. **`[DPO TO CONFIRM]` — the rights-request procedure is documented and accessible, and the position on automated processing is stated (note: NEO's design keeps a human decision-maker in the loop for any AI output affecting a learner, so no solely-automated significant decisions are made).**

## Data protection principles

### Privacy information

**GAP (23 Jun review):** a learner-facing / platform privacy notice does **not yet exist** — only web-user and commissioner notices are published. Required before launch: a child-friendly notice (11–13 and 14–18 registers) disclosing AI use, lesson transcription and any monitoring, surfaced before sign-up/sign-in and linked in both website footers, with parental consent gathered before learners use the platform. Parent and commissioner notices per policy §11/§12.

### Lawful basis

Article 6 bases relied on (policy §10): public task (Art. 6(1)(e)) for education provision; legal obligation (Art. 6(1)(c)) for safeguarding/tax/employment; consent (Art. 6(1)(a)); contract (Art. 6(1)(b)) for fees; legitimate interests (Art. 6(1)(f)) for institutional code/architecture; vital interests (Art. 6(1)(d)) to protect life. Special-category data under an Article 9 condition (explicit consent; safeguarding of children; legal obligation; substantial public interest).

**`[DPO TO COMPLETE]`** — For each processing purpose, state the specific Article 6 basis **and**, for special-category and criminal-offence data, the specific Article 9 condition and DPA 2018 Schedule 1 condition, with the Appropriate Policy Document referenced. Where legitimate interests is relied on, attach the LIA; where public task, attach the PIA.

### Purpose limitation and minimisation

Purpose limitation is enforced by the design principles and by the AI pre-call sanitisation layer (only the minimum data required for a task reaches the model; conservative defaults; data classes flagged "No" are never sent — agentic-platform §2). Minimisation is structural: relationship-based access means no staff member has general access to learner records by virtue of being staff.

### Accuracy

Pen portraits are versioned; learner records are maintained current by the assigned practitioner; the system flags session plans referencing outdated verses or policies. **`[DPO TO CONFIRM]` — process for keeping learner and safeguarding data accurate and up to date.**

### Storage limitation

Indicative retention (policy §16): learner records, safeguarding records and EHCP documentation until the learner's 25th birthday (DfE / KCSIE 2025 / SEND Code of Practice 2015); session recordings and lesson transcripts one academic term unless required for safeguarding; staff employment records six years; DBS certificates destroyed once recorded on the SCR; financial/payroll six years. Google Vault is used to apply policy-level retention (e.g. six-year secure retention for leaver data) and legal hold. Audit logs are exported beyond Google's 180-day native retention to span a full term-time year (architecture §2.1 principle 6; *Setting up NEO* §10.3 Google Vault retention). **`[DPO TO CONFIRM]`** retention for Google-owned in-provision data — Classroom chat, Meet transcripts and homework/assignment submissions. End-of-life data is securely deleted/destroyed; the DPO reviews retained data annually.

### Security

Architectural and organisational controls evidenced across the source documents:

- **Identity/access:** least privilege by default; capabilities-not-roles; relationship-based access; absolute domain walls; time-bounded access with daily expiry job and 14-day renewal alerts (architecture §5a).
- **Admin separation:** two-account pattern; Super Admin held only by a non-personal `systems@` (mature state) or a single-purpose named account (current state); hardware-key (FIDO2) authentication; one-hour sessions; alert-on-action; break-glass with DSL notification and post-event review.
- **Agentic-AI controls:** default third-party OAuth blocked at tenant level; new tools via the §11.3 authorisation flow (written request → Diamond AI Policy review → allowlist with end date → per-user authorisation → quarterly review → documented decommission); no unmonitored agents; no autonomous action privileges; Gemini for Workspace OFF for all OUs at launch pending AI Policy publication, DPIA sign-off and training.
- **Encryption:** data encrypted at rest and in transit; encrypted off-site backup (AES-256 over SSL); TLS for email; secure cloud storage for safeguarding/EHCP restricted to DSL/DPO/authorised staff.
- **Audit:** immutable, queryable audit of every sensitive access, permission change, break-glass and bulk export.
- **People controls:** enhanced DBS, Single Central Record, annual data-protection training, leaver access-revocation process.
- **Baseline:** Cyber Essentials Plus targeted; annual information-governance audit (supported by Data Protection People Ltd); 72-hour ICO breach notification and Data Incident Register (policy §14).

## Risk assessment

**`[DPO TO COMPLETE — risk scoring is the DPO's assessment, not to be inferred from architecture.]`** The table below seeds candidate risks drawn from the source documents. The DPO must set likelihood, severity, overall and residual scores, and confirm/extend mitigations. Likelihood: remote / possible / probable. Severity: minimal / significant / severe. Overall and residual: low / medium / high.

| # | Risk, source and nature of impact on individuals | Likelihood | Severity | Overall | Mitigations (from source docs; DPO to confirm/extend) | Effect | Residual |
|---|---|---|---|---|---|---|---|
| 1 | Learner personal/safeguarding data inadvertently included in an AI prompt → loss of confidentiality, potential harm | `[DPO]` | `[DPO]` | `[DPO]` | NOOMA pre-call sanitisation; pseudonymised refs only; no names/safeguarding content/recordings sent; build-phase human review | `[DPO]` | `[DPO]` |
| 2 | Unauthorised access to learner/safeguarding records → loss of confidentiality, risk of physical harm | `[DPO]` | `[DPO]` | `[DPO]` | Least privilege; relationship-based access; domain walls; hardware keys; immutable audit | `[DPO]` | `[DPO]` |
| 3 | Processor breach (Google / Anthropic / backup / filtering vendor) | `[DPO]` | `[DPO]` | `[DPO]` | DPAs; data minimisation to processors; quarterly AI review; breach-notification commitments | `[DPO]` | `[DPO]` |
| 4 | Filtering/monitoring of learners is disproportionate or opaque → intrusion, chilling effect | `[DPO]` | `[DPO]` | `[DPO]` | Dedicated DPIA before onboarding; UK residency selection criteria; transparency in privacy notices; human-decides principle | `[DPO]` | `[DPO]` |
| 5 | International transfer to a US processor (Anthropic) without an adequate mechanism | `[DPO]` | `[DPO]` | `[DPO]` | EU-endpoint pinning; transfer mechanism `[DPO TO CONFIRM]`; quarterly residency re-check | `[DPO]` | `[DPO]` |
| 6 | Children's data processed in ways exceeding reasonable expectation (AI, profiling) → Children's Code non-conformance | `[DPO]` | `[DPO]` | `[DPO]` | Age-appropriate notices; privacy-protective defaults; no targeted advertising; no solely-automated significant decisions; human-in-the-loop | `[DPO]` | `[DPO]` |
| 7 | Agentic component drifts / produces harmful output affecting a learner | `[DPO]` | `[DPO]` | `[DPO]` | Per-model-version validation; human certifies every output; tool-side capability enforcement; no autonomous action | `[DPO]` | `[DPO]` |
| 8 | Excessive retention of learner/safeguarding data | `[DPO]` | `[DPO]` | `[DPO]` | Defined retention schedule (policy §16); annual DPO retention review; secure destruction | `[DPO]` | `[DPO]` |
| 9 | Inaccurate pen-portrait/individualisation flags → wrong controls applied | `[DPO]` | `[DPO]` | `[DPO]` | Versioned pen portraits; taxonomy normalisation (open UQ); human certification of every RA | `[DPO]` | `[DPO]` |
| 10 | Domain transfer / DNS or break-glass misuse → availability or integrity loss | `[DPO]` | `[DPO]` | `[DPO]` | Transfer lock; break-glass review; immutable audit; backup/continuity plan | `[DPO]` | `[DPO]` |
| 11 | Lesson transcripts retained/accessed too widely, or inferences (reading age, ability) drawn without transparency → intrusion, inaccurate profiling of a child | `[DPO]` | `[DPO]` | `[DPO]` | One-term retention unless safeguarding; access controls; transparency in the learner privacy notice; human judgement on any inference; no solely-automated decisions | `[DPO]` | `[DPO]` |
| 12 | Processing without an executed Google/Anthropic DPA or completed due diligence → no contractual processor safeguards | `[DPO]` | `[DPO]` | `[DPO]` | DPAs and due-diligence questionnaires to be completed pre-launch (consultancy templates); data minimisation to processors meanwhile | `[DPO]` | `[DPO]` |
| 13 | Privacy notice absent at launch → processing children's data without transparency (Art. 13/14, Children's Code) | `[DPO]` | `[DPO]` | `[DPO]` | Learner privacy notice drafted, published and consent gathered before any learner uses the platform | `[DPO]` | `[DPO]` |

## Decision, approval and documentation

**`[DPO TO COMPLETE]`** — Summary of the DPO's advice and whether it is being followed; any variation explained. Confirm residual risks are recorded in the Data Protection Risk Register, and that any residual high risk that cannot be reduced triggers prior consultation with the ICO under Article 36.

### Mitigation measures

`[DPO TO COMPLETE — owner, executor, completion date for each agreed mitigation; who keeps this DPIA under review; who records residual risk in the register.]`

### DPIA prepared by / Privacy Officer approval

| Field | Value |
|---|---|
| DPIA screening carried out by | `[name]` |
| Date of screening | `[date]` |
| Result of screening | Full DPIA required |
| DPIA prepared by | `[DPO — Director, NEO during initial period]` |
| DPO / Privacy Officer approval | `[name]` `[date]` |
| Proprietor noted (OEAS accountable person) | Diego Melo `[date]` |
| Company DPO / Information Security consulted | Brian Mair `[date]` |
| Review date | `[set — recommend annually and on material change]` |

---

## Companion / child DPIAs required (do not treat this master as discharging them)

Per *Setting up NEO* §15.3 and architecture §12, separate DPIAs / addenda are required for:

- Learner account provisioning.
- The filtering & monitoring tool selection (before learner onboarding).
- The Claude Developer Platform (agentic-platform authorisation — draft addendum already referenced).
- The intake / enrolment agent processing.
- Any Gemini for Workspace enablement.
- Any new third-party AI tool or any new placement type processing new data classes.

---

## Document control

| Field | Value |
|---|---|
| Owner | Data Protection Officer (function held by Director, NEO during initial period) |
| Status | draft — for DPO completion and sign-off |
| Version | 0.1-draft |
| Scope | NEO platform (whole) |
| Template | `dpia-form.md` (canonical Nudge Education DPIA Form) |
| Drafted from | neo-architecture repo; NEO Data Protection Policy v04.26; Data Protection & Information Security Policy Dec 2025 |
