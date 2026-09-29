# METPO ROBOT Template Proposal - DS-46 System (v348, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-46 system, the
genome-level possession trait for a two-gene anti-phage locus from DeWeirdt et
al.'s final validation set. DeWeirdt et al. mapped the working identifier `RMRT`
to DS-46 in final Science supplementary Table S6, marked the cloned
transcriptional unit as defensive, recorded an HHblits-hit source screen, and
recorded the two product accessions on contig `NZ_RRVG01000021.1`. The
first-pass review found no final Science Table S7 phage-specific readout row,
no final Science Table S8 display-name or HHpred-domain row, and no DS-46 or
RMRT row in the pinned DefenseFinder article, HMM, or rules registries.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-46 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1042500` is reserved for this one-row class cohort. The v347 cohort
used `METPO:1042400`, so v348 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-46 TraitMech, METPO, history,
or prior proposal record, no RMRT record, no `ds_46_system` slug, no
`traitmech:000471`, and no `METPO:1042500` proposal block. It found only the
`GCF_003886135.1` assembly accession in DS-2 source evidence and an unrelated
`.venv` package hash false positive for the string `RMRT`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1042500` | DS-46 system | `METPO:1016300` phage defense system |

DS-46 system captures genome-level possession of the two-gene DS-46
phage-defense transcriptional unit cataloged as RMRT in final Science Table S6.
It excludes individual RMRT genes or proteins, the HHblits-hit screen evidence
that nominated the transcriptional unit, cloned-transcriptional-unit plaquing
assays, unresolved phage-specific Table S7 readouts, unresolved Table S8
display-name and HHpred-domain annotations, unresolved DefenseFinder model
coverage, and other DS systems.

`traitmech:000471` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `RMRT` is kept as a related synonym
because it names the source working transcriptional-unit identifier rather than
the genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-46` synonym and the related source key.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000471` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000471` as traceability during the migration.

## Change Log

- v348, 2026-09: lifts `traitmech:000471 DS-46 system` into the
  `METPO:1042500` placeholder block.
