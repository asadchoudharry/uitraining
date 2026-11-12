# WFL-002 — Multi-country tenant onboarding and provisioning

**Classification:** original implementation-ready proposal, not observed third-party backend behavior.
**Source pattern references:** S09 / static onboarding reference / FEAT-0071
**Actors:** Organization Owner, Invited Admin, Billing Operator, Provisioning Service
**User goal:** Create and activate a tenant safely with country/industry configuration, role grants, and reliable retry.
**Entry:** Sign up > Organization setup

## Screen-by-screen specification
| Screen ID | Name | Visible controls and content | Mandatory non-happy-path states |
| --- | --- | --- | --- |
| SCR-101 | Welcome and account | Identity provider and account confirmation | loading, empty, filtered-empty, denied, stale, error, success |
| SCR-102 | Organization identity | Legal name, operating name and timezone | loading, empty, filtered-empty, denied, stale, error, success |
| SCR-103 | Country pack | Country, currency, tax region, language and local compliance | loading, empty, filtered-empty, denied, stale, error, success |
| SCR-104 | Industry pack | Choose business workflows and seeded but non-sensitive modules | loading, empty, filtered-empty, denied, stale, error, success |
| SCR-105 | Team and permissions | Owner, invitees, roles, domain validation | loading, empty, filtered-empty, denied, stale, error, success |
| SCR-106 | Review and create | Summary, warnings, irreversible action confirmation | loading, empty, filtered-empty, denied, stale, error, success |
| SCR-107 | Provision status | Queued/running/partial/failed/ready, resumable | loading, empty, filtered-empty, denied, stale, error, success |
| SCR-108 | First workspace | Contextual getting-started list and contextual help | loading, empty, filtered-empty, denied, stale, error, success |

## Interaction contracts
| Action ID | Control | Actor | Authorization and validation | On success | Error recovery |
| --- | --- | --- | --- | --- | --- |
| ACT-101 | Save and continue | Owner | Section-valid fields; draft permission | draft saved | validation failure; network retry |
| ACT-102 | Choose country | Owner | Supported policy pack; explicit currency choice | country pack applied to preview | unsupported region and conflicts |
| ACT-103 | Invite team | Owner | Email format, approved domains, role restrictions | invites queued after create | duplicate/blocked invite |
| ACT-104 | Confirm provision | Owner | Checksum and idempotency key | 202 PROVISION_QUEUED | 409 duplicate create; 422 invalid configuration |
| ACT-105 | Retry provisioning | Owner/Operator | Stage retryable; locked idempotent phase | RUNNING or READY | unknown outcome pending reconciliation |

## State graph
ACCOUNT_CREATED → DRAFT → VALIDATED → PROVISION_QUEUED → PROVISIONING → READY → FAILED_RETRYABLE → FAILED_NEEDS_SUPPORT → CANCELLED (the actual branches and guards are defined in implementation tests; arrows are not all permitted transitions).

## Proposed data model
Tenant, TenantSettings, IndustryPack, CountryPack, OnboardingDraft, ProvisionJob, MemberInvitation, DomainPolicy, AuditEvent

## Proposed endpoints
- POST /api/v1/tenants/drafts
- PATCH /api/v1/tenants/drafts/{id}
- POST /api/v1/tenants/provision
- GET /api/v1/tenants/provision-jobs/{id}
- POST /api/v1/tenants/provision-jobs/{id}/retry

## Permission and consistency rules
- Every object is tenant-scoped; server-side authorization is mandatory on read and write, independent of frontend affordances.
- High-risk writes require idempotency keys, optimistic concurrency and an append-only audit event.
- Unknown external outcomes require reconciliation, not blind retry.
- Unauthorized state must be explicit; disabled buttons do not imply secure authorization.
- Every error preserves unsaved context and provides a user-visible retry or remediation path.

## Acceptance test dossier
1. Exact same idempotency key creates only one tenant
2. Country pack change invalidates incompatible tax values visibly
3. User can resume saved steps after reload
4. Provision partial failure leaves safe rollback checkpoints
5. Tenant cannot access another tenant's provisioning ID

## Scope and caveats
Paid billing, production tax submissions and legacy tenant import are outside this original prototype.
- Implementation status: SPECIFIED only. Figma-linked reference screen covers a generic approval UI, not all these specific workflow screens.
- Tests are acceptance proposals; not executed backend checks.
