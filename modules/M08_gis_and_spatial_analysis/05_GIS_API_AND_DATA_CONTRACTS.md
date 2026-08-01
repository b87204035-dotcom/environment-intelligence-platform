# GIS API 與資料契約

## 1. API 範圍

- `GET /api/v1/gis/layers`
- `GET /api/v1/gis/layers/{layer_id}`
- `POST /api/v1/gis/geocode/address`
- `POST /api/v1/gis/geocode/parcel`
- `POST /api/v1/gis/locate/gps`
- `POST /api/v1/gis/analysis/point-in-polygon`
- `POST /api/v1/gis/analysis/buffer`
- `POST /api/v1/gis/analysis/intersection`
- `POST /api/v1/gis/analysis/nearest`
- `POST /api/v1/gis/analysis/area-summary`
- `POST /api/v1/gis/maps/render`
- `GET /api/v1/gis/analysis/{analysis_id}`

## 2. 共通回應

```json
{
  "status": "completed|completed_with_warning|insufficient_data|failed",
  "request_id": "uuid",
  "data": {},
  "warnings": [],
  "errors": [],
  "sources": [
    {
      "source_id": "uuid",
      "snapshot_id": "uuid",
      "published_at": "2026-01-01",
      "last_successful_sync_at": "2026-08-01T00:00:00+08:00",
      "quality_status": "current"
    }
  ]
}
```

## 3. 空間輸入契約

```json
{
  "geometry": {
    "type": "Point",
    "coordinates": [121.0, 23.5]
  },
  "crs": "EPSG:4326",
  "layer_ids": ["contaminated_sites"],
  "snapshot_policy": "latest_approved|as_of_date|explicit",
  "as_of_date": "2026-08-01",
  "parameters": {
    "distance_m": 500
  }
}
```

## 4. 圖層回應欄位

每個圖徵至少回傳：`feature_id`、`geometry`、`properties`、`source_id`、`snapshot_id`、`published_at`、`last_successful_sync_at`、`quality_flags`、`legal_or_professional_review_required`。

## 5. 地址、地號與 GPS

- 地址定位回傳候選清單、標準化地址、信心值與定位服務。
- 地號定位回傳縣市、鄉鎮、段小段、地號、宗地幾何及資料日期。
- GPS 回傳原始座標、精度、轉換座標與行政區歸屬。
- 多候選或低信心不得自動選定，回傳 `user_confirmation_required`。

## 6. 權限

- 公開圖層可匿名或一般登入查詢。
- 地籍、客戶基地、現勘照片與專案圖層依租戶及案件權限。
- API 不得因查詢結果洩漏其他租戶的專案位置或附件。
- 匯出須重新檢查每個圖層授權與使用者權限。

## 7. 錯誤碼

`GIS-400-INVALID-GEOMETRY`、`GIS-400-UNKNOWN-CRS`、`GIS-404-LAYER`、`GIS-409-AMBIGUOUS-LOCATION`、`GIS-422-OUT-OF-COVERAGE`、`GIS-424-SOURCE-UNAVAILABLE`、`GIS-403-PERMISSION`、`GIS-500-TRANSFORMATION`。

## 8. 非同步工作

大型套疊與地圖輸出採工作佇列，回傳 `job_id`；工作紀錄保存輸入雜湊、來源快照、執行器版本、進度、錯誤與輸出檔案雜湊。
