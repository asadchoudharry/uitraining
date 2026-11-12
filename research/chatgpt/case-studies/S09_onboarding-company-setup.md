# Dribbble Onboarding & Company Setup — Static visual

- Source ID: S09
- Canonical reference: https://dribbble.com/shots/26442731-Onboarding-Company-Setup
- Source type: STATIC_DESIGN_SHOT
- Coverage: PAGE_TEXT_AND_IMAGE_LINK_OBSERVED_VISUAL_NOT_MEASURED
- Inspected date: 2026-11-12
- Rights: REFERENCE_ONLY; no source screenshots, media or template code redistributed
- Runtime browser/cross-device testing: NOT_EXECUTED

## Scope and provenance
Shot attributed to Jeremy Blaze for Never Before Seen. Public page lists palette colors including #EEEEEE, #0F1011, #D67035.

## Layout geometry and visual evidence
One shot image plus related Dribbble links observed in page; inner screen pixel geometry not measured, no claim of steps or form fields as observed.

## Typography
Unknown until direct visual inspection; source color tags are metadata, not full product token spec.

## Color / elevation
Metadata-listed colors only; no brand copying. Independently authored onboarding component recipe uses different semantic colors.

## Component inventory
The source is a static onboarding design reference. Every uninspected widget and interaction remains NOT_VERIFIED.

## On-screen functional chain and uncertainty
ORIGINAL PROPOSAL: create account -> organization identity -> country/tax -> industry -> users/roles -> review -> provisioning -> first dashboard, with save/resume, retries and rollback.

## Interaction census
| ID | Entry/control | Expected transition | Evidence |
| --- | --- | --- | --- |
| A01 | Next step | Advance on valid fields | PROPOSED |
| A02 | Back | Preserve entered values | PROPOSED |
| A03 | Provision organization | Idempotent tenant creation | PROPOSED |

## UX critique and original adaptation
**Observed value:** Useful visual theme for low-friction company setup research; exact interface efficiency is not yet measured.

**Risk and evidence gaps:** Do not attribute described form screens and completion flows to the static shot.

**Transferability:** ADOPT_AS_PRINCIPLE: guided organization setup, review before provisioning; IMPROVE: accessible step controls, resumable drafts, strong validation.

## Cross references
- Feature IDs: FEAT-0071
- Route index: ../source-route-graphs/discovered-routes-2026-11-12.jsonl
- Proposed automation system: ../automation-lab/workflow-engine-proposed-spec.md
- Original semantic tokens: ../reusable-ui/original-semantic-tokens/tokens.json

## Missing verification gates
- Exact on-screen viewport geometry, component coordinates, computed font values, responsive breakpoints and screenshots: NOT_MEASURED.
- Every button, focus, keyboard, validation, loading/empty/error, permission state and interaction: NOT_EXHAUSTIVELY_TESTED.
- Source licensing and redistribution rights: UNVERIFIED.
- User must not construe a conceptual future workflow as proof of functioning backend behavior.
