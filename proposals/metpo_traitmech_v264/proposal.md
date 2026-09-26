# METPO ROBOT Template Proposal - PD-T4-2 System (v264, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v263 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for PD-T4-2 system, the
genome-level possession trait for a DefenseFinder-modeled anti-phage locus from
Vassallo et al.'s *E. coli* pangenome screen. DefenseFinder models PD-T4-2 with
two required HMM profiles, `PD-T4-2__PD-T4-2_A` and `PD-T4-2__PD-T4-2_B`.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for PD-T4-2 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1034100` is reserved for this one-row class cohort. The v263 cohort
used `METPO:1034000`, so v264 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope PD-T4-2 system record,
`pd_t4_2_system` slug, `PD-T4-2__PD-T4-2_A`, `PD-T4-2__PD-T4-2_B`,
`traitmech:000387`, `metpo_traitmech_v264`, or `METPO:1034100`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1034100` | PD-T4-2 system | `METPO:1016300` phage defense system |

PD-T4-2 system captures genome-level possession of a two-profile
DefenseFinder phage-defense locus experimentally linked to T2, T4, T6, T5, and
SECphi27 protection when expressed in *E. coli*. It excludes the individual
PD-T4-2_A or PD-T4-2_B genes or proteins, the DefenseFinder
`PD-T4-2__PD-T4-2_A` and `PD-T4-2__PD-T4-2_B` profiles, the source key
`PD-T4-2`, phage protection outside a complete PD-T4-2 locus, RefSeq example
loci without experimental validation, sibling PD-T4 systems, prophages and
mobile genetic elements as mobile elements, and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual proteins, source database rows
naming the DefenseFinder model, HMM profiles, RefSeq example loci, and
protection against T2, T4, T6, T5, or SECphi27 are shifted from this
organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact external xrefs and related DefenseFinder profile labels.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000387` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000387` as traceability during the migration.

## Change Log

- v264, 2026-09: lifts `traitmech:000387 PD-T4-2 system` into the
  `METPO:1034100` block.
