# METPO ROBOT Template Proposal - VP1826 System (v365, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for VP1826 system, the
genome-level possession trait for one of the nine newly discovered Vibrio
parahaemolyticus integron-cassette anti-phage systems described by Getz et al.
Getz et al. cloned integron gene cassettes into VSV105 and identified nine
previously unrecognized systems that reduced bacteriophage plaquing. Their
supplementary tables map VP1826 to a cloned RIMD 2210633 integron cassette,
VSV105-vp1826, and VP1826 phage-plating readouts against Bas4, Bas6, and
Bas9, and Supplementary Data 1's VP1826 worksheet reports a BAC60089.1
PSI-BLAST query. The pinned DefenseFinder article registry maps VP1826 to the
same Getz et al. paper, and the pinned HMM inventory carries the
VP1826__VP1826 custom profile. The pinned DefenseFinder rules table checked in
this curation pass has no VP1826 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for VP1826 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1044200` is reserved for this one-row class cohort. The v364 cohort used
`METPO:1044100`, so v365 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus, excluding only `.git` and `.venv`. It found no exact same-scope
VP1826 TraitMech, METPO, history, or prior proposal record; no `vp1826_system`
slug; no `VP1826__VP1826`, `WP_005464673.1`, `BAC60089`, or `VP_RS08820`
mention; no `traitmech:000488`; no `metpo_traitmech_v365`; and no
`METPO:1044200` proposal block. The only pre-curation VP1826 mentions were in
the v362 VP1823, v363 VP1796, and v364 VP1817 proposals, which name VP1826 as a
distinct sibling system from the same Getz et al. integron-cassette branch.

Related records such as VP1796, VP1817, VP1823, and VP1840 already cover
sibling integron-cassette systems from the same Getz et al. paper; none
represents the VP1826 branch.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1044200` | VP1826 system | `METPO:1016300` phage defense system |

VP1826 system captures genome-level possession of a VP1826-family
integron-cassette phage-defense locus represented by a custom DefenseFinder HMM
profile. It excludes the VP_RS08820 locus tag, the individual BAC60089.1 query
protein, the individual WP_005464673.1 protein, the source Vp1826 cassette
label, the VP1826 HMM profile row, VSV105 plasmid-expression assays,
bacteriophage fold-change assay rows, PSI-BLAST homolog rows, the absent VP1826
rule-level DefenseFinder model, unresolved VP1826 component activity and phage
readouts, sibling VP1796, VP1817, VP1823, VP1839, VP1840, VP1848, VP1851, and
VP1853 systems, and other integron-encoded or phage-defense systems.

`traitmech:000488` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `VP1826` synonym and related `Vp1826` and `VP1826__VP1826` labels.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000488` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000488` as traceability during the migration.

## Change Log

- v365, 2026-09: lifts `traitmech:000488 VP1826 system` into the
  `METPO:1044200` placeholder block.
