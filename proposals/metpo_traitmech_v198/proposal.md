# METPO ROBOT Template Proposal - AbiU System (v198, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v197 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for AbiU system, the
genome-level possession trait for an `abiU` abortive-infection locus.
Dai et al. identified and characterized AbiU from *Lactococcus lactis*
LL51-1, showed that AbiU confers resistance to representative c2, 936, and
P335 lactococcal phages, and connected AbiU with delayed transcription of
phages 712 and c2. DefenseFinder models AbiU with one required `AbiU__AbiU`
profile.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for AbiU |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1027500` is reserved for this one-row class cohort. The v197 cohort used
`METPO:1027400`, so v198 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository, plus the pinned DefenseFinder registries used for candidate
discovery. No exact same-scope record, `abiu_system` slug, `AbiU system` label,
`AbiU__AbiU` model row, `traitmech:000321`, `metpo_traitmech_v198`,
`METPO:1027500`, `DOI:10.1128/AEM.67.11.5225-5232.2001`, `PMID:11679349`, or
`PMC93294` was present before this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1027500` | AbiU system | `METPO:1016800` abortive infection system |

AbiU system captures genome-level possession of an `abiU` locus represented by
DefenseFinder's `AbiU__AbiU` HMM profile and exemplified by the lactococcal
LL51-1 determinant. It excludes the individual `abiU1` and `abiU2` genes; AbiU1
or AbiU2 proteins; pND001 and pND002 plasmids; the individual DefenseFinder HMM
profile; source database rows naming one AbiU locus; individual lactococcal
phage host-range outcomes; delayed-phage-transcription processes; unresolved
AbiU triggers or direct transcription targets; and other abortive-infection
systems.

## External Mappings

No exact external mapping is proposed. AbiU, AbiU1, AbiU2, pND001, pND002, the
DefenseFinder HMM, individual phage-resistance outcomes, and delayed
transcription processes are shifted from this organism-level GENOMICS
possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  related shifted label, no exact synonyms, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000321` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000321` as traceability during the migration.

## Change Log

- v198, 2026-09: lifts `traitmech:000321 AbiU system` into the
  `METPO:1027500` block.
