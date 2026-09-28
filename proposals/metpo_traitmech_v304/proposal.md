# METPO ROBOT Template Proposal - DS-4 System (v304, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v303 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-4 system, the
genome-level possession trait for DefensePredictor-discovered system 4.
DeWeirdt et al. mapped the working identifier NTTI to display name DS-4 and
experimentally validated the cloned transcriptional unit in E. coli MG1655
plaquing assays. The pinned DefenseFinder HMM inventory records five custom
DS-4 rows, while the pinned DefenseFinder rules table has no DS-4 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-4 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1038100` is reserved for this one-row class cohort. The v303 cohort used
`METPO:1038000`, so v304 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-4 TraitMech, METPO, history,
or prior proposal record, no exact `NTTI` working-identifier record, no
`WP_087900468.1`, `WP_087900469.1`, `WP_087900470.1`, `WP_072044445.1`, or
`WP_047174762.1` product-accession mention, no `NZ_QOYB01000018.1` contig
mention, no `ds_4_system` slug, no `traitmech:000427`, no
`metpo_traitmech_v304`, and no `METPO:1038100` / `METPO:10381xx` proposal
block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1038100` | DS-4 system | `METPO:1016300` phage defense system |

DS-4 system captures genome-level possession of the five-gene
DefensePredictor-discovered system represented by the validated NTTI
transcriptional unit and by DefenseFinder DS-4 HMM-profile rows. It excludes
the individual DS-4 genes and proteins, the NTTI working identifier,
individual DefenseFinder HMM profile rows, Table S8 HHPred domain-annotation
rows, cloned-transcriptional-unit plaquing assays, the absent DS-4 rule-level
DefenseFinder model, unresolved DS-4 effector chemistry, and other
DefensePredictor-discovered or phage-defense systems.

`traitmech:000427` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `NTTI` is retained only as a related
source working identifier, and the `DS-4__DS-4*` labels are kept as related
synonyms because they name DefenseFinder profile keys rather than the
genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-4` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000427` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000427` as traceability during the migration.

## Change Log

- v304, 2026-09: lifts `traitmech:000427 DS-4 system` into the
  `METPO:1038100` block.
