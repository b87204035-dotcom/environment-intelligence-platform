# 19 Code Review Checklist

## Architecture
- Change follows documented module boundaries.
- No unnecessary coupling between source ingestion, domain data, reporting and UI.
- Background jobs are idempotent and retry-safe.

## Data integrity
- Raw snapshots remain immutable.
- Units, dates, CRS and identifiers are explicit.
- Missing/conflicting data are represented, not silently replaced.
- Migration has downgrade/rollback strategy.

## Provenance
- New factual outputs resolve to source snapshots.
- Source period and synchronization timestamp are exposed.
- Citation generation uses registered records.

## Security
- Default-deny authorization.
- No secrets or private data in logs/tests.
- Upload and export paths are validated.
- Audit events exist for material actions.

## AI
- Grounding set is explicit.
- Generated claims include evidence links.
- Human-review gate remains intact.
- Prompt/model/template versions are recorded.

## UI/accessibility
- Loading, error, empty, stale and incomplete states exist.
- Keyboard and screen-reader behavior is acceptable.
- Charts have data-table alternatives.

## Tests and operations
- Tests cover success and failure paths.
- Metrics/logs support diagnosis.
- Documentation and release notes are updated.
- Definition of Done is satisfied.