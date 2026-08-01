# 29 Operations Runbook

## Daily checks
- API and worker health
- failed jobs and synchronization alerts
- database/storage capacity
- security alerts

## Monthly source update run
1. Resolve all due datasets.
2. Retrieve into immutable raw storage.
3. Verify checksum and content type.
4. Parse and validate schema, units, identifiers, geometry and temporal continuity.
5. Compare with previous snapshot and flag anomalies.
6. Obtain review for material changes.
7. Publish version atomically.
8. Update last-successful-sync and next-expected-sync.
9. Rebuild affected aggregates/caches.
10. Retain run report and notify on failures.

## Incident priorities
- P1: unauthorized access, data loss, corrupted publication, public disclosure of private project data
- P2: report/source traceability failure, system-wide outage, incorrect legal version
- P3: single source/connector failure, degraded map/export function
- P4: cosmetic/non-critical defect

## Source failure
Keep the last approved publication, mark stale, record failure and retry. Never replace with synthetic values.

## Rollback
Rollback application release separately from dataset publication. Published dataset versions remain addressable. Revert by switching active publication pointer after approval.

## Backup recovery
Perform periodic restore drills and record actual recovery time. Verify database, object files, audit logs and encryption keys.

## Production launch checklist
- domains/TLS/secrets configured
- backups and monitoring enabled
- admin accounts protected by MFA
- source licenses approved
- privacy and retention policy approved
- security/accessibility/performance tests passed
- first monthly synchronization rehearsed
- support and incident contacts assigned