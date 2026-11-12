---
{
 "id": "LOG-DRIBBBLE",
 "source_id": "S01/S07/S08/S09",
 "title": "Dribbble discovery log (raw lane output)",
 "date_inspected": "2026-11-12",
 "evidence_status": "working log; curated records in data/shots.jsonl"
}
---

# Dribbble Discovery — UITraining Sources S01, S07, S08, S09

Method: `browser.search` + `browser.open` (page-text extraction) only, 2026-11-12. **No Dribbble images were downloaded or saved** (rights-restricted); this file contains metadata and written descriptions only. All descriptions are in the researcher's own words and are limited to what page text actually exposed — shot-internal layouts were **not** readable from the text extraction (see Limitations), so no screen internals are claimed for profile-listed shots.

Evidence statuses: `OBSERVED` = title/tags read from the live profile page text via browser.open · `SEARCH_SNIPPET_ONLY` = title seen only in a browser.search result snippet (older crawl of the same profile) · `ACCESS_BLOCKED` = page could not be read.

**Per-shot canonical URLs & shot IDs:** the profile extractions rendered every shot link as a signup-gated "Shot Link" placeholder and did **not** expose individual `/shots/<id>-<slug>` URLs or IDs. The `url` recorded for each shot (in the JSONL) is therefore the exact discovery page where it was enumerated. This is a tooling limitation, not a missing shot. The only shot with a known ID is S09 (from its task-supplied URL).

**Observed layout (all three profiles, own words):** each profile renders as a uniform grid of shot cards; every card shows a thumbnail still, the shot title as the card's link text, and like/save affordances that redirect to the signup page for logged-out extraction. Ilias Miah's cards additionally expose the author's own tag list per shot (reproduced in the S01 tables). Pagination is by `?page=N` links with Prev/Next controls and a "Sign up to continue / Loading more…" gate below the grid.

## Counts summary

| Source | Discovered (enumerated) | In scope | Out of scope | Blocked |
|---|---|---|---|---|
| S01 — Ilias Miah | 72 | 67 | 5 | 0 |
| S07 — Wolfpixel Agency | 26 | 13 | 13 | 0 |
| S08 — Hatypo Studio | 52 | 29 | 23 | 0 |
| S09 — single shot 26442731 | 1 | 1 (by topic, unverified) | 0 | 1 |
| **Total** | **151** | **110** | **41** | **1** |

---

## S01 — Ilias Miah — https://dribbble.com/ilias-miah/shots

Profile header as observed: "I turn AI-generated chaos into polished, launch-ready MVPs" · 959 followers · 78 following · 6,905 likes · "Available for new projects". **No total shot count is displayed on the profile**, so no claimed total exists to compare against. Enumerated pages 1–3 (24 shots each = 72); page 3 still shows a "Next →" control, so **the profile has more shots than were enumerated** — enumeration stopped at 3 pages as a bounded sample of the most recent work. The portfolio is dominated by animated SaaS/dashboard product shots (finance, healthcare, legal, B2B commerce, AI-agent apps).

### Page 1 (most recent)
| # | Shot title | In scope | Scope reason | Evidence | Author tags / visible labels (as extracted) |
|---|---|---|---|---|---|
| 1 | Ebbline Finance Dashboard Design & UI Animation | YES | dashboard / SaaS / fintech | OBSERVED | admin dashboard, ai dashboard, business intelligence, cash flow, data visualization, finance dashboard, financial analytics, financial forecasting, fintech, saas dashboard, web app |
| 2 | EquipFlow Asset Transfer Tracking UIUX Animation | YES | product / web app — asset transfer tracking workflow | OBSERVED | animation, interface, product, service, startup, ui, ux, web |
| 3 | EquipFlow Equipment Asset Detail UIUX Animation | YES | product / web app — equipment asset detail screen | OBSERVED | animation, interface, product, service, startup, ui, ux, web |
| 4 | From Fleet Data to Actionable Decisions | EquipFlow Dashboard | YES | dashboard — fleet data | OBSERVED | animation, interface, product, service, startup, ui, ux, web |
| 5 | Quoin AI Quantity Verification Dashboard Design | Animation | YES | dashboard — AI quantity verification | OBSERVED | animation, interface, product, service, startup, ui, ux, web |
| 6 | Quoin Construction Estimating Dashboard Design | Animation | YES | dashboard — construction estimating | OBSERVED | animation, interface, product, service, startup, ui, ux, web |
| 7 | Reeve · Test before it goes live | UIUX | Animation | YES | SaaS / enterprise dashboard — workflow builder | OBSERVED | ai agent, automation, dashboard, enterprise, product design, saas, web app, workflow builder |
| 8 | Reeve · Is the agent worth it | UIUX | Animation | YES | SaaS analytics dashboard — ROI/insights | OBSERVED | ai agent, analytics, dashboard, data visualization, enterprise, insights, roi, saas, web app |
| 9 | Reeve · When something goes wrong | UIUX | Animation | YES | SaaS dashboard — incident management / operations | OBSERVED | ai agent, dashboard, enterprise, incident management, logistics, operations, saas, web app |
| 10 | Reeve · How an agent earns your trust- UIUX | Animation | YES | SaaS / enterprise dashboard — agent trust | OBSERVED | ai agent, autonomy, dashboard, enterprise, operations, saas, trust, web app |
| 11 | Atrium Property Maintenance Dashboard UI Animation | YES | dashboard — property maintenance | OBSERVED | animation, interface, product, service, startup, ui, ux, web |
| 12 | Plenum | AI Procurement Dashboard Animation | YES | dashboard — AI procurement | OBSERVED | animation, interface, product, service, startup, ui, ux, web |
| 13 | Plenum AI | Intelligent Construction Dashbaord Design Animation | YES | dashboard — construction (title spelling as published: 'Dashbaord') | OBSERVED | ai dashboard, animation, interface, product, service, startup, ui, ux, web |
| 14 | Atrium | AI-Powered Property Management & Approval Dashboard | YES | dashboard — property management + approvals | OBSERVED | animation, interface, product, service, startup, ui, ux, web |
| 15 | Atrium · AI Property Ops Dashboard | AI Agent | YES | dashboard — property operations / AI agent | OBSERVED | animation, interface, product, service, startup, ui, ux, web |
| 16 | AI Workforce OS UIUX Design | Animation | YES | product / SaaS — workforce OS | OBSERVED | animation, interface, product, service, startup, ui, ux, web |
| 17 | Three industries. Three different workflows. One flexible POS | YES | product — POS workflows | OBSERVED | animation, interface, product, service, startup, ui, ux, web |
| 18 | Fiscent — AI Finance Operations Dashboard Animation | YES | dashboard — finance operations | OBSERVED | animation, interface, product, service, startup, ui, ux, web |
| 19 | Mandate — AI Agent Command Center | Risk & Compliance | YES | dashboard — command center / risk & compliance | OBSERVED | animation, interface, product, service, startup, ui, ux, web |
| 20 | Mandate · AI agents for vendor risk | YES | SaaS product — vendor risk agents | OBSERVED | animation, interface, product, service, startup, ui, ux, web |
| 21 | Scout — AI Shopping Agent | Explainer Animation | no | OUT — explainer/marketing animation; no product screen evidenced in title/tags | OBSERVED | animation, interface, product, service, startup, ui, ux, web |
| 22 | FleetFlow AI · Logistics CRM - Email to tomorrow's route | YES | CRM — logistics | OBSERVED | animation, interface, product, service, startup, ui, ux, web |
| 23 | FleetFlow AI · Logistics CRM - The reroute -Animation | YES | CRM — logistics rerouting | OBSERVED | animation, interface, product, service, startup, ui, ux, web |
| 24 | Keystone — From Lead to Listing | Real Estate CRM Animation | YES | CRM — real estate lead pipeline | OBSERVED | animation, interface, product, service, startup, ui, ux, web |

### Page 2
| # | Shot title | In scope | Scope reason | Evidence | Author tags / visible labels (as extracted) |
|---|---|---|---|---|---|
| 1 | Keystone CRM | Morning Brief for Real Estate Agents | YES | CRM — agent morning brief | OBSERVED | animation, interface, product, service, startup, ui, ux, web |
| 2 | Clinician — AI-Powered Healthcare Workspace | YES | SaaS dashboard / web app — clinical workspace, patient portal, telehealth | OBSERVED | ai, appointment booking, clinic, clinical software, dashboard, healthtech, lab results, medical dashboard, patient portal, saas, telehealth, web app |
| 3 | Throughline: AI Healthcare Patient Portal Dashboard | YES | dashboard — patient portal | OBSERVED | ai, dashboard, data visualization, healthtech, lab results, medical dashboard, patient portal, saas, web app |
| 4 | Hither · Responsive Event Page UIUX Design | YES | product / web app page — event discovery & ticket booking | OBSERVED | event discovery, event page, grid layout, landing page, mobile, product design, responsive design, ticket booking, web design |
| 5 | Hither — Event & Nightlife Discovery Platform | YES | product platform — event discovery | OBSERVED | interface, product, service, startup, ui, ux, web |
| 6 | Oriel Landing Page | AI Fintech Website Scroll Animation | no | OUT — marketing landing page only | OBSERVED | ai finance, animation, fintech landing page, hero section, homepage, landing page, marketing website, saas website, scroll animation |
| 7 | Oriel - AI Personal Finance Assistant Dashboard | Animation | YES | dashboard — AI finance assistant / copilot | OBSERVED | ai assistant, ai chat, chatbot, conversational ui, copilot, dashboard, fintech, llm, saas, web app |
| 8 | Oriel - AI Financial Intelligence Dashboard | Animation | YES | dashboard — financial intelligence | OBSERVED | animation, interface, product, service, startup, ui, ux, web |
| 9 | Oriel - AI Financial Intelligence | YES | product — financial intelligence | OBSERVED | interface, product, service, startup, ui, ux, web |
| 10 | Podlogix - Logo Animation | Podcast Platform Brand in Motion | no | OUT — logo/branding animation only | OBSERVED | brand identity, logo animation, logo reveal, motion identity, podcast branding, saas branding |
| 11 | Keel — Personal Finance App UI/UX | YES | mobile app — personal finance / financial dashboard | OBSERVED | data visualization, finance app, financial dashboard, fintech, ios ui, mobile app design, personal finance app, product design |
| 12 | Modura - Who Can Spend What | B2B Account Settings Animation | YES | admin — B2B account settings, permissions / role-based access, approval workflow | OBSERVED | account settings, admin panel, approval workflow, b2b saas, design system, enterprise ux, permissions, role based access |
| 13 | Podlogix - Landing Page in Motion | Website Scroll Animation | no | OUT — marketing landing page only | OBSERVED | dark ui, motion design, podcast platform, product marketing, saas landing page, scroll animation, web design |
| 14 | MODURA - One Order, Start to Finish | B2B Ecommerce Animation | YES | web app — B2B order management / procurement / checkout flow | OBSERVED | b2b ecommerce, checkout flow, enterprise ux, order management, procurement, product, saas, web app design, wholesale |
| 15 | MODURA - Priced for Your Account | B2B Product Page Animation | YES | product — B2B product page with contract pricing | OBSERVED | b2b ecommerce, contract pricing, data visualization, enterprise ux, pricing ux, product page design |
| 16 | MODURA B2B Product Catalog UI/UX Design | Animation | YES | web app — B2B product catalog with filters/sort | OBSERVED | b2b ecommerce, catalog design, ecommerce design, filters, sort, product design, web app |
| 17 | MODURA B2B Ecommerce Dashboard | Animation | YES | dashboard — B2B ecommerce / enterprise | OBSERVED | b2b, ecommerce dashboard, dashboard design, enterprise ux, product, saas, web app |
| 18 | Lexora - Landing Page | Legal AI SaaS Website Animation | no | OUT — SaaS marketing landing page only | OBSERVED | b2b saas, landing page design, legal ai, legal tech, saas landing page, website animation |
| 19 | Merit - An Honest Paywall | Mobile App Animation | YES | mobile app — paywall / pricing / subscription | OBSERVED | animation, free trial, ios, mobile app, paywall, pricing, product design, subscription |
| 20 | A Finding That Outlives Its Matter | Legal SaaS Animation | YES | SaaS dashboard — legal research / knowledge management | OBSERVED | ai, enterprise ux, knowledge management, legal ai, legal research, legal tech, saas dashboard, web app |
| 21 | Merit - A Search That Keeps Working | Job Search App Animation | YES | mobile app — job search with filters / saved search | OBSERVED | ai agent, chips, filters, ios, mobile app, saved search, search |
| 22 | Merit - Who Is In Charge | AI App Animation | YES | mobile app — AI agent settings / privacy / trust | OBSERVED | ai agent, ios, memory, mobile app, privacy, settings, trust |
| 23 | Lexora - Reading the Record | Document Review SaaS Animation | YES | SaaS dashboard — document review / contract analysis / redline | OBSERVED | contract analysis, document review, enterprise ux, legal ai, legal tech, redline, saas dashboard, web app |
| 24 | Lexora - Ask It, Then Check It | Legal Research SaaS Animation | YES | SaaS dashboard — legal research | OBSERVED | ai, enterprise ux, legal ai, legal research, legal tech, saas dashboard, trust and safety ux, web app |

### Page 3
| # | Shot title | In scope | Scope reason | Evidence | Author tags / visible labels (as extracted) |
|---|---|---|---|---|---|
| 1 | Merit - The Follow Up With an Undo | AI Agent App Animation | YES | mobile app — AI agent email follow-up / notifications / undo | OBSERVED | ai agent, email follow up, ios, mobile app, notifications, undo |
| 2 | Approve, Run, Keep | Legal Research SaaS Dashboard Animation | YES | SaaS dashboard — legal research for law firms | OBSERVED | ai, enterprise ux, law firm software, legal ai, legal research, saas dashboard, web app |
| 3 | Pulse Clinic -What It Costs | Patient Portal Dashboard Animation | YES | dashboard — patient portal / medical billing (healthcare SaaS) | OBSERVED | clinic management, health insurance, healthcare dashboard, healthcare saas, medical billing, medical dashboard, patient portal, saas dashboard, web app |
| 4 | Merit - A Pipeline That Runs Itself | Job Search App Animation | YES | mobile app — job pipeline / timeline / interview prep | OBSERVED | ai agent, interview prep, ios, mobile app, pipeline, timeline |
| 5 | What the Clinic Holds | Patient Portal Dashboard Animation | YES | dashboard — patient portal / medical records | OBSERVED | clinic management, healthcare dashboard, healthcare saas, medical dashboard, medical records, patient portal, saas dashboard, web app |
| 6 | Merit - Sure Versus Guessing | AI App Animation | YES | mobile app — explainable AI / citations / evidence | OBSERVED | ai agent, citations, evidence, explainable ai, ios, mobile app |
| 7 | Request to Record | Patient Portal Dashboard Animation | YES | dashboard — patient portal / appointment booking / medical records | OBSERVED | appointment booking, clinic management, healthcare dashboard, healthcare saas, medical dashboard, medical records, patient portal, saas dashboard, web app |
| 8 | Merit - Approve With a Receipt | AI Job Agent App Animation | YES | mobile app — approval flow / bottom sheet / undo | OBSERVED | ai agent, approval flow, bottom sheet, interaction design, ios, mobile app, undo |
| 9 | Merit - The Overnight Run Trace | AI Agent App Animation | YES | mobile app — agent activity log / funnel data visualization | OBSERVED | activity log, ai agent, data visualization, funnel, ios, mobile app |
| 10 | Pulse Clinic -Counter to Supplier | Pharmacy Dashboard Animation | YES | dashboard / ERP-tagged — pharmacy inventory & order management | OBSERVED | clinic management, erp, healthcare dashboard, healthcare saas, inventory management, order management, pharmacy, saas dashboard, web app |
| 11 | Merit - Rules the Agent Works By | AI App Animation | YES | mobile app — agent permissions / settings / empty state | OBSERVED | ai agent, empty state, ios, mobile app, permissions, settings |
| 12 | Pulse Clinic - Invoices to Payments | Healthcare Admin Dashboard | YES | admin dashboard — healthcare invoices / payments / data table | OBSERVED | admin dashboard, clinic management, data table, healthcare, invoices, payments, saas, web app |
| 13 | Merit - Your CV Becomes Evidence | AI App Animation | YES | mobile app — onboarding-tagged CV/evidence flow | OBSERVED | ai agent, cv, evidence, ios, mobile app, onboarding, product design |
| 14 | Merit - Getting Started | AI Job Agent App Animation | YES | mobile app — onboarding / walkthrough | OBSERVED | ai agent, design, interaction, ios, job search, mobile app, onboarding, walkthrough |
| 15 | Keel - AI Spending Coach | Fintech App Animation | YES | mobile app — fintech spending coach / data visualization | OBSERVED | ai, data visualization, fintech, interaction design, ios, mobile app |
| 16 | Keel - Savings Goal With a Real Date | Finance App Animation | YES | mobile app — savings goals | OBSERVED | finance app, interaction design, ios, mobile app, product design, savings goals |
| 17 | Keel - Recurring Commitments | Fintech App Animation | YES | mobile app — recurring payments / subscriptions | OBSERVED | fintech, interaction design, ios, mobile app, recurring payments, subscriptions |
| 18 | Keel - Transaction Detail and Ask | Fintech App Animation | YES | mobile app — transaction detail / search | OBSERVED | fintech, interaction design, ios, mobile app, search, transactions, ui ux |
| 19 | Keel - Ask a Spending Question | Fintech App Animation | YES | mobile app — AI assistant / cash flow | OBSERVED | ai assistant, cash flow, fintech, interaction design, ios, mobile app, product design |
| 20 | Merit AI Job Application Assistant | YES | product — AI job application assistant | OBSERVED | interface, product, service, startup, ui, ux, web |
| 21 | Merit AI Job Matching App UIUX Design | YES | product / app — AI job matching | OBSERVED | interface, product, service, startup, ui, ux, web |
| 22 | Merit AI Job Search App UIUX Design | YES | product / app — AI job search | OBSERVED | interface, product, service, startup, ui, ux, web |
| 23 | WEFT Fashion Ecommerce App UIUX Design | YES | mobile app — fashion ecommerce | OBSERVED | interface, product, service, startup, ui, ux, web |
| 24 | WEFT — E-commerce App- AI Fashion Shopping Experience | YES | mobile app — AI fashion shopping | OBSERVED | interface, product, service, startup, ui, ux, web |

Notable for UITraining: **Modura — Who Can Spend What** (admin panel, role-based access, approval workflow — a hidden-admin pattern), **Pulse Clinic — Invoices to Payments** (admin dashboard, data table), **Pulse Clinic — Counter to Supplier** (author-tagged `erp`, pharmacy inventory/orders), the **Merit onboarding pair** (Your CV Becomes Evidence; Getting Started — both author-tagged `onboarding`), and the **Reeve** enterprise AI-agent dashboard series (workflow builder, incident management, ROI analytics, trust).

---

## S07 — Wolfpixel Agency — https://dribbble.com/wolfpixelagency

Profile description as observed: "Crafted Branding & Product Design for Visionary Brands." Search-snippet profile data (older crawl): 932 followers, 3,667 likes, member since Dec 2024, services include SaaS Design and Mobile & Web App Design. **No total shot count displayed.** Only page 1 was reachable through the routes the tools returned (the /shots page returned the identical 19-title set; no Next control was exposed in extraction), plus 7 additional titles recovered from older search crawls of the same profile, marked SEARCH_SNIPPET_ONLY. Tags were not exposed in this profile's extraction, so visible components/labels are limited to the titles themselves.

### Page 1 (observed)
| # | Shot title | In scope | Scope reason | Evidence |
|---|---|---|---|---|
| 1 | Architecture Studio Website Design - Luxury Homes | no | OUT — marketing website design | OBSERVED |
| 2 | OpenGrok - Security Dashboard SaaS Design | YES | dashboard / SaaS — security | OBSERVED |
| 3 | Commercial Real Estate Website Design - Offices | no | OUT — marketing website design | OBSERVED |
| 4 | Spare Charge EV Charging & Electric Mobility Brand Design | no | OUT — brand design only | OBSERVED |
| 5 | Gluco - Health Dashboard with AI Food Scanner | YES | dashboard — health / AI food scanner | OBSERVED |
| 6 | Real Estate Platform Website Design - Habitra | no | OUT — platform marketing website; product UI not evidenced | OBSERVED |
| 7 | Zenopay Fintech Platform & Digital Payment Landing Page | no | OUT — landing page only | OBSERVED |
| 8 | SaaS Spend Analytics & Enterprise Subscription Dashboard | YES | dashboard / SaaS — spend analytics, enterprise subscriptions | OBSERVED |
| 9 | AI Health Assistant & Symptom Checker Mobile App | YES | mobile app — health assistant | OBSERVED |
| 10 | Employee Spend Management & Approval Dashboard | YES | dashboard — employee spend management + approvals | OBSERVED |
| 11 | AI Content Creation & SaaS Landing Page Design | no | OUT — SaaS landing page only | OBSERVED |
| 12 | AI Property Intelligence & Real Estate Brand Identity | no | OUT — brand identity only | OBSERVED |
| 13 | Trackza — AI-Powered Shipment Tracking App UI | YES | product / app UI — shipment tracking | OBSERVED |
| 14 | Smart Farming Energy & Crop Monitoring Dashboard | YES | dashboard — farming energy & crop monitoring | OBSERVED |
| 15 | Creative Agency Website — Branding & Digital Experience | no | OUT — agency marketing website / branding | OBSERVED |
| 16 | Logistics Customer Management & Revenue Dashboard | YES | dashboard / CRM-adjacent — logistics customer management & revenue | OBSERVED |
| 17 | Aexus — CRM & Lead Management Dashboard UI | YES | CRM dashboard — lead management | OBSERVED |
| 18 | Real Estate Investment Analytics & Property Management Website | no | OUT — website design (analytics product UI not evidenced) | OBSERVED |
| 19 | AI Code Intelligence SaaS Landing Page Design | no | OUT — SaaS landing page only | OBSERVED |

### Additional titles from search snippets of the same profile (older crawls)
| # | Shot title | In scope | Scope reason | Evidence |
|---|---|---|---|---|
| 1 | Healthcare Analytics & Patient Management Dashboard | YES | dashboard — healthcare analytics / patient management (snippet-only, older crawl) | SEARCH_SNIPPET_ONLY |
| 2 | AI-Powered CRM Automation & Sales Management Website | no | OUT — website design (snippet-only) | SEARCH_SNIPPET_ONLY |
| 3 | Real Estate CRM Dashboard — Property Management SaaS UI | YES | CRM dashboard / SaaS — property management (snippet-only) | SEARCH_SNIPPET_ONLY |
| 4 | Logistics Fleet Performance & Shipment Management Dashboard | YES | dashboard — fleet performance / shipment management (snippet-only) | SEARCH_SNIPPET_ONLY |
| 5 | AI Meeting Intelligence & Conversation Management SaaS Website | no | OUT — SaaS website design (snippet-only) | SEARCH_SNIPPET_ONLY |
| 6 | Customer Management Dashboard — CRM Analytics & Account Insights | YES | CRM dashboard — customer management / account insights (snippet-only) | SEARCH_SNIPPET_ONLY |
| 7 | AI Team Workspace & Productivity SaaS Landing Page | no | OUT — SaaS landing page only (snippet-only; listed twice in one crawl, counted once) | SEARCH_SNIPPET_ONLY |

---

## S08 — Hatypo Studio — https://dribbble.com/hatypostudio

Profile description as observed: "UI/UX & Product Design Partner for SaaS, Fintech, Healthtech". Search-snippet bio: product design studio for SaaS/fintech/healthtech startups, since 2021, 250+ projects; 3,627 followers / 5,277 likes in an older crawl. **No total shot count displayed.** Enumerated page 1 (20 titled shots) and page 2 (18 titled shots); page 2 is dominated by marketing websites, in sharp contrast to page 1's app/dashboard mix. Four numbered slots on page 1 and eight on page 2 rendered **without any title text** in the extraction and are therefore not counted or named. 14 further titles come from older search crawls (featured-shots and collection pages), marked SEARCH_SNIPPET_ONLY. Tags were not exposed in extraction.

### Page 1 (observed)
| # | Shot title | In scope | Scope reason | Evidence |
|---|---|---|---|---|
| 1 | Online Learning Mobile App | YES | mobile app — online learning | OBSERVED |
| 2 | Task Management Mobile App | YES | mobile app — task management | OBSERVED |
| 3 | Package Delivery Tracking Mobile App | YES | mobile app — delivery tracking | OBSERVED |
| 4 | EV Companion Mobile App | YES | mobile app — EV companion | OBSERVED |
| 5 | Personal Finance Mobile App | YES | mobile app — personal finance (instance 1) | OBSERVED |
| 6 | EV Controller Mobile App | YES | mobile app — EV controller | OBSERVED |
| 7 | HR Management Dashboard – Workforce, Payroll & Task Tracking | YES | dashboard / HR admin — workforce, payroll, task tracking | OBSERVED |
| 8 | Sales CRM Dashboard – Property Sales & Lead Management | YES | CRM dashboard — property sales & leads | OBSERVED |
| 9 | Package Shipping & Live Tracking App | YES | product / app — shipping & live tracking | OBSERVED |
| 10 | Health Spending & Wellness Tracker Mobile App | YES | mobile app — health spending tracker | OBSERVED |
| 11 | Healthcare & Wellness Mobile App | YES | mobile app — healthcare & wellness | OBSERVED |
| 12 | Personal Finance & Budgeting Mobile App | YES | mobile app — finance & budgeting | OBSERVED |
| 13 | Fintech UI Cards – Dark Mode Component Exploration | YES | product UI components — fintech cards, dark mode (design-system relevant) | OBSERVED |
| 14 | Calendar & Scheduling Web App | YES | web app — calendar & scheduling | OBSERVED |
| 15 | Personal Finance Mobile App | YES | mobile app — personal finance (instance 2, distinct listing with identical title) | OBSERVED |
| 16 | Team Messaging Mobile App | YES | mobile app — team messaging | OBSERVED |
| 17 | Project Management & Team Collaboration Dashboard | YES | dashboard — project management & collaboration | OBSERVED |
| 18 | GPU Cloud Provisioning Dashboard | YES | dashboard / admin — GPU cloud provisioning | OBSERVED |
| 19 | AI Data Center & Energy Website | no | OUT — marketing website design | OBSERVED |
| 20 | Network Topology Dashboard | YES | dashboard — network topology | OBSERVED |

### Page 2 (observed)
| # | Shot title | In scope | Scope reason | Evidence |
|---|---|---|---|---|
| 1 | Business Consulting Website Design | no | OUT — marketing website | OBSERVED |
| 2 | Spa & Wellness Website Design | no | OUT — marketing website | OBSERVED |
| 3 | Wealth Management Website | no | OUT — marketing website | OBSERVED |
| 4 | Poddo | Podcast Platform Branding | no | OUT — branding only | OBSERVED |
| 5 | Modern Insurance Tech Website | no | OUT — marketing website | OBSERVED |
| 6 | Financial Infrastructure Website | no | OUT — marketing website | OBSERVED |
| 7 | Venture Studio Website Design | no | OUT — marketing website | OBSERVED |
| 8 | Climate Tech & Carbon Management Website | no | OUT — marketing website | OBSERVED |
| 9 | Work Page Website | no | OUT — website page | OBSERVED |
| 10 | HR Management Website | no | OUT — marketing website (not the HR dashboard product) | OBSERVED |
| 11 | Industrial Robotics Website Design | no | OUT — marketing website | OBSERVED |
| 12 | Professional Law Firm Website | no | OUT — marketing website | OBSERVED |
| 13 | Audio Technica App | YES | product / app UI | OBSERVED |
| 14 | Global Investment Firm Website | no | OUT — marketing website | OBSERVED |
| 15 | Architecture Portfolio Website Design | no | OUT — portfolio website | OBSERVED |
| 16 | Venture Capital Firm Website | no | OUT — marketing website | OBSERVED |
| 17 | Private Equity Firm Website Design | no | OUT — marketing website | OBSERVED |
| 18 | Consumer Goods Company Website Design | no | OUT — marketing website | OBSERVED |

### Additional titles from search snippets (older crawls)
| # | Shot title | In scope | Scope reason | Evidence |
|---|---|---|---|---|
| 1 | Moire — AI-Powered Skin Shade Matcher | YES | product app — AI skin shade matcher (snippet-only; exact form factor not confirmed) | SEARCH_SNIPPET_ONLY |
| 2 | Serene - Fashion Ecommerce Website | no | OUT — ecommerce website design (snippet-only) | SEARCH_SNIPPET_ONLY |
| 3 | ElixSkin - Dermatology Intelligence Website | no | OUT — website design (snippet-only) | SEARCH_SNIPPET_ONLY |
| 4 | Heilth - Healthcare Hub Landing Page | no | OUT — landing page only (snippet-only) | SEARCH_SNIPPET_ONLY |
| 5 | VeloHub – Logistics Management Dashboard Animation | YES | dashboard — logistics management (snippet-only) | SEARCH_SNIPPET_ONLY |
| 6 | OSCE — Dental Health Intelligence Dashboard | YES | dashboard — dental health intelligence (snippet-only) | SEARCH_SNIPPET_ONLY |
| 7 | Saude - Health Tech Mobile App | YES | mobile app — health tech (snippet-only) | SEARCH_SNIPPET_ONLY |
| 8 | Personal Website - Developer | no | OUT — personal portfolio website (snippet-only) | SEARCH_SNIPPET_ONLY |
| 9 | Zora – Respiratory Health Dashboard | YES | dashboard — respiratory health (snippet-only) | SEARCH_SNIPPET_ONLY |
| 10 | Gaze - Logistic & Supply Chain Management Dashboard | YES | dashboard — logistics & supply chain (snippet-only) | SEARCH_SNIPPET_ONLY |
| 11 | VeloHub – Logistics & Warehouse Management Dashboard | YES | dashboard — logistics & warehouse management (snippet-only) | SEARCH_SNIPPET_ONLY |
| 12 | Hugo - CRM Dashboard | YES | CRM dashboard (snippet-only, via Branding collection crawl) | SEARCH_SNIPPET_ONLY |
| 13 | Chatty - Message Dashboard | YES | dashboard — messaging (snippet-only, via Branding collection crawl) | SEARCH_SNIPPET_ONLY |
| 14 | Meethink - Video Conference Landing Page | no | OUT — landing page only (snippet-only, via Draft collection crawl) | SEARCH_SNIPPET_ONLY |

---

## S09 — Single shot deep study — https://dribbble.com/shots/26442731-Onboarding-Company-Setup

**Evidence status: ACCESS_BLOCKED.**

- Shot ID: **26442731** (from the task-supplied canonical URL).
- Title: **"Onboarding - Company Setup"** (from the task-supplied URL slug; the page itself could not be read to confirm the rendered title).
- Designer: **NOT OBSERVED** — not stated in any accessible source; not invented here.
- Blocker evidence (exact): `browser.open` on the shot URL failed with `browser_open source fetch failed without a source HTTP status`, `failure_stage: source_fetch`, `service_status: 200`, message "The page was fetched, but no readable text could be extracted from it." Two follow-up `browser.search` queries (`Dribbble Onboarding Company Setup shot 26442731` and `"Onboarding - Company Setup" Dribbble stepper company`) returned **zero results matching this shot** — no snippet, designer name, or description is indexed.
- Deep-study fields requested (visible stepper steps, form fields, cards, CTAs, grouping): **NONE COULD BE VERIFIED.** Because the shot page returned no readable text and no image was downloaded (rights restriction + tool scope), any statement about its stepper, fields, cards or CTAs would be fabrication. Recorded honestly as unobserved.
- Scope qualification: onboarding / company-setup is in scope by topic (per the URL slug), but this is a **topic-level** qualification only; the design itself is unexamined.
- What is needed to unblock: a live-browser session (signed-in or challenge-passing) or an owner-supplied screenshot/export of shot 26442731. A generic subagent using search/fetch only cannot complete this study.

---

## Limitations & blockers (all sources)

1. **S09 fully blocked** — see above (fetch returned no readable text; search has no index entry for the shot).
2. **No per-shot URLs/IDs** for S01/S07/S08 — profile extraction hides them behind signup-gated placeholders.
3. **Shot-internal layout not observable** — browser.open returns page text and image *URLs* only; downloading/viewing the images was prohibited for this lane (rights), so component-level claims rest on titles + author tags, not on inspected artwork.
4. **Pagination is incomplete by design of access**: S01 has further pages beyond page 3 (Next control present); S07 exposed no further page route; S08 pages beyond 2 were not enumerated and several slots rendered title-less. No profile displays a total shot count, so completeness against a claimed total cannot be asserted for any source.
5. Duplicate titles exist as distinct listings (S08 "Personal Finance Mobile App" ×2 on page 1; S07 "AI Team Workspace & Productivity SaaS Landing Page" ×2 within one snippet crawl) — counted once per listing instance as noted, never merged silently.
