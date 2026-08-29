"""A PR-triggered job that installs dependencies must be triggered by them.

Sixth instance of one defect: a `paths:` filter narrower than what the job
actually reads. #184 (vendored-sync fired for 1 of 6 protected files), #200
(docs-only PRs got no checks), #250 (`research/**` missing), #252 (`conf/**`
missing, so weakening a ratchet baseline did not re-run qc), #554
(`data/traits/**` missing from pytest, so 13 records drifted off the
round-trip invariant unnoticed), and now #566/#567 — no workflow listed
`uv.lock` at all, and the blocking OAK gate did not list `pyproject.toml`
either, so the PR that changed which host OAK downloads from could not
trigger the one job that would have proved it (#565 had to be dispatched by
hand).

Every one was caught by human review, never by CI. `audit-qc-paths` closed
that for `qc.yaml` alone by deriving the read-set from the recipe chain. This
closes the dependency half for every workflow: if a job runs `uv sync`, the
resolved environment is one of its inputs, so `pyproject.toml` and `uv.lock`
belong in the filter that decides whether it runs.

Scope is deliberately narrow — only PR-triggered jobs that have a filter AND
install dependencies. A job with no `paths:` already runs on everything, and a
job that never touches uv has no dependency input to miss.
"""

from __future__ import annotations

import pathlib

import yaml

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
WORKFLOWS = REPO_ROOT / ".github" / "workflows"

DEPENDENCY_INPUTS = ("pyproject.toml", "uv.lock")
INSTALLER_MARKER = "astral-sh/setup-uv"


def _pull_request_paths(document: dict) -> list[str] | None:
    """Return the PR trigger's paths list, or None when it does not filter.

    `on:` parses to the boolean True under YAML 1.1, so both spellings are
    checked. A bare `pull_request:` key parses to None and means "every PR",
    which is not a filter and needs nothing added.
    """
    on = document.get(True) or document.get("on") or {}
    if not isinstance(on, dict) or "pull_request" not in on:
        return None
    trigger = on["pull_request"]
    if not isinstance(trigger, dict):
        return None
    paths = trigger.get("paths")
    return paths if paths else None


def test_filtered_pr_jobs_that_install_dependencies_are_triggered_by_them():
    offenders: list[str] = []
    checked = 0
    for path in sorted(WORKFLOWS.glob("*.y*ml")):
        text = path.read_text(encoding="utf-8")
        if INSTALLER_MARKER not in text:
            continue
        paths = _pull_request_paths(yaml.safe_load(text))
        if paths is None:
            continue
        checked += 1
        missing = [dep for dep in DEPENDENCY_INPUTS
                   if not any(dep in entry for entry in paths)]
        if missing:
            offenders.append(f"{path.name} omits {', '.join(missing)}")

    assert checked, (
        "no filtered, dependency-installing PR workflow was found — this test "
        "would pass vacuously, so its discovery is broken rather than the "
        "workflows being clean"
    )
    assert not offenders, (
        "these workflows install dependencies with uv but are not triggered by "
        "a dependency change, so a PR editing only pyproject.toml or uv.lock "
        f"cannot run them (#566/#567): {'; '.join(offenders)}"
    )


def test_push_and_pull_request_filters_agree_on_dependency_inputs():
    """A gate that guards `main` must guard PRs identically.

    Several workflows share one anchor between the two triggers, which keeps
    them aligned for free. The ones that repeat the list by hand can drift, and
    a push-only omission means a dependency change merged to `main` runs a
    thinner set of checks than the PR did.
    """
    mismatched: list[str] = []
    for path in sorted(WORKFLOWS.glob("*.y*ml")):
        text = path.read_text(encoding="utf-8")
        if INSTALLER_MARKER not in text:
            continue
        document = yaml.safe_load(text)
        pr_paths = _pull_request_paths(document)
        if pr_paths is None:
            continue
        on = document.get(True) or document.get("on") or {}
        push = on.get("push")
        if not isinstance(push, dict) or not push.get("paths"):
            continue
        for dep in DEPENDENCY_INPUTS:
            in_pr = any(dep in entry for entry in pr_paths)
            in_push = any(dep in entry for entry in push["paths"])
            if in_pr != in_push:
                mismatched.append(f"{path.name}: {dep} in pull_request={in_pr}, push={in_push}")

    assert not mismatched, (
        "pull_request and push filters disagree about dependency inputs: "
        + "; ".join(mismatched)
    )
