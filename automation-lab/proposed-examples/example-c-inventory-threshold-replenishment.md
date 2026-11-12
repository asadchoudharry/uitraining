# Example C — Inventory threshold and replenishment (PROPOSED_EXAMPLE)

Label: `PROPOSED_EXAMPLE` — an original blueprint for training and future implementation. Not observed in any source; source inspirations, where any, are named in the automation deep-dive.

## Flow
Stock position (on hand - reserved) or days-of-cover falls below the SKU/warehouse threshold → condition check (not discontinued; no open duplicate suggestion in 7 days) → suggested purchase request with quantity = reorder target - available → inventory manager approval → supplier selection (preferred supplier default) → approved PO draft → receiving path links goods receipt + reconciliation.

## Controls
- Approve Suggestion
- Edit Quantity
- Change Supplier
- Dismiss with Reason

## Validations
Threshold > 0; supplier active; warehouse matches SKU stocking profile; multi-warehouse evaluated per warehouse, never netted silently.

## State model
Suggested -> Approved -> PO Draft Created | Dismissed (with reason, suppresses re-alert for the configured window).

## Data entities
Stock Position, Reorder Rule, Purchase Suggestion, PO Draft, Goods Receipt

## Proposed API
`POST /v1/inventory/suggestions/{id}/approve` (proposal only)

## Acceptance test (Given/When/Then)
Given cover < threshold in one warehouse only, when the job runs, then exactly one suggestion is created for that warehouse. Given a dismissed suggestion, then no duplicate is raised inside the suppression window.

## Failure paths (all examples)
Cancellation by the actor returns the object to its pre-submit state with an audit entry; duplicate submission is blocked by idempotency key; session expiry preserves the draft; a missing-permission actor never sees the action (and the API returns 403 if called directly); concurrent decisions resolve first-wins with the losing actor shown the winning decision.
