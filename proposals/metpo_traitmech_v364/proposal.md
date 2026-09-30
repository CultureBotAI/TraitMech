# METPO ROBOT Template Proposal - VP1817 System (v364, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for VP1817 system, the
genome-level possession trait for one of the nine newly discovered Vibrio
parahaemolyticus integron-cassette anti-phage systems described by Getz et al.
Getz et al. cloned integron gene cassettes into VSV105 and identified nine
previously unrecognized systems that reduced bacteriophage plaquing. Their
supplementary tables map VP1817 to a cloned RIMD 2210633 integron cassette,
VSV105-vp1817, and VP1817 phage-plating readouts against Bas27 and Bas37, and
Supplementary Data 1's VP1817 worksheet reports a BAC60080.1 PSI-BLAST query.
The pinned DefenseFinder article registry maps VP1817 to the same Getz et al.
paper, and the pinned HMM inventory carries the VP1817__VP1817 custom profile.
The pinned DefenseFinder rules table checked in this curation pass has no VP1817
row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for VP1817 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1044100` is reserved for this one-row class cohort. The v363 cohort used
`METPO:1044000`, so v364 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus, excluding only `.git` and `.venv`. It found no exact same-scope
VP1817 TraitMech, METPO, history, or prior proposal record; no `vp1817_system`
slug; no `VP1817__VP1817`, `WP_024699215.1`, `BAC60080`, `ARC19819`, or
`VP_RS08765` mention; no `traitmech:000487`; no `metpo_traitmech_v364`; and no
`METPO:1044100` proposal block. The only pre-curation VP1817 mentions were in
the v362 VP1823 and v363 VP1796 proposals, which name VP1817 as a distinct
sibling system from the same Getz et al. integron-cassette branch.

Related records such as VP1796, VP1823, and VP1840 already cover sibling
integron-cassette systems from the same Getz et al. paper; none represents the
VP1817 branch.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1044100` | VP1817 system | `METPO:1016300` phage defense system |

VP1817 system captures genome-level possession of a VP1817-family
integron-cassette phage-defense locus represented by a custom DefenseFinder HMM
profile. It excludes the VP_RS08765 source locus tag, the individual BAC60080.1
query protein, the individual WP_024699215.1 protein, the VP1817 HMM profile
row, VSV105 plasmid-expression assays, bacteriophage fold-change assay rows,
PSI-BLAST homolog rows, the absent VP1817 rule-level DefenseFinder model,
unresolved VP1817 component activity and phage readouts, sibling VP1796, VP1823,
VP1826, VP1839, VP1840, VP1848, VP1851, and VP1853 systems, and other
integron-encoded or phage-defense systems.

`traitmech:000487` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `VP1817` synonym and related `VP1817__VP1817` DefenseFinder profile
  label.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000487` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000487` as traceability during the migration.

## Change Log

- v364, 2026-09: lifts `traitmech:000487 VP1817 system` into the
  `METPO:1044100` placeholder block.
