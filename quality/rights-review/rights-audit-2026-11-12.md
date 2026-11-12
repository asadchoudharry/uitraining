# Rights audit — 2026-11-12 (pre-publish)

- Repository tree scanned for binaries: only HTML/MD/JSON/JSONL/CSS/CSV/YAML/MMD text. No third-party images, page source, fonts or code committed. `assets/licensed-only/` empty.
- S03: no LICENSE upstream → no code reproduced; quotations limited to short identifiers/values required by the analysis (file paths, action names, token values).
- S04/S05/S06: page HTML held outside git during analysis (two S05 workflow pages), used for structural extraction, then discarded from the work area; the repository carries URLs, titles, and extracted facts only.
- S10: binaries withheld; hashes + analysis published.
- Dribbble: no images downloaded by any lane (search/fetch lanes collected metadata; the live-browser lane viewed S09 without saving).
- Validation: `scripts/validate.py` enforces the binary rule in CI.
