# METPO ROBOT Template Proposal - PD-Lambda-1 System (v281, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v280 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for PD-Lambda-1 system, the
genome-level possession trait for a one-gene phage-defense locus from Vassallo
et al.'s *E. coli* pangenome screen. The pinned DefenseFinder wiki describes
PD-Lambda-1 as a one-protein system that can confer LambdaVir resistance.
DefenseFinder models PD-Lambda-1 with one required HMM profile,
`PD-Lambda-1__PD-Lambda-1`, in the pinned rule and HMM inventories.

The pinned `List_system_article.md` registry does not carry a `PD-Lambda-1`
row, so the TraitMech record deliberately cites the pinned wiki, DOI, rule row,
and HMM row directly instead of using article-registry evidence.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for PD-Lambda-1 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1035800` is reserved for this one-row class cohort. The v280 cohort used
`METPO:1035700`, so v281 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope PD-Lambda-1 system record,
`pd_lambda_1_system` slug, validation or RefSeq source protein accessions,
`traitmech:000404`, `metpo_traitmech_v281`, or `METPO:1035800`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1035800` | PD-Lambda-1 system | `METPO:1016300` phage defense system |

PD-Lambda-1 system captures genome-level possession of a one-protein locus
represented by DefenseFinder as a single-profile `PD-Lambda-1` model requiring
`PD-Lambda-1__PD-Lambda-1` and experimentally linked to LambdaVir protection
when expressed in *Escherichia coli*. It excludes the individual PD-Lambda-1
gene or protein, the DefenseFinder `PD-Lambda-1__PD-Lambda-1` profile, the
source key `PD-Lambda-1`, LambdaVir protection outside a complete PD-Lambda-1
locus, unvalidated RefSeq examples, missing DefenseFinder article-registry
rows, sibling PD-Lambda systems, prophages and mobile genetic elements as
mobile elements, and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual PD-Lambda-1 genes or
proteins, DefenseFinder HMM profiles, source database rows naming one model,
and candidate RefSeq genomic examples are shifted from this organism-level
GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with a
  primary Vassallo et al. citation, no exact synonyms, no exact external xrefs,
  and two related source-key or HMM-profile synonyms.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000404` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000404` as traceability during the migration.

## Change Log

- v281, 2026-09: lifts `traitmech:000404 PD-Lambda-1 system` into the
  `METPO:1035800` block.
