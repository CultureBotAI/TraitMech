# METPO ROBOT Template Proposal - AbiG System (v183, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v182 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for AbiG system, the
genome-level possession trait for a two-gene lactococcal abortive-infection
system. O'Connor et al. identified AbiG as a plasmid pCI750-encoded mechanism
from *Lactococcus lactis* subsp. *cremoris* UC653, localized the Abi phenotype
to adjacent `abiGi` and `abiGii` open reading frames, found no block in phage
DNA replication, and later connected the system to inhibited phage sk1 and
late phage c2 RNA synthesis. DefenseFinder catalogs AbiG with a two-profile
rule requiring `AbiG__AbiGi` and `AbiG__AbiGii`.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for AbiG |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1026000` is reserved for this one-row class cohort. The v182 cohort used
`METPO:1025900`, so v183 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository,
excluding only `.git`, `.venv`, generated robot/page/app output, and embeddings.
No prior proposal reserved `metpo_traitmech_v183`, no live record used
`traitmech:000306`, and no prior proposal reserved `METPO:1026000`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1026000` | AbiG system | `METPO:1016800` abortive infection system |

AbiG system captures genome-level possession of a two-gene `abiG` locus whose
`abiGi` and `abiGii` open reading frames are represented by the DefenseFinder
`AbiG__AbiGi` and `AbiG__AbiGii` model components and exemplified by the
lactococcal pCI750 locus. It excludes the individual `abiGi` and `abiGii`
genes; AbiGi or AbiGii proteins; the pCI750 plasmid; individual DefenseFinder
HMM profiles; source database rows naming one AbiG locus; the RNA-synthesis
process affected during phage sk1 or late c2 infection; individual lactococcal
phage host-range outcomes; and other abortive-infection systems.

## External Mappings

No exact external mapping is proposed. AbiG, AbiGi, AbiGii, pCI750,
DefenseFinder HMMs, phage RNA synthesis, and downstream phage restriction
phenotypes are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with a
  related AbiG label and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000306` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000306` as traceability during the migration.

## Change Log

- v183, 2026-09: lifts `traitmech:000306 AbiG system` into the
  `METPO:1026000` block.
