# METPO ROBOT Template Proposal - NixI System (v210, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v209 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for NixI system, the
genome-level possession trait for a PLE-like `nixI` phage-satellite locus.
LeGault et al. characterized NixI as a PLE-encoded nicking endonuclease that
cleaves ICP1 bacteriophage DNA, is sufficient to limit ICP1 replication and
progeny production, and functions in a phage parasite that can be considered a
host defense system. DefenseFinder models NixI with required `NixI__NixI` and
optional `NixI__Stix` profiles.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for NixI |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1028700` is reserved for this one-row class cohort. The v209 cohort used
`METPO:1028600`, so v210 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository, plus the pinned DefenseFinder registries that supplied the
positive NixI article, rule, and HMM rows used for candidate discovery. The
only pre-existing `NixI`, `Stix`, `NixI__NixI`, `NixI__Stix`, and
`10.1101/2021.07.12.452122` hits were those positive DefenseFinder rows; no
exact same-scope TraitMech or METPO record, `nixi_system` slug, `NixI system`
label, `traitmech:000333`, `metpo_traitmech_v210`, `METPO:1028700`, or
`DOI:10.1093/nar/gkac002` was present before this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1028700` | NixI system | `METPO:1016300` phage defense system |

NixI system captures genome-level possession of a NixI-family locus represented
by DefenseFinder's `NixI__NixI` HMM profile and exemplified by LeGault et al.'s
PLE-encoded nicking endonuclease. It excludes individual `nixI` genes; NixI
enzymes; the individual DefenseFinder HMM profiles; source database rows naming
one phage-satellite nuclease; unresolved satellite self-protection or ICP1
nick-site chemistry; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. NixI, the DefenseFinder HMMs,
individual genes or nucleases, ICP1 genome cleavage, and ICP1 replication
inhibition are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  related shifted label, no exact synonyms, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000333` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000333` as traceability during the migration.

## Change Log

- v210, 2026-09: lifts `traitmech:000333 NixI system` into the
  `METPO:1028700` block.
