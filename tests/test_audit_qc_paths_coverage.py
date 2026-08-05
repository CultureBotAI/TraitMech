"""Unit tests for scripts/audit_qc_paths_coverage.py.

This gate exists because the same bug recurred four times (#184, #200, #250, and
the `conf/` instance it found on its first run — #252). A gate against a
four-time bug that cannot itself fail is worse than no gate, so these assert
both directions against a synthetic repo, plus the real tree.
"""

from __future__ import annotations

import sys
import textwrap
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from audit_qc_paths_coverage import (  # noqa: E402
    audit,
    filter_tops,
    qc_chain,
    recipe_body,
    scripts_invoked,
)


def _repo(tmp_path: Path, *, filter_paths: list[str], script_reads: list[str]) -> Path:
    (tmp_path / ".github/workflows").mkdir(parents=True)
    (tmp_path / "scripts").mkdir()
    for read in script_reads:
        (tmp_path / read.split("/")[0]).mkdir(exist_ok=True)
    (tmp_path / "justfile").write_text(textwrap.dedent("""\
        audit-thing:
            uv run python scripts/audit_thing.py

        qc: audit-thing
        """))
    reads = "\n".join(f'X{i} = REPO_ROOT / "{r}"' for i, r in enumerate(script_reads))
    (tmp_path / "scripts/audit_thing.py").write_text(
        f"REPO_ROOT = 1\n{reads}\n")
    paths = "\n".join(f'      - "{p}"' for p in filter_paths)
    (tmp_path / ".github/workflows/qc.yaml").write_text(
        f"name: qc\non:\n  pull_request:\n    paths:\n{paths}\njobs:\n  qc:\n    runs-on: x\n")
    return tmp_path


def test_a_covered_directory_is_clean(tmp_path):
    root = _repo(tmp_path, filter_paths=["data/**"], script_reads=["data/traits"])
    assert audit(root) == []


def test_an_uncovered_directory_is_flagged(tmp_path):
    """The `conf/` case: read by the chain, absent from the filter."""
    root = _repo(tmp_path, filter_paths=["data/**"], script_reads=["conf"])
    findings = audit(root)
    assert [f["path"] for f in findings] == ["conf"]
    assert "audit-thing" in findings[0]["readers"]


def test_a_path_the_script_names_but_the_repo_lacks_is_ignored(tmp_path):
    """Prose and illustrations are not reads — this script's own docstring
    contains `REPO_ROOT / "..."` and was flagged on the first run."""
    root = _repo(tmp_path, filter_paths=["data/**"], script_reads=["data/traits"])
    (root / "scripts/audit_thing.py").write_text(
        'REPO_ROOT = 1\nX = REPO_ROOT / "data"\n# see REPO_ROOT / "..." for the shape\n')
    assert audit(root) == []


def test_coverage_is_matched_at_the_top_level(tmp_path):
    """`data/embeddings/**` covers a read of `data/raw`, deliberately.

    Demanding an exact match would flag every recipe touching data/ at all; the
    failure being guarded is a directory missing entirely.
    """
    root = _repo(tmp_path, filter_paths=["data/embeddings/**"],
                 script_reads=["data/raw"])
    assert audit(root) == []


def test_the_qc_chain_is_parsed_from_the_justfile():
    text = "qc: pr-sanity audit-graphs audit-snippets\n"
    assert qc_chain(text) == ["pr-sanity", "audit-graphs", "audit-snippets"]


def test_no_qc_recipe_yields_no_chain():
    assert qc_chain("build:\n    echo hi\n") == []


def test_scripts_are_extracted_from_a_recipe_body():
    body = "    uv run python scripts/a_b.py --flag\n    uv run python scripts/c.py\n"
    assert scripts_invoked(body) == ["scripts/a_b.py", "scripts/c.py"]


def test_the_bare_on_key_is_read_despite_yaml_1_1():
    """PyYAML resolves `on:` to boolean True, which a plain doc["on"] misses."""
    wf = 'name: qc\non:\n  pull_request:\n    paths:\n      - "conf/**"\n'
    assert filter_tops(wf) == {"conf"}


def test_recipe_body_stops_at_the_next_recipe():
    text = "a:\n    run a\n\nb:\n    run b\n"
    assert "run a" in recipe_body(text, "a")
    assert "run b" not in recipe_body(text, "a")


def test_the_real_repo_satisfies_its_own_gate():
    """Fixture-only tests would let the gate pass while the tree drifts."""
    findings = audit(REPO_ROOT)
    assert findings == [], (
        "qc reads a directory qc.yaml's filter omits: "
        + ", ".join(f["path"] for f in findings))
