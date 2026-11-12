# PROPOSED journey — company setup (label: PROPOSED, not observed)

Basis: S09's *visible* 9-step rail (Company Info → Verify Bank Account → Select a Plan → Billing Info → Cost Savings → Features → Notifications → QuickBooks Online → Invite Your Team) and S03's code-verified 6-step workspace onboarding. Everything below is an original functional specification; the source shot demonstrates none of the behaviour.

## Journey contract
`ACTOR (owner/admin) → TRIGGER (account created) → ENTRY (setup rail, step 1) → PRECONDITIONS (authenticated, no company yet) → INPUTS (per step below) → VALIDATION (per field) → AUTHORIZATION (owner only; steps 3–4 also visible to a billing role) → UI TRANSITION (rail advances, completed steps get checks) → BUSINESS STATE (company record progressively committed; each step saves independently) → SIDE EFFECTS (bank verification micro-flow, plan subscription, integration connection, invitations) → SUCCESS (dashboard handoff with first-value checklist) / FAILURE (step-level error, state preserved) → AUDIT (every step completion + change logged) → NEXT ROUTE (dashboard).`

## Steps
1. **Company Info** — business type (select), legal name, address (with clear/edit), business email. Validation: name required; email format; address country drives step 2/4 formats. Observed in artwork.
2. **Verify Bank Account** — account holder, IBAN/account+routing by country, verification method (micro-deposit or instant verification provider). States: pending/verified/failed with retry; setup may continue while pending, payouts stay blocked (stated in UI).
3. **Select a Plan** — plan cards with per-plan limits; trial default where offered; changing plan later must not restart setup.
4. **Billing Info** — payment method, billing address, tax ID (validated per country pack); failure keeps the step editable, never deletes prior steps.
5. **Cost Savings** — value-proof step: with the business's expected volume, show the computed saving vs the stated baseline (the artwork's product claims $0 processing fees; an enterprise implementation must compute from real rates and label estimates as estimates).
6. **Features** — feature toggles grouped by module; defaults from business type (step 1); each toggle explains its data consequence in one line.
7. **Notifications** — channel matrix (email/SMS/in-app × event types), with a test-send action.
8. **QuickBooks Online** — OAuth connect (connect / connected-as / disconnect / reconnect-on-expiry states); a "skip — connect later in Settings" path that leaves a dashboard checklist item.
9. **Invite Your Team** — email rows with role select (Admin/Manager/Staff/View-only), bulk paste, per-invite status (sent/accepted/expired), resend; skippable.

## Branches & recovery (required by spec E04)
- Back navigation never loses saved steps; Cancel/Exit asks only when the current step is dirty.
- Partial save: each step commits on Continue; resuming lands on the first incomplete step with prior data intact.
- Duplicate submission: Continue is idempotent per step (submission token).
- Session expiry mid-setup: re-auth returns to the same step.
- Network loss: offline banner + retry; no silent failure.
- Missing permission (invited non-owner opens setup link): read-only progress view + "ask the owner" state.
- Concurrent edit (two admins): step-level lock notice with who/when; last-writer never silently overwrites financial steps (2, 4).
- Completion definition: steps 1–4 complete + at least one of {8 connected, 9 first invite sent} OR an explicit "finish later" — the dashboard then carries a persistent setup checklist until 100%.
