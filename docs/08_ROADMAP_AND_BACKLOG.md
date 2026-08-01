# 08 Roadmap and Backlog

## Milestone 0 — Platform bootstrap
- production monorepo
- Docker Compose, PostGIS, migrations
- authentication/organization skeleton
- CI, tests, health and observability

## Milestone 1 — Data governance and geography
- source registry, snapshots and freshness
- counties/towns/villages and spatial boundaries
- address, coordinate and parcel adapters
- GIS base map and layer catalog

## Milestone 2 — Environmental profile MVP
- geology, soil background, surface water, groundwater
- population, weather/rainfall, pollution sites, sensitive areas
- investigation history
- charts, tables, source cards and update timestamps

## Milestone 3 — Report generator
- report templates and section editor
- 880-character default/custom target
- evidence-constrained narrative generation
- APA citations, source appendix and DOCX/PDF export
- quality checks and version comparison

## Milestone 4 — Projects and field survey
- project workspace, site/parcel management
- mobile GPS photos and notes
- files, map annotations, sampling points and timeline
- roles, audit log and review workflow

## Milestone 5 — Article 8/9 module
- versioned legal corpus
- announced-business classification
- event/fact questionnaire and rule engine
- evidence path, missing information and reviewed export

## Milestone 6 — Control plan
- official-guideline-aligned template
- conceptual site model, objectives, methods, monitoring and QA/QC
- completeness checks, reviewer comments and export

## Milestone 7 — Remediation plan
- technology screening and alternative comparison
- pilot evidence, design assumptions, monitoring, contingency and verification
- sustainability, costs, schedule and export

## Milestone 8 — Production readiness
- security review, backup/restore and disaster recovery
- performance/load tests
- accessibility and mobile acceptance
- data license review
- deployment, operations manual and user training

## Product-level acceptance gates

1. Source lineage is implemented before any AI narrative.
2. Real government imports are introduced one dataset at a time with validation and licensing review.
3. Legal/engineering outputs remain drafts until a named reviewer approves them.
4. No environmental number or legal conclusion is shipped without evidence mapping.
5. Version 1.0 requires an end-to-end town report and one project workflow working in staging.