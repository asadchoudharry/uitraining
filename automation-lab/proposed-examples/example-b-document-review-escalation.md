# Example B — Document review and escalation (PROPOSED_EXAMPLE)

Label: `PROPOSED_EXAMPLE` — an original blueprint for training and future implementation. Not observed in any source; source inspirations, where any, are named in the automation deep-dive.

## Flow
Draft document assigned to reviewers in levels → due-date tracking per level → reminder at 50% and 90% of SLA → escalation to the level owner's manager after breach → approve / reject / return-for-revision → final state with a signed, versioned audit evidence pack.

## Controls
- Assign Reviewers
- Set Due Date
- Approve
- Reject
- Return for Revision
- Download Evidence Pack

## Validations
At least one reviewer per level; due date in the future (tenant calendar); document not locked by another editor.

## State model
Draft -> In Review (per-level pending) -> Approved | Rejected | Returned. SLA states: On Track -> At Risk -> Breached -> Escalated.

## Data entities
Document, Document Version, Review Assignment, Decision, SLA Clock, Audit Event

## Proposed API
`POST /v1/documents/{id}/reviews; POST /v1/reviews/{id}/decide` (proposal only)

## Acceptance test (Given/When/Then)
Given a review due in 24h, when 12h pass without a decision, then a reminder is sent once; when 24h pass, then escalation fires and the breach is recorded. Given all levels approve, then the document locks and the evidence pack is generated.

## Failure paths (all examples)
Cancellation by the actor returns the object to its pre-submit state with an audit entry; duplicate submission is blocked by idempotency key; session expiry preserves the draft; a missing-permission actor never sees the action (and the API returns 403 if called directly); concurrent decisions resolve first-wins with the losing actor shown the winning decision.
