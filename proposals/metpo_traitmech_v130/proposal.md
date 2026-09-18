# METPO ROBOT Template Proposal - Menshen System (v130, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v129 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Menshen system, the
genome-level possession trait for a bacterial antiphage defense locus named in
Millman et al. DefenseFinder models Menshen with NsnA, NsnB, and NsnC profile
choices in its article registry, rules table, and HMM inventory.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000253` was minted locally because METPO has no active exact Menshen-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1020700` is reserved for this one-row class cohort. The v129 cohort used
`METPO:1020600`, so v130 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v130`, no live record used
`traitmech:000253`, and no prior proposal reserved `METPO:1020700`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1020700` | Menshen system | `METPO:1016300` phage defense system |

Menshen system captures genome-level possession of a Menshen antiphage locus
represented by NsnA, NsnB, and NsnC DefenseFinder profile choices. It excludes
individual `nsnA`, `nsnB`, or `nsnC` genes; standalone NsnA, NsnB, or NsnC
proteins; unresolved molecular trigger or effector activities; DefenseFinder
HMM profiles; predicted source-database rows naming one Menshen locus; and
other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual Menshen genes, NsnA/NsnB/NsnC
protein profiles, DefenseFinder HMMs, and predicted locus calls are shifted
from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact Menshen synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000253` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000253` as traceability during the migration.

## Change Log

- v130, 2026-09: lifts `traitmech:000253 Menshen system` into the
  `METPO:1020700` block.
