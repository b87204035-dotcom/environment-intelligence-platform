# 法規與專案 Prompt Library

## 法規 Prompt
| Prompt ID | 用途 | 強制輸出 |
|---|---|---|
| LEG-A8-001 | 土污法第8條初步判定 | event_date、適用版本、證據、缺漏、人工審核 |
| LEG-A9-001 | 土污法第9條初步判定 | 行為類型、事業比對、適用版本、待主管機關確認 |
| LEG-BUSINESS-001 | 公告事業比對 | 登記業別、實際製程、原物料、設備、規模、置信度 |
| LEG-VERSION-001 | 法規版本差異 | 新舊條文、有效日期、案件影響、重新評估需求 |
| LEG-REVIEW-001 | 法規品質檢查 | 過期來源、缺法源、超越授權、未審核結論 |

### 法規輸出狀態
`likely_applicable`、`likely_not_applicable`、`insufficient_information`、`conflicting_sources`、`authority_confirmation_required`、`professional_review_required`。

法規 Prompt 不得輸出「主管機關已認定」或「依法一定適用」等語句，除非 Evidence Bundle 內有正式處分、函文或核准文件。

## 專案與現勘 Prompt
| Prompt ID | 用途 |
|---|---|
| PRJ-INTAKE-001 | 將客戶資料整理為案件基本資料與缺漏清單 |
| PRJ-PREFIELD-001 | 勘查前資料盤點與動線建議 |
| PRJ-FIELDNOTE-001 | 整理現勘筆記、照片與GPS紀錄 |
| PRJ-EVIDENCE-CLASS-001 | A文件、B口頭／LINE、C合理推定、D待確認分類 |
| PRJ-SAMPLING-BRIEF-001 | 依DQO產生採樣設計草案 |
| PRJ-QA-001 | 檢查案件資料完整性、矛盾與待辦 |

## 現勘摘要規則
- 文件內容、客戶口述、現場觀察與推論分開呈現。
- 照片僅描述可見內容，不自行判定物質種類或污染。
- GPS、EXIF、方向與時間缺失時須標示。
- LINE 匯入內容需保存提供者、日期及來源註記。
- 不得宣稱存取未連接之 LINE、客戶系統或政府內部資料。

## 通用法規 Prompt 片段
```text
以事件基準日 {event_date} 選取當時有效法規版本。逐項列出判定要件、支持證據、反對證據、缺漏資料與適用限制。結果僅為初步作業輔助；凡涉及正式法律義務、主管機關認定、控制／整治責任或解除列管，均標示 professional_review_required 或 authority_confirmation_required。
```
