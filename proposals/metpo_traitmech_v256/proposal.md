# METPO ROBOT Template Proposal - GAPS4 System (v256, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v255 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for GAPS4 system, the
genome-level possession trait for a DefenseFinder-modeled, GMT-encoded
anti-phage locus from Mahata et al.'s Gamma-Mobile-Trio island work.
DefenseFinder models GAPS4 with two required HMM profiles, `GAPS4__GAPS4a`
and `GAPS4__GAPS4b`.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for GAPS4 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1033300` is reserved for this one-row class cohort. The v255 cohort
used `METPO:1033200`, so v256 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope GAPS4 system record,
`gaps4_system` slug, `GAPS4` source key, `GAPS4__GAPS4a`,
`GAPS4__GAPS4b`, `traitmech:000379`, `metpo_traitmech_v256`, or
`METPO:1033300`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1033300` | GAPS4 system | `METPO:1016300` phage defense system |

GAPS4 system captures genome-level possession of a GMT-encoded GAPS4 locus
represented by DefenseFinder and experimentally linked to phage protection when
expressed in *E. coli*. It excludes individual GAPS4a or GAPS4b genes and
proteins, the DefenseFinder `GAPS4__GAPS4a` and `GAPS4__GAPS4b` profiles,
the source key `GAPS4`, the PDDEXK domain, host DNA degradation, phage
protection outside a complete GAPS4 locus, RefSeq example loci without
experimental validation, sibling GAPS1/GAPS2/GAPS6 systems,
Gamma-Mobile-Trio islands as mobile elements, and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual proteins, source database
rows naming the DefenseFinder model, HMM profiles, RefSeq example loci, the
PDDEXK domain, host DNA degradation, and protection against T7, T4, P1-vir, or
lambda-vir are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  no exact external xrefs and related DefenseFinder profile labels.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000379` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000379` as traceability during the migration.

## Change Log

- v256, 2026-09: lifts `traitmech:000379 GAPS4 system` into the
  `METPO:1033300` block.
