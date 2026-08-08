# Curation history

Append-only provenance for curation sessions. **One record per change** — per
target for hand curation, per *migration* for a bulk edit (see "One record per
CHANGE" below). Written once and **never edited afterwards**; corrections go in a
new record that references the old one in its `details`.

```
history/<kind-dir>/<slug>/<TIMESTAMP>-<actor>-<shortid>.yaml
```

## Why this exists

Nothing else in the repo records *which model, using which tool, changed what,
why, and under which issue*. Git tells you a commit happened; it does not tell you
that a claim was checked against a cached abstract, or which deep-research
provider produced an edge, or that a review deliberately changed nothing.

That gap matters more as autonomous agents start doing the changing. See
`culturebotai-claw/docs/AUTONOMOUS_LOOPS.md`.

## Why the layout looks like that

The directory-per-slug plus unguessable `shortid` is the whole design. Two agents
curating the same trait concurrently cannot write the same file, so this layer has
**no merge-conflict surface**. A single shared changelog would conflict on every
parallel PR; this never does.

## Writing a record

Do not hand-write the filename or the timestamp — scaffold it:

```bash
just new-history --kind record --slug cellulolysis \
  --target-root data/traits/metabolism \
  --event EDIT --outcome changed \
  --sections causal_graphs,grounding \
  --summary "Connect fragmented cellulolysis causal graph" \
  --model claude-opus-5 --agent-tool claude-code \
  --issue https://github.com/CultureBotAI/TraitMech/issues/183 \
  --details "What was done, what evidence was used, how it was validated."
```

Omit `--details` and you get a TODO placeholder to edit before committing —
`just validate-history` **fails** while it is still there, so an unfilled record
cannot slip through. The command prints the record path as its final stdout line,
so scripts can capture it.

`--kind record` and `--kind schema` can derive the target path from `--slug` plus
`--target-root`. Every other kind should pass an explicit `--path`, because only
those two are reliably `.yaml` — mappings are `.sssom.tsv`, reports `.md`,
infrastructure a justfile or workflow. Neither scaffolder *enforces* that: both
will derive `<target-root>/<slug>.yaml` for any kind, so passing `--target-root`
with `--kind mapping` silently yields a target path that does not exist.

Then validate and stage:

```bash
just validate-history history/records/cellulolysis/<file>.yaml
git add history/
```

## The vocabulary

`event`: `CREATE` · `EDIT` · `REVIEW` · `AUDIT` · `GENERAL`

`outcome`: `changed` · `no_change` · `needs_followup` · `blocked`

Outcome is **orthogonal** to event on purpose. A `REVIEW` that found nothing is
`no_change` — a real result worth recording, because it says something was
checked. An `EDIT` that hit a wall is `blocked`, and `details` must say what the
wall was so the next session does not rediscover it.

`kind`: `record` · `schema` · `mapping` · `report` · `infrastructure` · `other`
(`other` requires an explicit `--path`).

## One record per CHANGE, not per file

"One record per session per target" is the rule for **hand curation**, where the
session and the target coincide: someone reasons about one trait and writes down
what they concluded. The three records under `records/` are exactly that, and the
`sulfur_globule` one is what a good record looks like.

A **bulk change is a different animal** and the same rule read literally gives the
wrong answer. #302 touched 128 trait records mechanically; #334 touched 15. Writing
one record per file would produce 128 near-identical stubs and bury the handful of
substantive records this directory exists for — destroying the signal in the name
of provenance.

So for a change that edits many records under one decision, write **one** record:

| the change is | `kind` | `path` |
|---|---|---|
| one trait, curated | `record` | that trait's YAML |
| a migration driven by a script | `infrastructure` | the migration script |
| a bulk change with no single script | `other` | the file that best explains it |

Name the scope in `events[].details` — how many records, which issue, and what the
selection rule was. The migration script is usually the honest target: it *is* the
artifact that says what drove the change, and it is reviewable in a way that 128
copies of the same sentence are not.

The per-file `curation_history:` block still records what changed in each file.
The two are not redundant: that block has no slot for the model, the tool, or the
issue, and — because it hangs off an edit — **it cannot record a session that
changed nothing.** An `AUDIT` that checked a trait and correctly found nothing
wrong is invisible without a record here. That is what `outcome: no_change` is for.

## How strictly this is enforced

- **Presence blocks** (#325). A PR that changes any `.yaml` under `data/traits/`
  and adds no new history record fails CI.

  This was advisory until #325, on the reasoning that a hard gate "trains people to
  route around it". The measurement disagreed: of **134 commits** that modified
  trait records, **2** added a history record — 1.5%. Nobody routed around the
  gate, because there was no gate; the convention simply did not happen. Meanwhile
  **275 trait records** carry an issue number hand-typed into a `changes` string,
  which is the same information in a form nothing can query. An unenforced
  convention here drifts exactly as #182, #184 and #215 drifted.

  The cost is now one file per PR rather than one per changed record, which is what
  makes the gate reasonable to impose at all — the granularity fix above had to come
  first.

- **Validity blocks too.** If you write a record it must be schema-valid, and
  `just validate-history` fails like any other validation error. It also fails while
  the `--details` TODO placeholder is unfilled, so scaffolding an empty record to
  satisfy the presence gate does not work.

## The vendored schema still states the old policy

`src/traitmech/schema/history.yaml` describes presence as *advisory* and states
"one record per session per target" unqualified. Both are superseded by #325 and
**neither is edited here on purpose**: that file is vendored byte-identical from
claw, which is private and unreachable from this repo's CI, so a one-copy edit
would create drift that nothing detects — `src/traitmech/schema/history.yaml` is
NOT in `scripts/check_vendored_sync.sh`'s checked set, which is the gap #209
tracks. The canonical copy has to change in claw first and be re-vendored;
tracked in #358.

Until then this README and the `curation-history` workflow are the operative
statements of the policy, and the schema's prose is stale by design rather than
by neglect.

## Where the schema lives

Two copies, on purpose:

- **Canonical**: `culturebotai-claw/shared/history/history.yaml`, with the
  scaffolder at `culturebotai-claw/src/kg_microbe_history/`.
- **Vendored here**: `src/traitmech/schema/history.yaml`, byte-identical.

Check that identity rather than trusting this file — with a claw checkout:

```bash
diff "${CLAW_SRC:-../culturebotai-claw/src}/../shared/history/history.yaml" \
     src/traitmech/schema/history.yaml && echo "in sync"
```

An earlier draft of this README recorded the md5 inline. It went stale one commit
later, when the schema gained a field and the hash was not updated — which is the
argument against writing a hash into prose at all: nothing recomputes it, so it
decays into a confident false negative. A runnable command cannot go stale.

The vendored copy exists so validation has **no dependency on claw**, which is
private — a public repo's CI cannot check it out without a token. `just
validate-history` and the `curation-history` workflow both use the local copy and
work with no claw checkout at all.

`just new-history` **prefers** claw, via `CLAW_SRC` (default:
`../culturebotai-claw/src`), and falls back to
`scripts/new_history_record.py` when there is no checkout there. Claw stays the
canonical scaffolder so the record shape does not drift across the four Mech
repos; the fallback exists because the alternative to a slightly-divergent
record is no record at all.

That fallback was added in #296, after the #294 backfill wrote two records by
hand. The prompt for it is worth keeping: this file previously asserted that
"anyone writing curation records has claw checked out", which is an assumption
rather than a guarantee — it does not hold for a fresh clone, for CI (claw is
private), or for a contributor outside the fleet. It also did not hold in
practice for the reason you would expect: the recipe was *gated* on claw, so it
was easier to hand-write than to find out whether the gate would pass.

The two scaffolders take the **same arguments** and produce byte-identical
records apart from the id's hash suffix and one deliberate difference: a bare
`--issue 296` becomes a full URL here, because the schema declares those
`range: uri` and every committed record carries URLs, whereas claw passes the
string through. Check that parity rather than trusting this paragraph:

```bash
# Exercise a non-`record` kind too: the layout is history/<kind-dir>/<slug>/,
# and a fallback that hardcodes `records/` writes to the wrong place while still
# validating, because the schema does not constrain the path.
ARGS=(--kind infrastructure --slug curation-history --path docs/x.md \
      --sections causal_graphs,grounding \
      --summary "parity" --details "check" --issue 296)
PYTHONPATH="${CLAW_SRC:-../culturebotai-claw/src}" \
  uv run python -m kg_microbe_history new "${ARGS[@]}" --history-root /tmp/h_claw
uv run python scripts/new_history_record.py "${ARGS[@]}" --history-root /tmp/h_local
diff <(cat /tmp/h_claw/*/*/*.yaml) <(cat /tmp/h_local/*/*/*.yaml)
```

Omitting `--details` writes claw's placeholder **byte-for-byte**, so the record
fails `just validate-history` until you replace it — which is the promise two
paragraphs up, and which a near-miss wording would quietly break, since the
schema pattern is a negative lookahead on that exact string.

Changing the schema means changing the canonical copy and re-vendoring here — the
same hub-and-spoke rule as `mech_shared.yaml`. This copy is **not** on the
automated vendored-fleet drift check, so nothing enforces that rule yet: tracked
in #191, which also covers why appending it to `check_vendored_sync.sh` is not
straightforward (the canonical copy lives in claw, which is private, and the
existing check fetches over tokenless `raw.githubusercontent`).
