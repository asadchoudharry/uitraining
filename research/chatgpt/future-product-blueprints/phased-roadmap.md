# Future product capability roadmap — evidence calibrated

## Baseline constraint
No specific production target repository or deployed application was provided for feature parity comparison. Every new item below has target status **TARGET_STATUS_UNVERIFIED**. Future candidates are **not** verified gaps.

## Backlog A — Observed-reference patterns to study

| Priority | Capability | Ref | Evidence | Why | Prerequisites |
| --- | --- | --- | --- | --- | --- |
| P0 | Approval queue, history and human decision context | FEAT-0002, FEAT-0042 | Described in S02 case-study; UI route in S05 | High-risk decisions need clear next action | Role policy, event model, audit |
| P0 | Global keyboard command palette | FEAT-0010, FEAT-0011 | S03 source code inspected | Power users navigate complex apps faster | Authorized action registry |
| P0 | Project/site context persistence | FEAT-0019, FEAT-0020 | S04 UI/indexed | Avoid incorrect project assignment | Scoped context routing |
| P1 | Retail barcode and POS operational screens | FEAT-0055, FEAT-0058 | S06 UI/indexed | Streamline cash register transactions | Pricing, tender gateway, ledger |
| P1 | Construction audit and inspections | FEAT-0027, FEAT-0028 | S04 UI/indexed | Assign and resolve site findings | Evidence store, assignment |
| P1 | Flexible tables, saved views and density | FEAT-0012, FEAT-0014 | S03 code inspected | Lower repeated filtering work | Common filter/state model |

## Backlog B — Original proposals inspired by research

| Priority | Dossier | New capability | Dependencies | Evidence type |
| --- | --- | --- | --- | --- |
| P0 | WFL-001 | Maker-checker document approval with 409 conflict recovery | Policy engine, event store, tenant RBAC | PROPOSED |
| P0 | WFL-002 | Resumable, idempotent multi-country tenant provisioning | Pack manifest, provisioning job, rollback | PROPOSED |
| P0 | WFL-003 | Reconciled POS checkout, stock and receipt issuance | Sale journal, tender provider, transactional outbox | PROPOSED |
| P1 | WFL-004 | Inspection → finding → corrective action → independent closure | Evidence store, notification queue | PROPOSED |
| P1 | AUTO-001 | Versioned trigger/condition/action automation editor | Queue, scheduler, connector grants, run engine | PROPOSED |
| P2 | UX-001 | Verified keyboard/RTL/accessible state coverage | Semantic components and automation suite | PROPOSED |

## Backlog C — Verify target system before deciding a gap

| Investigation | Required evidence | Outcome until tested |
| --- | --- | --- |
| Is an approval workflow already present? | Target routes, DB schema, API, role tests | TARGET_STATUS_UNVERIFIED |
| Is multi-country tenant provisioning implemented? | Tenant control-plane source, job logs | TARGET_STATUS_UNVERIFIED |
| Are POS receipts and refunds transaction-safe? | Settlement/reconciliation data and tests | TARGET_STATUS_UNVERIFIED |
| Are site CAPA records durable and auditable? | CRUD API, evidence store, permissions | TARGET_STATUS_UNVERIFIED |
| Are saved views and command palette accessible? | Existing design system, live keyboard tests | TARGET_STATUS_UNVERIFIED |

## Engineering slices and release sequence

1. **Platform governance:** user/role/tenant policy, append-only audit and secure connector-grant models. Gate: privilege escalation tests.
2. **Approval vertical slice:** build WFL-001 all screens/actions/states and one end-to-end test. Gate: 409 handling, requester denial, audit immutability.
3. **Automation execution:** versioned workflow, idempotent outbox, approval waits and safe retries. Gate: no double effectful actions.
4. **Onboarding:** build WFL-002 with drafts, country/industry packs, provisioning replay and rollback. Gate: no duplicate tenants.
5. **Retail:** build WFL-003 with real tender, stock, receipt, return and shift reconciliation tests. Gate: no duplicate charge or stock posting.
6. **Field operations:** WFL-004 with offline evidence, CAPA and independent closure. Gate: no unverified closure.
7. **Visual integration:** original tokens, Figma components, responsive keyboard/RTL parity and accessibility checks. Gate: WCAG 2.2 AA target.

## Prioritization logic
Score each candidate from 1–5 on business throughput, regulatory risk reduction, source confidence, implementation risk, multi-industry reuse and actual target-gap evidence. Do not label a feature 'missing' until target proof exists.
