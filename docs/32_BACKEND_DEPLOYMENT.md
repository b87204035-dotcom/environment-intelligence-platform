# Backend deployment

## Local MVP

1. Copy `.env.example` to `.env` and replace `POSTGRES_PASSWORD`.
2. Run `docker compose up --build -d`.
3. Verify `curl --fail http://localhost:8001/health` and open `http://localhost:8001/docs`.
4. Add only reviewed official datasets to `source_datasets`; never use search-result URLs or guessed endpoints. Run `python scripts/sync_sources.py <dataset_key>` from an environment with the backend package installed.

## Production

Create the protected GitHub `production` environment with `DEPLOY_HOST`, `DEPLOY_USER`, and `DEPLOY_SSH_KEY`. On the host, create `/opt/eip/.env` with `DATABASE_URL`, `CORS_ORIGINS`, and optional OpenAI settings. The database must be managed PostGIS or separately backed up; it is deliberately not created by the production Compose file.

Push a reviewed semantic version tag. The deployment workflow builds and publishes the API image, copies the production descriptor, pulls the exact tag, runs Alembic migrations at container startup, and health-checks the service on loopback port 8001. Terminate TLS and authentication at the production ingress. Roll back by redeploying the prior immutable tag after confirming migration compatibility.
