# METPO ROBOT Template Proposal - Ophion System (v208, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v207 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Ophion system, the
genome-level possession trait for a three-gene Ophion anti-phage locus.
Keesman et al. named Ophion among three phage-defense systems validated from
more than 500 modularity-network candidates, reported that its OpnA-OpnC
components combine Radical SAM, PHP, and PRTase domains, and found
Ophion-mediated blocking of jumbo-phage infection before phage-nucleus
formation. DefenseFinder maps the named Ophion system to the Keesman et al.
modular phage-defense discovery preprint.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Ophion |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1028500` is reserved for this one-row class cohort. The v207 cohort used
`METPO:1028400`, so v208 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository, plus the pinned DefenseFinder registries used for candidate
discovery. No exact same-scope record, `ophion_system` slug, `Ophion system`
label, `traitmech:000331`, `metpo_traitmech_v208`, or `METPO:1028500` was
present before this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1028500` | Ophion system | `METPO:1016300` phage defense system |

Ophion system captures genome-level possession of a three-gene Ophion locus
encoding OpnA, OpnB, and OpnC components that can block jumbo-phage infection
before phage-nucleus formation. It excludes the individual `opnA`, `opnB`, and
`opnC` genes; individual Ophion proteins; the source Pseudomonas gene cluster;
DefenseFinder article-registry rows; DefenseFinder HMM or rule rows;
early-phage transcription-blocking processes; EPI-vesicle to nucleus-stage
arrest itself; Juk co-occurrence; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual Ophion genes and proteins,
the DefenseFinder registry row, the source gene cluster, phage-restriction
processes, nucleotide-modification products, early phage transcripts, and
EPI-to-nucleus arrest events are shifted from this organism-level GENOMICS
possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact Ophion synonym, no related shifted labels, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000331` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000331` as traceability during the migration.

## Change Log

- v208, 2026-09: lifts `traitmech:000331 Ophion system` into the
  `METPO:1028500` block.
