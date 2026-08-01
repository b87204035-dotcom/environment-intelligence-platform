# Prompt 架構與版本管理

## 1. Prompt 組裝順序
1. System policy：安全、資料隔離、禁止事項。
2. Developer policy：EIP 專業規則、引用、字數及輸出契約。
3. Prompt template：模組化任務指令。
4. Evidence context：來源快照、資料期間、欄位、引用及品質狀態。
5. User request：行政區、章節、字數、報告類型與特殊需求。

後層不得覆寫前層的安全、證據與專業審核限制。

## 2. Prompt Registry 必填欄位
- `prompt_id`
- `name_zh_tw`
- `module`
- `version`
- `status`: draft | review | active | deprecated
- `purpose`
- `input_schema`
- `output_schema`
- `required_evidence_types`
- `minimum_source_quality`
- `default_target_chars`
- `allowed_target_chars`
- `review_roles`
- `effective_from`
- `effective_to`
- `supersedes_prompt_id`
- `change_log`

## 3. 版本規則
採語意版本：`MAJOR.MINOR.PATCH`。
- MAJOR：輸出契約或專業判定邏輯不相容變更。
- MINOR：新增章節、證據類型或能力。
- PATCH：文字、錯字或不影響契約的修正。

已發布報告須保存當次 Prompt ID、版本、模型、參數、證據快照及輸出雜湊。

## 4. 通用輸入契約
```json
{
  "tenant_id": "uuid",
  "project_id": "uuid|null",
  "administrative_area_id": "uuid|null",
  "event_date": "YYYY-MM-DD|null",
  "target_chars": 880,
  "language": "zh-TW",
  "evidence_bundle_id": "uuid",
  "user_instructions": "string|null"
}
```

## 5. 通用輸出契約
```json
{
  "status": "completed|insufficient_information|conflicting_sources|professional_review_required|blocked",
  "title": "string",
  "content": "string",
  "actual_chars": 0,
  "claims": [],
  "citations": [],
  "references_apa7": [],
  "data_period": {},
  "last_successful_sync_at": null,
  "limitations": [],
  "missing_information": [],
  "review_requirements": []
}
```

## 6. 發布治理
Prompt 由內容負責人草擬，經環境專業、法規（適用時）、資料治理及產品負責人核准後啟用。任何高風險變更均須回歸測試並留下決策紀錄。
