# User Acceptance Test Scenarios v1

## UAT-01 Local environmental profile
Select 嘉義縣 / 民雄鄉. The system returns every configured topic with source metadata, coverage status, data period, last synchronization and explicit missing-data messages. No placeholder number is presented as official.

## UAT-02 Custom narrative length
Generate the geology section at the default target of 880 Chinese characters, then regenerate at 1,500. Output reports actual character count, preserves evidence links and does not introduce unsupported facts.

## UAT-03 Soil background distinction
Display soil series/properties and background concentration evidence separately from regulatory standards. Each concentration includes analyte, statistic, unit, sample count, depth, method, spatial population and source.

## UAT-04 Ten-year statistics
Population, temperature and rainfall charts use clearly defined ten-year periods, identify missing years/stations and expose calculation methods and source snapshots.

## UAT-05 Pollution-site query
Map and table agree on the number and identity of pollution sites. Direct overlap, nearby sites and sites merely within the same administrative area are not conflated.

## UAT-06 Article 8/9 preliminary evaluation
The user completes a checklist. The output shows matched rule version, evidence, unresolved questions, preliminary status and mandatory professional review notice. It never states final legal advice.

## UAT-07 Control/remediation plan drafting
Create a plan workspace, verify all required chapters, assumptions, conceptual site model, alternatives, schedule, cost basis, monitoring, contingency and verification placeholders. Publication is blocked until approval.

## UAT-08 Word export
Export a report containing edited sections, tables, figures, map, APA references, source appendix, revision record and approval status. Reopening the DOCX preserves Chinese text and numbering.

## UAT-09 Monthly source status
Simulate success, delayed publication, endpoint failure and schema change. The dashboard shows current/due/stale/unavailable correctly and retains the prior valid version.

## UAT-10 Mobile field survey
Capture GPS accuracy, photo, direction, voice note and observation while offline. Reconnect and sync exactly once with preserved timestamps and audit history.

## UAT-11 Tenant isolation
A user in one organization cannot list, fetch, search, export or infer another organization's projects or files.

## UAT-12 Report quality check
Upload or generate a draft containing a missing citation, conflicting value, outdated legal version and unsupported conclusion. QA identifies all four and blocks final approval where required.