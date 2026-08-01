# 11 UI/UX Specification

## 1. Design principles
- Professional environmental consulting interface, not a consumer dashboard.
- Every number, map, chart and paragraph must expose source, data period, last synchronized time and confidence/status.
- Desktop-first report editing; mobile-first field survey capture.
- No fabricated environmental values. Missing data is shown explicitly.

## 2. Global navigation
1. Dashboard
2. Local Environmental Database
3. Project Workspace
4. GIS Map
5. Report Builder
6. Soil and Groundwater Act Decision Support
7. Control Plan
8. Remediation Plan
9. Knowledge and References
10. Data Source Administration
11. System Administration

## 3. Main environmental query page
Inputs:
- County/city
- Township/district
- Optional address, parcel number or GPS
- Report target word count; default 880 Chinese characters per section
- Citation style; default APA 7
- Data cut-off date

Output tabs:
- Regional overview
- Geography and area
- Topography and land use
- Geology
- Soil background
- Surface hydrology
- Groundwater and hydrogeology
- Ten-year population
- Ten-year climate and rainfall
- Pollution sites
- Environmental and geological sensitive areas
- Soil/groundwater investigation history
- Integrated environmental interpretation
- References and provenance

## 4. Section card requirements
Each section card contains:
- Section title and status
- Generated narrative editor
- Current and requested word count
- Regenerate, copy, lock, restore and compare-version controls
- Tables, charts and map snapshots
- Inline citations linked to source records
- Reference list
- Data period, source publication date, system retrieval time and last successful synchronization
- Warning badges: stale, incomplete, estimated, manually entered, conflicting sources

## 5. Report builder
- Drag-and-drop chapter ordering
- Heading numbering and figure/table numbering
- Per-section word count override
- Source inclusion/exclusion controls
- Technical tone options: consultant, professional engineer, academic, executive summary
- Word preview with page breaks, captions, references and appendices
- Export DOCX, PDF, HTML and Markdown
- Export manifest listing datasets, snapshots and prompt/model versions

## 6. GIS map
- Layer panel with visibility, opacity, legend and source metadata
- Base maps: open street map and approved external tile services
- Operational layers: administrative boundaries, geology, soils, rivers, catchments, groundwater, pollution sites, sensitive areas, projects and field observations
- Identify tool, distance/area measurement, buffer analysis and map print
- Time slider for versioned datasets
- Every map export includes scale, north arrow, coordinate reference system, legend, source and date

## 7. Project workspace
- Overview, locations/parcels, timeline, field survey, documents, GIS, samples, boreholes/wells, legal assessment, reports and tasks
- Mobile field capture: GPS, photo, direction, timestamp, note, voice memo and offline queue
- Immutable audit history for approvals and published reports

## 8. Accessibility and responsive behavior
- WCAG 2.2 AA target
- Keyboard navigation, visible focus, semantic labels and chart data tables
- Mobile cards replace wide tables; report editing remains available but optimized for desktop

## 9. Acceptance criteria
- User can select an administrative area and see all required sections.
- Every displayed datum exposes provenance and freshness.
- User can request 880 or custom word counts and regenerate one section without changing locked sections.
- User can export a Word-ready report with references, figures and update timestamps.