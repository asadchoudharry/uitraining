# Proposed workflow & approval engine — original specification (NEW_PROPOSAL)

This is an **original** design informed by the corpus's gaps (see `document-workflow-deep-dive.md`). Nothing here is claimed to exist in any source. It generalises S05's observed minimal record (module + levels + escalation + active) into an implementable engine.

## 1. Entities
- **Workflow**: `id, tenant_id, name, owner_id, module, description, status (draft|testable|pending_approval|active|paused|archived), version, schema_version, activation_window {starts_at, ends_at}, created_by/at, updated_by/at`. Every edit while active creates a new `version`; runs pin the version they started with.
- **Trigger**: `workflow_id, event_type (record.created|updated|deleted|field.changed|status.transitioned|schedule.cron|date.proximity|email.received|webhook.received|file.event|approval.responded|stock.moved|payment.event|integration.event), source, filter (condition tree), cadence, payload_schema, dedupe_key_template`.
- **ConditionTree**: typed predicates `{field, operator (eq|neq|gt|gte|lt|lte|in|contains|is_null|is_not_null), value}` grouped by AND/OR nodes (max depth 4), null semantics = predicate false unless operator is an explicit null check; field permissions are checked at publish time (a rule may not read fields its owner cannot see).
- **ActionStep**: `order, parallel_group, type (assign|set_status|create_task|generate_document|notify_inapp|notify_email|notify_sms|webhook|start_approval|update_record|open_ticket|comment|enqueue_report|create_transaction), input_mapping, retry_policy {max_attempts, backoff}, idempotency_key_template, timeout_s, side_effect_class (none|internal|external|financial), compensation (none|manual|automatic_ref)`.
- **ApprovalStep**: `stage_no, assignee_policy (user|role|manager_chain|dynamic_amount_threshold|quorum|unanimous|parallel_set), delegated_to, due_in_hours, business_calendar_id, decision_options (approve|reject|return), escalation {after_hours, to_policy, repeat}`.
- **Run**: `workflow_run (id, workflow_id, version, trigger_event_id, status pending|running|awaiting_human|succeeded|failed|cancelled, started_at, finished_at)`, `step_run`, `approval_decision (actor, decision, reason, at)`, `error (code, message, retryable)`, `audit_event`, `notification`, `webhook_delivery (attempts, last_status)`.

## 2. State machines
- Workflow: `Draft → Testable → Pending Approval → Active → Paused → Archived` (Paused → Active allowed; Archived is terminal; publishing an automation itself requires approval when it contains financial/external side effects).
- Run: `Pending → Running → (Awaiting Human ⇄ Running) → Succeeded | Failed | Cancelled`. Failed steps with `retryable=true` re-enter Running per retry policy; exhausted retries → Failed + dead-letter entry for manual intervention.
- Mermaid sources: `automation-lab/sample-state-machines/`.

## 3. API proposal (versioned, illustrative — not a source API)
- `POST /v1/workflows` (create draft) · `GET /v1/workflows?module=&status=` (paginated) · `GET /v1/workflows/{id}` · `PATCH /v1/workflows/{id}` (draft only) · `POST /v1/workflows/{id}/test` (dry run against a sample event; returns step trace, executes no side effects) · `POST /v1/workflows/{id}/submit-approval` · `POST /v1/workflows/{id}/activate|pause|archive` · `GET /v1/workflow-runs?workflow_id=&status=` · `GET /v1/workflow-runs/{id}` (full trace) · `POST /v1/approval-tasks/{id}/decide {decision, reason}` · `POST /v1/webhooks/workflow-events/{workflow_id}` (HMAC-verified ingress).
- Errors: `422 RULE_VALIDATION_FAILED` (with per-node paths), `409 VERSION_CONFLICT`, `403 RULE_PERMISSION_DENIED`, `409 SELF_APPROVAL_BLOCKED`, `429 TENANT_RATE_LIMITED`. All list endpoints: cursor pagination, `total` omitted by default for large tenants.
- Idempotency: `Idempotency-Key` header required on decide/activate; trigger dedupe by `(tenant_id, dedupe_key)` unique index.

## 4. Guardrails (non-negotiable)
- No self-approval (requester ≠ approver at any stage; enforced server-side, surfaced in UI as a disabled action with reason).
- Maker-checker for rule publishing when side_effect_class includes financial/external.
- Rejection/return requires a reason; material edits to a document under approval reset its approvals.
- Secrets for webhooks/integrations live in a vault; rules reference secret IDs, never values; every run writes an audit event.
- Cross-tenant isolation: every query is tenant-scoped; rule tests run in a sandbox dataset.

## 5. UX screen map
Automation list (search, module filter, status, owner, last-run outcome) → workflow detail (header status/version, trigger summary, condition tree read view, steps timeline, runs table) → builder (trigger picker → condition tree editor with field picker → action sequence with per-step retry/idempotency → approval designer) → test panel (sample event JSON, dry-run trace) → version diff → log inspector (run → step → payload/error). Input/validation matrix is maintained per step type in the FDD for this capability (`future-product-blueprints/feature-development-dossiers/fdd-workflow-automation-engine.md`).

## 6. Observability & failure scenarios
- Structured logs + trace IDs across steps; metrics: runs, success/error rate, step latency, SLA compliance, approval turnaround, bottleneck stage report.
- Scenarios specified: partial step completion (compensate or park with manual task), duplicate events (dedupe key), concurrent approvals (first decision wins; others get 409 with the winning decision shown), unavailable integration (retry → DLQ → alert owner), revoked permission mid-run (step fails safe, run parked), timezone/DST in schedules (store UTC + tenant calendar; proximity triggers evaluated in tenant time), deleted assignee (fall back to role pool + notify owner), webhook retries (exponential backoff, signed, 5 attempts, then DLQ).
