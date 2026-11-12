# FDD — Workflow automation engine (P0/P1)

- Capability: tenant-configurable triggers → conditions → actions/approvals with dry-run testing and full run observability.
- Source basis: FP-001 (S05 register, UI_VISIBLE_ONLY) + S02 Relay console IA (RUNTIME_OBSERVED demo) + original engine design in `automation-lab/workflow-engine-proposed-spec.md`. Status of the capability in sources: **no working engine observed anywhere in the corpus**.

## Product decision
Businesses re-key approval policy into chat threads and spreadsheets because their ERP's "workflow" is a label, not a machine. Personas: process owner (builds), approver (decides), auditor (verifies). Alternatives: hard-coded per-module approvals (rigid) vs external iPaaS (data leaves the tenant). Value hypothesis: cycle time for PO/expense approvals drops; every decision becomes auditable. Trade-off accepted: v1 ships sequential/parallel approvals + record triggers only; cron/webhook triggers follow.

## Screens & UX
Automation list; workflow detail; builder (trigger picker, condition-tree editor, action sequence, approval designer); test panel; runs list; run inspector; approval inbox. Controls, validations and states are specified in the engine spec §5 and the approval-panel component spec. Role visibility: builders need `workflow.build`; activation needs `workflow.activate`; approvers need only the inbox.

## Flow
Draft → test (dry run, zero side effects) → submit for publishing approval (required when financial/external actions exist) → active → runs execute with pinned version → decisions in inbox → run completes or parks in DLQ with an owner task.

## Data architecture
Entities and invariants: engine spec §1. Tenant-scoped everywhere; `(tenant_id, dedupe_key)` unique; versions immutable once run.

## API & events
Engine spec §3. Events: `workflow.run.started/completed/failed`, `approval.requested/decided`, `workflow.published`.

## Security & operations
No self-approval; secrets by reference; sandbox test data; rate limits per tenant; structured logs + trace IDs (spec §6).

## Quality requirements (acceptance, Given/When/Then)
- Given a draft rule with a financial action, when the builder activates without publishing approval, then activation is refused with the reason.
- Given a duplicated trigger event (same dedupe key), when it arrives twice, then exactly one run exists.
- Given an approver who is also the requester, when they open the task, then decision controls are disabled with an explanation and the API returns 409 SELF_APPROVAL_BLOCKED.
- Keyboard: the full builder is operable without a pointer; condition tree announces changes via aria-live.
- Performance: run creation p95 < 300ms at 1,000 events/min/tenant (load-test target, to be verified at build).

## Delivery planning
Size band: L (platform capability). Dependencies: audit log service, notification service, tenant calendars. Rollout: flag per tenant; rollback = pause all rules (data preserved).
