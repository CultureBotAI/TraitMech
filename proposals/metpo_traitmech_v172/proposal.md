# METPO ROBOT Template Proposal - Charlie gp32 System (v172, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v171 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Charlie gp32 system,
the genome-level possession trait for a Charlie gp32 anti-phage locus.
Dedrick et al. identify Charlie 32 as the genetic determinant of heterotypic
Che9c defense, and DefenseFinder catalogs Charlie_gp32 with a gp32 HMM profile
entry.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Charlie gp32 |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1024900` is reserved for this one-row class cohort. The v171 cohort used
`METPO:1024800`, so v172 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v172`, no live record used
`traitmech:000295`, and no prior proposal reserved `METPO:1024900`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1024900` | Charlie gp32 system | `METPO:1016300` phage defense system |

Charlie gp32 system captures genome-level possession of a Charlie gp32 locus
cataloged by DefenseFinder under a Charlie_gp32 model namespace with a gp32 HMM
profile entry. It excludes individual gp32 genes; Gp32 proteins; DefenseFinder
HMM profiles; the Charlie prophage as a viral genome; recombinant Mycobacterium
smegmatis strains expressing Charlie 31-33; unresolved Che9c membrane-blocking
targets; unresolved homolog breadth; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. The Charlie prophage, gp32 genes, gp32
proteins, DefenseFinder HMMs, recombinant Charlie 31-33 strains, and unresolved
Charlie gp32 exclusion outputs are shifted from this organism-level GENOMICS
possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  related DefenseFinder source label and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000295` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000295` as traceability during the migration.

## Change Log

- v172, 2026-09: lifts `traitmech:000295 Charlie gp32 system` into the
  `METPO:1024900` block.
