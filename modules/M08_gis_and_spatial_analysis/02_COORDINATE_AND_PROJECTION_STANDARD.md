# 座標系統與投影標準

## 1. 標準座標

| 用途 | CRS | 規則 |
|---|---|---|
| 外部交換、GPS、Web 地圖 | EPSG:4326 WGS84 | 經度、緯度順序須明確；不得用於精確距離與面積 |
| Web Tile | EPSG:3857 | 僅供顯示；不得作正式距離與面積計算 |
| 臺灣本島正式分析 | TWD97 / TM2 121（常用 EPSG:3826） | 距離、面積、緩衝與工程圖主要分析 CRS |
| 澎湖及特定離島 | 依主管機關與資料來源指定 | 專案啟動時確認中央經線與 EPSG |
| 原始來源 | source CRS | 原始幾何與 CRS 必須保存，不得只留轉換後成果 |

## 2. 座標輸入

- GPS 輸入保存原始經緯度、水平精度、海拔、定位時間與裝置資訊。
- 地址與地號定位保存定位服務、回傳候選、信心值、人工選定結果與時間。
- 使用者手動點選保存畫面 CRS、縮放層級及底圖版本。
- 未知 CRS 的資料不得自動匯入正式圖層，狀態設為 `crs_confirmation_required`。

## 3. 轉換紀錄

每次轉換須建立：

```json
{
  "transformation_id": "uuid",
  "source_crs": "EPSG:4326",
  "target_crs": "EPSG:3826",
  "library": "PROJ",
  "library_version": "string",
  "operation": "string",
  "grid_file": "string|null",
  "executed_at": "datetime",
  "max_expected_error_m": 1.0,
  "status": "passed|warning|failed"
}
```

## 4. 計算規則

- 距離與緩衝：使用投影 CRS，單位公尺。
- 面積：投影 CRS，儲存平方公尺與換算公頃。
- 經緯度直線距離僅可作快速預覽，正式報告使用投影或測地線方法。
- 跨投影帶、離島或大範圍分析，需選用適合 CRS 或測地線演算法並揭露方法。
- 海拔需標示垂直基準；未知基準不得與其他高程直接比較。

## 5. 精度與有效位數

- GPS 精度大於設定門檻時顯示警告，不得假裝為地籍級定位。
- 地籍界址僅為查詢套繪，未經測量不得宣稱為現地界址認定。
- 報告座標有效位數依資料精度決定，不得顯示虛假精度。
- 轉換前後進行臺灣合理範圍、軸序、單位及控制點抽查。

## 6. 錯誤狀態

`unknown_crs`、`axis_order_suspected`、`out_of_bounds`、`transformation_failed`、`vertical_datum_unknown`、`accuracy_below_requirement`。
