"""Immutable importer for reviewed Taiwanese government open-data endpoints."""
import hashlib, ipaddress, json, socket
from pathlib import Path
from urllib.parse import urlparse
import httpx
from psycopg.rows import dict_row
from .config import settings
from .db import connection
from .source_formats import decode_records

def validate_official_url(url: str) -> None:
    parsed=urlparse(url)
    if parsed.scheme != "https" or not parsed.hostname or not parsed.hostname.lower().endswith(".gov.tw"):
        raise ValueError("Only reviewed HTTPS *.gov.tw endpoints are allowed")
    for result in socket.getaddrinfo(parsed.hostname, 443, type=socket.SOCK_STREAM):
        address=ipaddress.ip_address(result[4][0])
        if address.is_private or address.is_loopback or address.is_link_local or address.is_reserved:
            raise ValueError("Official endpoint resolved to a non-public address")

def sync_dataset(dataset_key: str) -> dict:
    with connection() as conn:
        dataset=conn.execute("SELECT * FROM source_datasets WHERE dataset_key=%s AND enabled",(dataset_key,),row_factory=dict_row).fetchone()
        if not dataset or not dataset["endpoint_url"]: raise ValueError("Enabled reviewed dataset endpoint not found")
        validate_official_url(dataset["endpoint_url"])
        batch=conn.execute("INSERT INTO import_batches(source_dataset_id,status,started_at) VALUES(%s,'running',now()) RETURNING id",(dataset["id"],)).fetchone()[0]
        conn.commit()
    try:
        with httpx.Client(timeout=60, follow_redirects=False) as client:
            response=client.get(dataset["endpoint_url"],headers={"Accept":"application/json,text/csv"}); response.raise_for_status()
        digest=hashlib.sha256(response.content).hexdigest()
        with connection() as conn:
            existing=conn.execute("SELECT id,record_count FROM import_batches WHERE source_dataset_id=%s AND sha256=%s AND status='succeeded'",(dataset["id"],digest)).fetchone()
            if existing:
                conn.execute("DELETE FROM import_batches WHERE id=%s",(batch,)); conn.commit()
                return {"batch_id":str(existing[0]),"dataset_key":dataset_key,"record_count":existing[1],"sha256":digest,"unchanged":True}
        root=Path(settings.source_snapshot_dir); root.mkdir(parents=True,exist_ok=True)
        path=root/f"{dataset_key}-{batch}-{digest[:12]}.raw"; path.write_bytes(response.content)
        records=decode_records(response.content,response.headers.get("content-type",""))
        with connection() as conn:
            for index, record in enumerate(records):
                record_id=str(record.get("id") or record.get("ID") or record.get("編號") or index)
                raw=json.dumps(record,ensure_ascii=False,sort_keys=True,separators=(",",":"))
                geometry=record.pop("_geometry",None)
                conn.execute("""INSERT INTO environmental_records(source_dataset_id,import_batch_id,source_record_id,retrieved_at,quality_grade,properties,geometry,raw_payload_hash)
                  VALUES(%s,%s,%s,now(),'A',%s,CASE WHEN %s IS NULL THEN NULL ELSE ST_SetSRID(ST_GeomFromGeoJSON(%s),4326) END,%s)""",
                  (dataset["id"],batch,record_id,json.dumps(record,ensure_ascii=False),json.dumps(geometry) if geometry else None,json.dumps(geometry) if geometry else None,hashlib.sha256(raw.encode()).hexdigest()))
            conn.execute("UPDATE import_batches SET status='succeeded',completed_at=now(),snapshot_path=%s,sha256=%s,record_count=%s WHERE id=%s",(str(path),digest,len(records),batch)); conn.commit()
        return {"batch_id":str(batch),"dataset_key":dataset_key,"record_count":len(records),"sha256":digest}
    except Exception as exc:
        with connection() as conn:
            conn.execute("UPDATE import_batches SET status='failed',completed_at=now(),error_detail=%s WHERE id=%s",(str(exc)[:2000],batch)); conn.commit()
        raise
