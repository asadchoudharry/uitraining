# Skills improvement proposals for enterprise experience work

Status: RECOMMENDATIONS_ONLY — no installed Skill was modified. Improvements require separate Skill governance/review.

| Proposal | Failure mode discovered | Required future Skill output | Acceptance evidence |
| --- | --- | --- | --- |
| Evidence-first source browser | Indexed links mistaken for studied screens | URL/route registry with discovered vs verified split | Every claim linked to screenshot/route/code |
| Source-code UI archeologist | Navigation names mistaken for backend features | SOURCE_IMPLEMENTED/UI_VISIBLE_ONLY classification | Action→state→API trace or explicit unknown |
| Screen interaction ledger | Screenshot-only research misses form states | Control/action/state matrix with keyboard/validation | Browser replay traces |
| Copyright-aware asset intake | Public artwork mistakenly redistributed | License manifest and gated screenshot output | Approval receipt / no unlicensed binaries |
| Enterprise action-contract author | Missing conflict/authorization outcomes | Actor, permission, idempotency, audit, rollback | Contract tests in CI |
| Original token-to-Figma kit | Inconsistent bespoke shell styling | One canonical token JSON with Figma variable binds | Theme parity checks |
| Dense dashboard mobile QA | Desktop patterns break mobile and RTL | Breakpoint and writing-direction acceptance table | Browser screenshots and keyboard tests |
| Multi-agent merge governance | One agent overwrites other tree | Namespaced workstream + signed merge plan | Branch diff / no unintended paths |

## Proposed source-to-product handoff checklist
1. Exactly which source and source version supports the observation?
2. Was the UI directly seen, source code inspected, or capability merely described?
3. Is the artifact licensed for reuse, or is this clean-room design?
4. Does each action have actor, guard, validation, state transition, API and failure behavior?
5. Are mobile, keyboard, RTL, empty/error/unauthorized states considered and actually tested?
6. Can another engineer reproduce the result from IDs, source links, token file and tests?

## Cross-agent safeguards
ChatGPT owns research/chatgpt/ on main. Muse owns its separate tree. Do not merge by copying whole subtrees. Use per-file provenance and a conflict matrix; preserve Muse's independent source files and commit history.
