# METPO ROBOT Template Proposal — TraitMech Predicate Lift (v2, 2026-06)

> **Upstream submission:** consolidated in [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535) (2026-06-14) — requesting real METPO IDs for this cohort.

## Context

[TraitMech](https://github.com/CultureBotAI/TraitMech) records carry
`causal_graphs:` with typed `nodes:` and evidence-backed `edges:`. Each
edge carries a free-text `predicate:` label and an optional
`predicate_id:` CURIE grounding (LinkML class `CausalEdge`).

The [v1 cohort](../metpo_traitmech_v1/) lifted the *class-level*
causal-graph scaffolding (`CausalGraph`, `CausalNode`, `CausalEdge`, and
the `CausalNodeTypeEnum` value set) but deferred the *predicate-level*
proposal:

> Scope B (causal-graph predicates): deferred — see Predicate proposals
> section — proposal would be premature; predicate-grounding migration
> must run first.

That migration has now run. The
[predicate-grounding pipeline](../../scripts/ground_causal_predicates.py)
applies a curated label → CURIE mapping
(`mappings/predicate_grounding.tsv`) across `data/traits/`. As of this
proposal, **618 of 1019 causal-edge `predicate_id` slots are
grounded** (28 RO / biolink / METPO / rdfs mappings landed in
[PR #61](https://github.com/CultureBotAI/TraitMech/pull/61), plus 10
additions in this cohort).

The remaining **401 edges across 181 distinct labels** are residual.
This v2 cohort closes out the largest, most semantically coherent
clusters of the residual by proposing **8 new METPO predicates**
(`METPO:2007400`–`METPO:2007407`) that together cover 128 edges (24%
of the residual at v1-merge time).

## Scope

| Scope | Source | # rows | Lift status |
|---|---|---:|---|
| A (synthetic trait classes) | `data/traits/**/*.yaml` records whose `identifier:` starts with `traitmech:` | 0 | not applicable — none in corpus |
| B (causal-graph predicates) | top clusters in `reports/predicate_grounding_residual.tsv` | **8 predicates / 128 edges** | included |
| C (controlled vocabularies) | already lifted in v1 (`CausalNodeTypeEnum`) | 0 | already covered |

Total property rows in v2: **8**. No class rows; the v1 cohort already
minted the domain class (`METPO:1007401` trait causal node).

## Predicate proposals

Each row uses domain = range = `METPO:1007401` (the v1-minted *trait
causal node* superclass). Reviewers should merge v1 and v2 together at
adoption time so the domain/range references resolve.

| ID | Label | Edges grounded | Cluster |
|---|---|---:|---|
| `METPO:2007400` | manifests as | 52 | Phenotype manifestation: physiological state → observable trait |
| `METPO:2007401` | selects for | 20 | Evolutionary selection: environmental condition → adapted trait |
| `METPO:2007402` | feeds electrons into | 12 | Electron flux: donor → respiratory / transport pathway |
| `METPO:2007403` | transfers electrons to | 6 | Redox: single-step donor → acceptor (sister-of `feeds electrons into`) |
| `METPO:2007404` | fixed by | 9 | Carbon / inorganic fixation: substrate → fixation pathway |
| `METPO:2007405` | oxidized to | 8 | Chemistry: reduced substrate → oxidized product |
| `METPO:2007406` | challenges | 9 | Environmental stress: stressor → tolerance trait |
| `METPO:2007407` | mitigates | 12 | Defense / homeostasis: defense mechanism → stressor (paired-positive of `challenges`) |

### Why not RO or Biolink for these?

For each proposed predicate, the most plausible upstream candidate was
explicitly considered and rejected:

| Proposed | Considered | Why rejected |
|---|---|---|
| `manifests as` | `biolink:manifestation_of`, `RO:0002488` realized in | `biolink:manifestation_of` has range `disease` (too narrow); `RO:0002488` is too OBO-style — TraitMech's typical object is a TraitMech-internal trait class. |
| `selects for` | `biolink:related_to`, `biolink:causes` | `related_to` is too weak (no causal claim); `causes` is too strong (selection is evolutionary, not mechanistic). |
| `feeds electrons into` | `biolink:contributes_to`, `RO:0002327` enables | Both are too generic; the corpus uses this specifically for redox-cofactor flux into transport chains, which is a domain-of-art relation that consumers want to query as such. |
| `transfers electrons to` | `RO:0002327` enables | enables is functional, not redox-specific. |
| `fixed by` | `biolink:produces` (inverse) | Wrong direction — substrate is acted upon, not produced. |
| `oxidized to` | `biolink:produces`, `RO:0003000` produces | The chemistry direction (substrate → product) is not captured by `produces`, which is agent → product. |
| `challenges` / `mitigates` | `biolink:treats`, `RO:0002408` directly inhibits process | `treats` is clinical; `directly inhibits process` is too narrow (the corpus uses stress/defense edges for homeostasis, not pathway inhibition). |

### Paired-predicate convention (one pair in this cohort)

`challenges` (`METPO:2007406`) and `mitigates` (`METPO:2007407`) form
the only paired predicate set in v2: a stressor *challenges* a trait,
and a defense *mitigates* the corresponding stress. The pair is
unidirectional (stressor → trait; defense → stressor) and is **not**
a positive/negative pair on the same axis (compare the
chemical-interaction paired-positive/negative convention in
`kg-microbe`).

## Hierarchy decisions

All 8 predicates are siblings at the top of the property tree (no
explicit `is_a` parent declared in the ROBOT row, which leaves the
property as a child of `owl:topObjectProperty`). They are not
disjoint — `transfers electrons to` is semantically narrower than
`feeds electrons into`, but encoding a property `subPropertyOf`
relationship in a ROBOT-template TSV requires a second TYPE column
that the canonical kg-microbe template does not use. Leave the
hierarchy flat for v2; upstream maintainers can refactor later if they
choose to add a `subPropertyOf` axis.

## ID space and subset

| Range | Use |
|---|---|
| `METPO:2007400`–`METPO:2007407` | v2 predicate block (allocated; first 8 IDs of the `2007400+` placeholder range) |

Subset tag: **`metpo_traitmech_2026_06`** (forward-dated relative to
the May 2026 v1 cohort; per the `metpo-proposal` skill, each new
cohort directory gets a new subset tag).

Collision check: `grep "METPO_2007" data/raw/metpo.owl` → 0 hits.

## Files

| File | Rows | Purpose |
|---|---:|---|
| `proposal.md` | this file | Reviewer narrative |
| `metpo_proposal_properties_robot.tsv` | 10 (2 header + 8 predicate) | Submittable ROBOT-template artifact |

No `metpo_proposal_classes_robot.tsv` — the domain/range class
(`METPO:1007401` *trait causal node*) was minted in v1.

## Verification

```
$ just verify-proposal metpo_traitmech_v2
  properties TSV: 10 rows
  scope-A: no traitmech:NNNNNN ids in corpus (nothing to cover)
  scope-C: CausalNodeTypeEnum not lifted in this cohort (skip)
  failures: 0
  status:   PASS

$ just robot-validate-proposal metpo_traitmech_v2
  merged.owl lines:    8454
  reasoned.owl lines:  8460
  delta:               +6
  status:              PASS (no UNSAT, ELK exited 0)
```

ELK reasoning runs against `data/raw/metpo.owl` merged with this
cohort's `props.owl`. The v1 cohort's `METPO:1007401` domain/range
reference resolves to an unnamed external IRI in this run (v1 has not
been adopted upstream), but ELK does not error — the property's
domain/range constraint is preserved as-is and will resolve cleanly
once v1 + v2 are merged into the upstream METPO ontology together.

## Corpus impact

After applying `mappings/predicate_grounding.tsv` (with this cohort's
10 new mappings: 8 METPO + `controls`/`directs` → `RO:0002211`):

|  | Before v2 | After v2 |
|---|---:|---:|
| Edges grounded | 482 | 618 |
| Edges residual | 537 | 401 |
| Distinct residual labels | 191 | 181 |
| Mappings TSV size | 28 rows | 38 rows |

The residual tail (401 edges, 181 labels) is dominated by
curator-paraphrased predicates with low edge counts (`drives` 19,
`defines` 14, `maintains` 13, then 178 labels with ≤12 edges each).
A v3 cohort could pick up another cluster (likely the homeostasis /
control-loop family) once the corpus has stabilized after v2 adoption.

## Upstream path

Per user request, this cohort is **not filed upstream in the
[berkeleybop/metpo](https://github.com/berkeleybop/metpo) repository
in this PR**. The cohort is committed here for review and to enable
the corpus-side grounding to reference the proposed CURIEs ahead of
upstream adoption.

When ready to file upstream:

1. Confirm v1 cohort is also being filed (these proposed predicates
   reference `METPO:1007401` from v1).
2. Open an issue at <https://github.com/berkeleybop/metpo> with
   `metpo_proposal_properties_robot.tsv` attached (plus a link to
   `proposal.md`).
3. After upstream mints real `METPO:2007400`-range IDs, refresh
   `data/raw/metpo.owl`, re-run `just ground-predicates --apply` to
   pick up any post-mint relabeling, and update `mappings/predicate_grounding.tsv`
   notes to remove the "proposed upstream in proposals/metpo_traitmech_v2"
   qualifier.

## Round-trip plan

If upstream renumbers the predicates (e.g. METPO chooses a different
block), the TraitMech-side migration is:

1. Update `mappings/predicate_grounding.tsv` (replace the v2 METPO
   CURIEs with the upstream-assigned ones).
2. Re-run `just ground-predicates --apply` — the script never
   overwrites existing `predicate_id` values, so a CURIE swap requires
   first clearing the affected `predicate_id` fields. Use a one-off
   migration script for that step.
3. Re-run `just validate-strict` (now CI-enforced via `.github/workflows/validate-strict.yaml`).

## Change log

- **v2 (2026-06)** — 8 new METPO predicates covering 128 of 537
  residual causal-edge predicates; subset `metpo_traitmech_2026_06`.
