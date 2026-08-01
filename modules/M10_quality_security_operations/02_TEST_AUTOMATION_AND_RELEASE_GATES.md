# 測試自動化與發布門檻

## 測試矩陣
- Unit：資料轉換、狀態機、字數與引用規則。
- Integration：資料庫、物件儲存、排程、AI、GIS。
- API Contract：OpenAPI、錯誤碼、權限、分頁與冪等。
- GIS：CRS、幾何、距離、面積、套疊與地圖輸出。
- AI Grounding：證據完整性、缺資料、衝突、Prompt injection。
- DOCX/PDF：標題、目錄、圖表、引用、中文字型與分頁。
- Security：認證、授權、租戶隔離、檔案上傳、秘密與依賴掃描。
- Performance：查詢、地圖、報告、同步及併發。
- UAT：地方查詢、報告、現勘、法規與控制／整治流程。

## 發布 Gate
`lint -> unit -> integration -> contract -> security -> migration -> UAT -> professional_review -> release_approval`

任何 Blocker 或 Critical 未關閉不得發布。高風險法律、污染、整治與 AI 結論必須有專業審核證據。資料庫 migration 必須有 rollback 或向前修復方案。

## 版本
採語意版本；每次發布保存 Commit SHA、映像 digest、migration 版本、Prompt 版本、資料快照版本、核准人與發布時間。