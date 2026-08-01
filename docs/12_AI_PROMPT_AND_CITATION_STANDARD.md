# 12 AI Prompt and Citation Standard

## 1. Purpose
Define auditable generation of environmental narratives, legal decision-support drafts, control plans and remediation plans.

## 2. Grounding rules
1. Generate only from approved source snapshots, project records and user-entered facts.
2. Never invent measurements, pollution conditions, facilities, processes, dates, legal applicability or citations.
3. Separate: documented fact, user statement, professional inference and item requiring confirmation.
4. Every factual paragraph must map to one or more citation records.
5. Conflicting sources must be disclosed, not silently reconciled.
6. Legal outputs are decision support and require qualified professional review.

## 3. Standard generation request
Required fields:
- administrative_area_id or project_id
- section_type
- target_length, default 880 Chinese characters
- language, default zh-TW
- writing_style
- citation_style, default APA 7
- data_cutoff_at
- allowed_source_snapshot_ids
- excluded_source_ids
- include_tables, include_figures and include_limitations

## 4. Standard response
- title
- narrative
- actual_character_count
- inline_citations
- reference_entries
- claims array containing claim text, evidence snapshot IDs and confidence
- limitations
- generated_at
- prompt_template_version
- model identifier
- source manifest hash

## 5. Section templates
### Geography
Describe location, neighboring administrative areas, area, principal settlements and regional context. Avoid unsupported qualitative claims.

### Geology
Describe mapped formations, lithology, age, structures and engineering/environmental relevance. Distinguish regional map interpretation from site-specific boring evidence.

### Soil background
Cover soil series/classification, texture and physicochemical characteristics where available; background metal concentration must identify sampling population, statistic, units, depth, analytical method and spatial applicability. Do not treat regulatory standards as background concentrations.

### Surface hydrology
Identify rivers, drainage, catchments, reservoirs, flood-prone areas and hydrologic relationship to the selected area.

### Groundwater and hydrogeology
Describe groundwater region, aquifers/aquitards, recharge/discharge, observed groundwater levels and data limitations. Do not infer site groundwater flow direction from regional data alone.

### Population, climate and rainfall
Use a defined ten-year period, state missing years, calculate trends reproducibly and include station selection rules.

### Pollution sites and investigation history
Differentiate active, controlled, remediation, emergency-response and delisted records. Never equate proximity with causation.

## 6. Citation standard
Default APA 7 format:
Organization. (Year). Title of dataset or publication (version if available) [Data set/Map/Report]. Publisher. Retrieval date when content is dynamic.

Each citation record stores:
- author/organization
- publication year/date
- title
- edition/version
- resource type
- publisher
- persistent identifier or canonical URL
- accessed date
- license
- source snapshot ID

## 7. Length control
- Target is Chinese character count excluding references unless user chooses words.
- Acceptable tolerance: ±10% for <=1,000 characters; ±7% above 1,000.
- Generation may not pad with repetition.

## 8. Quality gates
Reject publication when:
- factual paragraphs lack evidence
- reference does not resolve to a registered source
- requested period differs from extracted period without disclosure
- stale critical dataset is not acknowledged
- legal or remediation recommendation lacks assumptions and reviewer warning

## 9. Human review states
Draft → Generated → Technical review → Professional engineer review when required → Approved → Published → Superseded.