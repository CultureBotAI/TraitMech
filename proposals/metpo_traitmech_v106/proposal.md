# METPO ROBOT Template Proposal - AbiK System (v106, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v105 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the AbiK system, the
genome-level possession trait for an abortive-infection system in which an
organism possesses an `abiK` locus encoding a reverse-transcriptase-related
polymerase that uses conserved RT motifs for phage resistance and restricts
936/P335 lactococcal phage propagation. The v91 cohort proposed the broader
`abortive infection system` parent for Abi defense families; v102 split AbiQ
into its own narrower child; v103 split ToxIN into its own narrower child; v104
split AbiE into its own narrower child; v105 split AbiZ into its own narrower
child; and this cohort splits AbiK into its own narrower child.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000229` was minted locally because METPO has no active exact AbiK-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1018300` is reserved for this one-row class cohort. The v105 cohort used
`METPO:1018200`, so v106 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v106`, no live record used
`traitmech:000229`, and no prior proposal reserved `METPO:1018300` beyond the
v105 skill note pointing v106 at this block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1018300` | AbiK system | `METPO:1016800` abortive infection system |

AbiK system captures genome-level possession of an `abiK` locus encoding a
reverse-transcriptase-related AbiK polymerase that uses conserved RT motifs for
phage resistance and restricts 936/P335 lactococcal phage propagation. It
excludes individual `abiK` genes, AbiK proteins, AbiK RT motifs or polymerase
activity without direct Abi evidence, phage Sak escape proteins, AbiA systems,
AbiE systems, AbiQ systems, ToxIN systems, AbiZ systems, generic abortive
infection systems, and source database rows naming one Abi locus.

## External Mappings

No exact external mapping is proposed. Individual `abiK` genes, AbiK proteins,
AbiK RT-motif or DNA-polymerization assays without AbiK system evidence, phage
Sak escape proteins, and broader abortive-infection records are shifted from
this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with no
  exact AbiK-system synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000229` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000229` as traceability during the migration.

## Change Log

- v106, 2026-09: lifts `traitmech:000229 AbiK system` into the
  `METPO:1018300` block.
