# 17 Definition of Done

A feature is complete only when:

1. Requirements and acceptance criteria are linked to an Issue.
2. Data fields, provenance and freshness behavior are documented.
3. Database migration is reversible and tested.
4. API schema and error behavior are documented.
5. Authorization is enforced and tested.
6. Unit, integration and relevant end-to-end tests pass.
7. UI handles loading, empty, stale, incomplete and error states.
8. Accessibility checks pass for the affected interface.
9. Logs and metrics exist without exposing secrets or private content.
10. User-facing factual content has traceable sources.
11. No fabricated environmental data is committed as production data.
12. Documentation and release notes are updated.
13. A reviewer other than the implementer approves the pull request.
14. For legal, control, remediation or professional interpretations, the required human-review gate is implemented.
15. The feature runs in the containerized local environment and CI.

## MVP release definition
The MVP is releasable when a user can select an administrative area, view the required environmental sections with sources and timestamps, request custom-length narratives, edit and lock sections, view maps/charts/tables, and export a reproducible DOCX report. The source registry, monthly update framework, audit records and stale-data warnings must be operational.