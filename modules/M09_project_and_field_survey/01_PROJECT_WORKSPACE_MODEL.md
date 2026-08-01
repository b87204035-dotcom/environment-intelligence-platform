# 01 專案工作區資料模型

## 1. 核心實體
- Tenant：組織或顧問公司。
- User：使用者。
- Client：客戶。
- Project：案件。
- Site：基地。
- Parcel：地號。
- Contact：聯絡人。
- Document：文件。
- MediaAsset：照片、影片、音訊。
- FieldVisit：現勘批次。
- Observation：現場觀察。
- SamplingLocation：採樣點、鑽孔或監測井。
- Task：任務。
- Review：審核。
- ReportVersion：報告版本。
- AuditEvent：稽核事件。

## 2. Project 必填欄位
`project_id`, `tenant_id`, `project_code`, `name`, `client_id`, `status`, `project_type`, `manager_user_id`, `started_at`, `created_at`, `updated_at`。

狀態至少包含：`draft`, `active`, `fieldwork`, `analysis`, `review`, `submitted`, `closed`, `archived`。

## 3. 關聯規則
- 一個 Project 可包含多個 Site。
- 一個 Site 可包含多個 Parcel。
- FieldVisit 必須隸屬 Project 與 Site。
- Observation、MediaAsset、SamplingLocation 可連結至 FieldVisit。
- ReportVersion 必須記錄使用的資料快照、文件版本與審核狀態。

## 4. 權限
角色：`tenant_admin`, `project_manager`, `consultant`, `field_staff`, `reviewer`, `client_viewer`。

預設最小權限；`client_viewer` 僅能讀取明確發布給客戶的內容。所有查詢均須以 `tenant_id` 篩選。

## 5. 狀態與發布
未審核內容不得標示為正式成果。已發布報告版本不可覆寫，只能建立新版本並保留差異與簽核紀錄。

## 6. JSON 範例
```json
{
  "project_id": "prj_001",
  "tenant_id": "ten_001",
  "project_code": "PJ-2026-001",
  "name": "民雄廠初步勘查",
  "status": "fieldwork",
  "sites": ["site_001"],
  "evidence_classification_enabled": true
}
```
