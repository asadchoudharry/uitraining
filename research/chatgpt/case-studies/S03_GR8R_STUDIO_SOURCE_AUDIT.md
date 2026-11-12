# S03 — GR8R Studio source audit (initial, 2026-11-12)

**Repository:** https://github.com/gr8rstudio/gr8r-studio  
**Observed HEAD:** `904205c626918ee96054eb35495c394a60c0c601` (2026-10-07 commit)  
**Evidence level:** inspected GitHub repository contents and selected source files, not an executed browser QA run.  
**License caution:** No root `LICENSE` file was found during this check. Do not copy or redistribute its source/assets in UITRAINING without a separate rights check.

## Confirmed architecture
- `package.json`: Vite 6 + native JavaScript ES modules/CSS; lint (ESLint), format (Prettier), and build scripts; Node >=18.
- `src/main.js` is listed as entry point. `src/core/` has `store.js`, `theme.js`, constants and utilities.
- `src/shell/` includes render, layout, skeletons and view engine; `src/pages/` contains home, inbox, my tasks, projects, tasks, activity, members, settings, auth, notifications and system pages.
- `src/overlays/` includes drawer, modals, popovers, palette, context menu. `src/features/` includes subtasks, teams and archive.
- `src/styles/tokens.css` includes explicit light/dark surfaces, semantic status colors, 4px-base spacing, variable row density and accent modes.

## Traceable source behaviors (do not overclaim)
| Evidence ID | Observed code / claim | Evidence | Confidence | Scope |
| --- | --- | --- | --- | --- |
| S03-A01 | Delegated click dispatch from `[data-a]` to action table `A`; input handlers via `[data-in]`, form submit dispatch via `[data-submit]` | https://github.com/gr8rstudio/gr8r-studio/blob/main/src/actions/events.js | Verified source code | SOURCE_IMPLEMENTED, not browser-tested |
| S03-A02 | Command palette Ctrl/Cmd+K; shortcut and navigation handlers, Tab handling for modals | https://github.com/gr8rstudio/gr8r-studio/blob/main/src/actions/keyboard.js | Verified source code | SOURCE_IMPLEMENTED, not accessibility-tested |
| S03-A03 | Palette routes for task/project creation, global search, workspace switch, appearance, invite member, navigation | https://github.com/gr8rstudio/gr8r-studio/blob/main/src/overlays/palette.js | Verified source code | SOURCE_IMPLEMENTED, not browser-tested |
| S03-A04 | Focus/scroll restoration after shell re-render and explicit route list | https://github.com/gr8rstudio/gr8r-studio/blob/main/src/shell/render.js | Verified source code | SOURCE_IMPLEMENTED, not browser-tested |
| S03-A05 | Data loaded/saved from browser `localStorage` key `gr8r.v2` and seeded workspace data | https://github.com/gr8rstudio/gr8r-studio/blob/main/src/core/store.js | Verified source code | SOURCE_IMPLEMENTED, **not** evidence of multi-user backend persistence |
| S03-V01 | Design token variables include spacing, colors, component dimensions, dark mode, density and accent themes | https://github.com/gr8rstudio/gr8r-studio/blob/main/src/styles/tokens.css | Verified source code | VISUAL_SYSTEM_SOURCE |

## Screen/interaction extension contract — original UITRAINING proposal
For each source page: capture entry path, actor, displayed data, primary/secondary actions, validation, pending/success/error/empty/permission states, keyboard/RTL/mobile behavior, persistence type, API boundary and a reproducible QA case. Copy patterns conceptually only and implement original design/code.

### First reusable patterns to build as original implementations
1. **Global command menu:** grouped actions, search results, keyboard navigation, escape and role-filtered commands.
2. **Project multi-view switcher:** list/board/table/calendar/timeline/file views backed by a single filtered dataset, synchronized URL state and user permissions.
3. **Task detail drawer:** comments/subtasks/assignees/status, unsaved-change guard and conflict resolution.
4. **Flexible density/theme shell:** semantic status tokens; compact/comfortable modes; visible focus states; no raw color-code coupling.
5. **Activity/audit separation:** UI activity timeline is not by itself an authoritative backend audit trail.

## Open verification work
- Execute application in browser and test navigation/action states; inspect visual fidelity across responsive sizes.
- Check whether any tests exist beyond lint/format/build and run them.
- Confirm ownership and redistribution rights for images, icons and code.
- Map real field/action schemas and update each claim with verified runtime results.
- Benchmark source patterns against enterprise requirements (server-side RBAC, tenant isolation, audit evidence, persistence) before adoption.

This is a partial source-specific case study, not complete S03 coverage.
