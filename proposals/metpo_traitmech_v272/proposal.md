# METPO ROBOT Template Proposal - PD-T7-1 System (v272, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v271 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for PD-T7-1 system, the
genome-level possession trait for a DefenseFinder-modeled anti-phage locus from
Vassallo et al.'s *E. coli* pangenome screen. DefenseFinder models PD-T7-1
with one required HMM profile, `PD-T7-1__PD-T7-1`.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for PD-T7-1 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1034900` is reserved for this one-row class cohort. The v271 cohort
used `METPO:1034800`, so v272 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope PD-T7-1 system record,
`pd_t7_1_system` slug, `PD-T7-1__PD-T7-1`, `traitmech:000395`,
`metpo_traitmech_v272`, or `METPO:1034900`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1034900` | PD-T7-1 system | `METPO:1016300` phage defense system |

PD-T7-1 system captures genome-level possession of a single-profile
DefenseFinder phage-defense locus experimentally linked to T7 protection when
expressed in *E. coli*. It excludes the individual PD-T7-1 gene or protein, the
DefenseFinder `PD-T7-1__PD-T7-1` profile, the source key `PD-T7-1`, phage
protection outside a complete PD-T7-1 locus, RefSeq example loci without
experimental validation, sibling PD-T7 systems, and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual proteins, source database rows
naming the DefenseFinder model, HMM profiles, RefSeq example loci, and protection
against T7 are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact external xrefs and related DefenseFinder profile labels.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000395` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000395` as traceability during the migration.

## Change Log

- v272, 2026-09: lifts `traitmech:000395 PD-T7-1 system` into the
  `METPO:1034900` block.
