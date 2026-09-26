# METPO ROBOT Template Proposal - Type IIG Restriction-Modification System (v252, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v251 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for type IIG
restriction-modification system, the genome-level possession trait for Type IIG
R-M loci centered on a restriction-methyltransferase-specificity fusion gene.
Shen et al. characterize the BpuSI Type IIG system as an R-M fusion with
companion methyltransferases, Zhu et al. characterize the Tth111II Type IIGS
enzyme, and DefenseFinder models the `RM_Type_IIG` subsystem in its pinned rule
and HMM tables.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for type IIG restriction-modification system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1032900` is reserved for this one-row class cohort. The v251 cohort used
`METPO:1032800`, so v252 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope Type IIG
restriction-modification system record, `type_iig_restriction_modification`
slug, `RM_Type_IIG` source key, BpuSI or Tth111II DOI, `traitmech:000375`,
`metpo_traitmech_v252`, or `METPO:1032900`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1032900` | type IIG restriction-modification system | `METPO:1007694` restriction-modification system |

Type IIG restriction-modification system captures genome-level possession of a
Type IIG R-M locus represented by DefenseFinder as the RM_Type_IIG subsystem. It
excludes individual Type IIG enzymes, individual companion methyltransferases,
the DefenseFinder `RM_Type_IIG__Type_IIG` profile group, the eight custom
RM_Type_IIG HMM profiles, the source key `RM_Type_IIG`, BpuSI or Tth111II
biochemistry outside a complete Type IIG locus, and the broader
restriction-modification parent.

## External Mappings

No exact external mapping is proposed. The GO DNA restriction-modification
process, individual REBASE enzyme pages, individual Type IIG proteins,
DefenseFinder HMM profiles, and source database rows naming one RM_Type_IIG
model are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  no exact synonyms, no exact external xrefs, and two related DefenseFinder
  source-key or profile-group synonyms.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000375` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000375` as traceability during the migration.

## Change Log

- v252, 2026-09: lifts `traitmech:000375 type IIG restriction-modification
  system` into the `METPO:1032900` block.
