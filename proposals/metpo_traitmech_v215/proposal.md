# METPO ROBOT Template Proposal - Abi2 System (v215, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v214 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Abi2 system, the
genome-level possession trait for a DefenseFinder Abi2 model namespace backed
by the mandatory `Abi2__Abi_2`/PF07751 profile. Chopin et al. define lactococcal
abortive-infection systems as phage-exclusion systems that block phage
multiplication and cause premature host-cell death after phage infection. Anba
et al. and Bidnenko et al. show that the AbiD1 member of the PF07751 Abi-like
family is a single-gene abortive-infection determinant that restricts
Lactococcus lactis phage bIL66. The pinned DefenseFinder snapshot contains
Abi2 in its article registry, records `Abi2__Abi_2` in its HMM inventory, and
models Abi2 as a one-profile system in its rules table.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Abi2 |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1029200` is reserved for this one-row class cohort. The v214 cohort used
`METPO:1029100`, so v215 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository for exact TraitMech/METPO records and prior proposal/history
mentions. Separately, the pinned DefenseFinder article registry, HMM inventory,
and rules table supplied the positive Abi2 candidate rows used for candidate
discovery. No exact same-scope TraitMech or METPO record, `abi2_system` slug,
`Abi2 system` label, `Abi2__Abi_2` profile row, `traitmech:000338`,
`metpo_traitmech_v215`, or `METPO:1029200` was present in the repository before
this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1029200` | Abi2 system | `METPO:1016800` abortive infection system |

Abi2 system captures genome-level possession of a single-component Abi-like
locus represented by DefenseFinder's Abi2 namespace and the mandatory
`Abi2__Abi_2`/PF07751 profile. It excludes the individual PF07751 profile;
AbiD1 or other Abi-like proteins; the abiD1 gene; unresolved AbiD/F-group
subfamilies; upstream regulatory RNAs; individual phage escape mutations;
source database rows naming one Abi2 model; and other abortive-infection
systems.

## External Mappings

No exact external mapping is proposed. `Abi2`, `Abi2__Abi_2`, and `Abi_2` are
kept as related synonyms because they denote DefenseFinder model/profile and
Pfam profile keys rather than true labels for the organism-level trait itself.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  three related model/profile synonyms and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000338` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000338` as traceability during the migration.

## Change Log

- v215, 2026-09: lifts `traitmech:000338 Abi2 system` into the
  `METPO:1029200` block.
