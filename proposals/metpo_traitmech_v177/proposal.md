# METPO ROBOT Template Proposal - AbiV System (v177, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v176 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for AbiV system, the
genome-level possession trait for an abortive-infection system in which an
organism possesses an `abiV` locus whose encoded AbiV protein can restrict
936-like or c2-like lactococcal phages by interfering with late phage DNA
maturation. The v91 cohort proposed the broader `abortive infection system`
parent for Abi defense families; v102 through v107 split AbiQ, ToxIN, AbiE,
AbiZ, AbiK, and AbiT into narrower children; and this cohort splits AbiV into
another narrower child.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for AbiV |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1025400` is reserved for this one-row class cohort. The v176 cohort used
`METPO:1025300`, so v177 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v177`, no live record used
`traitmech:000300`, and no prior proposal reserved `METPO:1025400`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1025400` | AbiV system | `METPO:1016800` abortive infection system |

AbiV system captures genome-level possession of an `abiV` locus whose product
can confer abortive-infection phage resistance to 936-like and c2-like
lactococcal phages. It excludes the individual `abiV` gene; the AbiV protein;
the DefenseFinder HMM profile; the source-paper `orf1` pre-name; the
pGhost9::ISS1 activation events; the pJH2 expression vector; 936, c2, or P335
phage specificity; unresolved AbiV phage triggers, host targets, c2-specific
outputs, and phage-escape routes; and other abortive-infection systems.

## External Mappings

No exact external mapping is proposed. The individual `abiV` gene, AbiV protein,
DefenseFinder HMM profile, experimental expression plasmids, activating
insertion events, phage host-range outputs, and unresolved AbiV molecular
mechanism are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  related DefenseFinder source label and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000300` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000300` as traceability during the migration.

## Change Log

- v177, 2026-09: lifts `traitmech:000300 AbiV system` into the
  `METPO:1025400` block.
