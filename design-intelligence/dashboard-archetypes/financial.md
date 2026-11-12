# Archetype — Financial dashboard (ORIGINAL wireframe spec)

- Primary user: Finance controller
- Decision question: *Are receivables, payables and cash under control?*
- Status: original synthesis for UITraining; not a copy of any source screen.

## KPI set
- Receivables aging total
- Payables due 7d
- Bank balance (all accounts)
- Expenses MTD vs budget
- Unreconciled items

## Layout recipe (1440px)
- Shell: sidebar 252px (collapses to 64px icons at <=1024px, drawer at <=768px), topbar 48px, content on the shared 24px gutter.
- Aging buckets as stacked bar + table hybrid; cash runway line; reconciliation exception list. Amounts tabular, right-aligned, exportable.
- Density: comfortable default; compact toggle for tables. Mobile (390px): KPI cards stack 1-up, queues remain first, charts become data tables on demand.

## Drill-down contract
- Bucket -> invoice list -> invoice; unreconciled -> matching screen.
- Every number on this archetype must have a destination list; a KPI without a drill-down is deleted, not decorated.

## States
- Loading: skeleton mirroring the layout. Empty: first-run checklist (setup-oriented) instead of a blank dashboard. Permission: modules the role cannot see are absent, not greyed. Error: per-panel retry, page stays usable.

## Evidence & pattern sources
- S10 fintrack/Leel.Data/OripioFin screens (UIMG-023/033/045); S01 finance dashboard series (title level); S03 token discipline for money display.
- Token/component references: `design-system/tokens/tokens.json`, `design-system/components/component-specifications.md` (KPI card, approval panel, table, badge).
