# Minxiong Reference Acceptance Pack v1

Purpose: define a repeatable end-to-end acceptance target for 嘉義縣民雄鄉 without embedding fabricated official values.

## Required profile sections

1. Administrative location and area
2. Topography and landform
3. Regional geology and structures
4. Soil map, soil series and properties
5. Soil background concentration evidence, when available
6. Surface-water system and watershed context
7. Groundwater and hydrogeology
8. Ten-year population statistics
9. Ten-year temperature and rainfall analysis
10. Land use
11. Pollution sites and control areas
12. Environmental and geological sensitive areas
13. Soil/groundwater investigation history
14. Integrated limitations and professional interpretation
15. Section-level and report-level references

## Acceptance evidence

For every section store:

- normalized data rows or explicit unavailable status
- source dataset and snapshot ID
- geographic/temporal coverage
- transformation and calculation method
- table/chart/map specification
- generated narrative target length and actual length
- paragraph-to-evidence links
- APA reference entries
- reviewer status

## Prohibited shortcuts

- Do not infer township-specific geology solely from a county-wide statement without labeling the scale limitation.
- Do not calculate groundwater flow direction unless sufficient time-aligned head observations and well elevations exist.
- Do not call a value a soil background concentration without documented sampling population and method.
- Do not treat a pollution site in 民雄鄉 as overlapping a selected parcel unless geometry proves it.
- Do not fill unavailable ten-year observations with invented values.

## Golden-path demonstration

The acceptance demonstration shall select 嘉義縣/民雄鄉, load verified profile data, generate an 880-character section, regenerate at 1,500 characters, inspect citations, view GIS layers, export DOCX and show source freshness. Test fixtures must be clearly labeled synthetic when they are not official data.