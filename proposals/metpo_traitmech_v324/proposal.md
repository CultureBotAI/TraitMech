# METPO ROBOT Template Proposal - DS-22 System (v324, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-22 system, the
genome-level possession trait for DefensePredictor-discovered system 22.
DeWeirdt et al. mapped working identifier MVB1 to DS-22 and measured reduced
Bas11 bacteriophage plaquing in a heterologous plasmid-expression assay. The
final Science Table S6/S7/S8 files record the MVB1 locus, one high-confidence
plaquing readout, and the replicated DS-22 display name. The pinned
DefenseFinder article registry maps DS-22 to the DefensePredictor preprint, the
pinned DefenseFinder HMM inventory records one DS-22 custom profile,
`DS-22__DS-22`, and the pinned DefenseFinder rules table checked in this
curation pass has no DS-22 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-22 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1040100` is reserved for this one-row class cohort. The v323 cohort used
`METPO:1040000`, so v324 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-22 TraitMech, METPO, history,
or prior proposal record, no `DS-22__DS-22` profile-key mention, no
`WP_000162952.1` product-accession mention, no `NZ_QOWO01000045.1` contig
mention, no `ds_22_system` slug, no `traitmech:000447`, no
`metpo_traitmech_v324`, and no `METPO:1040100` proposal block. The MVB1 working
identifier appeared only in other DS records' Table S7 reference-image
filenames before this branch, not as a same-scope source working identifier.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1040100` | DS-22 system | `METPO:1016300` phage defense system |

DS-22 system captures genome-level possession of the single-gene
DefensePredictor-discovered system 22 locus cataloged as working identifier
MVB1 and represented by the DefenseFinder DS-22 custom HMM-profile row. It
excludes the MVB1 source working identifier, the DS-22 protein, the individual
DefenseFinder HMM profile row, cloned-transcriptional-unit plaquing assays,
the low-confidence HHpred-domain annotations, the absent DS-22 rule-level
DefenseFinder model, unresolved component activity, unresolved phage breadth,
and other DefensePredictor-discovered or phage-defense systems.

`traitmech:000447` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `MVB1` is kept as a related synonym
because it names the source working identifier, and `DS-22__DS-22` is kept as a
related synonym because it names a DefenseFinder profile key rather than the
genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-22` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000447` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000447` as traceability during the migration.

## Change Log

- v324, 2026-09: lifts `traitmech:000447 DS-22 system` into the
  `METPO:1040100` placeholder block.
