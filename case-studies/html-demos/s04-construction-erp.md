---
{
 "id": "S04",
 "source_id": "S04",
 "title": "Dreams Construction ERP (Tailwind demo)",
 "canonical_url": "https://dreamserp.dreamstechnologies.com/construction/tailwind/index.html",
 "author": "Dreams Technologies (vendor demo)",
 "source_type": "html-demo",
 "date_inspected": "2026-11-12",
 "license_status": "RIGHTS_RESTRICTED (commercial template demo; analysis only, no page source or screenshots republished)",
 "evidence_status": "Route census RUNTIME_OBSERVED (547-route BFS crawl shared with S05/S06: this source 53/53 HTTP 200); page internals DOCUMENTED_ONLY from titles + index structure except where stated"
}
---

# S04 — Dreams Construction ERP (Tailwind)

## 1. Identity
- Vendor demo for a construction ERP, Tailwind build, seed: `…/construction/tailwind/index.html` ("Dashboard | Dreams Construction ERP").
- **53 routes discovered, 53 HTTP 200, 0 errors** — the index page links all 53; BFS found no deeper routes. Full census: `research/site-maps/s04-construction-route-census.md`; machine record: `data/pages.jsonl` (source S04).

## 2. Scope & confidence
- Complete route-level coverage of the demo as published on 2026-11-12. Screen internals are **DOCUMENTED_ONLY** (titles + route semantics) except the module analysis below, which is derived from the full route/title set — a reliable map of the product's *intended* scope, not of working behaviour. Template demos render sample data; no backend is implied.

## 3. Purpose
- Audience: construction firms (contractors with multiple sites). Jobs: run projects end-to-end — plan, staff, equip, buy, build, inspect, bill — with cost and safety control.

## 4–8. Layout, typography, colour, components, IA (from route architecture)
- Single dashboard (`index.html`) as portfolio home; detail work happens per project/site.
- Module map (route → title):
  - **Projects**: Project List, Project Overview, Planning & Gantt, Project Phases & Tasks, Project Milestones, Project Progress, Project Documents.
  - **Sites & field**: Site Overview, Daily Site Reports, Inspections, Attendance, Employees.
  - **Commercial**: Estimates, Quotations, Budgets, Cost Tracking, Purchase Orders, Invoices, Payments, Expenses, Payroll.
  - **Resources**: Equipment List, Fleet Tracking, Maintenance, Material Requests, Stock Overview (inventory), Warehouses, Vendors.
  - **Governance & quality**: Audits, Quality Checks, Safety Incidents, RFIs & Submittals, Drawings, Document Library.
  - **Platform**: Company Settings, Integrations, Notifications, Users & Roles, My Profile, Reports (Custom / Financial / Project).
  - **Auth & system**: Sign In, Create Account, Forgot/Reset Password, Email Verification, OTP Verification, Two-Factor Authentication, Lock Screen, 404, 500.
- The IA lesson: construction gets its own first-class objects (drawings, RFIs/submittals, safety incidents, daily site reports, inspections) rather than generic "documents/tasks" — domain nouns beat generic containers.

## 9. Workflow matrix
- NOT_VERIFIED per workflow (static demo). The cross-module command-centre logic a real product needs is specified as a proposal in the construction archetype (`design-intelligence/dashboard-archetypes/construction-site-delivery.md`): one event (e.g., a failed inspection) must fan out to task, notification, cost and reporting modules with a single source of truth.

## 10–11. Responsive/a11y; critique
- NOT_VERIFIED at page level in this pass.
- Critique: scope is admirably complete for a mid-size contractor, including the unglamorous pages (OTP, lock screen, error pages) that portfolio shots omit. Risks typical of template demos: progress/planning pages (Gantt, progress %) are the hardest to make real — treat their presence as a requirements list, not a design solution.

## 12. Transferability
- **ADOPT_AS_PRINCIPLE**: domain-noun IA; portfolio-vs-project dashboard split; reports split by audience (custom/financial/project). **IMPROVE**: add approvals/SLA (the E06 gap — no workflow pages exist here). **AVOID**: assuming Gantt/progress UIs imply scheduling engines.

## 13. Evidence map
- BFS crawl 2026-11-12 (bounded, same-origin, `/construction/` prefix): 53 URLs, all 200, titles recorded in `data/pages.jsonl`. Index-page link inventory independently lists the same 53.

## 14. Attribution / rights
- © Dreams Technologies. Demo: https://dreamserp.dreamstechnologies.com/construction/tailwind/index.html. Commercial template — implementation requires the vendor's licence; this study is analysis only.
