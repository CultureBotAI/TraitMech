"""Unit tests for scripts/new_history_record.py.

The point of this scaffolder is that a record gets written on a machine with no
claw checkout, so the tests that matter are the ones about it being a genuine
drop-in: same required arguments, same field order, schema-valid output. An
interface that diverges from claw's reproduces the original trap in a new form —
a command that works with claw and fails without it (#296).
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from new_history_record import (  # noqa: E402
    CLAW_PLACEHOLDER,
    KIND_DIRS,
    _link,
    history_validation_errors,
    main,
    session_id,
)

def _kinds_from_schema() -> set[str]:
    """Parsed, not hand-copied.

    The previous version compared two hardcoded sets, so it could not notice the
    schema growing a kind — and the risk this guards is a KeyError at write time
    for a kind with no directory (#296 review).
    """
    schema = yaml.safe_load((REPO_ROOT / "src/traitmech/schema/history.yaml").read_text())
    return set(schema["enums"]["HistoryTargetKindEnum"]["permissible_values"])

BASE = ["--kind", "record", "--slug", "cellulolysis",
        "--target-root", "data/traits/metabolism",
        "--summary", "s", "--details", "d",
        "--timestamp", "2026-08-05T12:00:00Z"]


def _run(tmp_path, *extra):
    main(BASE + ["--history-root", str(tmp_path)] + list(extra))
    written = sorted(tmp_path.rglob("*.yaml"))
    assert len(written) == 1, written
    return yaml.safe_load(written[0].read_text()), written[0]


def test_the_record_lands_under_its_kind_directory(tmp_path):
    """history/<kind-dir>/<slug>/, not history/records/<slug>/ for every kind —
    history/infrastructure/curation-history/ is a live example. The schema does
    not constrain the path, so the wrong directory validates clean (#296)."""
    main(["--kind", "infrastructure", "--slug", "curation-history",
          "--path", "docs/x.md", "--summary", "s", "--details", "d",
          "--history-root", str(tmp_path), "--timestamp", "2026-08-05T12:00:00Z"])
    written = next(tmp_path.rglob("*.yaml"))
    assert written.parent.parent.name == "infrastructure"
    assert written.parent.name == "curation-history"


def test_every_kind_in_the_schema_has_a_directory():
    """A missing entry would KeyError at write time rather than at parse time."""
    assert set(KIND_DIRS) == _kinds_from_schema()


def test_kind_directories_match_claw():
    """Copied from claw's scaffold.py, not inferred — the pluralisation is uneven
    (mappings/reports but schema/other), which is why guessing was wrong."""
    assert KIND_DIRS == {"record": "records", "schema": "schema",
                         "mapping": "mappings", "report": "reports",
                         "infrastructure": "infrastructure", "other": "other"}


def test_no_scratch_file_survives(tmp_path):
    _run(tmp_path)
    assert list(tmp_path.rglob("*scratch*")) == []


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


def test_the_placeholder_is_claw_s_exact_string(tmp_path):
    """Byte-for-byte, not merely TODO-ish.

    The vendored schema carries `pattern: '^(?!TODO: replace this placeholder)'`
    so a plain linkml-validate catches an unfilled record. A near-miss wording
    slips past the negative lookahead and makes an unfilled record permanently
    committable, which is what the first version of this script did (#296).
    """
    main(["--kind", "record", "--slug", "x", "--target-root", "data/traits/metabolism",
          "--summary", "s", "--history-root", str(tmp_path),
          "--timestamp", "2026-08-05T12:00:00Z"])
    doc = yaml.safe_load(next(tmp_path.rglob("*.yaml")).read_text())
    assert doc["events"][0]["details"] == CLAW_PLACEHOLDER


def test_a_placeholder_record_fails_the_schema_as_the_readme_promises(tmp_path):
    """history/README: "an unfilled record cannot slip through"."""
    main(["--kind", "record", "--slug", "x", "--target-root", "data/traits/metabolism",
          "--summary", "s", "--history-root", str(tmp_path),
          "--timestamp", "2026-08-05T12:00:00Z"])
    path = next(tmp_path.rglob("*.yaml"))
    assert history_validation_errors(path), (
        "placeholder record validated; the guard is dead"
    )


def test_a_failed_force_rewrite_does_not_destroy_the_original(tmp_path, monkeypatch):
    """Append-only: validate a scratch file, then move. Writing first and
    unlinking on failure loses the record --force was correcting (#296)."""
    import new_history_record as m
    _, path = _run(tmp_path)
    before = path.read_text()
    real = m.build

    def broken(args, ts):
        rec, out = real(args, ts)
        rec["events"][0]["outcome"] = "NOT_AN_OUTCOME"
        return rec, out

    monkeypatch.setattr(m, "build", broken)
    with pytest.raises(SystemExit, match="failed validation"):
        m.main(BASE + ["--history-root", str(tmp_path), "--force"])
    assert path.read_text() == before
    assert list(tmp_path.rglob("*scratch*")) == []


def test_kind_and_summary_are_required_like_claw():
    """Claw requires both. A fallback that does not is not a drop-in."""
    for missing in (["--summary", "s"], ["--kind", "record"]):
        with pytest.raises(SystemExit):
            main(missing)


def test_the_generated_record_validates_against_the_vendored_schema(tmp_path):
    """main() validates before printing; this pins that the schema call is real."""
    _, path = _run(tmp_path, "--issue", "296", "--pr", "298",
                   "--sections", "a, b", "--model", "claude-opus-5")
    assert history_validation_errors(path) == []


def test_the_committed_records_still_validate():
    """The corpus this writes into, checked the way CI checks it."""
    records = sorted((REPO_ROOT / "history" / "records").rglob("*.yaml"))
    assert records, "no history records found"
    failures = {str(path): history_validation_errors(path) for path in records}
    failures = {path: errors for path, errors in failures.items() if errors}
    assert failures == {}


def test_sections_sits_between_outcome_and_summary(tmp_path):
    """Schema declaration order, and the order of the one committed record that
    carries it. history/README's headline example passes --sections, so getting
    this wrong put the DOCUMENTED invocation on the divergent path (#296)."""
    _, path = _run(tmp_path, "--sections", "causal_graphs, grounding")
    event = yaml.safe_load(path.read_text())["events"][0]
    assert list(event.keys()) == ["type", "outcome", "sections", "summary", "details"]
    assert event["sections"] == ["causal_graphs", "grounding"]


def test_the_placeholder_path_still_validates_everything_else(tmp_path):
    """Skipping validation wholesale let `--timestamp nonsense` write a record
    and exit 0. A copy with `details` substituted is validated instead."""
    with pytest.raises(SystemExit, match="failed validation"):
        main(["--kind", "record", "--slug", "x",
              "--target-root", "data/traits/metabolism", "--summary", "s",
              "--history-root", str(tmp_path), "--timestamp", "nonsense"])
    assert list(tmp_path.rglob("*.yaml")) == []
