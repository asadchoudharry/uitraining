# Feature passport — Document workflow record (levels + escalation) (FP-001)

- Evidence: **UI_VISIBLE_ONLY** · Module: Workflow · Priority: P1_HIGH_LEVERAGE · Target status: NOT_AUDITED
- Sources: S05 — https://dreamserp.dreamstechnologies.com/tailwind/document-workflows.html, https://dreamserp.dreamstechnologies.com/tailwind/workflow-approvals.html

## Observed behaviour
Two admin pages: a workflows table (ID, Name, Module, Levels 2-6, Escalation 12/24/36/48 hours, Active Yes/No) with Add/Edit modals (Workflow ID*, Module* select HR/Finance/Legal, Name*, Levels, Escalation, Active) and delete confirmation; and an approvals catalog table (ID, Module, Name, Description, Status) with module filter chips and an Add/Edit Record modal (ID*, Module*, Name*, Status* Active/Inactive, Description). Sample approval use cases: expense, PO by value, leave, discount >10%, timesheet, asset disposal, policy, access, contract, audit exception.

## Not verified
Any routing, condition evaluation, approver assignment, notification, SLA timing or execution. No builder, triggers, conditions or logs exist in the pages.

## Business problem / users / jobs
Approvals are configured inconsistently per module with no single register. Users: System administrators, process owners. Jobs: Register an approval workflow for a module; see its level count and escalation time; activate/deactivate it.

## Screens, actions, fields
Screens: S05-DOCWF, S05-WFAPP. Actions: Add, Edit, Delete (confirm), Search, Sort, Print, Export, paginate (10/25/50/100). Inputs: Workflow ID, Module, Name, Levels, Escalation, Active / ID, Module, Name, Status, Description. Outputs: Saved workflow record in the table.

## States & validations
States: Active / Inactive (record-level only). Validations: ID, Module, Name required (asterisk-marked in the source form)

## Permissions, notifications, audit
Permissions: Admin role implied; not verified. Notifications: None demonstrated. Audit: None demonstrated

## Data & proposed API
Entities: Workflow {id, module, name, levels, escalation_hours, active}; ApprovalRecord {id, module, name, description, status}. API (PROPOSED): PROPOSED: GET/POST/PATCH /v1/document-workflows (see automation-lab spec)

## Acceptance criteria
Given an admin, when they create a workflow with module+levels+escalation, then it appears in the table with an Active flag and can be deactivated without deletion.

## Test cases
Create/edit/delete happy path, Required-field validation, Deactivate hides the workflow from new documents (proposed semantics — not source behaviour)
