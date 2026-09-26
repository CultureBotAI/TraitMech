# METPO ROBOT Template Proposal - PD-Lambda-4 System (v261, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v260 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for PD-Lambda-4 system, the
genome-level possession trait for a DefenseFinder-modeled anti-phage locus from
Vassallo et al.'s *E. coli* pangenome screen. DefenseFinder models PD-Lambda-4
with two required HMM profiles, `PD-Lambda-4__PD-Lambda-4_A` and
`PD-Lambda-4__PD-Lambda-4_B`.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for PD-Lambda-4 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1033800` is reserved for this one-row class cohort. The v260 cohort
used `METPO:1033700`, so v261 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope PD-Lambda-4 system record,
`pd_lambda_4_system` slug, `PD-Lambda-4__PD-Lambda-4_A`,
`PD-Lambda-4__PD-Lambda-4_B`, `traitmech:000384`,
`metpo_traitmech_v261`, or `METPO:1033800`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1033800` | PD-Lambda-4 system | `METPO:1016300` phage defense system |

PD-Lambda-4 system captures genome-level possession of a two-profile
DefenseFinder phage-defense locus experimentally linked to T4, LambdaVir,
SECphi27, and T7 protection when expressed in *E. coli*. It excludes the
individual PD-Lambda-4 genes or proteins, the DefenseFinder
`PD-Lambda-4__PD-Lambda-4_A` and `PD-Lambda-4__PD-Lambda-4_B` profiles, the
source key `PD-Lambda-4`, phage protection outside a complete PD-Lambda-4
locus, RefSeq example loci without experimental validation, sibling PD-Lambda
systems, prophages and mobile genetic elements as mobile elements, and other
phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual proteins, source database rows
naming the DefenseFinder model, HMM profiles, RefSeq example loci, and
protection against T4, LambdaVir, SECphi27, or T7 are shifted from this
organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  no exact external xrefs and related DefenseFinder profile labels.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000384` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000384` as traceability during the migration.

## Change Log

- v261, 2026-09: lifts `traitmech:000384 PD-Lambda-4 system` into the
  `METPO:1033800` block.
