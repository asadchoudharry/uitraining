# Document workflow deep-dive — S05 Dreams ERP (Tailwind) + cross-source check

Status labels follow the mission evidence hierarchy. **Observed** below means the page HTML was fetched and its structure/data extracted on 2026-11-12 (headings, table columns/rows, form labels, select options, buttons). Interaction beyond page structure is `UI_VISIBLE_ONLY` — these are static template pages; no backend exists behind them.

## A. What S05 actually contains (OBSERVED page structure)

### A1. `document-workflows.html` — "Document Workflows"
- Data table, columns: **ID, Name, Module, Levels, Escalation, Active, Action**. Pagination 1–3; 10 rows rendered per page.
- Visible records include (ID, name, module, levels, escalation, active):
  - `#WFL0020` Employee Handbook Approval — HR — 2 — 24 hours — Yes
  - `#WFL0019` Sales Report Q1 Review — Finance — 3 — 12 hours — No
  - `#WFL0018` Vendor Contract Approval — Legal — 4 — 36 hours — Yes
  - `#WFL0017` IT Security Guidelines Review — IT — 2 — 48 hours — Yes
  - `#WFL0016` Project Plan ERP Review — Projects — 5 — 24 hours — No
  - `#WFL0013` Purchase Order Approval — Purchase — 4 — 24 hours — No
  - `#WFL0011` Client NDA Approval — Legal — 5 — 12 hours — No
  - (plus Tax Filing Approval, Training Schedule Approval, Annual Budget Review)
- **Add Workflow / Edit Workflow** modals with fields: Workflow ID*, Module* (select: HR / Finance / Legal), Name*, Levels, Escalation, Active (Yes/No select). Delete uses a confirmation dialog ("Yes, Delete"). Toolbar: Print, Export, Sort By, search, page-size select (10/25/50/100).
- **That is the entire demonstrated capability**: a CRUD record of (module, level count, escalation hours, active flag). There is **no** visual builder, condition editor, trigger picker, approver assignment UI, simulation, version history or execution log anywhere in the page structure.

### A2. `workflow-approvals.html` — "Workflow & Approvals"
- Data table: **ID, Module, Name, Description, Status, Action**; module filter chips: Finance, Purchase, HRM, Sales, Projects (+checkbox filters).
- Visible records (all status Active): Expense Approval ("Employee expense claims"), Purchase Order Approval ("PO approvals by value"), Leave Request Approval, Discount Approval ("Approvals for discounts >10%"), Timesheet Approval, Asset Disposal, Policy Approval ("Sign-off before publish"), Access Request Approval, Contract Sign off, Audit Exception.
- **Add Record / Edit Record** modal: ID*, Module*, Name*, Status* (Active/Inactive), Description. No rule fields at all.
- The threshold idea (">10%", "by value") exists **only as free-text descriptions** — there is no condition field that could evaluate it.

## B. E06.1 investigation checklist — verdicts for S05

| # | Capability dimension | Verdict in S05 |
|---|---|---|
| 1 | Workflow catalog (search, status, active toggle) | UI_VISIBLE_ONLY — table + search + Active flag; no folders/tags/usage counts |
| 2 | Builder modes (visual editor, condition table, sequential builder, templates) | NOT_FOUND_IN_SOURCE |
| 3 | Triggers (record events, schedules, webhooks, thresholds…) | NOT_FOUND_IN_SOURCE |
| 4 | Conditions (AND/OR, comparisons, expressions) | NOT_FOUND_IN_SOURCE (thresholds appear only in free-text descriptions) |
| 5 | Actions (assign, notify, update, webhook…) | NOT_FOUND_IN_SOURCE |
| 6 | Approval routing (sequential/parallel/quorum/delegation/amount-based) | PARTIAL_UI_ONLY — a numeric "Levels" count and module scoping; no assignee policy, no routing UI |
| 7 | SLA & escalation | PARTIAL_UI_ONLY — a single "Escalation" hours value per workflow (12/24/36/48h); no calendars, reminders, breach tracking |
| 8 | Validation & guardrails (maker-checker, SoD, self-approval block) | NOT_FOUND_IN_SOURCE |
| 9 | Execution control (versions, retries, DLQ, audit of runs) | NOT_FOUND_IN_SOURCE |
| 10 | Testing (preview, simulation, dry run, trace) | NOT_FOUND_IN_SOURCE |
| 11 | Analytics (run counts, SLA compliance, bottlenecks) | NOT_FOUND_IN_SOURCE on these pages |
| 12 | UX (list, detail, wizard, pickers, log inspector) | UI_VISIBLE_ONLY — list + modal CRUD only |
| 13 | Security (rule permissions, secrets, tenant isolation) | NOT_FOUND_IN_SOURCE |

## C. Cross-source check
- **S04 Construction ERP**: route census includes approvals-adjacent pages (see site map); no workflow-builder route was discovered in its index link inventory. Verdict: NOT_FOUND_IN_SOURCE at index level; full census in `research/site-maps/s04-construction-route-census.md`.
- **S06 Dreams POS**: no workflow/rule-builder route in its index inventory (252 links). NOT_FOUND_IN_SOURCE.
- **S03 GR8R Studio (CODE_VERIFIED)**: no automation engine; it has an *action table* (182 UI actions) and status workflows for tasks, which is UI interaction architecture, not a business rule engine. Its task status model (backlog → todo → in-progress → review → done, tokenised) is the corpus's best *state-machine presentation* reference.
- **S02 Relay (studio case narrative + live demo routes)**: a workflow-automation operating-system concept. Its public demo (inspected 2026-11-12, HTTP 200, Vite/React SPA) exposes bundle routes `/workflows`, `/agents`, `/approvals`, `/runs`, `/analytics`, `/integrations`, `/settings`, and its rendered overview shows a needs-attention queue (approvals, failed runs, blocked agents, expiring integrations), a live-activity table of running workflows with agent/progress/runtime, and run/intervention/cost metrics. Evidence level: UI structure RUNTIME_OBSERVED at overview level (demo data; no real execution, integrations or persistence is implied). This is the corpus's closest *interface* reference for an automation console — and it is still a front-end demo, not a verified engine.
- **S09**: the setup stepper names an "approvals-adjacent" sequence (verify → plan → billing) but demonstrates no rules. UI_VISIBLE_ONLY.

## D. Conclusion (evidence-based)
No source in this corpus demonstrates a working workflow-automation engine. The strongest *observed* artefacts are: (1) S05's minimal data model — workflow = module + levels + escalation hours + active flag; (2) S05's catalog of approval *use cases* across modules; (3) S03's rigorous UI state/action discipline. Everything beyond that in this repository's automation lab is labelled **NEW_PROPOSAL** and specified in `workflow-engine-proposed-spec.md`.
