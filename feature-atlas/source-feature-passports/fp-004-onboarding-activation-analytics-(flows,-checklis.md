# Feature passport — Onboarding activation analytics (flows, checklists, tours, nudges) (FP-004)

- Evidence: **UI_VISIBLE_ONLY** · Module: Onboarding/Analytics · Priority: P1_HIGH_LEVERAGE · Target status: NOT_AUDITED
- Sources: S10 — case-studies/user-images/uimg-030-free-trial-activation.md

## Observed behaviour
Dashboard "Free Trial Activation": KPI Total 15,612 users activated (30d), Impact $780K revenue influenced (30d); progress chart; attribution table per intervention (Welcome flow Running 420 users 34.7% $12,493; Product tour Active 288 23.8% $6,742; Setup checklist Running 356 29.4% $9,180; Nudge: Invite team Active 147 12.1% $3,908); nav taxonomy REVIEW/ONBOARDING/AUDIENCE (Goals, Reports, Flows, Checklists, Product tours, Nudges, Message library, Users, Segments); an AI agent panel with artefact-creation prompt chips.

## Not verified
Attribution methodology, event pipeline, whether revenue figures are modelled or actual.

## Business problem / users / jobs
Teams cannot see which onboarding intervention actually activates users. Users: Product ops, customer success. Jobs: Measure activation per intervention; iterate on the weakest step.

## Screens, actions, fields
Screens: UIMG-030. Actions: Inspect per-flow attribution; create flows/checklists/tours/nudges/segments (via agent chips or nav). Inputs: Flow definitions, checklist steps, segment rules. Outputs: Activation %, attributed revenue, per-flow status.

## States & validations
States: Intervention status: Running / Active (semantics to verify before reuse). Validations: None visible

## Permissions, notifications, audit
Permissions: Workspace admin implied. Notifications: None visible. Audit: None visible

## Data & proposed API
Entities: Flow, Checklist, Tour, Nudge, Segment, ActivationEvent, Attribution. API (PROPOSED): PROPOSED: GET /v1/activation/summary; GET /v1/activation/flows

## Acceptance criteria
Given two running flows, when their windows overlap, then the attribution model used is displayed next to the revenue figure.

## Test cases
KPI totals reconcile with the attribution table, Dark/light parity of the same screen, Status vocabulary consistency
