# 15 Test and Acceptance Plan

## 1. Test layers
- Unit tests for transformations, trend calculations, citation formatting and legal decision rules
- Database migration and constraint tests
- API contract, authorization and error-response tests
- Connector tests using recorded fixtures
- GIS geometry, projection and spatial-query tests
- Frontend component and accessibility tests
- End-to-end workflows
- Document export snapshot tests
- Performance, security and disaster-recovery tests

## 2. Critical end-to-end scenarios
1. Select county and township, retrieve all environmental sections, inspect provenance and export DOCX.
2. Change one section target from 880 to 1,500 characters, regenerate it and preserve locked sections.
3. View ten-year population and rainfall tables/charts and verify calculation period and missing-data disclosure.
4. Inspect soil background values with units, depths, statistic, method and spatial applicability.
5. Search an address/parcel/GPS point, display applicable spatial layers and generate a map with source/date/CRS.
6. Create a project, upload a geotagged photo, add a field observation and preserve audit history.
7. Generate a section from approved snapshots and prove every factual claim resolves to evidence.
8. Run monthly synchronization; verify immutable raw snapshot, validation, publication and freshness timestamps.
9. Simulate failed synchronization; show stale warning and preserve last valid publication.
10. Draft an Article 8/9 assessment or control/remediation plan and require professional review before approval.

## 3. Data quality acceptance
- No fabricated sample values in production paths.
- 100% of published factual paragraphs have source links.
- 100% of visible dataset cards show source period and last synchronization time.
- Trend calculations are reproducible from stored observations.
- Spatial data use declared CRS and valid geometry.

## 4. Report export acceptance
- Heading, figure, table and reference numbering are stable.
- Chinese fonts are configurable and not embedded without permission.
- Charts include accessible data tables.
- Reference list contains only cited works and no broken source IDs.
- Export manifest records dataset snapshots, generation template/model versions and generation time.

## 5. Performance targets for MVP
- Administrative-area summary API p95 below 1.5 seconds with cache after warm-up.
- Map viewport query p95 below 2 seconds for expected layer volume.
- Report draft generation request is asynchronous and exposes progress.
- DOCX export completes within 60 seconds for a standard report.

## 6. Release gate
A release is blocked by critical security defects, missing provenance, failed migrations, unreproducible reports, invalid legal citations or loss of audit history.