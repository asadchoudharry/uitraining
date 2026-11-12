# Contributing

1. Read `AGENTS.md` first — evidence levels, the observed/proposed firewall and the rights gate are the price of admission.
2. Branch from `main` (`research/<topic>`), keep commits logical (one source or one system per commit where practical), and open a PR. Do not merge your own PR without owner approval.
3. Before pushing: run `python3 scripts/validate.py` and fix everything it flags (JSON/JSONL parse, frontmatter presence, internal link resolution, forbidden-asset scan).
4. New source? Add it to `data/sources.yaml`, open coverage rows for every discovered item, and add its licence position to `LICENSING-NOTES.md` in the same PR.
5. New claim about an existing source? Update the case study's evidence map with the date and method; if the claim's level changes, update `data/coverage.jsonl` and the README scoreboard in the same commit.
6. Screenshots: only into `assets/licensed-only/` with a licence recorded in `data/assets.jsonl`. Otherwise describe, measure and link — never embed.
