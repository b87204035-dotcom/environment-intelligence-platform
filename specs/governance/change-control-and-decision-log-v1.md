# Change Control and Decision Log v1

## Change request required when

- scope adds a new product module or report type
- a source, license, field map or refresh rule changes
- a legal rule or government guidance changes
- a database/API contract breaks compatibility
- an AI prompt/model changes production behavior
- a security, retention or tenant-isolation rule changes
- a report template changes an authority-required chapter

## Change record fields

- change ID and title
- requester and date
- reason and desired outcome
- affected requirements, sources, rules, schemas, APIs, prompts and reports
- risk and privacy assessment
- migration/backfill requirements
- test and acceptance impact
- reviewer/approver decisions
- release target and rollback plan
- final status and evidence links

## Architecture decision record template

1. Context
2. Decision
3. Alternatives considered
4. Consequences
5. Security/data/legal impact
6. Migration and rollback
7. Approval

## Baseline decisions

- ADR-001: modular monorepo with Next.js, FastAPI, PostgreSQL/PostGIS and background workers.
- ADR-002: immutable source snapshots and publication versions.
- ADR-003: evidence-grounded generation; no free-form factual generation without registered evidence.
- ADR-004: human approval for legal, control, remediation and final report outputs.
- ADR-005: explicit unavailable/stale states; never replace missing official data with fabricated values.
- ADR-006: tenant-isolated project workspace and audit trail.

Approved baselines may be superseded only by a new recorded decision; they are not silently edited.