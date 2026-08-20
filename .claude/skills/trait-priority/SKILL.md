---
name: trait-priority
description: Decide what to curate or research next in TraitMech. Builds a weighted queue over all 477 records and returns a recommended ACTION per record (build/deepen a graph, add canonical_examples, drop, lump), plus a static dashboard. Use when asked what to work on next, which trait to deep-research, how to prioritise curation, or anything about lumping and splitting binned trait families. Replaces the retired prioritize-graph-research skill.
---

# What to curate next

`just trait-priority` scores every record and names an action. It reads **live
corpus state only** — no derived report, so it cannot go stale behind your back.

```bash
just trait-priority                              # top 25 by score
just trait-priority --top 0                      # everything (0 = all)
just trait-priority --action ADD_CANONICAL_EXAMPLES
just trait-priority --unresearched-only          # 0 today; see below
just trait-priority --format tsv --top 0 > /tmp/queue.tsv
just gen-priority-dashboard                      # app/dashboard/priority.{html,json}
```

Ported from DisMech's MONDO prioritiser (`monarch-initiative/dismech`,
`src/dismech/compare/mondo_priority.py`). What was taken: weighted scoring
tunable in `conf/trait_priority.yaml` with every component inspectable; an action
ladder where the first matching rule wins; a dashboard generated from the same
code as the CLI so the two cannot disagree.

## Read these two lines before the table

```
research: 0 mechanism record(s) have no artifact -- the rest need theirs APPLIED, not re-run
lumping: 10 series, mean sibling overlap 0.066 vs threshold 0.6 -> 0 lumped
```

**The research line.** Every mechanism-bearing record already has a
deep-research artifact — the 353 records that can carry a causal graph are
exactly the 353 that have one. So "deep-research the weakest graph" almost never
means commission new research. It means apply what is on disk. If that number is
ever non-zero, a genuinely unresearched trait has appeared and jumps the queue.

**The lumping line.** See below — it is the one place this diverges from DisMech.

## Lumping and splitting

DisMech penalises subtype series hard (`subtype_series_penalty: -18`) and
recommends `LUMP_INTO_PARENT`, because in MONDO an over-split series is usually
redundant term proliferation. **TraitMech does not lump, and the reason is
measured, not assumed:**

| test | result |
|---|---|
| child edges byte-identical to a parent edge | 18 of 3256 (0%) |
| mean node-label overlap between sibling bins | **5%** (max 20%) |
| mean node-label overlap child vs parent | ~8% |

`temperature_range_high` and `temperature_range_mid4` share almost no mechanism
content. The bins are numerically distinct phenotype bins carrying distinct
curation, so lumping them would **discard real work**. Series membership is
therefore reported as information, and `LUMP_INTO_PARENT` fires only above
`series_lump_min_sibling_overlap` (0.60), which nothing reaches.

If you are tempted to "fix" this by lowering the threshold, re-run the overlap
measurement first. A test asserts both halves so the change fails loudly.

**This is why the old `prioritize-graph-research` skill was retired.** Its tool
silently collapsed 44 records into 10 rows on the stated rationale that "one
research pass answers the whole family" — which 5% contradicts (#447) — and it
double-weighted a `missing_modules` column from a report that is stale for 347 of
353 traits (#443). Neither problem was fixable by tuning.

## The action ladder

First match wins:

| action | meaning |
|---|---|
| `DROP_NON_MECHANISM` | METPO object/datatype property or `upper` class — cannot carry a graph |
| `DROP_DEPRECATED` | retired record |
| `DROP_GROUPING_TERM` | bucket label, not a mechanism |
| `LUMP_INTO_PARENT` | siblings measurably duplicate (never fires today) |
| `CURATE_ROOT_WITH_SUBTYPES` | broad parent with a thin graph |
| `BUILD_CAUSAL_GRAPH` | mechanism record with no edges (none today) |
| `ADD_CANONICAL_EXAMPLES` | has a graph, no organism linked |
| `DEEPEN_CAUSAL_GRAPH` | thin or fragmented |
| `ALREADY_DEEP` | nothing obvious left |
| `CURATE_ROOT` | everything else |

Today: `DEEPEN_CAUSAL_GRAPH` 145 · `ADD_CANONICAL_EXAMPLES` 122 · `CURATE_ROOT`
72 · `DROP_NON_MECHANISM` 109 · `DROP_DEPRECATED` 20 · `ALREADY_DEEP` 9.

**Three rungs never fire on the current corpus**, and that is the data rather
than a bug — verified, not assumed. `BUILD_CAUSAL_GRAPH` (no mechanism record
has 0 edges), `CURATE_ROOT_WITH_SUBTYPES` (all 9 thin-parent records are
predicates or upper-ontology, so a DROP claims them first), `DROP_GROUPING_TERM`
(all 46 matching labels are already dropped). The counts print, so an
unreachable rule cannot masquerade as a passing check.

## Then verify the target before spending

The score says where to look; it does not say the graph is wrong. Read the
**edges**:

```bash
uv run python -c "
import yaml
d=yaml.safe_load(open('data/traits/<cat>/<slug>.yaml'))
for g in d['causal_graphs']:
    for e in g.get('edges') or []: print(e['subject'],'--',e['predicate'],'->',e['object'])
"
```

Do this even at a high score. **Node names imply a graph; only the edges are the
graph** — a lesson that cost six review rounds in #410, where four authored
knowledge gaps described structure the edges did not have because they were
written from node lists.

## Exclusions are never silent

Every run prints how many records were set aside and why (109 non-mechanism, 20
deprecated). If you report a ranking, report that line — without it the table
reads as "these are the worst" when it means "the worst of what I considered".

## Costed work

Deep research is paid. Edison returned `402 Payment Required` on 2026-08-17 —
the key authenticates, the account has no credit. Run `just
deep-research-providers` first; `asta` is the best discovery fit and the only
cheap+fast provider, needing only `ASTA_API_KEY`. Never fan out without one
canary through the same launcher the batch would use.

## Related

- `research-causal-graphs`, `deep-research-trait` — run the research
- `just audit-canonical-examples` — validate trait→organism links
- `conf/trait_priority.yaml` — the weights; every number in this file is a
  measurement, so prefer what the command prints
