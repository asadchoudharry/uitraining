# Example D — Project overdue alert (PROPOSED_EXAMPLE)

Label: `PROPOSED_EXAMPLE` — an original blueprint for training and future implementation. Not observed in any source; source inspirations, where any, are named in the automation deep-dive.

## Flow
Milestone schedule variance detected (planned date passed, status not complete, or forecast slip > X days) → risk task created for the milestone owner → notification → if overdue beyond the escalation window, escalate to project sponsor → re-baseline requires sponsor approval → revised timeline is versioned with an audit trail.

## Controls
- Acknowledge
- Re-plan
- Request Re-baseline
- Approve Re-baseline

## Validations
Milestone has an owner and a planned date; variance computed against the current approved baseline only.

## State model
On Track -> At Risk -> Overdue -> Escalated -> Re-baselined (approved) | Completed Late.

## Data entities
Milestone, Baseline, Risk Task, Escalation, Audit Event

## Proposed API
`POST /v1/projects/{id}/milestones/{mid}/rebaseline-requests` (proposal only)

## Acceptance test (Given/When/Then)
Given a milestone 3 days overdue, when the daily job runs, then the owner has a risk task and the sponsor is notified per policy. Given an approved re-baseline, then variance resets against the new baseline and the old baseline remains readable.

## Failure paths (all examples)
Cancellation by the actor returns the object to its pre-submit state with an audit entry; duplicate submission is blocked by idempotency key; session expiry preserves the draft; a missing-permission actor never sees the action (and the API returns 403 if called directly); concurrent decisions resolve first-wins with the losing actor shown the winning decision.
