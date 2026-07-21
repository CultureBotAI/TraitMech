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


@pytest.mark.parametrize(
    "body, offender",
    [
        # Incident 1: recipes for scripts that were never committed.
        (
            "research-trait-edison target *args=\"\":\n"
            "    uv run --extra dev python scripts/research_trait_edison.py\n",
            "scripts/research_trait_edison.py",
        ),
        # Incident 2: a just variable listing an uncommitted file.
        (
            'VENDORED_IDLABEL_FILES := "scripts/chem_formula.py"\n',
            "scripts/chem_formula.py",
        ),
    ],
)
def test_detects_untracked_reference(tmp_path, capsys, body, offender):
    fake = tmp_path / "justfile"
    fake.write_text(body)
    assert main(["--justfile", str(fake)]) == 1
    assert offender in capsys.readouterr().out
