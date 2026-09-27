# METPO ROBOT Template Proposal - RAZR System (v288, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v287 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for RAZR system, the
genome-level possession trait for a ring-activated zinc-finger HEPN RNase
phage-defense locus that can assemble into an active ring around phage protein
ring scaffolds, cleave RNA broadly, inhibit translation, and restrict phage
propagation. Zhang et al. experimentally support RAZR as a bacterial immune
RNase activated by the geometry of phage-encoded ring scaffolds, and the pinned
DefenseFinder article registry links the RAZR system name to that article.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for RAZR system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1036500` is reserved for this one-row class cohort. The v287 cohort used
`METPO:1036400`, so v288 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope RAZR record, `razr_system` slug,
`RAZR`, `RazR`, `ring-activated zinc-finger RNase`, the Zhang et al. DOI,
`traitmech:000411`, `metpo_traitmech_v288`, or `METPO:1036500` /
`METPO:10365xx` proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1036500` | RAZR system | `METPO:1016300` phage defense system |

RAZR system captures genome-level possession of a phage-defense locus encoding
a RAZR zinc-finger HEPN RNase. It excludes individual `razr` genes, RAZR RNase
proteins, HEPN or zinc-finger domains, the active RAZR ring complex,
nonspecific RNA-cleavage or translation-inhibition activities, individual phage
ring trigger proteins, source database rows naming one RAZR system,
DefenseFinder model rows that are absent from the pinned HMM and rules files,
and neighboring phage-defense systems.

`traitmech:000411` is a direct local child of `traitmech:000209` phage defense
system. This proposal uses `METPO:1016300`, the v86 placeholder for
`traitmech:000209`, as the closest proposed upstream ancestor.

## External Mappings

No exact external mapping is proposed. `RAZR` is included as a related synonym
because Zhang et al. use the acronym for the characterized RNase and the pinned
DefenseFinder article registry uses the same token as a system name, making the
bare acronym useful for search but ambiguous as the primary exact label for an
organism-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  RAZR acronym as a related synonym.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000411` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000411` as traceability during the migration.

## Change Log

- v288, 2026-09: lifts `traitmech:000411 RAZR system` into the
  `METPO:1036500` block.
