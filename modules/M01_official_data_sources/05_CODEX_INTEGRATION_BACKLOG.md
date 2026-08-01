# Codex 介接 Backlog v1.0

## 目標
將M01資料來源規格轉為可執行的來源登錄、同步、驗證、發布與前端揭露功能。

## 工作包
### WP1 來源登錄
- 建立publisher、dataset、endpoint、license、citation、refresh policy資料表。
- 支援API、檔案、OGC服務與人工匯入。
- 實作Metadata必填與狀態驗證。

### WP2 不可變快照
- 原始檔案物件儲存。
- SHA-256、大小、下載時間、HTTP Metadata。
- 禁止覆寫與刪除已發布快照。

### WP3 匯入與驗證
- Schema mapping、型別與單位轉換。
- 筆數、唯一性、日期、值域及GIS品質檢查。
- 版本差異報告與人工核准門檻。

### WP4 更新排程
- 依來源頻率排程，所有啟用來源至少每月檢查。
- current、due、stale、unavailable、retired狀態。
- 失敗重試、告警與保留上一版。

### WP5 API與前端
- `/sources`、`/sources/{id}`、`/snapshots`、`/sync-runs`、`/freshness`。
- 每一環境章節提供來源抽屜、資料日期、最後同步、限制與APA引用。
- 管理頁可檢視失敗、待核准與逾期來源。

### WP6 首批P0來源
按下列順序驗證與導入：
1. 行政區界與代碼。
2. 戶政人口。
3. 氣象測站、氣溫與雨量。
4. 河川、水系與地下水觀測井。
5. 地質與土壤圖。
6. 污染場址、污染管制區及列管歷程。
7. 公告事業與土污法規／指引。

## Definition of Done
- 每一來源有核准Metadata、授權、引用及欄位映射。
- 原始快照與發布版本可回溯。
- 同步失敗不破壞上一版。
- API與UI顯示資料期間和最後更新時間。
- 至少一個來源完成端到端自動同步測試。
- 無任何假資料冒充官方資料。
- 文件與Issue #2、#5的驗收條件一致。