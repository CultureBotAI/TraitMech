# METPO ROBOT Template Proposal - DS-16 System (v316, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-16 system, the
genome-level possession trait for DefensePredictor-discovered system 16.
DeWeirdt et al. mapped working identifier PLIK to DS-16 and measured reduced
Bas26 and T4 bacteriophage plaquing in heterologous plasmid-expression assays.
The final Science Table S6/S7/S8 files record the PLIK locus, two plaquing
readouts, the replicated DS-16 display name, and RelE and ABC ATPase HHpred
domain rows. The pinned DefenseFinder article registry maps DS-16 to the
DefensePredictor preprint, the pinned DefenseFinder HMM inventory records two
DS-16 custom profiles, `DS-16__DS-16A` and `DS-16__DS-16B`, and the pinned
DefenseFinder rules table checked in this curation pass has no DS-16 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-16 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1039300` is reserved for this one-row class cohort. The v315 cohort used
`METPO:1039200`, so v316 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-16 TraitMech, METPO, history,
or prior proposal record, no `DS-16__DS-16A` or `DS-16__DS-16B` profile-key
mention, no `PLIK` working-identifier mention, no `WP_001676492.1` or
`WP_001676491.1` product-accession mention, no `ds_16_system` slug, no
`traitmech:000439`, no `metpo_traitmech_v316`, and no `METPO:1039300` proposal
block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1039300` | DS-16 system | `METPO:1016300` phage defense system |

DS-16 system captures genome-level possession of the two-gene
DefensePredictor-discovered system 16 locus cataloged as working identifier
PLIK and represented by the DefenseFinder DS-16A and DS-16B custom HMM-profile
rows. It excludes the PLIK source working identifier, the individual DS-16 genes
and proteins, individual DefenseFinder HMM profile rows,
cloned-transcriptional-unit plaquing assays, RelE and ABC ATPase
HHpred-domain annotations, the absent DS-16 rule-level DefenseFinder model,
unresolved component activity, unresolved phage readouts, and other
DefensePredictor-discovered or phage-defense systems.

`traitmech:000439` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `PLIK` is kept as a related synonym
because it names the source working identifier, and `DS-16__DS-16A` and
`DS-16__DS-16B` are kept as related synonyms because they name DefenseFinder
profile keys rather than the genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-16` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000439` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000439` as traceability during the migration.

## Change Log

- v316, 2026-09: lifts `traitmech:000439 DS-16 system` into the
  `METPO:1039300` placeholder block.
