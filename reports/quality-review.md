# Quality review (2026-11-12)

Method: the rubric in `skill-improvements/review-rubric.md` applied to the corpus before publish; validation via `scripts/validate.py` (results recorded in `publish-receipt.md` after the publish run).

## Findings
1. **Strongest evidence**: S03 (code + executed build) and S09 (full visual study). Both carry complete evidence maps.
2. **Weakest evidence, honestly labelled**: Dribbble profile shots (title/tag level) and demo page internals (route/title level). 493 of 624 feature rows are UI_VISIBLE_ONLY — the corpus says so in the inventory itself rather than hiding it in prose.
3. **Corrected during the work** (kept visible in the records): POS variant count is 5, not the "POS 1–8" sometimes assumed for this template family (census-proven); S03 actions are 182 registrations / 175 unique, not a round "182 actions"; S01's profile is NOT fully enumerated (page 3 still paginates).
4. **Consistency checks passed**: 547/547 crawled pages have feature rows; coverage rows = shots 151 + S09 1 + pages 547 + work 19 + demos 13 + repo 1 + images 56 = 788.
5. **Known limitations**: feature module labels for demo routes are heuristic (filename-derived) — treat the module column as navigation aid, not taxonomy truth; the taxonomy sweep (`feature-atlas/module-taxonomy.yaml`) carries the considered verdicts. Explorer renders the first 400 filtered rows (full data in CSV/JSONL). Figma library not built (spec only). POS interaction matrix pending (resume item 1).
6. **Rights**: audit in `quality/rights-review/rights-audit-2026-11-12.md` — zero restricted binaries in tree; validate.py enforces it in CI.
