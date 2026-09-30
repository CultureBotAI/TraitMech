# METPO ROBOT Template Proposal - Type II Restriction-Modification System (v370, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for type II
restriction-modification system, the genome-level possession trait for Type II
R-M loci coupling Type II restriction endonuclease activity with cognate
methyltransferase self-protection. Kirillov et al. describe Type II R-M
systems as coupled REase/MTase systems, Pingoud et al. review Type II
restriction endonucleases and REBASE's role as the source for restriction
endonucleases and companion proteins, and Zhu et al. place the already
curated Type IIG branch in the Type II restriction-enzyme classification. The
pinned DefenseFinder registry maps the conventional `RM_Type_II` subsystem to
the 2023 REBASE update, requires both Type_II_MTases and Type_II_REases groups
in its rule row, and carries custom HMM rows for both groups.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for type II restriction-modification system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1044700` is reserved for this one-row class cohort. The v369 cohort used
`METPO:1044600`, so v370 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope Type II
restriction-modification system record, `type_ii_restriction_modification`
slug, `RM_Type_II` source key, `traitmech:000493`,
`metpo_traitmech_v370`, or `METPO:1044700`. The only pre-curation
RM_Type_II mention was an Ambrosia-system evidence note that explicitly
excluded Ambrosia from a conventional type II restriction-modification system.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1044700` | type II restriction-modification system | `METPO:1007694` restriction-modification system |

Type II restriction-modification system captures genome-level possession of a
Type II R-M locus. It excludes individual Type II restriction endonucleases,
individual cognate methyltransferases, individual Type IIG fusion enzymes, the
DefenseFinder `RM_Type_II__Type_II_MTases` and
`RM_Type_II__Type_II_REases` profile groups, individual custom RM_Type_II HMM
profiles, the source key `RM_Type_II`, conventional Type II loci outside a
complete R-M locus, specialized Type IIG subtype loci, and the broader
restriction-modification parent.

`traitmech:000493` is a direct local child of `traitmech:000095`
restriction-modification system and the new local parent of the existing
`traitmech:000375` type IIG restriction-modification system.

## External Mappings

No exact external mapping is proposed. The GO DNA restriction-modification
process, individual REBASE enzyme pages, individual Type II restriction
endonucleases, individual Type II methyltransferases, DefenseFinder HMM
profile groups, and source database rows naming the conventional RM_Type_II
model are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  no exact synonyms and three related DefenseFinder source-key or
  profile-group synonyms.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000493` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000493` as traceability during the migration.

## Change Log

- v370, 2026-09: lifts `traitmech:000493 type II
  restriction-modification system` into the `METPO:1044700` placeholder
  block.
