# METPO ROBOT Template Proposal - Brig1 System (v184, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v183 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Brig1 system, the
genome-level possession trait for a DNA-glycosylase phage-defense system.
Hallinan et al. functionally isolated `brig1` from a soil environmental-DNA
library, showed that Brig1 can excise alpha-glucosyl-hydroxymethylcytosine
nucleobases from T4 phage DNA, generate abasic sites, and inhibit T4 DNA
replication, and reported that Brig1 homologues provide immunity against
T-even phages across distinct bacterial clades. DefenseFinder catalogs Brig1
with `Brig1__Brig1` and `Brig1__ADP_ribosyl` HMM profiles.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Brig1 |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1026100` is reserved for this one-row class cohort. The v183 cohort used
`METPO:1026000`, so v184 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository,
excluding only `.git` and `.venv`. No prior proposal reserved
`metpo_traitmech_v184`, no live record used `traitmech:000307`, and no prior
proposal reserved `METPO:1026100`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1026100` | Brig1 system | `METPO:1016300` phage defense system |

Brig1 system captures genome-level possession of a `brig1`-family locus whose
encoded DNA glycosylase can target T4-like phage DNA and whose model namespace
is represented by the DefenseFinder `Brig1__Brig1` and `Brig1__ADP_ribosyl`
HMM profiles. It excludes the individual `brig1` gene; Brig1 proteins;
DNA-glycosylase activity outside a complete Brig1 antiphage locus;
alpha-glucosyl-hydroxymethylcytosine as a phage DNA modification; individual
T4 or T-even phage host-range outcomes; source database rows naming one Brig1
profile hit; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Brig1, Brig1-family proteins,
DefenseFinder HMMs, alpha-glucosyl-hydroxymethylcytosine base excision, abasic
site generation, and phage DNA replication inhibition are shifted from this
organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  related Brig1 labels and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000307` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000307` as traceability during the migration.

## Change Log

- v184, 2026-09: lifts `traitmech:000307 Brig1 system` into the
  `METPO:1026100` block.
