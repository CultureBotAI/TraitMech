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


def test_looks_like_yaml_writer_write_text_of_yaml_dump():
    """The post-#75 heuristic requires `write_text(yaml.dump(...))` —
    the yaml-serializer call must feed directly into write_text on the
    same line for the script to count as a YAML writer."""
    assert looks_like_yaml_writer("path.write_text(yaml.safe_dump(doc))")
    assert looks_like_yaml_writer("path.write_text( yaml.dump(doc) )")


def test_looks_like_yaml_writer_write_text_of_json_is_false():
    """A .write_text call writing JSON is NOT a YAML writer even if the
    file also reads from *.yaml elsewhere (the false-positive case
    that #75 fixed for scripts/build_embedding_index.py and
    scripts/render_trait_pages.py)."""
    src = (
        "for p in Path('data/traits').rglob('*.yaml'):\n"
        "    doc = yaml.safe_load(p.read_text())\n"
        "path.write_text(json.dumps(payload))\n"
    )
    assert not looks_like_yaml_writer(src)


def test_looks_like_yaml_writer_write_text_plain_is_false():
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


# ---------------------------------------------------------------- library-helper exemption


_LIB_HELPER_BODY = (
    '"""I am a library helper.\n\n'
    "audit-writers: library-helper\n"
    '"""\n'
    "import yaml\n"
    "def write(doc, path):\n"
    "    path.write_text(yaml.safe_dump(doc))\n"
)


def test_audit_skips_library_helper_marker(tmp_path):
    """A YAML-writing module under src/traitmech/ that opts out via
    the standalone-line `audit-writers: library-helper` marker is
    excluded — its curation_history and safeguard responsibilities
    belong to callers, not the helper."""
    sub = tmp_path / "src" / "traitmech" / "validation"
    sub.mkdir(parents=True)
    p = sub / "lib_helper.py"
    p.write_text(_LIB_HELPER_BODY)
    assert audit(p, _JUSTFILE) is None, (
        "src/traitmech/ modules with the library-helper marker must be "
        "excluded from the CLI-writer audit"
    )


def test_audit_does_not_skip_without_marker(tmp_path):
    """Sanity-check the exemption is opt-in: a writer without the marker
    is still audited normally."""
    sub = tmp_path / "src" / "traitmech" / "validation"
    sub.mkdir(parents=True)
    p = sub / "no_marker.py"
    p.write_text(
        "import yaml\n"
        "def write(doc, path):\n"
        "    path.write_text(yaml.safe_dump(doc))\n"
    )
    row = audit(p, _JUSTFILE)
    assert row is not None, "writer without marker must still be audited"
    assert row["writes_yaml"] == "yes"


def test_audit_does_not_skip_cli_writer_with_marker(tmp_path):
    """A CLI writer under scripts/ that mentions the marker phrase
    (e.g. in a docstring) must NOT be exempted — only files under
    src/traitmech/ can opt out, so scripts can't silently suppress
    themselves."""
    sub = tmp_path / "scripts"
    sub.mkdir()
    p = sub / "rogue_cli_writer.py"
    p.write_text(_LIB_HELPER_BODY)  # same body, just under scripts/
    row = audit(p, _JUSTFILE)
    assert row is not None, (
        "scripts/ files must NOT be able to opt out of the audit via "
        "the library-helper marker"
    )
    assert row["writes_yaml"] == "yes"


def test_audit_does_not_skip_marker_in_narrative_text(tmp_path):
    """A library file that mentions the marker phrase inside a
    sentence/paragraph (not on its own line) is NOT exempted — only
    the standalone-line directive opts out."""
    sub = tmp_path / "src" / "traitmech"
    sub.mkdir(parents=True)
    p = sub / "narrative.py"
    p.write_text(
        '"""A module whose docstring discusses the audit-writers: '
        'library-helper convention as PROSE without using it as a '
        'directive."""\n'
        "import yaml\n"
        "def write(doc, path):\n"
        "    path.write_text(yaml.safe_dump(doc))\n"
    )
    row = audit(p, _JUSTFILE)
    assert row is not None, (
        "marker inside running prose must not exempt the file"
    )


def test_audit_excludes_write_validated_helper():
    """End-to-end: the canonical write_validated.py library helper has
    the marker and is excluded from the audit."""
    helper_path = REPO_ROOT / "src" / "traitmech" / "validation" / "write_validated.py"
    assert helper_path.exists(), "write_validated.py must be on disk for this test"
    row = audit(helper_path, _JUSTFILE)
    assert row is None, (
        "write_validated.py opts out via the library-helper marker; "
        "audit_writers must exclude it"
    )
