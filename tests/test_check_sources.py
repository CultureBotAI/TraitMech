"""Guard the source catalogue's contract, not just today's contents.

`download.yaml` is where a source's licence and provenance live. The risk is
not that today's file is wrong — `just sources-check` proves it is not — but
that the checker quietly stops enforcing something, which is invisible while
the file happens to be clean.

Each test below mutates a valid catalogue and asserts the checker rejects it.
A guard nobody has tried to defeat is decoration.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CHECKER = REPO_ROOT / "scripts" / "check_sources.py"
MANIFEST = REPO_ROOT / "download.yaml"

VALID = [
    {
        "url": "https://example.org/thing",
        "name": "A source",
        "source": "a_source",
        "license": "CC0",
        "status": "candidate",
    }
]


def _run(blocks: list[dict], tmp_path: Path) -> subprocess.CompletedProcess[str]:
    """Run the checker against a manifest built from ``blocks``.

    The checker resolves download.yaml from its own location, so the tree is
    mirrored into tmp_path rather than the real manifest being touched.
    """
    scripts = tmp_path / "scripts"
    # exist_ok: callers loop over several mutations against one tmp_path.
    scripts.mkdir(exist_ok=True)
    (scripts / "check_sources.py").write_text(
        CHECKER.read_text(encoding="utf-8"), encoding="utf-8"
    )
    (tmp_path / "download.yaml").write_text(yaml.safe_dump(blocks), encoding="utf-8")
    return subprocess.run(
        [sys.executable, str(scripts / "check_sources.py")],
        capture_output=True, text=True,
    )


def test_a_valid_catalogue_passes(tmp_path):
    result = _run(VALID, tmp_path)
    assert result.returncode == 0, result.stdout + result.stderr


def test_the_real_catalogue_passes():
    """The committed download.yaml must satisfy its own gate."""
    result = subprocess.run(
        [sys.executable, str(CHECKER)], capture_output=True, text=True
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert MANIFEST.exists()


def test_a_missing_licence_is_an_error(tmp_path):
    """The field the catalogue exists to carry cannot be optional.

    This is the check the sibling repo promises in its docstring and does not
    implement, which is why it is asserted here rather than assumed.
    """
    blocks = [dict(VALID[0])]
    del blocks[0]["license"]
    result = _run(blocks, tmp_path)
    assert result.returncode == 1
    assert "missing required field: license" in result.stdout


def test_each_required_field_is_enforced(tmp_path):
    for field in ("url", "name", "source", "license", "status"):
        blocks = [dict(VALID[0])]
        del blocks[0][field]
        result = _run(blocks, tmp_path)
        assert result.returncode == 1, f"omitting {field} should fail"
        assert f"missing required field: {field}" in result.stdout


def test_an_unknown_status_is_an_error(tmp_path):
    blocks = [dict(VALID[0], status="probably-fine")]
    result = _run(blocks, tmp_path)
    assert result.returncode == 1
    assert "invalid status" in result.stdout


def test_duplicate_source_ids_are_an_error(tmp_path):
    """Two blocks claiming one id make the seeded/seeder cross-check ambiguous."""
    blocks = [dict(VALID[0]), dict(VALID[0], name="Another block")]
    result = _run(blocks, tmp_path)
    assert result.returncode == 1
    assert "duplicate source id" in result.stdout


def test_seeded_without_a_seeder_is_an_error(tmp_path):
    blocks = [dict(VALID[0], status="seeded")]
    result = _run(blocks, tmp_path)
    assert result.returncode == 1
    assert "no seeder is named" in result.stdout


def test_a_seeder_that_does_not_exist_is_an_error(tmp_path):
    blocks = [dict(VALID[0], status="seeded", seeder="seed_nothing_at_all.py")]
    result = _run(blocks, tmp_path)
    assert result.returncode == 1
    assert "seeder script not found" in result.stdout


def test_an_unresolved_licence_warns_without_failing(tmp_path):
    """Unresolved licences must be visible, but must not block the gate.

    Both external sources here are collaborator projects whose exact terms are
    still being settled; the catalogue's job is to say so, not to refuse.
    """
    blocks = [dict(VALID[0], license="unknown (collaborator project)")]
    result = _run(blocks, tmp_path)
    assert result.returncode == 0
    assert "licence unresolved" in result.stdout


# --- malformed input must be reported, not raised (#574 review) --------------
#
# All of these used to exit non-zero via a traceback, which keeps CI red but
# tells the operator nothing. `block is null` is not contrived: download.yaml's
# own style is a bare `-` with the mapping indented beneath, so one mis-indented
# key produces exactly that.

def _raw(text: str, tmp_path: Path) -> subprocess.CompletedProcess[str]:
    scripts = tmp_path / "scripts"
    scripts.mkdir(exist_ok=True)
    (scripts / "check_sources.py").write_text(
        CHECKER.read_text(encoding="utf-8"), encoding="utf-8"
    )
    (tmp_path / "download.yaml").write_text(text, encoding="utf-8")
    return subprocess.run(
        [sys.executable, str(scripts / "check_sources.py")],
        capture_output=True, text=True,
    )


def test_malformed_blocks_are_reported_not_raised(tmp_path):
    cases = {
        "bare string block": "- just-a-string\n",
        "null block": "-\n",
        "non-scalar status": (
            "- url: u\n  name: n\n  source: s\n  license: l\n  status: [seeded]\n"
        ),
        "blank seeder": (
            "- url: u\n  name: n\n  source: s\n  license: l\n"
            '  status: seeded\n  seeder: "   "\n'
        ),
    }
    for label, text in cases.items():
        result = _raw(text, tmp_path)
        assert result.returncode == 1, f"{label}: expected a reported error"
        assert "Traceback" not in result.stderr, (
            f"{label}: crashed instead of reporting — {result.stderr[:200]}"
        )


def test_unparseable_yaml_is_reported_not_raised(tmp_path):
    result = _raw("- url: [unclosed\n", tmp_path)
    assert result.returncode == 2
    assert "Traceback" not in result.stderr
    assert "not valid YAML" in result.stderr


def test_an_empty_catalogue_fails(tmp_path):
    """Deleting every source must not satisfy the gate."""
    result = _raw("[]\n", tmp_path)
    assert result.returncode == 2
    assert "no sources" in result.stderr


def test_a_seeder_must_be_a_seed_script(tmp_path):
    """`seeder: ../download.yaml` resolved to a real file and passed."""
    blocks = [dict(VALID[0], status="seeded", seeder="../download.yaml")]
    result = _run(blocks, tmp_path)
    assert result.returncode == 1
    assert "must be a scripts/seed_*.py file" in result.stdout
