# METPO ROBOT Template Proposal - Tha System (v374, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Tha system, the
genome-level possession trait for tail-activated HEPN anti-phage loci encoded by
Staphylococcus aureus prophages. Rostol et al. describe Tha as a phage-encoded
anti-phage system that is activated by conserved incoming-phage minor tail
proteins and validate Tha-1 and Tha-2 as experimentally distinct Tha systems.
The pinned DefenseFinder registries map the `Tha` source key to the same primary
paper and list one custom `Tha__Tha` HMM row under the Tha namespace.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Tha system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1045100` is reserved for this one-row class cohort. The v373 cohort used
`METPO:1045000`, so v374 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope Tha system record, `tha_system`
slug, `Tha__Tha` source HMM key, `traitmech:000497`, `metpo_traitmech_v374`,
`METPO:1045100`, DOI `10.1038/s41564-024-01661-6`, PMID `38565896`, or PMCID
`PMC11087260`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1045100` | Tha system | `METPO:1016300` phage defense system |

Tha system captures genome-level possession of a tail-activated HEPN anti-phage
locus. It excludes incoming-phage minor tail proteins, individual Tha effector
proteins, Ith inhibitors, exact Tha-1 and Tha-2 variant mechanisms, the
DefenseFinder `Tha__Tha` HMM row itself, and broader prophage autoimmunity
regulation.

`traitmech:000497` is a direct local child of `traitmech:000209` phage defense
system. This proposal uses `METPO:1016300`, the v86 placeholder for
`traitmech:000209`.

## External Mappings

No exact external mapping is proposed. Individual Tha effector proteins,
incoming-phage minor tail proteins, phage Ith inhibitors, and DefenseFinder HMM
profile rows are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with two
  exact synonyms and one related DefenseFinder HMM synonym.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000497` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000497` as traceability during the migration.

## Change Log

- v374, 2026-09: lifts `traitmech:000497 Tha system` into the `METPO:1045100`
  placeholder block.
