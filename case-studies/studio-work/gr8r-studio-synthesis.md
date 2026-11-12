---
{
 "id": "S02-SYNTH",
 "source_id": "S02",
 "title": "GR8R Studio work synthesis (lane output, curated)",
 "date_inspected": "2026-11-12",
 "evidence_status": "case pages opened via browser.open"
}
---

# GR8R Studio — Work / Case Studies (Source S02)

Source index: https://gr8rstudio.com/work/
Fetched: 2026-11-12 (Asia/Karachi). Method: `browser.open` on the work index and on every linked case-study page, cross-checked against https://gr8rstudio.com/sitemap.xml (which lists exactly the same 19 `/work/*` URLs) and against the raw page HTML for outbound demo links — the live-demo links are **not visible in the extracted page text**, they only appear as hrefs in the HTML, which is why they were recovered from the markup.

**Coverage: 19 work items found, 19 opened successfully, 0 failures. 15 of 19 link to a live public demo (13 unique demo URLs; the two UX audits reuse their product's demo). All 13 demo URLs are on `vercel.app`.**

> Licensing / attribution note: every case study on the site states the same line — "Built by Gr8r for its own portfolio. Not client work." These are self-initiated portfolio products, not named external-client engagements. Descriptions below are original summaries based only on page text/content; no source copy is reproduced beyond short phrases, and no demo was followed beyond recording its link/domain.

## Studio synthesis

Gr8r Studio positions itself on its homepage as "A Digital Product & AI Engineering Partner for Scaleups & Enterprise Teams" that designs and builds digital products, improves existing software, and helps companies "use AI where it makes sense," with designers and engineers working together from planning through delivery. Its credibility markers, repeated on the homepage and the work index, are "$115M+ Client Funding", "1.8K+ GitHub Stars" and "50+ Projects Shipped"; its commercial terms stated on the homepage are projects from $8,000, retainers from $5,500/month, and UX audits at $1,500. The work index itself is headed "Complex challenges, shipped." and frames each story as "the problem, what we did and what changed."

Across the 19 items a consistent house pattern is visible in the *content*: most product cases follow problem → problem/problem-map → information architecture (a sidebar grouped by the user's job) → a four-step workflow → product close-ups → interaction → light/dark themes → style guide (type + colour tokens) → "every screen" gallery → engineering notes → outcomes, with the recurring honesty caveat that measured business results are added "only with evidence and approval." The dominant design idea repeated across the AI products is human oversight of automation: agents do routine work, risky steps wait for a person, and every AI output carries evidence, confidence, or an audit trail (LedgerOS, Relay, Pulse AI, Lumis, SellerOS, Veluno). A second cluster is live operations centred on a map (Sortie, Axle, Loadline). A third, smaller cluster is expressive websites/branding (Contrail, Knowspace, Hinterland, Atlas, HostOp). The final two items are UX audits of Gr8r's own products, published with unflattering findings intact — a distinctive credibility device.

`robots.txt` (https://gr8rstudio.com/robots.txt): allows all crawlers including AI/search bots individually named (GPTBot, ClaudeBot, PerplexityBot, etc.), disallows only `/api/` for every agent, and declares `Sitemap: https://gr8rstudio.com/sitemap.xml`.

---

## 1. CloseCRM
- **URL:** https://gr8rstudio.com/work/closecrm
- **Client / industry:** Client listed as CloseCRM; index tags SaaS – CRM. Project: "CRM web app and website", desktop-first web app. Own portfolio, not client work.
- **Services / deliverables:** Product Design. Deliverable: "Dev-ready Figma + prototype"; timeline 62 days, 3 phases; 144 colour variables.
- **Live demo:** None linked (Figma/prototype deliverable only; no demo href in page HTML).
- **Design approach (original summary):** A calm, structured sales workspace organised around the rep's day — dashboard opening on four pipeline numbers, then ranked tasks, deal board with stage/amount/close date always on the card, dense but scannable companies table, and a workflow builder whose canvas reads as sentences. Inter throughout, near-white base, a periwinkle brand/primary colour with warm and cool accents reserved for status and charts; shown in light and dark modes.

## 2. Pulse AI
- **URL:** https://gr8rstudio.com/work/pulse-ai
- **Client / industry:** Client listed as Pulse AI; index tags AI – Analytics. Project: AI analytics web app, desktop-first.
- **Services / deliverables:** Product Design. Deliverable: 52 screens + design system in Figma, across 11 areas; 508 colour variables, dark-first.
- **Live demo:** None linked (Figma deliverable only; the page discusses demo *data*, not a live demo link).
- **Design approach:** Dark, layered analytics UI built for long sessions: four KPI tiles, a main revenue/users trend, churn-by-region and traffic panels, and a persistent AI-insights column. Every insight is a card stating its confidence, cause and next action (Investigate / Create Campaign). Inter; one violet carries brand and AI, status colours appear only when something needs attention.

## 3. LedgerOS
- **URL:** https://gr8rstudio.com/work/ledgeros
- **Client / industry:** Index tags AI – Fintech. Finance operations product (invoices, expenses, payments, cash flow, risk). Own portfolio. No explicit Client/Project/Deliverable table was present in the extracted page text.
- **Services / deliverables:** Product case study (design + build implied by "Real screens from the live demo"); five AI agents (Invoice, Expense, Flow, Payment, Risk Sentinel), each pausable with status, coverage and activity log.
- **Live demo:** Yes — https://ledger-os-v2.vercel.app/ (domain: `vercel.app`)
- **Design approach:** Decision-first finance layout: an overview leading with cash position, a "needs attention" list and agent findings, then approval queues and risk holds that explain their signals/scores. Quiet grey ledger surfaces, colour used only for status and money in/out; Geist in regular/medium weights; dark by default with a full light theme from the same tokens; desktop and mobile screens shown.

## 4. Task Management App
- **URL:** https://gr8rstudio.com/work/task-management-app
- **Client / industry:** Index tags SaaS – Productivity. Team task/project workspace. Own portfolio; the app was open-sourced (page claims 1.8K+ GitHub stars).
- **Services / deliverables:** Product case study; one task set rendered as board, list, calendar, timeline and personal list, with company and personal modes; screens sourced from the live demo.
- **Live demo:** Yes — https://gr8r-task-management.vercel.app/ (domain: `vercel.app`)
- **Design approach:** Calm, multi-view workspace: sidebar moving from personal (Home, Inbox, My Tasks) out to workspace, projects and teams; project cards carry labels, IDs, priority, due dates and owners. Warm neutrals with a single accent plus a colour per task status; Geist (including a Book weight); warm light theme and a full dark theme from the same tokens.

## 5. Lumis
- **URL:** https://gr8rstudio.com/work/lumis
- **Client / industry:** Client listed as Lumis; index tags AI – Automation. Project: AI automation web app, desktop-first.
- **Services / deliverables:** Product Design. Deliverable: desktop screens + design spec in Figma. Spec details stated: type scale 24/32, 20/24, 14/20, 12/18; cards 1px `#E5E5E5` border, 8px radius; 32px buttons, 20px badges.
- **Live demo:** None linked (Figma deliverable only).
- **Design approach:** An assistant-in-the-workspace layout: Command Centre of AI KPIs (queries, time saved, docs drafted, accuracy) with an activity feed, named AI threads with structured answers, and an in-document AI Assist panel where nothing applies without Apply/Retry/Copy. Editorial typography pairing — Instrument Serif for headings, Geist for body/labels — on a warm near-white base with three text greys, dark buttons, and a gold mark as the sole accent.

## 6. SellerOS
- **URL:** https://gr8rstudio.com/work/selleros
- **Client / industry:** Index tags AI – SaaS. Marketplace-seller operations (sales, stock, shipments, profit across marketplaces). Own portfolio.
- **Services / deliverables:** Product case study; 15 areas grouped by job in the sidebar; AI briefing, alerts with evidence, forecasting, purchase orders; screens sourced from the live demo.
- **Live demo:** Yes — https://selleros-xi.vercel.app/ (domain: `vercel.app`)
- **Design approach:** Briefing-first operations UI: the day opens with an AI briefing and a counted list of issues (14 in the example), each alert expanding to its evidence, method and recommended action, with PO/transfer creation inline. Inter, one brand colour over neutral surfaces, status colours kept for meaning; every screen in light and dark from one token set.

## 7. Veluno
- **URL:** https://gr8rstudio.com/work/veluno
- **Client / industry:** Index tags Procurement – Onboarding. Supplier onboarding for procurement/legal/finance teams, plus a supplier portal. Own portfolio.
- **Services / deliverables:** Built product (not only designs): single-page React app, six role-based demo accounts (workspace admin through to supplier), ⌘K command palette, search/status filters/export on lists, audit log of approvals/uploads/reminders.
- **Live demo:** Yes — https://veluno-omega.vercel.app/ (domain: `vercel.app`)
- **Design approach:** Status-and-owner-first workflow design: overview counts (reviews waiting, blocked, expiring), a needs-attention list and review queue; each supplier page names the blocker and who acts next; parallel team reviews sit side-by-side with approve / clarify / reject decisions; the supplier side is a progress checklist (82% complete in the example). No separate style-guide section was present in the extracted text.

## 8. Relay
- **URL:** https://gr8rstudio.com/work/relay
- **Client / industry:** Index tags AI – Automation. AI-agent workflow automation for operations teams. Own portfolio.
- **Services / deliverables:** Built product: single-page app with Vite + React, workflow canvas drawn with React Flow, ⌘K palette, keyboard shortcuts for approve/save, Ask Relay panel, dark/light/system themes, responsive to phone width.
- **Live demo:** Yes — https://relay-workflow-os.vercel.app/ (domain: `vercel.app`)
- **Design approach:** Run-centred layout: overview pairing workflow/cost metrics and live agent activity with a single needs-attention list (approvals, failed runs); approvals show the proposed action (e.g. a drafted outreach email), the agent's reasons and context before approve/edit/reject; failed runs open on the broken step with its error and input; analytics leads with "where to look first."

## 9. Sortie
- **URL:** https://gr8rstudio.com/work/sortie
- **Client / industry:** Index tags Drones – Logistics. Mission control for autonomous delivery drones. Own portfolio.
- **Services / deliverables:** Built product: React single-page app; live 3D city map with MapLibre GL on OpenFreeMap tiles (extruded buildings, restricted zones, routes), drone models rendered with three.js, ⌘K palette/search, filters on every list.
- **Live demo:** Yes — https://sortie-chi.vercel.app/overview (domain: `vercel.app`)
- **Design approach:** Map-first command centre: fleet numbers, airspace and live events flank a 3D city map (New York in the examples) carrying drones, routes and restricted zones, with the active-missions list alongside; selecting a mission makes the camera follow the drone while a telemetry panel streams altitude, speed, battery, signal, wind and ETA, with hold / return-to-hub controls; route planning compares three options by distance, time, battery and risk.

## 10. Axle
- **URL:** https://gr8rstudio.com/work/axle
- **Client / industry:** Index tags Logistics – Operations. Fleet command centre for trucking (tracking, dispatch, safety, compliance, maintenance). Own portfolio.
- **Services / deliverables:** Built product/demo: simulated telemetry feed for 36 trucks (playable/pausable at 30× and 120×), MapLibre GL map with 2D/3D/satellite views, command palette (Ctrl K), role-scoped views and search, light and dark themes, companion driver-app preview.
- **Live demo:** Yes — https://axle-fleet-os.vercel.app/ (domain: `vercel.app`)
- **Design approach:** One-screen fleet operations: command centre combining fleet status, a live map and a needs-attention list sorted by risk; a selected truck opens driver, speed, trailer temperature, fuel, hours-left and route progress with message/reassign/replay actions; dispatch is a drag-onto-timeline board with late routes in amber; safety and maintenance are score/queue dashboards.

## 11. Cendara
- **URL:** https://gr8rstudio.com/work/cendara
- **Client / industry:** Index tags Healthcare – SaaS. Healthcare claim-denial management for billing teams. Own portfolio.
- **Services / deliverables:** Built product: single-page React app with per-section code loading, command palette (Ctrl K), J/K keyboard stepping through queues, role-based demo accounts (billing specialist, supervisor, administrator), read-only audit history, light/dark/system themes.
- **Live demo:** Yes — https://cendara.vercel.app/overview (domain: `vercel.app`)
- **Design approach:** Deadline-driven claim workflow: overview greeting with an attention summary and a priority work list sorted by deadline; each claim page puts payer, amount, deadline and owner at the top, a seven-stage tracker below, and a next-action card listing what is still required; documents are preview-and-verify lists, appeals pass through a supervisor sign-off screen, and reports chart flow over 4/8/12 weeks.

## 12. Loadline
- **URL:** https://gr8rstudio.com/work/loadline
- **Client / industry:** Index tags 3D – Logistics. Transport operations: load planning, shipments, fleet, dispatch, live tracking. Own portfolio.
- **Services / deliverables:** Built product: React + Vite single-page app, code-split per screen; 3D trucks/cargo in WebGL via three.js; MapLibre maps on OpenFreeMap tiles; ⌘K palette; search/filters/status tabs on every list.
- **Live demo:** Yes — https://loadline-slks.vercel.app/ (domain: `vercel.app`)
- **Design approach:** Visual-planning layout: operations overview leads with daily metrics and the next departure shown as a 3D trailer load beside axle loads and trip economics; exceptions are explained on a side view of the trailer itself with a one-click fix; an optimise view diffs current vs proposed load (capacity, axle imbalance, operations, cost) before applying; tracking pairs an ETA list with a live map and time-replay controls.

## 13. Contrail
- **URL:** https://gr8rstudio.com/work/contrail
- **Client / industry:** Client listed as Contrail; index tags Website – Travel. Project: flight search and booking website, desktop and mobile.
- **Services / deliverables:** Motion Design (service tag on page). Built site: Next.js; each aircraft rendered in WebGL with three.js so one seat dataset drives both the 3D cabin and the accessible flat seat map (keyboard navigable); ⌘K palette. Page states flights/fares/payments are simulated and that the site says so in its footer.
- **Live demo:** Yes — https://flights-gr8r.vercel.app/ (domain: `vercel.app`)
- **Design approach:** A guided booking flow (search → compare → fare → seat in six steps) that keeps trip, price and next action visible throughout: results with a date-price strip and filters, three fares compared line-by-line in a table, then an immersive 3D cabin where selecting a seat moves the camera and prices legroom/power beside it, mirrored by an explanatory flat seat map with instant total updates.

## 14. Knowspace
- **URL:** https://gr8rstudio.com/work/knowspace
- **Client / industry:** Client listed as Knowspace; index tags Website – Learning. Project: interactive learning website, desktop and mobile.
- **Services / deliverables:** Motion Design (service tag on page). Built site: React single-page app; one pannable/zoomable canvas for the whole library, ⌘K search, topic side rail, progress/saved/recent items kept in the browser, touch canvas on mobile.
- **Live demo:** Yes — https://knowscape-seven.vercel.app/ (domain: `vercel.app`; note the demo slug is spelled "knowscape")
- **Design approach:** Spatial, exploratory alternative to a feed: a minimal homepage (one headline ringed by object photos, one button) opening onto an open canvas where facts about 16 topics sit as photos, cut-out objects, big numbers and short cards around a daily greeting; search gathers matching facts into a cluster; a daily goal of 20 facts with medals at 5/10/15/20 supplies the reason to keep wandering.

## 15. HostOp
- **URL:** https://gr8rstudio.com/work/hostop
- **Client / industry:** Client listed as HostOp; index tags Branding – Real estate. Real-estate operations platform brand.
- **Services / deliverables:** Brand Identity. Deliverable: "Logo, colour, type and applications" — mark, wordmark, colour system and applications across product, signage, stationery, packaging and merchandise.
- **Live demo:** None (brand-identity project; no demo href in page HTML).
- **Design approach:** A deliberately minimal identity system built to scale: a mark of two stacked panels inside a blue circle (the platform layering operations), a clean sans wordmark (Inter) locked to the mark on a construction grid, and essentially one owned colour — HostOp Blue, supported by a soft lilac second panel, pale blue ground, and black/white — demonstrated from app icon and watch face through to billboard and building signage.

## 16. Hinterland
- **URL:** https://gr8rstudio.com/work/hinterland
- **Client / industry:** Client listed as Hinterland; index tags Website – Wellbeing. Project: editorial website (mental-health publication), desktop and mobile.
- **Services / deliverables:** Brand Identity (service tag on page). Built site: React single-page app with client-side routing, site-wide search on the `/` key, check-in state and resource filters encoded in the URL, smoothed scrolling and reduced-motion rules throughout, responsive to phone width.
- **Live demo:** Yes — https://hinterland-plum.vercel.app/ (domain: `vercel.app`)
- **Design approach:** Calm editorial design in a single engraved illustration style: a homepage hero pairing a plain headline with an engraved landscape and two routes in (Explore the Library / Find Support), support/helplines also on the homepage, 12 topics each structured as the same five chapters with a sticky contents list, a word-based (not scored) check-in, guided practices such as paced breathing around an engraved moon, and a filterable 48-entry resources directory. Support is in the header of every page.

## 17. Atlas
- **URL:** https://gr8rstudio.com/work/atlas
- **Client / industry:** Index tags Website – Agency. Website concept for a (fictional) Lisbon design studio. Own portfolio; no Client/Project table in the extracted text.
- **Services / deliverables:** Built site concept: React single-page site with client-side routing, Lenis smooth scrolling driving pinned scroll sections (sideways gallery, process tapestry), full-screen menu that previews each page's painting on hover, single-column phone layout.
- **Live demo:** Yes — https://atlas-phi-amber-12.vercel.app/ (domain: `vercel.app`)
- **Design approach:** A gallery-visit concept carried through every page: each section is a numbered "room" with its own colour, an old-master painting reworked as a dot print, and a museum caption; seven service rooms, five project cards, a horizontal scroll gallery of experiments, a six-scene process tapestry (Discover to Launch), and a contact page written as a fill-in letter closed with a "Seal and send" button.

## 18. Veluno UX Audit
- **URL:** https://gr8rstudio.com/work/veluno-ux-audit
- **Client / industry:** Client listed as "Veluno (our product)"; index tags UX audit – Procurement. Project: UX audit of the Veluno supplier-onboarding web app, tested at desktop (1600/1440px), tablet (768px) and phone (390px).
- **Services / deliverables:** Product Design (service tag); UX audit deliverable — 13 findings, 3 high, each with recommended fix and fix / quick-win / decide / leave-alone disposition. Method stated: automated checks (axe-core on nine screens, overflow at three widths, load timings; 202 KB compressed JS first load, first paint 0.6–0.9s) plus senior designer/engineer task walkthroughs by mouse and keyboard, run against the live demo signed in as procurement lead and as supplier. Page states findings are recommendations, "nothing here has been fixed yet."
- **Live demo:** Yes — the audited product's demo, https://veluno-omega.vercel.app/ (domain: `vercel.app`)
- **Design approach (of the audit report page):** An evidence-led report layout: the three headline failures up front (counts that disagree between screens — 31 pending reviews vs team rows summing to 15; supplier rows unreachable by keyboard; a 390px phone view rendering an 867px-wide page), a findings map grouped by where it hurts (numbers, keyboard, phone/tablet, accessibility basics, decisions, first run), ranked top issues each illustrated with desktop and phone screenshots, a measured-numbers section, and an explicit what-to-leave-alone list.

## 19. Cendara UX Audit
- **URL:** https://gr8rstudio.com/work/cendara-ux-audit
- **Client / industry:** Client listed as "Cendara (our product)"; index tags UX audit – Healthcare. Project: UX audit of the Cendara claims web app at 1600/1440/768/390px, by mouse, keyboard and touch.
- **Services / deliverables:** Product Design (service tag); UX audit deliverable — 12 findings, 1 high, ranked with recommended fixes and fix-first / next / quick-win / leave-alone disposition. Method stated: Playwright + axe-core scripted checks on eight screens (sign-in passed with 0 violations), page-width measurement at three sizes, skeleton/load timings (163 KB compressed JS to reach sign-in), and expert task walkthroughs signed in as the billing-specialist demo account against the live demo. Page states nothing has been fixed yet.
- **Live demo:** Yes — the audited product's demo, https://cendara.vercel.app/overview (domain: `vercel.app`)
- **Design approach (of the audit report page):** Same report pattern as the Veluno audit, tuned to measurement: headline finding is tables pushing the *whole page* sideways on tablet/phone (Claims 1,118px wide at 768px) with a root-cause CSS explanation and one-rule fix; followed by a findings map (phone/tablet, getting in, overview, screen readers/voice, visual polish), ranked issues with screenshots (team totals on a personal overview, hover-only demo-login actions, unannounced priority icons), a numbers section, and a leave-alone list praising the palette, dialog focus handling and inline errors.

---

## Failures / gaps
- No case-study page failed to load; all 19 returned full content via `browser.open` on 2026-11-12.
- Text extraction alone does **not** surface the live-demo links or, for LedgerOS and Atlas, a Client/Project/Deliverable table; demo URLs above were recovered from the raw HTML hrefs of each case page (verified via `curl` + grep), and the two missing tables are noted in their sections rather than filled in by inference.
- Demo destinations were recorded only (URL + domain), per task instructions; they were not opened or evaluated.
