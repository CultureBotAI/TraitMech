# METPO ROBOT Template Proposal - Gao-TerY System (v237, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v236 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Gao-TerY system, the
genome-level possession trait for a `Gao_TerY` phage-defense locus modeled by
DefenseFinder as a three-profile system requiring `Gao_TerY__TerYA`,
`Gao_TerY__TerYB`, and `Gao_TerY__TerYC`. Gao et al. discovered widespread
antiviral gene cassettes with diverse enzymatic activities against specific
bacteriophages, and DefenseFinder maps `Gao_TerY` to that paper while pinning
the custom TerYA through TerYC profiles for the system.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Gao-TerY |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1031400` is reserved for this one-row class cohort. The v236 cohort used
`METPO:1031300`, so v237 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository. It found no exact same-scope record, `gao_tery_system` slug,
`Gao-TerY system` label, `Gao_TerY` key, TerY HMM profiles,
`traitmech:000360`, `metpo_traitmech_v237`, or `METPO:1031400` before this
cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1031400` | Gao-TerY system | `METPO:1016300` phage defense system |

Gao-TerY system captures genome-level possession of a `Gao_TerY` locus
represented by DefenseFinder as a three-profile model requiring
`Gao_TerY__TerYA`, `Gao_TerY__TerYB`, and `Gao_TerY__TerYC`. It excludes the
individual TerY HMM profiles; individual Gao-family genes or proteins; source
database rows naming one `Gao_TerY` model; other Gao-family systems; and other
phage-defense systems.

## External Mappings

No exact external mapping is proposed. The individual custom TerY profiles and
unresolved downstream antiviral activity are shifted from this organism-level
GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact synonyms, four related shifted labels, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000360` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000360` as traceability during the migration.

## Change Log

- v237, 2026-09: lifts `traitmech:000360 Gao-TerY system` into the
  `METPO:1031400` block.
