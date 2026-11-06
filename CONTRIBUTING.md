# Contributing

1. Start with an issue; make the problem, acceptance criteria and scope explicit.
2. Claim an issue before editing. Use one issue per PR and a separate feature branch or worktree.
3. Follow AGENTS.md and only the relevant skill. Preserve existing decisions unless the PR explicitly proposes a change.
4. Run `python3 scripts/validate.py`. For generated applications run their own lint, type-check, unit/integration tests and build.
5. Open a PR using the template; include test evidence, security considerations, breaking changes and docs.
6. Request review and address comments; do not self-merge without repository policy explicitly allowing it.
7. Never commit API keys, personal data, production credentials or generated secrets.

## Files and naming

Skills: `.agents/skills/<name>/SKILL.md` with YAML frontmatter. Keep skills independent, specific and verifiable. Reusable docs live in `templates/`; technology checklists live in `presets/`. Propose third-party integrations with a version, license and security review before adding them.

## Maintaining this starter

Treat instructions as code: every change should have an example usage, validation, clear backward-compatibility note and reviewer. Do not change lifecycle ownership casually.
