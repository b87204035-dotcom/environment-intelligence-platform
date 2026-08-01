# 資料來源 Metadata 標準 v1.0

每筆來源必須建立唯一 `source_id`，並保存下列欄位。

## A. 識別
- `source_id`
- `publisher_name_zh`
- `publisher_name_en`
- `dataset_title_zh`
- `dataset_title_en`
- `dataset_description`
- `official_landing_page`
- `access_endpoint`
- `access_method`: API / bulk download / WMS / WMTS / WFS / manual

## B. 時間
- `data_period_start`
- `data_period_end`
- `publisher_release_date`
- `publisher_modified_at`
- `first_ingested_at`
- `last_checked_at`
- `last_successful_sync_at`
- `next_check_due_at`
- `expected_refresh_frequency`

## C. 授權與使用限制
- `license_name`
- `license_url`
- `commercial_use_allowed`
- `redistribution_allowed`
- `attribution_required`
- `api_key_required`
- `rate_limit`
- `restricted_fields`
- `legal_review_status`

未取得明確授權者，不得公開再散布原始資料；可只保存來源指標與內部快照。

## D. 技術資訊
- `format`
- `encoding`
- `schema_version`
- `coordinate_reference_system`
- `geometry_type`
- `spatial_resolution`
- `temporal_resolution`
- `primary_key_strategy`
- `checksum_algorithm`
- `content_hash`

## E. 品質與治理
- `authority_rank`
- `coverage_scope`
- `known_limitations`
- `validation_profile`
- `freshness_status`: current / due / stale / unavailable / retired
- `publication_status`: draft / validated / published / rejected
- `data_steward`
- `professional_reviewer`

## F. 引用
預設 APA 7：

`機關名稱。（年份）。資料集名稱（版本或資料日期）[資料集]。取用日期，來源網址。`

動態資料應同時保存取用日期與快照版本。AI輸出不得只有首頁網址，必須連結實際使用的資料集或快照。

## G. 來源與主題映射
每筆來源須列出：
- 對應環境章節
- 對應資料表
- 主要欄位映射
- 可產生的圖、表、GIS圖層
- 是否可用於法律／專業結論
- 是否需要人工審核

## 驗收
Metadata缺少來源機關、資料日期、授權或最後同步時間時，資料不得標示為正式可用。