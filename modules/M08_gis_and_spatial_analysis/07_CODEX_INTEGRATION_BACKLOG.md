# Codex 整合 Backlog

## 工作包 A：資料模型

- 建立 `gis_layers`、`gis_layer_snapshots`、`gis_features`、`gis_styles`、`coordinate_transformations`、`spatial_analysis_jobs`、`map_exports`。
- PostGIS 幾何欄位、SRID 約束、GIST 索引與租戶欄位。
- 原始幾何、轉換幾何、快照與品質旗標不可混用。

## 工作包 B：資料導入

- 建立行政區、地籍、地質、土壤、水文、地下水、污染場址與敏感區 Adapter 介面。
- 保存原始檔、內容雜湊、授權、Schema、同步紀錄及欄位映射。
- 提供重跑、回復上一快照與資料差異報告。

## 工作包 C：定位服務

- 地址標準化與多候選確認。
- 地號查詢及宗地定位介面。
- GPS 精度、座標轉換與行政區歸屬。
- 所有外部服務金鑰以秘密管理，不寫入程式庫。

## 工作包 D：空間分析服務

- Point-in-polygon、Buffer、Intersection、Nearest、Distance、Area summary。
- 大型工作採非同步佇列。
- 保存輸入、參數、來源快照、執行器版本、輸出與雜湊。
- 分析結果附警告與限制，不自動產生污染或法律結論。

## 工作包 E：Web GIS

- 圖層樹、透明度、順序、篩選、點選、量距、量面積及列印。
- 地址、地號與 GPS 搜尋。
- 點線面繪製、專案基地、照片、採樣、鑽孔與井位。
- 行動版適合 iPhone 使用，並與 M09 共用資料契約。

## 工作包 F：地圖輸出

- 產出 PNG、SVG、PDF 與 DOCX 可嵌入圖檔。
- 自動加入圖名、圖例、比例尺、指北針、CRS、來源及日期。
- 已發布報告鎖定圖層快照與樣式版本。

## 工作包 G：測試與安全

- CRS 轉換、幾何有效性、邊界案例、面積與距離測試。
- 圖層權限、跨租戶隔離與簽名下載連結。
- 輸入大小、複雜度、查詢範圍與頻率限制。
- 民雄鄉測試資料須標示為 synthetic。

## 建議實作順序

1. 資料模型與 Migration。
2. CRS／幾何共用函式。
3. 圖層 Registry 與 Snapshot。
4. 空間分析 API。
5. Web GIS 與定位。
6. 地圖輸出。
7. M06 報告、M09 現勘、M10 品質整合。

## Definition of Done

- 文件、Schema、Migration、API、測試與操作說明齊全。
- 所有正式空間結果可由輸入與快照重現。
- 無未授權圖層或跨租戶資料洩漏。
- 不新增 M11 以上頂層模組。
