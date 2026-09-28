# METPO ROBOT Template Proposal - DS-20 System (v322, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-20 system, the
genome-level possession trait for DefensePredictor-discovered system 20.
DeWeirdt et al. mapped working identifier PDX1 to DS-20 and measured reduced
Bas3 bacteriophage plaquing in a heterologous plasmid-expression assay. The
final Science Table S6/S7/S8 files record the PDX1 locus, one plaquing readout,
the replicated DS-20 display name, and a PDDEXK HHpred-domain row. The pinned
DefenseFinder article registry maps DS-20 to the DefensePredictor preprint, the
pinned DefenseFinder HMM inventory records one DS-20 custom profile,
`DS-20__DS-20`, and the pinned DefenseFinder rules table checked in this
curation pass has no DS-20 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-20 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1039900` is reserved for this one-row class cohort. The v321 cohort used
`METPO:1039800`, so v322 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-20 TraitMech, METPO, history,
or prior proposal record, no `DS-20__DS-20` profile-key mention, no `PDX1`
working-identifier mention, no `WP_032291790.1` product-accession mention, no
`NZ_QOYR01000022.1` contig mention, no `ds_20_system` slug, no
`traitmech:000445`, no `metpo_traitmech_v322`, and no `METPO:1039900` proposal
block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1039900` | DS-20 system | `METPO:1016300` phage defense system |

DS-20 system captures genome-level possession of the single-gene
DefensePredictor-discovered system 20 locus cataloged as working identifier
PDX1 and represented by the DefenseFinder DS-20 custom HMM-profile row. It
excludes the PDX1 source working identifier, the individual DS-20 gene and
protein, individual DefenseFinder HMM profile rows, cloned-transcriptional-unit
plaquing assays, the PDDEXK HHpred-domain annotation, the absent DS-20
rule-level DefenseFinder model, unresolved component activity, unresolved phage
breadth, and other DefensePredictor-discovered or phage-defense systems.

`traitmech:000445` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `PDX1` is kept as a related synonym
because it names the source working identifier, and `DS-20__DS-20` is kept as a
related synonym because it names a DefenseFinder profile key rather than the
genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-20` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000445` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000445` as traceability during the migration.

## Change Log

- v322, 2026-09: lifts `traitmech:000445 DS-20 system` into the
  `METPO:1039900` placeholder block.
