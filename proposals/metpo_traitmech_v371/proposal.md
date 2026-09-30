# METPO ROBOT Template Proposal - Type I Restriction-Modification System (v371, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for type I
restriction-modification system, the genome-level possession trait for Type I
R-M loci coupling HsdR-like restriction, HsdM-like methylation, and
HsdS-like DNA sequence recognition. Loenen et al. describe Type I
restriction enzymes as pentameric proteins with separate restriction,
methylation, and DNA sequence-recognition subunits. The pinned DefenseFinder
registry maps the `RM_Type_I` subsystem to the 2023 REBASE update, requires
both Type_I_MTases and Type_I_REases groups in its rule row, accepts the
Type_I_S group as an accessory marker, and carries custom HMM rows for all
three groups under the broad `RM` system namespace.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for type I restriction-modification system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1044800` is reserved for this one-row class cohort. The v370 cohort used
`METPO:1044700`, so v371 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope Type I
restriction-modification system record, `type_i_restriction_modification`
slug, `RM_Type_I` source key on an R-M system record, `traitmech:000494`,
`metpo_traitmech_v371`, or `METPO:1044800`. The only pre-curation
`RM__Type_I_REases` or `RM__Type_I_S` hits were a PrrC system rule row where
those Type I R-M components are accessory markers, not an exact Type I
restriction-modification system trait.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1044800` | type I restriction-modification system | `METPO:1007694` restriction-modification system |

Type I restriction-modification system captures genome-level possession of a
Type I R-M locus. It excludes individual Type I HsdR restriction subunits,
HsdM methyltransferases, HsdS specificity subunits, individual custom
DefenseFinder HMM profiles, the source key `RM_Type_I`, the use of Type I
restriction components as accessory markers in PrrC/EcoprrI models, and the
broader restriction-modification parent.

`traitmech:000494` is a direct local child of `traitmech:000095`
restriction-modification system.

## External Mappings

No exact external mapping is proposed. The GO DNA restriction-modification
process, individual REBASE enzyme pages, individual Hsd proteins,
DefenseFinder HMM profile groups, and source database rows naming the
`RM_Type_I` model are shifted from this organism-level GENOMICS possession
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  no exact synonyms and four related DefenseFinder source-key or
  profile-group synonyms.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000494` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000494` as traceability during the migration.

## Change Log

- v371, 2026-09: lifts `traitmech:000494 type I
  restriction-modification system` into the `METPO:1044800` placeholder
  block.
