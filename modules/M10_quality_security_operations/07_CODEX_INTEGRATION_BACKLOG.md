# Codex 整合 Backlog

## Work Package A｜品質與時效
- 建立 `source_snapshot`、`sync_run`、`quality_check`、`freshness_status` 資料表。
- 實作每月至少一次來源檢查、原子發布、上一正式版本保留與 stale 警示。
- 建立資料品質 Dashboard 與阻擋發布 Gate。

## Work Package B｜測試與 CI/CD
- 建立 unit、integration、contract、GIS、AI grounding、DOCX/PDF、security、performance 測試。
- PR 必須產生測試報告、SBOM、漏洞掃描與 migration 檢查。
- 發布保存 Commit SHA、映像 digest、Prompt 與資料版本。

## Work Package C｜IAM 與稽核
- 實作 RBAC、tenant scope、服務帳號、API Key 生命週期與 append-only audit log。
- 建立跨租戶自動化測試，涵蓋搜尋、檔案、匯出、AI context、快取與背景工作。

## Work Package D｜資安與備份
- 整合 Secret Manager、檔案惡意掃描、依賴與映像漏洞掃描。
- 建立資料庫及物件儲存備份、checksum 驗證、還原演練與報告。

## Work Package E｜監控與事件
- 建立服務、資料、AI、GIS、報告、儲存與安全監控。
- 定義 SEV-1～4 告警、值班、事件時間軸、事後檢討與問題追蹤。

## Work Package F｜正式上線
- 將 `06_GO_LIVE_UAT_AND_COMPLIANCE_CHECKLIST.md` 轉成可執行 Release Checklist。
- 未通過專業、法律、資料、資安、備份及 UAT Gate 不得部署 Production。

## Definition of Done
每項工作必須有 owner、測試證據、操作文件、回滾／復原方式、監控與驗收紀錄；不得弱化 M01～M09 的證據追溯、人工審核或租戶隔離規則。