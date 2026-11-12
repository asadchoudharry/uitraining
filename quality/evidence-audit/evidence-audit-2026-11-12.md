# Evidence audit — 2026-11-12

Spot checks performed before publish:
- S03 build claims re-run locally (install/lint/format/build) — outputs in the case study §13.
- S05 workflow facts re-extracted from the live pages twice (index probe + dedicated fetch) with identical columns/rows.
- Crawl totals reconciled three ways: crawler summary (53/231/263), `data/pages.jsonl` line counts, feature-inventory URL coverage (547/547 pages have feature rows after the collision fix).
- UIMG duplicate pair (UIMG-046 = UIMG-052) confirmed by SHA-256 equality and by the visual lane independently.
- S09 metadata cross-read: browser report (designer Jeremy Blaze, palette, tags) vs the Dribbble lane's blocked record — the lane's ACCESS_BLOCKED stands for its route; the case study records the successful live-browser route.
