# Archetype — Project / task dashboard (ORIGINAL wireframe spec)

- Primary user: Delivery lead
- Decision question: *What is late, blocked or unassigned across projects?*
- Status: original synthesis for UITraining; not a copy of any source screen.

## KPI set
- Overdue tasks
- Milestones at risk
- Workload by member
- Blocked items
- Completion % by project

## Layout recipe (1440px)
- Shell: sidebar 252px (collapses to 64px icons at <=1024px, drawer at <=768px), topbar 48px, content on the shared 24px gutter.
- Portfolio list with health badges; my-work panel; workload bars. Five interchangeable views (board/list/table/calendar/timeline) over one dataset (S03 CODE_VERIFIED pattern).
- Density: comfortable default; compact toggle for tables. Mobile (390px): KPI cards stack 1-up, queues remain first, charts become data tables on demand.

## Drill-down contract
- Project -> view of choice -> task drawer.
- Every number on this archetype must have a destination list; a KPI without a drill-down is deleted, not decorated.

## States
- Loading: skeleton mirroring the layout. Empty: first-run checklist (setup-oriented) instead of a blank dashboard. Permission: modules the role cannot see are absent, not greyed. Error: per-panel retry, page stays usable.

## Evidence & pattern sources
- S03 (code-verified views + drawer + saved views); S02 Task Management case; S10 panze/JYSigma project dashboards UIMG-024/UIMG-049.
- Token/component references: `design-system/tokens/tokens.json`, `design-system/components/component-specifications.md` (KPI card, approval panel, table, badge).
