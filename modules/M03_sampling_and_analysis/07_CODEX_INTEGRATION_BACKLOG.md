# Codex介接Backlog

## Work Package A：資料模型
建立：
- sampling_objectives
- dqos及dqos_versions
- areas_of_concern
- sampling_points及point_versions
- sampling_intervals
- analytes、analytical_methods及method_versions
- sample_containers_and_preservation
- qa_qc_samples
- chain_of_custody_events
- field_instruments_and_calibrations
- laboratory_results及validation_flags
- sampling_plan_versions及approvals

所有資料須具tenant、來源、版本、建立／修改者、時間及稽核欄位。

## Work Package B：規則引擎
- 由DQO、關注區、證據及介質產生候選採樣設計。
- 明確區分建議、待確認與已核准。
- 支援點位、深度、分析項目、方法、偵測極限及QA/QC檢核。
- 禁止以業別矩陣、PID或XRF直接產生確認污染結論。

## Work Package C：GIS與行動現勘
- 地圖新增、拖曳、複製及替代點。
- 顯示基地、地號、關注區、地下設施、井及排除區。
- iPhone離線記錄GPS精度、照片、深度、篩測與偏差。
- 同步需idempotent並保存衝突處理紀錄。

## Work Package D：監管鏈及實驗室資料
- 條碼／QR樣品識別。
- 電子CoC簽署、交接、封條及溫度紀錄。
- 匯入實驗室EDD並驗證樣品、方法、單位、RL／MDL、旗標及版本。
- 原始結果不可覆寫；修正版建立新版本。

## Work Package E：報告輸出
依`06_SAMPLING_PLAN_REPORT_TEMPLATE.md`輸出DOCX/PDF，包含自動目錄、圖表編號、採樣表、方法表、QA/QC及APA參考文獻。

## 驗收條件
1. 每個建議點位可追溯至DQO、關注區及證據。
2. 系統能保存目標與實際位置／深度差異。
3. 方法偵測極限高於門檻時阻擋正式發布或要求核准。
4. CoC全程可追溯且原紀錄不可覆寫。
5. 篩測資料與確認分析明確分離。
6. 無資料時顯示缺口，不產生假點位、假方法或假結果。
7. 租戶隔離、角色權限及稽核測試通過。
8. 採樣計畫須經指定環境專業人員核准後才能轉為正式版。

## 建議Issue
- M03-01 Sampling/DQO schema and migrations
- M03-02 Sampling design rule engine
- M03-03 GIS sampling designer
- M03-04 Mobile field sampling workflow
- M03-05 Electronic CoC and laboratory EDD import
- M03-06 Sampling plan DOCX/PDF export
- M03-07 QA/QC validation and acceptance tests
