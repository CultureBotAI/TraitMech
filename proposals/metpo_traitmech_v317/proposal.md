# METPO ROBOT Template Proposal - DS-17 System (v317, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-17 system, the
genome-level possession trait for DefensePredictor-discovered system 17.
DeWeirdt et al. mapped working identifier NUCS to DS-17 and measured reduced
T4 bacteriophage plaquing in a heterologous plasmid-expression assay. The final
Science Table S6/S7/S8 files record the NUCS locus, one plaquing readout, the
replicated DS-17 display name, and a PDDEXK HHpred-domain row. The pinned
DefenseFinder article registry maps DS-17 to the DefensePredictor preprint, the
pinned DefenseFinder HMM inventory records one DS-17 custom profile,
`DS-17__DS-17`, and the pinned DefenseFinder rules table checked in this
curation pass has no DS-17 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-17 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1039400` is reserved for this one-row class cohort. The v316 cohort used
`METPO:1039300`, so v317 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-17 TraitMech, METPO, history,
or prior proposal record, no `DS-17__DS-17` profile-key mention, no `NUCS`
working-identifier mention, no `WP_001240354.1` product-accession mention, no
`ds_17_system` slug, no `traitmech:000440`, no `metpo_traitmech_v317`, and no
`METPO:1039400` proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1039400` | DS-17 system | `METPO:1016300` phage defense system |

DS-17 system captures genome-level possession of the single-gene
DefensePredictor-discovered system 17 locus cataloged as working identifier
NUCS and represented by the DefenseFinder DS-17 custom HMM-profile row. It
excludes the NUCS source working identifier, the individual DS-17 gene and
protein, individual DefenseFinder HMM profile rows,
cloned-transcriptional-unit plaquing assays, the PDDEXK HHpred-domain
annotation, the absent DS-17 rule-level DefenseFinder model, unresolved
component activity, unresolved phage readouts, and other
DefensePredictor-discovered or phage-defense systems.

`traitmech:000440` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `NUCS` is kept as a related synonym
because it names the source working identifier, and `DS-17__DS-17` is kept as a
related synonym because it names a DefenseFinder profile key rather than the
genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-17` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000440` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000440` as traceability during the migration.

## Change Log

- v317, 2026-09: lifts `traitmech:000440 DS-17 system` into the
  `METPO:1039400` placeholder block.
