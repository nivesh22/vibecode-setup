# VibeCode Setup

A cloud-ready, agent-agnostic starter kit for building software with humans and AI coding agents. One workflow owner, specialized skills loaded only when needed, and GitHub collaboration safeguards.

## Quick start

1. Select **Use this template** on GitHub (once template-repository setting is enabled), or clone this repository.
2. Open the project in Codex, Claude Code, Cursor, or another coding agent that can read `AGENTS.md`.
3. Ask: **"Read AGENTS.md and start discovery for my project."**
4. Work through discovery → PRD → architecture → plan → small implementation PRs → verification → release.
5. Choose an optional preset (React/FastAPI, Next.js/Supabase, or Python agents) only after architecture decisions.

> This repository is a **workflow and skill starter**, not a deployed application. It does not install dependencies, create cloud accounts, or provision infrastructure automatically.

## Philosophy

- **One orchestrator:** `AGENTS.md` defines the lifecycle. Skills supply task-specific checklists; none can override the orchestrator.
- **No competing frameworks:** This repository does not bundle BMAD, GSD, Superpowers, gstack or other end-to-end controllers. It provides a small original, compatible baseline inspired by strong practices from that ecosystem.
- **Progressive disclosure:** The agent reads only the skill needed for the current task. Never load all skills into every prompt.
- **Human review:** Agents may propose changes but must not silently merge, deploy, change production resources, or handle secrets.
- **Portable:** Plain Markdown instructions work across tools; tool-specific support for auto-discovery varies.
- **No hidden network install:** Nothing executes remote setup scripts or installs unpinned third-party skills.

## Skill catalog

| Stage | Skill | When to use |
| --- | --- | --- |
| 1 | [discovery](.agents/skills/discovery/SKILL.md) | Idea is ambiguous; challenge assumptions (Grill-Me style) |
| 2 | [prd](.agents/skills/prd/SKILL.md) | Turn discovery into a testable PRD |
| 3 | [architecture](.agents/skills/architecture/SKILL.md) | Choose stack, boundaries, data and cloud |
| 4 | [planning](.agents/skills/planning/SKILL.md) | Break an approved design into small tasks |
| 5 | [frontend-design](.agents/skills/frontend-design/SKILL.md) | UI, accessibility and responsive layouts |
| 5 | [backend-engineering](.agents/skills/backend-engineering/SKILL.md) | APIs, databases, migrations |
| 5 | [ai-agent-engineering](.agents/skills/ai-agent-engineering/SKILL.md) | LLM workflows, prompts, evals |
| 6 | [testing](.agents/skills/testing/SKILL.md) | TDD, unit/integration/e2e checks |
| 6 | [security-review](.agents/skills/security-review/SKILL.md) | Auth, secrets, supply chain and cloud |
| 7 | [github-maintenance](.agents/skills/github-maintenance/SKILL.md) | Issues, PRs, branches, contributors |
| 8 | [documentation](.agents/skills/documentation/SKILL.md) | Keep docs synced with decisions |
| 9 | [deployment](.agents/skills/deployment/SKILL.md) | Cloud releases and rollbacks |

Each skill is an original `SKILL.md` with a narrow trigger, steps, outputs, and a completion gate. Use the document templates in `templates/` and stack checklists in `presets/`.

## Team workflow

1. Open an issue with acceptance criteria and a single owner.
2. Make a small feature branch or isolated worktree. Avoid two agents editing the same files concurrently.
3. Open a PR using the provided template; link the issue, describe risk, and include test evidence.
4. Run CI, request review (CODEOWNERS where appropriate), then merge with an authorized human.
5. Record meaningful decisions in an ADR. Keep the PRD and runbook aligned.

`CODEOWNERS` is advisory until repository rules/branch protection are configured in GitHub settings. The included CI validates this starter kit; it **does not automatically test applications generated from it**. Add project-specific build, tests, secret scanning and deployment checks before shipping.

## Tool compatibility

- **Codex / AGENTS.md-aware agents:** read `AGENTS.md` first and open referenced `SKILL.md` files as directed.
- **Claude Code:** `CLAUDE.md` points at `AGENTS.md`. Native skill auto-discovery may require adapting the skill folder to the tool's conventions.
- **Cursor / other IDE agents:** explicitly point the agent at `AGENTS.md` or adapt a native rules file. Do not assume every IDE automatically discovers `.agents/skills`.

## External ecosystem (optional, not bundled)

- [Matt Pocock skills](https://github.com/mattpocock/skills) — discovery / spec inspiration
- [Superpowers](https://github.com/obra/superpowers) — disciplined engineering lifecycle
- [BMAD](https://github.com/bmad-code-org/BMAD-METHOD) — comprehensive team methodology
- [Vercel agent skills](https://github.com/vercel-labs/agent-skills) — web performance guidance
- [PR-Agent](https://github.com/qodo-ai/pr-agent) — optional GitHub PR review integration

**Do not install another workflow orchestrator on top of this one without disabling its overlapping lifecycle instructions.** Assess upstream licenses, permissions and version pins independently before installing optional tools.

## Validate

```bash
python3 scripts/validate.py
```

## What still requires a human

Enable GitHub's template-repository setting, configure branch rules and required CI, choose reviewers, supply cloud credentials only through your provider's secret store, and approve deployments. See [setup checklist](docs/SETUP.md).

## License

MIT. See [LICENSE](LICENSE).
