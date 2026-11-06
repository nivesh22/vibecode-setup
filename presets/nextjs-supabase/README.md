# Optional preset: Next.js + Supabase

Choose this **only after architecture approval**; it is a checklist, not a full generated application.

- Next.js with TypeScript and server/client component boundaries.
- Supabase auth with **server-side authorization and RLS** (RLS policies require explicit tests).
- Separate local/staging/prod projects; never embed service-role keys in browser bundles.
- Use schema migrations with review, seed test data and define rollback.
- Prefer [Vercel's maintained agent skills](https://github.com/vercel-labs/agent-skills) as **optional** performance references; check license/version before installation.
- CI should run install (with lockfile), lint, typecheck, unit/integration tests and build.
- Environment example: NEXT_PUBLIC_SUPABASE_URL, NEXT_PUBLIC_SUPABASE_ANON_KEY. Do not use actual secrets in this repo.

This preset does not provision a database or configure deployment.