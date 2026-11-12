# FDD — Company setup + activation analytics (P1)

- Capability: a named-step company setup (S09 pattern) instrumented end-to-end so product/CS teams see per-step activation and stalled accounts (FP-004 pattern).
- Source basis: S09 (UI_VISIBLE_ONLY rail), S03 onboarding (CODE_VERIFIED UI), S10 Fulcrum (UI_VISIBLE_ONLY analytics). No source demonstrates the instrumentation itself — the analytics contract here is NEW_PROPOSAL.

## Product decision
Setup abandonment is invisible in most SaaS admin tools; teams learn about it at churn. Personas: new tenant owner (completes setup), CS operator (unblocks), product ops (improves steps). Value hypothesis: naming the exact incomplete step in reminders lifts completion more than generic nudges.

## Screens & UX
Tenant-side: setup rail + step screens per `interaction-atlas/user-journeys/s09-company-setup-proposed.md`; persistent dashboard checklist until complete. Operator-side: activation dashboard (archetype `onboarding-activation`): funnel by step name, median time per step, stalled table (>48h) with step + nudge action, invite acceptance rate.

## Flow & data
Every step emits `setup.step.viewed/completed/skipped` + `setup.completed`, `invite.sent/accepted`, `first_value.achieved` with tenant + step + timestamp + actor role. Entities: Tenant, SetupState {tenant_id, step, status, updated_at}, SetupEvent, Invitation, Milestone. Invariant: funnel order is the rail order; a tenant's current step = first incomplete required step.

## API (PROPOSED)
`GET /v1/activation/funnel?period=`, `GET /v1/activation/stalled`, `POST /v1/tenants/{id}/setup/nudge {template}` (audited, rate-limited per tenant).

## Security & quality
Operator nudges are audit-logged; no operator can edit tenant setup data from the analytics side (assist actions are separate, permissioned and logged). Acceptance: Given a tenant idle 48h at step "Verify Bank Account", when the daily job runs, then the stalled list shows that step name and a nudge is available; Given a completed tenant, then it never appears in stalled lists. A11y: rail is a real list with aria-current; analytics charts ship data tables.
