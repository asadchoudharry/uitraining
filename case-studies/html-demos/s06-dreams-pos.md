---
{
 "id": "S06",
 "source_id": "S06",
 "title": "DreamsPOS Retail (HTML demo)",
 "canonical_url": "https://dreamspos.dreamstechnologies.com/retail-pos/html/index.html",
 "author": "Dreams Technologies (vendor demo)",
 "source_type": "html-demo",
 "date_inspected": "2026-11-12",
 "license_status": "RIGHTS_RESTRICTED (commercial template demo; analysis only)",
 "evidence_status": "Route census RUNTIME_OBSERVED (263/263 HTTP 200); variant/dashboard counts OBSERVED from census; page internals DOCUMENTED_ONLY"
}
---

# S06 — DreamsPOS Retail (HTML)

## 1. Identity
- Retail POS + back-office admin demo (HTML build). Seed title: "Dreams POS - Inventory Management & Admin Dashboard". **263 routes, all HTTP 200.** Census: `research/site-maps/s06-pos-route-census.md`; records: `data/pages.jsonl`.

## 2. Scope & confidence
- Route-complete for the retail product as published 2026-11-12. The index also links **sibling products** (restaurant POS, pharmacy POS, laundry POS) and vendor documentation — recorded here as outbound references; they are separate demos and were **not** crawled (out of the S06 path scope).

## 3. Purpose
- Run a retail business: sell (terminal), stock (inventory/warehouses), buy (purchases/suppliers), account (expenses/banking), report — plus super-admin functions for multi-company operation.

## 4–8. IA, dashboards, POS variants (OBSERVED from census)
- **Four dashboards**: `index.html` (Inventory Management & Admin), `dashboard.html` (Overview), `admin-dashboard.html` (Admin), `sales-dashboard.html` (Sales).
- **POS terminal variants: exactly 5** — `pos.html`, `pos-2.html`, `pos-3.html`, `pos-4.html`, `pos-5.html` — plus `pos-orders.html` and `pos-settings.html`. (Earlier speculation about POS 1–8 is corrected by the census: five variants exist in this build.)
- Families visible in the census: products (add/edit/list, categories, brands, units, barcode/label printing class pages), stock (transfers, adjustments, low/expired stock), purchases & returns, sales & returns, quotations, customers/suppliers, expenses, bank accounts, reports (sales and more), HR (users, employees, attendance class pages), super-admin (companies, subscriptions, domains class pages), apps (chat/email/calendar class pages), settings & roles.
- **Interaction comparison of POS variants (required by E09)**: at census level the variants share route furniture (orders, settings) and differ as separate terminal pages; a control-by-control comparison (catalog navigation, cart adjustment, discount/tax controls, checkout layout, keyboard/touch behaviour) requires per-page interaction study and is recorded as **NOT_VERIFIED** in this pass — it is the first item in the resume checkpoint (`reports/coverage-summary.md`), not silently claimed.

## 9. Workflow matrix
- NOT_VERIFIED (static template). Transactional integrity cues to test in any real build: idempotent sale posting, parked-sale consistency across registers, refund authorisation — specified as acceptance tests in FP-005.

## 10–11. Responsive/a11y; critique
- NOT_VERIFIED at page level.
- Critique: breadth is genuine (263 routes is a full back office, not a landing page), and the super-admin trio (companies/subscriptions/domains) shows the vendor designs for multi-tenant operation. The risk is the inverse of S05's: so many near-identical CRUD pages that *density and consistency* — not features — decide usability.

## 12. Transferability
- **ADOPT_AS_PRINCIPLE**: one back office behind the terminal; variant layouts per retail format; super-admin as a designed surface. **IMPROVE**: terminal variants need an interaction matrix before adoption (see §8). **AVOID**: counting routes as capability — behaviour is template-deep only.

## 13. Evidence map
- BFS crawl 2026-11-12 (scope `/retail-pos/`): 263 URLs, all 200; titles in `data/pages.jsonl`. POS/dashboard counts are direct census queries over that file.

## 14. Attribution / rights
- © Dreams Technologies. Demo: https://dreamspos.dreamstechnologies.com/retail-pos/html/index.html. Commercial template; licence required for implementation use.
