# METPO ROBOT Template Proposal - AbiP2 System (v220, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v219 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for AbiP2 system, the
genome-level possession trait for a single-component AbiP2-family
reverse-transcriptase-like abortive infection locus represented by
DefenseFinder's AbiP2 model namespace and the mandatory `AbiP2__AbiP2`
profile. Odegrip et al. characterized the original P2-like-coliphage locus;
Mestre et al. defined the defense-associated UG/Abi reverse-transcriptase
family; the FEMS review explicitly places AbiP2 in that family; and Figiel et
al. structurally characterized Abi-P2 as a template-independent Abi polymerase.
The pinned DefenseFinder snapshot records the mandatory `AbiP2__AbiP2` HMM row
in its HMM inventory and models AbiP2 as a one-profile system in its rules
table.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for AbiP2 |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1029700` is reserved for this one-row class cohort. The v219 cohort used
`METPO:1029600`, so v220 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository for exact TraitMech/METPO records and prior proposal/history
mentions. Separately, the pinned DefenseFinder HMM inventory and rules table
supplied the positive AbiP2 candidate rows used for candidate discovery. No
exact same-scope TraitMech or METPO record, `abip2_system` slug, `AbiP2 system`
label, `AbiP2` or `AbiP2__AbiP2` profile row, `traitmech:000343`,
`metpo_traitmech_v220`, or `METPO:1029700` was present in the repository before
this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1029700` | AbiP2 system | `METPO:1016800` abortive infection system |

AbiP2 system captures genome-level possession of a
reverse-transcriptase-like AbiP2-family locus represented by DefenseFinder's
AbiP2 namespace and the mandatory `AbiP2__AbiP2` profile. It excludes the
individual AbiP2__AbiP2 profile; Abi-P2 proteins; P2 `orf570` genes; generic
reverse transcriptases; broader UG/Abi systems; AbiK-family systems; the
unrelated lactococcal AbiP system; unresolved AbiP2 phage triggers; unresolved
arrest or death routes; source database rows naming one AbiP2 model; and other
abortive-infection systems.

## External Mappings

No exact external mapping is proposed. `AbiP2` and `AbiP2__AbiP2` are kept as
related synonyms because they denote model/profile names rather than true labels
for the organism-level trait itself.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with two
  related model/profile synonyms and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000343` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000343` as traceability during the migration.

## Change Log

- v220, 2026-09: lifts `traitmech:000343 AbiP2 system` into the
  `METPO:1029700` block.
