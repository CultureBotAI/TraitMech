# METPO ROBOT Template Proposal - DS-43 System (v345, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-43 system, the
genome-level possession trait for the single-gene DefensePredictor-discovered
anti-phage locus from DeWeirdt et al.'s machine-learning search. DeWeirdt et
al. mapped the working identifier `D668` to DS-43, marked the cloned
transcriptional unit as defensive, and measured reduced Bas19 and SECphi18
bacteriophage plaquing. The final Science Table S8 maps `D668` to the
replicated DS-43 display name. The pinned DefenseFinder article registry maps
DS-43 to the DefensePredictor preprint, the pinned DefenseFinder HMM inventory
records one DS-43 custom profile, `DS-43__DS-43`, and the pinned
DefenseFinder rules table checked in this curation pass has no DS-43 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-43 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1042200` is reserved for this one-row class cohort. The v344 cohort
used `METPO:1042100`, so v345 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-43 TraitMech, METPO, history,
or prior proposal record, no `DS-43__DS-43` profile-key mention, no
`WP_001057122.1` product-accession mention, no `D668` source working
identifier mention, no `ds_43_system` slug, no `traitmech:000468`, and no
`METPO:1042200` proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1042200` | DS-43 system | `METPO:1016300` phage defense system |

DS-43 system captures genome-level possession of the single-gene
DefensePredictor-discovered phage-defense transcriptional unit cataloged as
D668 and represented by one DefenseFinder DS-43 custom HMM-profile row. It
excludes the D668 source working identifier, the individual DS-43 gene or
protein, the DS-43 HMM profile row, cloned-transcriptional-unit plaquing
assays, the absent DS-43 rule-level DefenseFinder model, unresolved DS-43
component activity and phage readouts, and other DefensePredictor-discovered or
phage-defense systems.

`traitmech:000468` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `D668` is kept as a related synonym
because it names the source working identifier, and `DS-43__DS-43` is kept as a
related synonym because it names a DefenseFinder profile key rather than the
genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-43` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000468` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000468` as traceability during the migration.

## Change Log

- v345, 2026-09: lifts `traitmech:000468 DS-43 system` into the
  `METPO:1042200` placeholder block.
