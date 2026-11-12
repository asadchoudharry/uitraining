# Feature passport — POS terminal variants (layout family) (FP-005)

- Evidence: **UI_VISIBLE_ONLY** · Module: POS · Priority: P2_DOMAIN_PACK · Target status: NOT_AUDITED
- Sources: S06 — https://dreamspos.dreamstechnologies.com/retail-pos/html/pos.html

## Observed behaviour
The retail POS demo links distinct terminal pages pos.html and pos-2.html … pos-5.html from its index (252 unique links site-wide); further variants/pagination are enumerated in the route census (research/site-maps/). Sibling vertical demos (restaurant, pharmacy, laundry) are linked from the same index but are separate products, recorded as outbound references.

## Not verified
Checkout behaviour, payment/hardware integration, offline behaviour — template pages demonstrate layout, not processing.

## Business problem / users / jobs
Different retail formats need different terminal layouts (grid density, cart position, category navigation). Users: Cashiers, store managers. Jobs: Run a sale quickly by touch or keyboard; park/resume; refund; close the shift.

## Screens, actions, fields
Screens: pos.html … pos-5.html. Actions: Variant-specific (see interaction comparison in the S06 case study). Inputs: Product search/scan, quantity, discount, tax, tender. Outputs: Receipt, totals, drawer events.

## States & validations
States: Sale: open / parked / completed / refunded (proposed semantics). Validations: None verified

## Permissions, notifications, audit
Permissions: Cashier role + shift implied. Notifications: None demonstrated. Audit: End-of-day reconciliation implied by reports routes (audit)

## Data & proposed API
Entities: Sale, SaleLine, Payment, Shift, DrawerEvent. API (PROPOSED): PROPOSED: /v1/pos/sales with idempotent posting

## Acceptance criteria
Given a parked sale, when the cashier resumes it on another register, then totals and lines are identical.

## Test cases
Variant layout comparison checklist (E09), Park/resume, Refund with authorisation
