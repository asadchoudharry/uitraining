# WFL-001 — Role-scoped document approval

**Classification:** original implementation-ready proposal, not observed third-party backend behavior.
**Source pattern references:** S05 / document-workflows.html / FEAT-0040; S02 / relay / FEAT-0002
**Actors:** Requester, Department Approver, Finance Controller, Auditor
**User goal:** Request a policy-controlled sign-off with observable review, conflict and audit states.
**Entry:** Workspace > Approvals > Create request

## Screen-by-screen specification
| Screen ID | Name | Visible controls and content | Mandatory non-happy-path states |
| --- | --- | --- | --- |
| SCR-001 | Approval inbox | Search/filter/claim requests; list status, amount, SLA and requester | loading, empty, filtered-empty, denied, stale, error, success |
| SCR-002 | Request detail | Evidence, version, decision history, policy and decision | loading, empty, filtered-empty, denied, stale, error, success |
| SCR-003 | Rejection modal | Require rejection reason, impact confirmation and a clean focus return | loading, empty, filtered-empty, denied, stale, error, success |
| SCR-004 | Workflow designer | Define roles, amount thresholds, approval sequences and publish review | loading, empty, filtered-empty, denied, stale, error, success |
| SCR-005 | Audit timeline | Immutable decision record and correlated events | loading, empty, filtered-empty, denied, stale, error, success |

## Interaction contracts
| Action ID | Control | Actor | Authorization and validation | On success | Error recovery |
| --- | --- | --- | --- | --- | --- |
| ACT-01 | Submit | Request owner | All required fields valid and document exists | 201 PENDING | 400 field errors; 403 permission |
| ACT-02 | Claim | Eligible approver | Same tenant, quorum policy, not requester | 200 CLAIMED | 409 already claimed |
| ACT-03 | Approve | Eligible approver | Document checksum, if-match version, maker-checker | 200 decision event | 409 stale; 403 self-approval |
| ACT-04 | Reject | Eligible approver | Nonempty reason and valid decision version | 200 REJECTED | 422 reason absent; 409 stale |
| ACT-05 | Return | Eligible approver | Action permission and feedback provided | 200 RETURNED | 409 stale |
| ACT-06 | Cancel | Requester or admin | Allowed only before final decision | 200 CANCELLED | 409 final state |

## State graph
DRAFT → SUBMITTED → PENDING → CLAIMED → APPROVED → REJECTED → RETURNED → EXPIRED → CANCELLED (the actual branches and guards are defined in implementation tests; arrows are not all permitted transitions).

## Proposed data model
ApprovalRequest, ApprovalPolicy, ApprovalDecision, DocumentVersion, AuditEvent

## Proposed endpoints
- GET /api/v1/approvals
- GET /api/v1/approvals/{id}
- POST /api/v1/approvals
- POST /api/v1/approvals/{id}/decisions
- GET /api/v1/audit-events?entity=approval

## Permission and consistency rules
- Every object is tenant-scoped; server-side authorization is mandatory on read and write, independent of frontend affordances.
- High-risk writes require idempotency keys, optimistic concurrency and an append-only audit event.
- Unknown external outcomes require reconciliation, not blind retry.
- Unauthorized state must be explicit; disabled buttons do not imply secure authorization.
- Every error preserves unsaved context and provides a user-visible retry or remediation path.

## Acceptance test dossier
1. Requester cannot approve own high-risk transaction
2. Duplicate click on Approve yields a single decision
3. Stale ETag returns 409 and refresh affordance
4. Missing evidence blocks submit with field-specific remediation
5. Expiry produces one escalation event

## Scope and caveats
No live payment or outbound messaging without separate authorization.
- Implementation status: SPECIFIED only. Figma-linked reference screen covers a generic approval UI, not all these specific workflow screens.
- Tests are acceptance proposals; not executed backend checks.
