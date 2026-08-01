from datetime import datetime, timezone
from typing import Literal

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(title="Environment Intelligence Platform API", version="0.1.0")
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
    industry_keywords: list[str] = []
    processes: list[str] = []
    chemicals: list[str] = []


@app.get("/health")
def health() -> dict:
    return {
        "status": "ok",
        "service": "eip-api",
        "time": datetime.now(timezone.utc).isoformat(),
    }


@app.post("/v1/location/resolve")
def resolve_location(payload: LocationQuery) -> dict:
    return {
        "status": "pending_official_connector",
        "query": payload.model_dump(),
        "message": "查詢模型已建立；地址、地號與 GPS 將分別接官方定位及地籍服務。",
    }


@app.get("/v1/contaminated-sites/nearby")
def nearby_sites(
    latitude: float = Query(ge=-90, le=90),
    longitude: float = Query(ge=-180, le=180),
    radius_m: int = Query(default=1000, ge=1, le=50000),
) -> dict:
    return {
        "type": "FeatureCollection",
        "features": [],
        "query": {"latitude": latitude, "longitude": longitude, "radius_m": radius_m},
        "data_status": "awaiting_moenv_sync",
    }


@app.post("/v1/regulations/articles-8-9/assess")
def assess_articles_8_9(payload: IndustryAssessmentRequest) -> dict:
    return {
        "classification": "insufficient_evidence",
        "article_8": "requires_transaction_context",
        "article_9": "requires_business_and_event_context",
        "inputs": payload.model_dump(),
        "required_evidence": [
            "實際營業或製程內容",
            "公告事業定義比對",
            "土地移轉或設立、停歇業、變更等觸發事件",
            "原物料、化學品、廢棄物及許可資料",
        ],
        "legal_disclaimer": "本結果為系統初判，不取代依法辦理的評估調查及主管機關認定。",
    }


@app.get("/v1/data-sources")
def data_sources() -> dict:
    return {
        "minimum_sync_frequency": "monthly",
        "sources": [],
        "message": "同步登錄表將記錄官方更新、本站下載、驗證、發布及錯誤時間。",
    }
