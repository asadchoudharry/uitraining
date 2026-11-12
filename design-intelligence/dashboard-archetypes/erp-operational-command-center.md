# Archetype — ERP operational command center (ORIGINAL wireframe spec)

- Primary user: Operations manager
- Decision question: *What needs action today across sales, purchase, stock and cash?*
- Status: original synthesis for UITraining; not a copy of any source screen.

## KPI set
- Open orders
- Deliveries due today
- Low-stock SKUs
- Payments due / overdue
- Approvals waiting

## Layout recipe (1440px)
- Shell: sidebar 252px (collapses to 64px icons at <=1024px, drawer at <=768px), topbar 48px, content on the shared 24px gutter.
- Action-queue first (approvals, exceptions), KPI strip second, module tiles with live counts third. No decorative charts above the queue.
- Density: comfortable default; compact toggle for tables. Mobile (390px): KPI cards stack 1-up, queues remain first, charts become data tables on demand.

## Drill-down contract
- Queue item -> document -> approval panel. Tile -> module list pre-filtered.
- Every number on this archetype must have a destination list; a KPI without a drill-down is deleted, not decorated.

## States
- Loading: skeleton mirroring the layout. Empty: first-run checklist (setup-oriented) instead of a blank dashboard. Permission: modules the role cannot see are absent, not greyed. Error: per-panel retry, page stays usable.

## Evidence & pattern sources
- S05 Dreams ERP module census (route inventory), S06 POS operations pages, E07 taxonomy section C.
- Token/component references: `design-system/tokens/tokens.json`, `design-system/components/component-specifications.md` (KPI card, approval panel, table, badge).
