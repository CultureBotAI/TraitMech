# METPO ROBOT Template Proposal - Panoptes System (v284, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v283 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Panoptes system, the
genome-level possession trait for the `optSE` antiphage locus described by
Sullivan et al. Panoptes couples constitutive OptS cyclic-dinucleotide synthesis
to OptE repression; phage Acb2-like proteins that sequester the OptS-derived
signal release OptE-mediated inner-membrane disruption and restrict phage
replication.

The pinned DefenseFinder article registry maps `Panoptes` to Sullivan et al.,
but the same pinned commit has no `Panoptes` rows in `DefenseFinder_rules.tsv`
or `Liste_hmm_system.md`, so this proposal treats the registry as
name-to-paper evidence rather than as profile support.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Panoptes system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1036100` is reserved for this one-row class cohort. The v283 cohort
used `METPO:1036000`, so v284 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope Panoptes system record, `optSE`
or `OptSE` synonym, `panoptes_system` slug, `10.1038/s41586-025-09557-z`,
`traitmech:000407`, `metpo_traitmech_v284`, or `METPO:1036100`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1036100` | Panoptes system | `METPO:1016300` phage defense system |

Panoptes system captures genome-level possession of a two-gene `optSE`
phage-defense locus that uses constitutive cyclic-dinucleotide production as a
decoy guard signal for Acb2-like anti-defense activity. It excludes individual
`optS`/OptS and `optE`/OptE genes or proteins, the `VnOptSE` or `KpOptSE`
experimental constructs, cyclic-dinucleotide synthesis as a standalone process,
Acb2 anti-defense activation, phage cyclic-nucleotide sequestration, OptE
inner-membrane disruption, broad immune-evasion detection, and DefenseFinder
article-registry rows without a model profile.

## External Mappings

No exact external mapping is proposed. Individual genes, protein effectors,
heterologous plasmid constructs, cyclic nucleotide products, phage
counter-defense proteins, and source database rows naming the literature key
are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  Panoptes antiphage system exact synonym and related `optSE`/`OptSE` labels.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000407` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000407` as traceability during the migration.

## Change Log

- v284, 2026-09: lifts `traitmech:000407 Panoptes system` into the
  `METPO:1036100` block.
