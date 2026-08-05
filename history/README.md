# Curation history

Append-only provenance for curation sessions. One record per session per target,
written once and **never edited afterwards**. Corrections go in a new record that
references the old one in its `details`.

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
`--target-root`. Every other kind needs an explicit `--path`, because only those
two are reliably `.yaml`.

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

## How strictly this is enforced

Deliberately split:

- **Presence is advisory.** CI warns when a trait record changes without a
  matching history record. It does not block. A hard gate on provenance blocks
  legitimate work at inconvenient moments and trains people to route around it.
- **Validity is not.** If you write a record it must be schema-valid, and
  `just validate-history` fails like any other validation error.

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
ARGS=(--kind record --slug cellulolysis --target-root data/traits/metabolism \
      --summary "parity" --details "check" --issue 296)
PYTHONPATH="${CLAW_SRC:-../culturebotai-claw/src}" \
  uv run python -m kg_microbe_history new "${ARGS[@]}" --history-root /tmp/h_claw
uv run python scripts/new_history_record.py "${ARGS[@]}" --history-root /tmp/h_local
diff <(cat /tmp/h_claw/*/*.yaml) <(cat /tmp/h_local/*/*.yaml)
```

Changing the schema means changing the canonical copy and re-vendoring here — the
same hub-and-spoke rule as `mech_shared.yaml`. This copy is **not** on the
automated vendored-fleet drift check, so nothing enforces that rule yet: tracked
in #191, which also covers why appending it to `check_vendored_sync.sh` is not
straightforward (the canonical copy lives in claw, which is private, and the
existing check fetches over tokenless `raw.githubusercontent`).
