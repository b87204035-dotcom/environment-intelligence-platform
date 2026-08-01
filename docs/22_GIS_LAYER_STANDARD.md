# 22 GIS Layer Standard

## Required metadata
Every layer records title, abstract, responsible organization, source dataset/snapshot, license, native CRS, service CRS, scale/resolution, effective dates, retrieved/synchronized times, geometry type, fields, legend and limitations.

## Coordinate systems
- Store canonical vector geometry in an agreed Taiwan-appropriate projected CRS plus WGS84 representation where needed.
- Never transform coordinates without recording source CRS and transformation.
- Map exports state CRS and scale.

## Layer groups
- Administrative boundaries
- Basemaps and imagery references
- Terrain/elevation/slope
- Geology and geological sensitivity
- Soils and soil background sampling
- Rivers, drainage, catchments and flood-related layers
- Groundwater regions, wells and hydrogeologic units
- Pollution sites and regulated facilities
- Environmental sensitive areas
- Projects, parcels, field observations, samples, boreholes and wells

## Spatial analysis services
- Point-in-polygon
- Nearest features with explicit distance method
- Buffer search
- Layer intersection/overlap area
- Administrative-area aggregation
- Time/version selection

## Cartography
- Consistent layer naming and legends
- No red/green-only distinction
- Data status visible in symbology or legend
- Map output includes title, legend, scale, north arrow, source, date, CRS and disclaimer

## Precision and privacy
Location precision must match source accuracy. Restricted/private point data may be generalized for non-authorized viewers.