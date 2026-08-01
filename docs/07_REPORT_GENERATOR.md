# 07 Report Generator

## 1. Section generation contract

Input:
- section type
- administrative area or project site
- target character count, default 880
- report purpose and professional tone
- selected evidence/source IDs
- citation style, default APA
- optional user instructions

Output:
- title and structured paragraphs
- actual character count
- inline citation markers mapped to source IDs
- figures/tables suggested or generated from data
- data limitations and warnings
- reference list entries

## 2. Character-count behavior

- Accept 200–5,000 Chinese characters per section.
- Target tolerance: ±10%.
- Do not pad with repetition.
- When evidence is insufficient for the requested length, return a shorter sourced section and an explicit warning.

## 3. Editor

- rich text with heading levels
- lock paragraphs against regeneration
- regenerate selected paragraph or whole section
- compare versions and restore
- insert figure/table/citation
- source side panel showing exact supporting records
- reviewer comments and approval state

## 4. Citation rules

- Specific claims, numbers, dates, spatial relationships and legal conclusions require citations.
- References are deduplicated in the document bibliography.
- Each figure/table includes source, data date and processing note.
- AI must never invent author, title, year, dataset ID or URL.

## 5. DOCX export

- configurable cover and organization identity
- automatic table of contents
- hierarchical numbering
- figure/table captions and lists
- headers, footers and page numbers
- Chinese font fallback and styles
- citations and bibliography
- appendix for source inventory and last-update table

## 6. Quality checks

- uncited factual claim detection
- stale source warning
- conflicting values or units
- missing chapter/figure/table
- invalid citation metadata
- target word-count deviation
- unsupported legal/engineering assertion
- unresolved reviewer comments

The export is blocked only for critical errors; warnings remain visible in the document status report.