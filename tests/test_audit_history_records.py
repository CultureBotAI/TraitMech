"""Unit tests for scripts/audit_history_records.py (#325).

The rule is three lines, so what these pin is mostly the edges that would make it
silently permissive: an empty history list, a MODIFIED record standing in for an
added one, and a no-trait-change PR being clean rather than blocked.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from audit_history_records import missing_record  # noqa: E402

TRAIT = "data/traits/morphology/motile.yaml"
RECORD = "history/records/motile/2026-08-07T000000Z-claude-code-abc123.yaml"


def test_trait_change_without_a_record_is_blocked():
    assert missing_record([TRAIT], []) is True


def test_one_record_covers_many_changed_traits():
    """The granularity fix, and the reason the gate is impose-able at all.

    Under the literal 'one record per session per target' reading, a 128-file
    migration owed 128 records. This asserts the opposite: ONE is enough for a
    whole migration, so the cost is one file per PR rather than one per record.
    """
    many = [f"data/traits/morphology/t{i}.yaml" for i in range(128)]
    assert missing_record(many, [RECORD]) is False


def test_no_trait_change_is_clean_not_blocked():
    """A PR touching only history/, the schema or the workflow owes nothing."""
    assert missing_record([], []) is False
    assert missing_record([], [RECORD]) is False


def test_a_modified_record_does_not_count_as_an_added_one():
    """Records are append-only: written once, never edited, corrections go in a
    NEW record referencing the old one. `collect` passes only --diff-filter=A
    files, so an edit to an existing record reaches this as an empty list --
    which must still block, or the gate accepts the one thing the append-only
    design forbids."""
    assert missing_record([TRAIT], []) is True


def test_the_scripts_own_cli_agrees_with_the_rule():
    """End-to-end through argparse, since the workflow calls the CLI and not the
    function -- a wiring error there would leave the rule correct and unused."""
    def run(changed, added):
        return subprocess.run(
            [sys.executable, str(REPO_ROOT / "scripts" / "audit_history_records.py"),
             "--changed", *changed, "--added", *added],
            capture_output=True, text=True)

    bad = run([TRAIT], [])
    assert bad.returncode == 1
    assert "adds no history record" in bad.stderr
    # The remediation must name the ONE-record rule, since the whole reason this
    # is blocking is that the per-file reading was unreasonable.
    assert "not one per file" in bad.stderr

    good = run([TRAIT], [RECORD])
    assert good.returncode == 0

    nothing = run([], [])
    assert nothing.returncode == 0


# --- #357 review: the pathspec itself, which missing_record() cannot see -------


def _git(cwd, *args):
    subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True)


def _repo(tmp_path: Path) -> Path:
    _git(tmp_path, "init", "-q", "-b", "main")
    _git(tmp_path, "config", "user.email", "t@t")
    _git(tmp_path, "config", "user.name", "t")
    (tmp_path / "README").write_text("base\n")
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-qm", "base")
    return tmp_path


def test_collect_sees_a_trait_directly_under_data_traits(tmp_path):
    """A git pathspec is NOT a shell glob.

    git's `*` already crosses `/`, so `data/traits/**/*.yaml` must still consume
    the literal slash in `**/` and therefore needs at least one intervening
    directory -- it misses `data/traits/x.yaml`. The workflow's trigger is
    `paths: data/traits/**`, which is GitHub Actions semantics and DOES match
    that file, so the job would start and then clear the gate at "0 changed".
    Silently permissive, and invisible to missing_record().
    """
    repo = _repo(tmp_path)
    for rel in ["data/traits/toplevel.yaml", "data/traits/morphology/nested.yaml"]:
        p = repo / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("identifier: x\n")
    _git(repo, "add", "-A")
    _git(repo, "commit", "-qm", "traits")

    import audit_history_records as m
    cwd = Path.cwd()
    try:
        import os
        os.chdir(repo)
        changed, added = m.collect("main~1")
    finally:
        os.chdir(cwd)
    assert sorted(changed) == ["data/traits/morphology/nested.yaml",
                               "data/traits/toplevel.yaml"]


def test_collect_counts_a_history_record_at_any_depth(tmp_path):
    """Same bug on the other side: a record not nested under a slug dir would
    not have counted toward presence."""
    repo = _repo(tmp_path)
    for rel in ["history/flat.yaml", "history/records/slug/deep.yaml"]:
        p = repo / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("history_version: 1\n")
    (repo / "data/traits").mkdir(parents=True)
    (repo / "data/traits/t.yaml").write_text("identifier: x\n")
    _git(repo, "add", "-A")
    _git(repo, "commit", "-qm", "records")

    import audit_history_records as m
    import os
    cwd = Path.cwd()
    try:
        os.chdir(repo)
        changed, added = m.collect("main~1")
    finally:
        os.chdir(cwd)
    assert sorted(added) == ["history/flat.yaml", "history/records/slug/deep.yaml"]
    assert m.missing_record(changed, added) is False
