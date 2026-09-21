# METPO ROBOT Template Proposal - ApeA System (v211, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v210 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for ApeA system, the
genome-level possession trait for a single-component ApeA phage-defense locus.
Juozapaitis et al. characterize ApeA DNA-phage defense through a HEPN-domain
antiviral RNase that cleaves host tRNAs within their anticodon loops and
functions as an abortive infection system. Drobysheva et al. characterize a
second non-abortive ApeA output in which ApeA cleaves infecting RNA-phage
genomes. DefenseFinder models the source namespace as `Gao_Ape` with the
single mandatory `Gao_Ape__ApeA` profile.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for ApeA |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1028800` is reserved for this one-row class cohort. The v210 cohort used
`METPO:1028700`, so v211 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository, plus the pinned DefenseFinder registries that supplied the
positive Gao_Ape article, rule, and HMM rows used for candidate discovery. No
exact same-scope TraitMech or METPO record, `gao_ape_system` slug, `ApeA
system` label, `traitmech:000334`, `metpo_traitmech_v211`, `METPO:1028800`,
`Gao_Ape`, `ApeA`, or `DOI:10.64898/2026.01.26.701840` was present before
this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1028800` | ApeA system | `METPO:1016300` phage defense system |

ApeA system captures genome-level possession of a single-component ApeA locus
represented by DefenseFinder's `Gao_Ape__ApeA` HMM profile. It excludes
individual `apeA` genes; individual ApeA HEPN RNase proteins; the
DefenseFinder HMM profile; source database rows naming the Gao_Ape model; the
Ec2ApeA deoxydinucleotide activation mechanism; RNA-phage genomic-RNA
cleavage; host-tRNA anticodon-loop cleavage; unresolved Ec1ApeA activators;
and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. ApeA, the Gao_Ape DefenseFinder HMM
profile, individual genes or RNases, tRNA anticodon-loop cleavage,
phage-genomic-RNA cleavage, abortive phage restriction, and non-abortive
RNA-phage restriction are shifted from this organism-level GENOMICS possession
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with two
  related shifted labels, no exact synonyms, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000334` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000334` as traceability during the migration.

## Change Log

- v211, 2026-09: lifts `traitmech:000334 ApeA system` into the
  `METPO:1028800` block.
