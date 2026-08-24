# PostgreSQL / PostGIS operations

Production must use PostgreSQL 16 with PostGIS 3.4 or newer. Never expose port 5432 publicly. Use a managed secret for `DATABASE_URL`, TLS (`sslmode=require`) outside the private container network, daily encrypted backups, point-in-time recovery, and a separate least-privilege migration identity.
