# Example E — SaaS onboarding activation (PROPOSED_EXAMPLE)

Label: `PROPOSED_EXAMPLE` — an original blueprint for training and future implementation. Not observed in any source; source inspirations, where any, are named in the automation deep-dive.

## Flow
Tenant creation requested → plan/industry/country selected → validations (domain, tax format per country pack, admin email) → provisioning job (schema, seed roles, default chart/tax per country pack) → role invitations → setup checklist (company profile, fiscal year, first warehouse/branch, payment method) → feature enablement by plan → first-value milestone (first invoice / first order / first project) → incomplete-setup reminders on days 2/5/10 with the exact next step named.

## Controls
- Create Tenant
- Resend Invite
- Resume Setup
- Mark Step Complete (system)
- Nudge Admin

## Validations
Unique tenant slug; plan exists; country pack available or explicitly waived; admin email deliverable.

## State model
Requested -> Validating -> Provisioning -> Invited -> Setting Up -> Activated | Stalled (per reminder policy) | Failed (with retryable step named).

## Data entities
Tenant, Provisioning Job, Invitation, Setup Checklist Item, Activation Milestone

## Proposed API
`POST /v1/tenants; POST /v1/tenants/{id}/setup/nudge` (proposal only)

## Acceptance test (Given/When/Then)
Given a failed provisioning step, when an operator retries, then only the failed step re-runs (idempotent) and the tenant never sees a half-created workspace. Given no setup progress for 48h, then a reminder naming the exact incomplete step is sent.

## Failure paths (all examples)
Cancellation by the actor returns the object to its pre-submit state with an audit entry; duplicate submission is blocked by idempotency key; session expiry preserves the draft; a missing-permission actor never sees the action (and the API returns 403 if called directly); concurrent decisions resolve first-wins with the losing actor shown the winning decision.
