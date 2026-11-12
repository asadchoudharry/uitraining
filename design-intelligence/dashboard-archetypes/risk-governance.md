# Archetype — Risk & governance dashboard (ORIGINAL wireframe spec)

- Primary user: Compliance lead
- Decision question: *What is overdue, unapproved or out of policy right now?*
- Status: original synthesis for UITraining; not a copy of any source screen.

## KPI set
- Open findings by severity
- Overdue remediations
- Policy exceptions
- Audit evidence completeness %
- Access reviews due

## Layout recipe (1440px)
- Shell: sidebar 252px (collapses to 64px icons at <=1024px, drawer at <=768px), topbar 48px, content on the shared 24px gutter.
- Severity-ordered queues; evidence completeness by control; aging chart. Every number drills to an evidence list — no orphan metrics.
- Density: comfortable default; compact toggle for tables. Mobile (390px): KPI cards stack 1-up, queues remain first, charts become data tables on demand.

## Drill-down contract
- Finding -> remediation workflow -> evidence upload/attestation.
- Every number on this archetype must have a destination list; a KPI without a drill-down is deleted, not decorated.

## States
- Loading: skeleton mirroring the layout. Empty: first-run checklist (setup-oriented) instead of a blank dashboard. Permission: modules the role cannot see are absent, not greyed. Error: per-panel retry, page stays usable.

## Evidence & pattern sources
- S02 LedgerOS/Relay governance narratives; S10 consently.io suite UIMG-053/055/056 (consent log as governance evidence pattern).
- Token/component references: `design-system/tokens/tokens.json`, `design-system/components/component-specifications.md` (KPI card, approval panel, table, badge).
