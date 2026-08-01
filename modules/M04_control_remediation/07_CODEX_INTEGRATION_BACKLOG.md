# Codex 介接 Backlog

## 工作包 A：資料模型
建立：
- `control_plans`、`control_measures`、`control_targets`
- `remediation_plans`、`remediation_targets`、`remediation_alternatives`
- `technology_screening_scores`、`pilot_tests`、`design_parameters`
- `cost_estimates`、`schedule_activities`、`risk_registers`
- `monitoring_programs`、`monitoring_triggers`、`verification_programs`
- `plan_reviews`、`plan_versions`、`authority_submissions`

所有表須具租戶、專案、場址、來源、版本、建立者、審核狀態與稽核欄位。

## 工作包 B：控制／整治工作區
- 依模板建立章節與完成度。
- 關聯場址、污染物、採樣、井、圖層與文件。
- 可逐章生成、編輯、鎖定、比較與審核。
- 顯示資料缺口、來源新鮮度及未結審查意見。
- 未核准AI文字須有明顯草稿標示。

## 工作包 C：技術篩選引擎
輸入結構化污染物、介質、相態、地層、水文地質、範圍、受體與施工限制，輸出候選技術、排除理由、必要試驗、風險與證據。不得在資料不足時自動選定唯一工法。

## 工作包 D：成本與期程
- 工作分解結構、數量、單價、基準日與估算層級。
- 低／基準／高情境及敏感度。
- 甘特圖、相依關係、里程碑與關鍵路徑。
- 成本估算、契約價及實際支出分開。

## 工作包 E：監測與應變
- 監測矩陣、頻率、點位、分析項目及QA/QC。
- 警戒值、行動值、觸發事件、通報與應變流程。
- 時間序列、趨勢、停機與反彈測試。
- 驗證狀態不得由操作監測自動取代。

## 工作包 F：文件與輸出
- 控制計畫與整治計畫DOCX/PDF。
- 自動目錄、圖表編號、參考文獻、修訂紀錄與附錄。
- 匯出時嵌入資料版本、來源清單與生成／審核紀錄。

## 驗收條件
1. 無完整證據時，系統不產生確定工法、成效或解除列管結論。
2. 所有目標、標準、監測值與實測值可明確區分。
3. 成本顯示估算層級、基準日、區間與假設。
4. 每個計畫版本不可覆寫，可比較差異。
5. 高風險章節未完成專業審核時不得標記為可送審。
6. 所有輸出可追溯至資料快照、法規版本、Prompt版本與審核人。

## 相依關係
依賴 M01資料來源治理、M02污染物知識與M03採樣分析規格；後續應與法規、AI報告、GIS及專案工作區模組整合。
