# AGENTS.md — working rules for this repository

## Mission
Maintain an evidence-backed design-intelligence corpus. The corpus is only useful while its evidence discipline holds; a smaller true corpus beats a larger invented one.

## Non-negotiables
1. **Evidence levels are mandatory.** Every factual claim about a source carries one of: CODE_VERIFIED, RUNTIME_OBSERVED, OFFICIALLY_DOCUMENTED, UI_VISIBLE_ONLY, INFERRED_PRODUCT_LOGIC, NEW_PROPOSAL, UNVERIFIED_OR_BLOCKED. A demo screen is not a backend. A route is not a workflow.
2. **Observed vs proposed never mix.** Proposals live in `automation-lab/` (labelled), `future-product-blueprints/`, PROPOSED journeys and NEW_PROPOSAL inventory rows. When a proposal generalises a source, cite the source *and* its evidence level.
3. **Rights gate before commit.** No third-party screenshots, page source, artwork, fonts or code unless a licence permitting redistribution is recorded in `LICENSING-NOTES.md` / `data/assets.jsonl`. No LICENSE file upstream = no republication. User-supplied images: hashes + analysis only until the owner confirms redistribution rights per image.
4. **Coverage ledger completeness.** Every discovered item ends in exactly one status: VERIFIED_AND_STUDIED, DOCUMENTED_ONLY, RIGHTS_RESTRICTED, ACCESS_BLOCKED, OUT_OF_SCOPE_WITH_REASON, DUPLICATE. Never delete a row to make coverage look better; mark it.
5. **Numbers must be reproducible.** Counts in README/reports come from `data/*.jsonl` and `feature-atlas/*.csv`. If you change data, regenerate the dependent counts in the same commit.
6. **Unknowns are data.** Use `null`, `NOT_FOUND_IN_SOURCE`, `NOT_VERIFIED`, `TARGET_STATUS_UNVERIFIED`. Never fill a gap with a plausible value. No target product was audited in this mission — do not write that a product "lacks" a feature.
7. **Demos are other people's systems.** Non-destructive, read-only interaction only: no orders, payments, registrations, or mutations on third-party demos. Respect robots.txt and bounded crawl rates.

## Conventions
- IDs: sources `S01…S10`; pages `S0x-Pnnn`; shots `SHOT-nnn`; images `UIMG-nnn`; features `F-nnnn`; passports `FP-nnn`.
- Case studies follow the 14-section schema (§ identity … § rights) with YAML/JSON frontmatter.
- Tokens: components reference `design-system/tokens/tokens.json` names; no hardcoded hex in specs.
- Validation: run `python3 scripts/validate.py` before committing (also runs in CI).

## Publishing
Work lands on `research/design-intelligence` via pull request to `main`. No force-push, no direct commits to `main` beyond the initial foundation, no merging without the owner's approval. Forks are references, not rights.
