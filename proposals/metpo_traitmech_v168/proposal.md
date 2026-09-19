# METPO ROBOT Template Proposal - Prometheus System (v168, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v167 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Prometheus system, the
genome-level possession trait for a Prometheus anti-phage locus. van den Berg et
al. reported a search over bacterial homologs of innate eukaryotic antiviral
defense genes and validated six phage defense systems, and DefenseFinder
catalogs Prometheus with a Prometheus__ProA HMM profile entry.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Prometheus |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1024500` is reserved for this one-row class cohort. The v167 cohort used
`METPO:1024400`, so v168 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v168`, no live record used
`traitmech:000291`, and no prior proposal reserved `METPO:1024500`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1024500` | Prometheus system | `METPO:1016300` phage defense system |

Prometheus system captures genome-level possession of a Prometheus locus
cataloged by DefenseFinder under a Prometheus model namespace with a
Prometheus__ProA HMM profile entry. It excludes the ambiguous bare ProA label,
individual ProA genes; ProA proteins; DefenseFinder HMM profiles; predicted
source-database rows naming one Prometheus locus; unresolved Prometheus trigger
or effector activities; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. The Prometheus__ProA HMM, individual
ProA-labeled genes, their corresponding proteins, and unresolved Prometheus
molecular outputs are shifted from this organism-level GENOMICS possession
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  exact Prometheus synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000291` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000291` as traceability during the migration.

## Change Log

- v168, 2026-09: lifts `traitmech:000291 Prometheus system` into the
  `METPO:1024500` block.
