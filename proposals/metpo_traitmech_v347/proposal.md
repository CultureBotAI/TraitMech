# METPO ROBOT Template Proposal - DS-30 System (v347, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-30 system, the
genome-level possession trait for a four-gene DefensePredictor-discovered
anti-phage locus from DeWeirdt et al.'s machine-learning search. DeWeirdt et
al. mapped the working identifier `ABC3` to DS-30, marked the cloned
transcriptional unit as defensive, and measured smaller SECphi27 bacteriophage
plaques plus reduced efficiency of plating. The final Science Table S8 maps
`ABC3` to the replicated DS-30 display name and records ABC-3C C-terminal,
ABC-3C middle, ABC ATPase, and FtsL HHpred-domain rows for its four Table S6
product accessions. The pinned DefenseFinder HMM inventory records four
DS-30-specific custom profiles under `Lamassu-Fam`, while the pinned
DefenseFinder rules table checked in this curation pass records only generic
Lamassu-Fam effector subtypes and no DS-30-specific rule row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-30 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1042400` is reserved for this one-row class cohort. The v346 cohort
used `METPO:1042300`, so v347 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-30 TraitMech, METPO, history,
or prior proposal record, no ABC3 record, no Lamassu-Fam DS-30 component
profile-key mention outside the pinned source rows, no `ds_30_system` slug, no
`traitmech:000470`, and no `METPO:1042400` proposal block. It found only the
existing broader `Lamassu system`, generic proposal references to Lamassu as
another antiphage family, and the pinned sources.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1042400` | DS-30 system | `METPO:1018600` Lamassu system |

DS-30 system captures genome-level possession of the four-gene
DefensePredictor-discovered phage-defense transcriptional unit cataloged as
ABC3 and represented by four DefenseFinder DS-30 custom HMM-profile rows under
Lamassu-Fam. It excludes the broader Lamassu system, individual ABC3 genes or
proteins, individual Lamassu-Fam DS-30 HMM profile rows, generic Lamassu-Fam
rule rows and effector subtypes, cloned-transcriptional-unit plaquing assays,
ABC-3C/SMC/FtsL HHpred annotations, unresolved DS-30 component activities and
LmuC requirement, and other Lamassu or DefensePredictor-discovered systems.

`traitmech:000470` is a direct local child of `traitmech:000232` Lamassu
system.

## External Mappings

No exact external mapping is proposed. `ABC3` is kept as a related synonym
because it names the source working identifier, and the four
`Lamassu-Fam__Lmu*_DS-30*` labels are kept as related synonyms because they
name DefenseFinder profile keys rather than the genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-30` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000470` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000470` as traceability during the migration.

## Change Log

- v347, 2026-09: lifts `traitmech:000470 DS-30 system` into the
  `METPO:1042400` placeholder block.
