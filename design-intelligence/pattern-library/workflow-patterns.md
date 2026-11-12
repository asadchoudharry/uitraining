# Workflow patterns (original pattern library)

Each pattern: context → contract → failure handling → corpus evidence. Behaviour claims are labelled.

## P1. Named-step setup (onboarding)
Vertical or horizontal rail with **all steps named up front**, current highlighted, completed checked; per-step save; exit-and-resume. Evidence: S09 rail (OBSERVED visual), S03 6-step onboarding (CODE_VERIFIED: use-case cards → workspace name/URL with availability hint → team size → templated first project → invites → finish). Full spec: `interaction-atlas/user-journeys/s09-company-setup-proposed.md`.

## P2. CRUD admin table with modal create/edit + confirm delete
Search + page-size (10/25/50/100) + sort + print/export toolbar; Add/Edit modals with required-field asterisks; delete via explicit confirm dialog. Evidence: S05 document-workflows + workflow-approvals (OBSERVED structure). Improve on the source: add row-level audit (created by/at), bulk actions, and an empty state — none demonstrated in the source pages.

## P3. Approval queue with decision panel
Queue list (age, SLA state) → detail with approval panel (see component spec §14) → decide with reason on reject/return → timeline. Evidence: use-case catalog OBSERVED in S05; queue behaviour is PROPOSED (automation lab).

## P4. Saved views over one dataset
Multiple views (board/list/table/calendar/timeline) + saved filter sets over the same records; view state persisted per user. Evidence: S03 (CODE_VERIFIED incl. `saveView/renameView/delView` actions and five project views).

## P5. Command-palette navigation
Cmd/Ctrl+K, grouped results, full keyboard operation, recent items. Evidence: S03 (CODE_VERIFIED).

## P6. Detail drawer over a list
Selecting a row opens a drawer (details/comments/activity tabs) without losing list context, scroll or filters; expandable to full width. Evidence: S03 (CODE_VERIFIED drawer + `toggleDrawerFull`).

## P7. Record detail with vertical timeline
Summary banner → information cards → status timeline (initiated → processed → completed) → related records. Evidence: S10 UIMG-044 Quanta transaction detail (OBSERVED visual).

## P8. Scan/status strip above a data table
A status band (last run, next run, detected count, deltas) sits above the governed table it describes. Evidence: S10 UIMG-055 Cookie Manager scan-status strip (OBSERVED visual). Generalises to imports, sync, reconciliation and backup screens.

## P9. Activation funnel as a product surface
Per-flow/step activation %, status pills (Running/Active), revenue or outcome attribution per intervention (flows, checklists, tours, nudges). Evidence: S10 UIMG-030 Fulcrum (OBSERVED visual). Pair with archetype `onboarding-activation`.

## P10. Integration gallery with per-card signal control
Connector cards with Connected/Disconnected state, "connection expired" recovery action, and per-integration signal/noise toggles. Evidence: S10 UIMG-003 Throughline Tool Stack (OBSERVED visual: ClassDojo/Clever/Remind connected; Canvas/PowerSchool/Google Classroom/Seesaw disconnected with expired-connection alerts). Enterprise rule (from the owner's integration standard): activation validates credentials for real — wrong credentials produce an error, never a silent half-active state.

## P11. Grouped/flat table duality
The same dataset in flat and grouped (e.g., by year) presentations with a filters modal; grouping is a view option, not a separate page. Evidence: S10 Payne Missione rebates ×4 states (OBSERVED visual).

## P12. Spec-sheet-driven build
A dashboard ships with its own type/colour spec sheet as a design artifact (Inter Display, canvas/ink hexes). Evidence: S10 UIMG-040 (OBSERVED). Adopt as process: no screen is "done" without its token sheet (this repo's tokens are the worked example).
