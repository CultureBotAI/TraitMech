# METPO ROBOT Template Proposal - SanaTA System (v250, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v249 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for SanaTA system, the
genome-level possession trait for a two-gene sanaTA toxin-antitoxin locus.
Sberro et al. support sanaTA as an experimentally validated toxin-antitoxin
family that reduces sensitivity to T7 phages lacking gene 4.5 anti-defense
activity. DefenseFinder maps the `SanaTA` key to that paper in its article
registry and models the system in the pinned rule and HMM tables with
`SanaTA__SanaA` and `SanaTA__SanaT` profiles.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for SanaTA |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1032700` is reserved for this one-row class cohort. The v249 cohort used
`METPO:1032600`, so v250 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope SanaTA system record,
`sanata_system` slug, Sberro DOI, Sberro PMID, `traitmech:000373`,
`metpo_traitmech_v250`, or `METPO:1032700`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1032700` | SanaTA system | `METPO:1016300` phage defense system |

SanaTA system captures genome-level possession of a sanaTA toxin-antitoxin
locus represented by DefenseFinder as a SanaA/SanaT two-profile model and
experimentally linked to resistance against T7 phage mutants lacking gene 4.5
anti-defense activity. It excludes individual SanaA or SanaT proteins, the
`SanaTA` source key, the DefenseFinder `SanaTA__SanaA` and `SanaTA__SanaT`
profiles, the extra `SanaTA__SanaT_1` HMM row, T7 Gp4.5, Lon protease,
gene-4.5 anti-defense activity, and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual SanaA and SanaT proteins,
T7 gene 4.5, Lon protease inhibition, DefenseFinder HMM profiles, and source
database rows naming one SanaTA model are shifted from this organism-level
GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  no exact synonyms, no exact external xrefs, and four related source-key or
  HMM-profile synonyms.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000373` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000373` as traceability during the migration.

## Change Log

- v250, 2026-09: lifts `traitmech:000373 SanaTA system` into the
  `METPO:1032700` block.
