"""Keep package compatibility separate from the fleet's single CI runtime."""

import re
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
COMPATIBLE = {"3.10", "3.11", "3.12", "3.13"}


def test_package_compatibility_is_preserved():
    pyproject = (REPO_ROOT / "pyproject.toml").read_text()
    declared = set(re.findall(
        r'"Programming Language :: Python :: (3\.\d+)"', pyproject
    ))
    assert 'requires-python = ">=3.10,<3.14"' in pyproject
    assert declared == COMPATIBLE


def test_ci_selects_the_single_fleet_runtime():
    runtime = (REPO_ROOT / ".python-version").read_text().strip()
    assert runtime == "3.13"
    assert runtime in COMPATIBLE
    workflow = yaml.safe_load(
        (REPO_ROOT / ".github/workflows/pytest.yaml").read_text()
    )
    job = workflow["jobs"]["pytest"]
    assert not job.get("strategy", {}).get("matrix")
    setup = next(s for s in job["steps"] if "setup-uv@" in s.get("uses", ""))
    assert setup["with"]["python-version"] == runtime
    assert any("uv run pytest tests/" in s.get("run", "") for s in job["steps"])
