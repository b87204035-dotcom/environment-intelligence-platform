# Environment Knowledge Graph v1

版本：v1.0  
日期：2026-08-01

## 目的

建立可供搜尋、AI生成、法規檢核、工法比選與報告引用使用的環境專業知識圖譜。知識圖譜不得取代原始證據；任何結論仍須回連資料快照、法規版本或文獻。

## 核心節點類型

### SpatialUnit
- Country
- CountyCity
- TownshipDistrict
- Village
- Parcel
- ProjectSite
- BufferZone
- Watershed
- GroundwaterRegion

### EnvironmentalMedium
- Soil
- VadoseZone
- Groundwater
- SurfaceWater
- Sediment
- SoilGas
- IndoorAir

### PhysicalSetting
- GeologicUnit
- Lithology
- SoilSeries
- SoilTexture
- Aquifer
- Aquitard
- Fault
- Landform
- DrainageClass
- HydraulicConductivity
- GroundwaterLevel
- GroundwaterFlowDirection

### Contaminant
- TPH
- BTEX
- MTBE
- TCE
- PCE
- VinylChloride
- 1_1_1_TCA
- 1_2_DCA
- Benzene
- PAH
- Arsenic
- Cadmium
- Chromium
- HexavalentChromium
- Copper
- Mercury
- Nickel
- Lead
- Zinc

### SourceActivity
- GasStation
- UndergroundStorageTank
- Electroplating
- MetalFinishing
- Semiconductor
- DryCleaning
- SolventUse
- ChemicalStorage
- WasteDisposal
- AgriculturalUse
- TransformerArea
- WastewaterTreatment

### InvestigationElement
- HistoricalReview
- SiteReconnaissance
- SoilSampling
- GroundwaterSampling
- SoilGasSampling
- Borehole
- MonitoringWell
- Geophysics
- LaboratoryAnalysis
- QAQC
- ConceptualSiteModel

### LegalInstrument
- SoilAndGroundwaterPollutionRemediationAct
- Article8
- Article9
- AnnouncedBusiness
- ControlSite
- RemediationSite
- ControlPlan
- RemediationPlan
- Verification
- Deregistration
- OfficialAnnouncement
- InterpretationLetter

### RemediationTechnology
- Excavation
- OffsiteDisposal
- SoilWashing
- StabilizationSolidification
- SVE
- AirSparging
- MPE
- PumpAndTreat
- ISCO
- ISCR
- EnhancedBioremediation
- ZVI
- PermeableReactiveBarrier
- ThermalTreatment
- MonitoredNaturalAttenuation
- HydraulicContainment

### Evidence
- OfficialDataset
- OfficialAnnouncement
- RegulationVersion
- GuidanceDocument
- PeerReviewedArticle
- TechnicalReport
- LaboratoryReport
- FieldObservation
- Photograph
- MapLayer
- DataSnapshot

### ReportComponent
- GeographySection
- GeologySection
- SoilBackgroundSection
- HydrologySection
- HydrogeologySection
- PopulationSection
- ClimateSection
- ContaminatedSitesSection
- SensitiveAreasSection
- InvestigationHistorySection
- Article8Assessment
- Article9Assessment
- ControlPlanChapter
- RemediationPlanChapter

## 關係類型

- LOCATED_IN：基地、場址、井位、採樣點位於行政區或地號。
- OVERLAPS：基地與污染場址、敏感區、地質單元直接重疊。
- NEARBY：位於指定距離內；必須保存距離與計算方法。
- HAS_MEDIUM：場址涉及土壤、地下水等介質。
- CONTAINS_CONTAMINANT：介質或場址含特定污染物；須連結分析證據。
- POTENTIALLY_ASSOCIATED_WITH：產業活動與污染物的可能關聯，僅為調查假設。
- CONFIRMED_BY：事實由公告、檢測或正式資料確認。
- MEASURED_BY：數值由採樣、觀測井或分析方法取得。
- GOVERNED_BY：程序受某法規版本管制。
- REQUIRES_REVIEW：輸出須由技師、法規或資料管理人審核。
- TREATED_BY：污染物／介質可由工法處理，但需適用性條件。
- INHIBITED_BY：工法受pH、地層、滲透性、共存物質等限制。
- PRODUCES：資料來源產生資料集、快照或圖層。
- CITED_BY：證據被報告段落引用。
- DERIVED_FROM：統計、圖表、AI段落衍生自特定快照。
- SUPERSEDES：新版法規、資料或模板取代舊版。

## 核心規則

1. `POTENTIALLY_ASSOCIATED_WITH` 永遠不得自動升級為 `CONFIRMED_BY`。
2. 污染物存在必須至少連結一筆 LaboratoryReport、OfficialAnnouncement 或可信資料快照。
3. 地下水流向若非由同期水位測量與高程基準計算，只能標示「區域推估」或「未知」。
4. 土壤背景值必須具空間母體、深度、樣本數、統計量、方法與來源；不得等同管制標準。
5. 工法適用性需同時考慮污染物、介質、濃度、深度、地層、滲透性、地下水位、pH、氧化還原條件及場址限制。
6. 法規節點必須有生效日、失效日／現行狀態與官方來源。
7. AI產生段落只能引用可追溯Evidence節點。

## 示例知識鏈

### TCE地下水案例
`DryCleaning POTENTIALLY_ASSOCIATED_WITH TCE`  
`TCE CONTAINS_CONTAMINANT Groundwater`（僅在有檢測證據時）  
`TCE TREATED_BY EnhancedBioremediation`  
`EnhancedBioremediation INHIBITED_BY LowElectronDonorAvailability`  
`TreatmentDecision REQUIRES_REVIEW ProfessionalReviewer`

### 加油站TPH案例
`GasStation POTENTIALLY_ASSOCIATED_WITH TPH`  
`UndergroundStorageTank POTENTIALLY_ASSOCIATED_WITH BTEX`  
`ProjectSite NEARBY ContaminatedSite`  
此鏈只能支持「應查核及規劃調查」，不能支持「基地已污染」。

### 土壤背景資料
`SoilBackgroundObservation MEASURED_BY LaboratoryAnalysis`  
`SoilBackgroundObservation LOCATED_IN BackgroundPopulationArea`  
`SoilBackgroundStatistic DERIVED_FROM SoilBackgroundObservation`  
`SoilBackgroundSection CITED_BY SoilBackgroundStatistic`

## 最小節點欄位

- id
- node_type
- canonical_name_zh
- canonical_name_en
- description
- status
- valid_from
- valid_to
- source_id
- source_snapshot_id
- reviewer_status
- created_at
- updated_at

## 最小關係欄位

- id
- subject_id
- predicate
- object_id
- qualifier_json
- evidence_id
- confidence_level
- valid_from
- valid_to
- reviewer_status

## 信賴等級

- A：法規、正式公告、主管機關原始資料。
- B：具方法與品質資訊的政府監測或正式技術報告。
- C：同儕審查論文、標準或國際技術文件。
- D：現場觀察、客戶說明、未驗證歷史資訊。
- E：AI推論或規則比對結果，必須保留推論標記。

## 禁止事項

- 不得把行政區內曾有污染場址推論為所有土地皆受污染。
- 不得把鄰近污染場址推論為基地污染來源。
- 不得用單一觀測井代表整個鄉鎮地下水品質。
- 不得用農業土壤圖直接判定重金屬背景濃度。
- 不得把AI建議當成主管機關核准的控制或整治方案。
