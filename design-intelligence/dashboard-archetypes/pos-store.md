# Archetype — POS / store dashboard (ORIGINAL wireframe spec)

- Primary user: Store manager
- Decision question: *How is each register/store performing and what stock needs attention?*
- Status: original synthesis for UITraining; not a copy of any source screen.

## KPI set
- Sales today by register
- Returns
- Low/expired stock count
- Drawer variances
- Top categories

## Layout recipe (1440px)
- Shell: sidebar 252px (collapses to 64px icons at <=1024px, drawer at <=768px), topbar 48px, content on the shared 24px gutter.
- Register cards with live totals; stock alert table; hourly sales bars. Density high, touch targets >=44px for POS-adjacent screens.
- Density: comfortable default; compact toggle for tables. Mobile (390px): KPI cards stack 1-up, queues remain first, charts become data tables on demand.

## Drill-down contract
- Register -> session detail -> Z-report; alert -> product -> adjustment.
- Every number on this archetype must have a destination list; a KPI without a drill-down is deleted, not decorated.

## States
- Loading: skeleton mirroring the layout. Empty: first-run checklist (setup-oriented) instead of a blank dashboard. Permission: modules the role cannot see are absent, not greyed. Error: per-panel retry, page stays usable.

## Evidence & pattern sources
- S06 Dreams POS route census incl. POS variants and stock pages (route inventory evidence).
- Token/component references: `design-system/tokens/tokens.json`, `design-system/components/component-specifications.md` (KPI card, approval panel, table, badge).
