# METPO ROBOT Template Proposal - AbiO System (v219, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v218 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for AbiO system, the
genome-level possession trait for a single-component AbiO-family abortive
infection locus represented by DefenseFinder's AbiO model namespace and the
mandatory `AbiO__AbiO` profile. Prevots and Ritzenthaler characterized the
lactococcal `abiO` locus; a recent FEMS review retains AbiO among
experimentally confirmed lactococcal Abi-like systems, summarizes predicted
restriction-endonuclease-like and SF1B-helicase-like domains, and leaves the
exact trigger and effector mechanism unresolved. The pinned DefenseFinder
snapshot contains AbiO in its article registry, records the mandatory
`AbiO__AbiO` HMM row in its HMM inventory, and models AbiO as a one-profile
system in its rules table.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for AbiO |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1029600` is reserved for this one-row class cohort. The v218 cohort used
`METPO:1029500`, so v219 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository for exact TraitMech/METPO records and prior proposal/history
mentions. Separately, the pinned DefenseFinder article registry, HMM inventory,
and rules table supplied the positive AbiO candidate rows used for candidate
discovery. No exact same-scope TraitMech or METPO record, `abio_system` slug,
`AbiO system` label, `AbiO` or `AbiO__AbiO` profile row, `traitmech:000342`,
`metpo_traitmech_v219`, or `METPO:1029600` was present in the repository before
this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1029600` | AbiO system | `METPO:1016800` abortive infection system |

AbiO system captures genome-level possession of a single-component AbiO-family
locus represented by DefenseFinder's AbiO namespace and the mandatory
`AbiO__AbiO` profile. It excludes the individual AbiO__AbiO profile; the `abiO`
gene; predicted restriction-endonuclease or helicase interpretations;
unresolved AbiO phage triggers; unresolved arrest or death routes; source
database rows naming one AbiO model; and other abortive-infection systems.

## External Mappings

No exact external mapping is proposed. `AbiO` and `AbiO__AbiO` are kept as
related synonyms because they denote model/profile names rather than true labels
for the organism-level trait itself.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with two
  related model/profile synonyms and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000342` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000342` as traceability during the migration.

## Change Log

- v219, 2026-09: lifts `traitmech:000342 AbiO system` into the
  `METPO:1029600` block.
