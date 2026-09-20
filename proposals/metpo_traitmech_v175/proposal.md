# METPO ROBOT Template Proposal - Butters gp30-gp31 System (v175, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v174 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Butters gp30-gp31
system, the genome-level possession trait for a Butters gp30-gp31 anti-phage
locus. Mageeney et al. support a two-component system articulated by
interactions between Butters genes 30 and 31 that confers defense against
heterotypic phage infection by PurpleHaze or Alma, and DefenseFinder catalogs
Butters_gp30_gp31 with Butters_gp30 and Butters_gp31 HMM profile entries plus a
two-profile system rule.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Butters gp30-gp31 |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1025200` is reserved for this one-row class cohort. The v174 cohort used
`METPO:1025100`, so v175 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v175`, no live record used
`traitmech:000298`, and no prior proposal reserved `METPO:1025200`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1025200` | Butters gp30-gp31 system | `METPO:1016300` phage defense system |

Butters gp30-gp31 system captures genome-level possession of a Butters
gp30-gp31 locus cataloged by DefenseFinder under a Butters_gp30_gp31 model
namespace with Butters_gp30 and Butters_gp31 HMM profile entries. It excludes
individual gp30 or gp31 genes; Gp30 or Gp31 proteins; DefenseFinder HMM
profiles; the Butters prophage as a viral genome; homologous Sbash or CarolAnn
systems; recombinant Mycobacterium smegmatis strains expressing Butters gene 30
or 31; the gp30-independent Island3 defense; unresolved phage triggers; and
other phage-defense systems.

## External Mappings

No exact external mapping is proposed. The Butters prophage, gp30 or gp31
genes, Gp30 or Gp31 proteins, DefenseFinder HMMs, Sbash or CarolAnn homologous
systems, recombinant Butters 30/31 strains, and unresolved Butters gp30-gp31
activation outputs are shifted from this organism-level GENOMICS possession
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  related DefenseFinder source label and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000298` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000298` as traceability during the migration.

## Change Log

- v175, 2026-09: lifts `traitmech:000298 Butters gp30-gp31 system` into the
  `METPO:1025200` block.
