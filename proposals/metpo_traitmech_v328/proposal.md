# METPO ROBOT Template Proposal - DS-27 System (v328, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-27 system, the
genome-level possession trait for the single-gene DefensePredictor-discovered
anti-phage locus from DeWeirdt et al.'s machine-learning search. DeWeirdt et
al. mapped the working identifier `SMEK` to DS-27, marked the cloned
transcriptional unit as defensive, and measured reduced RB69 bacteriophage
plaquing. The final Science Table S8 maps `SMEK` to the replicated DS-27
display name. The pinned DefenseFinder article registry maps DS-27 to the
DefensePredictor preprint, the pinned DefenseFinder HMM inventory records one
DS-27 custom profile, `DS-27__DS-27`, and the pinned DefenseFinder rules table
checked in this curation pass has no DS-27 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-27 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1040500` is reserved for this one-row class cohort. The v327 cohort used
`METPO:1040400`, so v328 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-27 TraitMech, METPO, history,
or prior proposal record, no `DS-27__DS-27` profile-key mention, no `SMEK`
source working identifier mention, no `WP_087896215.1` product-accession
mention, no `NZ_QOXX01000051.1` contig mention, no `ds_27_system` slug, no
`traitmech:000451`, no `metpo_traitmech_v328`, and no `METPO:1040500`
proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1040500` | DS-27 system | `METPO:1016300` phage defense system |

DS-27 system captures genome-level possession of the single-gene
DefensePredictor-discovered phage-defense transcriptional unit cataloged as
SMEK and represented by the DefenseFinder DS-27 custom HMM-profile row. It
excludes the SMEK source working identifier, the individual DS-27 gene or
protein, the DS-27 HMM profile row, cloned-transcriptional-unit plaquing
assays, the absent DS-27 HHpred-domain annotation, the absent DS-27 rule-level
DefenseFinder model, unresolved component activity, unresolved phage breadth,
and other DefensePredictor-discovered or phage-defense systems.

`traitmech:000451` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `SMEK` is kept as a related synonym
because it names the source working identifier, and `DS-27__DS-27` is kept as a
related synonym because it names a DefenseFinder profile key rather than the
genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-27` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000451` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000451` as traceability during the migration.

## Change Log

- v328, 2026-09: lifts `traitmech:000451 DS-27 system` into the
  `METPO:1040500` placeholder block.
