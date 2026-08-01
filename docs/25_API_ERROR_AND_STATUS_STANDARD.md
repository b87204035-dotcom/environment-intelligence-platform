# 25 API Error and Status Standard

## Response envelope
Successful responses return data plus metadata containing request ID, publication version, source freshness and generated timestamp where applicable.

Errors use RFC 7807-style problem details with:
- type
- title
- status
- detail
- instance
- request_id
- code
- field_errors
- retryable

## Domain status codes
- SOURCE_STALE
- SOURCE_UNAVAILABLE
- DATA_INCOMPLETE
- DATA_CONFLICT
- INVALID_ADMINISTRATIVE_AREA
- INVALID_GEOMETRY
- UNSUPPORTED_CRS
- REPORT_GENERATION_PENDING
- REPORT_GENERATION_FAILED
- EVIDENCE_REQUIRED
- PROFESSIONAL_REVIEW_REQUIRED
- EXPORT_FAILED
- FORBIDDEN_PROJECT

## Asynchronous jobs
Long operations return 202 with job ID, status URL and optional progress. Job states: queued, running, awaiting_review, succeeded, failed, cancelled.

## Pagination/filtering
Cursor pagination for large changing sets; stable sorting; explicit date ranges; spatial bbox filters; publication version filters.

## Idempotency
Create/export/synchronization endpoints accept idempotency keys. Worker handlers must be retry safe.

## Versioning
REST base `/api/v1`. Backward-incompatible changes require a new major API version. OpenAPI is generated and checked in CI.