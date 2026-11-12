# Example A — Purchase order maker-checker (PROPOSED_EXAMPLE)

Label: `PROPOSED_EXAMPLE` — an original blueprint for training and future implementation. Not observed in any source; source inspirations, where any, are named in the automation deep-dive.

## Flow
Buyer raises a requisition → PO draft. On submit: budget/limit verification (cost centre budget remaining >= PO total; buyer limit check) → routing by amount (<= threshold T1: Procurement Manager; <= T2: + Finance Controller; > T2: + Director) → document completeness check (supplier bank details, tax registration, at least one line with price) → decisions → PO status becomes Approved → supplier notification is sent only after authorisation → audit trail entry per transition.

## Controls
- Submit
- Save Draft
- Edit Lines
- Attach Document
- Cancel

## Validations
Supplier required; >=1 line; amount > 0; currency + cost centre required; attachments required above T2.

## State model
Draft -> Pending -> Approved | Rejected | Returned for Revision. Material edit after submit (amount/lines/supplier change) voids approvals and returns to Draft with reason.

## Data entities
PO, PO Line, Approval Request, Approval Decision, Budget Reservation, Audit Event

## Proposed API
`POST /v1/purchase-orders/{id}/submit-approval; POST /v1/approval-tasks/{id}/decide` (proposal only)

## Acceptance test (Given/When/Then)
Given a valid PO above T1, when the buyer submits, then two approval stages are created in order and the buyer cannot approve any stage (self-approval blocked). Given a rejection with reason, then the PO returns to Draft and the reason is visible in the timeline.

## Failure paths (all examples)
Cancellation by the actor returns the object to its pre-submit state with an audit entry; duplicate submission is blocked by idempotency key; session expiry preserves the draft; a missing-permission actor never sees the action (and the API returns 403 if called directly); concurrent decisions resolve first-wins with the losing actor shown the winning decision.
