# METPO ROBOT Template Proposal - AbiL System (v217, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v216 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for AbiL system, the
genome-level possession trait for a two-component AbiL abortive-infection locus
represented by DefenseFinder's AbiL model namespace and the mandatory
`AbiL__AbiLi` and `AbiL__AbiLii` profiles. Deng et al. characterized AbiL as a
novel phage abortive infection system from `Lactococcus lactis`; a recent FEMS
review lists AbiL among confirmed two-component lactococcal Abi-like systems
and compares AbiL with ATPase-plus-TOPRIM phage-defense systems while leaving
the exact mechanism unresolved. The pinned DefenseFinder snapshot contains
AbiL in its article registry, records the mandatory `AbiL__AbiLi` and
`AbiL__AbiLii` HMM rows in its HMM inventory, and models AbiL as a two-profile
system in its rules table.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for AbiL |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1029400` is reserved for this one-row class cohort. The v216 cohort used
`METPO:1029300`, so v217 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository for exact TraitMech/METPO records and prior proposal/history
mentions. Separately, the pinned DefenseFinder article registry, HMM inventory,
and rules table supplied the positive AbiL candidate rows used for candidate
discovery. No exact same-scope TraitMech or METPO record, `abil_system` slug,
`AbiL system` label, `AbiL__AbiLi` or `AbiL__AbiLii` profile row,
`traitmech:000340`, `metpo_traitmech_v217`, or `METPO:1029400` was present in
the repository before this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1029400` | AbiL system | `METPO:1016800` abortive infection system |

AbiL system captures genome-level possession of a two-component AbiL-family
locus represented by DefenseFinder's AbiL namespace and the mandatory
`AbiL__AbiLi` and `AbiL__AbiLii` profiles. It excludes the individual
AbiL__AbiLi and AbiL__AbiLii profiles; the accessory AbiL__AbiLi2 and
AbiL__AbiLii2 HMM rows; the `abiLi` and `abiLii` genes; unresolved ATPase and
TOPRIM nuclease activity predictions; the related PARIS mechanism; source
database rows naming one AbiL model; and other abortive-infection systems.

## External Mappings

No exact external mapping is proposed. `AbiL`, `AbiL__AbiLi`, and
`AbiL__AbiLii` are kept as related synonyms because they denote model/profile
names rather than true labels for the organism-level trait itself.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  three related model/profile synonyms and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000340` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000340` as traceability during the migration.

## Change Log

- v217, 2026-09: lifts `traitmech:000340 AbiL system` into the
  `METPO:1029400` block.
