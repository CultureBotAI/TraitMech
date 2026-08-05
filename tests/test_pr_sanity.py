"""Unit tests for scripts/pr_sanity.py.

The point of pr_sanity is to run on PRs that no other workflow inspects, so a
check that silently matches nothing would recreate the exact problem it exists
to solve (#200). These therefore assert both directions for every check: that it
fires on a real defect, and that it stays quiet on the legitimate lookalike.
"""

from __future__ import annotations

import subprocess
import sys
import textwrap
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from pr_sanity import (  # noqa: E402
    CONFLICT_RE,
    check_conflict_markers,
    check_markdown_links,
    check_action_pins,
    check_workflow_concurrency,
    check_workflows,
    prose_lines,
    sanity,
)

UNFILTERED_WF = """\
name: catchall
on:
  pull_request:
jobs:
  a:
    runs-on: ubuntu-latest
    steps: [{run: "true"}]
"""

FILTERED_WF = """\
name: narrow
on:
  pull_request:
    paths:
      - "src/**"
jobs:
  a:
    runs-on: ubuntu-latest
    steps: [{run: "true"}]
"""


def _repo(tmp_path: Path) -> Path:
    """A real git repo — pr_sanity reads the file list from `git ls-files`."""
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    (tmp_path / ".github" / "workflows").mkdir(parents=True)
    return tmp_path


def _commit(root: Path) -> None:
    subprocess.run(["git", "add", "-A"], cwd=root, check=True)


def _checks(findings) -> set[str]:
    return {f["check"] for f in findings}


# --- workflow validity ------------------------------------------------------


def test_valid_unfiltered_workflow_is_clean(tmp_path):
    root = _repo(tmp_path)
    (root / ".github/workflows/a.yaml").write_text(UNFILTERED_WF)
    assert check_workflows(root) == []


def test_unparseable_workflow_flagged(tmp_path):
    root = _repo(tmp_path)
    (root / ".github/workflows/a.yaml").write_text(UNFILTERED_WF)
    (root / ".github/workflows/bad.yaml").write_text("name: x\n  bad: [indent\n")
    assert "WORKFLOW_INVALID" in _checks(check_workflows(root))


def test_workflow_without_jobs_flagged(tmp_path):
    root = _repo(tmp_path)
    (root / ".github/workflows/a.yaml").write_text(UNFILTERED_WF)
    (root / ".github/workflows/nojobs.yaml").write_text("name: x\non:\n  push:\n")
    findings = check_workflows(root)
    assert any(f["check"] == "WORKFLOW_INVALID" and "jobs" in f["detail"]
               for f in findings)


# --- the #200 invariant -----------------------------------------------------


def test_all_filtered_workflows_trips_the_invariant(tmp_path):
    """Every workflow behind a paths filter == some PRs run nothing."""
    root = _repo(tmp_path)
    (root / ".github/workflows/a.yaml").write_text(FILTERED_WF)
    (root / ".github/workflows/b.yaml").write_text(FILTERED_WF)
    assert "NO_UNFILTERED_CI" in _checks(check_workflows(root))


def test_one_unfiltered_workflow_satisfies_the_invariant(tmp_path):
    root = _repo(tmp_path)
    (root / ".github/workflows/a.yaml").write_text(FILTERED_WF)
    (root / ".github/workflows/b.yaml").write_text(UNFILTERED_WF)
    assert "NO_UNFILTERED_CI" not in _checks(check_workflows(root))


def test_pull_request_with_empty_paths_list_counts_as_unfiltered(tmp_path):
    root = _repo(tmp_path)
    (root / ".github/workflows/a.yaml").write_text(
        "name: x\non:\n  pull_request:\n    branches: [main]\njobs:\n"
        "  a:\n    runs-on: ubuntu-latest\n    steps: [{run: \"true\"}]\n"
    )
    assert "NO_UNFILTERED_CI" not in _checks(check_workflows(root))


def test_missing_workflows_dir_is_a_finding_not_a_skip(tmp_path):
    """A deleted CI directory must fail, not pass quietly. An early `return []`
    here would make `just qc` green on a repo with no CI at all."""
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    assert "NO_UNFILTERED_CI" in _checks(check_workflows(tmp_path))


def test_real_repo_satisfies_the_invariant():
    """Guards the live repo: if the last unfiltered workflow gains a paths
    filter, this fails rather than silently reducing coverage."""
    assert "NO_UNFILTERED_CI" not in _checks(check_workflows(REPO_ROOT))


# --- conflict markers -------------------------------------------------------


def test_conflict_marker_flagged(tmp_path):
    root = _repo(tmp_path)
    (root / "f.py").write_text("a = 1\n<<<<<<< HEAD\nb = 2\n")
    _commit(root)
    findings = check_conflict_markers([root / "f.py"], root)
    assert [f["check"] for f in findings] == ["CONFLICT_MARKER"]
    assert findings[0]["file"].endswith(":2")


def test_setext_heading_is_not_a_conflict_marker():
    """`=======` under a line is a Markdown H1, which is why only <<< and >>>
    are matched. Matching `=` would false-positive on ordinary prose."""
    assert not CONFLICT_RE.match("=======")
    assert not CONFLICT_RE.match("=========")
    assert CONFLICT_RE.match("<<<<<<< HEAD")
    assert CONFLICT_RE.match(">>>>>>> branch")


# --- markdown links ---------------------------------------------------------


def test_broken_relative_link_flagged(tmp_path):
    root = _repo(tmp_path)
    md = root / "a.md"
    md.write_text("see [docs](docs/nope.md)\n")
    _commit(root)
    findings = check_markdown_links([md], root)
    assert [f["check"] for f in findings] == ["BROKEN_LINK"]


def test_resolving_link_and_anchor_and_url_are_clean(tmp_path):
    root = _repo(tmp_path)
    (root / "target.md").write_text("hi\n")
    md = root / "a.md"
    md.write_text(textwrap.dedent("""\
        [ok](target.md)
        [anchored](target.md#section)
        [external](https://example.com/missing)
        [internal anchor](#heading)
        [mail](mailto:someone@example.com)
    """))
    _commit(root)
    assert check_markdown_links([md], root) == []


def test_links_escaping_the_repo_are_skipped(tmp_path):
    """README points at sibling fleet checkouts (../CultureMech). Whether those
    resolve depends on what is cloned next door, so checking them makes the
    result machine-dependent — they passed locally and failed on the runner."""
    root = _repo(tmp_path)
    md = root / "README.md"
    md.write_text("[sibling](../CultureMech) and [deep](../../elsewhere/x.md)\n")
    _commit(root)
    assert check_markdown_links([md], root) == []


def test_case_only_mismatch_is_flagged_even_on_case_insensitive_fs(tmp_path):
    """`skill.md` vs `SKILL.md` resolves on macOS and not on Linux. A plain
    exists() therefore passes locally and fails in CI — which is how a stale
    lowercase link survived the SKILL.md rename in #190."""
    root = _repo(tmp_path)
    (root / "docs").mkdir()
    (root / "docs/SKILL.md").write_text("hi\n")
    md = root / "a.md"
    md.write_text("[wrong case](docs/skill.md)\n")
    _commit(root)
    findings = check_markdown_links([md], root)
    assert [f["check"] for f in findings] == ["BROKEN_LINK"]

    md.write_text("[right case](docs/SKILL.md)\n")
    assert check_markdown_links([md], root) == []


def test_within_handles_relative_candidates(tmp_path):
    """A relative candidate compared against an absolute root always raises
    ValueError, which would classify every in-repo link as external and make
    the link check silently vacuous."""
    from pr_sanity import _within

    root = _repo(tmp_path)
    assert _within(Path("docs/x.md"), Path("."))
    assert _within(root / "docs/x.md", root)
    assert not _within(Path("../outside/x.md"), Path("."))


# --- fenced code blocks (#202) ---------------------------------------------


def _links_kept(text: str) -> list[str]:
    lines, _ = prose_lines(text)
    return [line.strip() for _, line in lines if "](" in line]


def test_link_inside_a_fence_is_ignored_and_prose_links_survive():
    kept = _links_kept("[a](x.md)\n```\n[b](y.md)\n```\n[c](z.md)\n")
    assert kept == ["[a](x.md)", "[c](z.md)"]


def test_longer_fence_contains_a_shorter_one():
    """A ````-fence is how one documents a ```-fence. A 3-backtick line must
    not close a 4-backtick block, or the example's contents leak out as prose."""
    kept = _links_kept("````markdown\n```\n[in](y.md)\n```\n````\n[out](z.md)\n")
    assert kept == ["[out](z.md)"]


def test_tilde_fences_and_indented_fences():
    assert _links_kept("~~~\n[in](y.md)\n~~~\n[out](z.md)\n") == ["[out](z.md)"]
    # A fence indented under a list item still opens a block.
    assert _links_kept("- item:\n  ```\n  [in](y.md)\n  ```\n[out](z.md)\n") \
        == ["[out](z.md)"]


def test_backtick_fence_is_not_closed_by_a_tilde_fence():
    kept = _links_kept("```\n~~~\n[still-in](y.md)\n```\n[out](z.md)\n")
    assert kept == ["[out](z.md)"]


def test_inline_code_span_is_not_a_link():
    kept = _links_kept("use `[x](y.md)` here [real](z.md)\n")
    assert kept == ["use  here [real](z.md)"]


def test_unterminated_fence_is_reported_not_silently_swallowed(tmp_path):
    """An unclosed fence hides every later line. Shrinking coverage quietly is
    the failure this whole script exists to prevent, so it must be loud."""
    lines, unterminated = prose_lines("[a](x.md)\n```\n[never](y.md)\n")
    assert unterminated == 2
    assert [line for _, line in lines if "](" in line] == ["[a](x.md)"]

    root = _repo(tmp_path)
    md = root / "a.md"
    md.write_text("```\n[never](nope.md)\n")
    _commit(root)
    assert [f["check"] for f in check_markdown_links([md], root)] \
        == ["UNTERMINATED_FENCE"]


def test_broken_link_in_a_fence_does_not_fire(tmp_path):
    root = _repo(tmp_path)
    md = root / "a.md"
    md.write_text("```markdown\n[example](totally/missing.md)\n```\n")
    _commit(root)
    assert check_markdown_links([md], root) == []


def test_root_relative_link_resolves_from_repo_root(tmp_path):
    root = _repo(tmp_path)
    (root / "docs").mkdir()
    (root / "docs/target.md").write_text("hi\n")
    nested = root / "docs/a.md"
    nested.write_text("[up](/docs/target.md)\n")
    _commit(root)
    assert check_markdown_links([nested], root) == []


# --- end to end -------------------------------------------------------------


def test_sanity_aggregates_all_checks(tmp_path):
    root = _repo(tmp_path)
    (root / ".github/workflows/a.yaml").write_text(FILTERED_WF)  # trips invariant
    (root / "f.py").write_text("<<<<<<< HEAD\n")
    (root / "a.md").write_text("[x](missing.md)\n")
    _commit(root)
    assert _checks(sanity(root)) == {
        "NO_UNFILTERED_CI", "CONFLICT_MARKER", "BROKEN_LINK",
    }


def test_cli_exit_codes(tmp_path):
    root = _repo(tmp_path)
    (root / ".github/workflows/a.yaml").write_text(UNFILTERED_WF)
    _commit(root)
    script = str(REPO_ROOT / "scripts" / "pr_sanity.py")

    ok = subprocess.run([sys.executable, script, "--root", str(root)],
                        capture_output=True, text=True)
    assert ok.returncode == 0, ok.stderr

    (root / "bad.md").write_text("[x](nope.md)\n")
    _commit(root)
    bad = subprocess.run([sys.executable, script, "--root", str(root)],
                         capture_output=True, text=True)
    assert bad.returncode == 1
    assert "BROKEN_LINK" in bad.stderr


# --- CONCURRENCY_SHARED_ACROSS_TRIGGERS (#218) -------------------------------
#
# The bug this guards against (#215) was invisible for a subtle reason: GitHub
# evaluates `concurrency` at the RUN level, before a job's `if:`. A run that
# skips every job still joins the group and still cancels what is in it. These
# assert the real historical defect fires, and that every legitimate shape the
# repo actually uses stays quiet — a lint that flagged those would be turned off
# within a week.

def _conc(doc_text):
    doc = yaml.safe_load(textwrap.dedent(doc_text))
    return check_workflow_concurrency("wf.yaml", doc, doc.get("on", doc.get(True)))


JOBS = "jobs: {a: {runs-on: ubuntu-latest}}"


def test_the_actual_215_configuration_is_flagged():
    """The pre-#216 claude-code-review.yml, verbatim in shape."""
    found = _conc(f"""
        on:
          pull_request: {{types: [opened, synchronize]}}
          issue_comment: {{types: [created]}}
        concurrency:
          group: claude-review-${{{{ github.event.pull_request.number || github.event.issue.number }}}}
          cancel-in-progress: true
        {JOBS}
    """)
    assert [f["check"] for f in found] == ["CONCURRENCY_SHARED_ACROSS_TRIGGERS"]
    assert "issue_comment" in found[0]["detail"]


def test_group_keyed_by_event_name_is_clean():
    """The #216 fix."""
    assert _conc(f"""
        on:
          pull_request:
          issue_comment:
        concurrency:
          group: r-${{{{ github.event.pull_request.number }}}}-${{{{ github.event_name == 'pull_request' && 'push' || github.run_id }}}}
          cancel-in-progress: true
        {JOBS}
    """) == []


def test_conditional_cancel_in_progress_is_clean():
    """vendored-sync.yaml's shape: cancellation itself is gated on the event."""
    assert _conc(f"""
        on:
          pull_request:
          issue_comment:
        concurrency:
          group: v-${{{{ github.ref }}}}
          cancel-in-progress: ${{{{ github.event_name == 'pull_request' }}}}
        {JOBS}
    """) == []


def test_cancel_expression_pointing_the_wrong_way_is_flagged():
    """`github.event_name` present, but separating the wrong thing.

    `!= 'push'` leaves pull_request and issue_comment both cancelling in one
    group — #215 verbatim — so merely mentioning github.event_name must not be
    enough to read as fixed.
    """
    found = _conc(f"""
        on:
          pull_request:
          issue_comment:
        concurrency:
          group: r-${{{{ github.event.pull_request.number }}}}
          cancel-in-progress: ${{{{ github.event_name != 'push' }}}}
        {JOBS}
    """)
    assert [f["check"] for f in found] == ["CONCURRENCY_SHARED_ACROSS_TRIGGERS"]


def test_cancel_expression_excluding_the_colliding_trigger_is_clean():
    """The other valid shape: name the trigger being kept out."""
    assert _conc(f"""
        on:
          pull_request:
          issue_comment:
        concurrency:
          group: r-${{{{ github.event.pull_request.number }}}}
          cancel-in-progress: ${{{{ github.event_name != 'issue_comment' }}}}
        {JOBS}
    """) == []


def test_schedule_alongside_pull_request_does_not_trip_it():
    """A scheduled run's ref is a branch, never refs/pull/N/merge.

    Same property that exempts `push`, so flagging this would be the day-one
    false positive on a ref-keyed group — one trigger over from the shape the
    push test already covers.
    """
    assert _conc(f"""
        on:
          pull_request:
          schedule: [{{cron: "0 3 * * *"}}]
        concurrency:
          group: ch-${{{{ github.ref }}}}
          cancel-in-progress: true
        {JOBS}
    """) == []


def test_list_shorthand_on_is_not_a_blind_spot():
    """`on: [pull_request, issue_comment]` is valid and must still be checked.

    The dict-only guard silently returned no findings here, which is the same
    "nothing evaluated it" failure the whole script exists to prevent.
    """
    found = _conc(f"""
        on: [pull_request, issue_comment]
        concurrency:
          group: shared-${{{{ github.event.issue.number }}}}
          cancel-in-progress: true
        {JOBS}
    """)
    assert [f["check"] for f in found] == ["CONCURRENCY_SHARED_ACROSS_TRIGGERS"]


def test_list_shorthand_counts_as_unfiltered_ci(tmp_path):
    """The same shorthand blind spot in NO_UNFILTERED_CI: no `paths:` is possible."""
    root = _repo(tmp_path)
    (root / ".github/workflows/a.yaml").write_text(
        "name: x\non: [pull_request]\njobs:\n  a:\n    runs-on: ubuntu-latest\n"
        "    steps: [{run: \"true\"}]\n"
    )
    _commit(root)
    assert "NO_UNFILTERED_CI" not in _checks(check_workflows(root))


def test_no_cancellation_is_clean():
    """Sharing a group only queues; without cancellation there is no hazard."""
    assert _conc(f"""
        on:
          pull_request:
          issue_comment:
        concurrency:
          group: shared
          cancel-in-progress: false
        {JOBS}
    """) == []


def test_push_alongside_pull_request_does_not_trip_it():
    """curation-history.yaml's shape — must not false-positive.

    A pull_request run and a push run get different `github.ref`
    (refs/pull/N/merge vs refs/heads/X), so a ref-keyed group already separates
    them. Flagging this would be the noise that gets the whole check disabled.
    """
    assert _conc(f"""
        on:
          pull_request:
          push: {{branches: [main]}}
          workflow_dispatch:
        concurrency:
          group: ch-${{{{ github.ref }}}}
          cancel-in-progress: true
        {JOBS}
    """) == []


def test_job_level_concurrency_is_checked_too():
    """#216 moved the block onto the job; the hazard moves with it."""
    doc = yaml.safe_load(textwrap.dedent("""
        on:
          pull_request:
          issue_comment:
        jobs:
          a:
            runs-on: ubuntu-latest
            concurrency:
              group: shared-${{ github.event.issue.number }}
              cancel-in-progress: true
    """))
    found = check_workflow_concurrency("wf.yaml", doc, doc.get("on", doc.get(True)))
    assert len(found) == 1
    assert "job `a`" in found[0]["detail"]


def test_string_shorthand_concurrency_is_clean():
    """`concurrency: name` defaults cancel-in-progress to false."""
    assert _conc(f"""
        on:
          pull_request:
          issue_comment:
        concurrency: just-a-name
        {JOBS}
    """) == []


def test_without_pull_request_it_does_not_apply():
    assert _conc(f"""
        on:
          issue_comment:
          schedule: [{{cron: "0 3 * * *"}}]
        concurrency:
          group: shared
          cancel-in-progress: true
        {JOBS}
    """) == []


def test_real_repo_has_no_shared_cancelling_group():
    """Regression guard on the repo itself, not just on fixtures."""
    found = [f for f in check_workflows(REPO_ROOT)
             if f["check"] == "CONCURRENCY_SHARED_ACROSS_TRIGGERS"]
    assert found == [], found


def test_cancel_expression_confined_to_the_colliding_trigger_is_flagged():
    """`== 'issue_comment'` mentions github.event_name and is #215 stated as a
    condition: cancellation happens ONLY on comment runs, which is precisely the
    run that must not cancel."""
    found = _conc(f"""
        on:
          pull_request:
          issue_comment:
        concurrency:
          group: r-${{{{ github.event.pull_request.number }}}}
          cancel-in-progress: ${{{{ github.event_name == 'issue_comment' }}}}
        {JOBS}
    """)
    assert [f["check"] for f in found] == ["CONCURRENCY_SHARED_ACROSS_TRIGGERS"]


def test_pull_request_target_counts_as_the_same_pr():
    found = _conc(f"""
        on:
          pull_request:
          pull_request_target:
        concurrency:
          group: r-${{{{ github.event.pull_request.number }}}}
          cancel-in-progress: true
        {JOBS}
    """)
    assert [f["check"] for f in found] == ["CONCURRENCY_SHARED_ACROSS_TRIGGERS"]


def test_excluding_only_one_of_two_colliders_is_flagged():
    """`!= 'issue_comment'` leaves pull_request_review runs cancelling."""
    found = _conc(f"""
        on:
          pull_request:
          issue_comment:
          pull_request_review:
        concurrency:
          group: r-${{{{ github.event.pull_request.number }}}}
          cancel-in-progress: ${{{{ github.event_name != 'issue_comment' }}}}
        {JOBS}
    """)
    assert [f["check"] for f in found] == ["CONCURRENCY_SHARED_ACROSS_TRIGGERS"]


def test_excluding_every_collider_is_clean():
    assert _conc(f"""
        on:
          pull_request:
          issue_comment:
          pull_request_review:
        concurrency:
          group: r-${{{{ github.event.pull_request.number }}}}
          cancel-in-progress: ${{{{ github.event_name != 'issue_comment' && github.event_name != 'pull_request_review' }}}}
        {JOBS}
    """) == []


# --- indented code blocks (#208) ---------------------------------------------
#
# The blank-line requirement is the whole safety argument: CommonMark says an
# indented code block cannot interrupt a paragraph, so requiring one keeps
# wrapped prose and list continuations in scope. Both directions are asserted
# because skipping too much here is a silent COVERAGE loss, which is worse than
# the false positive it fixes.

def test_indented_code_block_is_not_scanned(tmp_path):
    root = _repo(tmp_path)
    (root / "target.md").write_text("hi\n")
    md = root / "a.md"
    md.write_text("Example:\n\n    [x](does/not/exist.md)\n\nback to prose.\n")
    _commit(root)
    assert check_markdown_links([md], root) == []


def test_indentation_without_a_blank_line_is_still_prose(tmp_path):
    """An indented block cannot interrupt a paragraph, so this is wrapped text."""
    root = _repo(tmp_path)
    md = root / "a.md"
    md.write_text("Some prose\n    [x](does/not/exist.md)\n")
    _commit(root)
    assert [f["check"] for f in check_markdown_links([md], root)] == ["BROKEN_LINK"]


def test_list_continuation_keeps_its_links_checked(tmp_path):
    """The regression that would matter: list bodies are indented prose.

    Uses the 4-space, blank-line-separated form on purpose. The lazy two-space
    form passes for two independent reasons — under 4 columns AND no preceding
    blank line — so it pins neither condition and hid this exact bug.
    """
    root = _repo(tmp_path)
    md = root / "a.md"
    md.write_text("- item\n\n    body [x](does/not/exist.md)\n")
    _commit(root)
    assert [f["check"] for f in check_markdown_links([md], root)] == ["BROKEN_LINK"]


def test_ordered_list_continuation_keeps_its_links_checked(tmp_path):
    root = _repo(tmp_path)
    md = root / "a.md"
    md.write_text("1. step\n\n    body [x](does/not/exist.md)\n")
    _commit(root)
    assert [f["check"] for f in check_markdown_links([md], root)] == ["BROKEN_LINK"]


def test_code_block_inside_a_list_is_still_skipped():
    """Relative measurement cuts both ways: 6 spaces under `- item` IS code."""
    pairs, _ = prose_lines("- item\n\n      [x](nope.md)\n")
    assert not any("nope.md" in line for _, line in pairs)


def test_list_closes_at_the_margin_so_later_code_is_skipped():
    pairs, _ = prose_lines("- item\n\nprose\n\n    [x](nope.md)\n")
    assert not any("nope.md" in line for _, line in pairs)


def test_blank_line_inside_an_indented_block_does_not_end_it():
    pairs, _ = prose_lines("Ex:\n\n    code\n\n    [x](nope.md)\n\nend\n")
    assert not any("nope.md" in line for _, line in pairs)


def test_dedenting_ends_the_indented_block():
    pairs, _ = prose_lines("Ex:\n\n    code\n\n[x](nope.md)\n")
    assert any("nope.md" in line for _, line in pairs)


def test_indented_block_at_start_of_document():
    pairs, _ = prose_lines("    [x](nope.md)\n")
    assert not any("nope.md" in line for _, line in pairs)


def test_bullet_shaped_line_inside_a_code_block_is_still_code():
    """List tracking must not run on lines that are code.

    Updating `list_col` before the in_indented branch let a bullet-shaped line
    inside a block move the threshold, which un-skipped the rest of the block —
    reopening the exact false positive #208 exists to close.
    """
    pairs, _ = prose_lines("Example:\n\n    - bullet in code\n    [x](nope.md)\n")
    assert not any("nope.md" in line for _, line in pairs)


def test_code_block_whose_only_line_looks_like_a_bullet():
    pairs, _ = prose_lines("Example:\n\n    - [x](nope.md)\n")
    assert not any("nope.md" in line for _, line in pairs)


def test_list_body_resumes_after_a_code_block_inside_the_item():
    """The threshold must survive a block: 6 spaces is code, 4 is body again."""
    pairs, _ = prose_lines("- item\n\n      code\n\n    body [x](nope.md)\n")
    assert any("nope.md" in line for _, line in pairs)


def test_uri_schemes_are_skipped_not_treated_as_paths(tmp_path):
    """Tracking research/ brought in Edison's `artifact:` refs and broke CI.

    A scheme rule replaced the old http/https/mailto/tel allowlist, which had to
    grow every time a new one appeared.
    """
    root = _repo(tmp_path)
    md = root / "a.md"
    md.write_text(
        "[a](artifact:artifact-02)\n[b](doi:10.1/x)\n[c](https://e.com/x)\n"
        "[d](mailto:x@e.com)\n[e](#anchor)\n"
    )
    _commit(root)
    assert check_markdown_links([md], root) == []


def test_a_relative_path_is_still_checked_alongside_schemes(tmp_path):
    """The scheme rule must not swallow ordinary broken relative links."""
    root = _repo(tmp_path)
    md = root / "a.md"
    md.write_text("[ok](artifact:x)\n[bad](does/not/exist.md)\n")
    _commit(root)
    assert [f["check"] for f in check_markdown_links([md], root)] == ["BROKEN_LINK"]


# --- action pinning (#273) --------------------------------------------------

SHA = "11d5960a326750d5838078e36cf38b85af677262"


def _wf_with_uses(root, uses: str) -> None:
    (root / ".github/workflows/a.yaml").write_text(textwrap.dedent(f"""\
        name: a
        on:
          pull_request:
        jobs:
          j:
            runs-on: ubuntu-latest
            steps:
              - uses: {uses}
        """))


def test_a_sha_pinned_action_is_clean(tmp_path):
    root = _repo(tmp_path)
    _wf_with_uses(root, f"actions/checkout@{SHA} # v4.4.0")
    assert check_action_pins(root) == []


def test_a_floating_major_tag_is_flagged(tmp_path):
    root = _repo(tmp_path)
    _wf_with_uses(root, "actions/checkout@v4")
    findings = check_action_pins(root)
    assert _checks(findings) == {"ACTION_UNPINNED"}
    assert "v4" in findings[0]["detail"]
    assert findings[0]["file"].endswith(":8"), findings[0]["file"]


@pytest.mark.parametrize("ref", [
    "actions/checkout@main",            # a branch moves every push
    "actions/checkout@v4.4.0",          # a version tag is still movable
    "actions/checkout@11d5960",         # abbreviated SHAs are not immutable enough
    "actions/checkout",                 # no ref at all
])
def test_every_movable_ref_shape_is_flagged(tmp_path, ref):
    root = _repo(tmp_path)
    _wf_with_uses(root, ref)
    assert _checks(check_action_pins(root)) == {"ACTION_UNPINNED"}


@pytest.mark.parametrize("ref", [
    "./.github/actions/local-composite",   # resolves inside this repo
    "docker://alpine:3.20",                # not a GitHub Action reference
])
def test_local_and_container_uses_are_exempt(tmp_path, ref):
    root = _repo(tmp_path)
    _wf_with_uses(root, ref)
    assert check_action_pins(root) == []


def test_the_real_workflows_are_all_pinned():
    """The gate is only a gate if the tree it guards actually satisfies it."""
    assert check_action_pins(REPO_ROOT) == []


def test_a_local_composite_action_is_scanned_too(tmp_path):
    """The ./ exemption is only safe if in-repo actions are checked (#276)."""
    root = _repo(tmp_path)
    _wf_with_uses(root, f"./.github/actions/local # composite")
    composite = root / ".github/actions/local"
    composite.mkdir(parents=True)
    (composite / "action.yml").write_text(textwrap.dedent("""\
        name: local
        runs:
          using: composite
          steps:
            - uses: actions/checkout@v4
        """))
    findings = check_action_pins(root)
    assert _checks(findings) == {"ACTION_UNPINNED"}
    assert findings[0]["file"].startswith(".github/actions/local/action.yml")


def test_a_pinned_composite_action_is_clean(tmp_path):
    root = _repo(tmp_path)
    composite = root / ".github/actions/local"
    composite.mkdir(parents=True)
    (composite / "action.yml").write_text(textwrap.dedent(f"""\
        name: local
        runs:
          using: composite
          steps:
            - uses: actions/checkout@{SHA} # v4.4.0
        """))
    assert check_action_pins(root) == []
