# METPO ROBOT Template Proposal - VP1848 System (v367, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for VP1848 system, the
genome-level possession trait for one of the nine newly discovered Vibrio
parahaemolyticus integron-cassette anti-phage systems described by Getz et al.
Getz et al. cloned integron gene cassettes into VSV105 and identified nine
previously unrecognized systems that reduced bacteriophage plaquing. Their
supplementary tables map VP1848 to a cloned RIMD 2210633 integron cassette,
VSV105-vp1848, and VP1848 phage-plating readouts against Bas64 and Bas65, and
Supplementary Data 1's VP1848 worksheet reports a BAC60111.1 PSI-BLAST query.
The pinned DefenseFinder article registry maps VP1848 to the same Getz et al.
paper, and the pinned HMM inventory carries the VP1848__VP1848 custom profile.
The pinned DefenseFinder rules table checked in this curation pass has no
VP1848 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for VP1848 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1044400` is reserved for this one-row class cohort. The v366 cohort used
`METPO:1044300`, so v367 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus, excluding only `.git` and `.venv`. It found no exact same-scope
VP1848 TraitMech, METPO, history, or prior proposal record; no `vp1848_system`
slug; no `VP1848__VP1848`, `WP_005483286.1`, `BAC60111`, or `VP_RS08970`
mention; no `traitmech:000490`; no `metpo_traitmech_v367`; and no
`METPO:1044400` proposal block. The only pre-curation VP1848 mentions were in
the v362 VP1823, v363 VP1796, v364 VP1817, v365 VP1826, and v366 VP1839
proposals, which name VP1848 as a distinct sibling system from the same Getz et
al. integron-cassette branch.

Related records such as VP1796, VP1817, VP1823, VP1826, VP1839, and VP1840
already cover sibling integron-cassette systems from the same Getz et al.
paper; none represents the VP1848 branch.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1044400` | VP1848 system | `METPO:1016300` phage defense system |

VP1848 system captures genome-level possession of a VP1848-family
integron-cassette phage-defense locus represented by a custom DefenseFinder HMM
profile. It excludes the VP_RS08970 source locus tag, the individual BAC60111.1
query protein, the individual WP_005483286.1 protein, the source Vp1848 cassette
label, the VP1848 HMM profile row, VSV105 plasmid-expression assays,
bacteriophage fold-change assay rows, PSI-BLAST homolog rows, the absent VP1848
rule-level DefenseFinder model, unresolved VP1848 component activity and phage
readouts, sibling VP1796, VP1817, VP1823, VP1826, VP1839, VP1840, VP1851, and
VP1853 systems, and other integron-encoded or phage-defense systems.

`traitmech:000490` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `VP1848` synonym and related `Vp1848` and `VP1848__VP1848` labels.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000490` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000490` as traceability during the migration.

## Change Log

- v367, 2026-09: lifts `traitmech:000490 VP1848 system` into the
  `METPO:1044400` placeholder block.
