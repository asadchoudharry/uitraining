# WFL-004 — Construction inspection to corrective action closure

**Classification:** original implementation-ready proposal, not observed third-party backend behavior.
**Source pattern references:** S04 / site-inspections.html / FEAT-0027; S04 / documents.html / FEAT-0023
**Actors:** Site Inspector, Site Engineer, Safety Manager, Project Manager, Auditor
**User goal:** Raise evidence-backed site inspection findings, assign corrective actions and close after independent verification.
**Entry:** Construction > Sites > Inspections > Schedule

## Screen-by-screen specification
| Screen ID | Name | Visible controls and content | Mandatory non-happy-path states |
| --- | --- | --- | --- |
| SCR-301 | Inspection calendar | Site, type, date, assignee, checklist status | loading, empty, filtered-empty, denied, stale, error, success |
| SCR-302 | Field inspection | Offline checklist, camera evidence, asset/site context | loading, empty, filtered-empty, denied, stale, error, success |
| SCR-303 | Finding detail | Severity, evidence, affected area, owner and due date | loading, empty, filtered-empty, denied, stale, error, success |
| SCR-304 | Corrective action | Response plan, tasks, proof of completion | loading, empty, filtered-empty, denied, stale, error, success |
| SCR-305 | Verification | Independent verifier, accepted/returned conclusion | loading, empty, filtered-empty, denied, stale, error, success |
| SCR-306 | Site compliance dashboard | Overdue items, trend, traceability and closure proof | loading, empty, filtered-empty, denied, stale, error, success |

## Interaction contracts
| Action ID | Control | Actor | Authorization and validation | On success | Error recovery |
| --- | --- | --- | --- | --- | --- |
| ACT-301 | Schedule | Safety Manager | Site, checklist, assignee, date valid | inspection scheduled | duplicate schedule detection |
| ACT-302 | Record evidence | Inspector | File type/size and scan | secure evidence hash stored | offline replay/conflict |
| ACT-303 | Raise finding | Inspector | Severity, location and non-empty finding | assigned and due | 422 field validation |
| ACT-304 | Submit correction | Assignee | Evidence attached and mitigation checked | verification pending | invalid evidence/permission |
| ACT-305 | Verify closure | Independent Verifier | Cannot verify own correction; policy version | closed and immutable closure event | 403 self-verification, 409 version conflict |

## State graph
SCHEDULED → IN_PROGRESS → SUBMITTED → FINDING_OPEN → ACTION_IN_PROGRESS → READY_FOR_VERIFICATION → RETURNED_FOR_REWORK → VERIFIED_CLOSED → CANCELLED (the actual branches and guards are defined in implementation tests; arrows are not all permitted transitions).

## Proposed data model
Site, Inspection, ChecklistItem, Finding, CorrectiveAction, EvidenceObject, Verification, AuditEvent

## Proposed endpoints
- GET /api/v1/sites/{id}/inspections
- POST /api/v1/inspections
- POST /api/v1/inspections/{id}/findings
- POST /api/v1/findings/{id}/corrective-actions
- POST /api/v1/findings/{id}/verification

## Permission and consistency rules
- Every object is tenant-scoped; server-side authorization is mandatory on read and write, independent of frontend affordances.
- High-risk writes require idempotency keys, optimistic concurrency and an append-only audit event.
- Unknown external outcomes require reconciliation, not blind retry.
- Unauthorized state must be explicit; disabled buttons do not imply secure authorization.
- Every error preserves unsaved context and provides a user-visible retry or remediation path.

## Acceptance test dossier
1. Finding cannot close without verification
2. Original evidence is hash-preserved after modifications
3. Inspector cannot close their own critical finding
4. Offline evidence upload retries do not duplicate attachments
5. Changing finding severity requires audit reason
6. Overdue escalation fires at policy-defined cadence

## Scope and caveats
Template navigation does not establish a real construction compliance backend.
- Implementation status: SPECIFIED only. Figma-linked reference screen covers a generic approval UI, not all these specific workflow screens.
- Tests are acceptance proposals; not executed backend checks.
