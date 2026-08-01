# 30 Codex Execution Order

Codex must implement in this order unless a reviewed architecture decision changes it:

1. Issue #1 production monorepo foundation.
2. Authentication/RBAC/audit foundation.
3. Source registry, snapshots, validation and freshness.
4. Administrative-area model and boundary ingestion.
5. Environmental section data contracts and APIs.
6. GIS layer catalog and map application.
7. Report section editor, grounding/citation service and versioning.
8. DOCX export and reproducibility manifest.
9. Project workspace and field survey.
10. Article 8/9 decision support.
11. Control and remediation plan builders.
12. Production operations, security and release hardening.

For every task:
- read applicable `/docs` files
- link a GitHub Issue
- implement tests and documentation
- do not add fabricated production environmental values
- open a focused pull request
- stop and document unresolved legal, licensing or data-access assumptions

The first Codex prompt should be:

> Implement Issue #1. Read all repository documentation, especially `docs/10_CODEX_HANDOFF.md`, `docs/17_DEFINITION_OF_DONE.md` and `docs/19_CODE_REVIEW_CHECKLIST.md`. Build only the production foundation requested by the issue. Run tests, document commands and open a pull request. Do not add business logic or fabricated environmental sample data.