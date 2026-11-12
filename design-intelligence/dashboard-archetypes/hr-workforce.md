# Archetype — HR / workforce dashboard (ORIGINAL wireframe spec)

- Primary user: HR manager
- Decision question: *Who is absent, pending approval, or at risk in the workforce today?*
- Status: original synthesis for UITraining; not a copy of any source screen.

## KPI set
- Headcount by department
- Attendance today %
- Leave requests pending
- Open positions
- Payroll exceptions

## Layout recipe (1440px)
- Shell: sidebar 252px (collapses to 64px icons at <=1024px, drawer at <=768px), topbar 48px, content on the shared 24px gutter.
- Attendance strip; approvals queue (leave/overtime); department table; hiring funnel mini-kanban.
- Density: comfortable default; compact toggle for tables. Mobile (390px): KPI cards stack 1-up, queues remain first, charts become data tables on demand.

## Drill-down contract
- Request -> approval panel; employee -> profile.
- Every number on this archetype must have a destination list; a KPI without a drill-down is deleted, not decorated.

## States
- Loading: skeleton mirroring the layout. Empty: first-run checklist (setup-oriented) instead of a blank dashboard. Permission: modules the role cannot see are absent, not greyed. Error: per-panel retry, page stays usable.

## Evidence & pattern sources
- S05 HRM module census; S08 HR Management dashboard shots (title level); S10 hospital/team dashboards as adjacent evidence.
- Token/component references: `design-system/tokens/tokens.json`, `design-system/components/component-specifications.md` (KPI card, approval panel, table, badge).
