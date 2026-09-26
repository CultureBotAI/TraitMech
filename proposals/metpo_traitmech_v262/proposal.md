# METPO ROBOT Template Proposal - PD-Lambda-5 System (v262, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v261 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for PD-Lambda-5 system, the
genome-level possession trait for a DefenseFinder-modeled anti-phage locus from
Vassallo et al.'s *E. coli* pangenome screen. DefenseFinder models PD-Lambda-5
with two required HMM profiles, `PD-Lambda-5__PD-Lambda-5_A` and
`PD-Lambda-5__PD-Lambda-5_B`.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for PD-Lambda-5 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1033900` is reserved for this one-row class cohort. The v261 cohort
used `METPO:1033800`, so v262 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope PD-Lambda-5 system record,
`pd_lambda_5_system` slug, `PD-Lambda-5__PD-Lambda-5_A`,
`PD-Lambda-5__PD-Lambda-5_B`, `traitmech:000385`,
`metpo_traitmech_v262`, or `METPO:1033900`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1033900` | PD-Lambda-5 system | `METPO:1016300` phage defense system |

PD-Lambda-5 system captures genome-level possession of a two-profile
DefenseFinder phage-defense locus experimentally linked to T2, T4, T6,
LambdaVir, SECphi17, SECphi18, SECphi27, T3, and T7 protection when expressed
in *E. coli*. It excludes the individual PD-Lambda-5 genes or proteins, the
DefenseFinder `PD-Lambda-5__PD-Lambda-5_A` and
`PD-Lambda-5__PD-Lambda-5_B` profiles, the source key `PD-Lambda-5`, the
P2-like prophage context, phage protection outside a complete PD-Lambda-5
locus, RefSeq example loci without experimental validation, sibling PD-Lambda
systems, prophages and mobile genetic elements as mobile elements, and other
phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual proteins, source database rows
naming the DefenseFinder model, HMM profiles, RefSeq example loci, and
protection against T2, T4, T6, LambdaVir, SECphi17, SECphi18, SECphi27, T3, or
T7 are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  no exact external xrefs and related DefenseFinder profile labels.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000385` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000385` as traceability during the migration.

## Change Log

- v262, 2026-09: lifts `traitmech:000385 PD-Lambda-5 system` into the
  `METPO:1033900` block.
