# METPO ROBOT Template Proposal - Ig-like Schlafen System (v385, 2026-10)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Ig-like Schlafen system,
the genome-level possession trait for a prokaryotic Schlafen nuclease fused to
an immunoglobulin-like phage-sensor domain. Perez Taboada et al. support
prokaryotic Schlafen nucleases as widespread antiviral effectors fused to
phage-sensing domains and characterize the RorSlfn5 Ig-like Schlafen nuclease as
a T5-like tail assembly chaperone-triggered tRNase. The pinned DefenseFinder
article registry maps `Shlafen_Ig-like` to the same DOI, while the pinned HMM
inventory and rules table have no exact Schlafen row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Ig-like Schlafen system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1046200` is reserved for this one-row class cohort. The v384 cohort used
`METPO:1046100`, so v385 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope Schlafen record,
`ig_like_schlafen_system` slug, `traitmech:000508`, `METPO:1046200`,
`metpo_traitmech_v385`, Perez Taboada et al. Nature DOI
`10.1038/s41564-026-02277-8`, title `Bacterial Schlafen proteins mediate phage
defence`, `pSlfn5`, or DefenseFinder source key `Shlafen_Ig-like`.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1046200` | Ig-like Schlafen system | `METPO:1016300` phage defense system |

Ig-like Schlafen system captures genome-level possession of a prokaryotic
Schlafen nuclease fused to an immunoglobulin-like sensor domain that recognizes
T5-like phage tail assembly chaperones and activates Schlafen tRNase defense. It
excludes individual Schlafen proteins, individual prokaryotic `schlafen` genes,
other prokaryotic Schlafen nuclease domain architectures, tail assembly
chaperone phage triggers, Schlafen tRNase activity outside a complete Ig-like
anti-phage system, and the DefenseFinder `Shlafen_Ig-like` source key outside a
complete organism-level system.

`traitmech:000508` is a direct local child of `traitmech:000209` phage defense
system. This proposal uses `METPO:1016300`, the v86 placeholder for
`traitmech:000209`.

## External Mappings

No exact external mapping is proposed. Individual Schlafen proteins, individual
prokaryotic `schlafen` genes, phage trigger proteins, bacterial or phage tRNA
substrates, the broader Schlafen antiviral effector class, and the DefenseFinder
article-registry key are shifted from this organism-level GENOMICS possession
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000508` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000508` as traceability during the migration.

## Change Log

- v385, 2026-10: lifts `traitmech:000508 Ig-like Schlafen system` into the
  `METPO:1046200` placeholder block.
