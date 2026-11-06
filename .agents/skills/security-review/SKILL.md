---
name: security-review
description: Review application, dependency and cloud security before PR and release.
---

# security-review

## Trigger

Review application, dependency and cloud security before PR and release. Load only for the relevant lifecycle stage in AGENTS.md.

## Scope

Apply least privilege and secure defaults.

## Procedure

1. Threat-model identities, trust boundaries and sensitive data.
2. Check authorization server-side, input validation, rate limiting and audit logging.
3. Scan for secrets and unsafe dependencies; use GitHub secrets or cloud secret manager, never commit credentials.
4. Examine workflows for excessive token permissions and untrusted PR code execution.
5. Verify privacy/retention, network exposure and production IAM before deployment.

## Deliverable

Findings ranked by severity with remediation, evidence and owner.

## Exit check

Block critical/high unresolved flaws from release; never claim a full audit based on a checklist.

## Conflict policy

AGENTS.md owns phase order and human approval gates. This skill does not supersede another lifecycle stage, tool permissions, or repository rules.
