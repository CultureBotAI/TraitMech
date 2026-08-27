---
name: review-open-issues
description: Sweep and triage TraitMech's complete open GitHub issue queue — not just NEXT_TASKS.md — using current schema, curated-record, grounding, provenance, and derived-artifact evidence. Fetches every open issue with its comments, places each at the earliest affected curation stage, checks each claim against the live repository for staleness, flags duplicates, and assigns a priority tier plus a separate cost class. Produces a ranked, dependency-ordered report. Use for full backlog triage or deciding what is genuinely urgent; do not use as permission to close issues, run paid research, apply migrations, or implement fixes.
category: workflow
requires_database: false
requires_internet: true
version: 2.0.0
---

# Review & Prioritize Open Issues

Produce a complete, dependency-aware triage of TraitMech's open issues. The
issue queue and `NEXT_TASKS.md` are different surfaces: sweep the queue itself,
then test every claim against the current repository and the authoritative
curation contracts.

This is a **read-only review by default**. It does not implement fixes, apply
migrations, launch paid research, close or edit issues, change labels, or
maintain a tracker unless the user separately authorizes that exact mutation.

**When to use**: the user asks to review, triage, or prioritize issues or the
backlog; asks what is genuinely urgent; or a review pass has just filed a batch
of issues that need sorting.

**When NOT to use**: `NEXT_TASKS.md` upkeep or picking the next unit of work to
implement — that is `next-tasks`, whose Step 1 runs `gh issue list --limit 30`
merely as *context* and never assesses issue validity. This skill is the deep
pass, expensive enough that it should not run on every "what's next" question.

## Sources of truth

Use these before relying on an issue title or an old planning document:

- `CLAUDE.md` — the safe mutation contract and where work should be routed;
- `docs/CURATION_PLAYBOOK.md` and `docs/GROUNDING_POLICY.md` — what a
  defensible record, grounding, and exemplar look like;
- `history/README.md` — what provenance a change owes (one record per change,
  per *migration* for a bulk edit), and how strictly it is enforced;
- `DO_NOT_WORK.md` — records excluded from agentic curation entirely;
- the `justfile` — which gates exist, which run in `just qc`, and which are
  deliberately excluded (network-dependent ones like `audit-uniprot`);
- `conf/*_baseline.tsv` — what a ratchet currently freezes, so "the audit is
  green" can be read correctly;
- current schema, records, tests, CI workflows, and committed reports for
  actual behavior.

`NEXT_TASKS.md` is a curated claim about the backlog, not the backlog. Treat
issue bodies and titles the same way. **Read comments**: this repository records
corrections, withdrawals, and narrowed residual scope there, so a body-only
fetch systematically overstates what is open. A merged PR is evidence only after
its code and acceptance criteria are checked.

Per `CLAUDE.md`, never carry a count, coverage percentage, or identifier range
from prose into the report. Derive it live.

## Workflow

### 1. Fetch the entire queue

Confirm the repository, the true count, the labels, and the full queue. Never
silently accept `gh`'s default 30-item limit.

```bash
gh repo view --json nameWithOwner,url,defaultBranchRef
gh issue list --state open --limit 5000 --json number | jq length
gh issue list --state open --limit 5000 \
  --json number,title,body,comments,labels,createdAt,updatedAt,author
gh label list --limit 200
```

A high `--limit` is safe: `gh` auto-paginates through the API, so one call
returns the full set rather than a first page. Omitting `--limit` silently caps
at 30, which is how a sweep ends up sampling without saying so. Confirm the
count first, then fetch comfortably above it.

State the exact number reviewed and whether coverage was complete. Read every
issue body and its comments; for a long queue, inspect related groups in
parallel but preserve one disposition per issue. For a single ambiguous issue,
`gh issue view <N> --comments` is the quickest way to see the thread.

**Labels carry meaning here**, and the label descriptions are authoritative —
re-read them with `gh label list --limit 200 --json name,description` rather
than trusting this paragraph. As written today, `agent-ok` says "Opt-in: an
agent may pick this up. Absence means hands off," and `needs-human` says "Hard
stop for agents. Ontology minting, deletions, schema changes." So an unlabeled
issue is *not* pre-authorized for autonomous pickup. That is a statement about
standing permission, not about triage: this skill ranks every open issue
regardless of label, and an explicit user instruction to work on one is its own
authorization. Report each issue's labels so the reader can see which are
pre-cleared. The `*_effort` labels are the author's estimate and are tied to
model routing, so treat them as a hint, not a measurement.

### 2. Place each issue on the curation pipeline before assigning rank

```text
upstream ontology release (METPO, GO, ChEBI, NCBITaxon, UniProt)
  -> LinkML schema (src/traitmech/schema/traitmech.yaml)
  -> curated TraitRecords (data/traits/**)
  -> node/predicate groundings, causal-graph structure, exemplars
  -> audits, ratchet baselines, and the qc gate chain
  -> derived reports, dashboards, and rendered pages
  -> outward claims (README, policy statistics, proposals, KG-Microbe consumers)
```

An upstream identity or correctness problem invalidates everything downstream:
a wrong grounding propagates into every report, page, and downstream KG that
reads it. Recommend fixing or auditing the root problem before polishing
downstream output or commissioning new research.

**Group, then dedupe.** Issues filed by one review pass often describe the same
root cause from different angles. Group by a shared PR or commit reference, the
same file or function named, or a near-identical failure scenario. Note the
group explicitly and keep every issue number visible — never silently merge
them, because closing a duplicate is a decision for a human to make deliberately
rather than one to have hidden inside a ranking.

For each issue, record when applicable:

- pipeline stage and owning repository (several defects belong to METPO,
  CultureMech, or claw, not here);
- affected records, graphs, groundings, or reports, by identifier;
- schema, predicate, node-type, domain, and range assumptions;
- counts and coverage figures **derived live**, with the command used;
- prerequisites, blockers, duplicates, and superseding issues;
- the cheapest decisive evidence and the acceptance test;
- cost class: read-only audit, single-record curation, corpus-wide migration,
  derived-artifact regeneration, or **paid research call**.

### 3. Check current reality and staleness

For each issue or group representative:

- Search exact issue references in history:

  ```bash
  git log --all --oneline --perl-regexp --grep '#<N>\b'
  gh pr list --state merged --search '<N>' --limit 100
  ```

  The word boundary is required: `#48` must not match `#480`. GitHub search
  matches the number anywhere in indexed text, so every hit is a lead — open it
  and confirm it actually resolves the issue before citing it.

- Use `rg`/`grep` to confirm that named files, functions, recipes, flags, and
  CURIEs still exist and behave as described. Inspect tests as well as
  implementation: a claim can be true of the code and false of its gate.
- Compare acceptance criteria against the merged change. If only part is fixed,
  keep the issue open with a narrowed residual; do not recommend closure merely
  because a related PR merged.
- Distinguish an observation from its action issue. Prefer closing a fully
  recorded observation as superseded when a separate open issue owns the only
  remaining work.
- Verify artifacts by content and provenance, not filenames or prose. A
  coverage number without the command that produced it, a report without its
  regeneration recipe, or an exemplar without a resolvable accession, taxon,
  and citation is not evidence.

### 4. Apply curation stop-the-line checks

Treat these as P0 when live or outward-facing:

- a grounding CURIE whose concept is not the node's concept — the
  right-sounding-synonym failure recorded in #391 and #402 and repaired again
  in PR #405;
- a fabricated or mismatched exemplar: an accession, NCBITaxon id, or DOI that
  does not resolve, or resolves to a different organism, protein, or paper;
- a note or claim that overstates what its cited source measured — a
  localization percentage restated as a count, an overexpression phenotype as a
  clean loss of function, a heterologous-host result as in-situ (#557);
- evidence loss: nodes, edges, or citations removed without provenance;
- a mutation that bypassed `write_validated_trait`/closed-schema validation, or
  shipped without its per-record `curation_history` event or repository history
  record (#517/#518);
- a hand-edited derived artifact made to satisfy a freshness check;
- **a gate that cannot fail**: an audit flag that ignores its own error class
  (#522), or a CI `paths:` filter narrower than what the job reads
  (#184/#200/#250/#252/#554). A third form has no issue behind it yet but the
  same shape: a ratchet whose baseline has absorbed a real regression — the
  files under `conf/*_baseline.tsv` freeze known findings by design, so read
  the baseline before reading a green audit as an all-clear. These are P0
  because they silently disable the detection everything else relies on;
- an edit to a record listed in `DO_NOT_WORK.md`;
- a paid research call or batch that would run without approval or without a
  verified canary.

Prefer the maintained checker over a hand-rolled one: `just validate-strict`
for closed-schema validity, `just audit-graphs` for graph structure, and
`just audit-canonical-examples --ncbi-api` for exemplar taxonomy. `just qc`
runs the offline gate chain, but it is **not** everything: `validate-history`,
`validate-products`, `audit-canonical-examples`, and `audit-uniprot` are all
outside it, the last two deliberately because they need the network. Read the
`qc:` dependency list before calling any claim "covered by qc", and say so
explicitly when a finding rests on a gate that is not in it.

### 5. Assign priority, then order by readiness and cost

Use priority for consequence and a separate cost annotation for ordering.

- **P0 — stop the line.** Wrong curated science that is live, corpus corruption,
  evidence or provenance loss, an outward-facing claim the data does not
  support, a disabled or unfailable gate, or a blocker in front of an already
  planned expensive step. Also any security-relevant defect — command
  injection, secret or token exposure, a workflow that executes untrusted
  input — which this repo is exposed to through generated commands, `gh`
  automation, and CI, not through a served application.
- **P1 — important and schedulable.** Real correctness, reproducibility,
  provenance, or coverage gaps; missing guards for a likely workflow;
  test-coverage gaps on safety-critical paths.
- **P2 — low-risk or historical.** Documentation drift, stale comments,
  refactors, theoretical edge cases, optional audits.
- **CLOSE/UPDATE.** Fixed, superseded, duplicate, no longer applicable, or a
  title materially broader than the remaining work. Cite the exact commit, PR,
  code location, or comment supporting the disposition.

Calibrate P0 sparingly. Then order within and across tiers:

1. upstream unblockers before downstream consumers;
2. restore a disabled gate before burning down what it should have caught;
3. **apply research already paid for before commissioning new research.**
   `research/` is tracked precisely because it was expensive, and a report is
   an input, not curated content — so check what is already on disk against
   what the records actually carry before treating "research this trait" as the
   next action. Measure it rather than assuming either way: compare the
   artifacts under `research/traits/` with the records that cite them, and run
   `just audit-unapplied-groundings` for the grounding half;
4. read-only and offline falsifiers before paid or network-dependent work;
5. provenance and validation readiness before a bulk tranche, so the tranche
   does not need a backfill afterwards;
6. combine issues only when one patch or one measured run genuinely satisfies
   each issue's acceptance criteria.

Do not prioritize by age, by sunk cost, or by a `P0` string in a stale title.

### 6. Report

Return a compact report with:

1. coverage: repository, timestamp, number reviewed, completeness;
2. the top 2–3 next actions and why they unblock later work;
3. a dependency-ordered P0/P1/P2 table: issue number, current status, evidence,
   blockers, cost class, next acceptance test;
4. CLOSE/UPDATE candidates with specific evidence;
5. unresolved evidence gaps and cross-repository ownership;
6. a short sequence showing which costly work must wait, and on what.

Call out old issues explicitly rather than silently dropping them; a
six-month-old open issue is itself a signal. Separate measured findings, code
inspection, inference, and proposed-but-untested work.

### 7. Act only when asked

A general "yes, go ahead" is not blanket approval for an unattended loop.

- **Closing issues**: confirm the specific numbers first, then
  `gh issue close <N> --comment "<evidence>"` one at a time, each with the
  Step 3 evidence. Never bulk-close: an agent closing a live issue because it
  *looks* stale is worse than noise in the queue.
- **Tracker issue** (the `[P0-P2 tracker]` pattern used elsewhere in this org,
  e.g. CommunityMech#669): the search is authoritative, not this note —
  `gh issue list --search "tracker" --state open`. Update one in place if it
  exists rather than opening a second. Create one only if asked, using the
  Step 6 ranking as its body and linking every tracked issue number.

## Conventions this skill enforces

- **Full-queue coverage, not first-page sampling.** State exactly how many
  issues were reviewed and whether coverage was complete.
- **Evidence over vibes.** Every CLOSE/UPDATE/duplicate recommendation cites a
  specific commit, PR, artifact, or code location — never "this looks done."
- **P0 is rare.** If more than ~10% of the queue lands P0, the calibration is
  wrong; recheck. A stale `P0:` string in a title is not evidence.
- **Titles are claims and they drift.** Issues get retitled mid-life, including
  to `[WITHDRAWN/RESOLVED]`, while staying open. Re-read titles at report time
  rather than trusting the ones fetched at the start of the sweep.
- **The queue moves during the sweep.** Parallel agents and PRs resolve issues
  while triage is in progress, and `main` can advance under you. Re-check the
  open set immediately before reporting, and say so if it changed.
- **Read-only by default.** Ranking happens automatically; every mutation
  requires explicit confirmation.

## Measurement discipline

The recurring failure here is not misreading evidence, it is mismeasuring it.
Before citing any of the following, confirm how it was obtained:

- **Exit codes through pipes.** `just validate-history 2>&1 | tail -1 && next`
  reports the pipeline's status, not the recipe's, so a failing gate reads as
  green and the `&&` still fires. Use `cmd >/tmp/o 2>/tmp/e; echo $?`, or
  `${PIPESTATUS[0]}`. Demonstrate it rather than taking it on faith: any
  command that exits non-zero here reports 0 once `| tail -1` is appended.
- **Freshness audits use two comparison bases, and the stricter one is the
  majority.** `just audit-derived-reports` diffs some reports against the
  working tree, where regenerating clears the failure at once, and others
  against **`git show HEAD:`**, where a regenerated-but-uncommitted report
  still reports STALE until you commit. The justfile states the rule at the
  recipe's head: the basis "follow[s] from whether anything else in the run
  mutates the file" — comparing a file this same `qc` run already refreshed
  would always pass while a stale committed copy sailed through (#223). Do not
  guess which case a report is in, and do not trust a list in prose; measure it:

  ```bash
  grep -n 'git show "HEAD:reports/' justfile   # the strict set
  grep -n 'diff -q "reports/' justfile         # the working-tree set
  ```

  Note the rule is descriptive, not predictive: at least one report is compared
  strictly without any `qc` step rewriting it, so the grep is the authority.
- **Two-dot vs three-dot diffs.** When `main` has advanced,
  `git diff origin/main..HEAD` shows *main's* newer commits reversed and
  attributes them to the branch. Use `origin/main...HEAD` or an explicit
  merge-base for "what this branch changed."
- **Run repository tooling through `uv`.** `pytest` under the system
  interpreter fails at import with `ModuleNotFoundError: traitmech`, which is
  an environment artifact, not a defect. Use `uv run pytest`.
- **Truncated output.** A `grep` piped through `head`, or a tool that elides
  long lines, yields a number that looks measured and is not — and provenance
  strings are written from those numbers. Count with `-c`, or read the whole
  result, before quoting one.
- **Ignore rules tested by shape.** A regex or `case` check against a
  `.gitignore` pattern tests what the pattern looks like;
  `git check-ignore --no-index <path>` tests what it does. Only the second is
  evidence, and `CLAUDE.md` asks for exactly this before assuming an
  artifact's tracking policy.
- **YAML plain scalars.** A space followed by `#` starts a comment mid-scalar
  and can silently break a block mapping. Prefer wording that avoids `#N`
  inside unquoted prose, and re-parse the file after editing.
- **Backticks in a double-quoted `-m`.** `git commit -m "...`cmd`..."` executes
  the backticked text. Write commit messages and issue bodies containing shell
  examples via `-F <file>` or a quoted heredoc (`<<'EOF'`), then read the result
  back before pushing.
- **Green CI is scoped.** A job with a `paths:` filter did not necessarily run.
  Confirm the check actually executed on the commit you are citing.

## Notes & limitations

- `gh issue list --json` omits `comments` unless explicitly requested. This
  repository records corrections and narrowed residual scope in comments, so a
  body-only fetch will overstate what is open.
- `gh pr list --search "<N>"` matches the number anywhere in indexed text and
  returns unrelated PRs; `git log --grep '#<N>'` needs the `\b` anchor.
- An issue may be fully addressed in code while its acceptance criteria are
  not. Partial fixes stay open with a narrowed residual; say which part is done.
- Cross-repo defects are common in this org (METPO, CultureMech, claw,
  MicroGrowLink). Note where a fix should propagate, but do not open issues in
  sibling repos without being asked.
- When an issue's residual asks for an artifact the repository records as
  absent, recovery may be impossible; recommend superseding it rather than
  leaving it open indefinitely.
- No @-mentions in issue comments or reports without explicit per-mention
  authorization (standing rule).

## Mutation boundary

Do not close, comment on, relabel, retitle, or create issues or trackers during
the review. If the user later asks to act, present the exact issue numbers and
the proposed mutation first, then apply them one at a time with cited evidence.

Do not run a migration with `--apply`, regenerate tracked artifacts, or edit
curated records as part of triage. A recommended command is a proposal.

**Do not launch paid research.** `research/` is tracked provenance because
recreating it costs money; a triage pass never spends it. Recommending a
research call is not permission to make one, and any approved batch is
canary-first.

Do not open issues in sibling repositories, and do not `@`-mention anyone in a
comment or report, without explicit per-mention authorization.

## Related

- `next-tasks` — the lighter `NEXT_TASKS.md`-scoped check; run that for "what's
  next" during active work, this for a full-queue sweep.
- `trait-priority` — ranks *curation* targets, not issues; use it when the
  question is which trait to work on, not which issue.
- `metpo-proposal` — when an issue's real fix is an upstream ontology term, the
  proposal is the actionable next step, not a change in this repo.
- `audit-schema-gaps` — the maintained path for schema, instance, and writer
  quality claims an issue may assert.

## Related files

- `NEXT_TASKS.md` — items promoted from this ranking are often logged here so
  `next-tasks` picks them up on the next reconcile.
- `DO_NOT_WORK.md` — check before recommending work on any specific record.
