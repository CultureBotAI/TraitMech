"""Offline regression for immutable provenance surviving squash/branch deletion."""

import os
import subprocess
import sys
from copy import deepcopy
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import fetch_record_review_bases as recovery  # noqa: E402
from tests.test_record_review_contract import sample as sample  # noqa: E402
from tests.test_vendored_sync_workflow import _executable  # noqa: E402


@pytest.fixture
def reviews():
    return recovery.reviews


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], stderr=subprocess.PIPE).decode().strip()


@pytest.fixture
def squashed(sample, reviews, tmp_path, monkeypatch, request):
    upstream, record = sample
    git(upstream, "branch", "-M", "main")
    git(upstream, "checkout", "-b", "feature")
    saved = []
    for index in range(getattr(request, "param", 1)):
        document = deepcopy(record)
        document["review_id"] += f"-{index}"
        (upstream / "record.yaml").write_text(f"id: EX:fixture\nlabel: Reviewed {index}\n")
        git(upstream, "add", ".")
        git(upstream, "commit", "-m", "Reviewed checkpoint")
        document["source"] = reviews.inspect_source(upstream, document["targets"])["source"]
        path = reviews.save_review(upstream, document)
        saved.append((document, str(path.relative_to(upstream))))
        git(upstream, "add", ".")
        git(upstream, "commit", "-m", "Persist review")
    git(upstream, "update-ref", "refs/pull/1/head", "HEAD")
    git(upstream, "checkout", "main")
    git(upstream, "merge", "--squash", "feature")
    git(upstream, "commit", "-m", "Squash feature")
    git(upstream, "branch", "-D", "feature")
    clone = tmp_path / "clean-main"
    git(tmp_path, "clone", "--no-local", "--single-branch", "--branch", "main",
        str(upstream), str(clone))
    git(clone, "remote", "set-url", "origin", "https://github.com/Example/FixtureMech.git")
    calls = []
    original = recovery.git

    def offline_git(root, *args, **kwargs):
        calls.append(args)
        if args[0] == "fetch":
            assert args[1:5] == ("--no-tags", "--no-write-fetch-head",
                                  "--no-recurse-submodules", "https://github.com/Example/FixtureMech.git")
            assert len(args) >= 6
            args = (*args[:4], str(upstream), *args[5:])
        return original(root, *args, **kwargs)

    monkeypatch.setattr(recovery, "git", offline_git)
    return clone, *saved[0], calls


def test_squash_branch_deletion_dry_run_and_recovery(squashed, reviews):
    root, record, relative, calls = squashed
    revision = record["source"]["git_revision"]
    before = {name: (root / name).read_bytes() for name in (relative, relative.replace(".yaml", ".md"))}
    assert git(root, "rev-parse", "--is-shallow-repository") == "false"
    with pytest.raises(reviews.ReviewError, match="provenance unverified"):
        reviews.read_review(root, relative)
    plan = recovery.recover(root)
    assert plan["status"] == "dry_run" and plan["bases"][0]["missing"]
    assert not any(call[0] in {"fetch", "update-ref"} for call in calls)
    assert not (root / ".git/FETCH_HEAD").exists()
    receipt = recovery.recover(root, apply=True)
    assert receipt["status"] == "validated"
    assert reviews.read_review(root, relative) == record
    assert git(root, "rev-parse", recovery.REF_PREFIX + revision) == revision
    assert not (root / ".git/FETCH_HEAD").exists()
    assert {name: (root / name).read_bytes() for name in before} == before
    assert git(root, "status", "--porcelain") == ""
    calls.clear()
    recovery.recover(root, apply=True)
    assert not any(call[0] in {"fetch", "update-ref"} for call in calls)
    git(root, "reflog", "expire", "--expire=now", "--all")
    git(root, "gc", "--prune=now")
    assert reviews.read_review(root, relative) == record


@pytest.mark.parametrize("squashed", [2], indirect=True)
def test_missing_bases_are_fetched_together(squashed, reviews):
    root, _, _, calls = squashed
    plan = recovery.recover(root)
    assert len(plan["bases"]) == 2 and all(item["missing"] for item in plan["bases"])
    recovery.recover(root, apply=True)
    fetches = [call for call in calls if call[0] == "fetch"]
    assert len(fetches) == 1
    assert fetches[0][5:] == tuple(item["revision"] for item in plan["bases"])
    for relative in reviews.review_paths(root):
        reviews.read_review(root, relative)


def rewrite(root, relative, record, reviews):
    (root / relative).write_text(yaml.safe_dump(record, sort_keys=False))
    (root / relative).with_suffix(".md").write_text(reviews.render_markdown(record))


@pytest.mark.parametrize("mutation", [
    "repository", "short_sha", "markdown", "duplicate_key", "symlink", "invalid_utf8",
])
def test_invalid_bundles_never_fetch_or_mutate(squashed, reviews, mutation):
    root, record, relative, calls = squashed
    if mutation == "repository":
        record["repository"] = "Example/DifferentMech"
        rewrite(root, relative, record, reviews)
    elif mutation == "short_sha":
        record["source"]["git_revision"] = record["source"]["git_revision"][:12]
        # Deliberately bypass the shared renderer, which also validates.
        (root / relative).write_text(yaml.safe_dump(record, sort_keys=False))
    elif mutation == "markdown":
        (root / relative).with_suffix(".md").write_text("Unrelated assessment")
    elif mutation == "duplicate_key":
        with (root / relative).open("a") as stream:
            stream.write("repository: Example/FixtureMech\n")
    elif mutation == "invalid_utf8":
        (root / relative).with_suffix(".md").write_bytes(b"\xff")
    else:
        path = root / relative
        contents = path.read_bytes()
        path.unlink()
        (root / "outside.yaml").write_bytes(contents)
        path.symlink_to(root / "outside.yaml")
    with pytest.raises((reviews.ReviewError, OSError, UnicodeError)):
        recovery.recover(root, apply=True)
    if mutation == "invalid_utf8":
        assert recovery.main(["--repo-root", str(root), "--apply"]) == 2
    assert not any(call[0] in {"fetch", "update-ref"} for call in calls)


def test_ignored_bundles_are_included(squashed):
    root, _, _, _ = squashed
    git(root, "rm", "--cached", "-r", "reviews")
    (root / ".gitignore").write_text("reviews/\n")
    assert recovery.recover(root)["reviews"] == 1


def test_bad_origin_refused_before_fetch(squashed, reviews):
    root, _, _, calls = squashed
    git(root, "remote", "set-url", "origin", "https://example.invalid/Example/FixtureMech.git")
    with pytest.raises(reviews.ReviewError, match="GitHub repository"):
        recovery.recover(root, apply=True)
    assert not calls


def test_unavailable_commit_fails_without_success(squashed, monkeypatch):
    root, _, _, calls = squashed
    original = recovery.git

    def unavailable(root, *args, **kwargs):
        if args[0] == "fetch":
            raise recovery.reviews.ReviewError("source unavailable")
        return original(root, *args, **kwargs)

    monkeypatch.setattr(recovery, "git", unavailable)
    with pytest.raises(recovery.reviews.ReviewError, match="source unavailable"):
        recovery.recover(root, apply=True)
    assert not any(call[0] == "update-ref" for call in calls)


def test_retention_conflict_never_overwritten(squashed):
    root, record, _, calls = squashed
    git(root, "update-ref", recovery.REF_PREFIX + record["source"]["git_revision"], "HEAD")
    with pytest.raises(recovery.reviews.ReviewError, match="conflicting retained"):
        recovery.recover(root, apply=True)
    assert not any(call[0] in {"fetch", "update-ref"} for call in calls)


@pytest.mark.parametrize("present", [False, True])
def test_historical_hash_mismatch_is_not_accepted(squashed, reviews, present):
    root, record, relative, calls = squashed
    if present:
        recovery.recover(root, apply=True)
        calls.clear()
    record["source"]["state"] = "git_commit"
    record["source"]["inputs"][0]["sha256"] = "0" * 64
    rewrite(root, relative, record, reviews)
    with pytest.raises(reviews.ReviewError, match="hash disagrees"):
        recovery.recover(root, apply=True)
    if present:
        assert not any(call[0] in {"fetch", "update-ref"} for call in calls)


def test_cli_and_ci_explicit_preparation(squashed, capsys):
    root, _, _, calls = squashed
    assert recovery.main(["--repo-root", str(root)]) == 0
    assert '"status": "dry_run"' in capsys.readouterr().out
    assert not any(call[0] in {"fetch", "update-ref"} for call in calls)
    assert recovery.main(["--repo-root", str(root), "--apply"]) == 0
    assert '"status": "validated"' in capsys.readouterr().out
    repo = Path(__file__).resolve().parents[1]
    workflow = yaml.safe_load((repo / ".github/workflows/pytest.yaml").read_text())
    steps = workflow["jobs"]["pytest"]["steps"]
    commands = [step.get("run", "") for step in steps]
    preparation = next(index for index, step in enumerate(steps)
                       if step.get("name") == "Recover retained review source commits")
    assert "uv run python scripts/fetch_record_review_bases.py --apply" in commands[preparation]
    assert preparation < commands.index("uv run pytest tests/ -v --tb=short")
    assert "github.event.pull_request.base.sha" in workflow["env"]["RECORD_REVIEW_BASE"]
    assert "reviews/structured/**" in workflow[True]["push"]["paths"]
    assert "fetch-record-review-bases *args:" in (repo / "justfile").read_text()


@pytest.mark.parametrize(("error", "status"), [
    (recovery.FetchError("remote fetch failed"), 1),
    (recovery.reviews.ReviewError("invalid local review"), 2),
    (OSError("local file unavailable"), 2),
    (UnicodeDecodeError("utf-8", b"\xff", 0, 1, "invalid review encoding"), 2),
    (RuntimeError("unexpected local failure"), 2),
])
def test_cli_failure_classes(monkeypatch, capsys, error, status):
    def fail(*args, **kwargs):
        raise error

    monkeypatch.setattr(recovery, "recover", fail)
    assert recovery.main([]) == status
    result = capsys.readouterr()
    assert not result.out
    assert str(error) in result.err


@pytest.mark.parametrize("operation", ["fetch", "update-ref"])
def test_git_timeout_reports_operation_revision_and_bound(tmp_path, monkeypatch, operation):
    revision = "a" * 40

    def timeout(command, **kwargs):
        assert kwargs["timeout"] == 300
        raise subprocess.TimeoutExpired(command, kwargs["timeout"], stderr=b"partial Git diagnostic")

    monkeypatch.setattr(recovery.subprocess, "run", timeout)
    with pytest.raises(recovery.reviews.ReviewError) as caught:
        recovery.git(tmp_path, operation, revision)
    assert isinstance(caught.value, recovery.FetchError) == (operation == "fetch")
    assert f"timed out after 300s: {operation} {revision}" in str(caught.value)
    assert "partial Git diagnostic" in str(caught.value)


@pytest.mark.parametrize("operation", ["fetch", "update-ref"])
def test_git_nonzero_status_retains_diagnostics(tmp_path, monkeypatch, operation):
    def failed(command, **kwargs):
        return subprocess.CompletedProcess(command, 128, "", "upstream or local rejection")

    monkeypatch.setattr(recovery.subprocess, "run", failed)
    with pytest.raises(recovery.reviews.ReviewError) as caught:
        recovery.git(tmp_path, operation, "a" * 40)
    assert isinstance(caught.value, recovery.FetchError) == (operation == "fetch")
    assert operation in str(caught.value) and "upstream or local rejection" in str(caught.value)


def test_missing_git_is_not_a_retryable_fetch_error(tmp_path, monkeypatch):
    def absent(*args, **kwargs):
        raise FileNotFoundError("git executable unavailable")

    monkeypatch.setattr(recovery.subprocess, "run", absent)
    with pytest.raises(recovery.reviews.ReviewError) as caught:
        recovery.git(tmp_path, "fetch", "a" * 40)
    assert not isinstance(caught.value, recovery.FetchError)
    assert "git executable unavailable" in str(caught.value)


@pytest.mark.parametrize(("statuses", "result_code", "call_count", "sleep_count"), [
    ([0], 0, 1, 0), ([1, 0], 0, 2, 1), ([1, 1, 0], 0, 3, 2),
    ([1, 1, 1], 1, 3, 2), ([2], 2, 1, 0), ([99], 99, 1, 0),
    ([1, 2], 2, 2, 1), ([130], 130, 1, 0),
])
def test_ci_retries_only_fetch_failures(tmp_path, statuses, result_code, call_count, sleep_count):
    repo = Path(__file__).resolve().parents[1]
    workflow = yaml.safe_load((repo / ".github/workflows/pytest.yaml").read_text())
    block = next(step["run"] for step in workflow["jobs"]["pytest"]["steps"]
                 if step.get("name") == "Recover retained review source commits")
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    calls, sleeps, sequence = (tmp_path / name for name in ("calls", "sleeps", "statuses"))
    calls.write_text("")
    sleeps.write_text("")
    sequence.write_text("\n".join(map(str, statuses)) + "\n")
    _executable(bin_dir / "uv", """#!/usr/bin/env bash
set -eu
test "$*" = "run python scripts/fetch_record_review_bases.py --apply"
echo call >> "$CALL_LOG"
count=$(wc -l < "$CALL_LOG")
status=$(sed -n "${count}p" "$STATUS_FILE")
exit "${status:-1}"
""")
    _executable(bin_dir / "sleep", """#!/usr/bin/env bash
set -eu
test "$*" = "5"
echo sleep >> "$SLEEP_LOG"
""")
    result = subprocess.run(
        ["bash", "-e", "-c", block], cwd=tmp_path, capture_output=True, text=True,
        env={**os.environ, "PATH": f"{bin_dir}:{os.environ['PATH']}",
             "CALL_LOG": str(calls), "SLEEP_LOG": str(sleeps), "STATUS_FILE": str(sequence)},
        timeout=10,
    )
    assert result.returncode == result_code, result.stderr
    assert len(calls.read_text().splitlines()) == call_count
    assert len(sleeps.read_text().splitlines()) == sleep_count
