# UITraining — Enterprise Design Intelligence

An evidence-backed research and design-intelligence system built from ten sources: three live ERP/POS demos, two Dribbble studio profiles and one deep-studied onboarding shot, a design studio's 19 portfolio case studies and their 13 live demos, one fully audited open GitHub product, and 56 user-supplied dashboard/onboarding images.

**The one rule of this repository:** every claim carries an evidence level, and proposed functionality is never dressed up as observed behaviour.

| Evidence level | Meaning |
|---|---|
| `CODE_VERIFIED` | Read in source code (and, for S03, built/linted) |
| `RUNTIME_OBSERVED` | Seen running in a browser/demo |
| `OFFICIALLY_DOCUMENTED` | Stated by the source owner in their own material |
| `UI_VISIBLE_ONLY` | A screen/route exists; behaviour is **not** verified |
| `INFERRED_PRODUCT_LOGIC` | A reasoned reading, labelled as such |
| `NEW_PROPOSAL` | Original design work in this repository |
| `UNVERIFIED_OR_BLOCKED` | Could not be checked; the blocker is recorded |

## Verified scoreboard (2026-11-12)

| Corpus | Result |
|---|---|
| Sources registered | 10 (S01–S10) in `data/sources.yaml` |
| Demo routes crawled | **547 / 547 HTTP 200** (S04: 53, S05: 231, S06: 263) |
| Dribbble shots recorded | 151 (109 in scope) + S09 deep study |
| Studio case studies | 19 / 19 opened; 13 linked demos inspected (13/13 live) |
| GitHub repo audited | S03 @ `904205c6` — lint PASS, format PASS, build PASS |
| User images studied | 56 / 56 individually inspected (54 unique) |
| Features inventoried | 624 rows (`feature-atlas/feature-master-inventory.csv`) |
| Coverage ledger | 788 items, each with exactly one terminal status (`data/coverage.jsonl`) |
| Rights-restricted assets republished | **0** — no unlicensed imagery, page source or code is committed |

## Where things live

- `data/` — sources, coverage ledger, pages, shots, assets (hashes), provenance.
- `case-studies/` — per-source studies in a fixed 14-section format (identity → rights), each with evidence maps.
- `visual-fidelity-atlas/` — screen reconstruction specs (geometry/colour labelled measured or ESTIMATED).
- `interaction-atlas/` — routes, 191 inventoried controls, state machines, journeys (observed vs PROPOSED separated).
- `feature-atlas/` — 624-feature inventory, full passports for headline capabilities, taxonomy sweep, evidence matrix, observed-vs-proposed firewall.
- `automation-lab/` — the special investigation: S05's "workflows" are a levels+escalation **register**, not an engine (checklist verdicts inside) — plus an original, labelled workflow-engine specification and five proposed worked examples.
- `design-system/` + `design-intelligence/` — **original** tokens (JSON + CSS), typography, 18 component specs, 11 dashboard archetypes, 12 workflow patterns. Mode B clean-room output; not copied from any source.
- `future-product-blueprints/` — three separate backlogs (reference-verified / cross-source / original concepts), scored priorities, phased roadmap, feature dossiers.
- `apps/design-explorer/` — a self-contained, searchable explorer over the corpus data (open `index.html`).
- `reusable-ui/` — component recipes, an original prototype screen, and the Figma handoff spec (no Figma file is claimed until a receipt exists).
- `reports/` — coverage summary, quality review, blocked-and-restricted register, publish receipt.

## Start here by goal

- **Rebuild an enterprise dashboard** → `design-intelligence/dashboard-archetypes/` + `design-system/tokens/`.
- **Design approvals/automation** → `automation-lab/document-workflow-deep-dive.md`, then `workflow-engine-proposed-spec.md`.
- **Design onboarding** → `case-studies/dribbble/s09-onboarding-company-setup.md` + `interaction-atlas/user-journeys/s09-company-setup-proposed.md` + archetype `onboarding-activation`.
- **Copy a pattern safely** → `design-intelligence/pattern-library/workflow-patterns.md` (each pattern names its evidence).
- **Check what is NOT known** → `reports/blocked-and-restricted.md` and `reports/coverage-summary.md` (resume checkpoint).

## Rights

Third-party designs remain © their owners. This repository contains original analysis, metadata, hashes and original design work only. `assets/licensed-only/` is empty by design. See `LICENSING-NOTES.md` before reusing anything, and `AGENTS.md` before contributing research.

## Publishing status

The remote `main` holds the owner's initial commit only. This branch was prepared for merge via pull request; if you are reading this on GitHub, the PR was the delivery route. If you are reading the prepared bundle, see `reports/publish-receipt.md` for the exact publish state and the one-command push.
Evidence-backed enterprise design intelligence. Research deliverables are prepared in a separate branch and pull request. Source behavior, inferred behavior and original proposals must remain distinct. Third-party media and code require explicit redistribution rights.

## ChatGPT / UITRAINING Enterprise Design Intelligence

**[Open the full ChatGPT research index](research/chatgpt/README.md)** — includes the [standalone HTML Design Explorer](research/chatgpt/design-explorer/index.html), 10-source registry, 131 discovered routes, 71 evidence-graded features, source-specific case studies, four original enterprise workflow dossiers, original Figma tokens/design and QA/rights ledgers.

- [Native editable UITRAINING Figma workspace](https://www.figma.com/design/6ilnXLVvHo81h7QIAW5AAw)
- [Latest execution and outstanding acceptance gates](research/chatgpt/reports/execution-report-2026-11-12.md)

**Separation:** ChatGPT output is namespaced under `research/chatgpt/` on `main`; Muse output lives in a separate tree and is not overwritten. Indexed routes are not equivalent to completed screen-level or backend verification.
