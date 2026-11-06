#!/usr/bin/env python3
"""Dependency-free structural checks for the starter (not generated apps)."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "AGENTS.md", "CLAUDE.md", "CONTRIBUTING.md", "LICENSE",
    ".github/CODEOWNERS", ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/workflows/validate.yml", ".github/dependabot.yml",
    "templates/PRD.md", "templates/architecture.md",
    "templates/decisions/ADR-template.md", "docs/SETUP.md",
]
SKILLS = (
    "discovery", "prd", "architecture", "planning", "frontend-design",
    "backend-engineering", "ai-agent-engineering", "testing",
    "security-review", "github-maintenance", "documentation", "deployment",
)
errors = []
for rel in REQUIRED:
    if not (ROOT / rel).is_file():
        errors.append(f"Missing required file: {rel}")
for skill in SKILLS:
    rel = f".agents/skills/{skill}/SKILL.md"
    path = ROOT / rel
    if not path.is_file():
        errors.append(f"Missing skill: {rel}")
        continue
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---\n") or not re.search(
        rf"(?m)^name: {re.escape(skill)}$", content
    ):
        errors.append(f"Invalid skill frontmatter: {rel}")
    for heading in ("## Trigger", "## Procedure", "## Deliverable", "## Exit check", "## Conflict policy"):
        if heading not in content:
            errors.append(f"Missing {heading} in {rel}")
for md in ROOT.rglob("*.md"):
    # Ignore generated dependency folders if the validator is copied to an app.
    if any(part in ("node_modules", ".venv") for part in md.parts):
        continue
    content = md.read_text(encoding="utf-8")
    if not content.endswith("\n"):
        errors.append(f"Missing final newline: {md.relative_to(ROOT)}")
# Keep the single orchestrator from being silently shadowed.
if "AGENTS.md" not in (ROOT / "CLAUDE.md").read_text(encoding="utf-8"):
    errors.append("CLAUDE.md must point at AGENTS.md")
if errors:
    print("Validation failed:")
    for error in errors:
        print(" -", error)
    sys.exit(1)
print(f"OK: {len(SKILLS)} skills; starter contracts validated")
