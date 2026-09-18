# METPO ROBOT Template Proposal - Dodola System (v129, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v128 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Dodola system, the
genome-level possession trait for a bacterial antiphage defense locus named in
Millman et al. DefenseFinder models Dodola as a two-component system
represented by DolA and DolB profiles in its article registry, rules table, and
HMM inventory.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000252` was minted locally because METPO has no active exact Dodola-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1020600` is reserved for this one-row class cohort. The v128 cohort used
`METPO:1020500`, so v129 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v129`, no live record used
`traitmech:000252`, and no prior proposal reserved `METPO:1020600`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1020600` | Dodola system | `METPO:1016300` phage defense system |

Dodola system captures genome-level possession of a two-component Dodola
antiphage locus represented by DolA and DolB DefenseFinder profiles. It excludes
individual `dolA` or `dolB` genes; standalone DolA or DolB proteins; unresolved
molecular trigger or effector activities; DefenseFinder HMM profiles; predicted
source-database rows naming one Dodola locus; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual Dodola genes, DolA/DolB
protein profiles, DefenseFinder HMMs, and predicted locus calls are shifted
from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact Dodola synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000252` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000252` as traceability during the migration.

## Change Log

- v129, 2026-09: lifts `traitmech:000252 Dodola system` into the
  `METPO:1020600` block.
