# METPO ROBOT Template Proposal - Toga System (v375, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Toga system, the
genome-level possession trait for a single-protein P4-encoded anti-phage locus.
de Sousa et al. describe Toga as one of the novel P4-associated systems that
they experimentally tested for phage protection in Escherichia coli, and the
pinned DefenseFinder article registry maps the `Toga` source key to the same
study's preprint.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Toga system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1045200` is reserved for this one-row class cohort. The v374 cohort used
`METPO:1045100`, so v375 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files outside
`.git` across the curation corpus. It found no exact same-scope Toga system
record, `toga_system` slug, `Toga` label or synonym, `traitmech:000498`,
`metpo_traitmech_v375`, `METPO:1045200`, DOI `10.1093/nar/gkag898`, DOI
`10.64898/2026.02.27.708500`, PMID `42755366`, or PMCID `PMC13586616`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1045200` | Toga system | `METPO:1016300` phage defense system |

Toga system captures genome-level possession of a single-protein P4-associated
anti-phage locus. It excludes individual Toga protein products, P4 helper
satellite biology outside the Toga locus, candidate domain assignments, source
supplement rows naming a tested plasmid, the missing DefenseFinder HMM/rule
model, and other novel P4-encoded anti-phage systems validated in the same
study.

`traitmech:000498` is a direct local child of `traitmech:000209` phage defense
system. This proposal uses `METPO:1016300`, the v86 placeholder for
`traitmech:000209`.

## External Mappings

No exact external mapping is proposed. Individual Toga protein products,
P4/P2 mobile elements, predicted protein domains, the DefenseFinder article
namespace, and assay plasmids are shifted from this organism-level GENOMICS
possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one exact
  synonym.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000498` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000498` as traceability during the migration.

## Change Log

- v375, 2026-09: lifts `traitmech:000498 Toga system` into the `METPO:1045200`
  placeholder block.
