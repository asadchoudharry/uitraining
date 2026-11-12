# WFL-003 — Retail POS sale, payment and stock posting

**Classification:** original implementation-ready proposal, not observed third-party backend behavior.
**Source pattern references:** S06 / pos.html / FEAT-0055; S06 / barcode.html / FEAT-0058
**Actors:** Cashier, Shift Supervisor, Store Manager, Finance Auditor
**User goal:** Convert a cart into a reconciled receipt without duplicate payment or inventory posting.
**Entry:** Retail > POS > Open shift > New sale

## Screen-by-screen specification
| Screen ID | Name | Visible controls and content | Mandatory non-happy-path states |
| --- | --- | --- | --- |
| SCR-201 | Shift opening | Assigned register, store, cash float, permissions | loading, empty, filtered-empty, denied, stale, error, success |
| SCR-202 | Checkout | Barcode search, cart, customer, taxes, discounts | loading, empty, filtered-empty, denied, stale, error, success |
| SCR-203 | Discount override | Supervisor authorization and amount/percentage guard | loading, empty, filtered-empty, denied, stale, error, success |
| SCR-204 | Payment modal | Tender type, authorization, split and due amount | loading, empty, filtered-empty, denied, stale, error, success |
| SCR-205 | Receipt | Issue, print, email with separate consent, correction actions | loading, empty, filtered-empty, denied, stale, error, success |
| SCR-206 | Sales return | Original receipt lookup, eligibility, supervisor approval | loading, empty, filtered-empty, denied, stale, error, success |
| SCR-207 | Shift reconciliation | Cash count, variance, card settlement and lock | loading, empty, filtered-empty, denied, stale, error, success |

## Interaction contracts
| Action ID | Control | Actor | Authorization and validation | On success | Error recovery |
| --- | --- | --- | --- | --- | --- |
| ACT-201 | Scan item | Cashier | Valid SKU, price and available stock policy | cart updated | unknown SKU / negative stock guard |
| ACT-202 | Apply discount | Cashier or Supervisor | Within threshold or approved override | price recomputed | 403 override denied |
| ACT-203 | Commit payment | Cashier | Tender valid, totals stable, idempotency key | payment pending/confirmed | uncertain processor result; no retry blindly |
| ACT-204 | Post sale | System | Confirmed authorized tender and stock constraints | receipt and ledgers posted | compensating event on partial failure |
| ACT-205 | Return | Supervisor | Receipt item quantity not already returned | return request then credit | 409 returned amount conflict |
| ACT-206 | Close shift | Supervisor | Reconciled cash, supervisor attestation | locked shift report | unposted payment blocks close |

## State graph
SHIFT_CLOSED → SHIFT_OPEN → CART_OPEN → PAYMENT_PENDING → PAYMENT_UNCERTAIN → PAID → POSTED → VOIDED → RETURN_PENDING → RETURNED (the actual branches and guards are defined in implementation tests; arrows are not all permitted transitions).

## Proposed data model
RegisterShift, Sale, SaleLine, PriceList, TaxSnapshot, PaymentAttempt, Receipt, InventoryLedger, CashMovement, Return, AuditEvent

## Proposed endpoints
- POST /api/v1/retail/shifts
- POST /api/v1/retail/carts
- POST /api/v1/retail/payments/authorize
- POST /api/v1/retail/sales/commit
- POST /api/v1/retail/returns
- POST /api/v1/retail/shifts/{id}/close

## Permission and consistency rules
- Every object is tenant-scoped; server-side authorization is mandatory on read and write, independent of frontend affordances.
- High-risk writes require idempotency keys, optimistic concurrency and an append-only audit event.
- Unknown external outcomes require reconciliation, not blind retry.
- Unauthorized state must be explicit; disabled buttons do not imply secure authorization.
- Every error preserves unsaved context and provides a user-visible retry or remediation path.

## Acceptance test dossier
1. Duplicate payment submission never charges twice
2. Stock decremented once and only for posted sale
3. Refund cannot exceed original paid quantity/amount
4. Unknown payment state blocks blind duplicate processor retry
5. Cashier cannot issue unauthorized discount
6. Offline capture displays unposted warning and bounded queue

## Scope and caveats
This proposed contract is not claimed to exist in DreamsPOS static HTML.
- Implementation status: SPECIFIED only. Figma-linked reference screen covers a generic approval UI, not all these specific workflow screens.
- Tests are acceptance proposals; not executed backend checks.
