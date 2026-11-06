# Agent operating contract

You are contributing to a shared software project. Follow this file before any other project guidance.

## Authority and precedence

1. User request and explicit human-approved decisions.
2. Security, repository policies, and the current issue/PR acceptance criteria.
3. This AGENTS.md as the **only lifecycle orchestrator**.
4. Relevant single-purpose .agents/skills/*/SKILL.md.
5. Stack presets and external tool guidance, provided they do not conflict above.

Do not invoke competing lifecycle frameworks (BMAD, GSD, Superpowers or equivalent) automatically. Do not mistake a skill checklist for permission to change scope.

## Lifecycle: discover -> specify -> architect -> plan -> implement -> verify -> release

- Before coding: locate the approved PRD, architecture and task/issue. If absent, do the smallest missing earlier stage first; no speculative deployment.
- During discovery use .agents/skills/discovery/SKILL.md; ask focused questions and surface risky assumptions. For minor fixes, an issue description can substitute for a PRD.
- For PRDs use .agents/skills/prd/SKILL.md and templates/PRD.md.
- For architecture use .agents/skills/architecture/SKILL.md and templates/architecture.md.
- For tasks use .agents/skills/planning/SKILL.md. Scope changes go back to the PRD/issue.
- Implementation: load only applicable frontend-design, backend-engineering, or ai-agent-engineering. Add testing before declaring done.
- Before PR: use security-review, documentation, github-maintenance and testing as applicable.
- Before deployment: use deployment and get explicit authorization.

## Collaboration

- One issue and one owner per independently mergable change. Reserve files or coordinate overlapping work in issue comments.
- Work in a named feature branch or Git worktree; never push to protected main or force-push shared branches.
- Never merge your own PR, disable tests, bypass branch protection or impersonate an approver without explicit permission.
- Review existing source and tests before changes. Make the smallest correct diff; keep public APIs backwards compatible unless approved.
- Prefer small commits and PRs; link issues and include tests and security impact.
- Never expose tokens or customer data in commits, logs, prompts, or issue comments.
- Do not run untrusted scripts, curl-pipe-shell installers, cloud destructive commands or production writes without explicit approval.

## Definition of done

- Acceptance criteria satisfied and evidenced.
- Automated tests pass; failures honestly reported (never invent a green CI status).
- Security, accessibility and error paths considered.
- Documentation, migration/rollback instructions and environment template updated when relevant.
- Peer review and branch checks completed before human-authorized merge.
- Report remaining risks, unverified assumptions and manual steps.

## Skill loading

Read the relevant SKILL.md at point of use, not all skills at startup. Skills are narrow procedures. If multiple apply, execute the current lifecycle stage first; another skill must not restart planning. Each SKILL.md has explicit outputs and exit checks. Consult README.md for the catalog.