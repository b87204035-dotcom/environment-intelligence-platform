"""Core provenance, spatial, reports and generation schema."""
from alembic import op
revision="0001"; down_revision=None; branch_labels=None; depends_on=None

def upgrade():
    op.execute('CREATE EXTENSION IF NOT EXISTS postgis')
    op.execute('CREATE EXTENSION IF NOT EXISTS pg_trgm')
    op.execute("""
    CREATE TYPE quality_grade AS ENUM ('A','B','C','D','U');
    CREATE TYPE job_status AS ENUM ('pending','running','succeeded','failed');
    CREATE TABLE source_datasets (
      id uuid PRIMARY KEY DEFAULT gen_random_uuid(), dataset_key text UNIQUE NOT NULL,
      publisher text NOT NULL, title text NOT NULL, landing_url text NOT NULL,
      endpoint_url text, license text NOT NULL, refresh_interval interval NOT NULL,
      enabled boolean NOT NULL DEFAULT true, created_at timestamptz NOT NULL DEFAULT now());
    CREATE TABLE import_batches (
      id uuid PRIMARY KEY DEFAULT gen_random_uuid(), source_dataset_id uuid NOT NULL REFERENCES source_datasets(id),
      status job_status NOT NULL DEFAULT 'pending', started_at timestamptz, completed_at timestamptz,
      retrieved_at timestamptz NOT NULL DEFAULT now(), source_etag text, source_last_modified text,
      snapshot_path text, sha256 char(64), record_count integer, error_detail text,
      UNIQUE(source_dataset_id, sha256));
    CREATE TABLE environmental_records (
      id uuid PRIMARY KEY DEFAULT gen_random_uuid(), source_dataset_id uuid NOT NULL REFERENCES source_datasets(id),
      import_batch_id uuid NOT NULL REFERENCES import_batches(id), source_record_id text NOT NULL,
      source_data_date date, retrieved_at timestamptz NOT NULL, quality_grade quality_grade NOT NULL DEFAULT 'U',
      properties jsonb NOT NULL, geometry geometry(Geometry,4326), raw_payload_hash char(64) NOT NULL,
      search_vector tsvector GENERATED ALWAYS AS (to_tsvector('simple', coalesce(properties::text,''))) STORED,
      UNIQUE(source_dataset_id, source_record_id, import_batch_id));
    CREATE INDEX environmental_records_geometry_gix ON environmental_records USING gist(geometry);
    CREATE INDEX environmental_records_search_gin ON environmental_records USING gin(search_vector);
    CREATE TABLE projects (id uuid PRIMARY KEY DEFAULT gen_random_uuid(), name text NOT NULL, created_at timestamptz NOT NULL DEFAULT now());
    CREATE TABLE reports (id uuid PRIMARY KEY DEFAULT gen_random_uuid(), project_id uuid REFERENCES projects(id), title text NOT NULL, status text NOT NULL DEFAULT 'draft', created_at timestamptz NOT NULL DEFAULT now());
    CREATE TABLE report_sections (id uuid PRIMARY KEY DEFAULT gen_random_uuid(), report_id uuid NOT NULL REFERENCES reports(id) ON DELETE CASCADE, section_code text NOT NULL, heading text NOT NULL, content text, review_status text NOT NULL DEFAULT 'unreviewed', UNIQUE(report_id,section_code));
    CREATE TABLE generation_requests (id uuid PRIMARY KEY DEFAULT gen_random_uuid(), report_section_id uuid NOT NULL REFERENCES report_sections(id), model text NOT NULL, prompt_version text NOT NULL, evidence_ids uuid[] NOT NULL, status job_status NOT NULL DEFAULT 'pending', output text, warnings jsonb NOT NULL DEFAULT '[]', created_at timestamptz NOT NULL DEFAULT now());
    CREATE TABLE audit_events (id bigserial PRIMARY KEY, actor text NOT NULL, action text NOT NULL, entity_type text NOT NULL, entity_id text NOT NULL, occurred_at timestamptz NOT NULL DEFAULT now(), detail jsonb NOT NULL DEFAULT '{}');
    """)

def downgrade():
    op.execute('DROP TABLE audit_events, generation_requests, report_sections, reports, projects, environmental_records, import_batches, source_datasets CASCADE')
    op.execute('DROP TYPE job_status; DROP TYPE quality_grade')
