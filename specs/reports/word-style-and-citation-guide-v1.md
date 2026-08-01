# Word Style and Citation Guide v1

## Default document settings

- Page: A4 portrait; landscape allowed for wide tables/maps.
- Language: Traditional Chinese (Taiwan).
- Body text: 12 pt equivalent, 1.5 line spacing, justified where appropriate.
- Heading levels: Heading 1 through Heading 4 with automatic numbering.
- Captions: 圖 X-X and 表 X-X, cross-referenceable.
- Units: SI units; preserve official source units and document conversions.
- Dates: YYYY年MM月DD日 in narrative; ISO 8601 in metadata.
- Coordinates: show CRS and precision.

## Section package

Each generated environmental section contains:

1. Heading
2. Narrative (default target 880 Chinese characters, configurable)
3. Key limitations
4. Table(s)
5. Figure/chart/map where applicable
6. Data freshness block
7. Section references

## Citation behavior

- Default bibliography style: APA 7 adapted for Taiwanese government datasets.
- Government dataset template: Agency. (Year or n.d.). *Dataset title* [Data set]. Platform/Agency. Retrieval date when content is continuously updated.
- Map/layer template: Agency. (Year or n.d.). *Layer title* [GIS data]. Scale/CRS/version when available.
- Law/guidance template: Issuing authority. (Year). *Title* (version/effective date).
- Do not cite a search engine result as the underlying source.
- Every table, chart and map must contain a source note.
- Repeated references are deduplicated in the report bibliography while paragraph evidence links remain preserved internally.

## Export quality controls

- Generate automatic table of contents and lists of figures/tables.
- Keep tables within printable margins; repeat header rows.
- Embed or package images at report-suitable resolution.
- Preserve editable text and tables; do not rasterize whole pages.
- Include report metadata, revision history, approval status and source appendix.
- Apply a visible DRAFT watermark to unapproved AI-generated reports.
- Store the approved content snapshot ID and export checksum.