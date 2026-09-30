# METPO ROBOT Template Proposal - Type IV Modification-Dependent Restriction System (v373, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for type IV
modification-dependent restriction system, the genome-level possession trait
for Type IV loci that attack modified DNA rather than the unmodified targets of
canonical Type I-III restriction-modification systems. Loenen and Raleigh define
Type IV as modification-dependent restriction and contrast it with
modification-blocked Types I-III. Bair and Black support GmrSD as a concrete
Type IV nuclease that targets glucosylated hydroxymethylcytosine DNA. The pinned
DefenseFinder registries model `RM_Type_IV` as an RM subsystem requiring the
`Type_IV_REases` group and carry eight custom HMM rows under that model
namespace.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for type IV modification-dependent restriction system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1045000` is reserved for this one-row class cohort. The v372 cohort used
`METPO:1044900`, so v373 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope Type IV
modification-dependent restriction system record,
`type_iv_modification_dependent_restriction_system` slug, `RM_Type_IV` source
key, `Other_Type_IV` source key, `traitmech:000496`,
`metpo_traitmech_v373`, or `METPO:1045000`. The only pre-curation broad Type IV
candidate hit was a label-only note in the broad
`restriction_modification_system` research artifact.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1045000` | type IV modification-dependent restriction system | `METPO:1016300` phage defense system |

Type IV modification-dependent restriction system captures genome-level
possession of a Type IV restriction-enzyme locus. It excludes the canonical
Type I, Type II, Type IIG, and Type III restriction-modification branches,
individual Type IV restriction-enzyme proteins, the DefenseFinder
`RM_Type_IV__Type_IV_REases` group, individual custom DefenseFinder HMM
profiles, DNA-modification substrate classes, and narrower article-registry
subfamilies such as McrBC and GmrSD_RM_Type_IV.

`traitmech:000496` is a direct local child of `traitmech:000209` phage defense
system. This proposal uses `METPO:1016300`, the v86 placeholder for
`traitmech:000209`, because Type IV modification-dependent restriction is
distinct from canonical Type I-III restriction-modification self/non-self
discrimination.

## External Mappings

No exact external mapping is proposed. Individual REBASE enzyme families,
individual Type IV restriction-enzyme proteins, DNA modification substrate
classes, DefenseFinder HMM profile groups, and source database rows naming the
`RM_Type_IV` model are shifted from this organism-level GENOMICS possession
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  no exact synonyms and three related DefenseFinder source-key or profile-group
  synonyms.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000496` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000496` as traceability during the migration.

## Change Log

- v373, 2026-09: lifts `traitmech:000496 type IV
  modification-dependent restriction system` into the `METPO:1045000`
  placeholder block.
