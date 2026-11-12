# Archetype — Executive KPI dashboard (ORIGINAL wireframe spec)

- Primary user: Owner / C-suite
- Decision question: *Is the business healthy this period, and where is it drifting?*
- Status: original synthesis for UITraining; not a copy of any source screen.

## KPI set
- Revenue (period, vs target)
- Gross margin %
- Cash position
- Active customers/tenants
- Churn or overdue %

## Layout recipe (1440px)
- Shell: sidebar 252px (collapses to 64px icons at <=1024px, drawer at <=768px), topbar 48px, content on the shared 24px gutter.
- 4 KPI cards max; one trend line (revenue vs target); one composition (revenue by segment); exception list (top 5 variances) instead of a second chart row.
- Density: comfortable default; compact toggle for tables. Mobile (390px): KPI cards stack 1-up, queues remain first, charts become data tables on demand.

## Drill-down contract
- KPI -> segment trend -> entity list (filtered). Exceptions -> operational queue.
- Every number on this archetype must have a destination list; a KPI without a drill-down is deleted, not decorated.

## States
- Loading: skeleton mirroring the layout. Empty: first-run checklist (setup-oriented) instead of a blank dashboard. Permission: modules the role cannot see are absent, not greyed. Error: per-panel retry, page stays usable.

## Evidence & pattern sources
- S10 corpus (29 dashboards: KPI-row pattern and its overuse), S01 executive dashboard shots (titles/tags level), S02 LedgerOS/Atlas case narratives.
- Token/component references: `design-system/tokens/tokens.json`, `design-system/components/component-specifications.md` (KPI card, approval panel, table, badge).
