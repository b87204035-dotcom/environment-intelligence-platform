# 21 Environmental Section Data Contracts

Every environmental section returns a common envelope:

```json
{
  "administrative_area_id": "...",
  "section_type": "soil_background",
  "status": "current|stale|incomplete|unavailable",
  "data_period": {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"},
  "last_successful_sync_at": "ISO-8601",
  "observations": [],
  "statistics": [],
  "map_layers": [],
  "figures": [],
  "sources": [],
  "limitations": [],
  "publication_version_id": "..."
}
```

## Geography
Location, neighbors, official area, centroid/boundary, elevations when supported and land-use summary.

## Geology
Mapped unit code/name, lithology, age, source scale, structures, geometry and interpretation limitations.

## Soil background
Soil class/series, horizon/depth, texture, pH, organic matter, CEC, bulk density, hydraulic properties and background analytes. Each concentration records analyte, value/statistic, unit, sample count, depth, method, spatial population and source. Regulatory criteria are stored separately.

## Surface hydrology
Waterbody/river/drainage identifiers, catchment, flow or stage observations, flood-related layers, periods and station/source relations.

## Groundwater/hydrogeology
Hydrogeologic unit, aquifer/aquitard, well/station, screen interval, water level datum, observation time, quality parameters and uncertainty.

## Population
Year/month, population, households, age/sex where available, village/administrative level and density calculated from version-matched area.

## Climate/rainfall
Station identity, station distance/elevation, variable, temporal aggregation, completeness, units and ten-year analysis window.

## Pollution sites
Authoritative site identifier, regulatory status, pollutants/media, announcement/status dates, location precision, area and source. Proximity analysis is a derived relation, never evidence of causation.

## Sensitive areas
Category, legal/technical basis, geometry, effective/version dates, restrictions/notes and source.

## Investigation history
Public project/report identity, investigation dates, locations, media, methods, analytes, summarized findings, document references and confidentiality level.