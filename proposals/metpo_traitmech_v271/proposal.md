# METPO ROBOT Template Proposal - PD-T4-10 System (v271, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v270 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for PD-T4-10 system, the
genome-level possession trait for a two-profile DefenseFinder abortive-infection
locus from Vassallo et al.'s *E. coli* pangenome screen. DefenseFinder models
PD-T4-10 with the two required HMM profiles `PD-T4-10__PD-T4-10_A` and
`PD-T4-10__PD-T4-10_B`.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for PD-T4-10 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1034800` is reserved for this one-row class cohort. The v270 cohort
used `METPO:1034700`, so v271 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope PD-T4-10 system record,
`pd_t4_10_system` slug, `PD-T4-10__PD-T4-10` profile namespace,
`traitmech:000394`, `metpo_traitmech_v271`, or `METPO:1034800`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1034800` | PD-T4-10 system | `METPO:1016800` abortive infection system |

PD-T4-10 system captures genome-level possession of a two-profile DefenseFinder
abortive-infection locus experimentally linked to T2, T4, T6, T5, and SECphi27
protection when expressed in *E. coli*. It excludes the individual PD-T4-10_A or
PD-T4-10_B gene or protein, the DefenseFinder `PD-T4-10__PD-T4-10_A` and
`PD-T4-10__PD-T4-10_B` profiles, the source key `PD-T4-10`, overlapping ORFs or
toxin-antitoxin mechanism hints outside a complete PD-T4-10 locus, phage
protection outside a complete PD-T4-10 locus, RefSeq example loci without
experimental validation, sibling PD-T4 systems, and other abortive-infection or
phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual proteins, source database rows
naming the DefenseFinder model, HMM profiles, RefSeq example loci,
toxin-antitoxin hints, and specific phage-protection phenotypes are shifted from
this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact external xrefs and related DefenseFinder profile labels.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000394` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000394` as traceability during the migration.

## Change Log

- v271, 2026-09: lifts `traitmech:000394 PD-T4-10 system` into the
  `METPO:1034800` block.
