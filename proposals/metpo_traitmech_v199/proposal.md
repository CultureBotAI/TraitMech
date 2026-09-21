# METPO ROBOT Template Proposal - AbiAlpha System (v199, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v198 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for AbiAlpha system, the
genome-level possession trait for an abi-alpha-family abortive-infection locus.
Lossouarn et al. identified the Enterococcus faecalis V583 prophage 6
determinant later represented by the DefenseFinder `AbiAlpha` namespace, showed
that ef2833 is responsible for the abortive mechanism, and linked the
DUF4393/PF14337-family system to perturbation of the Idefix lytic cycle and
premature lysis of infected E. faecalis. DefenseFinder maps AbiAlpha to the
`AbiAlpha__AbiAlpha` HMM profile.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for AbiAlpha |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1027600` is reserved for this one-row class cohort. The v198 cohort used
`METPO:1027500`, so v199 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository, plus the pinned DefenseFinder registries used for candidate
discovery. No exact same-scope record, `abialpha_system` slug, `AbiAlpha
system` label, `AbiAlpha__AbiAlpha` model row, `DUF4393`, `PF14337`,
`traitmech:000322`, `metpo_traitmech_v199`, `METPO:1027600`,
`DOI:10.3390/v11010048`, `PMID:30634666`, or `PMC6356687` was present before
this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1027600` | AbiAlpha system | `METPO:1016800` abortive infection system |

AbiAlpha system captures genome-level possession of an abi-alpha-family locus
represented by DefenseFinder's `AbiAlpha__AbiAlpha` HMM profile and exemplified
by the Enterococcus faecalis V583 prophage 6 determinant. It
excludes the individual `abi-alpha` or `ef2833` gene; AbiAlpha proteins; the
DUF4393/PF14337 domain and HMM profile; V583 prophage 6 itself; individual
Idefix host-range outcomes; Idefix adsorption phenotypes; premature-lysis
processes; unresolved direct AbiAlpha lysis targets; and other
abortive-infection systems.

## External Mappings

No exact external mapping is proposed. AbiAlpha, ef2833, V583 prophage 6,
DUF4393, PF14337, the DefenseFinder HMM, individual Idefix-resistance outcomes,
and premature-lysis processes are shifted from this organism-level GENOMICS
possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  related shifted label, no exact synonyms, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000322` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000322` as traceability during the migration.

## Change Log

- v199, 2026-09: lifts `traitmech:000322 AbiAlpha system` into the
  `METPO:1027600` block.
