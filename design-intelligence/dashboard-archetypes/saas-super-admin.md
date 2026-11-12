# Archetype — SaaS super-admin dashboard (ORIGINAL wireframe spec)

- Primary user: Platform operator
- Decision question: *Is the platform healthy and which tenants need intervention?*
- Status: original synthesis for UITraining; not a copy of any source screen.

## KPI set
- Active tenants
- MRR / trials expiring
- Failed jobs (24h)
- Provisioning queue
- Support escalations

## Layout recipe (1440px)
- Shell: sidebar 252px (collapses to 64px icons at <=1024px, drawer at <=768px), topbar 48px, content on the shared 24px gutter.
- Tenant table with plan/status/health; job failure list with retry; provisioning stepper states. Dangerous actions gated + audited.
- Density: comfortable default; compact toggle for tables. Mobile (390px): KPI cards stack 1-up, queues remain first, charts become data tables on demand.

## Drill-down contract
- Tenant -> tenant detail -> impersonation (audited) or plan change.
- Every number on this archetype must have a destination list; a KPI without a drill-down is deleted, not decorated.

## States
- Loading: skeleton mirroring the layout. Empty: first-run checklist (setup-oriented) instead of a blank dashboard. Permission: modules the role cannot see are absent, not greyed. Error: per-panel retry, page stays usable.

## Evidence & pattern sources
- S06 super-admin pages census; S10 Fulcrum activation analytics UIMG-030 (trial activation as a first-class metric).
- Token/component references: `design-system/tokens/tokens.json`, `design-system/components/component-specifications.md` (KPI card, approval panel, table, badge).
