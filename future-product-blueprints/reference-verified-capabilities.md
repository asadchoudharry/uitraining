# Backlog 1 — Reference-Verified Capabilities

Capabilities with direct source evidence (level in brackets). These exist in the references as working front-end code or demonstrated UI; re-implementation still requires real backends where noted.

| Capability | Evidence | Source |
|---|---|---|
| Token-driven theming (light redefined dark, swappable accent, color-mix derivatives) | CODE_VERIFIED | S03 tokens.css |
| Five project views over one dataset + task drawer + saved views/filters | CODE_VERIFIED | S03 |
| Command palette with full keyboard model | CODE_VERIFIED | S03 |
| 6-step workspace onboarding (use-case -> identity/URL -> size -> templated project -> invites -> finish) | CODE_VERIFIED (UI + local state) | S03 auth.js |
| Document workflow register (module, levels, escalation hours, active) | UI_VISIBLE_ONLY | S05 |
| Approval use-case catalog across modules (expense, PO, leave, discount, timesheet, assets, policy, access, contract, audit) | UI_VISIBLE_ONLY | S05 |
| POS terminal layout variants (at least pos + pos-2..pos-5) | UI_VISIBLE_ONLY | S06 |
| Construction project suite (phases/tasks, milestones, planning, progress, drawings, audits, quality checks, fleet, material requests) | UI_VISIBLE_ONLY (routes) | S04 |
| Automation console IA (workflows/agents/approvals/runs/analytics + needs-attention queue) | RUNTIME_OBSERVED (demo UI) | S02 Relay demo |
| Supplier onboarding/reviews/documents/renewals + supplier portal | RUNTIME_OBSERVED (routes, sign-in gated) | S02 Veluno demo |
| Consent suite (overview, cookie manager with scan status, evidence log) | UI_VISIBLE_ONLY | S10 consently.io |
| Activation analytics per onboarding intervention | UI_VISIBLE_ONLY | S10 Fulcrum |
| Named 9-step company setup incl. integration + value-proof steps | UI_VISIBLE_ONLY | S09 |
