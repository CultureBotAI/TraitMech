# Workflow conventions

Rules for `.github/workflows/`, each one written down because it was learned the
expensive way. Every entry cites the incident.

> **Scope.** This is TraitMech's copy. #217 argues this knowledge is fleet-wide
> and belongs in CultureMech or `culturebotai-claw` with the spokes linking to
> it, rather than copied four times and drifting — see #209 for how copying
> goes. That consolidation is still open; this page exists so the pinning policy
> settled in #224 has somewhere to live that is not a comment in one workflow.

## Action pinning

**Every action is pinned to a full commit SHA, with its version in a trailing
comment.** No floating tags, including GitHub's own `actions/*`.

```yaml
- uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4.4.0
```

A tag is mutable: `@v4` is a pointer its owner can move, so a compromised or
merely careless upstream reaches CI with repo credentials and no diff on our
side. A SHA is not a pointer.

`.github/dependabot.yml` is **part of this policy, not housekeeping.** #224
rejected pinning-everything precisely because pins rot silently, which is worse
than floating tags — a floating `@v4` at least receives security patches, while
a forgotten SHA is frozen at whatever shipped on pin day. Dependabot updates the
SHA and the trailing comment together. Removing that file re-opens the hole the
pinning was adopted to close.

Why not the cheaper policy of pinning only the risky actions? That is what the
repo did before #224, with `anthropics/claude-code-action` SHA-pinned because it
reads untrusted PR content while holding an OAuth token and a reviewer App
token, and everything else floating. It was defensible, but it required every
future author to correctly classify a new action as risky-or-not, and it was
discoverable only by opening the one file that happened to show it. A single
rule needs no judgement call.

**Enforced, not merely written down.** `just pr-sanity` fails on any `uses:`
whose ref is not a 40-character SHA (`ACTION_UNPINNED`), because this repo's own
rule is that a convention repeated becomes a gate — and the one pin that existed
before #272 was already commented with a version its SHA did not match, one for
one (#273). The check verifies the SHA only; whether the trailing comment still
names the right tag needs network and is Dependabot's job.

`astral-sh/setup-uv` also forced the question: it **stopped publishing floating
major tags after v7**, so `@v8` will not exist and the next upgrade has to name
a version or a SHA regardless (#224).

## Concurrency

**Cancellation is for superseding, not deduplication.** Key a group across runs
only when you genuinely want one to supersede another — in practice, pushes to a
single PR. Give everything else a unique key (`github.run_id`) rather than
reasoning about whether it will collide.

**Never cancel on `main`.** Cancelling an in-progress run there leaves the
earlier commit unverified. The idiom in use:

```yaml
concurrency:
  group: pr-sanity-${{ github.ref }}
  cancel-in-progress: ${{ github.event_name == 'pull_request' }}
```

**Do not reason about whether a skipped job acquires its group.** GitHub
documents `jobs.<job_id>.concurrency` but never says whether a job skipped by a
false `if:` takes the group. Make the key structurally distinct instead of
depending on either answer.

Three separate incidents, three separate diagnoses: #199 (`vendored-sync` could
skip verifying an intermediate `main` commit), #196's review (group scoped too
broadly, narrowed to PRs), and #215 (`claude-code-review` cancelled *itself*,
because its own progress comment fired `issue_comment` into the shared group).
`pr-sanity` now enforces the rule rather than only documenting it (#218, #225).

## Triggers that run from the default branch

**`issue_comment` and `schedule` workflows execute the default branch's copy of
the file**, not the branch under test. A workflow can be correct on its feature
branch and broken the instant it merges, with no pre-merge signal. That is
exactly how #215 got in.

## `paths:` filters

**A `paths:` filter is a promise that the job does not need the files it
excludes.** When a job grows a new input, the filter has to grow with it.

This has now happened four times — #184, #200, #250 (where `qc` gained
`audit-research-artifacts` reading `research/**` while the filter still listed
only the old inputs, so the gate could not fire on the artifact-only PRs it was
built for), and `conf/`, where both ratchet baselines lived outside the filter so
*weakening* one did not re-run `qc`.

**Enforced now.** `just audit-qc-paths` derives what the `qc` chain reads —
justfile chain → recipes → scripts → path constants, parsed with `ast` — and
fails on any top-level directory the filter omits (#252). It found the `conf/`
instance on its first run. It also fails when it cannot inspect anything, since
a gate that passes while blind is the failure mode the section below is about.

## Verify the check ran, not that it was green

#182, #184 and #215 were all *green because nothing evaluated them*. A passing
job that silently skipped its own verification is worse than a failing one,
because it reads as evidence.

When adding or changing a gate, confirm it can fail: introduce the defect it
targets, watch it exit non-zero, then remove it. Several audits in this repo
carry a canary note in their PR for that reason — see `audit-snippets` (#247)
and the malformed-CURIE scan in `trait-graph-sweep --verify` (#242), both of
which landed against corpora that were already clean and so could have reported
zero forever without anyone noticing.
