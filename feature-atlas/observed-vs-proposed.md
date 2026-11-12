# Observed vs proposed — the corpus firewall

- **Observed (all levels)**: 616 of 624 feature rows carry a source evidence level (CODE_VERIFIED 33, OFFICIALLY_DOCUMENTED 19, UI_VISIBLE_ONLY the remainder incl. all 547 demo routes).
- **Proposed**: 8 rows are NEW_PROPOSAL (workflow engine, maker-checker documents, multi-tenant provisioning, API/webhook management, import wizard, custom fields/form builder, scheduled reports, AI document summarisation) plus everything in `automation-lab/` beyond the S05 register facts, `future-product-blueprints/future-original-product-concepts.md`, and the PROPOSED journey for S09.
- **Rule**: a proposed item never inherits a source's credibility. Where a proposal generalises a source pattern, the source is named as *inspiration* with its evidence level, e.g. the engine spec generalises FP-001 (UI_VISIBLE_ONLY).
- **Target status**: no target product was supplied for a gap audit in this mission, so every row is `NOT_AUDITED` / `TARGET_STATUS_UNVERIFIED` per E05 — nothing in this repository claims a named product "lacks" a feature.
