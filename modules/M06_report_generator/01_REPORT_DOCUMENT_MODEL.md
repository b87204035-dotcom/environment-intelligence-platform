# 報告文件資料模型

## 1. 階層
`Report > ReportVersion > Chapter > Section > Block > EvidenceLink`

### Report
- `report_id`
- `tenant_id`
- `project_id`
- `report_type`
- `title`
- `status`
- `template_id`
- `created_by`

### ReportVersion
- `version_no`
- `parent_version_id`
- `generation_context_id`
- `status`: draft／review／approved／published／superseded
- `created_at`
- `approved_by`
- `approved_at`
- `content_hash`

### Section
- `section_code`
- `heading`
- `target_length`
- `actual_length`
- `generation_mode`: ai／manual／mixed
- `review_status`
- `data_as_of`
- `last_source_sync_at`

### Block
支援 paragraph、table、chart、map、figure、callout、limitation、reference-list及page-break。

## 2. 不可變性
- 已發布版本不得覆寫，只能建立新版本。
- 每次AI生成保存模型、Prompt版本、輸入證據ID、參數及輸出雜湊。
- 圖、表、地圖保存產製參數及來源快照。

## 3. 報告狀態
1. `assembling`
2. `draft`
3. `technical_review`
4. `legal_review`（適用時）
5. `approved`
6. `published`
7. `superseded`

## 4. 權限
- Author：建立及編輯草稿。
- Reviewer：提出意見、退回或通過。
- Professional Approver：核准專業與法規章節。
- Publisher：發布與匯出正式版本。
- Auditor：唯讀查看版本與稽核紀錄。

## 5. 必備追溯欄位
每個Section至少保存：
- 來源資料集ID及版本
- 來源發布日期、擷取時間、最後成功同步時間
- 引用清單
- 人工編修紀錄
- QA結果
- 未解決限制

## 6. 字數定義
- 中文以可見漢字、字母及數字計算，標點不計或依產品設定統一。
- 系統顯示目標、實際、偏差百分比。
- 預設允許偏差±10%；法規或固定表單章節可另設規則。