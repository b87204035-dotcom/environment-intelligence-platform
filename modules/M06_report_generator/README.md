# M06 AI報告產生器與引用系統

## 目的
建立可追溯、可審核、可版本化的環境報告產生架構，支援地方環境基本資料、土污法第8／9條、Phase I ESA、控制計畫、整治計畫、調查及監測報告。

## 核心原則
- AI只能依已登錄證據產生內容。
- 每一事實性段落必須可追溯至資料來源、資料版本及證據片段。
- 預設章節長度為880字，使用者可自訂；系統回傳實際字數與偏差。
- 缺資料、來源衝突或資料過期時，必須顯示限制，不得補造結論。
- AI草稿、人工編修、技師審核及正式發布版本必須分離。
- Word與PDF輸出應保留章節、圖表、引用、資料日期及最後更新時間。

## 文件
1. `01_REPORT_DOCUMENT_MODEL.md`
2. `02_SECTION_GENERATION_RULES.md`
3. `03_EVIDENCE_AND_CITATION_ENGINE.md`
4. `04_WORD_PDF_EXPORT_STANDARD.md`
5. `05_VERSION_REVIEW_AND_QA.md`
6. `06_REPORT_TEMPLATE_LIBRARY.md`
7. `07_CODEX_INTEGRATION_BACKLOG.md`

## 相依模組
- M01 官方資料來源
- M02 污染物與產業知識庫
- M03 採樣與分析
- M04 控制與整治
- M05 法規規則引擎

## 非範圍
本模組不實作模型呼叫、DOCX渲染或前端編輯器；其內容作為Codex實作契約。