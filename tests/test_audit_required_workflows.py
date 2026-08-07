"""Unit tests for scripts/audit_required_workflows.py (#348).

Locks in the three properties that make this check meaningful:

- the required set is DERIVED from the workflow files, including the `on:`-is-
  parsed-as-True trap that would otherwise make it find nothing and pass;
- a `paths:` filter that legitimately excludes the PR is not a missing run;
- a PR that cannot be predicted is SKIPPED AND NAMED, never silently dropped.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from audit_required_workflows import (  # noqa: E402
    MIN_AGE_MINUTES,
    PATHS_FILTER_FILE_LIMIT,
    _glob_to_regex,
    offenders,
    partition,
    pr_workflows,
    should_run,
)

FILTERED = """\
name: qc
on:
  pull_request:
    paths:
      - 'data/traits/**'
      - 'scripts/**.py'
jobs:
  qc:
    runs-on: ubuntu-latest
    steps: [{run: just qc}]
"""

UNFILTERED = """\
name: pr-sanity
on:
  pull_request:
jobs:
  s:
    runs-on: ubuntu-latest
    steps: [{run: 'true'}]
"""

PUSH_ONLY = """\
name: deploy
on:
  push:
    branches: [main]
jobs:
  d:
    runs-on: ubuntu-latest
    steps: [{run: 'true'}]
"""


def _wf_dir(tmp_path: Path, **files: str) -> Path:
    d = tmp_path / "workflows"
    d.mkdir(exist_ok=True)
    for name, body in files.items():
        (d / name.replace("__", ".")).write_text(body)
    return d


# --- deriving the required set ----------------------------------------------


def test_only_pull_request_workflows_are_required(tmp_path):
    d = _wf_dir(tmp_path, qc__yaml=FILTERED, sanity__yaml=UNFILTERED,
                deploy__yaml=PUSH_ONLY)
    assert {w["file"] for w in pr_workflows(d)} == {
        ".github/workflows/qc.yaml", ".github/workflows/sanity.yaml"}


def test_the_on_key_parsed_as_a_boolean_is_still_found(tmp_path):
    """PyYAML 1.1 resolves the unquoted key `on:` to the BOOLEAN True.

    Reading only doc["on"] would find zero required workflows in this repo and
    exit 0 -- a check that passes because it looked at nothing, which is the
    exact shape of vacuous green it exists to catch. Pinned because the bug is
    invisible: the audit stays green while doing nothing.
    """
    d = _wf_dir(tmp_path, qc__yaml=FILTERED)
    import yaml
    parsed = yaml.safe_load((d / "qc.yaml").read_text())
    assert "on" not in parsed and True in parsed  # the trap itself
    assert len(pr_workflows(d)) == 1


def test_the_required_set_grows_with_a_new_workflow(tmp_path):
    """Derived, not declared (#252): adding a workflow needs no second edit."""
    d = _wf_dir(tmp_path, qc__yaml=FILTERED)
    before = len(pr_workflows(d))
    (d / "extra.yaml").write_text(UNFILTERED)
    assert len(pr_workflows(d)) == before + 1


def test_unsupported_filter_syntax_is_declined_not_guessed(tmp_path):
    d = _wf_dir(tmp_path, weird__yaml=UNFILTERED.replace(
        "  pull_request:\n", "  pull_request:\n    paths: ['!docs/**']\n"))
    wf = pr_workflows(d)[0]
    assert wf["unsupported"] == ["!docs/**"]
    # ...and a workflow it cannot predict never produces an offender.
    assert offenders([{"number": 1, "title": "t", "changed_files": ["a.py"],
                       "ran": [], "age_minutes": 999}], [wf]) == []


# --- path-filter semantics ---------------------------------------------------


@pytest.mark.parametrize("pattern,path,expected", [
    ("data/traits/**", "data/traits/a/b.yaml", True),
    # Anchored at BOTH ends. Matching only the tail would let a vendored copy
    # satisfy the filter for the real directory.
    ("data/traits/**", "vendor/data/traits/x.yaml", False),
    # A single star does NOT cross a slash, which is where fnmatch differs and
    # would over-predict.
    ("scripts/*", "scripts/a/b.py", False),
    ("scripts/**", "scripts/a/b.py", True),
    ("scripts/**.py", "scripts/a/b.py", True),
    ("scripts/**.py", "scripts/a/b.md", False),
    ("justfile", "justfile", True),
    ("justfile", "justfile.bak", False),
])
def test_glob_semantics(pattern, path, expected):
    assert bool(_glob_to_regex(pattern).fullmatch(path)) is expected


def test_a_filtered_out_workflow_is_not_expected(tmp_path):
    wf = pr_workflows(_wf_dir(tmp_path, qc__yaml=FILTERED))[0]
    assert should_run(wf, ["docs/README.md"]) is False
    assert should_run(wf, ["data/traits/x.yaml"]) is True
    # One match out of many changed files is enough, as GitHub does it.
    assert should_run(wf, ["docs/README.md", "scripts/a.py"]) is True


def test_an_unfiltered_workflow_is_always_expected(tmp_path):
    wf = pr_workflows(_wf_dir(tmp_path, s__yaml=UNFILTERED))[0]
    assert should_run(wf, ["anything/at/all.txt"]) is True
    assert should_run(wf, []) is True


def test_paths_ignore_excludes_only_when_every_file_is_ignored(tmp_path):
    wf = pr_workflows(_wf_dir(tmp_path, s__yaml=UNFILTERED.replace(
        "  pull_request:\n", "  pull_request:\n    paths-ignore: ['docs/**']\n")))[0]
    assert should_run(wf, ["docs/a.md"]) is False
    assert should_run(wf, ["docs/a.md", "src/x.py"]) is True


# --- the rule ----------------------------------------------------------------


def _prs(**over):
    base = {"number": 7, "title": "t", "changed_files": ["data/traits/x.yaml"],
            "ran": [], "age_minutes": 999}
    return [{**base, **over}]


def test_a_missing_expected_run_is_an_offender(tmp_path):
    wfs = pr_workflows(_wf_dir(tmp_path, qc__yaml=FILTERED))
    bad = offenders(_prs(), wfs)
    assert [pr["missing"] for pr in bad] == [[".github/workflows/qc.yaml"]]


def test_partial_silence_is_caught_where_total_silence_check_passes(tmp_path):
    """The whole point of #348.

    The reviewer bot fires on every PR, so audit-pr-checks-present sees an
    event and passes. qc is mute. This must still report.
    """
    wfs = pr_workflows(_wf_dir(tmp_path, qc__yaml=FILTERED, review__yaml=UNFILTERED))
    bad = offenders(_prs(ran=[".github/workflows/review.yaml"]), wfs)
    assert [pr["missing"] for pr in bad] == [[".github/workflows/qc.yaml"]]


def test_a_fully_checked_pr_is_clean(tmp_path):
    wfs = pr_workflows(_wf_dir(tmp_path, qc__yaml=FILTERED, review__yaml=UNFILTERED))
    assert offenders(_prs(ran=[".github/workflows/qc.yaml",
                               ".github/workflows/review.yaml"]), wfs) == []


def test_a_workflow_the_pr_does_not_touch_is_not_missing(tmp_path):
    wfs = pr_workflows(_wf_dir(tmp_path, qc__yaml=FILTERED))
    assert offenders(_prs(changed_files=["docs/README.md"]), wfs) == []


def test_young_prs_are_skipped_and_named(tmp_path):
    wfs = pr_workflows(_wf_dir(tmp_path, qc__yaml=FILTERED))
    bad, skipped = partition(_prs(age_minutes=MIN_AGE_MINUTES - 1), wfs)
    assert bad == []
    assert [pr["number"] for pr in skipped] == [7]
    assert "min ago" in skipped[0]["reason"]


def test_evidence_beats_youth(tmp_path):
    """A young PR that already has its runs is CLEAN, not 'skipped'.

    Counting it as skipped would understate the coverage the run achieved.
    """
    wfs = pr_workflows(_wf_dir(tmp_path, qc__yaml=FILTERED))
    bad, skipped = partition(_prs(age_minutes=0, ran=[".github/workflows/qc.yaml"]),
                             wfs)
    assert bad == [] and skipped == []


def test_huge_prs_are_skipped_and_named(tmp_path):
    """Past GitHub's path-filter evaluation limit the prediction is unsound, so
    reporting would manufacture offenders. Named rather than dropped: a PR that
    vanished from both counts would make the output read as full coverage."""
    wfs = pr_workflows(_wf_dir(tmp_path, qc__yaml=FILTERED))
    many = [f"data/traits/f{i}.yaml" for i in range(PATHS_FILTER_FILE_LIMIT + 1)]
    bad, skipped = partition(_prs(changed_files=many), wfs)
    assert bad == []
    assert "changed files" in skipped[0]["reason"]


def test_no_pr_is_lost_between_the_two_buckets(tmp_path):
    """Every reported PR lands in exactly one of (clean, offender, skipped)."""
    wfs = pr_workflows(_wf_dir(tmp_path, qc__yaml=FILTERED))
    prs = (_prs(number=1)
           + _prs(number=2, age_minutes=0)
           + _prs(number=3, ran=[".github/workflows/qc.yaml"])
           + _prs(number=4, changed_files=["docs/x.md"]))
    bad, skipped = partition(prs, wfs)
    assert {pr["number"] for pr in bad} == {1}
    assert {pr["number"] for pr in skipped} == {2}
    # 3 and 4 are clean, so 1+2+3+4 are all accounted for.
    assert len(bad) + len(skipped) + 2 == len(prs)


def test_the_repos_own_workflows_parse(tmp_path):
    """A canary against the real directory: if this repo's workflows stop being
    readable the audit would find nothing and pass."""
    wfs = pr_workflows(REPO_ROOT / ".github" / "workflows")
    assert len(wfs) >= 5
    assert any(w["file"].endswith("qc.yaml") for w in wfs)
    assert all(not w["unsupported"] for w in wfs)
