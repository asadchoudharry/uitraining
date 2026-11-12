# Archetype — CRM / sales funnel dashboard (ORIGINAL wireframe spec)

- Primary user: Sales lead
- Decision question: *Where is pipeline stuck and who needs follow-up today?*
- Status: original synthesis for UITraining; not a copy of any source screen.

## KPI set
- Pipeline value by stage
- Win rate
- Activities due
- Deals at risk (no activity N days)
- Forecast vs quota

## Layout recipe (1440px)
- Shell: sidebar 252px (collapses to 64px icons at <=1024px, drawer at <=768px), topbar 48px, content on the shared 24px gutter.
- Kanban funnel summary (stage columns with value + count), at-risk list, activity timeline. Deal cards carry stage/amount/close date always visible (S02 CloseCRM pattern).
- Density: comfortable default; compact toggle for tables. Mobile (390px): KPI cards stack 1-up, queues remain first, charts become data tables on demand.

## Drill-down contract
- Stage -> deal list -> deal detail with activity composer.
- Every number on this archetype must have a destination list; a KPI without a drill-down is deleted, not decorated.

## States
- Loading: skeleton mirroring the layout. Empty: first-run checklist (setup-oriented) instead of a blank dashboard. Permission: modules the role cannot see are absent, not greyed. Error: per-panel retry, page stays usable.

## Evidence & pattern sources
- S02 CloseCRM case study; S07/S08 CRM-tagged shots (title level); S10 BizLink/Cliento CRM screens UIMG-047/UIMG-054.
- Token/component references: `design-system/tokens/tokens.json`, `design-system/components/component-specifications.md` (KPI card, approval panel, table, badge).
