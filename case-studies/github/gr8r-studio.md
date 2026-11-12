---
{
 "id": "S03",
 "source_id": "S03",
 "title": "GR8R Studio — public GitHub repository (source audit)",
 "canonical_url": "https://github.com/gr8rstudio/gr8r-studio",
 "author": "GR8R Studio (gr8rstudio)",
 "source_type": "github-repository",
 "date_inspected": "2026-11-12",
 "source_commit": "904205c626918ee96054eb35495c394a60c0c601",
 "license_status": "NO LICENCE FILE — all rights reserved by default; analysis and GitHub fork only, no code republication",
 "evidence_status": "CODE_VERIFIED (cloned, read, built, linted)"
}
---

# S03 — GR8R Studio repository: source-verified audit

## 1. Identity
- Repository: `gr8rstudio/gr8r-studio`, default branch `main`, HEAD pinned at **`904205c626918ee96054eb35495c394a60c0c601`** (verified by `git clone` + `git rev-parse HEAD`, 2026-11-12).
- 86 files; ~13,853 lines of JS+CSS under `src/` (CSS alone 5,228 lines). No runtime dependencies; dev-only tooling (Vite 6, ESLint 9, Prettier 3, Lucide icon package).
- Product (per README, confirmed in code): a calm, structured project-management workspace — home dashboard, inbox, my tasks, projects with board/list/table/calendar/timeline/files views, members, teams, activity, settings.

## 2. Scope & confidence
- **CODE_VERIFIED**: the full tree was cloned and read; build pipeline executed (section 13). This is the only source in the corpus where behaviour claims can be code-verified.
- **Licence: there is NO `LICENSE`/`NOTICE` file.** Consequence: no code, CSS or assets from this repository are republished in `uitraining`. This audit quotes only short functional identifiers (file names, action names, token values) for analysis. A GitHub fork preserves lineage without granting reuse rights; fork status is recorded in `reports/publish-receipt.md`.

## 3. Purpose
- Audience: small product teams. Jobs: plan projects, track tasks across five views, triage an inbox, coordinate members/teams, review activity.
- Screen types: dashboard (home), list/board/table/calendar/timeline data views, detail drawer, settings suite, auth + onboarding, design-system showcase page, error pages.

## 4. Layout geometry (CODE_VERIFIED from `src/styles/tokens.css`)
- Sidebar width `--side-w: 252px`; sidebar row height 30px; topbar height 46px; table row height `--row-h: 40px`.
- One shared horizontal content edge: `--gutter: 24px` — breadcrumb, page header, toolbar, list, table and board all start on the same line (README convention, enforced by the token).
- Radii: 4 / 6 / 8 / 10 / 999 px. Spacing: 4pt scale 4–48px. Control heights: 22 / 26 / 30 / 36px.
- Elevation: `--shadow-card` is a hairline ring (`0 0 0 1px var(--border)`) + 1px soft shadow — borders do the structural work, shadows are reserved for popovers/drag.

## 5. Typography (CODE_VERIFIED)
- Stack: `'Geist', ui-sans-serif, system fallbacks`; mono `'Geist Mono'`. (Geist is an open font by Vercel; the repo references it by name — binaries are not bundled here.)
- Scale (dense, app-grade): 11 / 12 / 12.5 / 13.5 (base) / 14.5 / 16 / 19 / 23 px. Base 13.5px is notably denser than marketing sites — appropriate for a work tool.

## 6. Colour and elevation (CODE_VERIFIED, light theme on `:root`, dark redefined — not inverted)
- Surfaces: `--bg #fbfaf8`, sidebar `#f4f3f0`, surface `#ffffff`, sunken `#f7f6f3`; borders `#e9e7e2` / strong `#dad7d0`.
- Text: `#1d1c1a` → `#57544e` → `#6b6760` → `#8c8880` (four-step ramp).
- Accent is swappable: light `#4b5bd6`, dark `#8e9af3`, with `color-mix` soft/line derivatives — one accent drives the whole theme.
- Semantic: green `#25754b`, amber `#8f5e0e`, red `#b23c30`, blue `#3570c4`, violet `#7652c2`, teal `#1e8580`, rose `#bc4270`, orange `#c0612b`. Status colours map to workflow states (backlog/todo/in-progress/review/done).

## 7. Components and composition (CODE_VERIFIED)
- Pages (16 modules in `src/pages/`): home, inbox, my-tasks, tasks, projects, project, overview, members, activity, notifications, favorites, search, settings, auth, design-system, errors.
- Project views (6 in `src/views/`): board, list (via components/task-list), table, calendar, timeline, files, project-overview.
- Overlays (5 in `src/overlays/`): task drawer, modals, popovers, context menu, command palette.
- Rendering model: each page/view is a function returning an HTML string from the store `S`; a central `render()` rebuilds the shell while preserving focus and scroll. Interactions are declared with `data-a="actionName"` and delegated to a shared action table `A` — **182 action registrations (175 unique action names)** were counted in `src/actions/` (navigation, CRUD for tasks/projects/files/members, bulk select/set/delete, filters, saved views, sorting/grouping, calendar/timeline navigation, sharing/invites, palette, theme, onboarding, offline simulation, demo toasts/confirms).
- Native `<select>` elements are progressively enhanced into design-system menus (`src/ui/select.js`) while the native element stays the source of truth — a strong enterprise pattern.
- Icons: Lucide subset inlined as SVG via a Vite `virtual:icons` plugin (only used icons are bundled); 254 `ic()` call sites; stroke-width 1.8, `aria-hidden`.

## 8. Content and information architecture
- Left sidebar: workspace switcher, primary nav (home/inbox/my tasks), project list (expandable, reorderable by keyboard actions `projUp/projDown` and drag), teams, favorites.
- Global: command palette (Cmd/Ctrl+K), global search page, notifications page, activity feed.

## 9. Workflow matrix (CODE_VERIFIED highlights)
- **Onboarding** (`src/pages/auth.js`, 6 steps, state `S.ui.onb` 0–5): (0) use-case radio cards → (1) workspace name + URL slug with live "available" hint and inline validation error state → (2) team size segmented control (`Just me / 2-10 / 11-50 / 51-200 / 200+`) → (3) first project from templates → (4) invite team (3 email fields, or copy invite link; "Send invites" / "Skip for now") → (5) finish → "Open workspace". Step dots + "Step X of N", Back where applicable, Exit setup. All state is local (see §11).
- **Task lifecycle**: create (composer) → edit in drawer (comments with @mentions, subtasks, attachments, dependencies, labels, priority, status popovers with number-key shortcuts 1–5) → drag between board columns / list rows / calendar days → complete, duplicate, archive, delete (with confirm), restore from archive.
- **Saved views & filters**: filter builder (add/edit/toggle/remove/clear), save/rename/delete views, column visibility toggles, grouping, sorting — all persisted locally.
- **Settings**: theme cards (light/dark/system), accent colour, density, role-permissions table, keyboard-shortcuts reference, 2FA screen with recovery codes (UI-level), archived projects restore/delete, danger zone (delete workspace).

## 10. Responsive, keyboard, accessibility, RTL
- Keyboard (CODE_VERIFIED, `src/actions/keyboard.js`): Cmd/Ctrl+K palette; arrow/Home/End navigation inside menus and palette; Enter/Space activation for `role=button/link`; Escape closes overlays; number keys pick statuses; visible focus handling and a skip-to-content action exist.
- Responsive: dedicated `responsive.css` (355 lines) + mobile nav actions (`openMnav/closeMnav`). Dark mode via `prefers-color-scheme` plus explicit `data-theme`. Motion tokens: `--dur 140ms`, three cubic-bezier curves (standard, spring, drawer).
- RTL: NOT_VERIFIED (no RTL code found in the audited tree).

## 11. UX critique
- **Works**: single-gutter alignment discipline; token-driven theming with a genuinely redefined dark palette; dense-but-calm type scale; action-table architecture makes every control auditable; native-select enhancement keeps forms robust; onboarding collects workspace identity, size, first project and invites in 6 low-friction steps.
- **Limits (state them plainly)**: persistence is **localStorage only** (`STORE_KEY 'gr8r.v2'`, seed-data fallback) — there is no backend, no real authentication, no server-side permission enforcement, no real email/invite delivery. Actions named `demoToast/demoConfirm/demoLoad`, `toggleOffline/retryOnline` and `resetDemo` confirm demo behaviours exist. It is an exemplary *front-end* reference, not evidence of a production system.

## 12. Transferability
- **ADOPT_AS_PRINCIPLE**: token architecture (surfaces/text ramp/accent-with-color-mix derivatives), one-gutter layout rule, action-table interaction census method, saved-views + filter-builder pattern, 6-step onboarding shape, select enhancement, icon subsetting.
- **IMPROVE for enterprise**: add server persistence, RBAC enforcement, audit log, and real invite delivery behind the same UI contracts (see `future-product-blueprints/` dossiers that cite S03).
- **AVOID**: presenting local-only demo state as product capability.

## 13. Evidence map
- Clone + HEAD: `git clone https://github.com/gr8rstudio/gr8r-studio.git`, HEAD `904205c6…`, 2026-11-12.
- Build/test (executed locally on the clone, Node 24): `npm install` OK (102 packages); `npm run lint` **PASS** (exit 0); `npx prettier --check .` **PASS** ("All matched files use Prettier code style"); `npm run build` **PASS** — Vite 6.4.4, 56 modules transformed, `dist/assets/index-*.css` 75.21 kB (gzip 15.16), `index-*.js` 358.11 kB (gzip 103.34), built in 1.34s.
- CI in repo (`.github/workflows/ci.yml`): on push to main + PRs — `npm ci`, lint, format:check, build (Node from `.nvmrc` = 22).
- Action count: `grep -rh "^A\.\w* =" src/actions/*.js | wc -l` = **182 registrations**; unique names after `sort -u` = **175** (full list: `interaction-atlas/ui-controls.jsonl`).
- Token values: `src/styles/tokens.css` (207 lines) read in full.

## 14. Attribution / rights
- © GR8R Studio. No licence file at the audited commit → treat as all-rights-reserved. Upstream: https://github.com/gr8rstudio/gr8r-studio @ `904205c6`. This audit is original analysis; no source code is reproduced beyond short identifiers and token values needed for the analysis.
