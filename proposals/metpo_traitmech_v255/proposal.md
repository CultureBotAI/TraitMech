# METPO ROBOT Template Proposal - PD-Lambda-2 System (v255, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v254 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for PD-Lambda-2 system,
the genome-level possession trait for a DefenseFinder-modeled anti-phage
locus from the Vassallo et al. *E. coli* pangenome functional selection.
DefenseFinder models PD-Lambda-2 with two mandatory HMM profiles,
`PD-Lambda-2__PD-Lambda-2_A` and `PD-Lambda-2__PD-Lambda-2_B`, and one
accessory profile, `PD-Lambda-2__PD-Lambda-2_C`.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for PD-Lambda-2 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1033200` is reserved for this one-row class cohort. The v254 cohort
used `METPO:1033100`, so v255 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope PD-Lambda-2 system record,
`pd_lambda_2_system` slug, `PD-Lambda-2` source key, `traitmech:000378`,
`metpo_traitmech_v255`, or `METPO:1033200`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1033200` | PD-Lambda-2 system | `METPO:1016300` phage defense system |

PD-Lambda-2 system captures genome-level possession of a PD-Lambda-2 locus
represented by DefenseFinder. It excludes individual PD-Lambda-2 A, B, or C
genes, individual PD-Lambda-2 A, B, or C proteins, the DefenseFinder
`PD-Lambda-2__PD-Lambda-2_A`, `PD-Lambda-2__PD-Lambda-2_B`, and
`PD-Lambda-2__PD-Lambda-2_C` profiles, the source key `PD-Lambda-2`,
protection against the listed phages outside a complete PD-Lambda-2 locus,
RefSeq example loci without experimental validation, and other PD-Lambda or
phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual proteins, source database
rows naming the DefenseFinder model, HMM profiles, RefSeq example loci, and
protection against LambdaVir, SECphi17, SECphi18, SECphi27, and T3 are
shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  no exact external xrefs and related DefenseFinder profile labels.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000378` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000378` as traceability during the migration.

## Change Log

- v255, 2026-09: lifts `traitmech:000378 PD-Lambda-2 system` into the
  `METPO:1033200` block.
