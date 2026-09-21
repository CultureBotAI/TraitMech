# METPO ROBOT Template Proposal - GasderMIN System (v213, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v212 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for GasderMIN system, the
genome-level possession trait for a bacterial gasdermin antiphage locus. Johnson
et al. characterize bacterial gasdermin homologs that can defend against
phages, undergo caspase-like protease cleavage, assemble pores, disrupt
membranes, and execute cell death. The pinned DefenseFinder snapshot contains
GasderMIN in its article registry, records `GasderMIN__bGSDM` in its HMM
inventory, and models `GasderMIN` as a one-profile system in its rules table.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for GasderMIN |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1029000` is reserved for this one-row class cohort. The v212 cohort used
`METPO:1028900`, so v213 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository for exact TraitMech/METPO records and prior proposal/history
mentions. Separately, the pinned DefenseFinder article registry, HMM inventory,
and rules table supplied the positive GasderMIN candidate rows used for
candidate discovery. No exact same-scope TraitMech or METPO record,
`gasdermin_system` slug, `GasderMIN system` label, `traitmech:000336`,
`metpo_traitmech_v213`, `METPO:1029000`, `GasderMIN`,
`GasderMIN__bGSDM`, `bGSDM`, `DOI:10.1126/science.abj8432`,
`PMID:35025633`, or `https://pmc.ncbi.nlm.nih.gov/articles/PMC9134750/` was
present in the repository before this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1029000` | GasderMIN system | `METPO:1016300` phage defense system |

GasderMIN system captures genome-level possession of a bacterial gasdermin
phage-defense locus represented by the standalone DefenseFinder
`GasderMIN__bGSDM` model profile. It excludes individual `bGSDM` genes or
proteins; individual caspase-like proteases; bacterial-gasdermin cleavage,
pore assembly, membrane-integrity disruption, or cell death without the
phage-defense-system context; CARD-NLR gasdermin detector contexts; source
database rows naming one GasderMIN model profile; and other bacterial
phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual bacterial gasdermins,
caspase-like proteases, bGSDM cleavage reactions, pore assembly, membrane
disruption, and gasdermin-triggered cell death are shifted from this
organism-level GENOMICS possession trait. `GasderMIN` and
`GasderMIN__bGSDM` are kept as related synonyms because they denote
DefenseFinder model and profile keys rather than true labels for the
organism-level trait itself.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with two
  related model/profile synonyms and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000336` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000336` as traceability during the migration.

## Change Log

- v213, 2026-09: lifts `traitmech:000336 GasderMIN system` into the
  `METPO:1029000` block.
