# 05 Data Source Catalog

> This catalog is the starting registry. Exact dataset IDs, access terms, API limits and schemas must be verified before production ingestion.

| Domain | Preferred publisher/source | Target refresh | Notes |
|---|---|---:|---|
| Administrative boundaries | National Land Surveying and Mapping Center / government open data | Monthly check | Preserve boundary version and effective date. |
| Address/geocoding | TGOS or authorized national geospatial service | Monthly check | Credentials and usage terms may be required. |
| Cadastral lookup | National land/cadastral authorized service | Monthly check | Do not redistribute restricted parcel data without permission. |
| Population | Ministry of the Interior household registration statistics | Monthly | Store town and village time series. |
| Weather and rainfall | Central Weather Administration open data | Daily/monthly aggregation | Record station selection and missing-data rules. |
| Surface water and basins | Water Resources Agency and relevant river authorities | Monthly check | Spatial layers change irregularly. |
| Groundwater levels/wells | Water Resources Agency groundwater observation services | Monthly | Store raw observations and derived annual/monthly statistics. |
| Geology and hydrogeology | Geological Survey and Mining Management Agency | Monthly change check | Many maps update irregularly; record publication edition. |
| Soil classification/properties | Ministry of Agriculture agencies, soil survey publications and authorized datasets | Quarterly change check | Separate mapped soil units from measured background concentrations. |
| Soil background concentrations | Official surveys and peer-reviewed studies | Quarterly change check | Store region, sampling design, statistic and analytical method. Never present a local background value without scope. |
| Pollution sites | Ministry of Environment soil and groundwater systems/open data | Daily or monthly | Preserve current status and status history. |
| Announced businesses | Ministry of Environment legal notices | Monthly legal check | Version by effective date. |
| Environmental sensitive areas | Responsible agencies by legal category | Monthly change check | Do not merge categories without legal definition and source. |
| Land use/cover | National land use investigation/open geospatial data | Annual or release-based | Preserve survey year. |
| Flood hazard | Water Resources Agency | Release-based monthly check | Show scenario and return period. |
| Investigation history | Ministry/local government reports, public tenders, theses and project documents | Monthly discovery | Classify evidence quality and public availability. |
| Laws/guidelines | Ministry of Environment legal system | Weekly/monthly check | Freeze law version used in every decision/report. |

## Mandatory source metadata

- official title
- publisher
- dataset identifier or publication number
- access endpoint or landing page
- license/usage restriction
- spatial and temporal coverage
- native format and CRS
- update policy stated by publisher
- system refresh schedule
- last successful retrieval
- last source data date
- checksum and snapshot location
- APA citation template

## Citation pattern

Government dataset example:

`機關名稱。（年份）。資料集名稱（版本或資料日期）[資料集]。資料平台名稱。存取日期。`

Technical map/report example:

`機關或作者。（年份）。出版品或圖幅名稱（比例尺／版本）[地圖或技術報告]。出版機關。`

Web links should be stored in metadata and rendered in the exported reference list; displayed claims must cite source IDs rather than a bare URL.

## Freshness rules

- Dynamic datasets: system must attempt refresh at least monthly, even if source updates more frequently.
- Release-based layers: run monthly change detection; do not overwrite the prior edition.
- A chapter is marked `stale` if any critical source exceeds its source-specific freshness threshold.
- Page header shows report generation time; each chapter shows source data date and last synchronization time.