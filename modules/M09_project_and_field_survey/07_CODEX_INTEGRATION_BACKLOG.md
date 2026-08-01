# 07 Codex 整合 Backlog

## Epic M09-A：資料模型
- 建立 Project、Site、Parcel、Contact、FieldVisit、Observation、MediaAsset、SamplingLocation、Task、Review、ReportVersion、AuditEvent 資料表。
- 建立租戶隔離、索引、狀態機與 migration。

## Epic M09-B：API
- 專案、基地、地號、現勘、照片、點線面、任務、時間軸、審核與稽核 API。
- 支援分段上傳、續傳、雜湊去重及媒體衍生檔。
- 所有 API 套用 tenant、project 與角色權限。

## Epic M09-C：iPhone Web App
- 手機優先 PWA。
- GPS、相機、檔案、語音、離線快取、地圖標註與離場檢查。
- 清楚顯示同步狀態、錯誤、衝突及待補資料。

## Epic M09-D：證據與 AI
- A/B/C/D 證據分類。
- AI 摘要僅能使用已授權證據。
- 將摘要中的每項主張連結原始資產或觀察。

## Epic M09-E：報告與 GIS
- 將照片、點位、現勘表與時間軸提供給 M06。
- 將 Site、Parcel、Observation、SamplingLocation 提供給 M08。

## Epic M09-F：安全與測試
- 跨租戶隔離、離線加密、惡意檔案掃描、權杖撤銷。
- 單元、整合、端對端、離線、衝突、效能及 UAT。

## Definition of Done
- 通過 `docs/17_DEFINITION_OF_DONE.md` 與 `docs/19_CODE_REVIEW_CHECKLIST.md`。
- 不得虛構現勘、污染、法規或資料來源。
- 所有原始資產、修改、審核與發布均可追溯。
- 不新增 M11 以上頂層模組。
