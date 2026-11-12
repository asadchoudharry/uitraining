# Proposed enterprise automation engine — original technical blueprint

**Evidence distinction:** S02 Relay publicly describes human approval of risky agent actions and run timelines. S05 Dreams ERP shows workflow/approval frontend routes. The architecture, API, data model and permission schemes below are entirely **PROPOSED**, not verified source backend behavior.

## Actors and guardrails

- Workflow author can draft, test and publish versioned definitions within tenant scope.
- Operator can inspect run steps, error codes, elapsed duration and redacted context.
- Approver can approve, reject, return or escalate only when tenant/role/segregation-of-duties policy permits it.
- Auditor can filter immutable event histories without viewing secrets.
- Live payments, external email sends and refunds must never execute from a mock workflow or unapproved action.

## Screens, actions and UI states

| Screen | Trigger/actions | Validations | States | Next |
| --- | --- | --- | --- | --- |
| Workflow register | New, Filter, Duplicate, Pause, Publish | Tenant, role, unique key | loading, empty, error, denied, conflict | Builder |
| Rule builder | Add trigger, condition, action, approval gate, Test | Node graph, connector grant, loop guard | draft, invalid, dirty, saved, conflict | Review |
| Publish review | Publish or return for editing | Permission, version checksum, review | waiting, approved, rejected, stale | Running |
| Run list | Filter, inspect, replay eligible run | Tenant, idempotency, policy | queued, running, waiting, failed, success | Run detail |
| Run detail | Expand step, retry from safe checkpoint | Role, replay eligibility | partial, retrying, timeout, cancelled | Resolution |
| Approval inbox | Claim, approve, reject, return | Maker-checker, time, role, ETag | pending, expired, conflict, success | Decision detail |
| Audit history | Search, correlate, export sanitized | Audit access scope and retention | redacted, loading, denied | Investigation |

## State machines

Definition: DRAFT → VALIDATED → PUBLISHED → PAUSED → ARCHIVED. An edit to a published rule creates a new immutable version.
Run: QUEUED → RUNNING → WAITING_APPROVAL / RETRY_SCHEDULED / SUCCEEDED / FAILED / CANCELLED.
Approval: PENDING → APPROVED / REJECTED / RETURNED / EXPIRED / REASSIGNED. An approval decision is append-only evidence.

## Proposed PostgreSQL entities

| Entity | Essential columns | Invariants |
| --- | --- | --- |
| WorkflowDefinition | id, tenant_id, key, status, owner_role | Unique tenant+key |
| WorkflowVersion | id, definition_id, schema_json, hash, published_at | Immutable once published |
| WorkflowRun | id, tenant_id, version_id, correlation_id, state, started_at | Tenant-scoped |
| RunStep | id, run_id, step_key, sequence, attempt, status, output_ref | Retry by idempotency |
| ApprovalPolicy | id, tenant_id, version, approver_role, quorum, sla | Versioned |
| ApprovalRequest | id, tenant_id, entity_ref, requester_id, policy_version, state | Cannot self-approve risky action |
| ApprovalDecision | id, request_id, principal_id, decision, reason, decided_at | Append-only |
| ConnectorGrant | id, tenant_id, scopes, vault_ref, revoked_at | Never return secret material |
| AuditEvent | id, tenant_id, principal_id, action, correlation_id, hash | Append-only |

## Proposed API contract

| Endpoint | Permission | Result / failure |
| --- | --- | --- |
| GET /api/v1/automations/definitions | automation.read | Filtered cursor list, 403 on denial |
| POST /api/v1/automations/definitions | automation.create | Draft + idempotency receipt |
| POST /api/v1/automations/definitions/{id}/validate | automation.edit | Field/node errors, never external side effects |
| POST /api/v1/automations/definitions/{id}/publish | automation.publish | New immutable version; 409 stale version |
| GET /api/v1/automations/runs/{id} | automation.runs.read | Redacted history only in tenant |
| POST /api/v1/automations/runs/{id}/retry | automation.runs.retry | Checkpoint replay and idempotency |
| GET /api/v1/approvals | approval.read | Approver-filtered inbox |
| POST /api/v1/approvals/{id}/decisions | approval.decide | 200 event on success; 409 decision conflict |
| GET /api/v1/audit-events | audit.read | Redacted cursor log |

## Transactional/security requirements

- Workflow versions and events are immutable; tenant isolation is enforced at service and database boundaries.
- Sensitive integrations use revocable scoped grants and vault references; OAuth tokens never appear in client JSON.
- Webhook ingress validates signatures, timestamps, size and replay windows.
- Retry uses idempotency keys and outbox delivery; uncertain external writes require reconciliation before replay.
- Escalation must fire exactly once per request/policy version; worker crashes must not create duplicate decisions.
- High-risk approvals require segregation of duties and reason text for overrides/rejection.

## Acceptance checks (PROPOSED, not executed)

1. A valid draft can validate without contacting effectful connectors.
2. Published definition remains immutable; editing creates version N+1.
3. Self-approval for high-risk payment returns server-side 403.
4. Two concurrent decisions yield one success and one 409 Conflict.
5. Expired connector grant blocks future writes without erasing audit evidence.
6. Replay of same step never double-creates invoice, email or payment.
7. Requests from tenant A cannot list or act on tenant B objects.
8. Waiting/failed/partial states are keyboard accessible on mobile and desktop.
