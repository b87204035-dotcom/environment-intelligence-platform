# 02 基地、地號與利害關係人模型

## 1. Site
必填欄位：`site_id`, `project_id`, `name`, `address_raw`, `county_code`, `town_code`, `geometry`, `crs`, `location_source`, `location_accuracy_m`, `created_at`。

`location_source` 可為 `address_geocode`, `parcel`, `gps`, `manual_map`, `official_document`。

## 2. Parcel
欄位：`parcel_id`, `site_id`, `county_code`, `office_code`, `section_code`, `subsection_code`, `land_no_main`, `land_no_sub`, `geometry`, `source_id`, `snapshot_id`, `verified_status`。

地號輸入與官方定位結果必須分開保存；查無結果不得自行補造。

## 3. Party 與 Contact
角色至少包含：土地所有權人、使用人、事業負責人、承租人、客戶窗口、現場陪同人、主管機關、技師、採樣與實驗室人員。

保存：姓名或組織名稱、角色、聯絡方式、資料來源、同意與使用限制。個資須依最小化原則保存。

## 4. Site Boundary
基地邊界可來自地籍、客戶圖面、GPS 軌跡或人工繪製。每一版邊界須保存：
- 幾何與座標系統
- 來源與日期
- 建立者
- 精度與限制
- 是否經專業確認

## 5. 衝突處理
地址、地號、GPS 與圖面不一致時，系統須顯示衝突，不得自動選定其中之一為正式結果。正式邊界需人工確認。

## 6. JSON 範例
```json
{
  "site_id": "site_001",
  "address_raw": "嘉義縣民雄鄉...",
  "town_code": "10010050",
  "location_source": "parcel",
  "location_accuracy_m": 3.0,
  "boundary_status": "pending_professional_review"
}
```
