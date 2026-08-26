"""Contract tests for the manifest-driven vendored-sync workflow."""

from __future__ import annotations

import os
import stat
import subprocess
from pathlib import Path

import pytest
import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
WORKFLOW = REPO_ROOT / ".github/workflows/vendored-sync.yaml"


def _run_block() -> str:
    document = yaml.safe_load(WORKFLOW.read_text())
    steps = document["jobs"]["vendored-sync"]["steps"]
    return next(step["run"] for step in steps if "run" in step)


def _executable(path: Path, body: str) -> None:
    path.write_text(body)
    path.chmod(path.stat().st_mode | stat.S_IXUSR)


def _run_workflow(tmp_path: Path, statuses: list[int]) -> tuple[subprocess.CompletedProcess[str], int, int]:
    scripts = tmp_path / "scripts"
    scripts.mkdir()
    sequence = tmp_path / "statuses"
    sequence.write_text("\n".join(str(status) for status in statuses) + "\n")
    calls = tmp_path / "calls"
    sleeps = tmp_path / "sleeps"
    _executable(
        scripts / "check_vendored_sync.sh",
        """#!/usr/bin/env bash
set -eu
count=0
if [ -f "$CALL_LOG" ]; then count=$(cat "$CALL_LOG"); fi
count=$((count + 1))
echo "$count" > "$CALL_LOG"
status=$(sed -n "${count}p" "$STATUS_FILE")
exit "${status:-1}"
""",
    )
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    _executable(
        bin_dir / "sleep",
        """#!/usr/bin/env bash
set -eu
count=0
if [ -f "$SLEEP_LOG" ]; then count=$(cat "$SLEEP_LOG"); fi
echo $((count + 1)) > "$SLEEP_LOG"
""",
    )
    env = {
        **os.environ,
        "PATH": f"{bin_dir}:{os.environ['PATH']}",
        "CALL_LOG": str(calls),
        "SLEEP_LOG": str(sleeps),
        "STATUS_FILE": str(sequence),
    }
    result = subprocess.run(
        ["bash", "-c", _run_block()],
        cwd=tmp_path,
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )
    return result, int(calls.read_text()), int(sleeps.read_text()) if sleeps.exists() else 0


def test_workflow_names_claw_as_the_only_authority() -> None:
    text = WORKFLOW.read_text()
    workflow = yaml.safe_load(text)
    triggers = workflow.get("on", workflow.get(True))
    concurrency = workflow["concurrency"]

    assert "CultureBotAI/culturebotai-claw" in text
    assert "CultureBotAI/CultureMech" not in text
    assert "canonical hub" not in text.lower()
    assert all("paths" not in (config or {}) for config in triggers.values())
    assert workflow["jobs"]["vendored-sync"]["timeout-minutes"] == 5
    assert "github.run_id" in concurrency["group"]
    assert concurrency["cancel-in-progress"] == "${{ github.event_name == 'pull_request' }}"


@pytest.mark.parametrize(
    ("statuses", "returncode", "calls", "sleeps"),
    [
        ([0], 0, 1, 0),
        ([1, 0], 0, 2, 1),
        ([1, 1, 1], 1, 3, 2),
        ([2], 2, 1, 0),
        ([99], 99, 1, 0),
    ],
)
def test_workflow_retries_only_exit_one(
    tmp_path: Path,
    statuses: list[int],
    returncode: int,
    calls: int,
    sleeps: int,
) -> None:
    result, observed_calls, observed_sleeps = _run_workflow(tmp_path, statuses)
    assert result.returncode == returncode, result.stderr
    assert observed_calls == calls
    assert observed_sleeps == sleeps
