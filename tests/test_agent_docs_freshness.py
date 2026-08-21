"""Regression checks for high-risk repository guidance.

These assertions intentionally cover policy facts that previously drifted into
the opposite of executable behavior. They do not freeze corpus counts or
proposal versions; the guidance must tell agents how to derive those live.
"""

from __future__ import annotations

import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


def read(relative_path: str) -> str:
    return (REPO_ROOT / relative_path).read_text()


def test_root_claude_guidance_routes_to_canonical_workflows():
    guidance = read("CLAUDE.md")
    assert "just qc" in guidance
    assert "just new-history" in guidance
    assert "explicit user approval" in guidance
    assert ".claude/skills/audit-schema-gaps/SKILL.md" in guidance
    assert "traitmech_dataclasses.py" in guidance
    assert "live implementation" in guidance


def test_schema_gap_alias_has_no_duplicate_procedure_or_snapshot():
    alias = read(".claude/skills/schema-gap-analysis/SKILL.md")
    assert "../audit-schema-gaps/SKILL.md" in alias
    assert len(alias.splitlines()) < 40
    assert not re.search(r"\b\d+\s+records?\b", alias, re.IGNORECASE)


def test_claude_guidance_does_not_restore_known_stale_instructions():
    claude_files = [
        path
        for root in (REPO_ROOT / ".claude/skills", REPO_ROOT / ".claude/commands")
        for path in root.rglob("*.md")
    ]
    content = "\n".join(path.read_text() for path in claude_files)

    stale_phrases = [
        "Don't use the existing `just validate-all`",
        "commit the regenerated `traitmech_dataclasses.py`",
        "Don't forget to commit the regenerated",
        "Expected today:",
        'show "no checks reported"',
        "needs `git add -f`",
        "research/` is gitignored",
    ]
    for phrase in stale_phrases:
        assert phrase not in content


def test_grounding_command_derives_cohort_and_coverage_live():
    command = read(".claude/commands/ground-or-propose-metpo.md")
    assert "just audit-derived-reports" in command
    assert "sort -V" in command
    assert not re.search(r"metpo_traitmech_v\d+", command)
    assert not re.search(r"(?:predicates|nodes) were ~?\d+%", command)


def test_generated_dataclass_policy_matches_gitignore():
    guidance = read(".claude/skills/audit-schema-gaps/SKILL.md")
    gitignore = read(".gitignore")
    generated = "src/traitmech/schema/traitmech_dataclasses.py"
    assert generated in guidance
    assert "do not commit it" in guidance.lower()
    assert generated in gitignore


def test_schema_audit_reports_do_not_restore_resolved_pipeline_claims():
    reports = "\n".join(read(path) for path in [
        "reports/instance_validation_summary.md",
        "reports/schema_gap_audit.md",
        "reports/pipeline_gap_audit.md",
        "reports/gap_fix_backlog.md",
        "reports/gap_fix_backlog.tsv",
    ])
    stale_claims = [
        "runs the CLI in open mode",
        "nothing blocks a PR",
        "the only real trait-YAML writer",
        "does not validate output",
        "Lead item is always **G01",
    ]
    for claim in stale_claims:
        assert claim not in reports
