# METPO ROBOT Template Proposal - PsyrTA System (v134, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v133 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for PsyrTA system, the
genome-level possession trait for a bacterial antiphage defense locus named in
Millman et al. DefenseFinder models PsyrTA with required PsyrA and PsyrT
profiles in its article registry, rules table, and HMM inventory.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000257` was minted locally because METPO has no active exact PsyrTA-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1021100` is reserved for this one-row class cohort. The v133 cohort used
`METPO:1021000`, so v134 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v134`, no live record used
`traitmech:000257`, and no prior proposal reserved `METPO:1021100`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1021100` | PsyrTA system | `METPO:1016300` phage defense system |

PsyrTA system captures genome-level possession of a PsyrTA antiphage locus
represented by PsyrA and PsyrT DefenseFinder profiles. It excludes individual
`psyrA` or `psyrT` genes; standalone PsyrA or PsyrT proteins; unresolved
molecular trigger or effector activities; DefenseFinder HMM profiles; predicted
source-database rows naming one PsyrTA locus; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual PsyrTA genes, PsyrA/PsyrT
protein profiles, DefenseFinder HMMs, and predicted locus calls are shifted
from this organism-level GENOMICS possession trait.

The pinned DefenseFinder registry row for PsyrTA uses the 2022 bioRxiv
preprint DOI/title used by its sibling Millman-system rows.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact PsyrTA synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000257` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000257` as traceability during the migration.

## Change Log

- v134, 2026-09: lifts `traitmech:000257 PsyrTA system` into the
  `METPO:1021100` block.
