# METPO ROBOT Template Proposal - PD-Lambda-3 System (v259, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v258 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for PD-Lambda-3 system, the
genome-level possession trait for a DefenseFinder-modeled anti-phage locus from
Vassallo et al.'s *E. coli* pangenome screen. DefenseFinder models PD-Lambda-3
with two required HMM profiles, `PD-Lambda-3__PD-Lambda-3_A` and
`PD-Lambda-3__PD-Lambda-3_B`.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for PD-Lambda-3 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1033600` is reserved for this one-row class cohort. The v258 cohort
used `METPO:1033500`, so v259 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope PD-Lambda-3 system record,
`pd_lambda_3_system` slug, `PD-Lambda-3__PD-Lambda-3_A`,
`PD-Lambda-3__PD-Lambda-3_B`, `traitmech:000382`,
`metpo_traitmech_v259`, or `METPO:1033600`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1033600` | PD-Lambda-3 system | `METPO:1016300` phage defense system |

PD-Lambda-3 system captures genome-level possession of a two-profile
DefenseFinder phage-defense locus experimentally linked to LambdaVir protection
when expressed in *E. coli*. It excludes individual PD-Lambda-3 genes and
proteins, the DefenseFinder `PD-Lambda-3__PD-Lambda-3_A` and
`PD-Lambda-3__PD-Lambda-3_B` profiles, the source key `PD-Lambda-3`, phage
protection outside a complete PD-Lambda-3 locus, RefSeq example loci without
experimental validation, sibling PD-Lambda systems, prophages and mobile
genetic elements as mobile elements, and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual proteins, source database rows
naming the DefenseFinder model, HMM profiles, RefSeq example loci, and
protection against LambdaVir are shifted from this organism-level GENOMICS
possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  no exact external xrefs and two related DefenseFinder profile labels.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000382` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000382` as traceability during the migration.

## Change Log

- v259, 2026-09: lifts `traitmech:000382 PD-Lambda-3 system` into the
  `METPO:1033600` block.
