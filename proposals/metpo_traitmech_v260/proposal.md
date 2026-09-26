# METPO ROBOT Template Proposal - PD-Lambda-6 System (v260, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v259 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for PD-Lambda-6 system, the
genome-level possession trait for a DefenseFinder-modeled anti-phage locus from
Vassallo et al.'s *E. coli* pangenome screen. DefenseFinder models PD-Lambda-6
with one required HMM profile, `PD-Lambda-6__PD-Lambda-6`.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for PD-Lambda-6 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1033700` is reserved for this one-row class cohort. The v259 cohort
used `METPO:1033600`, so v260 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope PD-Lambda-6 system record,
`pd_lambda_6_system` slug, `PD-Lambda-6__PD-Lambda-6`,
`traitmech:000383`, `metpo_traitmech_v260`, or `METPO:1033700`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1033700` | PD-Lambda-6 system | `METPO:1016300` phage defense system |

PD-Lambda-6 system captures genome-level possession of a single-profile
DefenseFinder phage-defense locus experimentally linked to LambdaVir and T5
protection when expressed in *E. coli*. It excludes the individual PD-Lambda-6
gene or protein, the DefenseFinder `PD-Lambda-6__PD-Lambda-6` profile, the
source key `PD-Lambda-6`, phage protection outside a complete PD-Lambda-6
locus, RefSeq example loci without experimental validation, sibling PD-Lambda
systems, prophages and mobile genetic elements as mobile elements, and other
phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual proteins, source database rows
naming the DefenseFinder model, HMM profiles, RefSeq example loci, and
protection against LambdaVir or T5 are shifted from this organism-level
GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  no exact external xrefs and one related DefenseFinder profile label.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000383` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000383` as traceability during the migration.

## Change Log

- v260, 2026-09: lifts `traitmech:000383 PD-Lambda-6 system` into the
  `METPO:1033700` block.
