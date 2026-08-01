# 13 Data Governance and Update Policy

## 1. Objectives
Ensure every published value and narrative is traceable, reproducible, versioned and reviewed.

## 2. Dataset lifecycle
Registered → Access verified → Retrieved → Raw snapshot preserved → Parsed → Validated → Approved → Published → Superseded/Retired.

Raw source snapshots are immutable. Transformations create new versions and never overwrite original records.

## 3. Required timestamps
Each dataset and visible section exposes:
- source_published_at
- source_period_start/end
- retrieved_at
- validated_at
- published_at
- last_successful_sync_at
- next_expected_sync_at

The web page prominently shows `資料最後更新時間` and separately shows the source data period.

## 4. Minimum update policy
- Every active source is checked at least monthly.
- Sources published more frequently may be checked daily or weekly.
- Static or irregular sources are still checked monthly for a new version.
- Monthly schedule must include retry, failure logging and notification.

## 5. Freshness states
- current: before next expected sync
- due: expected sync window reached
- stale: more than one update interval overdue
- unavailable: source failed repeatedly or was withdrawn
- manual_review: schema, license or content changed

A stale state does not delete previously published data; it adds a warning and may block generated reports for critical sections.

## 6. Validation
Automated checks:
- schema and required fields
- coordinate reference system and geometry validity
- duplicate keys
- temporal continuity
- unit and range checks
- row-count anomaly
- unexpected category changes
- checksum and source version comparison

Professional review is required for legal classifications, soil background interpretation, hydrogeologic interpretation and control/remediation recommendations.

## 7. Conflict handling
Store all competing records. Create a conflict record stating affected field, sources, temporal context, resolution status and reviewer. Reports disclose unresolved material conflicts.

## 8. Licensing and attribution
No dataset is ingested until license, permitted use, attribution and redistribution rules are recorded. Restricted datasets may be linked or processed privately but must not be redistributed.

## 9. Audit and rollback
All manual changes store actor, timestamp, old value, new value and reason. Published versions can be reproduced from snapshot IDs and transformation versions.

## 10. Monthly run acceptance
A monthly run succeeds only when:
- every due connector returns success or a documented exception
- validation passes or is approved with exceptions
- freshness records update
- published material remains reproducible
- a run report is retained.