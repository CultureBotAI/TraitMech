# METPO ROBOT Template Proposal - GAPS6 System (v258, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v257 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for GAPS6 system, the
genome-level possession trait for a DefenseFinder-modeled, GMT-encoded
anti-phage locus from Mahata et al.'s Gamma-Mobile-Trio island work.
DefenseFinder models GAPS6 with two required HMM profiles, `GAPS6__GAPS6a`
and `GAPS6__GAPS6b`.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for GAPS6 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1033500` is reserved for this one-row class cohort. The v257 cohort
used `METPO:1033400`, so v258 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope GAPS6 system record,
`gaps6_system` slug, `GAPS6__GAPS6a`, `GAPS6__GAPS6b`,
`traitmech:000381`, `metpo_traitmech_v258`, or `METPO:1033500`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1033500` | GAPS6 system | `METPO:1016300` phage defense system |

GAPS6 system captures genome-level possession of a GMT-encoded GAPS6 locus
represented by DefenseFinder and experimentally linked to phage protection when
expressed in *E. coli*. It excludes individual GAPS6a or GAPS6b genes and
proteins, the DefenseFinder `GAPS6__GAPS6a` and `GAPS6__GAPS6b` profiles, the
source key `GAPS6`, TPR repeats, PINc ribonuclease domains, PINc-domain activity
outside a complete GAPS6 locus, phage protection outside a complete GAPS6 locus,
RefSeq example loci without experimental validation, sibling GAPS1/GAPS2/GAPS4
systems, Gamma-Mobile-Trio islands as mobile elements, and other phage-defense
systems.

## External Mappings

No exact external mapping is proposed. Individual proteins, source database
rows naming the DefenseFinder model, HMM profiles, RefSeq example loci, TPR
repeats, PINc domains, and protection against T7, T4, P1-vir, or lambda-vir are
shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  no exact external xrefs and two related DefenseFinder profile labels.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000381` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000381` as traceability during the migration.

## Change Log

- v258, 2026-09: lifts `traitmech:000381 GAPS6 system` into the
  `METPO:1033500` block.
