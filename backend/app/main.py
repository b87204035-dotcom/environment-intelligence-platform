from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from psycopg.rows import dict_row
from .config import settings
from .db import connection, pool
@asynccontextmanager
async def lifespan(app: FastAPI):
    pool.open(); pool.wait()
    yield
    pool.close()
app=FastAPI(title="Environment Intelligence Platform API", version="0.1.0", lifespan=lifespan)
origins=[v.strip() for v in settings.cors_origins.split(",") if v.strip()]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["GET","POST"], allow_headers=["Authorization","Content-Type"])
@app.get("/health")
def health():
    with connection() as conn:
        conn.execute("SELECT 1")
    return {"status":"ok","database":"ok"}
@app.get("/api/v1/sources")
def sources():
    with connection() as conn:
        rows=conn.execute("""SELECT dataset_key,publisher,title,landing_url,endpoint_url,license,refresh_interval::text,
          CASE WHEN max(completed_at) IS NULL THEN 'unavailable' WHEN max(completed_at)+refresh_interval < now() THEN 'due' ELSE 'current' END freshness_status,
          max(completed_at) last_successful_sync_at FROM source_datasets d LEFT JOIN import_batches b ON b.source_dataset_id=d.id AND b.status='succeeded'
          WHERE enabled GROUP BY d.id ORDER BY dataset_key""", row_factory=dict_row).fetchall()
    return {"items":rows,"total":len(rows)}
from .search import router as search_router
app.include_router(search_router)
from .reports import router as reports_router
app.include_router(reports_router)
from .generation import router as generation_router
app.include_router(generation_router)
