# Publish receipt (2026-11-12)

## Current status: PUBLISHED to branch `research/design-intelligence`

**355 of 356 corpus files are live on GitHub** on branch `research/design-intelligence` of `asadchoudharry/uitraining`, published 2026-11-12 by the Muse GitHub integration after the owner installed the App (see phase 2). A pull request to `main` accompanies this receipt; merging is the owner's decision. One file is held back by a GitHub platform restriction (see Residual).

### Verification (2026-11-12, after the final batch)
- Branch head after the last content batch: `f69c853a4c94a60a046ca7deed1364a7a5a03ba8` (this receipt's own commit follows it).
- Remote root listing shows all 22 expected top-level entries (README.md, AGENTS.md, CONTRIBUTING.md, LICENSING-NOTES.md, .gitignore, scripts/, data/, case-studies/, research/, visual-fidelity-atlas/, interaction-atlas/, feature-atlas/, automation-lab/, future-product-blueprints/, design-intelligence/, design-system/, reusable-ui/, skill-improvements/, apps/, assets/, quality/, reports/).
- Byte-identity spot proofs (git blob SHA, remote == local): `data/coverage.jsonl` `f2bd6346195d9097c6921008de5fb51d8455d982`; `data/pages.jsonl` `dbb9cb078c06ce201271caa807dbbb444f91ffac`.

### Residual (1 file not published)
- `.github/workflows/validate.yml` — GitHub refuses workflow-file writes from this integration on **both** write routes (Contents API: 403; Git Data API: any tree containing a workflow file fails with 403 "Resource not accessible by integration"). The integration lacks the **Workflows** permission. The file exists in the local tree and in the owner's bundle (`uitraining.bundle`); the owner can add it in one web-UI upload (branch `research/design-intelligence` → `.github/workflows/` → Add file). Until then, CI validation runs locally via `python3 scripts/validate.py` (0 errors, 0 warnings).

### Repository state note
- `main` advanced independently during the publish window with the owner's own commits (a parallel ChatGPT-produced corpus under `research/`, current head verified separately). This branch forked from the owner's init commit `8ebe430054fc694120f875063c04fd7862c1b065`. The PR diff is therefore relative to that base; overlapping paths (notably `README.md`, `research/`) may conflict at merge time. **No merge is performed by the agent.**

## Phase 1 — blocked attempts (recorded, not retried blindly)
| # | Action | Tool route | Result |
|---|---|---|---|
| 1 | Create branch `research/design-intelligence` from `main` | GitHub integration `create_branch` | **403 "Resource not accessible by integration"** (POST /git/refs) |
| 2 | Push foundation files | GitHub integration `push_files` | **403 "Resource not accessible by integration"** (POST /git/trees) |
| 3 | Fork `asadchoudharry/uitraining` | GitHub integration `fork_repository` | **403 "Resource not accessible by integration"** (POST /forks) |
| 4 | Fork `gr8rstudio/gr8r-studio` (S03 reference fork) | GitHub integration `fork_repository` | **403 "Resource not accessible by integration"** (POST /forks) |
| 5 | Create branch (retry after owner added `s22benlg1m01140-sudo` as collaborator, 2026-11-12 ~12:22 PKT) | GitHub integration `create_branch` | **403 "Resource not accessible by integration"** (POST /git/refs) |
| 6 | List collaborators (diagnostic) | GitHub integration `list_repository_collaborators` | **403 "Resource not accessible by integration"** (GET /collaborators) |

Root cause of phase 1 (proven by attempt 6): the Muse GitHub **App was not installed on the `asadchoudharry` account at all** — public reads worked only because the repository is public, and a user-level collaborator invitation cannot unblock an uninstalled App.

## Phase 2 — unblock and publish (2026-11-12 ~12:29 PKT onward)
- The owner installed/authorised the App — listed on GitHub as **Meta Muse AI** (slug `meta-muse-ai`) — on `asadchoudharry`, selecting this repository. Collaborators read immediately succeeded (owner = admin; `s22benlg1m01140-sudo` = write collaborator).
- Branch `research/design-intelligence` created at `8ebe4300` (verified via `list_branches`).
- **Contents-API phase (70 files):** the Git Data route still failed at first, so files were written individually via `create_or_update_file` (grouped commit messages), including a permission probe file that was created and deleted again (commits `da946901`, `d9323e31`). One loop crash (subprocess timeout) and one runtime restart interrupted this phase; the resumable progress log (`push-progress.jsonl`, held outside git) preserved every confirmed file. This phase is why the branch history contains many small commits; the PR can be squash-merged by the owner if a single-commit history is preferred.
- **Diagnosis that unlocked bulk publish:** batches containing `.github/workflows/validate.yml` fail tree creation with 403 on the Git Data route as well (Workflows permission again); a 5-file test batch without it succeeded immediately (head `56f94259090b4aaa2be57b3f42df12be4a60787f`).
- **Bulk phase (284 files)** via `push_files` snapshot batches, heads in order: `cc00b169af15cf51277d273b72c552395d04d81a` (100 files) → `d6dc643c06e6880fd393ae8baace5497712437cc` (100 files, incl. the two large data ledgers that exceed single-call argument limits) → `2d61838bf20ef03c7dcaab2c8518da39f8969e97` (28) → `dadb06d515be8e3954eff9b153b738b92729cc3f` (28) → `f69c853a4c94a60a046ca7deed1364a7a5a03ba8` (28). One 84-file attempt timed out at tree creation ("input too large") and was re-split into the three 28-file batches above; the failed attempt created no commit (head verified unchanged before retry).
- This receipt is the final publish commit.

## Local package (unchanged)
- The full repository tree (356 files) with local Git history lives in the owner's workspace with a Git bundle (`uitraining.bundle`) and tarball (`uitraining-research-branch.tar.gz`) as offline fallbacks.
- Local validation: `python3 scripts/validate.py` → 0 errors, 0 warnings.
