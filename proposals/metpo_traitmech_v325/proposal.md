# METPO ROBOT Template Proposal - DS-23 System (v325, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-23 system, the
genome-level possession trait for DefensePredictor-discovered system 23.
DeWeirdt et al. mapped working identifier E2DP to DS-23 and measured reduced
Bas19 bacteriophage plaquing in a heterologous plasmid-expression assay. The
final Science Table S6/S7/S8 files record the E2DP locus, one high-confidence
plaquing readout, and the replicated DS-23 display name. The pinned
DefenseFinder article registry maps DS-23 to the DefensePredictor preprint, the
pinned DefenseFinder HMM inventory records one DS-23 custom profile,
`DS-23__DS-23`, and the pinned DefenseFinder rules table checked in this
curation pass has no DS-23 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-23 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1040200` is reserved for this one-row class cohort. The v324 cohort used
`METPO:1040100`, so v325 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-23 TraitMech, METPO, history,
or prior proposal record, no `DS-23__DS-23` profile-key mention, no
`WP_020231147.1` product-accession mention, no `NZ_RRVV01000032.1` contig
mention, no `ds_23_system` slug, no `traitmech:000448`, no
`metpo_traitmech_v325`, and no `METPO:1040200` proposal block. The E2DP working
identifier appeared only in other DS records' Table S7 reference-image filenames
before this branch, not as a same-scope source working identifier.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1040200` | DS-23 system | `METPO:1016300` phage defense system |

DS-23 system captures genome-level possession of the single-gene
DefensePredictor-discovered system 23 locus cataloged as working identifier
E2DP and represented by the DefenseFinder DS-23 custom HMM-profile row. It
excludes the E2DP source working identifier, the DS-23 protein, the individual
DefenseFinder HMM profile row, cloned-transcriptional-unit plaquing assays,
the ZF and PDDEXK HHpred-domain annotations, the absent DS-23 rule-level
DefenseFinder model, unresolved component activity, unresolved phage breadth,
and other DefensePredictor-discovered or phage-defense systems.

`traitmech:000448` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `E2DP` is kept as a related synonym
because it names the source working identifier, and `DS-23__DS-23` is kept as a
related synonym because it names a DefenseFinder profile key rather than the
genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-23` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000448` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000448` as traceability during the migration.

## Change Log

- v325, 2026-09: lifts `traitmech:000448 DS-23 system` into the
  `METPO:1040200` placeholder block.
