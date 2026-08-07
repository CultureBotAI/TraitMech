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

from audit_pr_checks_present import MIN_AGE_MINUTES, offenders  # noqa: E402


def _pr(n, events, age_minutes=MIN_AGE_MINUTES + 1):
    return {"number": n, "title": f"pr {n}", "events": events,
            "age_minutes": age_minutes}


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


def test_a_push_event_run_alone_is_not_evidence():
    """#346 review: evidence is an allowlist, so it fails closed.

    Every workflow here is `push: branches: [main]`, so a push run against a PR
    head would not mean the PR was evaluated. Under the old denylist it counted.
    """
    assert [p["number"] for p in offenders([_pr(5, ["push"])])] == [5]


def test_an_unknown_future_trigger_is_not_evidence():
    """The reason for an allowlist: a trigger added later must not silently
    start counting without a test failing."""
    assert [p["number"] for p in offenders([_pr(6, ["merge_group"])])] == [6]


def test_pull_request_target_counts():
    assert offenders([_pr(7, ["pull_request_target"])]) == []


def test_a_freshly_opened_pr_is_skipped():
    """A PR opened seconds before the run has no checks yet through no fault of
    its own; reporting it would be a false alarm on every merge (#346 review)."""
    assert offenders([_pr(8, [], age_minutes=1)]) == []


def test_an_old_pr_with_no_runs_is_still_flagged():
    assert [p["number"] for p in offenders([_pr(9, [], age_minutes=600)])] == [9]


def test_age_is_optional():
    """offenders() stays usable without age data, e.g. from --json fixtures."""
    assert [p["number"] for p in offenders([{"number": 10, "title": "t", "events": []}])] == [10]


def test_skipped_prs_are_returned_not_dropped():
    """#346 review: a PR excluded for youth must stay visible.

    Dropping it made `open PRs: N` read as full coverage of N when one was never
    checked -- the silent-omission shape this tool exists to catch, one level
    down.
    """
    from audit_pr_checks_present import partition

    bad, young = partition([_pr(1, []), _pr(2, [], age_minutes=1)])
    assert [p["number"] for p in bad] == [1]
    assert [p["number"] for p in young] == [2]


def test_a_long_open_pr_with_a_freshly_pushed_head_is_skipped():
    """The age gate must measure the HEAD COMMIT, not the PR's open date.

    collect() supplies age from the head commit for exactly this case: a PR
    opened last week and pushed seconds ago has a brand-new SHA with no runs yet.
    Push is far more frequent than open, so createdAt covered the rarer case.
    """
    assert offenders([_pr(3, [], age_minutes=0.5)]) == []


# --- collect(): the seam that has bitten twice (#346 review) -----------------
#
# Both real defects in this file were in collect(), not in the rule: json.loads
# on a bare scalar, then a documented createdAt fallback that could not fire.
# The separation that makes the rule testable left the fetching uncovered, and
# only a live run found either. These stub the gh boundary instead.

import audit_pr_checks_present as mod  # noqa: E402


def _fake_gh(monkeypatch, *, runs_total=0, commit_date="", commit_fails=False):
    monkeypatch.setattr(mod, "_gh_json", lambda args: (
        [{"number": 1, "title": "t", "headRefOid": "abc",
          "createdAt": "2020-01-01T00:00:00Z"}]
        if args[0] == "pr" else runs_total))
    monkeypatch.setattr(
        mod, "_gh_text_opt",
        lambda args: None if commit_fails else (commit_date or None))


def test_collect_uses_the_head_commit_date_when_available(monkeypatch):
    _fake_gh(monkeypatch, commit_date="2020-06-01T00:00:00Z")
    (pr,) = mod.collect("o/r")
    assert pr["events"] == []
    # Measured from the 2020-06 commit, not the 2020-01 PR open date.
    assert pr["age_minutes"] > 0


def test_collect_falls_back_to_created_at_when_the_commit_lookup_fails(monkeypatch):
    """The 🟡: this used to SystemExit(2) and discard the whole report."""
    _fake_gh(monkeypatch, commit_fails=True)
    (pr,) = mod.collect("o/r")
    assert pr["age_minutes"] is not None and pr["age_minutes"] > 0


def test_collect_survives_an_unparseable_timestamp(monkeypatch):
    """`gh api -q` prints the literal "null" for a missing field."""
    _fake_gh(monkeypatch, commit_date="null")
    (pr,) = mod.collect("o/r")
    # "null" is filtered by _gh_text_opt, so createdAt is used; either way the
    # run must not raise.
    assert pr["number"] == 1


def test_collect_short_circuits_once_evidence_is_found(monkeypatch):
    _fake_gh(monkeypatch, runs_total=3)
    (pr,) = mod.collect("o/r")
    assert pr["events"] and pr["age_minutes"] is None


def test_a_young_pr_that_already_has_runs_is_not_reported_as_skipped():
    """Evidence before youth: it is fine, not skipped (#346 review)."""
    bad, young = mod.partition([_pr(1, ["pull_request"], age_minutes=1)])
    assert bad == [] and young == []
