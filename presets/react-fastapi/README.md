# Optional preset: React + FastAPI

Use after design signoff.

- React + TypeScript frontend with accessible components and API client contract.
- FastAPI with Pydantic validation, structured errors, typed schemas and versioned endpoints.
- SQL migrations (e.g. Alembic) and role-based access checks on server.
- Contract tests between frontend and API; unit/integration/e2e tests with fake external services.
- Containerized staging deployment with health checks and least-privilege credentials.
- CI: frontend install+lint+typecheck+test+build; backend install+lint+typecheck+pytest.

No framework packages are bundled; pin supported versions when scaffolding.
