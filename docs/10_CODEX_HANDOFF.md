# 10 Codex Handoff

## Objective

Implement the first production-capable skeleton for EIP. Read all documents in `/docs` before changing code.

## Initial implementation scope

1. Monorepo structure with `frontend`, `backend`, `worker`, `database`, `infra` and `docs`.
2. Next.js + TypeScript frontend.
3. FastAPI backend with `/health` and `/api/v1` routing.
4. PostgreSQL + PostGIS and migration framework.
5. Docker Compose local development.
6. Initial models: towns, source datasets, sync jobs, reports, report sections, references and projects.
7. OpenAPI, linting, tests and CI.
8. No fabricated environmental sample data.

## Required quality gates

- application starts with one documented command
- database migrations run from a clean database
- tests pass in CI
- environment variables documented in `.env.example`
- no secrets in repository
- source provenance fields included from first migration
- architecture decisions documented as ADRs

## First Codex task

Create a branch named `codex/bootstrap-platform`. Implement only the scalable skeleton and the first migrations. Do not implement AI generation, legal conclusions or real data imports yet. Open a draft pull request describing architecture choices, commands, tests and remaining risks.

## Definition of done

- `docker compose up` starts database, API and web app
- API health endpoint works
- frontend displays a system status page
- migrations create PostGIS extension and core tables
- CI runs formatting, type checks and tests
- README contains exact local setup and troubleshooting steps

## Non-negotiable constraints

- Keep imported data provenance and versioning.
- Separate official source facts from generated narrative.
- Legal and engineering modules remain human-reviewed drafts.
- Mobile-first field workflows must remain possible.