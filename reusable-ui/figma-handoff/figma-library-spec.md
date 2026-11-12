# Figma handoff — import-ready library specification

Status: **SPECIFICATION ONLY.** No Figma file is claimed by this repository at this revision. (A Figma connector is connected in the authoring environment, but the editable library build is a separate, separately-verified deliverable; this spec is the contract for it. Do not cite a Figma URL from this repository until `reports/publish-receipt.md` records one.)

## Library structure to build
- **File**: "UITraining — Enterprise Design System (Original)".
- **Pages**: 00 Cover & how-to · 01 Foundations (colour/type grids) · 02 Tokens & variables · 10 Components · 20 Archetype screens · 30 Onboarding · 99 Playground.
- **Variables** (from `design-system/tokens/tokens.json`, 1:1 names): color/surface/*, color/text/*, color/border/*, color/status/*, color/accent/* (modes: Light/Dark), space/*, radius/*, size/control-*, size/sidebar-*, font/scale/* (as number variables), motion durations as string documentation (Figma variables cannot drive prototype easing per-token; document only).
- **Text styles**: Display, H1, H2, H3, Body, Body-Sm, Label, Caption, KPI, Money (from `design-intelligence/typography/typography-system.md`).
- **Component sets** (variants + properties per `design-system/components/component-specifications.md`): Button {variant, size, state, icon}, Badge {tone}, Field {state, required}, KPI Card, Table Header/Row {density}, Stepper {orientation, step-state}, Approval Panel, Toast, Dialog {size}, Drawer {width}, Palette Row.
- **Auto-layout rules**: cards = vertical auto-layout, padding = space tokens, gap = space tokens; tables = horizontal rows with fixed first/last columns; shell frame 1440 with sidebar as a component instance (swap expanded/mini).
- **Archetype screens** (from `design-intelligence/dashboard-archetypes/`): build Executive KPI, ERP Command Center, Onboarding Activation first — they exercise the most components.
- **Parity check**: export one archetype screen to PNG at 1440 and compare against the Design Explorer implementation of the same archetype; record differences in `quality/visual-regression/`.
