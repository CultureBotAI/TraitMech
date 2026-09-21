# METPO ROBOT Template Proposal - AbiN System (v218, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v217 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for AbiN system, the
genome-level possession trait for a single-component AbiN-family abortive
infection locus represented by DefenseFinder's AbiN model namespace and the
mandatory `AbiN__AbiN` profile. Prevots et al. characterized the chromosomal
`abiN` locus in `Lactococcus lactis` subsp. `cremoris` S114; a recent FEMS
review retains AbiN among experimentally confirmed lactococcal Abi-like systems
but leaves the affected phage-cycle step, escape route, and arrest or death
mechanism unresolved. The pinned DefenseFinder snapshot contains AbiN in its
article registry, records the mandatory `AbiN__AbiN` HMM row in its HMM
inventory, and models AbiN as a one-profile system in its rules table.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for AbiN |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1029500` is reserved for this one-row class cohort. The v217 cohort used
`METPO:1029400`, so v218 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository for exact TraitMech/METPO records and prior proposal/history
mentions. Separately, the pinned DefenseFinder article registry, HMM inventory,
and rules table supplied the positive AbiN candidate rows used for candidate
discovery. No exact same-scope TraitMech or METPO record, `abin_system` slug,
`AbiN system` label, `AbiN` or `AbiN__AbiN` profile row, `traitmech:000341`,
`metpo_traitmech_v218`, or `METPO:1029500` was present in the repository before
this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1029500` | AbiN system | `METPO:1016800` abortive infection system |

AbiN system captures genome-level possession of a single-component AbiN-family
locus represented by DefenseFinder's AbiN namespace and the mandatory
`AbiN__AbiN` profile. It excludes the individual AbiN__AbiN profile; the
`abiN` gene; predicted periplasmic ligand-binding sensor-domain interpretations;
unresolved AbiN phage triggers; unresolved phage lytic-cycle, arrest, or death
routes; source database rows naming one AbiN model; and other abortive-infection
systems.

## External Mappings

No exact external mapping is proposed. `AbiN` and `AbiN__AbiN` are kept as
related synonyms because they denote model/profile names rather than true labels
for the organism-level trait itself.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with two
  related model/profile synonyms and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000341` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000341` as traceability during the migration.

## Change Log

- v218, 2026-09: lifts `traitmech:000341 AbiN system` into the
  `METPO:1029500` block.
