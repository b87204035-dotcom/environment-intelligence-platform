# Environment Intelligence Platform (EIP)

地方環境資料庫暨土壤地下水智慧決策平台。

## 產品目標

整合臺灣行政區環境基本資料、GIS、政府開放資料、土壤及地下水專業知識、法規判定、控制／整治計畫撰寫、AI 報告生成與 Word/PDF 輸出。

## Version 1.0 核心模組

1. 地方環境資料庫：地理、地質、土壤背景、地表水文、地下水及水文地質、人口、氣象雨量、污染場址、環境敏感區、調查歷史。
2. 報告產生器：各章預設 880 字，可自訂字數，逐段附來源與 APA 參考文獻，可複製、匯出 Word/PDF。
3. 土污法模組：第 8、9 條、公告事業、污染場址、地址／地號／GPS 查詢與法規依據。
4. 控制計畫與整治計畫：章節引導、資料缺口檢核、工法比較、監測、驗證、成本與期程。
5. 專案工作區：案件、地號、照片、文件、GIS、時間軸、版本與知識庫。
6. 資料治理：每項資料來源、授權、最後更新時間、同步狀態、版本與品質檢核。

## 建議技術堆疊

- Frontend: Next.js + TypeScript + Tailwind CSS
- Backend: FastAPI + Python
- Database: PostgreSQL + PostGIS
- GIS: MapLibre GL JS
- Jobs: GitHub Actions / background worker
- Export: DOCX / PDF
- Deployment: Docker Compose，後續可部署至雲端平台

## 文件入口

請先閱讀 `docs/00_PROJECT_CHARTER.md`、`docs/01_PRD.md`、`docs/02_SYSTEM_ARCHITECTURE.md` 與 `docs/10_CODEX_HANDOFF.md`。

## 目前狀態

規格建立中；尚未開始應用程式程式碼實作。