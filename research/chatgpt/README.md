# UITRAINING / ChatGPT research workstream

> **Destination:** main branch, under research/chatgpt only. Muse data remains in its separate tree. This index is the authoritative entrypoint for the ChatGPT contribution, not a claim that every source screen has been verified.

## Open the research interface

- [Standalone Design Explorer (HTML)](design-explorer/index.html) — source/feature/route tabs, search, source filters, theme and filtered JSON export. Download the raw HTML to use offline if GitHub does not render it as an application.
- [Native editable Figma workspace](https://www.figma.com/design/6ilnXLVvHo81h7QIAW5AAw) — 20 variable definitions, two component definitions and one editable approval screen.

## Authoritative requirements and evidence

- [Original UITRAINING v2 mission](specifications/UITRAINING_MASTER_EXECUTION_PROMPT_v2.md)
- [Source registry](source-registry.json) — S01–S10, status, redistribution gates and provenance.
- [Indexed route registry](source-route-graphs/discovered-routes-2026-11-12.jsonl) — 131 unique entries, indexed only.
- [Source count snapshot](status/discovery-counts-2026-11-12.csv) — indexed totals, partial discovery.
- [Feature master inventory JSONL](feature-atlas/feature-master-inventory.jsonl) / [CSV](feature-atlas/feature-master-inventory.csv) — 71 evidence-graded features.
- [Feature JSON schema](feature-atlas/schema.json)

## Case-study library (not exhaustive)

- [S02 — Relay agent approval](case-studies/S02_relay-human-approved-agent-operations.md)
- [S03 — GR8R codebase research](case-studies/S03_GR8R_STUDIO_SOURCE_AUDIT.md)
- [S04 — Construction operations](case-studies/S04_construction-operational-control.md)
- [S05 — Document workflows](case-studies/S05_dreams-erp-document-workflow.md)
- [S06 — Retail POS](case-studies/S06_dreamspos-retail-operations.md)
- [S09 — Static onboarding design](case-studies/S09_onboarding-company-setup.md)

## Implementation-ready original workflow specifications

- [WFL-001 — Document approval](interaction-atlas/workflow-specifications/WFL-001-role-scoped-document-approval.md)
- [WFL-002 — Multi-country tenant onboarding](interaction-atlas/workflow-specifications/WFL-002-multi-country-tenant-onboarding-and-provisioning.md)
- [WFL-003 — Retail POS sale and payment](interaction-atlas/workflow-specifications/WFL-003-retail-pos-sale-payment-and-stock-posting.md)
- [WFL-004 — Construction inspection/CAPA](interaction-atlas/workflow-specifications/WFL-004-construction-inspection-to-corrective-action-closure.md)
- [Automation engine proposal](automation-lab/workflow-engine-proposed-spec.md)

## Original design infrastructure

- [Semantic token JSON](reusable-ui/original-semantic-tokens/tokens.json) / [CSS](reusable-ui/original-semantic-tokens/tokens.css)
- [Native editable Figma handoff](reusable-ui/figma-handoff/UITRAINING-native-editable-design.md)
- [Future product roadmap](future-product-blueprints/phased-roadmap.md)
- [Enterprise Skill improvement proposals](reports/skills-improvement-recommendations.md)

## QA and rights

- [13 passing corpus integrity checks](quality/evidence-audit/2026-11-12-integrity-check.md)
- [QA and release gate status](quality/evidence-audit/qa-and-release-matrix.md)
- [Source media/redistribution ledger](quality/rights-review/asset-and-licensing-ledger.md)
- [Current execution report](reports/execution-report-2026-11-12.md)
- [Previous recovery checkpoint](status/CHECKPOINT_2026-11-12.md)

## Evidence-state contract

**Discovered ≠ verified.** All indexed route entries remain DOCUMENTED_ONLY until direct screen and interaction evidence is added. Source-coded GR8R behaviors are SOURCE_IMPLEMENTED but not necessarily a server application. Feature proposals remain PROPOSED; no target product capability has been established missing without a baseline audit.

**Rights:** research links and original artifacts are published; unlicensed third-party screenshots, font binaries, templates and source code are not.

**Resume point:** inspect full route/action/state census, verify source licensing and review future screenshot upload batches. Do not overwrite work by other agents.
