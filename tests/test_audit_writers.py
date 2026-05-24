"""Unit tests for scripts/audit_writers.py.

Locks in:
- Self-suppression (G05): the auditor's own source contains
  `yaml.safe_dump` and would otherwise appear in its own output.
- looks_like_yaml_writer recognizes yaml.dump / .write_text on
  .yaml paths but not arbitrary write_text.
- audit() flags appends_curation_history, has_write_safeguard,
  validates_before_write, and wired_into_just correctly.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from audit_writers import audit, looks_like_yaml_writer  # noqa: E402


# ---------------------------------------------------------------- looks_like_yaml_writer


def test_looks_like_yaml_writer_safe_dump():
    assert looks_like_yaml_writer("yaml.safe_dump(doc)")


def test_looks_like_yaml_writer_dump():
    assert looks_like_yaml_writer("yaml.dump(doc, f)")


def test_looks_like_yaml_writer_write_text_with_yaml_hint():
    assert looks_like_yaml_writer("path.write_text(content)  # .yaml")


def test_looks_like_yaml_writer_write_text_without_yaml_hint_is_false():
    assert not looks_like_yaml_writer("path.write_text('hello')")


def test_looks_like_yaml_writer_arbitrary_code_is_false():
    assert not looks_like_yaml_writer("print('nothing to see')")


# ---------------------------------------------------------------- audit (per-file)


_JUSTFILE = """\
seed-from-metpo:
    uv run python scripts/seed_from_metpo.py
"""


def _writer_text(
    *, curation: bool = False, dry_run: bool = False, validates: bool = False
) -> str:
    parts = ["import yaml", "doc = {}"]
    if curation:
        parts.append("doc['curation_history'].append({'curator': 'me'})")
    if dry_run:
        parts.append("ap.add_argument('--dry-run')")
    if validates:
        parts.append("from linkml.validator import Validator")
        parts.append("validator = Validator()")
        parts.append("validator.validate(doc)")  # matches `validator\.validate\(`
    parts.append("yaml.safe_dump(doc)")
    return "\n".join(parts)


def test_audit_recognizes_full_safeguards(tmp_path):
    p = tmp_path / "good_writer.py"
    p.write_text(_writer_text(curation=True, dry_run=True, validates=True))
    row = audit(p, _JUSTFILE)
    assert row is not None
    assert row["writes_yaml"] == "yes"
    assert row["appends_curation_history"] == "yes"
    assert row["has_write_safeguard"] == "yes"
    assert row["validates_before_write"] == "yes"


def test_audit_flags_missing_safeguards(tmp_path):
    p = tmp_path / "bad_writer.py"
    p.write_text(_writer_text(curation=False, dry_run=False, validates=False))
    row = audit(p, _JUSTFILE)
    assert row is not None
    assert row["appends_curation_history"] == "no"
    assert row["has_write_safeguard"] == "no"
    assert row["validates_before_write"] == "no"


def test_audit_returns_none_for_non_writer(tmp_path):
    p = tmp_path / "not_a_writer.py"
    p.write_text("def main(): print('hello')")
    assert audit(p, _JUSTFILE) is None


def test_audit_wired_into_just_yes_when_stem_present(tmp_path):
    p = tmp_path / "seed_from_metpo.py"
    p.write_text(_writer_text())
    row = audit(p, _JUSTFILE)
    assert row is not None
    assert row["wired_into_just"] == "yes"


def test_audit_wired_into_just_no_when_absent(tmp_path):
    p = tmp_path / "uncalled.py"
    p.write_text(_writer_text())
    row = audit(p, _JUSTFILE)
    assert row is not None
    assert row["wired_into_just"] == "no"


# ---------------------------------------------------------------- self-suppression (G05)


def test_audit_suppresses_self_match():
    """The auditor must not appear in its own output (G05 from PR #64)."""
    self_path = REPO_ROOT / "scripts" / "audit_writers.py"
    row = audit(self_path, _JUSTFILE)
    assert row is None, "audit_writers.py must not flag itself"
