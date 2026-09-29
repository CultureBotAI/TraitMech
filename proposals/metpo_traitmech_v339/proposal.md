# METPO ROBOT Template Proposal - DS-40 System (v339, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-40 system, the
genome-level possession trait for the single-gene
DefensePredictor-discovered anti-phage locus from DeWeirdt et al.'s
machine-learning search. DeWeirdt et al. mapped the working identifier `D295`
to DS-40, marked the cloned transcriptional unit as defensive, and measured
reduced Bas26 bacteriophage plaquing. The final Science Table S8 maps `D295`
to the replicated DS-40 display name and reports a moderate-probability DUF6680
HHpred row for the D295 product. The pinned DefenseFinder article registry maps
DS-40 to the DefensePredictor preprint, the pinned DefenseFinder HMM inventory
records one DS-40 custom profile, `DS-40__DS-40`, and the pinned DefenseFinder
rules table checked in this curation pass has no DS-40 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-40 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1041600` is reserved for this one-row class cohort. The v338 cohort
used `METPO:1041500`, so v339 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-40 TraitMech, METPO, history,
or prior proposal record, no `DS-40__DS-40` profile-key mention, no
`NZ_QOYF01000088.1` contig mention, no `WP_097419291.1` product-accession
mention, no `ds_40_system` slug, no `traitmech:000462`, no
`metpo_traitmech_v339`, and no `METPO:1041600` proposal block. It found
`GCF_003334585.1` only as the assembly accession for the same-gapped but
different DS-7 locus and found `D295` only as a hexadecimal table key under the
ignored Python environment.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1041600` | DS-40 system | `METPO:1016300` phage defense system |

DS-40 system captures genome-level possession of the single-gene
DefensePredictor-discovered phage-defense transcriptional unit cataloged as
D295 and represented by one DefenseFinder DS-40 custom HMM-profile row. It
excludes the D295 source working identifier, the individual DS-40 gene or
protein, the DS-40 HMM profile row, cloned-transcriptional-unit plaquing
assays, the moderate-probability DUF6680 HHpred-domain annotation, the absent
DS-40 rule-level DefenseFinder model, unresolved DS-40 component activity and
phage readouts, and other DefensePredictor-discovered or phage-defense
systems.

`traitmech:000462` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `D295` is kept as a related synonym
because it names the source working identifier, and `DS-40__DS-40` is kept as a
related synonym because it names a DefenseFinder profile key rather than the
genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-40` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000462` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000462` as traceability during the migration.

## Change Log

- v339, 2026-09: lifts `traitmech:000462 DS-40 system` into the
  `METPO:1041600` placeholder block.
