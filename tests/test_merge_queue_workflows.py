"""Required checks must evaluate both PRs and native merge-group commits."""

import os
import shlex
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
REQUIRED_WORKFLOWS = {
    "canonical-example-taxonomy.yaml": ["canonical-example-taxonomy"],
    "curation-history.yaml": ["history"],
    "label-correspondence.yaml": ["label-correspondence / label-correspondence"],
    "pr-sanity.yaml": ["pr-sanity"],
    "pytest.yaml": ["pytest"],
    "qc.yaml": ["qc"],
    "validate-strict.yaml": ["validate-strict"],
    "vendored-sync.yaml": ["vendored-sync"],
}


@pytest.mark.parametrize("filename", REQUIRED_WORKFLOWS)
def test_required_workflow_reports_for_every_pr_and_merge_group(filename):
    document = yaml.safe_load((ROOT / ".github/workflows" / filename).read_text())
    events = document.get("on", document.get(True))
    assert "pull_request" in events
    assert not events["pull_request"], "workflow filters can leave a required PR check pending"
    assert events["merge_group"] == {"types": ["checks_requested"]}
    assert document["permissions"] == {"contents": "read"}
    concurrency = document["concurrency"]
    assert concurrency["cancel-in-progress"] == "${{ github.event_name == 'pull_request' }}"
    assert "github.run_id" in concurrency["group"]
    for job in document["jobs"].values():
        assert "if" not in job, "a required job must not skip the queue commit"
        for step in job.get("steps", []):
            if step.get("uses", "").startswith("actions/checkout@"):
                assert "ref" not in step.get("with", {}), (
                    "checkout must evaluate the event's combined commit"
                )


def test_required_job_contexts_remain_stable():
    for filename, expected in REQUIRED_WORKFLOWS.items():
        document = yaml.safe_load((ROOT / ".github/workflows" / filename).read_text())
        observed = []
        for job_id, job in document["jobs"].items():
            versions = job.get("strategy", {}).get("matrix", {}).get("python-version")
            if "uses" in job:
                observed.append(f"{job_id} / {job_id}")
            elif versions:
                for version in versions:
                    name = job.get("name")
                    observed.append(
                        name.replace("${{ matrix.python-version }}", version)
                        if name
                        else f"{job_id} ({version})"
                    )
            else:
                observed.append(job.get("name", job_id))
        assert sorted(observed) == sorted(expected)


def test_history_step_audits_earlier_changes_in_the_combined_group(tmp_path):
    workflow = yaml.safe_load((ROOT / ".github/workflows/curation-history.yaml").read_text())
    step = next(
        s
        for s in workflow["jobs"]["history"]["steps"]
        if s.get("name", "").startswith("Check for missing")
    )
    assert step["if"] == "github.event_name == 'pull_request' || github.event_name == 'merge_group'"
    assert step["env"]["HISTORY_BASE"] == (
        "${{ github.event_name == 'merge_group' && github.event.merge_group.base_sha "
        "|| github.event.pull_request.base.sha }}"
    )

    def git(*args):
        return subprocess.check_output(["git", *args], cwd=tmp_path, text=True).strip()

    git("init", "-q", "-b", "main")
    git("config", "user.name", "Test")
    git("config", "user.email", "test@example.com")
    (tmp_path / "README.md").write_text("base\n")
    git("add", ".")
    git("commit", "-qm", "base")
    base = git("rev-parse", "HEAD")
    trait = tmp_path / "data/traits/first.yaml"
    trait.parent.mkdir(parents=True)
    trait.write_text("identifier: first\n")
    git("add", ".")
    git("commit", "-qm", "first queued PR changes a trait without history")
    (tmp_path / "README.md").write_text("later queued PR changes documentation\n")
    git("add", ".")
    git("commit", "-qm", "later docs PR")

    # Execute the actual workflow shell. A HEAD^ diff would miss the first PR.
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    just = bin_dir / "just"
    just.write_text(
        '#!/bin/sh\n[ "$1" = audit-history-records ] || exit 99\nshift\nexec '
        + shlex.quote(sys.executable)
        + " "
        + shlex.quote(str(ROOT / "scripts/audit_history_records.py"))
        + ' "$@"\n'
    )
    just.chmod(0o755)
    env = {
        **os.environ,
        "PATH": str(bin_dir) + os.pathsep + os.environ["PATH"],
        "HISTORY_BASE": base,
        "GITHUB_STEP_SUMMARY": str(tmp_path / "summary"),
    }

    def run():
        return subprocess.run(
            ["bash", "-c", step["run"]],
            cwd=tmp_path,
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )

    missing = run()
    assert missing.returncode == 1
    assert "adds no history record" in missing.stdout
    history = tmp_path / "history/records/first.yaml"
    history.parent.mkdir(parents=True)
    history.write_text("history_version: 1\n")
    git("add", "history")
    git("commit", "-qm", "record the trait change")
    assert run().returncode == 0
    env["HISTORY_BASE"] = ""
    assert run().returncode != 0
