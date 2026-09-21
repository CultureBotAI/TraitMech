# METPO ROBOT Template Proposal - Ambrosia System (v206, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v205 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Ambrosia system, the
genome-level possession trait for a five-gene Ambrosia anti-phage locus.
Keesman et al. named Ambrosia among three phage-defense systems validated from
more than 500 modularity-network candidates, reported that its AbrR-AbrD
components combine RM-like and two-component regulatory-system features, and
found Ambrosia-mediated protection against siphophages and myophages.
DefenseFinder maps the named Ambrosia system to the Keesman et al. modular
phage-defense discovery preprint.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Ambrosia |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1028300` is reserved for this one-row class cohort. The v205 cohort used
`METPO:1028200`, so v206 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository, plus the pinned DefenseFinder registries used for candidate
discovery. No exact same-scope record, `ambrosia_system` slug, `Ambrosia
system` label, `traitmech:000329`, `metpo_traitmech_v206`, or `METPO:1028300`
was present before this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1028300` | Ambrosia system | `METPO:1016300` phage defense system |

Ambrosia system captures genome-level possession of a five-gene Ambrosia locus
encoding AbrR, AbrA, AbrB, AbrC, and AbrD components that can limit
siphophage and myophage propagation. It excludes the individual `abrR`, `abrA`,
`abrB`, `abrC`, and `abrD` genes; individual Ambrosia proteins; the source
Pseudomonas gene cluster; DefenseFinder article-registry rows; DefenseFinder
HMM or rule rows; the regulated RM-like response itself; conventional
restriction-modification systems; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual Ambrosia genes and proteins,
the DefenseFinder registry row, the source gene cluster, the phage-restriction
process, and RM-like regulatory events are shifted from this organism-level
GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact Ambrosia synonym, no related shifted labels, and no exact external
  xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000329` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000329` as traceability during the migration.

## Change Log

- v206, 2026-09: lifts `traitmech:000329 Ambrosia system` into the
  `METPO:1028300` block.
