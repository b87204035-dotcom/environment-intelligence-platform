# 02 System Architecture

## 1. Logical architecture

- Web app: Next.js + TypeScript
- API: FastAPI
- Relational/spatial database: PostgreSQL + PostGIS
- Object storage: project files, photos, exports and source snapshots
- Worker: ETL, scheduled synchronization, report export and AI generation
- Queue/cache: Redis-compatible service
- Map: MapLibre GL JS; GeoJSON/vector tiles/WMS/WMTS adapters
- Observability: structured logs, job status, audit events and health checks

## 2. Services

1. `web`: query, maps, report editor and project workspace.
2. `api`: authentication, business rules, source lineage and CRUD.
3. `worker`: imports, transformations, charts, DOCX/PDF and AI jobs.
4. `scheduler`: monthly sync plus source-specific schedules.
5. `database`: master data, versions, spatial data and provenance.
6. `storage`: immutable source files and project attachments.

## 3. Data flow

Source registry → connector/import → raw snapshot → validation → normalized tables → spatial linkage → publication version → chapter dataset → AI narrative → citations → export.

No generated narrative may bypass the chapter dataset and provenance layer.

## 4. Environments

- local: Docker Compose
- staging: protected test data and test imports
- production: separate secrets, database and storage

## 5. Security

- roles: owner, administrator, project manager, editor, reviewer, viewer
- row/project-level authorization
- encrypted transport and secret management
- audit log for data, report, legal decisions and exports
- uploads require malware/type/size validation

## 6. Resilience

- import jobs are idempotent
- source snapshots are immutable
- failed jobs are retryable without duplicating records
- publication only after validation
- rollback to prior dataset/report version

## 7. AI boundary

AI receives a structured evidence package containing facts, units, time range, source IDs and allowed claims. Outputs return paragraph text plus citation mapping and warnings. Legal and engineering outputs require human approval.