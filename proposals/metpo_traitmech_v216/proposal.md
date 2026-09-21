# METPO ROBOT Template Proposal - AbiJ System (v216, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v215 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for AbiJ system, the
genome-level possession trait for an AbiJ abortive-infection locus represented
by DefenseFinder's AbiJ model namespace and the mandatory `AbiJ__AbiJ` profile.
Deng et al. first described a plasmid-encoded phage abortive infection system
from `Lactococcus lactis` biovar. `diacetylactis`; a recent FEMS review
summarizes AbiJ as a lactococcal Abi-like system, records `abi-859` as a
related name, and explicitly leaves AbiJ molecular mechanism unresolved.
Mosterd et al. include AbiJ among distinct plasmid-encoded lactococcal
phage-resistance systems in an escape-mutant screen. The pinned DefenseFinder
snapshot contains AbiJ in its article registry, records `AbiJ__AbiJ` in its HMM
inventory, and models AbiJ as a one-profile system in its rules table.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for AbiJ |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1029300` is reserved for this one-row class cohort. The v215 cohort used
`METPO:1029200`, so v216 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository for exact TraitMech/METPO records and prior proposal/history
mentions. Separately, the pinned DefenseFinder article registry, HMM inventory,
and rules table supplied the positive AbiJ candidate rows used for candidate
discovery. No exact same-scope TraitMech or METPO record, `abij_system` slug,
`AbiJ system` label, `AbiJ__AbiJ` profile row, `traitmech:000339`,
`metpo_traitmech_v216`, or `METPO:1029300` was present in the repository before
this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1029300` | AbiJ system | `METPO:1016800` abortive infection system |

AbiJ system captures genome-level possession of an AbiJ-family locus represented
by DefenseFinder's AbiJ namespace and the mandatory `AbiJ__AbiJ` profile. It
excludes the individual AbiJ__AbiJ profile; the abiJ gene; unresolved
HEPN-domain predictions; the AbiA escape-mutant route that can also bypass
AbiJ; individual phage escape mutations; source database rows naming one AbiJ
model; and other abortive-infection systems.

## External Mappings

No exact external mapping is proposed. `AbiJ`, `AbiJ__AbiJ`, and `abi-859` are
kept as related synonyms because they denote model/profile/source names rather
than true labels for the organism-level trait itself.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  three related model/profile synonyms and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000339` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000339` as traceability during the migration.

## Change Log

- v216, 2026-09: lifts `traitmech:000339 AbiJ system` into the
  `METPO:1029300` block.
