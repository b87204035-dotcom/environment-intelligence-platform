import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Literal

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

DATA_ROOT = Path(os.getenv("DATA_ROOT", "/data"))
app = FastAPI(title="Environment Intelligence Platform API", version="0.2.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class LocationQuery(BaseModel):
    mode: Literal["address", "parcel", "gps"]
    address: str | None = None
    county: str | None = None
    district: str | None = None
    section: str | None = None
    parcel_no: str | None = None
    latitude: float | None = Field(default=None, ge=-90, le=90)
    longitude: float | None = Field(default=None, ge=-180, le=180)


class IndustryAssessmentRequest(BaseModel):
    business_name: str = ""
    industry_keywords: list[str] = Field(default_factory=list)
    processes: list[str] = Field(default_factory=list)
    chemicals: list[str] = Field(default_factory=list)


def read_json(relative_path: str, fallback: dict) -> dict:
    path = DATA_ROOT / relative_path
    if not path.exists():
        return fallback
    return json.loads(path.read_text(encoding="utf-8"))


@app.get("/health")
def health() -> dict:
    return {
        "status": "ok",
        "service": "eip-api",
        "version": app.version,
        "time": datetime.now(timezone.utc).isoformat(),
    }


@app.post("/v1/location/resolve")
def resolve_location(payload: LocationQuery) -> dict:
    if payload.mode == "gps" and payload.latitude is not None and payload.longitude is not None:
        return {
            "status": "resolved",
            "query": payload.model_dump(),
            "point": {"type": "Point", "coordinates": [payload.longitude, payload.latitude]},
            "parcel_status": "pending_official_connector",
        }
    return {
        "status": "pending_official_connector",
        "query": payload.model_dump(),
        "message": "地址及地號查詢必須接入官方定位與地籍服務，不回傳假定位結果。",
    }


@app.get("/v1/contaminated-sites/nearby")
def nearby_sites(
    latitude: float = Query(ge=-90, le=90),
    longitude: float = Query(ge=-180, le=180),
    radius_m: int = Query(default=1000, ge=1, le=50000),
) -> dict:
    sync = read_json("sync/status.json", {"status": "never_synced"})
    return {
        "type": "FeatureCollection",
        "features": [],
        "query": {"latitude": latitude, "longitude": longitude, "radius_m": radius_m},
        "data_status": sync,
    }


@app.post("/v1/regulations/articles-8-9/assess")
def assess_articles_8_9(payload: IndustryAssessmentRequest) -> dict:
    rules = read_json("regulations/article_8_9_seed.json", {"industries": []})
    haystack = " ".join(
        [payload.business_name, *payload.industry_keywords, *payload.processes, *payload.chemicals]
    ).lower()
    matches = []
    for industry in rules.get("industries", []):
        aliases = industry.get("aliases", [])
        matched_aliases = [alias for alias in aliases if alias.lower() in haystack]
        if matched_aliases:
            matches.append({**industry, "matched_aliases": matched_aliases})

    classification = "potential_match" if matches else "insufficient_evidence"
    pollutants = sorted({p for item in matches for p in item.get("potential_pollutants", [])})
    return {
        "classification": classification,
        "article_8": "requires_transaction_context",
        "article_9": "requires_business_and_event_context",
        "matches": matches,
        "recommended_analysis_candidates": pollutants,
        "inputs": payload.model_dump(),
        "required_evidence": [
            "實際營業或製程內容",
            "公告事業正式定義比對",
            "土地移轉或設立、停歇業、變更等法定觸發事件",
            "原物料、化學品、廢棄物及許可資料",
        ],
        "legal_disclaimer": rules.get("disclaimer", "本結果為系統初判，不取代主管機關認定。"),
    }


@app.get("/v1/regulations/articles-8-9/industries")
def list_industries() -> dict:
    return read_json("regulations/article_8_9_seed.json", {"industries": [], "status": "missing"})


@app.get("/v1/data-sources")
def data_sources() -> dict:
    catalog = read_json("source_catalog.json", {"sources": []})
    sync = read_json("sync/status.json", {"status": "never_synced", "sources": []})
    return {
        "minimum_sync_frequency": catalog.get("minimum_sync_frequency", "monthly"),
        "catalog": catalog.get("sources", []),
        "last_sync": sync,
    }
