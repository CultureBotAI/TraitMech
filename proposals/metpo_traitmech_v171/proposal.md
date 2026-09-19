# METPO ROBOT Template Proposal - Panchino gp28 System (v171, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v170 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Panchino gp28 system,
the genome-level possession trait for a Panchino gp28 anti-phage locus.
Dedrick et al. identify Panchino gp28 as a prophage-expressed restriction
system candidate, and DefenseFinder catalogs Panchino_gp28 with a gp28 HMM
profile entry.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Panchino gp28 |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1024800` is reserved for this one-row class cohort. The v170 cohort used
`METPO:1024700`, so v171 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v171`, no live record used
`traitmech:000294`, and no prior proposal reserved `METPO:1024800`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1024800` | Panchino gp28 system | `METPO:1016300` phage defense system |

Panchino gp28 system captures genome-level possession of a Panchino gp28 locus
cataloged by DefenseFinder under a Panchino_gp28 model namespace with a gp28 HMM
profile entry. It excludes individual gp28 genes; Gp28 proteins; DefenseFinder
HMM profiles; the Panchino prophage as a viral genome; recombinant
Mycobacterium smegmatis strains expressing Panchino 28; unresolved restriction
targets or methylation requirements; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. The Panchino prophage, gp28 genes, gp28
proteins, DefenseFinder HMMs, and unresolved Panchino gp28 restriction outputs
are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  exact Panchino_gp28 synonym, one related gp28 source-profile label, and no
  exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000294` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000294` as traceability during the migration.

## Change Log

- v171, 2026-09: lifts `traitmech:000294 Panchino gp28 system` into the
  `METPO:1024800` block.
