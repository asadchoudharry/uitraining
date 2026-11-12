# Capture settings & method notes

- Route crawls (S04/S05/S06): bounded BFS from the seed page, same-origin + path-prefix scope, ~0.15s politeness delay plus natural fetch latency, single agent string identifying the research. Titles + status recorded; page bodies were NOT archived into this repository (rights). Working HTML for the two S05 workflow pages was held outside git during analysis and discarded after extraction.
- GR8R (S03): `git clone` at pinned commit; build/test executed locally (Node 24): install, ESLint, Prettier check, Vite build — logs summarised in the case study.
- Dribbble profiles: text extraction of profile grids (titles + author tags). Per-shot canonical URLs were signup-gated in extraction; discovery URLs are recorded instead (see discovery log limitations).
- S09: live-browser visual inspection (page + enlarged view), 2026-11-12 ~11:48–11:50 PKT, after curl (HTTP 202/0 bytes) and text extraction both failed. Full study: `s09-live-browser-study.md` in this folder.
- User images (S10): every file opened individually; dimensions/SHA-256 computed locally; colour/geometry statements in case studies are labelled ESTIMATED.
- No screenshots of third-party surfaces are stored in this repository.
