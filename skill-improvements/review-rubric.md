# Independent review rubric (used for this corpus; PROPOSED for reuse)

Score each case study / spec 0–2 per line; anything at 0 blocks "VERIFIED" status.

1. Identity complete (ID, URL, author, date, version/commit where applicable).
2. Evidence level stated and honest (no UI-only claim dressed as behaviour).
3. Layout claims measured (DOM/code) or labelled ESTIMATED.
4. Typography identified with confidence, or explicitly NOT_MEASURED.
5. Colours measured or labelled ESTIMATED; palette roles named.
6. Workflow claims trace to an interaction, code path, or are labelled PROPOSED.
7. Failure/empty/permission states addressed.
8. Transferability judged (ADOPT_AS_PRINCIPLE / IMPROVE / AVOID / NOT_APPLICABLE) with a reason.
9. Rights: attribution present; no unlicensed binary/code in the repo.
10. Cross-links resolve (source → screen → feature → component → test).

Red-team prompts (from the Independent UX Critic role): What would break this pattern at 10× data volume? Which step assumes a permission the actor may not hold? What does the design hide that an auditor needs? Where does the demo's sample data flatter the design?
