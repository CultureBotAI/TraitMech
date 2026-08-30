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
closes the dependency half for every workflow: if a job resolves the project
environment, `pyproject.toml` and `uv.lock` are inputs and belong in the filter
that decides whether it runs.

Scope is deliberately narrow — only PR-triggered jobs that have a filter AND
install project dependencies. A job with no `paths:` already runs on everything,
and a job that uses only a standalone tool without resolving this project has
no dependency input to miss.
"""

from __future__ import annotations

import pathlib
import re
from fnmatch import fnmatchcase

import yaml

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
WORKFLOWS = REPO_ROOT / ".github" / "workflows"

DEPENDENCY_INPUTS = ("pyproject.toml", "uv.lock")
EXPECTED_FILTERED_DEPENDENCY_WORKFLOWS = frozenset(
    {
        "canonical-example-taxonomy.yaml",
        "curation-history.yaml",
        "label-correspondence.yaml",
        "pytest.yaml",
        "qc.yaml",
        "validate-strict.yaml",
    }
)
EXPECTED_FILTERED_PUSH_WORKFLOWS = EXPECTED_FILTERED_DEPENDENCY_WORKFLOWS - {"qc.yaml"}
PROJECT_INSTALL_COMMANDS = (
    re.compile(r"(?:^|[\s;&|])uv\s+sync(?:$|[\s;&|])"),
    re.compile(r"(?:^|[\s;&|])uv\s+run(?:$|[\s;&|])"),
    re.compile(r"(?:^|[\s;&|])(?:python\s+-m\s+)?pip\s+install\b.*(?:^|\s)\."),
)


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


def _workflow_installs_project_dependencies(document: dict) -> bool:
    """Return whether parsed job steps resolve this repository's environment.

    Looking at parsed ``run`` values avoids counting comments and is independent
    of the action used to install uv or Python. ``uv run --no-project`` is the
    documented escape hatch for standalone tools: it deliberately does not read
    this repository's lock file.
    """
    jobs = document.get("jobs") or {}
    for job in jobs.values():
        if not isinstance(job, dict):
            continue
        for step in job.get("steps") or []:
            if not isinstance(step, dict) or not isinstance(step.get("run"), str):
                continue
            for line in step["run"].splitlines():
                if "--no-project" in line:
                    continue
                if any(pattern.search(line) for pattern in PROJECT_INSTALL_COMMANDS):
                    return True
    return False


def _filtered_dependency_workflows() -> dict[str, tuple[dict, list[str]]]:
    workflows: dict[str, tuple[dict, list[str]]] = {}
    for path in sorted(WORKFLOWS.glob("*.y*ml")):
        document = yaml.safe_load(path.read_text(encoding="utf-8"))
        paths = _pull_request_paths(document)
        if paths is not None and _workflow_installs_project_dependencies(document):
            workflows[path.name] = (document, paths)
    return workflows


def _pattern_matches_root_file(pattern: str, filename: str) -> bool:
    """Match the root files covered here using GitHub path-pattern shapes."""
    if fnmatchcase(filename, pattern):
        return True
    # GitHub's recursive prefix can match zero directories; fnmatch cannot.
    return pattern.startswith("**/") and fnmatchcase(filename, pattern[3:])


def _path_is_included(filename: str, patterns: list[str]) -> bool:
    """Evaluate ordered positive/negative GitHub path patterns for one file."""
    included = False
    for entry in patterns:
        negative = entry.startswith("!")
        pattern = entry[1:] if negative else entry
        if _pattern_matches_root_file(pattern, filename):
            included = not negative
    return included


def test_filtered_pr_jobs_that_install_dependencies_are_triggered_by_them():
    offenders: list[str] = []
    workflows = _filtered_dependency_workflows()
    assert workflows.keys() == EXPECTED_FILTERED_DEPENDENCY_WORKFLOWS, (
        "the set of filtered PR workflows that install project dependencies "
        "changed; acknowledge the migration/addition here so coverage cannot "
        "silently shrink (#578): "
        f"expected {sorted(EXPECTED_FILTERED_DEPENDENCY_WORKFLOWS)}, "
        f"found {sorted(workflows)}"
    )
    for name, (_, paths) in workflows.items():
        missing = [dep for dep in DEPENDENCY_INPUTS if not _path_is_included(dep, paths)]
        if missing:
            offenders.append(f"{name} omits {', '.join(missing)}")

    assert not offenders, (
        "these workflows install project dependencies but are not triggered by "
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
    checked: set[str] = set()
    for name, (document, pr_paths) in _filtered_dependency_workflows().items():
        on = document.get(True) or document.get("on") or {}
        push = on.get("push")
        if not isinstance(push, dict) or not push.get("paths"):
            continue
        checked.add(name)
        for dep in DEPENDENCY_INPUTS:
            in_pr = _path_is_included(dep, pr_paths)
            in_push = _path_is_included(dep, push["paths"])
            if in_pr != in_push:
                mismatched.append(f"{name}: {dep} in pull_request={in_pr}, push={in_push}")

    assert checked == EXPECTED_FILTERED_PUSH_WORKFLOWS, (
        "the set of dependency-installing workflows with filtered push and PR "
        "triggers changed; acknowledge it so this comparison cannot pass "
        f"vacuously (#580): expected {sorted(EXPECTED_FILTERED_PUSH_WORKFLOWS)}, "
        f"found {sorted(checked)}"
    )

    assert not mismatched, (
        "pull_request and push filters disagree about dependency inputs: " + "; ".join(mismatched)
    )


def test_dependency_path_membership_respects_exact_paths_negation_and_globs():
    assert _path_is_included("pyproject.toml", ["pyproject.toml"])
    assert not _path_is_included("pyproject.toml", ["vendor/thirdparty/pyproject.toml"])
    assert not _path_is_included("pyproject.toml", ["!pyproject.toml"])
    assert _path_is_included("pyproject.toml", ["**"])
    assert not _path_is_included("pyproject.toml", ["**", "!pyproject.toml"])
    assert _path_is_included("pyproject.toml", ["**", "!pyproject.toml", "pyproject.toml"])


def test_dependency_install_detection_uses_commands_not_action_text():
    comment_only = yaml.safe_load(
        """
        # astral-sh/setup-uv and uv sync in comments are not dependency installs.
        jobs:
          lint:
            steps:
              - run: uv run --no-project --with ruff ruff check .
        """
    )
    pip_install = yaml.safe_load(
        """
        jobs:
          test:
            steps:
              - run: python -m pip install -e .[dev]
        """
    )
    assert not _workflow_installs_project_dependencies(comment_only)
    assert _workflow_installs_project_dependencies(pip_install)
