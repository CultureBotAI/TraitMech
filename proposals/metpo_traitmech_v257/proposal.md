# METPO ROBOT Template Proposal - GAPS2 System (v257, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v256 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for GAPS2 system, the
genome-level possession trait for a DefenseFinder-modeled, GMT-encoded
anti-phage locus from Mahata et al.'s Gamma-Mobile-Trio island work.
DefenseFinder models GAPS2 with one required HMM profile, `GAPS2__GAPS2`.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for GAPS2 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1033400` is reserved for this one-row class cohort. The v256 cohort
used `METPO:1033300`, so v257 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope GAPS2 system record,
`gaps2_system` slug, `GAPS2__GAPS2`, `traitmech:000380`,
`metpo_traitmech_v257`, or `METPO:1033400`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1033400` | GAPS2 system | `METPO:1016300` phage defense system |

GAPS2 system captures genome-level possession of a GMT-encoded GAPS2 locus
represented by DefenseFinder and experimentally linked to phage protection when
expressed in *E. coli*. It excludes individual GAPS2 genes and proteins, the
DefenseFinder `GAPS2__GAPS2` profile, the source key `GAPS2`, DNA BRCT domains,
phage protection outside a complete GAPS2 locus, RefSeq example loci without
experimental validation, sibling GAPS1/GAPS4/GAPS6 systems, Gamma-Mobile-Trio
islands as mobile elements, and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual proteins, source database
rows naming the DefenseFinder model, HMM profiles, RefSeq example loci, DNA
BRCT domains, and protection against P1-vir or lambda-vir are shifted from this
organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  no exact external xrefs and a related DefenseFinder profile label.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000380` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000380` as traceability during the migration.

## Change Log

- v257, 2026-09: lifts `traitmech:000380 GAPS2 system` into the
  `METPO:1033400` block.
