# METPO ROBOT Template Proposal - PD-T4-6 System (v268, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v267 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for PD-T4-6 system, the
genome-level possession trait for a DefenseFinder-modeled anti-phage locus from
Vassallo et al.'s *E. coli* pangenome screen. DefenseFinder models PD-T4-6 with
one required HMM profile, `PD-T4-6__PD-T4-6`.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for PD-T4-6 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1034500` is reserved for this one-row class cohort. The v267 cohort
used `METPO:1034400`, so v268 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope PD-T4-6 system record,
`pd_t4_6_system` slug, `PD-T4-6__PD-T4-6`, `traitmech:000391`,
`metpo_traitmech_v268`, or `METPO:1034500`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1034500` | PD-T4-6 system | `METPO:1016300` phage defense system |

PD-T4-6 system captures genome-level possession of a single-profile DefenseFinder
phage-defense locus experimentally linked to T2, T4, and T6 protection when
expressed in *E. coli*. It excludes the individual PD-T4-6 gene or protein, the
DefenseFinder `PD-T4-6__PD-T4-6` profile, the source key `PD-T4-6`, phage
protection outside a complete PD-T4-6 locus, RefSeq example loci without
experimental validation, sibling PD-T4 systems, and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual proteins, source database rows
naming the DefenseFinder model, HMM profiles, RefSeq example loci, and protection
against T2, T4, or T6 are shifted from this organism-level GENOMICS possession
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact external xrefs and related DefenseFinder profile labels.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000391` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000391` as traceability during the migration.

## Change Log

- v268, 2026-09: lifts `traitmech:000391 PD-T4-6 system` into the
  `METPO:1034500` block.
