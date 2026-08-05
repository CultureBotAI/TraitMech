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

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import audit_qc_paths_coverage as aqp  # noqa: E402
from audit_qc_paths_coverage import (  # noqa: E402
    AUDIT_READ_SET,
    BlindGate,
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


def test_the_real_read_set_does_not_shrink():
    """A ratchet, because `findings == []` is also satisfied by inferring less.

    `conf` is contributed by exactly two scripts, both of which also read data/
    and reports/ — so moving only their conf constants to a shared helper leaves
    every script non-silent and the union non-empty, and `conf/**` could then be
    deleted from the filter with the gate still green (#288).
    """
    audit(REPO_ROOT)
    required = {"conf", "data", "justfile", "mappings", "pages", "reports",
                "research", "scripts", "src"}
    missing = required - AUDIT_READ_SET
    assert not missing, f"read-set shrank, so the gate now infers less: {sorted(missing)}"


# --- liveness: a blind gate must not read as a clean one (#286) --------------


def test_a_missing_qc_chain_raises_rather_than_passing(tmp_path):
    """`qc *args:` or a rename yields no chain — which must not look like success."""
    root = _repo(tmp_path, filter_paths=["data/**"], script_reads=["data/traits"])
    jf = root / "justfile"
    jf.write_text(jf.read_text().replace("qc: audit-thing", "qc *args: audit-thing"))
    with pytest.raises(BlindGate, match="no `qc:` dependency chain"):
        audit(root)


def test_a_script_contributing_nothing_raises_rather_than_passing(tmp_path, monkeypatch):
    """Per-script liveness. Stubbing every read hits this branch, not the union
    one — the previous version of this test claimed the union branch while
    exercising this, because both messages contain "no readable paths" (#288)."""
    root = _repo(tmp_path, filter_paths=["data/**"], script_reads=["data/traits"])
    monkeypatch.setattr(aqp, "paths_read", lambda script, root: set())
    with pytest.raises(BlindGate, match="were not examined at all"):
        audit(root)


def test_one_blind_script_among_many_still_raises(tmp_path, monkeypatch):
    """The case the union check missed: conf comes from two scripts that also
    read data/ and reports/, so moving only their conf constants leaves the
    union large and every script non-silent (#288)."""
    root = _repo(tmp_path, filter_paths=["data/**", "conf/**"],
                 script_reads=["data/traits"])
    (root / "scripts/other.py").write_text(
        'REPO_ROOT = 1\nX = REPO_ROOT / "conf"\n')
    (root / "conf").mkdir(exist_ok=True)
    jf = root / "justfile"
    jf.write_text(jf.read_text().replace(
        "qc: audit-thing",
        "audit-other:\n    uv run python scripts/other.py\n\n"
        "qc: audit-thing audit-other"))
    real = aqp.paths_read
    monkeypatch.setattr(aqp, "paths_read",
                        lambda script, r: set() if script.name == "other.py" else real(script, r))
    with pytest.raises(BlindGate, match="scripts/other.py"):
        audit(root)


def test_the_read_set_is_published_for_the_success_message(tmp_path):
    """"0 findings" alone cannot be told from "inspected nothing"."""
    root = _repo(tmp_path, filter_paths=["data/**", "conf/**"],
                 script_reads=["data/traits", "conf"])
    assert audit(root) == []
    assert {"data", "conf"} <= AUDIT_READ_SET


def test_a_recipe_name_is_matched_exactly_not_by_prefix():
    """recipe_body("check") used to return check-biolink-coverage's body (#287)."""
    text = "check-other:\n    run wrong\n\ncheck:\n    run right\n"
    body = recipe_body(text, "check")
    assert "run right" in body
    assert "run wrong" not in body


def test_the_real_justfile_resolves_check_to_itself():
    """The live instance from the #285 review, pinned against the real file.

    `check: lint test` is dependency-only, so its body is legitimately empty —
    which is the point. Before the exact-match fix, prefix matching returned
    `check-biolink-coverage`'s body instead, and an empty result is the correct
    answer that the bug replaced with a wrong non-empty one. Asserting emptiness
    rather than merely the absence of "biolink" makes this fail if the match
    ever wanders to any other recipe, not just that one.
    """
    body = recipe_body((REPO_ROOT / "justfile").read_text(), "check")
    assert body.strip() == "", f"recipe_body('check') matched another recipe: {body[:80]!r}"
