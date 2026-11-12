# Dreams Construction — Projects, supply, field and controls

- Source ID: S04
- Canonical reference: https://dreamserp.dreamstechnologies.com/construction/tailwind/index.html
- Source type: FRONTEND_TEMPLATE
- Coverage: DASHBOARD_AND_INDEXED_ROUTES
- Inspected date: 2026-11-12
- Rights: REFERENCE_ONLY; no source screenshots, media or template code redistributed
- Runtime browser/cross-device testing: NOT_EXECUTED

## Scope and provenance
Construction demo has project, site, asset, supply, expense, inspection and notifications navigation.

## Layout geometry and visual evidence
Public dashboard contains compact global search, project switcher, quick actions and project-level dashboard widgets. No DOM-measured width/pixel dimensions.

## Typography
Not measured; CSS font assumptions must remain unverified until browser inspector access.

## Color / elevation
Source logo and colors intentionally not reproduced in this original case study.

## Component inventory
Project portfolio KPI, site selector, notification flyout, quick create menu, project list, material request review, RFQ comparison, inspection register, document library, equipment and fleet.

## On-screen functional chain and uncertainty
Proposed operational chain (not confirmed backend): site demand -> material request -> procurement -> quotation review -> PO -> issue to site -> evidence. Source demo provides UI labels for several steps.

## Interaction census
| ID | Entry/control | Expected transition | Evidence |
| --- | --- | --- | --- |
| A01 | Project switcher | Change contextual filters | UI visible, interaction not tested |
| A02 | Create purchase order | Opens order form | Not tested |
| A03 | Review material request | Approval/issue state flow proposed | Backend not verified |

## UX critique and original adaptation
**Observed value:** Hierarchy spans executive portfolio, site-level task and finance views with repeated project context.

**Risk and evidence gaps:** Demo navigation and screenshot labels cannot prove real approvals, cost accounting, GPS telemetry or stock posting.

**Transferability:** ADOPT_AS_PRINCIPLE: preserve project/site context across cross-functional workflows; IMPROVE: transactional status contracts, guard rails and realistic empty/error states.

## Cross references
- Feature IDs: FEAT-0019, FEAT-0020, FEAT-0023, FEAT-0024, FEAT-0025, FEAT-0026, FEAT-0037
- Route index: ../source-route-graphs/discovered-routes-2026-11-12.jsonl
- Proposed automation system: ../automation-lab/workflow-engine-proposed-spec.md
- Original semantic tokens: ../reusable-ui/original-semantic-tokens/tokens.json

## Missing verification gates
- Exact on-screen viewport geometry, component coordinates, computed font values, responsive breakpoints and screenshots: NOT_MEASURED.
- Every button, focus, keyboard, validation, loading/empty/error, permission state and interaction: NOT_EXHAUSTIVELY_TESTED.
- Source licensing and redistribution rights: UNVERIFIED.
- User must not construe a conceptual future workflow as proof of functioning backend behavior.
