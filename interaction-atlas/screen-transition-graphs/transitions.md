# Screen transition graphs

## S03 (CODE_VERIFIED, summarised)
Shell routes: home, inbox, my-tasks, tasks, projects, project (tab = board|list|table|calendar|timeline|files|overview), members, activity, notifications, favorites, search, settings, auth (+onboarding), design-system, errors. Overlays (drawer/modals/popovers/palette/context menu) never change the route; they layer over it and restore focus on close. Source: `src/pages/`, `src/shell/view-engine.js`, store `S.ui.route` @ `904205c6`.

## S09 setup (PROPOSED)
Account creation → Setup step 1…9 (rail) → Dashboard (with residual checklist if steps 8/9 skipped). Full contract: `interaction-atlas/user-journeys/s09-company-setup-proposed.md`.
