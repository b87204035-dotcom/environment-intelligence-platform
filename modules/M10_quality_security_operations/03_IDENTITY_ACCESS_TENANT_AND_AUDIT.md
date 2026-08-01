# 身分、權限、租戶與稽核

## 角色
- Platform Admin
- Tenant Admin
- Project Manager
- Environmental Professional
- Legal Reviewer
- Field User
- Client Reviewer
- Read-only Auditor

## 原則
- 最小權限、預設拒絕、職務分離。
- 所有 Project、Site、File、Photo、Report、Prompt Run 與 Export 均帶 `tenant_id`。
- 服務帳號不得共用；API Key 必須具範圍、有效期、輪替與撤銷機制。
- 高風險核准不得由建立者單獨完成。

## 稽核事件
保存 actor、tenant、action、resource、before/after hash、IP、device、request_id、timestamp、result。稽核紀錄採 append-only，不允許一般使用者修改或刪除。

## 跨租戶測試
每次發布必測：直接 ID 存取、搜尋、匯出、檔案 URL、AI context、快取、背景工作及錯誤訊息均不得洩漏其他租戶資料。