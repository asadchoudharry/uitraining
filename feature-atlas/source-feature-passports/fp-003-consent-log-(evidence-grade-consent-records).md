# Feature passport — Consent log (evidence-grade consent records) (FP-003)

- Evidence: **UI_VISIBLE_ONLY** · Module: Governance/Compliance · Priority: P1_HIGH_LEVERAGE · Target status: NOT_AUDITED
- Sources: S10 — case-studies/user-images/uimg-056-consent-log.md

## Observed behaviour
A searchable, exportable table of 48,920 consent records with summary strip (total, accepted 78%, rejected 13%, customised 9%), columns Consent ID / Date & Time / Country / Decision / Categories / Framework / IP (masked) / Device, framework values spanning GDPR, CCPA, LGPD, PIPEDA, APPI, Privacy Act; pagination to 5,436 pages; Export CSV action; filters for period, website, decision.

## Not verified
Collection mechanics, retention, proof-of-consent storage, deletion workflows.

## Business problem / users / jobs
Regulators and auditors require per-visitor consent evidence, not aggregate claims. Users: Compliance leads, DPOs. Jobs: Prove what a visitor consented to, when, under which framework; export evidence.

## Screens, actions, fields
Screens: UIMG-053, UIMG-055, UIMG-056. Actions: Search by ID/IP, filter, Export CSV, paginate. Inputs: Period, website, decision filters; search text. Outputs: Filtered records; CSV export.

## States & validations
States: Decision: Accepted / Rejected / Customised. Validations: IP masked in display (observed)

## Permissions, notifications, audit
Permissions: Compliance role implied; not verified. Notifications: None visible. Audit: The log itself is the audit artefact

## Data & proposed API
Entities: ConsentRecord {id, ts, country, decision, categories[], framework, ip_masked, device}. API (PROPOSED): PROPOSED: GET /v1/consent-records (cursor pagination, export job)

## Acceptance criteria
Given 48,920 records, when an auditor filters by framework=GDPR and exports, then a CSV job is created and the export contains only matching records with masked IPs.

## Test cases
Filter correctness per framework, Export completeness vs table count, IP masking in UI and export
