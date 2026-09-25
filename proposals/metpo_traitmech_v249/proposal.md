# METPO ROBOT Template Proposal - Mok-Hok-Sok System (v249, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v248 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Mok-Hok-Sok system, the
genome-level possession trait for a Hok/Sok toxin-antitoxin locus. Pecota and
Wood support T4 exclusion by a plasmid R1 hok/sok locus, and DefenseFinder maps
the `Mok_Hok_Sok` key to that paper in its article registry and models the
system in the pinned rule and HMM tables with `Mok_Hok_Sok__Hok` and
`Mok_Hok_Sok__Mok` profiles.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Mok-Hok-Sok |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1032600` is reserved for this one-row class cohort. The v248 cohort used
`METPO:1032500`, so v249 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository. It found no exact same-scope Mok-Hok-Sok system record,
`mok_hok_sok_system` slug, Pecota and Wood DOI, Pecota and Wood PMID,
`traitmech:000372`, `metpo_traitmech_v249`, or `METPO:1032600`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1032600` | Mok-Hok-Sok system | `METPO:1016300` phage defense system |

Mok-Hok-Sok system captures genome-level possession of a hok/sok
toxin-antitoxin locus represented by DefenseFinder as a Hok/Mok two-profile
model and experimentally linked to bacteriophage T4 exclusion by the plasmid R1
hok/sok locus. It excludes individual hok, mok, or sok genes, the Hok toxin
protein, the Sok antisense RNA, the Mok_Hok_Sok source key, the DefenseFinder
`Mok_Hok_Sok__Hok` and `Mok_Hok_Sok__Mok` profiles, plasmid R1 replication,
post-segregational killing, and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual Hok/Mok proteins, the Sok
antisense RNA, post-segregational killing activity, plasmid maintenance,
DefenseFinder HMM profiles, and source database rows naming one Hok/Mok model
are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  no exact synonyms, no exact external xrefs, and one related source-key
  synonym.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000372` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000372` as traceability during the migration.

## Change Log

- v249, 2026-09: lifts `traitmech:000372 Mok-Hok-Sok system` into the
  `METPO:1032600` block.
