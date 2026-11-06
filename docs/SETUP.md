# Setup and adoption checklist

## Create a project

1. In the repository's **Settings > General**, enable **Template repository** if you have administrative access. This is a GitHub setting, not a file this starter can enable.
2. Select **Use this template**, or clone and rename the repository.
3. Tell your coding agent to read `AGENTS.md`. Test whether your particular IDE auto-discovers `.agents/skills`; explicitly open a skill if it does not.
4. Write a discovery brief, then PRD, architecture and task list. Select only a relevant stack preset.
5. Add actual application code and project-specific checks to CI. The starter validator checks documentation conventions only.

## GitHub team safeguards

1. Protect `main` with a ruleset/branch protection: require PRs, at least one reviewer, up-to-date branch and checks appropriate to the application.
2. Require the `validate` check once GitHub Actions runs. Add app build/test checks separately.
3. Configure CODEOWNERS for real owners (default is @nivesh22); review requests are enforceable only if relevant rules are enabled.
4. Consider disallowing force pushes and deleting protected branches.
5. Optional: install PR-Agent or CodeRabbit from trusted publishers; follow their pricing, permissions and privacy controls. Do not install both without a reason.
6. Use issue assignment and Git worktrees/feature branches to isolate simultaneous agents.

## Cloud safeguards

- Never commit secrets. Use environment templates and managed secret stores.
- Choose cloud provider, account, region, budgets and permissions explicitly.
- Separate staging from production and gate production deploys with environment approvals.
- Configure monitoring, health checks, database backup, migration and rollback.
- Do not enable deployment from untrusted pull-request code with write permissions.

## Maintenance

- Run `python3 scripts/validate.py` on every skill change.
- Review third-party upstream versions, licenses and permission scopes before copying or installing.
- Keep one lifecycle controller; review overlaps before adding any large agent framework.
