# Feature passport — Saved views + filter builder over one dataset (FP-002)

- Evidence: **CODE_VERIFIED** · Module: Platform · Priority: P0_FOUNDATION · Target status: NOT_AUDITED
- Sources: S03 — https://github.com/gr8rstudio/gr8r-studio

## Observed behaviour
Actions exist and are wired in source: addFilter/fEdit/fToggleVal/rmFilter/clearFilters, saveView/saveViewSubmit/renameView/delView, setViewMode, toggleCol, sorting and grouping actions; views persist in localStorage with the workspace state.

## Not verified
Server persistence, sharing views between users, permission-scoped views.

## Business problem / users / jobs
Users re-create the same filtered lists daily. Users: All workspace users. Jobs: Save a named filter+columns+sort configuration and reapply it in one click across board/list/table/calendar/timeline.

## Screens, actions, fields
Screens: S03-VIEWS. Actions: Add/edit/remove/clear filters, save/rename/delete view, switch view mode, toggle columns, sort, group. Inputs: Filter field/operator/value; view name. Outputs: A persisted view definition applied to the dataset.

## States & validations
States: View: draft (unsaved changes) vs saved. Validations: View name required

## Permissions, notifications, audit
Permissions: Own views only (local app). Notifications: None. Audit: None (local only)

## Data & proposed API
Entities: View {id, name, filters[], columns[], sort, group, viewMode}. API (PROPOSED): PROPOSED: /v1/views CRUD with owner + shared scopes

## Acceptance criteria
Given a filtered table, when the user saves it as a view and switches to board, then the same filter set applies in board mode.

## Test cases
Save/rename/delete view, Filter persistence across view modes, Clear-all restores the unfiltered dataset
