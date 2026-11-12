---
{
 "id": "S05",
 "source_id": "S05",
 "title": "Dreams ERP (Tailwind demo)",
 "canonical_url": "https://dreamserp.dreamstechnologies.com/tailwind/index.html",
 "author": "Dreams Technologies (vendor demo)",
 "source_type": "html-demo",
 "date_inspected": "2026-11-12",
 "license_status": "RIGHTS_RESTRICTED (commercial template demo; analysis only)",
 "evidence_status": "Route census RUNTIME_OBSERVED (231/231 HTTP 200); document-workflow pages studied at structure level; other internals DOCUMENTED_ONLY"
}
---

# S05 — Dreams ERP (Tailwind)

## 1. Identity
- General-purpose ERP admin template (Tailwind build). Seed page title: "HRM Dashboard". **231 routes, all HTTP 200** (index links 178; BFS added 53 deeper routes). Census: `research/site-maps/s05-erp-route-census.md`; records: `data/pages.jsonl`.

## 2. Scope & confidence
- Route-complete for the published demo. Deep structural study: the two workflow pages (see §9 and `automation-lab/document-workflow-deep-dive.md`). Everything else is title/route-level documentation — behaviour NOT_VERIFIED.

## 3. Purpose
- One admin shell for a whole ERP: HRM, CRM, finance, inventory, procurement, sales, POS, projects, support, plus a full applications suite (email, chat, calendar, calls, files, notes, kanban/todo class pages per the census) and system settings.

## 4–8. IA & dashboards (OBSERVED from census)
- **Nine role dashboards**: HRM (the default `index.html`), Inventory, CRM, POS, Finance, Sales, Procurement, Project, Support — the strongest IA signal in this source: the product assumes *role-first* entry, not one generic dashboard.
- Module breadth (route families): employees/recruitment/jobs, deals/CRM, products/inventory, purchases, sales/invoices, expenses/finance, assets (register + analytics), tickets/support, POS, projects, email/apps, settings incl. roles, notifications, and the workflow pair.
- Recurring page grammar (from the two deeply-studied pages): H1 + toolbar (Print/Export/Sort/search/page-size) + data table + Add/Edit modal + delete-confirm — a consistent CRUD dialect across modules (pattern P2 in the pattern library).

## 9. Workflow matrix — the E06 special investigation
- `document-workflows.html`: workflow register — ID, Name, Module, **Levels (2–6)**, **Escalation (12/24/36/48 hours)**, Active flag; Add/Edit modal fields Workflow ID*, Module* (HR/Finance/Legal), Name*, Levels, Escalation, Active.
- `workflow-approvals.html`: approval catalog — Expense, PO "by value", Leave, Discount ">10%", Timesheet, Asset Disposal, Policy, Access, Contract, Audit Exception; Add/Edit Record modal (ID*, Module*, Name*, Status*, Description) with **no rule fields**.
- Verdict (full checklist in the deep-dive): **UI_VISIBLE_ONLY**. No builder, triggers, conditions, approver assignment, simulation, versioning or execution log exists in these pages. The demo names the *problem* (levels + escalation) and the *use-case catalog* — the engine is specified as an original proposal in `automation-lab/workflow-engine-proposed-spec.md`.

## 10–11. Responsive/a11y; critique
- NOT_VERIFIED at page level in this pass.
- Critique: role-dashboard breadth is the design's real strength; the workflow pages are its most instructive weakness — they *look* like automation while being a two-field register. Any team copying the screens without the engine inherits the gap.

## 12. Transferability
- **ADOPT_AS_PRINCIPLE**: role-first dashboards; one CRUD dialect; approval use-case catalog as a requirements checklist. **IMPROVE**: workflow register → real engine (automation lab). **AVOID**: free-text thresholds ("discounts >10%") as a substitute for conditions.

## 13. Evidence map
- BFS crawl 2026-11-12: 231 URLs, all 200, titles in `data/pages.jsonl`. Workflow pages: HTML structure extracted 2026-11-12 (columns, 10 sample rows each, modal labels, select options) — quoted in the deep-dive; page source itself is NOT republished (rights).

## 14. Attribution / rights
- © Dreams Technologies. Demo: https://dreamserp.dreamstechnologies.com/tailwind/index.html. Commercial template; licence required for implementation use.
