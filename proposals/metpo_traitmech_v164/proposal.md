# METPO ROBOT Template Proposal - Geb System (v164, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v163 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Geb system, the
genome-level possession trait for a Geb anti-phage locus. Mordret et al.
reported a protein- and genomic-language-model workflow that discovered and
experimentally validated six Actinomycetota defense systems with novel
antiphage proteins, and DefenseFinder catalogs Geb with GebA1 and GebA2 HMM
profile entries.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Geb |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1024100` is reserved for this one-row class cohort. The v163 cohort used
`METPO:1024000`, so v164 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v164`, no live record used
`traitmech:000287`, and no prior proposal reserved `METPO:1024100`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1024100` | Geb system | `METPO:1016300` phage defense system |

Geb system captures genome-level possession of a Geb locus cataloged by
DefenseFinder under a Geb model namespace with GebA1 and GebA2 HMM profile
entries. It excludes individual GebA genes; GebA proteins; DefenseFinder HMM
profiles; predicted source-database rows naming one Geb locus; unresolved Geb
trigger or effector activities; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. GebA genes, their corresponding
proteins, DefenseFinder HMMs, and unresolved Geb molecular outputs are shifted
from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  exact Geb synonym, two related GebA source-profile labels, and no exact
  external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000287` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000287` as traceability during the migration.

## Change Log

- v164, 2026-09: lifts `traitmech:000287 Geb system` into the
  `METPO:1024100` block.
