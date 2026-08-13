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
a version or a SHA regardless (#224). Still true as of the v9.0.0 bump (#280) —
re-checked against the tag list, which floats `v2`..`v7` and nothing above. The
gap between "newest floating major tag" (v7) and "newest release" (v9.x) is now
two majors wide, which is exactly why pins here name a SHA and never a tag.

**Never pin a version number into prose.** `pr-shepherd.yml` carried a comment
reading "v7 matches every other workflow here and is the newest major tag" three
lines above its `uses:`. Dependabot bumps the SHA and the trailing `#` comment;
it never touches surrounding prose, so that sentence went stale the moment
v9.0.0 landed, and `ACTION_UNPINNED` cannot see it — it checks the SHA only.
Write the *invariant* ("this pin matches every other setup-uv call site here")
rather than the value.

**`setup-uv` cache pruning: the new default is accepted deliberately.** v9.0.0's
breaking change is `prune-cache` defaulting to `false`, to ease load on PyPI.
Upstream warns it can mean more Actions cache usage. Taken here rather than
pinned back to `true`, because: this repo is public, so Actions cache and
minutes are unbilled; and all eight call sites set `enable-cache: true` with no
`cache-suffix`, so they share one key rather than filling eight entries against
the 10 GB per-repo LRU limit. Revisit if cache misses start showing up — they
degrade quietly and will not appear as a red check.

## Every workflow points at this page

The first line of every `.github/workflows/*.y{a,}ml` is:

```yaml
# Conventions for this directory: docs/WORKFLOW_CONVENTIONS.md
```

This page consolidated comment blocks that had been living in individual
workflow files — and then nothing linked to it, so it was strictly *less*
discoverable than what it replaced. That is the same failure #272 argued
against when it retired the old pinning policy for being "discoverable only by
opening the one file that happened to show it" (#275).

**Enforced, not merely written down.** `just pr-sanity` fails with
`MISSING_CONVENTIONS_POINTER` on any workflow whose first line is not the
pointer. A gate rather than a convention because 5 of the 9 workflows had
already drifted without one by the time anyone checked.

Where a workflow keeps its own explanatory comment block — several do, and
should — the pointer makes the two read together rather than as competing
copies.

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

## Dependabot runs have no secrets — skip, do not fail

A `pull_request` run whose `github.actor` is `dependabot[bot]` gets a
**read-only `GITHUB_TOKEN`** and **no access to Actions secrets**. Any job
needing either dies at its first step that consumes one; `claude-review` died on
`actions/create-github-app-token` with `Input required and not supplied: app-id`
on all five PRs `.github/dependabot.yml` opened (#293). The read-only-token half
is worth remembering separately from the secrets half: a future workflow that
needs write scope on a `pull_request` run may hit the same wall without using a
secret at all. Check before assuming either way.

That failure is not a signal about the bump. It is a permanent red on the class
of PR *least* likely to be read carefully — a red that trains people to ignore
reds, which is the failure in "Verify the check ran" above wearing the other
colour.

Gate such jobs on `github.actor != 'dependabot[bot]'`. Gate on `github.actor`,
not on `github.event.pull_request.user.login`: actor is what determines whether
secrets exist. A human pushing to a Dependabot branch correctly re-enables the
job, whereas the PR author stays `dependabot[bot]` forever. **Re-running does
not help** — GitHub keeps the restrictions "even if the workflow is re-run by a
different actor", so "Re-run failed jobs" is not a workaround.

Be honest about what that re-enabling costs. One commit from anyone with write
access makes PR head's workflow file — carrying the bumped, unreviewed action
SHAs — run holding both tokens. Nothing structural prevents it; what does is
trust in who holds write access, plus the fork guard for everyone who doesn't.
That is an acceptable place to land, but it is a trust boundary rather than a
mechanism, and a doc written to be copied should say which it is.

**A skipped job is not an absent check.** GitHub leaves checks *Pending* only
when the **workflow** is filtered out by `paths:`/branch/commit-message; a
**job** skipped by its own `if:` completes with conclusion `skipped` (grey).
Verify this kind of change by looking for *grey instead of red*, not for the
check disappearing — expecting it to vanish reads a working change as a failure.

Branch protection accepts `skipped` as satisfying a required check. Treat that
as an **accepted tradeoff, not a safety property**: if such a job is ever made
required, this makes a required check auto-satisfy on the one PR class that got
no review — precisely the false-green the section above warns about. It is
tolerable here because of what still runs — but be precise about that, because
"the other gates cover it" is weaker than it sounds. Most workflows carry
`paths:` filters naming only their own file, so how many gates run on a
Dependabot PR is a function of *which action got bumped*: observed coverage
across #277-#281 ranged from **two** functional gates (#277, bumping
`claude-code-action`, which appears in only two workflow files) to **seven**
(#281, bumping `actions/checkout`, which appears in nearly all of them).

The floor is `pr-sanity` and `vendored-sync` — the only two *functional gates*
with no `paths:` filter. `claude-code-review.yml` used to be unfiltered too but
never counted toward the floor (since #307: its only job is gated on an `if:`,
so it can run nothing on a Dependabot PR), and as of 2026-08-12 it no longer
runs on `pull_request` at all — automatic review is off while
`CLAUDE_CODE_OAUTH_TOKEN` has no quota, so it was turning every PR red without
saying anything about the PR. `/review` and manual dispatch still work. That floor is the reassuring part:
**`pr-sanity` is the gate that enforces SHA pinning** (see "Action pinning"
above), so the check that actually validates *this* class of change is exactly
the one immune to the filters.
Everything above two gates is a bonus that depends on the bump's blast radius.
State it that way wherever you copy this pattern; "seven gates cover it" would
be false on a #277-shaped PR.

This used to create a caveat: `NO_UNFILTERED_CI` decided "unfiltered" from a
workflow's `on:` block alone, so a workflow gated this way still counted toward
the floor while running on nothing. **Fixed in #307** — a workflow whose every
job carries an `if:` no longer counts, and if that leaves nothing, the failure
names it rather than reporting a bare "no unfiltered workflow", because those
two need different fixes. A job also counts as gated when every job it `needs:`
is gated — GitHub skips a dependent when its dependency skips, so an ungated job
hanging off a gated one is not guaranteed to run either. The check never
evaluates the `if:` expression; "has an `if:`" is the conservative reading, and
it can only shrink the counted set.

Note the separate hazard that remains: if `pr-sanity` alone gained a `paths:`
filter, `vendored-sync` would keep `NO_UNFILTERED_CI` green while the
SHA-pinning gate stopped covering dependency PRs. That is a coverage loss, not
an invariant failure, and no check catches it.

Skipping does not make these PRs unreviewable. Comment `/review`, or use
`workflow_dispatch` with the PR number. Neither is Dependabot-triggered, so both
get secrets. `/review` has a second advantage worth knowing: `issue_comment`
runs execute the **default branch's** copy of the workflow (see "Triggers that
run from the default branch" above), so it uses `main`'s pinned action SHAs
rather than the bumped ones under review.

Two known ways exist to give a Dependabot run secrets. **Do not enumerate them
as a closed set** — the list is not something a conventions doc can guarantee,
and an absolute is the one shape of claim that gets copied without re-deriving.
Reject each on its own merits instead.

**`pull_request_target` — live, not inert.** It is tempting to think Dependabot's
restrictions neutralise it. They do not, in the ordinary case: GitHub's
read-only-token/no-secrets rule applies when the pull request's **base ref** was
created by Dependabot — a Dependabot PR stacked on another Dependabot branch. A
Dependabot PR onto `main` under `pull_request_target` gets a writable token and
the Actions secrets, which is why `pull_request_target` + Dependabot is a named
privilege-escalation pattern rather than a dead end.

The three quoted fragments above — the read-only/no-secrets pair, the base-ref
condition, and "even if the workflow is re-run by a different actor" — are from
[Dependabot on GitHub Actions](https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-on-actions).
Re-read it rather than trusting this summary: the claim in this section has been
reversed twice already, which is why the refusal below is built to stand without
it.

Refuse it for the reason that actually holds: a job like `claude-review` runs
`gh pr checkout` and then `uv sync` and the branch's `just` recipes while
holding the OAuth and reviewer App tokens. Under `pull_request_target` that is
executing PR-controlled code with secrets attached — the hazard the "Refuse fork
PRs" guard exists to prevent (#212), through a different door.

**Dependabot secrets.** A separate store the `secrets` context resolves against
on these runs, which is why `app-id` arrived *empty* rather than denied.
Populating it would make the job run. Don't: on `pull_request` the executing
workflow comes from the PR itself, and where `dependabot.yml` enables the
`github-actions` ecosystem — as this repo's does — a Dependabot PR's entire
content is a change to which action SHAs the job runs. Populating Dependabot
secrets hands those credentials to an unreviewed, freshly-bumped action.

The same caution applies to the `/review` escape hatch the moment a `uv` or
`pip` ecosystem is added to `dependabot.yml`: that job runs `uv sync` and the
branch's `just` recipes while holding the OAuth and App tokens. Today the branch
diff is confined to `.github/workflows/**`, which those commands never execute,
so the exposure is theoretical — but it is the same hazard class, and it stops
being theoretical then.
