"""Unit tests for scripts/new_history_record.py.

The point of this scaffolder is that a record gets written on a machine with no
claw checkout, so the tests that matter are the ones about it being a genuine
drop-in: same required arguments, same field order, schema-valid output. An
interface that diverges from claw's reproduces the original trap in a new form —
a command that works with claw and fails without it (#296).
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from new_history_record import _link, main, session_id  # noqa: E402

BASE = ["--kind", "record", "--slug", "cellulolysis",
        "--target-root", "data/traits/metabolism",
        "--summary", "s", "--details", "d",
        "--timestamp", "2026-08-05T12:00:00Z"]


def _run(tmp_path, *extra):
    main(BASE + ["--history-root", str(tmp_path)] + list(extra))
    written = sorted(tmp_path.rglob("*.yaml"))
    assert len(written) == 1, written
    return yaml.safe_load(written[0].read_text()), written[0]


def test_writes_a_record_under_the_slug(tmp_path):
    doc, path = _run(tmp_path)
    assert path.parent.name == "cellulolysis"
    assert doc["target"] == {"kind": "record", "slug": "cellulolysis",
                             "path": "data/traits/metabolism/cellulolysis.yaml"}


def test_the_session_id_matches_the_existing_convention(tmp_path):
    """`2026-08-03T230903Z-claude-code-90a277` — date hyphens kept, colons not."""
    doc, path = _run(tmp_path)
    assert doc["session"]["id"].startswith("2026-08-05T120000Z-claude-code-")
    assert path.name == doc["session"]["id"] + ".yaml"


def test_the_id_is_derived_not_random(tmp_path):
    """Identical arguments must produce an identical id, so a re-run is caught
    by the append-only guard rather than writing a second record."""
    a = session_id("2026-08-05T12:00:00Z", "claude-code", "seed")
    b = session_id("2026-08-05T12:00:00Z", "claude-code", "seed")
    assert a == b
    assert a != session_id("2026-08-05T12:00:00Z", "claude-code", "other")


def test_rewriting_the_same_record_is_refused(tmp_path):
    _run(tmp_path)
    with pytest.raises(SystemExit, match="append-only"):
        main(BASE + ["--history-root", str(tmp_path)])


def test_force_overwrites_a_mis_scaffolded_record(tmp_path):
    _run(tmp_path)
    main(BASE + ["--history-root", str(tmp_path), "--force"])


def test_field_order_matches_the_committed_records(tmp_path):
    """A diff against a claw-written record should be empty, not a reshuffle."""
    _, path = _run(tmp_path, "--issue", "296")
    keys = list(yaml.safe_load(path.read_text()).keys())
    assert keys == ["history_version", "target", "session", "links", "events"]


def test_links_without_issues_or_prs_are_omitted(tmp_path):
    doc, _ = _run(tmp_path)
    assert "links" not in doc


@pytest.mark.parametrize("given,expected", [
    ("296", "https://github.com/CultureBotAI/TraitMech/issues/296"),
    ("#296", "https://github.com/CultureBotAI/TraitMech/issues/296"),
    # Already a URL: passed through, so a caller following claw's habit of
    # writing the full link is not double-expanded.
    ("https://example.org/x", "https://example.org/x"),
])
def test_bare_issue_numbers_become_uris(given, expected):
    """The schema declares these `range: uri`; claw writes "296" through as-is."""
    assert _link(given, "issues") == expected


def test_details_defaults_to_a_placeholder_like_claw(tmp_path):
    main(["--kind", "record", "--slug", "x", "--target-root", "data/traits/metabolism",
          "--summary", "s", "--history-root", str(tmp_path),
          "--timestamp", "2026-08-05T12:00:00Z"])
    doc = yaml.safe_load(next(tmp_path.rglob("*.yaml")).read_text())
    assert doc["events"][0]["details"].startswith("TODO")


def test_kind_and_summary_are_required_like_claw():
    """Claw requires both. A fallback that does not is not a drop-in."""
    for missing in (["--summary", "s"], ["--kind", "record"]):
        with pytest.raises(SystemExit):
            main(missing)


def test_the_generated_record_validates_against_the_vendored_schema(tmp_path):
    """main() validates before printing; this pins that the schema call is real."""
    _, path = _run(tmp_path, "--issue", "296", "--pr", "298",
                   "--sections", "a, b", "--model", "claude-opus-5")
    result = subprocess.run(
        ["uv", "run", "linkml-validate", "--schema",
         str(REPO_ROOT / "src/traitmech/schema/history.yaml"),
         "--target-class", "HistoryRecord", str(path)],
        cwd=REPO_ROOT, capture_output=True, text=True)
    assert result.returncode == 0, result.stdout or result.stderr


def test_the_committed_records_still_validate():
    """The corpus this writes into, checked the way CI checks it."""
    records = sorted((REPO_ROOT / "history" / "records").rglob("*.yaml"))
    assert records, "no history records found"
    result = subprocess.run(
        ["uv", "run", "linkml-validate", "--schema",
         str(REPO_ROOT / "src/traitmech/schema/history.yaml"),
         "--target-class", "HistoryRecord", *map(str, records)],
        cwd=REPO_ROOT, capture_output=True, text=True)
    assert result.returncode == 0, result.stdout or result.stderr
