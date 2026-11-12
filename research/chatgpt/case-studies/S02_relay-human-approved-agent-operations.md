# GR8R Relay — Agent operations and human approval

- Source ID: S02
- Canonical reference: https://gr8rstudio.com/work/relay
- Source type: PORTFOLIO_CASE_STUDY
- Coverage: CASE_STUDY_PAGE_OBSERVED
- Inspected date: 2026-11-12
- Rights: REFERENCE_ONLY; no source screenshots, media or template code redistributed
- Runtime browser/cross-device testing: NOT_EXECUTED

## Scope and provenance
Portfolio states that Relay is Gr8r's own work, not client work.

## Layout geometry and visual evidence
Case study showcases a headline, hero visual, metrics/needs-attention overview, approval context screenshot and workflow canvas screenshots. Actual CSS dimensions NOT measured.

## Typography
Observed page text, font family and numerical computed typography NOT measured.

## Color / elevation
Marketing artwork not copied; no calibrated color sampling. An original semantic palette is stored separately.

## Component inventory
Agent activity feed, needs-attention list, workflow canvas with insert connection action, approval detail with approve/edit/reject, failed run detail and timeline.

## On-screen functional chain and uncertainty
Trigger (form / deal stage / schedule) -> agent research and updates -> risky step approval -> approved action or rejection -> run history. This is described by the case study, NOT verified runtime.

## Interaction census
| ID | Entry/control | Expected transition | Evidence |
| --- | --- | --- | --- |
| A01 | View attention queue | Open a specific run/approval | UI described, not executed |
| A02 | Approve/edit/reject | Role and side-effect validation not evidenced | UI described, not executed |
| A03 | Open failed run | Focus step which failed | UI described, not executed |

## UX critique and original adaptation
**Observed value:** Risk-aware escalation turns opaque autonomous work into inspectable operational decisions.

**Risk and evidence gaps:** Public portfolio illustration does not confirm live scheduler, queue semantics, external integrations, RBAC or durable audit service.

**Transferability:** ADOPT_AS_PRINCIPLE: keep actions and human approvals close to run context; IMPROVE: explicit separation of authority, idempotent integration and approvals record.

## Cross references
- Feature IDs: FEAT-0001, FEAT-0002, FEAT-0003, FEAT-0004, FEAT-0005
- Route index: ../source-route-graphs/discovered-routes-2026-11-12.jsonl
- Proposed automation system: ../automation-lab/workflow-engine-proposed-spec.md
- Original semantic tokens: ../reusable-ui/original-semantic-tokens/tokens.json

## Missing verification gates
- Exact on-screen viewport geometry, component coordinates, computed font values, responsive breakpoints and screenshots: NOT_MEASURED.
- Every button, focus, keyboard, validation, loading/empty/error, permission state and interaction: NOT_EXHAUSTIVELY_TESTED.
- Source licensing and redistribution rights: UNVERIFIED.
- User must not construe a conceptual future workflow as proof of functioning backend behavior.
