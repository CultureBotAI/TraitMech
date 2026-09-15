# METPO ROBOT Template Proposal - AbiZ System (v105, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v104 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the AbiZ system, the
genome-level possession trait for an abortive-infection system in which an
organism possesses an `abiZ` locus encoding a membrane-associated lactococcal
phage-resistance determinant that accelerates infected-cell lysis through
AbiZ-enhanced holin/lysin activity and restricts P335 phage propagation. The
v91 cohort proposed the broader `abortive infection system` parent for Abi
defense families; v102 split AbiQ into its own narrower child; v103 split ToxIN
into its own narrower child; v104 split AbiE into its own narrower child; and
this cohort splits AbiZ into its own narrower child.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000228` was minted locally because METPO has no active exact AbiZ-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1018200` is reserved for this one-row class cohort. The v104 cohort used
`METPO:1018100`, so v105 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v105`, no live record used
`traitmech:000228`, and no prior proposal reserved `METPO:1018200` beyond the
v104 skill note pointing v105 at this block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1018200` | AbiZ system | `METPO:1016800` abortive infection system |

AbiZ system captures genome-level possession of an `abiZ` locus encoding a
membrane-associated lactococcal phage-resistance determinant that accelerates
infected-cell lysis through AbiZ-enhanced holin/lysin activity and restricts
P335 phage propagation. It excludes individual `abiZ` genes, AbiZ proteins, the
`pTRK914` experimental plasmid, AbiA or LlaI defenses coencoded on `pTR2030`,
holin/lysin lysis without AbiZ, AbiZ escape phages, ToxIN systems, AbiQ
systems, AbiE systems, generic abortive infection systems, and source database
rows naming one Abi locus.

## External Mappings

No exact external mapping is proposed. Individual `abiZ` genes, AbiZ proteins,
the `pTRK914` tool plasmid, holin/lysin lysis assays without AbiZ, and broader
abortive-infection records are shifted from this organism-level GENOMICS
possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with no
  exact AbiZ-system synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000228` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000228` as traceability during the migration.

## Change Log

- v105, 2026-09: lifts `traitmech:000228 AbiZ system` into the
  `METPO:1018200` block.
