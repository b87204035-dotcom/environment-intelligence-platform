# Codex 介接 Backlog

## 目的
將本模組轉換成可查詢、可版本化、可審核的污染物與產業知識服務。

## 工作包
### M02-C01 污染物主資料模型
- 建立 `pollutants`、`pollutant_aliases`、`pollutant_properties`、`pollutant_methods`、`pollutant_regulatory_values`。
- 所有物性與標準均需來源、版本、有效日期及審核狀態。
- 驗收：同一污染物可保存多來源、多溫度、多法規版本，不覆寫歷史值。

### M02-C02 產業／活動關聯模型
- 建立 `industries`、`activities`、`industry_pollutant_links`、`evidence_requirements`。
- 關聯需保存信心等級與依據，預設不得標示為確認污染。
- 驗收：API明確區分 confirmed、suspected、generic association。

### M02-C03 宿命與傳輸知識模型
- 建立 source-pathway-medium-receptor 節點與關係。
- 支援場址CSM版本與人工核准。
- 驗收：缺少井篩、水位或地層資料時，系統阻止輸出確定流向／羽流結論。

### M02-C04 採樣分析建議服務
- 輸入產業、活動、物料、介質及調查目的，輸出候選分析項目與理由。
- 法定必測與專業建議分開。
- 驗收：每項建議皆含證據、介質、QA/QC與限制；不得以產業名稱直接全套套用。

### M02-C05 報告與AI證據整合
- 將Evidence ID、污染物節點、分析結果與引用傳入AI報告引擎。
- 建立unsupported claim檢查。
- 驗收：沒有Evidence ID的污染事實不得進入核准版本。

### M02-C06 管理後台
- 提供污染物別名、物性、法規值、產業關聯與方法版本管理。
- 變更需審核、稽核軌跡與回復能力。

## API建議
- `GET /v1/pollutants`
- `GET /v1/pollutants/{id}`
- `GET /v1/industries/{id}/candidate-pollutants`
- `POST /v1/sampling/recommendations`
- `POST /v1/csm/evaluate-completeness`
- `POST /v1/reports/validate-pollutant-claims`

## 非功能要求
- 多租戶隔離；官方共用知識與企業私有知識分離。
- 所有節點可版本化及追溯。
- 專業規則更新不得直接改寫既有已核准報告。
- 禁止使用虛構濃度或未審核法規值作為示範正式資料。

## 相依Issue
- 基礎：#1、#3、#4。
- AI／報告：#8、#9。
- 第8／9條與控制整治：#10、#11。
- 測試與發布：#13。
