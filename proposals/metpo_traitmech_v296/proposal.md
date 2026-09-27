# METPO ROBOT Template Proposal - Prokaryotic Argonaute Defense System (v296, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v295 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for prokaryotic Argonaute
defense system, the genome-level possession trait for pAgo-centered mobile
genetic element defense loci. Makarova et al. proposed prokaryotic Argonaute
homologs as defense components against mobile genetic elements; later SPARTA
and DdmDE work supports experimentally characterized pAgo-centered defense
systems; and the pinned DefenseFinder registries model a `pAgo` namespace with
long pAgo, SPARTA, and optional APAZ-associated profile groups.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for prokaryotic Argonaute defense system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1037300` is reserved for this one-row class cohort. The v295 cohort used
`METPO:1037200`, so v296 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found only narrower SPARTA and DdmDE records and proposals
mentioning prokaryotic Argonautes, and found no exact same-scope prokaryotic
Argonaute defense record, exact pAgo-system proposal, `pago_system` slug,
`traitmech:000419`, `metpo_traitmech_v296`, or `METPO:1037300` /
`METPO:10373xx` proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1037300` | prokaryotic Argonaute defense system | `METPO:1000188` quality |

Prokaryotic Argonaute defense system captures genome-level possession of a
pAgo-centered defense locus that can act against plasmids, bacteriophages, or
other mobile genetic elements. It excludes individual pAgo genes or proteins,
guide RNAs, APAZ accessory proteins, SPARTA or DdmDE-specific complexes,
DefenseFinder HMM profiles, source database rows naming the pAgo model
namespace, long-pAgo subtypes without curated complete-locus boundaries, and
other plasmid-defense or phage-defense systems.

`traitmech:000419` is a direct local child of upstream `METPO:1000188` quality.
In the same TraitMech branch, it becomes the closest local parent of
`traitmech:000240` SPARTA system and `traitmech:000275` DdmDE system.

## External Mappings

No exact external mapping is proposed. `pAgo` is kept as a related synonym
because it is the DefenseFinder system key but can also denote an individual
prokaryotic Argonaute gene or protein.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  related `pAgo` source key.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000419` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000419` as traceability during the migration.

## Change Log

- v296, 2026-09: lifts `traitmech:000419 prokaryotic Argonaute defense
  system` into the `METPO:1037300` block.
