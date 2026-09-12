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

GitHub tests a combined candidate containing current `main` and preceding
queued changes. A failed candidate can remove the PR from the queue; inspect
its timeline and failed checks, repair the branch, and obtain review before
re-enqueuing. See [GitHub's merge-queue documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue).

The queue runs corpus QC, Python 3.13 tests, strict validation, taxonomy, labels, history, and vendored integrity. History presence is checked across the combined candidate, including earlier queued changes.

Confirm the PR reaches `MERGED`; an enqueue response alone does not establish
that the change landed. This guide does not enable repository rules or grant
merge approval.
