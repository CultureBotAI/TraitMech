# Merging through the native queue

When the native merge-queue rule is active on `main`, enqueue reviewed changes
after obtaining maintainer approval. With `PR_NUMBER` and `REVIEWED_SHA` set to
the approved PR and its exact reviewed head, use:

```bash
gh pr merge "$PR_NUMBER" --repo CultureBotAI/TraitMech --auto \
  --match-head-commit "$REVIEWED_SHA"
```

The [GitHub CLI](https://cli.github.com/manual/gh_pr_merge) waits for required
checks or adds an eligible PR to the queue. The repository's queue settings
select the merge method. Keep the normal queue path; `--admin` bypasses it.

## Verify admission

Enabled auto-merge and a successful CLI exit do not prove queue membership.
Inspect the reviewed PR after the required checks finish:

```bash
gh api graphql -F number="$PR_NUMBER" -f query='
  query($number: Int!) {
    repository(owner: "CultureBotAI", name: "TraitMech") {
      mergeQueue(branch: "main") { id }
      pullRequest(number: $number) {
        id state isDraft headRefOid isInMergeQueue
        baseRef { name }
        mergeQueueEntry { position state headCommit { oid } }
      }
    }
  }'
```

If the CLI only enabled auto-merge, use the queue-only fallback below **only**
after confirming an active native queue, an open non-draft PR targeting `main`,
the exact approved `REVIEWED_SHA`, all required checks passing on that head,
clean review feedback, and `isInMergeQueue: false`. Existing maintainer approval
is still required; this fallback does not grant approval or waive any gate.

```bash
PR_ID="$(gh pr view "$PR_NUMBER" --repo CultureBotAI/TraitMech --json id --jq '.id')"
gh api graphql -f id="$PR_ID" -f head="$REVIEWED_SHA" -f query='
  mutation($id: ID!, $head: GitObjectID!) {
    enqueuePullRequest(input: {pullRequestId: $id, expectedHeadOid: $head}) {
      mergeQueueEntry {
        position state headCommit { oid }
        pullRequest { id number headRefOid isInMergeQueue }
      }
    }
  }'
```

This is the same guarded native operation used by
`scripts/auto_merge_ready_prs.py`; unlike a direct merge, it cannot bypass the
queue if the queue rule changes. Do not set `jump`, use `--admin`, delete the
branch, or repeatedly submit the mutation. Verify that the receipt identifies
the requested PR and approved head with `isInMergeQueue: true`. On an error or
uncertain response, re-read authoritative membership before taking another
action. An initially null `headCommit` means there is no combined candidate to
inspect yet, not that the job failed. Once present, inspect required checks on
that exact candidate SHA, not just the PR head.

In #1788, all PR-head checks passed but CLI auto-merge left membership false;
the guarded native mutation admitted the same head. This observation does not
establish a general CLI defect or a particular service-incident cause (#1792).

GitHub tests a combined candidate containing current `main` and preceding
queued changes. A failed candidate can remove the PR from the queue; inspect
its timeline and failed checks, repair the branch, and obtain review before
re-enqueuing. See [GitHub's merge-queue documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue).

The queue runs corpus QC, Python 3.13 tests, strict validation, taxonomy, labels, history, and vendored integrity. History presence is checked across the combined candidate, including earlier queued changes.

Confirm the PR reaches `MERGED`; an enqueue response alone does not establish
that the change landed. Verify the actual landed tree with the maintained
`scripts/verify_merge_integrity.py` against the merge commit's actual parent
before branch cleanup. This guide does not enable repository rules or grant
merge approval.
