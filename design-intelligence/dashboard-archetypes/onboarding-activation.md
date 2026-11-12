# Archetype — Onboarding / activation dashboard (ORIGINAL wireframe spec)

- Primary user: Customer-success / product ops
- Decision question: *Where do new accounts stall in setup, and what unblocks them?*
- Status: original synthesis for UITraining; not a copy of any source screen.

## KPI set
- Activation rate by step
- Median time per step
- Stalled accounts (>48h)
- Invite acceptance %
- First-value milestone completions

## Layout recipe (1440px)
- Shell: sidebar 252px (collapses to 64px icons at <=1024px, drawer at <=768px), topbar 48px, content on the shared 24px gutter.
- Funnel by named setup steps (same names users see, S09 pattern); stalled-account table with last step + nudge action; per-step drop-off bars.
- Density: comfortable default; compact toggle for tables. Mobile (390px): KPI cards stack 1-up, queues remain first, charts become data tables on demand.

## Drill-down contract
- Stalled account -> setup state -> resend invite / assist action (audited).
- Every number on this archetype must have a destination list; a KPI without a drill-down is deleted, not decorated.

## States
- Loading: skeleton mirroring the layout. Empty: first-run checklist (setup-oriented) instead of a blank dashboard. Permission: modules the role cannot see are absent, not greyed. Error: per-panel retry, page stays usable.

## Evidence & pattern sources
- S09 (9 named steps, OBSERVED); S03 onboarding (6 steps, CODE_VERIFIED); S10 Fulcrum "Free Trial Activation" UIMG-030.
- Token/component references: `design-system/tokens/tokens.json`, `design-system/components/component-specifications.md` (KPI card, approval panel, table, badge).
