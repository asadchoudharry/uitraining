# S10 user-images corpus — synthesis (56 images, UIMG-001…056)

Method: every image was opened and inspected individually (records: `case-studies/user-images/`, raw logs `visual-analysis-log-a/b.md`). 54 unique files by SHA-256; one exact duplicate pair (UIMG-046 = UIMG-052) and several same-screen variants (below). Categories observed: **dashboard 29, table 13, other 10, onboarding 3, form 1, mobile 0**. Confidence: 53 HIGH, 3 MED.

## What the corpus actually is
A cross-section of contemporary SaaS/admin design references (mostly Dribbble-style product shots, several photographed/cropped): education (Nextstep admissions onboarding; Throughline teacher tooling; Algebra Foundations learner path), product analytics/onboarding (Fulcrum), consent/compliance (consently.io), payments (Quanta.), finance (fintrack, Leel.Data ING, OripioFin), commerce ops (Confidency OS, Payne Missione rebates, Solvix suppliers), CRM (BizLink, Cliento), healthcare (Elera patient-flow kanban, an unnamed hospital dashboard), agency/project tools (panze studio, JYSigma, Noteflow, Flowra, Axon, Spark Pixel), comms (unified inboxes, a dark email client, messaging screens), plus one literal design-spec sheet (UIMG-040: Inter Display on `#F7F7F7`/`#2B3749` for the Kravio dashboard UIMG-038).

## Recurring patterns (observed across multiple images)
1. **The analytics shell is converging**: left sidebar (grouped sections, ~200–260px class), top bar with breadcrumb + search, KPI row (3–4 cards), one chart card + one table card, and — the 2026 signature — a **right-hand AI/agent panel** (Fulcrum's "Agent" column with suggested prompts; the unnamed student-risk dashboard centred on one student; Throughline's de-noising positioning). Enterprise takeaway: design the agent panel as a *column with provenance*, not a floating chatbot.
2. **Onboarding is measured like a funnel**: Fulcrum's whole product is activation analytics (flows/checklists/tours/nudges with per-flow activation % and revenue attribution); Nextstep runs a 9-step application with a persistent progress strip and a "pulled from your account — you won't be asked again" data-reuse note; Algebra Foundations shows a 5-step diagnostic path with per-topic mastery and a results step ("Step 3 of 5"). Three different answers to the same problem; the strongest shared principle: **name the steps, show the count, reuse entered data visibly**.
3. **Tables carry the enterprise weight**: consent log with 48,920 records, framework column (GDPR/CCPA/LGPD/PIPEDA/APPI…) and masked IPs; rebates list in flat vs grouped-by-year variants with a filters modal (Payne Missione ×4 states of one screen — a free lesson in table state design); cookie manager with scan-status strip above the table.
4. **Detail pages are timelines + cards**: Quanta transaction detail (summary banner, information/payment/client cards, 3-step vertical timeline) is the corpus's cleanest record-detail template; TX-104892 links the detail to its transactions table row — cross-screen ID consistency done right.
5. **Light/dark pairs ship together**: Fulcrum and fintrack each appear in both modes with identical layout (UIMG-030/032, UIMG-033/034) — evidence that tokenised theming (cf. S03) is now the expected baseline, not a feature.
6. **Compliance is a product surface, not a PDF**: consently.io's trio (overview → cookie manager → consent log) shows scan status, framework coverage and an evidence-grade log as one suite — the model for governance packs in the feature atlas.

## Variants & duplicates (recorded, not silently merged)
- Ethan Brooks student-risk screen ×3 (UIMG-010/012/014; 012 canonical).
- Payne Missione Rebates List ×4 states (015 filters-modal, 016 flat, 017 grouped, 020 ≈ 016).
- panze studio Project Dashboard: two complementary crops of one screen (024 + 026).
- Stellix Connections appears as settings screen (025) and tablet mockup (029).
- Kravio dashboard (038) + its own spec sheet (040) — the corpus's only font/colour-evidenced item.

## Rights note
These images were supplied by the repository owner in the commissioning conversation for study. The depicted designs belong to their respective creators; binaries are **not** republished in this public repository (hashes + analysis only, `data/assets.jsonl`) until the owner confirms redistribution rights per image.
