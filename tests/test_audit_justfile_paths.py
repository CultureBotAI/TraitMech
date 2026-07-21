"""Tests for scripts/audit_justfile_paths.py.

The two failing cases are reproductions of real incidents (PR #154), not
invented ones: a recipe invoking an uncommitted script, and a just *variable*
listing uncommitted files. Both reached main and neither was caught by any
existing gate.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from audit_justfile_paths import main, referenced_paths  # noqa: E402


def test_finds_paths_in_recipe_bodies():
    text = """
audit-graphs *args:
    uv run python scripts/audit_causal_graphs.py {{args}}
"""
    assert referenced_paths(text) == {"scripts/audit_causal_graphs.py"}


def test_finds_paths_in_just_variables():
    """The VENDORED_IDLABEL_FILES incident: paths in a variable, not a recipe."""
    text = (
        'VENDORED_IDLABEL_FILES := "scripts/validate_id_label_correspondence.py '
        'tests/test_id_label_empty_adapter.py"\n'
    )
    assert referenced_paths(text) == {
        "scripts/validate_id_label_correspondence.py",
        "tests/test_id_label_empty_adapter.py",
    }


def test_ignores_sibling_repo_paths():
    """`../kg-microbe/scripts/x.py` is another repo's file; we cannot assert it."""
    text = "    uv run python ../kg-microbe/scripts/other.py\n"
    assert referenced_paths(text) == set()


def test_ignores_non_python_and_generated_paths():
    """Only scripts//tests/ .py files are load-bearing here.

    src/…/traitmech_dataclasses.py is a `just gen-schema` output and is
    legitimately absent from git, so the audit must not reach outside
    scripts/ and tests/.
    """
    text = (
        "    uv run gen-pydantic src/traitmech/schema/traitmech.yaml "
        "> src/traitmech/schema/traitmech_dataclasses.py\n"
        "    uv run python scripts/validate_strict.py conf/id_label_targets.yaml\n"
    )
    assert referenced_paths(text) == {"scripts/validate_strict.py"}


def test_real_justfile_passes(capsys):
    """The committed justfile must reference only tracked files."""
    assert main([]) == 0
    assert "All justfile-referenced scripts/tests are tracked." in capsys.readouterr().out


# Deliberately non-existent paths. An earlier version of this test used the
# real filenames from the two incidents, which passed only while those files
# were uncommitted -- committing them inverted the assertion and broke the
# suite. A fixture asserting a file is untracked must name one that can never
# become tracked, or it encodes a snapshot of the working tree.
_ABSENT_SCRIPT = "scripts/__absent_for_test__.py"
_ABSENT_TEST = "tests/__absent_for_test__.py"


@pytest.mark.parametrize(
    "body, offender",
    [
        # Shape of incident 1: a recipe invoking a script that is not committed.
        (
            f'some-recipe target *args="":\n    uv run python {_ABSENT_SCRIPT}\n',
            _ABSENT_SCRIPT,
        ),
        # Shape of incident 2: a just *variable* listing an uncommitted file.
        (
            f'VENDORED_IDLABEL_FILES := "{_ABSENT_TEST}"\n',
            _ABSENT_TEST,
        ),
    ],
)
def test_detects_untracked_reference(tmp_path, capsys, body, offender):
    fake = tmp_path / "justfile"
    fake.write_text(body)
    assert main(["--justfile", str(fake)]) == 1
    assert offender in capsys.readouterr().out


def test_absent_fixtures_really_are_absent():
    """Guard the guard: if someone ever creates these, the tests above go silently
    green-for-the-wrong-reason, which is how the original version broke."""
    for path in (_ABSENT_SCRIPT, _ABSENT_TEST):
        assert not (Path(__file__).resolve().parent.parent / path).exists()
