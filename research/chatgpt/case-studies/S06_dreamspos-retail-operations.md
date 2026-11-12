# DreamsPOS — Retail selling and inventory navigation

- Source ID: S06
- Canonical reference: https://dreamspos.dreamstechnologies.com/retail-pos/html/index.html
- Source type: FRONTEND_TEMPLATE
- Coverage: INDEXED_42_ROUTES_PARTIAL
- Inspected date: 2026-11-12
- Rights: REFERENCE_ONLY; no source screenshots, media or template code redistributed
- Runtime browser/cross-device testing: NOT_EXECUTED

## Scope and provenance
Indexed: POS, barcode printing, stock transfers, sales reports, invoices, coupons, employees, shift and more.

## Layout geometry and visual evidence
Retail dashboard and module menu visibly group sales, purchasing, inventory and business operations; no measured control geometry.

## Typography
Not computed or calibrated.

## Color / elevation
Do not reuse vendor template artwork, images or commercial CSS.

## Component inventory
POS billing entry, barcode-print view, inventory product register, store list, stock transfers, quotations, sales returns, finance reports and admin settings.

## On-screen functional chain and uncertainty
Barcode scan/cart -> line validation/discount/tax -> payment authorization -> receipt -> stock and ledger posting is PROPOSED for a production POS; front-end template does not prove that chain.

## Interaction census
| ID | Entry/control | Expected transition | Evidence |
| --- | --- | --- | --- |
| A01 | Open POS | Checkout screen route | Route indexed, transaction not tested |
| A02 | Print barcode | Label output action | Screen indexed, physical printing untested |
| A03 | Create transfer | Stock movement UI | Link indexed, inventory posting unverified |

## UX critique and original adaptation
**Observed value:** Centralized quick creation and broad operational module discovery.

**Risk and evidence gaps:** Retail cash, returns, taxes, refunds and stock writes require real transaction guarantees not established by static HTML.

**Transferability:** ADOPT_AS_PRINCIPLE: compact responsive checkout surface and direct task entry. IMPROVE: offline queues, reconciliation, permissions, fail-safe payment states.

## Cross references
- Feature IDs: FEAT-0055, FEAT-0057, FEAT-0058, FEAT-0059, FEAT-0060, FEAT-0069
- Route index: ../source-route-graphs/discovered-routes-2026-11-12.jsonl
- Proposed automation system: ../automation-lab/workflow-engine-proposed-spec.md
- Original semantic tokens: ../reusable-ui/original-semantic-tokens/tokens.json

## Missing verification gates
- Exact on-screen viewport geometry, component coordinates, computed font values, responsive breakpoints and screenshots: NOT_MEASURED.
- Every button, focus, keyboard, validation, loading/empty/error, permission state and interaction: NOT_EXHAUSTIVELY_TESTED.
- Source licensing and redistribution rights: UNVERIFIED.
- User must not construe a conceptual future workflow as proof of functioning backend behavior.
