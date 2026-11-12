# Dreams ERP — Document workflows and approval surfaces

- Source ID: S05
- Canonical reference: https://dreamserp.dreamstechnologies.com/tailwind/document-workflows.html
- Source type: FRONTEND_TEMPLATE
- Coverage: INDEXED_WORKFLOW_ROUTES
- Inspected date: 2026-11-12
- Rights: REFERENCE_ONLY; no source screenshots, media or template code redistributed
- Runtime browser/cross-device testing: NOT_EXECUTED

## Scope and provenance
Related routes include workflow approvals, requests, approval levels, workflow actions/audit and document workflows.

## Layout geometry and visual evidence
Enterprise sidebar, organization/language switcher and dense navigation visible on homepage; detailed workflow page layout sizes not captured.

## Typography
Not measured and no source font claim.

## Color / elevation
No copyrighted or source-specific style copied into training repo.

## Component inventory
Workflow register, approval levels, escalation interval control, active status, request queue and audit-actions screen. These are page/label-level observations.

## On-screen functional chain and uncertainty
Document draft -> submit -> configured approval level(s) -> approve/reject/return -> final disposition and audit is an ORIGINAL PROPOSED interaction model; source backend not verified.

## Interaction census
| ID | Entry/control | Expected transition | Evidence |
| --- | --- | --- | --- |
| A01 | Open Document Workflows | List workflow definitions | Route indexed |
| A02 | Inspect approval levels | Configure level roles | Screen indexed, actual control not tested |
| A03 | Review workflow action audit | Inspect decision evidence | Route indexed, backend unverified |

## UX critique and original adaptation
**Observed value:** Clear separation between definitions, requests, approval levels and action history as distinct user jobs.

**Risk and evidence gaps:** Do not infer trigger node editor, condition scripting, policy inheritance, maker-checker or committed data from menu routes alone.

**Transferability:** ADOPT_AS_PRINCIPLE: role-specific workflow navigation. IMPROVE: versioning, safe test mode, traceable decision chain, conflict behavior.

## Cross references
- Feature IDs: FEAT-0040, FEAT-0041, FEAT-0042, FEAT-0043, FEAT-0044
- Route index: ../source-route-graphs/discovered-routes-2026-11-12.jsonl
- Proposed automation system: ../automation-lab/workflow-engine-proposed-spec.md
- Original semantic tokens: ../reusable-ui/original-semantic-tokens/tokens.json

## Missing verification gates
- Exact on-screen viewport geometry, component coordinates, computed font values, responsive breakpoints and screenshots: NOT_MEASURED.
- Every button, focus, keyboard, validation, loading/empty/error, permission state and interaction: NOT_EXHAUSTIVELY_TESTED.
- Source licensing and redistribution rights: UNVERIFIED.
- User must not construe a conceptual future workflow as proof of functioning backend behavior.
