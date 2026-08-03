# /goal — review, prioritize, and work the open issues

Run the open-issue backlog end to end: reconcile it against reality, prioritize
it with PR dependencies in mind, then take items through
**branch → implement → PR → review → issues → address → merge → delete**.

Pause and ask when a decision is the user's to make. Do not guess on those.

---

## Phase 1 — Reconcile before recommending

**Never prioritize from issue titles.** Two targets in one session turned out to
be already merged; the branch named in the request had shipped weeks earlier.

```bash
gh issue list --state open --limit 40 --json number,title,createdAt
gh pr list --state open  --json number,title,headRefName,mergeable
git log --oneline -20
```

For each open issue, establish the *current* state before ranking it:

- **Does its deliverable already exist?** Check the code, not the issue body.
  A squash-merged branch has a different SHA than anything in `main`, so
  "not an ancestor" does not mean "not merged" — compare **content**.
- **Has it drifted?** #203 was filed at "3 versions across 6 workflows" and had
  become 3 across 7 by the time it was worked.
- **Is it partly done?** #198's spoke half had shipped in sibling repos while
  the hub half remained. Scope it down; do not close it whole.
- **Is it blocked elsewhere?** #193's fix lives in `culturebotai-claw`, not
  here. That is a different repo — see *When to pause*.

Say plainly what is already done, what is blocked, and what is genuinely
actionable. Reconciling is the deliverable of this phase even if nothing is
picked up.

## Phase 2 — Prioritize, with dependencies

Rank by **what unblocks the most downstream work**, not by issue age or size.

Dependencies that actually matter here:

- **Fix the thing that breaks review first.** While `claude-code-review` was
  self-cancelling, no PR got reviewed — every other PR was worth less until
  that merged.
- **Gate before queue.** A gate that makes a work-queue trustworthy (#214)
  comes before the loop that consumes the queue.
- **Same-file PRs serialize.** Two open PRs touching `justfile` or `qc.yaml`
  means the second rebases onto the first. Merge in dependency order and
  rebase — never assume a clean auto-merge because GitHub says `MERGEABLE`.
- **Prerequisite → dependent in one direction only.** If A must land before B,
  do not open B until A merges, or open it and say so in the description.

State the ordering and *why*, then recommend one. Offer the alternatives.

## Phase 3 — The cycle, per item

Follow this in order. Do not skip the review pass.

1. **Branch before the first edit.** Never commit to `main` — no exceptions for
   docs or "obviously safe" changes.
2. **Implement.** Verify claims against the repo rather than reasoning about
   them: run the query, check the tree, diff the file.
3. **`just qc` and the tests must pass locally** before pushing.
4. **Commit and push** with an explicit refspec:
   `git push origin HEAD:refs/heads/<branch>`.
5. **Open the PR.** Describe what was *checked*, not just what was changed, and
   state what remains unverified.
6. **Wait for CI and the review.** Confirm the check actually *ran* — a green
   check that skipped is this repo's most repeated failure (#182, #184, #215).
7. **Review it yourself, adversarially** — a separate pass, not a restatement
   of what you just wrote. Reviews are read-only.
8. **File every finding as an issue**, including ones you then fix.
9. **Address what belongs in this PR**; leave the rest filed and say which is
   which and why. "As needed" is a judgement, not a rubber stamp.
10. **Merge only with the user's go-ahead**, then delete the branch.
11. **Sync `main`** and confirm the change is actually there.

## Phase 4 — After merging

- `git fetch --prune`, reset local `main`, confirm the merged content is on
  `main` by inspecting it — not by trusting the merge message.
- Squash-merge means `git branch -d` refuses (different SHA). Verify the
  content landed, then `-D`.
- Re-run Phase 1 briefly: merging usually closes issues and files new ones.

---

## When to pause and ask

Ask a direct question, with a recommendation, when:

- **The named target is already done.** Do not fabricate an empty PR.
- **A choice is the user's**: which version to standardise on, whether to spend
  money (a paid re-run), whether generated `.md` should count as curation
  targets, how wide a refactor should go.
- **The work needs a sibling repo.** `CultureMech`, `MediaIngredientMech`,
  `CommunityMech`, `culturebotai-claw` are separate repos with their own PR
  flow. Do not edit them unprompted.
- **Something outside the task appears** — uncommitted changes you did not
  make, another session's branch checked out, a concurrent edit. Stop, report,
  touch nothing.
- **The fix is much larger than the issue implies.** #228 started as "one stale
  page" and was 119 stale pages plus a nondeterministic generator.

Do not pause for routine judgement calls. Make them and say what you assumed.

---

## Repo-specific gates

- `just qc` = `pr-sanity validate-strict audit-schema audit-writers
  audit-proposals audit-graphs audit-justfile-paths audit-derived-reports`.
- **Derived artifacts are gated.** Changing `data/traits/**` or `mappings/**`
  invalidates `reports/*_grounding_residual.tsv` and
  `reports/causal_graph_audit.tsv`; regenerate and commit them (#214, #223).
- **The causal-graph ratchet** (`conf/causal_graph_audit_baseline.tsv`) freezes
  known findings. Regenerate with `--write-baseline` only when the change is
  intended, and make the delta explainable in the commit message.
- **Trait-record edits want provenance both ways.** A change under
  `data/traits/` needs an in-file `curation_history` entry (reuse an existing
  `action` value) *and* a record under `history/` via `just new-history`.
  `just validate-history` must pass.
- **Never `@`-mention** anyone in a commit, PR, issue, or comment.

## Traps that have cost real time here

- **`push.default = matching`** pushes *every* matching branch. Always use an
  explicit refspec; a bare `--force-with-lease` once rewound `main`.
- **Three-dot vs two-dot diffs.** A PR's contents are `main...HEAD`. A branch
  merely *behind* `main` shows alarming reversions under `main..HEAD` and
  reverts nothing when merged. Settle it with
  `git merge-tree --write-tree main HEAD`.
- **`set -euo pipefail` in a `just` recipe**: `diff | sed` exits non-zero on a
  difference and aborts the recipe mid-loop. Guard with `|| true`.
- **YAML plain scalars**: a space followed by `#` starts a comment, so `#220`
  in an unquoted value truncates it. Quote such strings.
- **GitHub concurrency is evaluated before a job's `if:`**, so a run that skips
  every job still cancels what is in its group.
- **Generated pages/dashboards embed timestamps**, so regenerating them churns
  hundreds of files. Do not sweep that into an unrelated PR (#193, #228).
