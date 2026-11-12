# Component specifications (original)

Conventions: sizes/colors/spacing reference `design-system/tokens/tokens.json` only. Every component lists states: default, hover, focus-visible, active/pressed, selected, disabled, loading, empty, error, permission-denied — states that do not apply are marked n/a rather than omitted. Evidence links point at corpus patterns, not copied designs.

## 1. Button
- Variants: primary (accent fill), secondary (card fill + border), ghost (transparent), danger (danger fill / danger-ghost), link.
- Sizes: sm 26px, md 30px, lg 36px; padding-inline 12/14/16px; radius `--r` (8px); icon 14–16px, gap 6px.
- Rules: one primary per view region (S09: single full-width Continue); destructive actions never primary-accent; loading keeps width (spinner replaces icon, label stays); focus ring = 2px `--focus` + 2px offset.

## 2. Data table / grid
- Header: 12px/500 uppercase, sunken background, sticky; row heights 44px comfortable / 36px compact (toggle persisted per user, S03 density pref pattern).
- Columns: amounts right-aligned tabular; status = badge; row actions in a trailing `…` menu plus max 1 inline icon action; bulk bar appears on selection with count + actions + "select all results" for filtered sets (S06 POS/inventory pattern class).
- Sorting: click cycles asc/desc/none with aria-sort; filters live in the filter bar, not the header, except column show/hide.
- States: skeleton rows (loading), empty (illustration-free: title + one sentence + primary action), error (inline retry), permission (rows masked vs hidden — product decision, must be consistent).

## 3. Filter bar + saved views
- Pattern (S03 CODE_VERIFIED): add-filter menu → condition chips (field, operator, value) → clear all; views: save current (name), rename, delete, default view per user; view switcher is a segmented control above the table.
- Keyboard: `/` focuses global search within the list context when no input is focused (proposal; S03 uses Cmd+K palette globally).

## 4. Command palette
- Trigger Cmd/Ctrl+K (S03 CODE_VERIFIED); groups: Navigate, Actions, Recent; arrow/Home/End navigation, Enter runs, Esc closes, scope switch (all/current module); results show shortcut hints; empty state suggests recent items. Must trap focus and restore it on close.

## 5. KPI card
- Structure: label (12px, text-3) → value (24–30px, tabular, weight 650) → delta vs period (badge: success/danger by direction semantics of the metric, not by sign alone) → optional sparkline (single accent or neutral; no rainbow series) → drill-down affordance (whole card is a link when a destination exists).
- Corpus note: S10 dashboards overuse 4-across KPI rows; cap at 4, group the rest under "More metrics".

## 6. Status badge
- Tones: success/warning/danger/info/neutral (+soft backgrounds via color-mix). Text always present (never colour-only). Workflow states get one canonical tone map per product (S03 status tokens are the model).

## 7. Wizard / stepper
- Vertical rail variant (S09 OBSERVED): numbered discs + dotted connector, current = bold + accent-soft disc, completed = check, upcoming = muted; all step names visible up front.
- Horizontal variant for ≤5 steps. Every step: Back (except first), primary Continue, optional Skip only when the step is genuinely optional (S03 onboarding pattern), per-step validation summary at top + inline field errors, save-and-resume token, exit-with-confirm when dirty.
- Progress: rail + "Step X of N" text; a percentage bar is additive, never a replacement for named steps.

## 8. Dialog (modal)
- Sizes: sm 420 / md 560 / lg 720px; radius 12px; overlay `--overlay`; focus trapped; Esc closes except destructive-confirm in progress; confirm dialogs name the object and the consequence, danger button uses the verb ("Delete project").

## 9. Drawer
- Right drawer 420px (detail) / 720px (full, S03 `toggleDrawerFull` pattern); slides with `--ease-drawer`; header with entity title + status + close; tabs inside (Details / Comments / Activity — S03 drawer pattern); underlying page stays scroll-locked but visible.

## 10. Toast
- Bottom-right stack, max 3; success/info neutral surface with icon; error toasts persist until dismissed and include the recovery action; never use a toast as the only record of a financial posting.

## 11. Form field
- Label above (12px/500), helper below (11px, text-3), error replaces helper (danger + icon, `aria-describedby`); input height 30/36px; required marked in label text "(required)" for enterprise forms rather than asterisk-only; dependent fields announce changes (`aria-live` polite).

## 12. Searchable select
- Native-select enhancement model (S03): a real `<select>` remains the data source of truth; the enhanced menu adds type-to-filter, keyboard navigation, and clear action. Multi-select uses chips + count.

## 13. Charts
- One chart library per product (corpus lesson from IQRS programme + S10: mixed libraries break visual consistency). Bars/columns for category comparison, lines for time, stacked bars for composition, donut only ≤5 segments with a legend that doubles as values table. Every chart ships a data-table alternative (accessibility) and an empty state; axis labels 11px text-3; gridlines divider colour only.

## 14. Approval panel
- Shows: requester, rule that routed it, amount/context, attachments, decision buttons (Approve / Reject / Return) with reason required on Reject/Return, delegation indicator, SLA countdown + breach state, full decision history below. Self-approval is blocked in UI *and* API (see automation-lab spec).

## 15. Timeline / activity feed
- Reverse-chronological, grouped by day; actor avatar/initials, verb phrase, object link, timestamp (relative + absolute on hover); system events visually quieter than human actions; filter by actor/type.

## 16. File manager
- Grid/list toggle, type icons (single icon set per product), size + modified columns, preview drawer, upload with progress + per-file errors, virus-scan/permission states labelled honestly.

## 17. Breadcrumb
- Max 4 levels visible; overflow collapses middle; current page is plain text, ancestors are links; sits on the shared `--gutter` edge with the page header (S03 rule).

## 18. Empty / loading / error / permission state kit
- One illustration-free visual language: icon (24px, text-3), title, one-sentence cause, one primary action. Loading skeletons mirror the real layout geometry (S03 skeletons module pattern) — never generic spinners for content regions.
