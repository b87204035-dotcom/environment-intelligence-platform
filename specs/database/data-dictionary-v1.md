# EICP Database Data Dictionary v1

## Conventions
- Primary keys: UUID v7.
- Timestamps: `timestamptz` in UTC; UI renders Asia/Taipei.
- Spatial reference: storage in EPSG:4326; projected analysis must record the working CRS.
- Every imported fact must carry `source_snapshot_id`, `valid_from`, `valid_to`, `observed_at`, `published_at`, `retrieved_at`, and `quality_status` where applicable.
- Raw source snapshots are immutable.
- Soft deletion is allowed only for user-created records; official imported facts are superseded, not deleted.

## Core administrative geography
### administrative_areas
- id uuid PK
- parent_id uuid FK administrative_areas nullable
- area_type varchar(20) NOT NULL: country/county/town/village
- official_code varchar(20) UNIQUE NOT NULL
- name_zh varchar(100) NOT NULL
- name_en varchar(150)
- area_km2 numeric(14,4)
- geom geometry(MultiPolygon,4326) NOT NULL
- centroid geometry(Point,4326)
- valid_from date NOT NULL
- valid_to date
- source_snapshot_id uuid FK source_snapshots
Indexes: gist(geom), parent_id, area_type, official_code.

### addresses
- id uuid PK
- normalized_address text NOT NULL
- administrative_area_id uuid FK
- location geometry(Point,4326)
- geocode_source varchar(50)
- confidence numeric(5,4)
- source_snapshot_id uuid FK

### cadastral_parcels
- id uuid PK
- administrative_area_id uuid FK
- section_code varchar(30)
- land_no_main varchar(20)
- land_no_sub varchar(20)
- display_land_no varchar(80)
- area_m2 numeric(16,2)
- geom geometry(MultiPolygon,4326)
- source_snapshot_id uuid FK
Unique version key: (section_code, land_no_main, land_no_sub, source_snapshot_id).

## Source and provenance
### source_publishers
- id uuid PK
- official_name text NOT NULL
- short_name text
- jurisdiction text
- homepage_url text
- contact_url text

### source_datasets
- id uuid PK
- publisher_id uuid FK
- dataset_key varchar(100) UNIQUE NOT NULL
- title text NOT NULL
- description text
- license_name text
- license_url text
- update_frequency varchar(30)
- expected_max_age_days integer
- source_url text
- citation_template text
- enabled boolean default true

### source_snapshots
- id uuid PK
- dataset_id uuid FK
- checksum_sha256 char(64) NOT NULL
- storage_uri text NOT NULL
- published_at timestamptz
- retrieved_at timestamptz NOT NULL
- row_count bigint
- schema_version varchar(40)
- validation_status varchar(20)
- metadata jsonb
Unique: (dataset_id, checksum_sha256).

### import_batches
- id uuid PK
- snapshot_id uuid FK
- started_at timestamptz
- finished_at timestamptz
- status varchar(20)
- inserted_count bigint
- updated_count bigint
- rejected_count bigint
- error_summary jsonb

### data_quality_results
- id uuid PK
- import_batch_id uuid FK
- rule_code varchar(80)
- severity varchar(20)
- passed boolean
- affected_count bigint
- details jsonb

## Environmental facts
### geology_units
- id uuid PK
- administrative_area_id uuid FK nullable
- unit_code varchar(50)
- unit_name text
- age_text text
- lithology text
- description text
- geom geometry(MultiPolygon,4326)
- source_snapshot_id uuid FK

### faults
- id uuid PK
- fault_name text
- activity_class varchar(50)
- description text
- geom geometry(MultiLineString,4326)
- source_snapshot_id uuid FK

### soil_mapping_units
- id uuid PK
- map_unit_code varchar(50)
- soil_series text
- taxonomy text
- texture text
- drainage_class text
- ph_min numeric(5,2)
- ph_max numeric(5,2)
- organic_matter_pct numeric(7,3)
- bulk_density_g_cm3 numeric(7,3)
- hydraulic_conductivity_value numeric(14,6)
- hydraulic_conductivity_unit varchar(30)
- geom geometry(MultiPolygon,4326)
- source_snapshot_id uuid FK

### soil_background_observations
- id uuid PK
- analyte_code varchar(40) NOT NULL
- statistic_type varchar(30) NOT NULL: measurement/mean/median/p90/p95/range
- value numeric(18,8)
- value_text text
- unit varchar(30) NOT NULL
- sample_count integer
- depth_from_m numeric(8,3)
- depth_to_m numeric(8,3)
- analytical_method text
- population_definition text NOT NULL
- applicability_note text
- location geometry(Point,4326)
- coverage geometry(MultiPolygon,4326)
- source_snapshot_id uuid FK NOT NULL
Rule: regulatory standards must never be stored in this table.

### regulatory_thresholds
- id uuid PK
- jurisdiction varchar(50)
- regulation_id uuid FK legal_documents
- matrix varchar(30)
- land_use_class varchar(50)
- analyte_code varchar(40)
- threshold_type varchar(50)
- value numeric(18,8)
- unit varchar(30)
- effective_from date
- effective_to date

### surface_water_features
- id uuid PK
- feature_type varchar(30): river/drain/catchment/reservoir/pond
- official_code varchar(50)
- name text
- geom geometry(Geometry,4326)
- attributes jsonb
- source_snapshot_id uuid FK

### hydrogeologic_units
- id uuid PK
- unit_code varchar(50)
- unit_name text
- aquifer_type varchar(50)
- permeability_class varchar(50)
- description text
- geom geometry(MultiPolygon,4326)
- source_snapshot_id uuid FK

### groundwater_stations
- id uuid PK
- official_code varchar(50)
- name text
- ground_elevation_m numeric(10,3)
- screen_top_m numeric(10,3)
- screen_bottom_m numeric(10,3)
- location geometry(Point,4326)
- source_snapshot_id uuid FK

### groundwater_observations
- id uuid PK
- station_id uuid FK
- observed_at timestamptz
- parameter_code varchar(50)
- value numeric(18,8)
- unit varchar(30)
- qualifier varchar(20)
- source_snapshot_id uuid FK
Unique: (station_id, observed_at, parameter_code, source_snapshot_id).

### climate_stations
- id uuid PK
- official_code varchar(50)
- name text
- station_type varchar(30)
- elevation_m numeric(10,3)
- location geometry(Point,4326)
- source_snapshot_id uuid FK

### climate_observations
- id uuid PK
- station_id uuid FK
- period_start timestamptz
- period_end timestamptz
- parameter_code varchar(50)
- aggregation varchar(20)
- value numeric(18,8)
- unit varchar(30)
- source_snapshot_id uuid FK

### population_statistics
- id uuid PK
- administrative_area_id uuid FK
- period date
- population_total integer
- male integer
- female integer
- households integer
- age_bands jsonb
- source_snapshot_id uuid FK
Unique: (administrative_area_id, period, source_snapshot_id).

### contaminated_sites
- id uuid PK
- official_site_id varchar(80)
- site_name text
- status_code varchar(50)
- site_category varchar(50)
- announcement_date date
- delisting_date date
- area_m2 numeric(16,2)
- pollutants jsonb
- address text
- geom geometry(Geometry,4326)
- source_snapshot_id uuid FK

### sensitive_areas
- id uuid PK
- sensitive_type varchar(80)
- level varchar(30)
- name text
- legal_basis_id uuid FK legal_documents nullable
- geom geometry(Geometry,4326)
- source_snapshot_id uuid FK

### investigation_history
- id uuid PK
- title text
- investigation_type varchar(80)
- organization text
- start_date date
- end_date date
- summary text
- parameters jsonb
- geom geometry(Geometry,4326)
- source_snapshot_id uuid FK
- reference_id uuid FK references

## Legal and professional rules
### legal_documents
- id uuid PK
- title text NOT NULL
- authority text
- document_type varchar(40)
- official_url text
- promulgated_at date
- effective_from date
- effective_to date
- version_hash char(64)
- source_snapshot_id uuid FK

### legal_rules
- id uuid PK
- legal_document_id uuid FK
- rule_code varchar(80) UNIQUE
- title text
- condition_expression jsonb
- outcome_code varchar(80)
- human_review_required boolean default true
- explanation_template text

### announced_business_categories
- id uuid PK
- category_code varchar(50)
- category_name text
- applicable_article varchar(20)
- required_analytes jsonb
- effective_from date
- effective_to date
- legal_document_id uuid FK

## Projects and field work
### projects
- id uuid PK
- project_no varchar(50) UNIQUE
- name text NOT NULL
- client_name text
- status varchar(30)
- owner_user_id uuid FK users
- started_at date
- due_at date
- metadata jsonb

### project_sites
- id uuid PK
- project_id uuid FK
- name text
- address_id uuid FK
- administrative_area_id uuid FK
- geom geometry(Geometry,4326)
- area_m2 numeric(16,2)

### field_observations
- id uuid PK
- project_site_id uuid FK
- observed_at timestamptz
- observer_user_id uuid FK
- observation_type varchar(50)
- note text
- location geometry(Point,4326)
- accuracy_m numeric(8,2)
- device_metadata jsonb
- sync_status varchar(20)

### media_assets
- id uuid PK
- project_id uuid FK
- observation_id uuid FK nullable
- object_uri text
- media_type varchar(30)
- checksum_sha256 char(64)
- captured_at timestamptz
- location geometry(Point,4326)
- direction_deg numeric(6,2)
- metadata jsonb

### sampling_points
- id uuid PK
- project_site_id uuid FK
- point_code varchar(50)
- media_type varchar(30): soil/groundwater/sediment/gas
- purpose text
- planned_depths jsonb
- analytes jsonb
- location geometry(Point,4326)
- design_status varchar(30)

### boreholes
- id uuid PK
- project_site_id uuid FK
- borehole_code varchar(50)
- total_depth_m numeric(10,3)
- drilling_method text
- location geometry(Point,4326)

### stratigraphy_intervals
- id uuid PK
- borehole_id uuid FK
- depth_from_m numeric(10,3)
- depth_to_m numeric(10,3)
- material_code varchar(50)
- description text
- sample_ref text

## Reports, citations and AI
### references
- id uuid PK
- reference_type varchar(30)
- title text
- authors jsonb
- organization text
- publication_year integer
- publisher text
- doi text
- url text
- accessed_at date
- apa7_text text
- source_snapshot_id uuid FK nullable

### evidence_items
- id uuid PK
- evidence_type varchar(30)
- source_table varchar(80)
- source_record_id uuid
- reference_id uuid FK
- excerpt text
- locator text
- data_period text
- confidence varchar(20)

### report_documents
- id uuid PK
- project_id uuid FK nullable
- report_type varchar(50)
- title text
- status varchar(30)
- template_version varchar(40)
- current_version_id uuid

### report_versions
- id uuid PK
- report_document_id uuid FK
- version_no integer
- created_by uuid FK users
- created_at timestamptz
- content_json jsonb
- source_snapshot_manifest jsonb
- prompt_manifest jsonb
- approved_by uuid FK users nullable
- approved_at timestamptz nullable

### report_sections
- id uuid PK
- report_version_id uuid FK
- section_code varchar(50)
- heading text
- target_characters integer default 880
- actual_characters integer
- content_html text
- generation_status varchar(30)
- review_status varchar(30)

### section_citations
- id uuid PK
- report_section_id uuid FK
- evidence_item_id uuid FK
- citation_order integer
- claim_text text

### ai_generation_runs
- id uuid PK
- report_section_id uuid FK nullable
- prompt_template_key varchar(100)
- prompt_version varchar(40)
- model_id varchar(100)
- requested_characters integer
- input_manifest jsonb
- output_text text
- validation_results jsonb
- created_at timestamptz

## Users, access and audit
### users
- id uuid PK
- email citext UNIQUE
- display_name text
- status varchar(20)

### organizations
- id uuid PK
- name text

### memberships
- id uuid PK
- organization_id uuid FK
- user_id uuid FK
- role varchar(30)

### audit_events
- id uuid PK
- actor_user_id uuid FK nullable
- organization_id uuid FK nullable
- action varchar(80)
- target_type varchar(80)
- target_id uuid nullable
- occurred_at timestamptz
- ip_hash text
- details jsonb

## Required constraints
1. Every published report section containing factual claims must have at least one `section_citations` row.
2. A legal decision output cannot be marked `final` unless `approved_by` is populated.
3. Published report versions and source snapshots are immutable.
4. All geometries must pass `ST_IsValid`; invalid records are quarantined.
5. Background concentrations and regulatory thresholds are stored separately and presented with distinct labels.
