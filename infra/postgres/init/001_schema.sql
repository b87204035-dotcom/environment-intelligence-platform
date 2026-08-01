CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS projects (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  name text NOT NULL,
  client_name text,
  status text NOT NULL DEFAULT 'draft',
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS parcels (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  project_id uuid REFERENCES projects(id) ON DELETE CASCADE,
  county text,
  district text,
  section_name text,
  parcel_no text,
  address text,
  geometry geometry(MultiPolygon, 4326),
  source_name text,
  source_updated_at timestamptz,
  created_at timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS parcels_geometry_gix ON parcels USING gist (geometry);

CREATE TABLE IF NOT EXISTS contaminated_sites (
  id text PRIMARY KEY,
  site_name text NOT NULL,
  control_type text,
  status text,
  pollutants jsonb NOT NULL DEFAULT '[]'::jsonb,
  announcement_date date,
  release_date date,
  authority text,
  source_url text,
  geometry geometry(Geometry, 4326),
  source_updated_at timestamptz,
  synced_at timestamptz NOT NULL DEFAULT now(),
  raw_payload jsonb NOT NULL DEFAULT '{}'::jsonb
);
CREATE INDEX IF NOT EXISTS contaminated_sites_geometry_gix ON contaminated_sites USING gist (geometry);

CREATE TABLE IF NOT EXISTS regulatory_industries (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  official_name text NOT NULL,
  official_definition text NOT NULL,
  applies_article_8 boolean NOT NULL DEFAULT false,
  applies_article_9 boolean NOT NULL DEFAULT false,
  effective_from date,
  effective_to date,
  legal_source text NOT NULL,
  required_analytes jsonb NOT NULL DEFAULT '[]'::jsonb,
  recommended_analytes jsonb NOT NULL DEFAULT '[]'::jsonb,
  evidence_requirements jsonb NOT NULL DEFAULT '[]'::jsonb,
  version text NOT NULL
);

CREATE TABLE IF NOT EXISTS samples (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  project_id uuid NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
  sample_code text NOT NULL,
  media text NOT NULL,
  depth_from_m numeric,
  depth_to_m numeric,
  analytes jsonb NOT NULL DEFAULT '[]'::jsonb,
  rationale text,
  geometry geometry(Point, 4326) NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(project_id, sample_code)
);
CREATE INDEX IF NOT EXISTS samples_geometry_gix ON samples USING gist (geometry);

CREATE TABLE IF NOT EXISTS field_photos (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  project_id uuid NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
  object_key text NOT NULL,
  captured_at timestamptz,
  heading_degrees numeric,
  description text,
  geometry geometry(Point, 4326),
  exif jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS field_photos_geometry_gix ON field_photos USING gist (geometry);

CREATE TABLE IF NOT EXISTS data_sync_runs (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  source_key text NOT NULL,
  official_updated_at timestamptz,
  started_at timestamptz NOT NULL DEFAULT now(),
  downloaded_at timestamptz,
  validated_at timestamptz,
  published_at timestamptz,
  status text NOT NULL,
  source_record_count integer,
  inserted_count integer,
  updated_count integer,
  deleted_count integer,
  error_message text,
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb
);
CREATE INDEX IF NOT EXISTS data_sync_runs_source_started_idx ON data_sync_runs(source_key, started_at DESC);
