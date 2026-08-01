# Issue相依關係與交付地圖

## 目的
讓Codex依正確順序開發，避免在基礎架構、資料模型或來源治理尚未完成前先做高階功能。

## 主路徑

```text
#1 Production foundation
 ├─> #3 Database migrations
 │    └─> #4 FastAPI/OpenAPI
 │         ├─> #2 Source registry model
 │         │    └─> #5 Monthly synchronization
 │         ├─> #6 Local Environmental Database UI
 │         ├─> #7 GIS workspace
 │         ├─> #8 AI report generation
 │         │    └─> #9 Report builder and export
 │         ├─> #10 Article 8/9 evaluation
 │         │    └─> #11 Control/remediation workspace
 │         └─> #12 Project workspace and field survey
 └────────────────────────────────────────> #13 Acceptance/security/release gates
```

## 建議執行批次

### Batch A：技術基礎
- #1 建立Monorepo、Docker、CI與測試框架
- #3 建立PostgreSQL/PostGIS Migration
- #4 實作OpenAPI與FastAPI契約

交付：可啟動的開發環境、健康檢查、資料庫與API契約測試。

### Batch B：資料治理
- #2 資料來源登錄、快照、版本與時效模型
- #5 每月同步、驗證、發布與失敗保留上一版

交付：至少一個經核准來源的端到端同步示範；不得使用假官方資料。

### Batch C：地方環境資料MVP
- #6 行政區查詢與環境章節介面
- #7 GIS圖層、定位、套疊、距離及輸出

交付：選擇縣市／鄉鎮後可查看資料狀態、來源、最後更新時間、圖表與地圖。

### Batch D：報告生成
- #8 有證據的AI章節生成
- #9 編輯、版本、審核、DOCX/PDF輸出

交付：預設880字、自訂字數、逐段證據、APA 7、可複製與Word輸出。

### Batch E：專業工作流程
- #10 第8／9條初步判定
- #11 控制／整治計畫工作區
- #12 專案管理及iPhone現勘

交付：所有高風險結論皆有版本化規則、證據、限制與專業核准。

### Batch F：正式發布
- #13 自動驗收、權限、資安、資料品質與發布門檻

## Pull Request規則
- 每個Issue原則上一個PR。
- PR需引用Issue及對應規格檔。
- 不得在同一PR同時大量變更基礎架構與業務規則。
- 所有Migration、API與資料映射需有測試。
- 發現規格衝突時先建立Decision Record，不可自行猜測。

## Definition of Ready
Issue開始前必須具備：
- 明確範圍與非範圍
- 相依Issue已完成
- 介面或資料契約存在
- 驗收條件存在
- 來源授權及專業規則已核准（適用時）

## Definition of Complete
- 程式、測試、文件與Migration完成
- CI通過
- 無假資料冒充官方資料
- 資料來源與最後更新時間可追溯
- 權限與租戶隔離測試通過
- 專業／法規功能完成指定人工審核
