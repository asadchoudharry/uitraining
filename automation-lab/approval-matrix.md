# Approval matrix (PROPOSED patterns, with observed anchors)

| Pattern | When | Anchor |
|---|---|---|
| Single approver | Low value, low risk | S05 Levels=2 records (min. demonstrated shape) |
| Sequential levels | Increasing scrutiny per stage | S05 Levels 2-6 across modules (OBSERVED as counts only) |
| Amount-threshold routing | PO / discount / budget | S05 descriptions "PO approvals by value", "discounts >10%" (free text only in source) |
| Parallel / quorum | Boards, compliance exceptions | NEW_PROPOSAL (S05 Audit Exception record motivates it) |
| Manager chain | Leave, expenses | S05 Leave/Expense approval records |
| Delegation / out-of-office | Any | NOT_FOUND_IN_SOURCE — NEW_PROPOSAL |
| Escalation on SLA breach | Any timed approval | S05 Escalation hours 12/24/36/48 (single value per workflow in source) |

Rules that apply to every pattern: no self-approval; rejection requires reason; material change resets approvals; every decision is an audit event with actor, timestamp and rule version.
