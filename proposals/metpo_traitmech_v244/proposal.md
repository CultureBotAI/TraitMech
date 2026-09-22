# METPO ROBOT Template Proposal - RnlAB System (v244, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v243 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for RnlAB system, the
genome-level possession trait for a genome-encoded `rnlA-rnlB`
toxin-antitoxin locus modeled by DefenseFinder as a two-profile system
requiring `RnlAB__RnlA` and `RnlAB__RnlB`. Koga et al. identify `rnlA` as the
structural gene for the RNase LS toxin and `rnlB` as its neighboring cognate
antitoxin gene. Otsuka and Yonesaki show that bacteriophage T4 protein Dmd
suppresses RnlA toxicity by direct interaction, marking wild-type T4 evasion as
a scope boundary around the RnlAB phage-defense mechanism. DefenseFinder maps
the `RnlAB` key to the Koga et al. paper while pinning custom `RnlAB__RnlA`
and `RnlAB__RnlB` profiles for this system.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for RnlAB |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1032100` is reserved for this one-row class cohort. The v243 cohort used
`METPO:1032000`, so v244 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository, excluding only `.git`. It found no exact same-scope RnlAB
system record, `rnlab_system` slug, `RnlAB__RnlA` or `RnlAB__RnlB` profile row,
RnlAB DOI or PMID, `traitmech:000367`, `metpo_traitmech_v244`, or
`METPO:1032100`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1032100` | RnlAB system | `METPO:1016300` phage defense system |

RnlAB system captures genome-level possession of a genome-encoded `rnlA-rnlB`
toxin-antitoxin locus represented by DefenseFinder as a two-profile model
requiring `RnlAB__RnlA` and `RnlAB__RnlB`. It excludes the individual RnlA
RNase LS toxin, the RnlB antitoxin, RNase LS activity, wild-type T4 evasion
through Dmd, the `RnlAB__RnlA` and `RnlAB__RnlB` HMM profiles, source database
rows naming one RnlAB model, and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual RnlA/RnlB proteins, RNase LS
activity, Dmd-mediated phage evasion, and DefenseFinder profile rows are
shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact synonyms, three related shifted labels, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000367` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000367` as traceability during the migration.

## Change Log

- v244, 2026-09: lifts `traitmech:000367 RnlAB system` into the
  `METPO:1032100` block.
