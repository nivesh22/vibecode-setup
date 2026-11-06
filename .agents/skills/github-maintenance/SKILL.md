---
name: github-maintenance
description: Coordinate human and AI contributors through issues, PRs and CI.
---

# github-maintenance

## Trigger

Coordinate human and AI contributors through issues, PRs and CI. Load only for the relevant lifecycle stage in AGENTS.md.

## Scope

GitHub policy and human review remain authoritative.

## Procedure

1. Triage backlog, deduplicate issues and assign one owner per change.
2. Check open PRs and changed paths for parallel work conflicts.
3. Keep branches short-lived; require linked issue and reviewable scope.
4. Use CODEOWNERS and required checks where configured; do not assume committed config enables protection.
5. Summarize stalled PRs, dependencies, release notes and post-merge follow-ups.

## Deliverable

Maintainer status report, issue/PR links, review queue and release checklist.

## Exit check

Never silently close issues, approve own code, auto-merge or alter branch rules without authorization.

## Conflict policy

AGENTS.md owns phase order and human approval gates. This skill does not supersede another lifecycle stage, tool permissions, or repository rules.
