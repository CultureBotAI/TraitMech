"""Keep declared Python support aligned with the pytest CI matrix."""

import re
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
SUPPORTED = {"3.10", "3.11", "3.12", "3.13"}


def test_declared_python_versions_are_exercised_in_ci():
    pyproject = (REPO_ROOT / "pyproject.toml").read_text()
    declared = set(re.findall(
        r'"Programming Language :: Python :: (3\.\d+)"', pyproject
    ))
    assert 'requires-python = ">=3.10,<3.14"' in pyproject
    assert declared == SUPPORTED

    workflow = yaml.safe_load(
        (REPO_ROOT / ".github/workflows/pytest.yaml").read_text()
    )
    matrix = workflow["jobs"]["pytest"]["strategy"]["matrix"]
    assert set(matrix["python-version"]) == declared
    assert workflow["jobs"]["pytest"]["strategy"]["fail-fast"] is False
