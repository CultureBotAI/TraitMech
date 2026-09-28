# METPO ROBOT Template Proposal - DS-19 System (v321, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-19 system, the
genome-level possession trait for DefensePredictor-discovered system 19.
DeWeirdt et al. mapped working identifier PDP4 to DS-19 and measured reduced
Bas19 bacteriophage plaquing in a heterologous plasmid-expression assay. The
final Science Table S6/S7/S8 files record the PDP4 locus, one plaquing readout,
the replicated DS-19 display name, and a lower-probability PDDEXK HHpred-domain
row. The pinned DefenseFinder article registry maps DS-19 to the
DefensePredictor preprint, the pinned DefenseFinder HMM inventory records one
DS-19 custom profile, `DS-19__DS-19`, and the pinned DefenseFinder rules table
checked in this curation pass has no DS-19 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-19 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1039800` is reserved for this one-row class cohort. The v320 cohort used
`METPO:1039700`, so v321 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-19 TraitMech, METPO, history,
or prior proposal record, no `DS-19__DS-19` profile-key mention, no `PDP4`
working-identifier mention, no `WP_000020904.1` product-accession mention, no
`NZ_RRVV01000031.1` contig mention, no `ds_19_system` slug, no
`traitmech:000444`, no `metpo_traitmech_v321`, and no `METPO:1039800` proposal
block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1039800` | DS-19 system | `METPO:1016300` phage defense system |

DS-19 system captures genome-level possession of the single-gene
DefensePredictor-discovered system 19 locus cataloged as working identifier
PDP4 and represented by the DefenseFinder DS-19 custom HMM-profile row. It
excludes the PDP4 source working identifier, the individual DS-19 gene and
protein, individual DefenseFinder HMM profile rows, cloned-transcriptional-unit
plaquing assays, the lower-probability PDDEXK HHpred-domain annotation, the
absent DS-19 rule-level DefenseFinder model, unresolved component activity,
unresolved phage breadth, and other DefensePredictor-discovered or phage-defense
systems.

`traitmech:000444` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `PDP4` is kept as a related synonym
because it names the source working identifier, and `DS-19__DS-19` is kept as a
related synonym because it names a DefenseFinder profile key rather than the
genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-19` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000444` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000444` as traceability during the migration.

## Change Log

- v321, 2026-09: lifts `traitmech:000444 DS-19 system` into the
  `METPO:1039800` placeholder block.
