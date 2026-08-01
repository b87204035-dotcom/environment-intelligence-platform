# 資料品質與時效門檻

## 1. 必填追溯欄位
每筆正式資料至少保存：`source_id`、`snapshot_id`、`published_at`、`retrieved_at`、`last_successful_sync_at`、`license_code`、`quality_status`、`checksum`、`transform_version`。

## 2. 時效狀態
- `current`：尚未到預定檢查日。
- `checked_no_new_release`：已檢查但來源未發布新版。
- `due`：已到檢查日。
- `stale`：超過允許時效。
- `sync_failed`：同步失敗，保留上一正式版本。
- `unavailable`：來源暫時或永久不可用。

所有有效來源至少每月檢查一次；不得把「已檢查」誤寫成「資料已更新」。

## 3. 品質門檻
| Gate | Trigger | Evidence | Pass | Block |
|---|---|---|---|---|
| Schema | 每次匯入 | 欄位驗證報告 | 必填欄位完整 | 阻擋發布 |
| Referential | 每次匯入 | FK/代碼檢查 | 無孤兒紀錄 | 阻擋發布 |
| Spatial | GIS 匯入 | 幾何/CRS報告 | 幾何有效、座標合理 | 阻擋圖層發布 |
| Temporal | 排程完成 | 時效報告 | 日期與頻率合理 | 標示 stale 或阻擋 |
| Citation | 報告發布 | 引用稽核 | Claim 可回溯 Evidence | 阻擋報告發布 |
| Legal | 法規更新 | 版本差異與審核 | 事件日版本正確 | 阻擋法律輸出 |

## 4. 同步失敗
同步採原子交換：新快照完成下載、解析、驗證及簽核後才成為 current。任何失敗均保留上一正式版本並產生事件，不得以假資料、零值或空表覆蓋。

## 5. 責任
Data Steward 負責來源與品質；Environmental Reviewer 負責專業合理性；Legal Reviewer 負責法規版本；Release Manager 決定是否解除發布阻擋。