# METPO ROBOT Template Proposal - PD-T4-4 System (v266, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v265 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for PD-T4-4 system, the
genome-level possession trait for a DefenseFinder-modeled anti-phage locus from
Vassallo et al.'s *E. coli* pangenome screen. DefenseFinder models PD-T4-4 with
two required HMM profiles, `PD-T4-4__PD-T4-4_A` and
`PD-T4-4__PD-T4-4_B`.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for PD-T4-4 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1034300` is reserved for this one-row class cohort. The v265 cohort
used `METPO:1034200`, so v266 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope PD-T4-4 system record,
`pd_t4_4_system` slug, `PD-T4-4__PD-T4-4_A`,
`PD-T4-4__PD-T4-4_B`, `traitmech:000389`, `metpo_traitmech_v266`,
or `METPO:1034300`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1034300` | PD-T4-4 system | `METPO:1016300` phage defense system |

PD-T4-4 system captures genome-level possession of a two-profile DefenseFinder
phage-defense locus experimentally linked to T2, T4, T6, and SECphi17
protection when expressed in *E. coli*. It excludes the individual PD-T4-4_A or
PD-T4-4_B genes or proteins, the DefenseFinder `PD-T4-4__PD-T4-4_A` and
`PD-T4-4__PD-T4-4_B` profiles, the source key `PD-T4-4`, phage protection
outside a complete PD-T4-4 locus, RefSeq example loci without experimental
validation, sibling PD-T4 systems, integrative and conjugative elements as
mobile elements, and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual proteins, source database rows
naming the DefenseFinder model, HMM profiles, RefSeq example loci, and protection
against T2, T4, T6, or SECphi17 are shifted from this organism-level GENOMICS
possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact external xrefs and related DefenseFinder profile labels.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000389` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000389` as traceability during the migration.

## Change Log

- v266, 2026-09: lifts `traitmech:000389 PD-T4-4 system` into the
  `METPO:1034300` block.
