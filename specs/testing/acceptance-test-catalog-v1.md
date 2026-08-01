# Acceptance Test Catalog v1

## AT-ADM-001 Administrative hierarchy
Given an official county, town and village dataset, when imported, parent-child relationships, official codes, areas and valid geometries are preserved. No duplicate active official code is allowed.

## AT-SRC-001 Source freshness
Given a dataset with expected_max_age_days=31 and last successful retrieval 32 days ago, API and UI return `stale`, display the timestamp and retain the last published snapshot.

## AT-SRC-002 Failed update
When a monthly import fails validation, no partial batch becomes current; the previous published version remains available and an operational alert is recorded.

## AT-PROV-001 Fact provenance
Every environmental fact returned by the profile API contains dataset key, snapshot ID, retrieved date, data period, freshness and APA citation text.

## AT-SOIL-001 Background vs standard
Soil background observations and regulatory thresholds are displayed in separate tables with explicit labels. The system must fail publication if a background value is presented as a legal threshold.

## AT-POP-001 Ten-year statistics
For a complete ten-year series, start/end values, absolute change, percentage change and density calculations match independent test fixtures. Missing years are visibly flagged and not interpolated unless explicitly selected and documented.

## AT-CLIM-001 Station representativeness
Climate output states station, distance, elevation, completeness and period. It cannot describe the station as fully representative when configured limits are exceeded without a limitation note.

## AT-GIS-001 Spatial match type
A contaminated site intersecting the subject parcel returns direct_overlap. A site only inside a buffer returns nearby and never changes the subject parcel regulatory status.

## AT-GIS-002 Map export metadata
Every exported map contains title, legend, scale, north arrow, CRS, source organization, dataset date, retrieval date and export date.

## AT-AI-001 Target length
For target 880 characters, generated narrative is 792–968 characters excluding references, or returns an explicit length limitation. Actual count is shown.

## AT-AI-002 Unsupported claims
A generated section containing any factual sentence without an evidence ID fails publication. The QA response identifies sentence, severity and missing evidence.

## AT-AI-003 Missing data
When no reliable groundwater-flow evidence is supplied, output must state that flow direction cannot be determined and must not infer direction from regional topography alone.

## AT-CITE-001 APA references
Structured reference fixtures generate stable APA 7 output. Missing metadata is not guessed. Duplicate references are deduplicated using DOI or normalized metadata.

## AT-LEGAL-001 Effective version
An evaluation date selects only legal documents effective on that date. The result includes document version and effective date.

## AT-LEGAL-002 Mandatory review
No Article 8/9 result can be marked final without reviewer identity and approval timestamp.

## AT-CTRL-001 Control plan completeness
A control-plan chapter with unresolved required evidence remains incomplete and appears in the completion checklist.

## AT-REMED-001 Alternatives analysis
A remediation recommendation lacking geology, groundwater, contaminant phase or treatability basis is flagged as insufficient and cannot be approved automatically.

## AT-PROJ-001 Project isolation
A user from Organization A cannot access Organization B projects, media, exports or search results. Attempt is logged.

## AT-FIELD-001 Offline observation sync
Offline photos and observations retain capture time, location accuracy, checksum and local identifier; repeated sync does not create duplicates.

## AT-REP-001 DOCX export
Exported DOCX opens without repair warnings, uses heading styles, automatic table of contents, numbered figures/tables, references, data-source appendix and revision history.

## AT-REP-002 Version immutability
Approved report versions cannot be edited. New edits create a new version with diff and audit trail.

## AT-SEC-001 File safety
Unsupported files, excessive sizes and malware-positive uploads are rejected. Accepted files receive checksum, owner, access policy and audit record.

## AT-PERF-001 Profile response
Cached town-level profile metadata responds within 2 seconds at p95 under the defined MVP load test; large geometries use vector tiles or simplified responses.

## UAT scenarios
1. Select 嘉義縣／民雄鄉, review all data sections, freshness and references, generate 880-character chapters and export Word.
2. Create a factory project from address/parcels, capture GPS photos on iPhone, overlay official layers and generate a traceable preliminary Article 8/9 report.
3. Create control/remediation report drafts from approved investigation evidence; confirm placeholders and review gates.
4. Simulate a failed monthly data source and verify stale display, retained prior version and operational notification.

## Release gate
All critical and high tests pass; medium failures require documented acceptance. Security, provenance, legal review and unsupported-claim tests have zero waivers for production release.
