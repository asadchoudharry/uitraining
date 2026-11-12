# GR8R Demo Inspection — Source S02 (Extension)

- Inspected: 2026-11-12 (Asia/Karachi) via `curl` entry-page fetches, rendered-text reads, and route-string listing from each demo's main JS bundle (route-like strings only; no bundle decompilation, no code or assets copied).
- Scope: entry page per demo plus, where needed, the main bundle and Axle's named page scripts. Request volume was bounded and polite.
- Result: **13 / 13 reachable (HTTP 200), 0 down.** 12 are JS single-page apps (Vite/React, Next.js, or vanilla JS); Contrail and the Task app are Next.js with server-rendered entry HTML.
- Note: Python `urllib` fetches timed out on TLS handshake from this VM for all hosts; `curl` succeeded for all 13, so all statuses below are from curl.

---

## 1. LedgerOS
- Demo URL: https://ledger-os-v2.vercel.app
- HTTP status: 200 (564-byte Vite shell)
- Title: `LedgerOS` — meta description: "AI finance operations control center"
- SPA: Yes — Vite/React (`<div id="root">`, `/assets/index-Ctd18BVR.js`). No router paths were found in the bundle; navigation appears state-based.
- Modules visible: Finance Overview, Cash Flow, Cash Position, Accounts Payable, Accounts Receivable, Transactions, Invoices, Payments, Expenses, AI Agents, Ask LedgerOS, Notifications
- Evidence status: verified — rendered entry page read (Finance Overview with cash position, AP/AR, needs-attention queue, AI insight, AI agents panel, recent transactions table).
- Description: LedgerOS presents an AI-assisted finance operations control centre for a business, centred on a Finance Overview showing cash position, payables, receivables, monthly spend and net cash flow. An attention queue surfaces risky payments, approvals, overdue invoices and cash-flow alerts, while named AI agents (Payment, Expense, Invoice, Risk Sentinel) are shown handling and reviewing transactions. Supporting areas cover transactions, invoices, payments, expenses and a cash-flow forecast.

## 2. Task Management App
- Demo URL: https://gr8r-task-management.vercel.app
- HTTP status: 200 (10,274-byte Next.js entry)
- Title: `Gr8r Studio` — meta description: "Gr8r Studio — a calm, structured project management workspace."
- SPA: Yes — Next.js (Turbopack chunks, `__next` flight payload); entry HTML contains almost no rendered body text beyond the title.
- Modules visible: All projects, Tasks, Project progress
- Evidence status: verified — rendered entry page read (workspace-health header, All projects / Tasks tabs, active/open/completed/overdue counters, project-progress table).
- Description: This is a calm, structured project-management workspace branded "Gr8r Studio" in its page metadata. The home view summarises workspace health across active projects, with counts for open, completed and overdue tasks. A project-progress table lists each project with status, percentage progress, due date and team members.

## 3. SellerOS
- Demo URL: https://selleros-xi.vercel.app
- HTTP status: 200 (1,042-byte Vite shell)
- Title: `SellerOS`
- SPA: Yes — Vite/React (`<div id="root">`, `/assets/index-D0XdKFn8.js`)
- Routes found in bundle: `/activity`, `/advertising`, `/ai`, `/forecasting`, `/inventory`, `/notifications`, `/onboarding`, `/products`, `/profitability`, `/purchase-orders`, `/reports`, `/sales`, `/sales/orders`, `/settings`, `/settings/billing`, `/settings/integrations`, `/shipments`, `/suppliers`, `/tasks`, `/workspaces`
- Modules visible: Overview, Sales, Sales Orders, Products, Inventory, Forecasting, Advertising, Profitability, Purchase Orders, Shipments, Suppliers, Reports, Tasks, Activity, Notifications, AI Briefing, Settings
- Evidence status: verified — rendered entry page read (Overview with AI briefing, revenue/profit figures, stockout risks, inventory health, shipment list, profit-and-loss breakdown).
- Description: SellerOS is an operations and profit console for an e-commerce seller, opening on an Overview with an AI briefing of today's revenue, profit and attention items such as stockout risks, delays and margin/ad anomalies. It tracks inventory health by SKU with days-of-cover, inbound shipments and purchase orders, and a profitability view breaking revenue down through COGS, marketplace/FBA fees and advertising to net profit. Further modules cover sales/orders, products, forecasting, advertising, suppliers, reports and tasks.

## 4. Veluno
- Demo URL: https://veluno-omega.vercel.app
- HTTP status: 200 (939-byte Vite shell)
- Title: `Veluno` — meta description: "Veluno — supplier onboarding, reviews, documents and renewals in one shared workspace. Know exactly where every supplier stands."
- SPA: Yes — Vite/React (`<div id="root">`, `/assets/index-CvyqXNml.js`)
- Routes found in bundle: `/overview`, `/suppliers`, `/suppliers/new`, `/reviews`, `/reviews/all`, `/reviews/clarifications`, `/documents`, `/renewals`, `/reports`, `/audit`, `/portal`, `/portal/company`, `/portal/documents`, `/portal/clarifications`, `/settings` (+ organisation/policies/users/notifications/integrations/profile), `/login`, `/signup`, `/setup`, `/invite`, `/help`
- Modules visible: Sign-in, Overview, Suppliers, Reviews, Clarifications, Documents, Renewals, Reports, Audit, Supplier Portal, Settings, Help
- Evidence status: verified, sign-in gated — rendered entry page is the sign-in screen ("any password of 4+ characters works" for the demo workspace, plus role try-out and create-account links); module inventory is from bundle route strings.
- Description: Veluno is a supplier-management workspace covering onboarding, reviews, documents and renewals in one shared place. Internal users work through supplier records, review/approval flows and clarification threads, while suppliers get their own portal for company details, documents and clarifications. Audit, reports and policy/user settings round out the administration surface.

## 5. Relay
- Demo URL: https://relay-workflow-os.vercel.app
- HTTP status: 200 (507-byte Vite shell)
- Title: `Relay` (rendered: "Overview | Relay")
- SPA: Yes — Vite/React (`<div id="root">`, `/assets/index-CYWEZTKk.js`)
- Routes found in bundle: `/workflows`, `/agents`, `/approvals`, `/runs`, `/analytics`, `/integrations`, `/settings` (plus the overview home)
- Modules visible: Overview, Workflows, Agents / Workforce, Approvals, Runs, Analytics, Integrations, Settings
- Evidence status: verified — rendered entry page read (needs-attention queue, live activity table of active workflows, workflow-performance metrics, workforce panel).
- Description: Relay is a workflow-automation operating system where AI agents run business workflows across tools such as HubSpot, Salesforce, Intercom, Stripe and Notion. The Overview shows a needs-attention queue (approvals, failed runs, blocked agents, expiring integrations), a live-activity table of running workflows with their agent, progress and runtime, and performance metrics for runs, interventions and cost. Dedicated areas cover workflows, agents, approvals, run history, analytics and integrations.

## 6. Sortie
- Demo URL: https://sortie-chi.vercel.app/overview
- HTTP status: 200 (541-byte Vite shell)
- Title: `Sortie — Autonomous Delivery Operations`
- SPA: Yes — Vite/React (`<div id="root">`, `/assets/index-DbNPeKND.js`, ~2.0 MB)
- Routes found in bundle: `/overview`, `/live`, `/live/tracker`, `/deliveries`, `/deliveries/new`, `/fleet`, `/flight`, `/routes`, `/alerts`, `/analytics`, `/history`, `/terrain`, `/team`, `/team/audit`, `/settings`, `/settings/profile`, `/login`, `/signup`, `/forgot`
- Modules visible: Overview, Live, Live Tracker, Deliveries, Fleet, Flight, Routes, Alerts, Analytics, History, Terrain, Team, Settings
- Evidence status: verified at HTTP level + bundle routes only — the rendered-text read returned no extractable content for this URL, so the module inventory rests on the entry shell and bundle route strings; no rendered screen text was captured.
- Description: Sortie presents an operations console for autonomous delivery, titled "Autonomous Delivery Operations". Its route structure centres on a live operations view with a tracker, delivery creation and management, and fleet and flight views, suggesting drone-style delivery operations. Routes, terrain, alerts, analytics and delivery history, plus team/audit and settings, complete the surface.

## 7. Axle
- Demo URL: https://axle-fleet-os.vercel.app
- HTTP status: 200 (1,693-byte HTML shell)
- Title: `Axle — Command Center` — meta description: "Axle Fleet OS: live operations command center for trucking fleets."
- SPA: Yes, but not a framework SPA — vanilla JS single-page app loading `data.js`, `app.js` and page scripts `pages-core.js`, `pages-fleet.js`, `pages-safety.js`, `pages-compliance.js`, with MapLibre GL and Lucide.
- Modules visible: Command Center, Live Map, Dispatch Board, Fleet, Vehicles, Drivers, Routes, Alerts, Maintenance, Diagnostics, Safety Events, Coaching, Driver Scores, Compliance, HOS / ELD, Inspections / DVIR, IFTA, Driver Qualification, Documents, Fuel & Spend, Geofences, Analytics, Admin
- Evidence status: verified — rendered entry page read (Command Center with fleet status, active drivers, routes, alerts, live operations map, needs-attention faults, HOS watch, coworker assistant, maintenance) and labels confirmed in the named page scripts.
- Description: Axle is a live operations command centre for trucking fleets, opening on a Command Center summarising vehicles, drivers, routes and alerts over a live map. Deep modules cover dispatch, vehicle diagnostics and maintenance work orders, safety events with dashcam-style evidence and driver coaching/scores, and a full compliance stack — hours-of-service/ELD logs, DVIR inspections, IFTA, documents and driver qualification. Fuel/spend, geofences and an AI "Coworker" assistant that proposes actions for approval are also present.

## 8. Cendara
- Demo URL: https://cendara.vercel.app/overview
- HTTP status: 200 (1,445-byte Vite shell; `/overview` lands on sign-in when unauthenticated)
- Title: `Cendara` — meta description: "Cendara — claims operations workspace for billing teams. Prototype with synthetic data."
- SPA: Yes — Vite/React (`<div id="root">`, `/assets/index-C_vaj3iR.js`)
- Routes found in bundle: `/overview`, `/claims`, `/queue`, `/appeals`, `/responses`, `/documents`, `/tasks`, `/reports`, `/audit`, `/team`, `/settings`, `/settings/account`, `/settings/notifications`, `/settings/organization`, `/onboarding/1`, `/setup`, `/login`, `/signup`, `/forgot-password`, `/reset-password`
- Modules visible: Sign-in, Overview, Claims, Queue, Appeals, Responses, Documents, Tasks, Reports, Audit, Team, Settings, Onboarding
- Evidence status: verified, sign-in gated — rendered entry page is the sign-in screen ("Work your denials and rejections to resolution", demo accounts listed with a demo password shown on the page); module inventory is from bundle route strings.
- Description: Cendara is a claims-operations workspace for (healthcare) billing teams, explicitly labelled a prototype with synthetic data. Its workflow centres on working denials and rejections to resolution: a claims queue, appeals and payer responses, supporting documents and team tasks. Reports, an audit trail, team management and organisation settings complete the back-office surface.

## 9. Loadline
- Demo URL: https://loadline-slks.vercel.app
- HTTP status: 200 (988-byte Vite shell)
- Title: `Loadline` — meta description: "Loadline — 3D load planning and transportation operations."
- SPA: Yes — Vite/React (`<div id="root">`, main bundle plus separate `three`, `geo`, `app` and `ui` chunks, indicating a 3D view)
- Routes found in bundle: `/app/overview`, `/app/planning`, `/app/planning/board`, `/app/dispatch`, `/app/shipments`, `/app/freight`, `/app/tracking`, `/app/routes`, `/app/drivers`, `/app/trucks`, `/app/exceptions`, `/app/documents`, `/app/analytics`, `/app/settings`, `/app/settings/users`, `/app/settings/workspace`, `/workspace/new`, `/onboarding`, `/signin`, `/signup`, `/forgot`, `/verify`
- Modules visible: Overview, Planning, Planning Board, Dispatch, Shipments, Freight, Tracking, Routes, Drivers, Trucks, Exceptions, Documents, Analytics, Settings
- Evidence status: verified at HTTP level + bundle routes only — the rendered-text read returned no extractable content for this URL, so the module inventory rests on the entry shell (including its 3D chunk names) and bundle route strings; no rendered screen text was captured.
- Description: Loadline combines 3D load planning with transportation operations for freight. Inside the app shell, a planning board and dispatch view sit alongside shipments, freight, live tracking and routes, with driver and truck resources managed as first-class modules. Exceptions, documents and analytics, plus workspace/user settings, complete the operations surface.

## 10. Contrail
- Demo URL: https://flights-gr8r.vercel.app
- HTTP status: 200 (217,853-byte server-rendered Next.js entry — by far the largest entry page)
- Title: `Search flights · Contrail` — meta description: "Book flights and choose your seat inside a 3D model of the aircraft."
- SPA: Yes — Next.js app (server-rendered HTML with `__next` flight payload, client hydration); the page itself states it is a product prototype with simulated flights, fares and payments.
- Routes visible in entry HTML: `/`, `/explore`, `/explore/aircraft/b789`, `/explore/aircraft/b77w`, `/explore/aircraft/a359`, `/explore/aircraft/a20n`, `/trips`, `/deals`, `/help`, `/help#baggage`, `/help#refunds`, `/profile`
- Modules visible: Search Flights / Book, Explore Aircraft, My Trips, Deals, Check-in, Profile, Help Centre, Baggage Rules, Changes & Refunds, 3D Seat Selection
- Evidence status: verified — full rendered entry page read (search form with trip-type/date/traveller controls, popular destinations, aircraft showcase with seat counts and cabin layouts, footer navigation).
- Description: Contrail is a flight-booking prototype whose differentiator is choosing a seat inside a 3D model of the actual aircraft, with live seat availability. The search flow supports round-trip, one-way and multi-city searches with flexible dates and nearby airports, and an Explore section showcases four aircraft types (Boeing 787-9, 777-300ER, Airbus A350-900, A320neo) with seat counts and cabin configurations. My Trips, Deals, check-in, profile and a help centre covering baggage and refunds complete the traveller surface.

## 11. Knowspace
- Demo URL: https://knowscape-seven.vercel.app
- HTTP status: 200 (984-byte Vite shell) — note the host is spelled `knowscape` while the product is "Knowspace"
- Title: `Knowspace` — meta description: "Knowspace — an infinite canvas of small, true things worth knowing. A product by Gr8r Studio."
- SPA: Yes — Vite/React (`<div id="root">`, `/assets/index-CBH1p92U.js`, ~1.5 MB). No router paths were found in the bundle; it behaves as a single canvas surface.
- Modules visible: Canvas Home, Pick a Topic, plus topic categories found as bundle strings, e.g. Materials, Birds, Mammals, Memory, Botany, Chemistry, Planets, Kitchen Science, Weather, Music, Physics, Taste, Origins, Insects, Fish, Sound, Spices, Spaceflight, Observing the Sky, Trees, Seeds, Games, Language, Computing, Oceans, Earth, Fungi, Typography, Maps, Sleep and Dreams, Optical Illusions
- Evidence status: verified at HTTP level + bundle strings only — the rendered-text read returned no extractable content for this URL, so the inventory rests on the entry shell metadata and topic strings in the bundle; no rendered screen text was captured.
- Description: Knowspace is an infinite-canvas knowledge product by Gr8r Studio, presenting "small, true things worth knowing". Content appears to be organised as bite-size factual cards grouped by topic, spanning nature, science, food, language, space and everyday phenomena, with attribution/licence strings (CC variants) visible in the bundle. The experience is a single explorable canvas rather than a routed multi-page app.

## 12. Hinterland
- Demo URL: https://hinterland-plum.vercel.app
- HTTP status: 200 (724-byte Vite shell)
- Title: `Hinterland — an atlas of the inner life` — meta description: "Hinterland is an editorial publication about mental health and emotional wellbeing — written plainly, drawn carefully."
- SPA: Yes — Vite/React (`<div id="root">`, `/assets/index-DidfeFyP.js`)
- Routes found in bundle: `/topics` (+ 10 topic routes), `/stories` (+ story routes), `/tools` (+ 6 tool routes: paced breathing, leaves on a stream, name what is here, three-minute grounding, evening wind-down, worry appointment), `/check-in`, `/support`, `/resources`, `/search`, `/about`, `/contact`, `/privacy`, `/terms`
- Modules visible: Topics, Featured / Library (Stories), Check-in, Practice (Tools), Support, Search, About, Contact, Corrections / Suggestions / Letters
- Evidence status: verified — rendered entry page read in full (12 numbered topics from Anxiety to Digital Wellbeing, featured essay, recent-pieces library list, check-in prompt, practice section, support/helpline section, corrections/suggestions/letters).
- Description: Hinterland is an editorial publication — self-described as a concept publication — about mental health and emotional wellbeing, organised as an "atlas of the inner life" across twelve topics including anxiety, burnout, grief, loneliness and sleep. It combines essays and plain-language explainers in a library, a gentle non-diagnostic check-in moment, and short self-guided practice tools that run on-device. A support section points readers to external helplines, and corrections, suggestions and letters are handled in the open.

## 13. Atlas
- Demo URL: https://atlas-phi-amber-12.vercel.app
- HTTP status: 200 (1,008-byte Vite shell)
- Title: `Atlas — Design agency for the digital age` — meta description: "Atlas is a design agency for the digital age. Websites, brands, products and the occasional strange idea — designed and built with care."
- SPA: Yes — Vite/React (`<div id="root">`, `/assets/index-BkuSrvGi.js`)
- Routes found in bundle: `/about`, `/services`, `/work`, `/team`, `/insights`, `/contact` (the rendered home is one long gallery-style page)
- Modules visible: Studio (Home), UI/UX Design, Web Design, Development, Branding, SEO, AI Marketing, Creative Strategy, Experiments / Gallery, Guild (Team), Witnesses (Testimonials), Contact
- Evidence status: verified — rendered entry page read in full (hero, seven numbered service "rooms", experiments gallery, guild/process section, testimonials, contact call-to-action).
- Description: Atlas is a design-agency site styled as a walk through gallery rooms, pairing classical-art framing with modern studio services. Seven services are presented in sequence — UI/UX design, web design, development, branding, SEO, AI marketing and creative strategy — each with its own capability list. An experiments gallery, a six-person "guild" team/process section and client testimonials lead to a contact call-to-action.

---

## Summary counts

| Metric | Count |
|---|---|
| Demos inspected | 13 |
| Reachable (HTTP 200) | 13 |
| Down / blocked | 0 |
| JS SPA (any kind) | 13 |
| — Vite/React shell SPAs | 10 |
| — Next.js (SSR entry + hydration) | 2 (Task Management App, Contrail) |
| — Vanilla JS SPA | 1 (Axle) |
| Sign-in gated at entry | 2 (Veluno, Cendara) |
| Rendered text captured | 10 |
| Bundle-routes-only inventory | 3 (Sortie, Loadline, Knowspace) |

Method limits: inventories are entry-surface only (entry page + bundle route strings + Axle's named page scripts). Authenticated interiors of Veluno and Cendara were not entered; their modules are route-evidenced, not screen-evidenced. No demo code or assets were copied into this file — all descriptions are original.
