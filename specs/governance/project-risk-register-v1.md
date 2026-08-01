# Project Risk Register v1

| ID | Risk | Likelihood | Impact | Mitigation | Release blocker |
|---|---|---|---|---|---|
| R-01 | Official source schema changes | High | High | Schema fingerprinting, validation, quarantine and mapping versions | Yes |
| R-02 | Source license does not permit storage or redistribution | Medium | High | License gate and blocked status until approved | Yes |
| R-03 | AI fabricates facts, values or citations | Medium | Critical | Structured evidence only, unsupported-claim detection, paragraph evidence links and human review | Yes |
| R-04 | Legal rules become outdated | High | Critical | Effective-dated rule versions, monthly legal review queue and mandatory displayed version | Yes |
| R-05 | Background concentration confused with regulatory standard | Medium | Critical | Separate entities, labels, units, methods and QA tests | Yes |
| R-06 | Sensitive client/project information leaks across tenants | Low | Critical | Tenant isolation, least privilege, encryption, audit logs and security tests | Yes |
| R-07 | Map overlay implies direct impact when only nearby | Medium | High | Distinct direct overlap, buffer proximity and administrative occurrence classifications | Yes |
| R-08 | Government endpoint outage | High | Medium | Immutable prior version, retry, alert, stale status and no fake replacement | No |
| R-09 | DOCX export changes approved text or references | Medium | High | Export snapshot, checksum and document regression tests | Yes |
| R-10 | Historical aerial/cadastral layer terms restrict use | Medium | High | Layer-specific licensing and credentials; public link fallback | Yes |
| R-11 | 368-town rollout reveals geographic data gaps | High | Medium | Explicit unavailable states, coverage dashboard and staged onboarding | No |
| R-12 | Scope expansion delays usable MVP | High | High | Milestone gates, dependency order and change-control board | No |
| R-13 | Mobile field observations sync twice or lose media | Medium | High | Idempotency keys, offline queue, checksums and reconciliation | Yes |
| R-14 | Cost/remediation suggestions treated as quotations or guaranteed design | Medium | Critical | Assumption ranges, uncertainty, professional review and non-final watermark | Yes |

Risks are reviewed before each release and whenever a source, legal rule, prompt or security control changes.