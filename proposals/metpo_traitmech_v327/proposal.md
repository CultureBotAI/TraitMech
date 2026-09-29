# METPO ROBOT Template Proposal - VP1840 System (v327, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for VP1840 system, the
genome-level possession trait for the Vp1840-like Vibrio parahaemolyticus
integron-defense locus represented by DefenseFinder model key VP1840.
Getz et al. cloned V. parahaemolyticus RIMD 2210633 gene cassette vp1840,
expressed it from the VSV105-vp1840 plasmid, and reported strong fold-change
reductions in bacteriophage plating assays. Supplementary Data 1 reports
PSI-BLAST homologs, the pinned DefenseFinder article registry maps VP1840 to
the Getz et al. paper, the pinned DefenseFinder HMM inventory records one
VP1840 custom profile, `VP1840__VP1840`, and the pinned DefenseFinder rules
table checked in this curation pass has no VP1840 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for VP1840 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1040400` is reserved for this one-row class cohort. The v326 cohort used
`METPO:1040300`, so v327 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope VP1840 TraitMech, METPO, history,
or prior proposal record, no `Vp1840` source-locus mention, no
`VP1840__VP1840` profile-key mention, no `WP_005483293.1` product-accession
mention, no `vp1840_system` slug, no `traitmech:000450`, no
`metpo_traitmech_v327`, and no `METPO:1040400` proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1040400` | VP1840 system | `METPO:1016300` phage defense system |

VP1840 system captures genome-level possession of a Vp1840-like integron
defense locus cataloged by DefenseFinder as VP1840 and represented by the
custom VP1840__VP1840 HMM-profile row. It excludes the Vp1840 source locus
tag, the VP_RS08920 locus tag, the VP1840 protein, the individual DefenseFinder
HMM profile row, VSV105 plasmid-expression assays, bacteriophage fold-change
assay rows, PSI-BLAST homolog rows, the absent VP1840 rule-level DefenseFinder
model, unresolved component activity, unresolved phage breadth, and other
integron-encoded or phage-defense systems.

`traitmech:000450` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `Vp1840` is kept as a related synonym
because it names the RIMD 2210633 source locus tag, and `VP1840__VP1840` is
kept as a related synonym because it names a DefenseFinder profile key rather
than the genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `VP1840` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000450` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000450` as traceability during the migration.

## Change Log

- v327, 2026-09: lifts `traitmech:000450 VP1840 system` into the
  `METPO:1040400` placeholder block.
