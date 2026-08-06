"""Unit tests for the no-CI-at-all detector (#345).

The rule has to hold regardless of WHY the runs went missing, since the
mechanism behind #344 is still unidentified. What it must never do is pass a PR
whose only runs were dispatched by hand -- that is what someone does *after*
noticing the problem, so counting it would make the check green on exactly the
PRs it exists to find.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from audit_pr_checks_present import offenders  # noqa: E402


def _pr(n, events):
    return {"number": n, "title": f"pr {n}", "events": events}


def test_a_pr_with_pull_request_runs_is_fine():
    assert offenders([_pr(1, ["pull_request", "pull_request"])]) == []


def test_a_pr_with_no_runs_at_all_is_flagged():
    """The #344 shape: mergeStateStatus CLEAN, nothing evaluated."""
    assert [p["number"] for p in offenders([_pr(344, [])])] == [344]


def test_hand_dispatched_runs_do_not_count_as_evidence():
    """The trap: dispatching by hand is the RESPONSE, not the verification."""
    assert [p["number"] for p in offenders([_pr(344, ["workflow_dispatch"] * 4)])] == [344]


def test_a_dispatched_run_alongside_a_real_one_is_fine():
    assert offenders([_pr(1, ["workflow_dispatch", "pull_request"])]) == []


def test_scheduled_runs_do_not_count_either():
    assert [p["number"] for p in offenders([_pr(2, ["schedule"])])] == [2]


def test_only_the_offenders_are_returned():
    got = offenders([_pr(1, ["pull_request"]), _pr(2, []), _pr(3, ["workflow_dispatch"])])
    assert [p["number"] for p in got] == [2, 3]
