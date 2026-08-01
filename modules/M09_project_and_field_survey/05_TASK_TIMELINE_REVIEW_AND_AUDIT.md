# 05 任務、時間軸、審核與稽核

## 1. Task
欄位：`task_id`, `project_id`, `title`, `task_type`, `assignee_id`, `priority`, `status`, `due_at`, `dependency_ids`, `evidence_required`, `completed_at`。

狀態：`todo`, `in_progress`, `blocked`, `review`, `done`, `cancelled`。完成需附證據或原因。

## 2. Timeline
時間軸整合：文件取得、現勘、照片、採樣、實驗室資料、主管機關往來、AI 生成、報告版本、審核、提交與結案。時間軸事件不可覆寫，只能補充或更正並保留原紀錄。

## 3. Review
審核類型：資料、技術、法規、編輯、專業簽核。每次審核保存：版本、審核人、結論、問題分級、意見、處置與完成日期。

高風險結論如污染認定、地下水流向、法規適用、控制／整治工法與正式報告，未完成指定審核不得發布。

## 4. AuditEvent
至少記錄：登入、讀取敏感案件、建立／修改／刪除、下載、分享、權限變更、AI 生成、匯出、簽核與發布。

欄位：`event_id`, `tenant_id`, `actor_id`, `action`, `resource_type`, `resource_id`, `before_hash`, `after_hash`, `ip_or_device`, `occurred_at`, `reason`。

## 5. 通知
通知來源包括到期、資料缺漏、同步失敗、審核退回、權限異動與高風險操作。通知不得包含超出收件人權限的敏感內容。

## 6. 結案
結案前檢查：任務完成、待確認事項處理、正式報告發布、資料來源與版本完整、權限收斂、備份成功及保留期限設定。
