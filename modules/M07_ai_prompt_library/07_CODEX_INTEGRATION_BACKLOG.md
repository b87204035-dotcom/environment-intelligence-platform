# Codex Integration Backlog

## P0：資料模型與版本
- 建立 `prompt_registry`、`prompt_versions`、`prompt_tests`、`generation_runs`、`claims`、`claim_evidence_links`。
- 保存 Prompt、模型、參數、證據快照、輸出、字數、雜湊與審核狀態。
- 建立不可變發布版本與 supersede 關係。

## P0：Prompt Runtime
- 實作 system → developer → template → evidence → user 的組裝順序。
- 使用 JSON Schema 驗證輸入輸出。
- 實作 evidence token budget、來源排序、去重與衝突標記。
- 缺資料時回傳結構化狀態，不以自由文字掩蓋。

## P0：Grounding 與安全
- 每段 Claim 與 Evidence 強制關聯。
- 文內引用與參考文獻雙向驗證。
- 租戶、專案及文件權限檢查。
- Prompt injection、惡意附件、跨租戶與秘密外洩防護。
- 高風險輸出必須 professional review。

## P1：Prompt 管理介面
- Prompt 搜尋、版本差異、啟用／停用、審核與回復。
- 顯示依賴模組、必要證據、測試狀態與使用紀錄。
- 禁止直接編輯已發布版本；修改須建立新版本。

## P1：地方環境章節
- 實作 14 個地方環境 Prompt。
- 支援預設880字、自訂字數、實際字數與資料時效顯示。
- 與 M01 資料來源、M06 報告及 M08 GIS 串接。

## P1：法規、專案與整治
- 與 M05 法規版本規則串接。
- 與 M03 採樣、M04 控制整治及 M09 現勘證據分類串接。
- 法規與工程建議不得跳過審核狀態。

## P1：評估框架
- 建立固定 fixtures、批次測試、評分與回歸比較。
- CI 阻擋 JSON Schema 失敗、引用缺漏、安全測試失敗及重大品質退步。
- 保存人工評分與問題分類。

## API 建議
- `GET /api/v1/prompts`
- `POST /api/v1/prompts/{id}/versions`
- `POST /api/v1/generations`
- `GET /api/v1/generations/{id}`
- `POST /api/v1/generations/{id}/review`
- `POST /api/v1/prompts/{id}/evaluate`
- `GET /api/v1/prompt-tests/{run_id}`

## Definition of Done
- 文件、資料模型、API、測試與權限一致。
- 至少完成 PT-001～PT-015 自動化或可重現測試。
- 無 Blocker／Critical 問題。
- 所有正式輸出具 Prompt 版本、Evidence、Citation、審核與稽核紀錄。
- 不新增 M11 以上頂層模組。
