# METPO ROBOT Template Proposal - MazEF System (v222, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v221 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for MazEF system, the
genome-level possession trait for a two-component `mazEF` toxin-antitoxin
locus whose MazE antitoxin and MazF endoribonuclease can protect Escherichia
coli against RNA phages. Nikolic et al. showed that native `mazEF` moderately
reduces E. coli population susceptibility to MS2 and Qbeta RNA phages, increases
the survival of individual cells, and appears to act predominantly through
direct interference rather than abortive infection in that assay context.
DefenseFinder models MazEF as a two-profile system requiring `MazEF__MazE`
and `MazEF__MazF`.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for MazEF |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1029900` is reserved for this one-row class cohort. The v221 cohort used
`METPO:1029800`, so v222 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository outside `.git`, `.venv`, and scratch `reports/robot`, plus the
pinned DefenseFinder registries used for candidate discovery. MazEF occurred
only as a shifted toxin-antitoxin-module example in the existing dormancy
record; no exact same-scope record, `mazef_system` slug, `MazEF system` label,
`traitmech:000345`, `metpo_traitmech_v222`, or `METPO:1029900` was present
before this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1029900` | MazEF system | `METPO:1016300` phage defense system |

MazEF system captures genome-level possession of a two-component MazEF
toxin-antitoxin locus whose MazE antitoxin and MazF endoribonuclease can
protect Escherichia coli against RNA phages and that DefenseFinder represents
with mandatory MazEF__MazE and MazEF__MazF profiles. It excludes individual
`mazE` and `mazF` genes; MazE and MazF proteins; MazF ACA-cleavage sites;
cellular RNA degradation; generic toxin-antitoxin systems; unresolved MazEF
activation routes; RNA phage genomes escaping MazF cleavage; source database
rows naming one MazEF model; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. MazE and MazF proteins, the `mazEF`
operon, MazF endoribonuclease activity, ACA-cleavage sites, RNA phage escape
features, DefenseFinder HMM profiles, and downstream RNA phage replication
interference are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  exact synonym, related shifted labels, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000345` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000345` as traceability during the migration.

## Change Log

- v222, 2026-09: lifts `traitmech:000345 MazEF system` into the
  `METPO:1029900` block.
