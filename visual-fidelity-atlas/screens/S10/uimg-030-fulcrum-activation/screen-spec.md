# SRS — UIMG-030 Fulcrum "Free Trial Activation" (S10)

- Source: user-supplied image UIMG-030 (light) with variants UIMG-035 (near-duplicate crop) and UIMG-032 (dark mode, identical layout/content). Evidence: OBSERVED visual inspection, HIGH confidence. All geometry ESTIMATED from the image; colours ESTIMATED except where the dark variant proves tokenised theming.
- Rights: analysis only; image not republished (see `data/assets.jsonl`).

## Layout geometry (ESTIMATED)
- Three-column app shell: left sidebar (~230px class), centre content, right AI "Agent" panel (~300px class). Top header with breadcrumb + search above the content column.
- Content: KPI row of 2 large cards; below, a "Progress" chart card (dotted bar chart, Mar 10 – Apr 6 axis); below, an "Attribution" table card.

## Content (visible, quoted labels)
- Sidebar sections: REVIEW / ONBOARDING / AUDIENCE with items incl. Goals, Reports, User activity, Flow activity, Flows, Checklists, Product tours, Nudges, Message library, Users, Segments. Account chip bottom-left: "Lazulix Pro".
- KPIs: "Total 15,612 — Users activated in the last 30 days"; "Impact $780K — Revenue influenced in the last 30 days".
- Attribution table columns (flow, status, users, share, revenue): Welcome flow — Running — 420 — 34.7% — $12,493; Product tour: Core features — Active — 288 — 23.8% — $6,742; Setup checklist — Running — 356 — 29.4% — $9,180; Nudge: Invite team — Active — 147 — 12.1% — $3,908.
- Agent panel: greeting "Good morning, Yasir"; prompt chips: "What are flows?", "Suggest a flow", "Activation best practices", "Build a checklist", "Create a segment", "Create a nudge".

## Typography & colour (ESTIMATED)
- Sans UI type; KPI numerals large/semibold; table text small/regular. Light: white/grey surfaces, blue chart, green status pills. Dark variant (UIMG-032): near-black surfaces, white text, same blue chart — layout and content identical, proving a token swap rather than a redesign.

## Components
Sidebar nav (grouped, count-free), KPI card ×2, bar-chart card, status-pilled data table, AI agent panel with suggestion chips, account chip.

## Reconstruction checklist
- [ ] Shell grid 230 / 1fr / 300 with independent scroll for the agent panel.
- [ ] KPI cards: label-under-value pattern ("Users activated in the last 30 days").
- [ ] Attribution table: status pill vocabulary {Running, Active} kept distinct (running = in-flight experiment, active = live) — a naming lesson, verify semantics before reuse.
- [ ] Agent panel: greeting + 6 task-shaped prompt chips; every chip creates the named artefact type.
- [ ] Dark mode via tokens only; verify chart palette in both modes.
- Workflow/back-end: NOT_VERIFIED (single image). Proposed activation-analytics pattern: `design-intelligence/dashboard-archetypes/onboarding-activation.md`.
