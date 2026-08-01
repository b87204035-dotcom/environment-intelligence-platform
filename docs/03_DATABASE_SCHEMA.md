# 03 Database Schema

## 1. Design rules

- Primary keys: UUID.
- Spatial reference: store original CRS metadata; normalized geometry in EPSG:4326 and Taiwan analysis CRS where required.
- Every imported record includes source dataset, source record key, data date, retrieved time, import batch and publication version.
- Soft delete only for user content; imported snapshots remain immutable.

## 2. Core tables

### Identity and projects
- `users`, `organizations`, `memberships`, `roles`
- `projects`, `project_sites`, `parcels`, `project_members`
- `project_files`, `field_photos`, `map_annotations`, `project_events`

### Geography
- `admin_counties`, `admin_towns`, `admin_villages`
- `addresses`, `cadastral_sections`, `land_parcels`
- `land_use_zones`, `land_cover_snapshots`, `elevation_stats`

### Environmental datasets
- `geologic_units`, `faults`, `geologic_sensitive_areas`
- `soil_units`, `soil_properties`, `soil_background_values`
- `rivers`, `drainage_basins`, `flood_hazard_areas`
- `groundwater_regions`, `aquifers`, `monitoring_wells`, `groundwater_observations`
- `weather_stations`, `weather_monthly_stats`, `rainfall_monthly_stats`
- `population_annual_stats`, `population_age_stats`, `population_village_stats`
- `pollution_sites`, `pollution_site_contaminants`, `pollution_site_status_history`
- `environmental_sensitive_areas`, `investigation_records`

### Law and professional modules
- `laws`, `law_versions`, `law_provisions`, `legal_notices`, `legal_interpretations`
- `announced_business_categories`, `business_category_versions`
- `legal_assessments`, `legal_assessment_facts`, `legal_assessment_results`
- `control_plans`, `remediation_plans`, `plan_sections`, `review_comments`
- `remediation_methods`, `method_applicability_rules`, `cost_assumptions`

### Sources and provenance
- `source_publishers`, `source_datasets`, `source_endpoints`
- `source_snapshots`, `import_batches`, `validation_results`
- `data_publications`, `record_provenance`
- `references`, `reference_authors`, `reference_links`

### Reports and AI
- `report_templates`, `reports`, `report_sections`, `report_versions`
- `generation_requests`, `generation_evidence`, `generation_outputs`
- `section_citations`, `figures`, `tables`, `export_jobs`

## 3. Minimum provenance columns

`source_dataset_id`, `source_record_id`, `source_data_date`, `retrieved_at`, `import_batch_id`, `publication_id`, `quality_grade`, `geometry`, `raw_payload_hash`.

## 4. Quality grade

- A: official structured data, current and validated
- B: official publication requiring transformation
- C: peer-reviewed or recognized technical source
- D: local/project document not independently verified
- U: unknown or pending verification

## 5. Key relationships

- Towns link to all environmental statistics by `town_id` and time period.
- Spatial features may intersect multiple towns; use relation tables with area/length proportion.
- Report sections link to evidence records and references through many-to-many citation mapping.
- Legal assessments preserve input facts, law version and rule result as a frozen version.