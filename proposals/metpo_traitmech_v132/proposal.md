# METPO ROBOT Template Proposal - Shango System (v132, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v131 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Shango system, the
genome-level possession trait for a bacterial antiphage defense locus named in
Millman et al. DefenseFinder models Shango with a mandatory SngA profile and
SngB/SngC accessory profile choices in its article registry, rules table, and
HMM inventory.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000255` was minted locally because METPO has no active exact Shango-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1020900` is reserved for this one-row class cohort. The v131 cohort used
`METPO:1020800`, so v132 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v132`, no live record used
`traitmech:000255`, and no prior proposal reserved `METPO:1020900`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1020900` | Shango system | `METPO:1016300` phage defense system |

Shango system captures genome-level possession of a Shango antiphage locus
represented by a mandatory SngA DefenseFinder profile and SngB/SngC accessory
profile choices. It excludes individual `sngA`, `sngB`, or `sngC` genes;
standalone SngA, SngB, or SngC proteins; unresolved molecular trigger or
effector activities; DefenseFinder HMM profiles; predicted source-database rows
naming one Shango locus; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual Shango genes, SngA/SngB/SngC
protein profiles, DefenseFinder HMMs, and predicted locus calls are shifted
from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact Shango synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000255` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000255` as traceability during the migration.

## Change Log

- v132, 2026-09: lifts `traitmech:000255 Shango system` into the
  `METPO:1020900` block.
