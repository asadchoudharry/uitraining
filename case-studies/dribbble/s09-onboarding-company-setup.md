---
{
 "id": "S09",
 "source_id": "S09",
 "title": "Onboarding & Company Setup — HYFIN (Dribbble shot 26442731)",
 "canonical_url": "https://dribbble.com/shots/26442731-Onboarding-Company-Setup",
 "author": "Jeremy Blaze (team: Never Before Seen)",
 "source_type": "dribbble-shot-single",
 "date_inspected": "2026-11-12",
 "license_status": "RIGHTS_RESTRICTED (portfolio artwork; analysis only)",
 "evidence_status": "OBSERVED via live browser visual inspection (text-fetch routes failed: curl HTTP 202/0 bytes; text extraction returned no readable text)"
}
---

# S09 — Onboarding & Company Setup (HYFIN): deep case study

## 1. Identity
- Shot: "Onboarding & Company Setup", Dribbble shot `26442731`, by **Jeremy Blaze** for team **Never Before Seen**.
- Page facts (Dribbble metadata, not artwork): posted Dec 16, 2025; 6,234 views; 21 likes; 10 saves; 1 comment. Tags: webapp, lightmode, form, signup, onboarding, ui, minimal, clean, shadcnui, shadcn, tailwind, dashboard, saas.
- Dribbble-listed palette for the shot: `#EEEEEE`, `#C0C1BE`, `#0F1011`, `#5D5E5F`, `#D67035`, `#D87B42`.
- Frames: **one** single tall portrait image; no carousel or attachments.

## 2. Scope & confidence
- OBSERVED: everything in §4–§9 that describes visible artwork, from a live-browser visual inspection on 2026-11-12 (the shot rendered fully; nothing was blocked in the live browser).
- The artwork shows **two screens stacked in one image**: (A) an account-creation screen, (B) the Company Setup wizard at step 1. The bottom of screen B fades to white inside the artwork — no footer/CTA is visible below the last field.

## 3. Purpose
- Product in the artwork: **HYFIN**, a payments platform (its own in-artwork marketing claim is a $0 processing-fee proposition — design copy, not a verified fact).
- Jobs: create an account, then complete a 9-step company setup that ends in team invitation.

## 4. Layout geometry (ESTIMATED from artwork)
- Canvas: very pale grey (`#EEEEEE` family); two large white rounded cards stacked vertically with a small gap.
- Screen A is a split card: form column left, marketing column right (headline + overlapping laptop/phone device mockups, bottom fading to white).
- Screen B: app shell — slim left sidebar carrying the vertical stepper; main column with page title, sections and fields; company switcher at top-right.

## 5. Typography
- Clean modern sans throughout (the page tags indicate a shadcn/Tailwind build culture; exact font NOT_VERIFIED). Large bold marketing headline; bold medium form headings; small regular grey helper text; tabular-looking numerals in the mock dashboard.

## 6. Colour and elevation
- Light mode, flat. White surfaces, near-black text (`#0F1011` family), mid-grey secondary text (`#5D5E5F`), hairline field borders, one accent: soft peach-orange (`#D67035`/`#D87B42`) used for the primary CTA, the checked checkbox, the current-step highlight and chart line. Elevation is minimal — cards separate from the canvas by tone, not shadow.

## 7. Components and composition
- Screen A: first/last name fields side by side; password + confirm password; pre-checked orange agreement checkbox with underlined Terms/Privacy links; full-width solid orange **Continue** button.
- Screen B stepper (left rail, numbered, faint dotted connector; current step = bold text + pale orange disc; no percentage, no progress bar):
  1. **Company Info** (current) 2. Verify Bank Account 3. Select a Plan 4. Billing Info 5. Cost Savings 6. Features 7. Notifications 8. QuickBooks Online 9. Invite Your Team
- Screen B form (heading "Company Information"): section "Business Type and Name" — Business Type dropdown, Business Name text field; divider; section "Location" — Address field with clear (×) affordance, Business Email field. A company/location switcher dropdown sits at top-right (its displayed company differs from the name typed in the form — recorded as shown).

## 8. Content and information architecture
- The 9-step order is itself the IA lesson: identity → bank verification → plan → billing → value proof ("Cost Savings") → feature configuration → notifications → accounting integration (QuickBooks Online) → team invites last. Setup is framed as value activation, not data entry.

## 9. Workflow matrix (OBSERVED visible states only)
- Actor: new business owner. Entry: account creation (screen A) → Continue → Company Setup step 1 of 9 (screen B).
- UI transitions, validation, save/resume, provisioning, integration behaviour, invite delivery: **NOT_VERIFIED** — a static shot demonstrates none of these. The full functional journey is specified as a PROPOSED design in `interaction-atlas/user-journeys/s09-company-setup-proposed.md`.

## 10. Responsive / accessibility / RTL
- NOT_VERIFIED (single desktop-oriented artwork). Notes: the vertical stepper degrades gracefully to a compact progress indicator on mobile in the proposed journey; the pre-checked consent checkbox is an accessibility/consent anti-pattern flagged in §11.

## 11. UX critique
- **Works**: radical step transparency (all 9 steps named up front, including the payoff step "Cost Savings"); one accent colour with strict discipline; form sections with plain-language helper text; integration (QuickBooks) treated as a first-class setup step rather than a settings afterthought; invites last, after value is established.
- **Problems**: consent checkbox appears pre-checked (dark-pattern risk; enterprise version must default unchecked); no visible save/resume or step-validation cues; the switcher/form company mismatch in the artwork shows how easily sample data inconsistency creeps into setup flows; no visible error states.

## 12. Transferability
- **ADOPT_AS_PRINCIPLE**: named 9-step setup rail; value-proof step inside onboarding; integration as a setup step; single-accent discipline.
- **IMPROVE**: unchecked consent, per-step validation + save/resume, completion percentage alongside the rail, role-aware invite step.
- **AVOID**: pre-checked consent; claiming backend behaviour from a static shot.

## 13. Evidence map
- Live browser inspection, 2026-11-12 ~11:48–11:50 PKT: page + enlarged view rendered; palette/tags/counts read from the page's details panel.
- Failed routes recorded for honesty: `curl` returned HTTP 202 with 0 bytes; text extraction returned no readable text (both 2026-11-12).

## 14. Attribution / rights
- © Jeremy Blaze / Never Before Seen. Source: https://dribbble.com/shots/26442731-Onboarding-Company-Setup. No artwork reproduced in this repository; this is an original analytical record.
