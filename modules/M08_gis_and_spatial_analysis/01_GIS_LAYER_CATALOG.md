# GIS 圖層目錄與 Metadata 標準

## 1. 圖層分類

| 類別 | 主要圖層 | 幾何 | 最低必要屬性 |
|---|---|---|---|
| 行政區 | 縣市、鄉鎮市區、村里 | Polygon/MultiPolygon | code、name、valid_from、valid_to |
| 地籍 | 段、小段、地號、宗地界 | Polygon | county、town、section、parcel_no、source_id |
| 影像底圖 | 航照、正射影像、衛星影像 | Raster/Tile | capture_date、resolution、license |
| 地形 | DEM、等高線、坡度、坡向 | Raster/Line | vertical_datum、resolution、derived_from |
| 地質 | 地質圖、斷層、鑽探、敏感區 | Polygon/Line/Point | unit_code、age、lithology、scale |
| 土壤 | 土壤類別、母質、背景值範圍 | Polygon/Point | soil_code、depth、analyte、statistic |
| 地表水 | 河川、排水、水體、集水區 | Line/Polygon | waterbody_id、name、class、basin |
| 地下水 | 觀測井、含水層、地下水分區 | Point/Polygon | well_id、screen_depth、aquifer、status |
| 污染場址 | 控制、整治、公告及解除場址 | Point/Polygon | site_id、status、pollutants、announcement_date |
| 環境敏感區 | 飲用水、保育、洪氾、地質等 | Polygon | sensitivity_type、legal_basis、effective_date |
| 專案 | 基地、現勘、照片、採樣、鑽孔、井 | Point/Line/Polygon | project_id、evidence_class、created_by |

## 2. 圖層 Metadata 必填欄位

```json
{
  "layer_id": "string",
  "layer_name_zh": "string",
  "category": "administrative|cadastral|imagery|terrain|geology|soil|surface_water|groundwater|contaminated_site|sensitive_area|project",
  "geometry_type": "Point|LineString|Polygon|MultiPolygon|Raster|Tile",
  "source_id": "uuid",
  "snapshot_id": "uuid",
  "source_agency": "string",
  "license_code": "string",
  "published_at": "date|null",
  "retrieved_at": "datetime",
  "last_successful_sync_at": "datetime",
  "crs": "EPSG code",
  "scale_or_resolution": "string|null",
  "coverage": "string",
  "quality_status": "current|due|stale|invalid|unavailable",
  "access_level": "public|tenant|project|restricted",
  "style_version": "string",
  "schema_version": "string"
}
```

## 3. 版本與時效

- 原始快照以 `snapshot_id` 唯一識別，不得覆寫。
- 每次同步須記錄新增、修改、刪除與無變更筆數。
- 圖層頁面同時顯示：來源發布日、資料期間、擷取日、最後成功同步時間。
- 來源沒有新版時，記錄「已檢查、無新版」，不得更新發布日期。
- 法規或公告範圍應保存 `effective_from`、`effective_to` 與法律來源版本。

## 4. 圖徵必要欄位

所有向量圖徵至少具有：

- `feature_id`
- `source_feature_id`
- `snapshot_id`
- `geometry`
- `geometry_original_crs`
- `geometry_transformation_id`
- `valid_from`／`valid_to`
- `properties_json`
- `quality_flags`
- `created_at`

## 5. 樣式與顯示

- 樣式與資料分離，採 `style_version` 管理。
- 污染場址以狀態而非污染物濃度作主要符號分類。
- 敏感區應支援多重重疊與透明度控制。
- 地籍、航照及專案資料需依權限決定可見尺度與屬性。
- 不可因符號顏色或圖例文字暗示未經證實的污染結論。
