# METPO ROBOT Template Proposal - EcoKMcrA System (v386, 2026-10)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for EcoKMcrA system, the
genome-level possession trait for an EcoKMcrA Type IV
modification-dependent restriction locus. Czapinska et al. support E. coli McrA
as EcoKMcrA, a methylcytosine- and hydroxymethylcytosine-dependent restriction
endonuclease whose cellular DNA restriction is impaired by nuclease-active-site
mutations. The pinned DefenseFinder article registry maps `EcoKMcrA` to the
same DOI, while the pinned HMM inventory and rules table have no exact EcoKMcrA
row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for EcoKMcrA system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1046300` is reserved for this one-row class cohort. The v385 cohort used
`METPO:1046200`, so v386 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope EcoKMcrA record,
`ecokmcra_system` slug, `traitmech:000509`, `METPO:1046300`,
`metpo_traitmech_v386`, Czapinska et al. DOI `10.1093/nar/gky731`, title
`Activity and structure of EcoKMcrA`, or DefenseFinder source key `EcoKMcrA`.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1046300` | EcoKMcrA system | `METPO:1045000` type IV modification-dependent restriction system |

EcoKMcrA system captures genome-level possession of an EcoKMcrA `mcrA`
Type IV modification-dependent restriction locus that acts on DNA modified in
the correct sequence context through an EcoKMcrA nuclease-active-site-dependent
activity. It excludes the broader McrA family, individual EcoKMcrA proteins,
individual `mcrA` genes, McrA nuclease activity outside a complete
organism-level Type IV anti-phage system, individual methylcytosine or
hydroxymethylcytosine DNA substrate classes, and the DefenseFinder `EcoKMcrA`
source key outside a complete organism-level system.

`traitmech:000509` is a direct local child of `traitmech:000496` type IV
modification-dependent restriction system. This proposal uses `METPO:1045000`,
the v373 placeholder for `traitmech:000496`.

## External Mappings

No exact external mapping is proposed. Individual EcoKMcrA proteins, individual
`mcrA` genes, the broader McrA family, specific methylcytosine or
hydroxymethylcytosine DNA target classes, and the DefenseFinder article-registry
key are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000509` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000509` as traceability during the migration.

## Change Log

- v386, 2026-10: lifts `traitmech:000509 EcoKMcrA system` into the
  `METPO:1046300` placeholder block.
