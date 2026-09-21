# METPO ROBOT Template Proposal - Dionysus System (v207, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v206 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Dionysus system, the
genome-level possession trait for a three-gene Dionysus anti-phage locus.
Keesman et al. named Dionysus among three phage-defense systems validated from
more than 500 modularity-network candidates, reported that its DinA-DinC
components combine MAEBL, TerB-like, and pore-forming-toxin domains, and found
Dionysus-mediated blocking of jumbo-phage infection. DefenseFinder maps the
named Dionysus system to the Keesman et al. modular phage-defense discovery
preprint.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Dionysus |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1028400` is reserved for this one-row class cohort. The v206 cohort used
`METPO:1028300`, so v207 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository, plus the pinned DefenseFinder registries used for candidate
discovery. No exact same-scope record, `dionysus_system` slug, `Dionysus
system` label, `traitmech:000330`, `metpo_traitmech_v207`, or `METPO:1028400`
was present before this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1028400` | Dionysus system | `METPO:1016300` phage defense system |

Dionysus system captures genome-level possession of a three-gene Dionysus
locus encoding DinA, DinB, and DinC components that can block jumbo-phage
infection. It excludes the individual `dinA`, `dinB`, and `dinC` genes;
individual Dionysus proteins; the source Pseudomonas gene cluster;
DefenseFinder article-registry rows; DefenseFinder HMM or rule rows; the
EPI-vesicle pore-forming process itself; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual Dionysus genes and proteins,
the DefenseFinder registry row, the source gene cluster, phage-restriction
processes, and EPI-vesicle pore-forming events are shifted from this
organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact Dionysus synonym, no related shifted labels, and no exact external
  xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000330` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000330` as traceability during the migration.

## Change Log

- v207, 2026-09: lifts `traitmech:000330 Dionysus system` into the
  `METPO:1028400` block.
