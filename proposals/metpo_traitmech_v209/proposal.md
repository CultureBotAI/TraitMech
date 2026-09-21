# METPO ROBOT Template Proposal - Nhi System (v209, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v208 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Nhi system, the
genome-level possession trait for an `nhi` nuclease-helicase immunity locus.
Bari et al. described Nhi as a single enzyme with nuclease and helicase
activities, showed that it protects against diverse staphylococcal phages and
prevents phage DNA accumulation, and inferred that Nhi targets and degrades
phage-specific replication intermediates. DefenseFinder models Nhi with one
required `Nhi__Nhi` profile.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Nhi |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1028600` is reserved for this one-row class cohort. The v208 cohort used
`METPO:1028500`, so v209 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository, plus the pinned DefenseFinder registries that supplied the
positive Nhi article, rule, and HMM rows used for candidate discovery. No exact
same-scope TraitMech or METPO record, `nhi_system` slug, `Nhi system` label,
`traitmech:000332`, `metpo_traitmech_v209`, `METPO:1028600`, or
`DOI:10.1016/j.chom.2022.03.001` was present before this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1028600` | Nhi system | `METPO:1016300` phage defense system |

Nhi system captures genome-level possession of an Nhi-family locus represented
by DefenseFinder's `Nhi__Nhi` HMM profile and exemplified by Bari et al.'s
single-enzyme nuclease-helicase immunity system. It excludes individual `nhi`
genes; Nhi enzymes; the individual DefenseFinder HMM profile; source database
rows naming one Nhi locus; unresolved phage triggers or exact
replication-intermediate substrates; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Nhi, the DefenseFinder HMM, individual
genes or enzymes, phage-specific replication-intermediate degradation, and
phage DNA accumulation prevention are shifted from this organism-level GENOMICS
possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  related shifted label, no exact synonyms, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000332` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000332` as traceability during the migration.

## Change Log

- v209, 2026-09: lifts `traitmech:000332 Nhi system` into the
  `METPO:1028600` block.
