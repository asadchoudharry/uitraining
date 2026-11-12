# Archetype — Construction / site delivery dashboard (ORIGINAL wireframe spec)

- Primary user: Project director
- Decision question: *Which sites are behind plan, over budget or blocked on safety/materials?*
- Status: original synthesis for UITraining; not a copy of any source screen.

## KPI set
- Planned vs actual progress %
- Budget utilisation
- Open RFIs/submittals
- HSE incidents (period)
- Material shortages

## Layout recipe (1440px)
- Shell: sidebar 252px (collapses to 64px icons at <=1024px, drawer at <=768px), topbar 48px, content on the shared 24px gutter.
- Portfolio table of sites with variance badges; selected-site panel: phase progress bars, alert queue (approvals, shortages, inspections). Map optional, never the only view.
- Density: comfortable default; compact toggle for tables. Mobile (390px): KPI cards stack 1-up, queues remain first, charts become data tables on demand.

## Drill-down contract
- Site -> phase/task detail -> approval or site report.
- Every number on this archetype must have a destination list; a KPI without a drill-down is deleted, not decorated.

## States
- Loading: skeleton mirroring the layout. Empty: first-run checklist (setup-oriented) instead of a blank dashboard. Permission: modules the role cannot see are absent, not greyed. Error: per-panel retry, page stays usable.

## Evidence & pattern sources
- S04 Construction ERP route census + module analysis (site-maps + case study).
- Token/component references: `design-system/tokens/tokens.json`, `design-system/components/component-specifications.md` (KPI card, approval panel, table, badge).
