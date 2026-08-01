# Codex介接Backlog

## Work Package A：報告資料模型
- 建立Report、ReportVersion、Chapter、Section、Block、EvidenceLink、ReviewComment及ExportJob資料表。
- 已發布版本不可變，建立內容雜湊及租戶隔離。
- 驗收：Migration、索引、權限及不可變性測試通過。

## Work Package B：章節生成API
- 實作建立提綱、生成、重生、擴寫、縮寫、改寫及摘要API。
- 接受target_length，預設880字，回傳實際字數及偏差。
- 保存模型、Prompt、證據、參數與輸出。
- 缺證據時回傳明確限制，不得回傳假資料。

## Work Package C：證據與引用
- 建立段落－證據多對多關係。
- 實作APA 7產生器、正文引用與參考文獻雙向檢查。
- 支援來源抽屜、資料日期、版本及證據定位。
- 驗收：無幽靈引用、無未使用文獻、無虛構DOI。

## Work Package D：報告編輯器
- 章節樹、富文字、表格、圖表、地圖、引用及限制元件。
- 顯示來源狀態、最後更新、字數及QA結果。
- 支援版本差異、意見、退回、核准及鎖版。

## Work Package E：DOCX／PDF
- 依Style Profile輸出封面、目錄、圖表目錄、標題、原生表格、圖說、引用及附錄。
- 地圖含圖例、比例尺、指北針、座標系統、來源與日期。
- 驗收：DOCX可編輯、PDF版面一致、引用及頁碼正確。

## Work Package F：QA引擎
- unsupported claim、數值無證據、過期來源、字數、地名、單位、期間、圖文一致及法規版本檢查。
- Blocker與Critical阻擋發布。
- 來源更新觸發revalidation_required。

## Work Package G：模板管理
- 管理地方環境資料、第8／9條、Phase I、控制、整治及監測模板。
- 模板版本化、必要章節、字數、圖表、審核及法規有效期。

## 建議Issue
1. `M3-03 Implement report domain model and immutable versions`
2. `M3-04 Implement evidence-linked section generation API`
3. `M3-05 Implement citation engine and reference audit`
4. `M3-06 Build report editor and review workflow`
5. `M3-07 Implement DOCX/PDF rendering pipeline`
6. `M3-08 Implement report QA and release gates`
7. `M3-09 Implement versioned report template administration`

## Definition of Done
- 所有事實段落可追溯。
- 預設880字及自訂字數可驗證。
- 無證據不產生確定結論。
- DOCX／PDF通過內容與版面測試。
- 版本、審核、發布及稽核紀錄完整。
- 租戶隔離、權限與正式版不可變性測試通過。