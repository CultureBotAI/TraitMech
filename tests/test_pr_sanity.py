"""Unit tests for scripts/pr_sanity.py.

The point of pr_sanity is to run on PRs that no other workflow inspects, so a
check that silently matches nothing would recreate the exact problem it exists
to solve (#200). These therefore assert both directions for every check: that it
fires on a real defect, and that it stays quiet on the legitimate lookalike.
"""

from __future__ import annotations

import subprocess
import sys
import textwrap
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from pr_sanity import (  # noqa: E402
    CONFLICT_RE,
    check_conflict_markers,
    check_markdown_links,
    check_workflows,
    sanity,
)

UNFILTERED_WF = """\
name: catchall
on:
  pull_request:
jobs:
  a:
    runs-on: ubuntu-latest
    steps: [{run: "true"}]
"""

FILTERED_WF = """\
name: narrow
on:
  pull_request:
    paths:
      - "src/**"
jobs:
  a:
    runs-on: ubuntu-latest
    steps: [{run: "true"}]
"""


def _repo(tmp_path: Path) -> Path:
    """A real git repo — pr_sanity reads the file list from `git ls-files`."""
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    (tmp_path / ".github" / "workflows").mkdir(parents=True)
    return tmp_path


def _commit(root: Path) -> None:
    subprocess.run(["git", "add", "-A"], cwd=root, check=True)


def _checks(findings) -> set[str]:
    return {f["check"] for f in findings}


# --- workflow validity ------------------------------------------------------


def test_valid_unfiltered_workflow_is_clean(tmp_path):
    root = _repo(tmp_path)
    (root / ".github/workflows/a.yaml").write_text(UNFILTERED_WF)
    assert check_workflows(root) == []


def test_unparseable_workflow_flagged(tmp_path):
    root = _repo(tmp_path)
    (root / ".github/workflows/a.yaml").write_text(UNFILTERED_WF)
    (root / ".github/workflows/bad.yaml").write_text("name: x\n  bad: [indent\n")
    assert "WORKFLOW_INVALID" in _checks(check_workflows(root))


def test_workflow_without_jobs_flagged(tmp_path):
    root = _repo(tmp_path)
    (root / ".github/workflows/a.yaml").write_text(UNFILTERED_WF)
    (root / ".github/workflows/nojobs.yaml").write_text("name: x\non:\n  push:\n")
    findings = check_workflows(root)
    assert any(f["check"] == "WORKFLOW_INVALID" and "jobs" in f["detail"]
               for f in findings)


# --- the #200 invariant -----------------------------------------------------


def test_all_filtered_workflows_trips_the_invariant(tmp_path):
    """Every workflow behind a paths filter == some PRs run nothing."""
    root = _repo(tmp_path)
    (root / ".github/workflows/a.yaml").write_text(FILTERED_WF)
    (root / ".github/workflows/b.yaml").write_text(FILTERED_WF)
    assert "NO_UNFILTERED_CI" in _checks(check_workflows(root))


def test_one_unfiltered_workflow_satisfies_the_invariant(tmp_path):
    root = _repo(tmp_path)
    (root / ".github/workflows/a.yaml").write_text(FILTERED_WF)
    (root / ".github/workflows/b.yaml").write_text(UNFILTERED_WF)
    assert "NO_UNFILTERED_CI" not in _checks(check_workflows(root))


def test_pull_request_with_empty_paths_list_counts_as_unfiltered(tmp_path):
    root = _repo(tmp_path)
    (root / ".github/workflows/a.yaml").write_text(
        "name: x\non:\n  pull_request:\n    branches: [main]\njobs:\n"
        "  a:\n    runs-on: ubuntu-latest\n    steps: [{run: \"true\"}]\n"
    )
    assert "NO_UNFILTERED_CI" not in _checks(check_workflows(root))


def test_missing_workflows_dir_is_a_finding_not_a_skip(tmp_path):
    """A deleted CI directory must fail, not pass quietly. An early `return []`
    here would make `just qc` green on a repo with no CI at all."""
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    assert "NO_UNFILTERED_CI" in _checks(check_workflows(tmp_path))


def test_real_repo_satisfies_the_invariant():
    """Guards the live repo: if the last unfiltered workflow gains a paths
    filter, this fails rather than silently reducing coverage."""
    assert "NO_UNFILTERED_CI" not in _checks(check_workflows(REPO_ROOT))


# --- conflict markers -------------------------------------------------------


def test_conflict_marker_flagged(tmp_path):
    root = _repo(tmp_path)
    (root / "f.py").write_text("a = 1\n<<<<<<< HEAD\nb = 2\n")
    _commit(root)
    findings = check_conflict_markers([root / "f.py"], root)
    assert [f["check"] for f in findings] == ["CONFLICT_MARKER"]
    assert findings[0]["file"].endswith(":2")


def test_setext_heading_is_not_a_conflict_marker():
    """`=======` under a line is a Markdown H1, which is why only <<< and >>>
    are matched. Matching `=` would false-positive on ordinary prose."""
    assert not CONFLICT_RE.match("=======")
    assert not CONFLICT_RE.match("=========")
    assert CONFLICT_RE.match("<<<<<<< HEAD")
    assert CONFLICT_RE.match(">>>>>>> branch")


# --- markdown links ---------------------------------------------------------


def test_broken_relative_link_flagged(tmp_path):
    root = _repo(tmp_path)
    md = root / "a.md"
    md.write_text("see [docs](docs/nope.md)\n")
    _commit(root)
    findings = check_markdown_links([md], root)
    assert [f["check"] for f in findings] == ["BROKEN_LINK"]


def test_resolving_link_and_anchor_and_url_are_clean(tmp_path):
    root = _repo(tmp_path)
    (root / "target.md").write_text("hi\n")
    md = root / "a.md"
    md.write_text(textwrap.dedent("""\
        [ok](target.md)
        [anchored](target.md#section)
        [external](https://example.com/missing)
        [internal anchor](#heading)
        [mail](mailto:someone@example.com)
    """))
    _commit(root)
    assert check_markdown_links([md], root) == []


def test_links_escaping_the_repo_are_skipped(tmp_path):
    """README points at sibling fleet checkouts (../CultureMech). Whether those
    resolve depends on what is cloned next door, so checking them makes the
    result machine-dependent — they passed locally and failed on the runner."""
    root = _repo(tmp_path)
    md = root / "README.md"
    md.write_text("[sibling](../CultureMech) and [deep](../../elsewhere/x.md)\n")
    _commit(root)
    assert check_markdown_links([md], root) == []


def test_case_only_mismatch_is_flagged_even_on_case_insensitive_fs(tmp_path):
    """`skill.md` vs `SKILL.md` resolves on macOS and not on Linux. A plain
    exists() therefore passes locally and fails in CI — which is how a stale
    lowercase link survived the SKILL.md rename in #190."""
    root = _repo(tmp_path)
    (root / "docs").mkdir()
    (root / "docs/SKILL.md").write_text("hi\n")
    md = root / "a.md"
    md.write_text("[wrong case](docs/skill.md)\n")
    _commit(root)
    findings = check_markdown_links([md], root)
    assert [f["check"] for f in findings] == ["BROKEN_LINK"]

    md.write_text("[right case](docs/SKILL.md)\n")
    assert check_markdown_links([md], root) == []


def test_within_handles_relative_candidates(tmp_path):
    """A relative candidate compared against an absolute root always raises
    ValueError, which would classify every in-repo link as external and make
    the link check silently vacuous."""
    from pr_sanity import _within

    root = _repo(tmp_path)
    assert _within(Path("docs/x.md"), Path("."))
    assert _within(root / "docs/x.md", root)
    assert not _within(Path("../outside/x.md"), Path("."))


def test_root_relative_link_resolves_from_repo_root(tmp_path):
    root = _repo(tmp_path)
    (root / "docs").mkdir()
    (root / "docs/target.md").write_text("hi\n")
    nested = root / "docs/a.md"
    nested.write_text("[up](/docs/target.md)\n")
    _commit(root)
    assert check_markdown_links([nested], root) == []


# --- end to end -------------------------------------------------------------


def test_sanity_aggregates_all_checks(tmp_path):
    root = _repo(tmp_path)
    (root / ".github/workflows/a.yaml").write_text(FILTERED_WF)  # trips invariant
    (root / "f.py").write_text("<<<<<<< HEAD\n")
    (root / "a.md").write_text("[x](missing.md)\n")
    _commit(root)
    assert _checks(sanity(root)) == {
        "NO_UNFILTERED_CI", "CONFLICT_MARKER", "BROKEN_LINK",
    }


def test_cli_exit_codes(tmp_path):
    root = _repo(tmp_path)
    (root / ".github/workflows/a.yaml").write_text(UNFILTERED_WF)
    _commit(root)
    script = str(REPO_ROOT / "scripts" / "pr_sanity.py")

    ok = subprocess.run([sys.executable, script, "--root", str(root)],
                        capture_output=True, text=True)
    assert ok.returncode == 0, ok.stderr

    (root / "bad.md").write_text("[x](nope.md)\n")
    _commit(root)
    bad = subprocess.run([sys.executable, script, "--root", str(root)],
                         capture_output=True, text=True)
    assert bad.returncode == 1
    assert "BROKEN_LINK" in bad.stderr
