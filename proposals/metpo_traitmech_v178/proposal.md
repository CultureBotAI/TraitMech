# METPO ROBOT Template Proposal - BstA System (v178, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v177 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for BstA system, the
genome-level possession trait for an abortive-infection system in which an
organism possesses a BstA-family phage-defense locus whose encoded BstA protein
can suppress lytic phage DNA replication and whose cognate anti-BstA `aba`
element can self-immunize the encoding prophage from BstA activity. The v91
cohort proposed the broader `abortive infection system` parent for Abi defense
families; v102 through v107 split AbiQ, ToxIN, AbiE, AbiZ, AbiK, and AbiT into
narrower children; v177 split AbiV into another narrower child; and this cohort
splits BstA into a prophage-encoded abortive-infection child.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for BstA |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1025500` is reserved for this one-row class cohort. The v177 cohort used
`METPO:1025400`, so v178 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v178`, no live record used
`traitmech:000301`, and no prior proposal reserved `METPO:1025500`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1025500` | BstA system | `METPO:1016800` abortive infection system |

BstA system captures genome-level possession of a BstA-family locus whose
encoded BstA protein can suppress lytic phage DNA replication and whose cognate
`aba` element can suppress BstA activity during lytic replication by the
encoding prophage. It excludes the individual `bstA` gene; BstA proteins; the
BstA__BstA DefenseFinder HMM profile; anti-BstA `aba` elements;
BstA-`aba` cognate self-immunity pairs; the BTP1 prophage as a viral genome;
BTP1 `gtrAC` LPS modification defense; BstA-sensitive or BstA-insensitive
phage host-range outputs; the unresolved phage triggers that recruit BstA to
phage DNA; the unresolved BstA DNA-replication targets; and generic
abortive-infection systems.

## External Mappings

No exact external mapping is proposed. The individual `bstA` gene, BstA protein,
BstA__BstA DefenseFinder HMM profile, `aba` DNA element, BstA-`aba`
self-immunity interaction, BTP1 prophage, BstA-sensitive phage host-range
outputs, and unresolved direct BstA target are shifted from this organism-level
GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  related DefenseFinder source label and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000301` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000301` as traceability during the migration.

## Change Log

- v178, 2026-09: lifts `traitmech:000301 BstA system` into the
  `METPO:1025500` block.
