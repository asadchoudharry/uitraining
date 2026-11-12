# S09 — Live-browser visual study (2026-11-12, ~11:48–11:50 PKT)

Method: live browser session opened the shot page and enlarged view. No image downloaded or saved. Text-fetch route had previously failed (HTTP 202 / no extractable text via curl; browser.open extracted no readable text) — live browser is the successful evidence route. Status upgrade: ACCESS_BLOCKED (fetch) -> VERIFIED_AND_STUDIED (live visual inspection).

## Page metadata (Dribbble page, not artwork)
- Title: "Onboarding & Company Setup"
- URL: https://dribbble.com/shots/26442731-Onboarding-Company-Setup
- Designer: Jeremy Blaze, team "Never Before Seen"; status "Available for work"
- Posted: Dec 16, 2025; Views 6,234; Likes 21; Saves 10; Comments 1
- Tags: webapp, lightmode, form, signup, onboarding, ui, minimal, clean, shadcnui, shadcn, tailwind, dashboard, saas
- Dribbble-listed palette: #EEEEEE, #C0C1BE, #0F1011, #5D5E5F, #D67035, #D87B42
- Frames: ONE single tall portrait image; no carousel/attachments.
- No shot-description paragraph exists on the page.

## Artwork (visible content only)
Two stacked white rounded cards on pale grey (#EEEEEE family). Product wordmark: HYFIN. Accent: soft peach-orange (palette #D67035/#D87B42). Clean modern sans, light mode, flat.

### Upper card — account creation (split layout)
- Left: form. Heading "Continue to your account". Fields: First Name, Last Name (side by side), Password, Confirm Password. Checked orange checkbox with terms/privacy agreement line (links underlined). Full-width solid orange CTA "Continue".
- Right: marketing headline about a payment platform with $0 processing-fee claim (design's own copy, not a verified product fact), plus overlapping laptop + phone mockups: mini dashboard (sidebar items incl. Dashboard, Invoices, Payment Requests; "Revenue Summary" $2,415; orange line chart) and phone showing an invoice with "Pending" status and $250.00. Bottom fades to white (artwork effect).

### Lower card — Company Setup, step 1 of 9
- Header: HYFIN wordmark; title "Company Setup"; top-right company switcher dropdown showing a company name + street address (differs from the business name typed in the form — both as shown in artwork).
- Left vertical stepper, numbered, faint dotted connector, current step highlighted with pale orange circle. Steps:
  1. Company Info (current)
  2. Verify Bank Account
  3. Select a Plan
  4. Billing Info
  5. Cost Savings
  6. Features
  7. Notifications
  8. QuickBooks Online
  9. Invite Your Team
  No percentage or progress bar — the numbered list is the only progress element.
- Main: heading "Company Information". Section "Business Type and Name": Business Type dropdown (value: a US LLC label), Business Name text field (value: a photography business name). Divider. Section "Location": Address field with clear (x) button, Business Email field (faint value). Image bottom fades to white; no footer/CTA visible below Business Email.

## Observed vs not verified
- OBSERVED (visual): layout, stepper labels/order, field labels, CTA label, palette (page-listed), light-mode minimal style, shadcn/tailwind tags.
- NOT VERIFIED: any behaviour of Continue, validation, save/resume, provisioning, QuickBooks integration, invitations — the shot is a static design; none of that is demonstrated.
