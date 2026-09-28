# METPO ROBOT Template Proposal - DS-6 System (v307, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v306 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-6 system, the
genome-level possession trait for DefensePredictor-discovered system 6.
DeWeirdt et al. mapped the working identifier HIPA to display name DS-6 and
to the later publication name HipAD, and experimentally validated the cloned
transcriptional unit in E. coli MG1655 plaquing assays. The pinned
DefenseFinder HMM inventory records two custom DS-6 rows, while the pinned
DefenseFinder rules table has no DS-6 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-6 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1038400` is reserved for this one-row class cohort. The v306 cohort used
`METPO:1038300`, so v307 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus and pinned METPO OWL. It found no exact same-scope DS-6
TraitMech, METPO, history, or prior proposal record, no exact `HIPA`
working-identifier record, no `WP_000210934.1` or `WP_000389051.1`
product-accession mention, no `NZ_QOWQ01000062.1` contig mention, no
`GCF_003334335.1` assembly mention, no `ds_6_system` slug, no
`traitmech:000430`, no `metpo_traitmech_v307`, and no `METPO:1038400` /
`METPO:10384xx` proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1038400` | DS-6 system | `METPO:1016300` phage defense system |

DS-6 system captures genome-level possession of the two-gene
DefensePredictor-discovered system represented by the validated HIPA/HipAD
transcriptional unit and by the DefenseFinder DS-6A and DS-6B HMM-profile
rows. It excludes the individual DS-6 genes and proteins, the HIPA working
identifier, the individual DefenseFinder HMM profile rows,
cloned-transcriptional-unit plaquing assays, the absent DS-6 rule-level
DefenseFinder model, unresolved DS-6 DUF3037, DUF1829, and HipA-like kinase
chemistry, and other DefensePredictor-discovered or phage-defense systems.

`traitmech:000430` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `HipAD` is proposed only as an exact
publication synonym, `HIPA` is retained only as a related source working
identifier, and `DS-6__DS-6A` and `DS-6__DS-6B` are kept as related synonyms
because they name DefenseFinder profile keys rather than the genome-level
possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-6` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000430` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000430` as traceability during the migration.

## Change Log

- v307, 2026-09: lifts `traitmech:000430 DS-6 system` into the
  `METPO:1038400` block.
