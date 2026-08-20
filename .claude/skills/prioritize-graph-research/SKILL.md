---
name: prioritize-graph-research
description: Pick which TraitMech trait to deep-research next, by ranking causal-graph weakness and reporting whether research already exists. Excludes records that cannot carry a mechanism graph (METPO object properties, datatype properties, deprecated observation classes, upper ontology), reports binned-series membership per row (bins share only ~5-7% of their content, so they rank separately), and refuses to rank on a stale completeness audit. Use when asked to prioritize a weak causal graph for research, choose a canary trait for a new research provider, or decide what to research next — BEFORE running deep-research-trait or research-causal-graphs, which spend money.
---

# Choosing the next deep-research target

This skill answers **which trait**, not **how to research it**. Once you have a
target, hand off to `research-causal-graphs` (Edison/falcon) or
`deep-research-trait`. Those cost money per call; this one is free, so run it
first, every time.

## Run it

```bash
just prioritize-research                        # worst graphs overall
just prioritize-research --sort missing          # <-- for choosing a RESEARCH target
just prioritize-research --sort fragmentation    # curation targets
just prioritize-research --limit 0               # everything
just prioritize-research --unresearched-only     # traits with no artifact at all
just prioritize-research --json                  # for scripting
just prioritize-research --include-nonmechanism  # show what was set aside
just prioritize-research --collapse-families     # one row per binned series
```

**Use `--sort missing` when the question is what to research** — but know that it
ranks purely on the completeness audit, and when most of that audit's rows no
longer match the live corpus it EXITS WITH AN ERROR rather than ranking on stale
data (#443). That is its current state, and there is **no in-repo way to
regenerate the audit** — it came from the paid 353-agent Edison sweep and
restoring it means re-running that sweep (#480). `--trust-stale-completeness`
overrides knowingly (and ranks on the stale values; below the error threshold,
stale rows simply sink to the bottom of this sort instead). The default sort
answers "which graph is worst", which is a different question and usually
resolves to curation work — see below.

## Read the answer before you trust the ranking

**The single most important output is the last line**, not the table:

```
of the ranked candidates, 0 have no deep-research artifact; the rest already
do -- those need their existing research APPLIED, not re-run
```

As of 2026-08-20 that number is **0**. Every trait that can carry a mechanism
graph already has one *and* already has an Edison/falcon report — every one of
the 348 ranked candidates. So a request to "deep-research the weakest graph"
usually should not produce a new research call at all. It should produce one of:

1. **Apply the research that exists.** `reports/graph_enrichment_backlog.md`
   holds 351 traits with named missing modules and DOI-backed candidate edges,
   already paid for — but it is a point-in-time sweep and **most of it has
   already been applied**: 345 of its 348 corpus-matched rows no longer match
   the live corpus (the command prints the live figure), and all six edges it
   proposes for `biofilm_formation` are already present (#443). Check the live
   graph before treating a backlog row as open work.
2. **A deliberate second pass with a different provider**, where the point is
   comparing providers rather than filling a gap. Use the ranking to pick the
   canary.
3. **A first pass for a genuinely new trait**, if `--unresearched-only` returns
   anything. Today it returns nothing; if it ever does, that trait jumps the
   queue and `test_every_ranked_candidate_on_the_real_corpus_is_already_researched`
   will have failed to tell you so.

Say which of the three you are doing. Conflating 1 and 2 is how a paid call gets
spent re-deriving something already on disk.

## What the score means

```
score = missing_modules*2 + orphan_nodes + (components-1)*2 + max(0, 8-edges)
```

`missing_modules` comes from the Edison completeness audit — mechanism modules
the literature has and the graph does not — so it is the only term measuring
what is actually *absent* rather than what the graph's shape implies. Hence the
double weight. It is also the only input with **no freshness guarantee** (#443):
each report row's `graph_edges` is checked against the live count, and a row
that no longer matches is marked stale — its `missing_modules` prints with a `*`
and is **excluded from the score**. When *most* rows are stale (today's state)
the term comes out of **every** score, fresh rows included — otherwise the few
coincidentally-matching rows would collect a double-weighted bonus the rest
cannot, and the composite sort would quietly become "fresh audit rows first".
The footer says which regime you are reading. The `8-edges` floor exists because
edges-per-node cannot see thinness: 1 edge over 2 nodes scores 0.5, identical
to 20 over 40.

It is a triage heuristic for ordering a queue, not a quality measurement.
Disagree with it on the printed evidence, not on faith — the reasons are in the
columns.

### A high score is not the same as a good research target

The two columns that separate them pull in opposite directions, and this is the
distinction that actually decides whether to spend money:

| pattern | what it is | what to do |
|---|---|---|
| many components, few missing modules | **connective** gap — the graph has the right pieces and never wired them together | curate; no research needed |
| few components, many missing modules | **content** gap — the graph is coherent and incomplete | research |

Worked example, both real:

- `metabolism/biopolymer_degradation` sits on **six** components. Its edges
  name `endoglucanase`, `endochitinase` and `lignin_oxidative_enzymes` without
  connecting any of them to the trait or to `assimilable_units`. Nothing in the
  literature is missing — the *edges* are. Researching this buys a report that
  tells you what you already have.
- `ecology/nitrogen_fixing_symbiosis` has **one** component, no orphans, and the
  highest missing-module count in the corpus (**11**) — though that count is
  from a stale audit row (`11*` in the output), so treat it as a lead to verify
  against the live graph, not a fact.

So the higher-scoring trait is usually the *curation* target and the coherent,
content-starved one the *research* target. Sorting by score alone picks the
wrong one.

## Three traps it already handles, and why they are not obvious

**1. Most graph-less records are not traits.** 124 of 477 records have no causal
graph, and a naive "no graph = weakest graph" ranking puts every one of them on
top. None is researchable:

| what | how many | example |
|---|---|---|
| `term_kind: OBJECT_PROPERTY` | 94 | `uses_for_growth`, `degrades`, `has_phenotype`, `exports` |
| `term_kind: DATATYPE_PROPERTY` | 7 | `has_value`, `is_negative_data` |
| `mapping_status: DEPRECATED` | 20 | `growth_ph_observation` |
| category `upper` (graph-less) | 3 | `microbe`, `enzyme`, `chemical_entity` |

They are METPO object properties seeded into `data/traits`. There is no
mechanism to research in "does not assimilate".

**Decide this by schema field, never by slug shape.** The first version of the
script used a hand-written list of prefixes and matched 47 of the 94 — silently
ranking `uses_for_growth`, `has_phenotype`, `exports` and `transports` as
research candidates. `term_kind` was in the record the whole time.

**2. Upper-ontology classes that *do* have graphs still are not targets.**
`material_entity` and `quality` carry 3-edge graphs, `phenotype` 4 — thin enough
to rank near the top. A thin graph on `quality` is not a research question; it is
a sign the graph should probably not exist. The whole category is set aside, so
the exclusion is by category and not by emptiness.

**3. Binned siblings look like one research question and are not.**
`ph_delta_mid2`, `ph_delta_mid3`, `temperature_range_mid4` are METPO binning
classes, and this script used to collapse each family into one row on the
assumption one research pass answers the whole family. Measured, that is false
(#447): sibling bins share a mean **~5–7%** of their node labels (max 20–25%,
depending on label extraction — #481 tracks the exact-figure discrepancy), and
almost no child edge is byte-identical to a parent edge. Each bin is its own
work item, so bins rank separately and rows carry `[series ph_delta, 6 bins]`
as information. `--collapse-families` restores the merged view when you want
family granularity — knowing that the surviving representative is the worst
member by *composite score* even under another `--sort` (#479);
`scripts/trait_priority.py` holds the retuned rule (lump only above measured
overlap, which nothing reaches).

Exclusions are always counted and broken down in the output. If you report a
ranking, report that line too: without it the table reads as "these are the
worst", when it means "these are the worst of what I considered".

> **Every count quoted in this file is a measurement, not a constant.** They were
> true on 2026-08-18 and `test_corpus_composition_matches_what_the_skill_claims`
> fails if the corpus moves, naming this file in its message. If you are reading
> a number here, prefer the number the command prints.

## Then verify the target before spending

The ranking says where to look; it does not say the graph is wrong. Before
committing a paid call, read the target's **edges**:

```bash
uv run python -c "
import yaml
d=yaml.safe_load(open('data/traits/<cat>/<slug>.yaml'))
for g in d['causal_graphs']:
    for e in g.get('edges') or []: print(e['subject'],'--',e['predicate'],'->',e['object'])
"
```

Do this even when the score is high. **Node names imply a graph; only the edges
are the graph** — a lesson that cost six review rounds in #410, where four
authored knowledge gaps described structure the edges did not have because they
were written from node lists. A trait with 15 nodes and 8 edges in 7 components
is not "a graph with some gaps"; it is seven fragments, and knowing which
fragments before you research changes the question you ask.

## Canary rule applies

Deep research is paid, batched work. Never fan out from this ranking. Take the
top row, run **one** trait end to end through the same launcher the batch would
use, confirm the artifact is on disk and non-empty, then decide. A cache-backed
client constructed without its cache path bills you and persists nothing.

Note that Edison returned `402 Payment Required` on 2026-08-17 — the key
authenticates but the account has no credit. Check that before planning any run,
or the canary tells you nothing about the batch.

## Related

- `research-causal-graphs` — runs the research (Edison/falcon), batch + resume
- `deep-research-trait` — single-trait research with a full provenance bundle
- `reports/graph_enrichment_backlog.md` — 351 traits, already-paid-for missing
  modules with DOIs. Largely applied already (#443); verify against the live
  graph before treating a row as open work.
- `audit-graphs` / `reports/causal_graph_connectivity.tsv` — the fragmentation
  and orphan-node numbers this ranking consumes
