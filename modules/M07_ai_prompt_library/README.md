# M07 AI Prompt Library 與防幻覺系統

本模組定義 EIP 所有 AI Prompt 的架構、版本、輸入輸出契約、證據組裝、防幻覺規則、測試及 Codex 介接需求。

## 目標
- 支援地方環境基本資料、法規判定、專案管理、控制計畫與整治計畫。
- 每章預設約 880 字，允許自訂目標字數並回傳實際字數。
- 所有事實性敘述均須追溯至證據與 APA 7 參考資料。
- 資料不足、過期、衝突或未經專業審核時，不得輸出確定結論。

## 文件
1. `01_PROMPT_ARCHITECTURE_AND_VERSIONING.md`
2. `02_LOCAL_ENVIRONMENT_PROMPTS.md`
3. `03_LEGAL_AND_PROJECT_PROMPTS.md`
4. `04_CONTROL_REMEDIATION_PROMPTS.md`
5. `05_GROUNDING_AND_HALLUCINATION_GUARDS.md`
6. `06_PROMPT_EVALUATION_AND_TEST_CASES.md`
7. `07_CODEX_INTEGRATION_BACKLOG.md`

## 固定原則
- 頂層模組固定為 M01～M10。
- Prompt 不得直接取代環境專業、法規或主管機關判定。
- 不得虛構污染場址、地下水流向、土壤背景值、法規、函釋、引用或數值。
