# METPO ROBOT Template Proposal - RexAB System (v201, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v200 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for RexAB system, the
genome-level possession trait for a bacteriophage-lambda Rex-family
abortive-infection locus. Parma et al. described bacteriophage lambda `rexA`
and `rexB` as a two-component system that aborts lytic growth of bacterial
viruses. DefenseFinder maps the named `RexAB` namespace to required
`RexAB__RexA` and `RexAB__RexB` HMM profiles.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for RexAB |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1027800` is reserved for this one-row class cohort. The v200 cohort used
`METPO:1027700`, so v201 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository, plus the pinned DefenseFinder registries used for candidate
discovery. No exact same-scope record, `rexab_system` slug, `RexAB system`
label, `RexAB__RexA` or `RexAB__RexB` model row, `traitmech:000324`,
`metpo_traitmech_v201`, `METPO:1027800`, or `DOI:10.1101/gad.6.3.497`
was present before this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1027800` | RexAB system | `METPO:1016800` abortive infection system |

RexAB system captures genome-level possession of a bacteriophage-lambda
Rex-family locus represented by DefenseFinder's `RexAB__RexA` and
`RexAB__RexB` HMM profiles and exemplified by the rexA/rexB system that aborts
lytic growth of bacterial viruses. It excludes individual `rexA` and `rexB`
genes; RexA and RexB proteins; lambda prophages; the individual DefenseFinder
HMM profiles; source database rows naming one RexAB locus; sensitive-phage
exclusion outcomes; unresolved direct phage triggers; lambda self-exclusion
control; and generic abortive-infection systems.

## External Mappings

No exact external mapping is proposed. RexAB, RexA, RexB, bacteriophage lambda,
the DefenseFinder HMMs, individual phage-exclusion outcomes, and
abortive-infection processes are shifted from this organism-level GENOMICS
possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  related shifted label, no exact synonyms, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000324` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000324` as traceability during the migration.

## Change Log

- v201, 2026-09: lifts `traitmech:000324 RexAB system` into the
  `METPO:1027800` block.
