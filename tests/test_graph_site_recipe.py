"""Actual maintained recipe order/argv, with no model, graph or corpus operation."""

from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def recorder(tmp_path):
    if shutil.which("just") is None:
        pytest.skip("the just developer tool is required")
    tools = tmp_path / "tools"
    tools.mkdir()
    receipt = tmp_path / "argv.jsonl"
    uv = tools / "uv"
    uv.write_text(
        "#!/usr/bin/env python3\n"
        "import json, os, sys\n"
        "with open(os.environ['TRAIT_GRAPH_RECIPE_LOG'], 'a') as out:\n"
        "    out.write(json.dumps(sys.argv[1:]) + '\\n')\n"
        "raise SystemExit(17 if os.environ.get('TRAIT_GRAPH_FAIL_METHOD') in sys.argv[1:] else 0)\n"
    )
    uv.chmod(0o755)
    environment = {
        **os.environ,
        "PATH": str(tools) + os.pathsep + os.environ["PATH"],
        "TRAIT_GRAPH_RECIPE_LOG": str(receipt),
    }
    marker = tmp_path / "SHELL_MUST_NOT_RUN"
    source = str(tmp_path / f"selected source; $(touch {marker}).tsv.gz")
    aliases = str(tmp_path / f"aliases `touch {marker}`.tsv")

    def run(recipe="gen-site", fail=None):
        receipt.unlink(missing_ok=True)
        env = environment | ({"TRAIT_GRAPH_FAIL_METHOD": fail} if fail else {})
        result = subprocess.run(
            ["just", recipe, source, aliases], cwd=ROOT, env=env, capture_output=True, text=True
        )
        calls = [json.loads(line) for line in receipt.read_text().splitlines()]
        assert not marker.exists(), "recipe evaluated literal argument text as shell code"
        return result, calls, source, aliases

    return run


@pytest.mark.parametrize("recipe", ["gen-site", "build-embeddings"])
def test_both_explicit_sources_are_built_in_order_before_rendering(recorder, recipe):
    result, calls, source, aliases = recorder(recipe)
    assert result.returncode == 0, result.stderr
    expected = [
        [
            "run",
            "--locked",
            "python",
            "scripts/build_embedding_index.py",
            "--src",
            source,
            "--kgm-aliases",
            aliases,
            "--method",
            method,
            "--umap-out",
            output,
        ]
        for method, output in (
            ("pacmap", "data/embeddings/trait_umap.json"),
            ("sfdp", "data/embeddings/trait_graph.json"),
        )
    ]
    if recipe == "gen-site":
        expected.append(["run", "python", "scripts/render_trait_pages.py"])
    assert calls == expected  # also excludes implicit seeding or semantic inference


@pytest.mark.parametrize("method,count", [("pacmap", 1), ("sfdp", 2)])
def test_failed_graph_refresh_never_reaches_page_writer(recorder, method, count):
    result, calls, _, _ = recorder(fail=method)
    assert result.returncode != 0
    assert len(calls) == count
    assert all("scripts/build_embedding_index.py" in call for call in calls)
