# Phased roadmap (proposal)

Scoring: factors are 0–5 as in `priorities-and-dependencies.csv` (value, reuse, frequency, evidence quality, strategy alignment, effort-inverse, dependency-risk-inverse, compliance-risk-inverse), unweighted sum shown for transparency; bands were assigned by judgement on top of scores, because P0 is reserved for cross-cutting prerequisites regardless of glamour.

- **Phase 1 (foundations)**: design tokens + component kit (this repo's design-system), saved views/filter platform, workflow register with audit. Exit: one module (e.g., approvals) runs end-to-end on the register with real persistence.
- **Phase 2 (leverage)**: workflow engine v1 (triggers/conditions/actions per automation-lab spec, dry-run included), company setup + activation analytics, integration gallery with validated activation, governance evidence pack.
- **Phase 3 (domain packs)**: POS variant family + offline queue; construction delivery pack; supplier portal pack (Veluno pattern).
- **Phase 4 (experiments)**: AI agent panels behind human-review gates; SLA forecasting. Gate: no AI action executes a financial side effect without a human decision in v1.

Dependencies: engine depends on register + audit; activation analytics depends on setup events; domain packs depend on views platform. Rollback: every phase ships behind tenant-level feature flags with data-preserving downgrade paths.
