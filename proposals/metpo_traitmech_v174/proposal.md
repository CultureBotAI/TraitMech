# METPO ROBOT Template Proposal - MMB gp29-gp30 System (v174, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v173 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for MMB gp29-gp30
system, the genome-level possession trait for a MichelleMyBell gp29-gp30
anti-phage locus. Dedrick et al. show that an MMB 29-30 deletion loses
prophage-mediated defense and that recombinant MMB 29 and 30 reproduce the
MMB defense pattern, and DefenseFinder catalogs MMB_gp29_gp30 with gp29 and
gp30 HMM profile entries plus a two-profile system rule.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for MMB gp29-gp30 |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1025100` is reserved for this one-row class cohort. The v173 cohort used
`METPO:1025000`, so v174 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v174`, no live record used
`traitmech:000297`, and no prior proposal reserved `METPO:1025100`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1025100` | MMB gp29-gp30 system | `METPO:1016300` phage defense system |

MMB gp29-gp30 system captures genome-level possession of a MichelleMyBell
gp29-gp30 locus cataloged by DefenseFinder under an MMB_gp29_gp30 model
namespace with gp29 and gp30 HMM profile entries. It excludes individual gp29
or gp30 genes; Gp29 or Gp30 proteins; DefenseFinder HMM profiles; the
MichelleMyBell prophage as a viral genome; recombinant Mycobacterium smegmatis
strains expressing MMB genes 29 and 30; unresolved lytic triggers; unresolved
gp29-gp30 activation events; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. The MichelleMyBell prophage, gp29 or
gp30 genes, Gp29 or Gp30 proteins, DefenseFinder HMMs, recombinant MMB 29-30
strains, and unresolved MMB gp29-gp30 activation outputs are shifted from this
organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  related DefenseFinder source label and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000297` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000297` as traceability during the migration.

## Change Log

- v174, 2026-09: lifts `traitmech:000297 MMB gp29-gp30 system` into the
  `METPO:1025100` block.
