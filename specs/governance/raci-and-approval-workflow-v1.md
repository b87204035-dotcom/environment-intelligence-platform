# RACI and Approval Workflow v1

## Roles

- Product Owner: defines priorities and accepts business outcomes.
- Environmental Professional: validates environmental interpretation, sampling, control and remediation content.
- Legal/Regulatory Reviewer: validates current legal basis, effective dates and procedural interpretation.
- Data Steward: approves sources, mappings, units, refresh behavior and data quality.
- Technical Lead: approves architecture, security and implementation quality.
- Report Author: edits and assembles project reports.
- Reviewer/Approver: authorizes report publication.
- Operations Administrator: monitors synchronization, backup, incidents and releases.

## RACI matrix

| Deliverable | Product Owner | Environmental Professional | Legal Reviewer | Data Steward | Technical Lead | Report Approver |
|---|---|---|---|---|---|---|
| Product scope | A/R | C | C | C | C | I |
| Environmental section template | A | R | C | C | C | C |
| Source onboarding | I | C | C | A/R | C | I |
| Article 8/9 rule version | I | C | A/R | C | C | I |
| Control/remediation template | A | R | C | C | C | C |
| AI prompt release | A | R | C | C | C | C |
| Database/API implementation | I | C | I | C | A/R | I |
| Report publication | I | C | C | I | I | A/R |
| Production release | A | C | C | C | R | I |

A = Accountable, R = Responsible, C = Consulted, I = Informed.

## Approval gates

1. Source gate: license, endpoint, field map, sample validation and citation approved.
2. Rule gate: legal text, effective date, applicability and limitations approved.
3. Prompt gate: evidence contract, prohibited claims, citation behavior and QA tests approved.
4. Report gate: completeness, factual support, figures/tables, references and professional signature approved.
5. Release gate: automated tests, security checks, migration plan, rollback and operations readiness approved.

No AI-generated legal, contamination, control or remediation conclusion may bypass the designated human approval gate.