from fastapi import APIRouter, Query
from psycopg.rows import dict_row
from .db import connection
router=APIRouter(prefix="/api/v1",tags=["Search"])
@router.get("/search")
def search(q:str|None=None,dataset_key:str|None=None,bbox:str|None=None,limit:int=Query(50,ge=1,le=200),offset:int=Query(0,ge=0)):
    clauses=[]; params=[]
    if q: clauses.append("r.search_vector @@ websearch_to_tsquery('simple',%s)"); params.append(q)
    if dataset_key: clauses.append("d.dataset_key=%s"); params.append(dataset_key)
    if bbox:
        try: values=[float(v) for v in bbox.split(",")]
        except ValueError: values=[]
        if len(values)!=4 or values[0]>=values[2] or values[1]>=values[3]:
            from fastapi import HTTPException
            raise HTTPException(422,"bbox must be min_lng,min_lat,max_lng,max_lat")
        clauses.append("r.geometry && ST_MakeEnvelope(%s,%s,%s,%s,4326)"); params.extend(values)
    where="WHERE "+" AND ".join(clauses) if clauses else ""
    sql=f"""SELECT r.id,r.source_record_id,r.source_data_date,r.retrieved_at,r.quality_grade,r.properties,
      CASE WHEN r.geometry IS NULL THEN NULL ELSE ST_AsGeoJSON(r.geometry)::json END geometry,
      d.dataset_key,d.publisher,d.title dataset_title,d.landing_url,b.id batch_id,b.sha256 snapshot_sha256
      FROM environmental_records r JOIN source_datasets d ON d.id=r.source_dataset_id JOIN import_batches b ON b.id=r.import_batch_id
      {where} ORDER BY r.retrieved_at DESC,r.id LIMIT %s OFFSET %s"""
    with connection() as conn: rows=conn.execute(sql,(*params,limit,offset),row_factory=dict_row).fetchall()
    return {"items":rows,"limit":limit,"offset":offset}
