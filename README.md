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

## 可部署的網站

目前提供可安裝的靜態 GIS 現勘工作台，整合地址／GPS 定位、圖層切換、採樣與照片點位、污染場址匯入、法規初判、瀏覽器案件保存及 GeoJSON 匯出。網站由 GitHub Pages 工作流程部署，核心介面在離線時仍可開啟；需要網路的底圖與地址服務會清楚顯示離線狀態。

```bash
# 本機預覽（請勿直接以 file:// 開啟，Service Worker 需要 HTTP）
python -m http.server 8000 --directory docs

# 零相依靜態網站檢查
python -m unittest discover -s tests -v
```

瀏覽 `http://localhost:8000`。推送至 `main` 後，`.github/workflows/deploy-pages.yml` 會發布 `docs/`。

> 法規判定與污染資料均為決策支援或使用者匯入資料，不取代主管機關認定及專業人員覆核。

## Phase 2 資料平台 MVP

資料平台位於 `backend/`，使用 FastAPI、PostgreSQL 16 與 PostGIS 3.4。它提供：

- 具不可變快照、SHA-256、批次狀態及來源欄位的正式政府資料匯入流程；
- 每月排程及依各資料集更新週期判斷的同步工作；
- 全文、資料集與空間範圍搜尋 API；
- 報告與章節草稿 API；
- 只接受已保存證據 ID、保留模型與 Prompt 版本、強制專業覆核的 AI 草稿 API；
- 可逆 Alembic migrations、Docker Compose、PostGIS CI、GHCR 映像與版本標籤部署。

```bash
cp .env.example .env
# 編輯 .env，至少更換 POSTGRES_PASSWORD
docker compose up --build -d
curl --fail http://localhost:8001/health
```

互動式 API 文件位於 `http://localhost:8001/docs`。正式部署、機密設定、來源上架與回滾程序請見 `docs/32_BACKEND_DEPLOYMENT.md`。
