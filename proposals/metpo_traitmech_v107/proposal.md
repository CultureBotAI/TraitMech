# METPO ROBOT Template Proposal - AbiT System (v107, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v106 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the AbiT system, the
genome-level possession trait for an abortive-infection system in which an
organism possesses the two-gene pED1 `abiT` locus whose constitutively
cotranscribed `abiTi` and `abiTii` genes encode an AbiTi-AbiTii
phage-resistance module that acts late in the 936/P335 lactococcal phage lytic
cycle. The v91 cohort proposed the broader `abortive infection system` parent
for Abi defense families; v102 split AbiQ into its own narrower child; v103
split ToxIN into its own narrower child; v104 split AbiE into its own narrower
child; v105 split AbiZ into its own narrower child; v106 split AbiK into its own
narrower child; and this cohort splits AbiT into its own narrower child.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000230` was minted locally because METPO has no active exact AbiT-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1018400` is reserved for this one-row class cohort. The v106 cohort used
`METPO:1018300`, so v107 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No live record used `traitmech:000230`, no prior proposal reserved
`metpo_traitmech_v107`, no prior proposal reserved `METPO:1018400` beyond the
v106 skill and history notes pointing v107 at this block, and no exact AbiT
system record was already live.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1018400` | AbiT system | `METPO:1016800` abortive infection system |

AbiT system captures genome-level possession of the `abiT` locus whose `abiTi`
and `abiTii` host genes confer abortive-infection phage resistance against 936
and P335 lactococcal phages and act at a late phage-development stage. It
excludes individual `abiTi` or `abiTii` genes, AbiTi or AbiTii proteins,
936/P335 phage early genes or major capsid proteins that modulate AbiT
sensitivity, AbiE systems, AbiK systems, AbiQ systems, AbiZ systems, ToxIN
systems, generic abortive infection systems, and source database rows naming one
Abi locus.

## External Mappings

No exact external mapping is proposed. Individual host `abiT` genes, their
encoded proteins, phage escape determinants, and broader abortive-infection
records are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with no
  exact AbiT-system synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000230` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000230` as traceability during the migration.

## Change Log

- v107, 2026-09: lifts `traitmech:000230 AbiT system` into the
  `METPO:1018400` block.
