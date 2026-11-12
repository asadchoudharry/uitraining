# Coverage summary (2026-11-12)

## Scoreboard (all counts reproducible from `data/` + `feature-atlas/`)
| Metric | Count |
|---|---|
| Sources registered | 10 |
| Coverage-ledger rows | 788 |
| Demo routes verified (HTTP 200) | 547 (S04 53, S05 231, S06 263) |
| Dribbble shot records | 151 (S01 72, S07 26, S08 52, S09 1) — 110 in scope incl. S09 |
| Studio case studies opened | 19 / 19 |
| Linked demos inspected | 13 / 13 live (all SPA) |
| GitHub repos cloned + built | 1 (S03: lint PASS, format PASS, build PASS) |
| User images inspected | 56 / 56 (54 unique) |
| Case-study files | 233 |
| Features inventoried | 624 |
| Full feature passports | 5 (FP-001…FP-005) + structured records for all 624 |
| Screen specs | S09 setup, S05 document-workflows, S10 Fulcrum, S10 Nextstep (+56 per-image case files) |
| Dashboard archetypes | 11 |
| Proposed automation examples | 5 (A–E, labelled PROPOSED_EXAMPLE) |
| Rights-restricted binaries committed | 0 |

## Status by source
- S01 DOCUMENTED_ONLY — 72 shots (67 in scope); **pagination incomplete** (profile continues past page 3).
- S02 VERIFIED_AND_STUDIED — 19/19 cases; demos DOCUMENTED_ONLY at entry/route level (2 sign-in gated).
- S03 VERIFIED_AND_STUDIED — code-level, build-executed. Rights-restricted for republication.
- S04/S05/S06 DOCUMENTED_ONLY — route-complete censuses; deep structure study for S05's workflow pair; per-page behaviour unverified (static templates).
- S07 DOCUMENTED_ONLY — 26 records (13 in scope; 7 snippet-only).
- S08 DOCUMENTED_ONLY — 52 records (29 in scope; 14 snippet-only; 12 unnamed grid slots not counted).
- S09 VERIFIED_AND_STUDIED — via live browser after two fetch routes failed.
- S10 VERIFIED_AND_STUDIED — all 56 inspected; binaries withheld (rights).

## Resume checkpoint (exact next actions, in order)
1. **POS interaction matrix**: open S06 `pos.html`…`pos-5.html` + `pos-orders/settings`; record per-variant catalog/cart/discount/checkout controls into `interaction-atlas/ui-controls.jsonl` and complete the E09 comparison in the S06 case study §8.
2. **S01 pagination**: continue profile enumeration from page 4 until the grid ends; add SHOT rows + case files; update this scoreboard.
3. **S05/S06 deep pages**: structure-extract one page per module family (fields/labels like the workflow pair) and upgrade those pages from DOCUMENTED_ONLY.
4. **Figma library**: build from `reusable-ui/figma-handoff/figma-library-spec.md`; record the file URL in `reports/publish-receipt.md` only when it exists.
5. **S10 rights**: owner confirms redistribution per image (or per product family) → move cleared binaries to `assets/licensed-only/` with licence rows.
6. **GR8R runtime pass**: drive the built S03 app screen-by-screen and attach interaction notes to `quality/interactions/`.
