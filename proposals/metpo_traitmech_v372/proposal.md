# METPO ROBOT Template Proposal - Type III Restriction-Modification System (v372, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for type III
restriction-modification system, the genome-level possession trait for Type III
R-M loci coupling a Mod-like methyltransferase/specificity subunit with a
Res-like ATP-dependent restriction subunit. Butterer et al. describe Type III
restriction endonucleases as hetero-oligomeric assemblies encoded by `mod` and
`res` genes and support Res-to-Mod subunit stoichiometry in characterized
EcoP15I, EcoPI, and PstII complexes. The pinned DefenseFinder registry maps the
`RM_Type_III` subsystem to the 2023 REBASE update, requires both
`Type_III_MTases` and `Type_III_REases` groups in its rule row, and carries
custom HMM rows for both groups under the `RM_Type_III` system namespace.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for type III restriction-modification system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1044900` is reserved for this one-row class cohort. The v371 cohort used
`METPO:1044800`, so v372 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope Type III
restriction-modification system record, `type_iii_restriction_modification`
slug, `RM_Type_III` source key, `traitmech:000495`,
`metpo_traitmech_v372`, or `METPO:1044900`. The only pre-curation
Type III R-M candidate hit was a label-only note in the broad
`restriction_modification_system` research artifact.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1044900` | type III restriction-modification system | `METPO:1007694` restriction-modification system |

Type III restriction-modification system captures genome-level possession of a
Type III R-M locus. It excludes individual Type III Mod or Res subunits,
individual custom DefenseFinder HMM profiles, the source key `RM_Type_III`, the
broader Type I, Type II, Type IIG, and type IV branches, and the broader
restriction-modification parent.

`traitmech:000495` is a direct local child of `traitmech:000095`
restriction-modification system.

## External Mappings

No exact external mapping is proposed. The GO DNA restriction-modification
process, individual REBASE enzyme pages, individual Type III Mod and Res
proteins, DefenseFinder HMM profile groups, and source database rows naming the
`RM_Type_III` model are shifted from this organism-level GENOMICS possession
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  no exact synonyms and three related DefenseFinder source-key or profile-group
  synonyms.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000495` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000495` as traceability during the migration.

## Change Log

- v372, 2026-09: lifts `traitmech:000495 type III
  restriction-modification system` into the `METPO:1044900` placeholder
  block.
