# SRS — Nextstep admissions onboarding (UIMG-001 + UIMG-002, S10)

- Sources: UIMG-001 (step 1 of 9, name capture) and UIMG-002 (Application Form — Personal Details). Same product/flow, two screens. Evidence: OBSERVED visual inspection, HIGH confidence. Geometry/colours ESTIMATED. Rights: analysis only.

## UIMG-001 — "What Should We Call You?" (Step 1 of 9)
- Browser-window mockup; split layout: left = live mini-preview of the product (welcome + application status cards: one "Submitted", one "Pending"), right = the form panel.
- Single field: Full Name (pre-filled with the applicant's name). Orange **Continue** button.
- Footer strip: segmented progress bar labelled "Step 1 Of 9" + reassurance text: setup typically takes about 5 minutes.
- Palette (ESTIMATED): white, pale mint/teal gradient, orange accent, soft beige.
- Pattern: the applicant sees the *destination product* while onboarding (preview-as-motivation), one question per screen, time expectation stated up front.

## UIMG-002 — Application Form / Personal Details
- App header with user chip; left vertical step navigation: **Personal Details (active) → Academic Details → Documents → Essays & Info → Overview → Payment**.
- Centre: profile summary card (name, email, date of birth, gender, nationality, phone) with the note that this data was pulled from the account and will not be asked again.
- Right: remaining fields for this step — Passport Number, City (dropdown), Postal Code (with example-format placeholder), Street Address. Footer actions: Cancel / Next.
- Palette (ESTIMATED): white/off-white, pale mint gradient, orange accent, dark green secondary.

## Reconstruction checklist
- [ ] Two progress systems that agree: step rail (named steps) + "Step X of 9" strip; never show both with different counts.
- [ ] Data-reuse note pattern: wherever a field is pre-filled from account data, say so at the field group level.
- [ ] Placeholders that teach format ("Ex: 3100") instead of repeating the label.
- [ ] Keep the product preview panel honest: it must render the applicant's real applications, not stock art (NOT_VERIFIED in source).
- Workflow/back-end: NOT_VERIFIED. Proposed journey pattern: `interaction-atlas/user-journeys/s09-company-setup-proposed.md` (same stepper family as S09).
