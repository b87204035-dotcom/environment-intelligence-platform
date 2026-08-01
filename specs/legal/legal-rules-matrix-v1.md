# Legal and Professional Rules Matrix v1

## General policy
- Store every law, regulation, announcement, guidance and official form as a versioned legal document with effective dates and source snapshot.
- Evaluation is performed against the version effective on the user-selected evaluation date.
- Automated output is a preliminary decision-support result, not final legal advice.
- Final Article 8/9, control-plan, remediation-plan, verification or delisting conclusions require an authorized professional reviewer.

## Rule families
### LR-89-001 Announced business identification
Inputs: business registration, factory registration, historical operations, official announced-business category version, evaluation date.
Outputs: matched category, match basis, confidence, unmatched facts, required analytes if officially prescribed.
Fail-safe: ambiguous industry descriptions return insufficient_information.

### LR-89-002 Article 8 trigger evaluation
Inputs: effective legal text, land transaction/change facts, announced-business match, parcel identity, exemptions, dates.
Outputs: likely_applicable / likely_not_applicable / insufficient_information; conditions checklist; citations; missing evidence.
Review gate: mandatory.

### LR-89-003 Article 9 trigger evaluation
Inputs: effective legal text, business cessation/transfer/change facts, announced-business match, dates, competent-authority records.
Outputs and review gate same as LR-89-002.

### LR-SITE-001 Listed-site status
Inputs: official site record snapshot, announcement/delisting dates, geometry/parcel match.
Outputs: status as of evaluation date, spatial match type (exact parcel/direct overlap/nearby/administrative occurrence), pollutants and official document references.
Rule: proximity alone is not site status.

### LR-CONTROL-001 Control plan required chapters
The active guidance version defines chapter requirements. Minimum traceability: requirement ID, chapter, evidence needed, completion state, reviewer, guidance citation.
No chapter can be marked complete while required evidence placeholders remain unresolved.

### LR-REMED-001 Remediation plan required chapters
Same versioned mechanism as control plan, including objectives, alternatives evaluation, design basis, construction, monitoring, contingency, verification, schedule, cost and health/safety where required by the active guidance.

### LR-VERIFY-001 Verification and completion
Inputs: approved plan, target values, sampling design, laboratory results, QA/QC, effective regulatory criteria and competent-authority conditions.
Automated system may calculate and flag compliance but cannot declare regulatory completion without reviewer approval and official decision record.

## Decision record schema
- evaluation_id
- evaluation_date
- site/parcel identifiers
- legal_document_version_ids[]
- rule_codes[]
- facts_considered[] with evidence IDs
- conditions_met[]
- conditions_not_met[]
- missing_information[]
- preliminary_result
- rationale
- human_review_required=true
- reviewer_id/reviewed_at/final_disposition

## Evidence hierarchy
1. Official legal text and announcements.
2. Official competent-authority site and registration records.
3. Certified registrations, contracts and transaction documents.
4. Approved reports and laboratory data.
5. Client statements and field observations, clearly labeled.
6. Professional inference, explicitly identified and never substituted for missing legal facts.

## Required user-facing warnings
- Legal data effective date.
- Last successful synchronization time.
- Preliminary nature of automated result.
- Missing or conflicting evidence.
- Need for competent-authority/professional confirmation when applicable.
