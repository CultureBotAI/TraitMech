# METPO ROBOT Template Proposal — Energetic Drivers of Molecular Machines (v10, 2026-08)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535) alongside
> the v1–v9 cohorts — requesting a real METPO ID for this cohort.

## Context

This cohort exists to close the last five edges of TraitMech#334, and it proposes
exactly one predicate.

`data/raw/biolink-model.yaml` gives `enables` (`RO:0002327`) the range
`biological process or activity`. Of `CausalNodeTypeEnum`'s members only
`BIOLOGICAL_PROCESS`, `PATHWAY` and `MOLECULAR_FUNCTION` satisfy it. TraitMech#315
widened the corpus audit from its original TRAIT-only test to that full range and
surfaced 33 violating edges; #351 repaired 17, and #334 repaired the remaining 16.

Eleven of those 16 needed no new term — they were repointed at a process the graph
already contained, reversed to the direction the record's own prose stated, or moved
onto an existing relation (`produces`, `has output`, `transports`, `part of`,
`promotes`, `confers`, `manifests as`). **Five could not be.**

## Scope

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| B — causal-graph predicate lift | 1 | 7 causal edges across 6 trait records assert that an energetic driver operates a molecular machine; no RO or OBI relation admits the protein-complex object |
| A — synthetic trait class lift | 0 | no `traitmech:` identifiers were minted by #334 |
| C — schema enum lift | 0 | already covered by `metpo_traitmech_v1` |

## Predicate proposal

| ID | label | domain | range | source record |
|---|---|---|---|---|
| `METPO:2007900` | powers | `METPO:1007401` | `METPO:1007401` | `morphology/motile.yaml#motile_energy_dependent_locomotion` |

### Why not an existing relation

**Not `RO:0002327` (enables).** That is what these edges said, and it is the
defect: a flagellar motor is a protein complex, which cannot satisfy
`biological process or activity`.

**Not `RO:0002233` (has input) reversed.** Its domain is a process, and the subject
here would be the protein complex.

**Not RO at all.** RO models energetics at the *process* level while all seven corpus
objects are protein complexes. That is not a new observation in this repo — it is the
same gap `METPO:2007804` (*exports*) and `METPO:2007805` (*imports*) were minted to
fill, whose note reads *"RO models transport at the process level, so no RO relation
admits the GENE_OR_PROTEIN subject these edges use."*

**The label is not a coinage.** Every one of the five #334 edge descriptions already
used the verb, and the term was chosen by reading them rather than by inventing a
name:

| record | edge description |
|---|---|
| `morphology/motile.yaml` | "Ion motive force **powers** rotation of the flagellar motor." |
| `morphology/motile.yaml` | "Torque generation drives rotation of the flagellar motor." |
| `morphology/motility.yaml` | "Ion motive force **powers** rotation of many bacterial flagellar motors." |
| `morphology/flagellated.yaml` | "Ion flux through stator complexes **powers** torque generation." |
| `morphology/gliding.yaml` | "Proton motive force can **power** gliding motility motors." |

### Two edges beyond #334

The gate also matches two pre-existing corpus edges that were never part of #334, and
both read correctly under this definition:

| record | edge |
|---|---|
| `environment/ph_optimum_mid2.yaml` | `proton_motive_force` (BIOLOGICAL_PROCESS) → `f0f1_atp_synthase` |
| `physiology/carboxydotrophic.yaml` | `proton_motive_force` (STATE) → `atp_synthase` |

They are counted in the 7 above, and they matter to the round-trip plan below: a
grounding pass will stamp `METPO:2007900` onto them, so whoever swaps in the minted ID
has to look at seven edges, not five.

A further four `powers` edges stay `blocked_by_node_type`, and three of those are
blocked **correctly** — their objects are processes, which satisfy `enables`' range and
belong on `RO:0002327`. The fourth, `physiology/phototrophic.yaml`, is blocked only
because it types `proton_motive_force` as `CAPACITY` where `carboxydotrophic.yaml` types
the byte-identical assertion's subject `STATE`. That inconsistency predates this cohort
and is tracked in TraitMech#356.

### Gating

`mappings/predicate_grounding.tsv` gates the term to
`subject_types = BIOLOGICAL_PROCESS|STATE`, `object_types = GENE_OR_PROTEIN`.

The object gate is the point of the term, not a convenience: an energetic driver
feeding a *process* satisfies `enables`' range already and must stay on `RO:0002327`.
Leaving `object_types` open would let this term absorb edges that are not broken,
and the range violation it exists to fix would stop being visible.

## ID space and subset

`METPO:2007900`, opening the `2007900`–`2007999` block. v8 occupies `2007700`+ and v9
occupies `2007800`+, so this collides with neither, and no block is reused. Subset tag
`metpo_traitmech_2026_13`, continuing the per-cohort sequence (v9 was `2026_12`).

## Files

| File | Rows |
|---|---:|
| `metpo_proposal_properties_robot.tsv` | 1 predicate (+2 header rows) |
| `metpo_proposal_mappings.sssom.tsv` | 1 mapping |
| `proposal.md` | this file |

No classes template: this cohort proposes no classes.

## Verification

```
just verify-proposal metpo_traitmech_v10
  properties TSV: 3 rows
  failures: 0
  status:   PASS
```

Corpus effect, measured rather than predicted:
`ENABLES_RANGE_VIOLATION` **16 → 0**, `MICROBE_DOMAIN_ON_NONORGANISM` stays **0**, and
`audit-graphs` is unchanged at 218 `FRAGMENTED_GRAPH` / 1303 `UNREACHABLE_FROM_TRAIT`
— the repairs repointed edges without stranding any node.

## Upstream path

Consolidate into berkeleybop/metpo#535 with the v1–v9 cohorts.

## Round-trip plan

After upstream mints a real ID: update `data/raw/metpo.owl`, re-seed, and swap
`METPO:2007900` for the minted CURIE in `mappings/predicate_grounding.tsv` and in the
seven edges' `predicate_id` (the five from #334 plus the two named above).
Until then the placeholder is confined to those two places, and `audit-predicate-domains` fails if an edge drifts back onto `RO:0002327`.

## Change log

| Version | Date | Change |
|---|---|---|
| v10 | 2026-08 | Initial cohort — `powers` (`METPO:2007900`), closing the last 5 edges of TraitMech#334 |
