# METPO ROBOT Template Proposal - Detocs System (v179, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v178 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Detocs system, the
genome-level possession trait for a Detocs anti-phage locus. Rousset et al.
discovered and characterized Detocs as bacterial defense systems with
two-component phosphotransfer-signaling architecture in a Cell paper on
phage-triggered ATP and dATP degradation, and DefenseFinder catalogs Detocs with
required `dtcA` and `dtcB` profiles plus optional `dtcC`-family profiles.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Detocs |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1025600` is reserved for this one-row class cohort. The v178 cohort used
`METPO:1025500`, so v179 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v179`, no live record used
`traitmech:000302`, and no prior proposal reserved `METPO:1025600`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1025600` | Detocs system | `METPO:1016300` phage defense system |

Detocs system captures genome-level possession of a locus represented in
DefenseFinder by DtcA and DtcB profiles plus optional DtcC-family profiles, with
an ATP nucleosidase output that can degrade ATP and dATP upon phage infection
and halt phage propagation. It excludes individual `dtcA`, `dtcB`, or `dtcC`
genes; Dtc proteins; Detocs HMM profiles; individual DtcC REase, TOPRIM, or
hydrolase subtypes; ATP nucleosidase activity outside a complete Detocs locus;
generic two-component phosphotransfer signaling; source-database rows naming
one Detocs locus; unresolved Detocs phage triggers; unresolved DtcC-variant
effector outputs; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Dtc component profiles, DtcC-family
subtypes, ATP nucleosidase activity, and DefenseFinder rows are shifted from
this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact Detocs synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000302` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000302` as traceability during the migration.

## Change Log

- v179, 2026-09: lifts `traitmech:000302 Detocs system` into the
  `METPO:1025600` block.
