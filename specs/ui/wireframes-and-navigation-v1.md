# UI Navigation and Wireframes v1

## Primary navigation
1. Dashboard
2. Local Environmental Database
3. GIS Map
4. Projects
5. Reports
6. Legal Evaluation
7. Control / Remediation
8. Knowledge and References
9. Data Source Operations
10. Administration

## Dashboard
Desktop layout:
- top status bar: current user, organization, global search, notifications
- KPI cards: active projects, reports awaiting review, stale sources, failed syncs
- timeline: upcoming project deadlines and data refresh dates
- recent work: reports, projects, exports
- operations panel: last monthly update and unresolved errors
Mobile layout: stacked cards; bottom navigation for Dashboard, Search, Projects, Field and More.

## Local Environmental Database
Header controls:
- county selector
- town/city/district selector
- optional village selector
- time range default latest complete ten years
- report character target default 880
- citation style default APA 7
- Generate complete report

Content tabs:
Overview | Geography | Geology | Soil | Surface Water | Groundwater | Population | Climate | Pollution | Sensitive Areas | Investigation History | Sources

Each section card:
- heading and availability/freshness badge
- generated narrative and actual character count
- edit/regenerate/copy buttons
- chart/table/map panel
- source drawer listing data period, publisher, dataset, last successful sync and APA reference
- limitations panel
- approval state

## GIS Map
Three-pane desktop:
- left: layer catalog and search
- center: map
- right: selected feature, source metadata and analysis results
Tools: address/parcel/GPS locate, draw, measure, buffer, intersection, distance, identify, opacity, timeline, map export.
Mobile: full-screen map, bottom sheet for layers/results, large GPS and photo buttons.

## Project Workspace
Project header: project no., name, client, status, owner, due date.
Tabs: Summary | Sites | Timeline | Field Survey | Documents | GIS | Sampling | Legal | Reports | Tasks | Audit.
Summary shows completion checklist and missing information.
Field Survey supports offline queue, GPS accuracy, photo direction, voice note and sync state.

## Report Builder
Left: report outline and completion badges.
Center: rich-text section editor with generated/edited diff.
Right: evidence, citations, data freshness, QA findings and reviewer controls.
Top controls: target characters, tone, generate, compare versions, run QA, export.
Publication requires zero critical QA findings and reviewer approval where required.

## Legal Evaluation
Wizard:
1. Property identity
2. Transaction/operation facts
3. Current and historical business categories
4. Official site records
5. Missing documents
6. Preliminary result
Result screen always shows effective law date, rules evaluated, evidence, missing facts and human-review warning.

## Control / Remediation Workspace
- plan template/version selector
- chapter completeness matrix
- conceptual site model panel
- alternatives comparison table
- schedule/cost/risk registers
- monitoring and verification designer
- unresolved evidence placeholders

## Data Source Operations
Table columns: topic, dataset, publisher, status, expected frequency, data published, last retrieved, age, last validation, record count, next due, owner.
Actions: inspect snapshot, compare schema, rerun import, pause, approve candidate, view citation and license.

## Visual design rules
- professional neutral interface; information density suitable for consultants
- status never communicated by color alone
- Traditional Chinese first; English names optional
- desktop minimum 1280 px; responsive mobile field workflow
- WCAG 2.2 AA target
- source/freshness labels remain visible in print and export
- destructive actions require confirmation; legal/report approvals require explicit signed action
