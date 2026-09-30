# METPO ROBOT Template Proposal - VP1851 System (v368, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for VP1851 system, the
genome-level possession trait for one of the nine newly discovered Vibrio
parahaemolyticus integron-cassette anti-phage systems described by Getz et al.
Getz et al. cloned integron gene cassettes into VSV105 and identified nine
previously unrecognized systems that reduced bacteriophage plaquing. Their
supplementary tables map VP1851 to a cloned RIMD 2210633 integron cassette,
VSV105-vp1851, and VP1851 phage-plating readouts against LL1 and VL1, and
Supplementary Data 1's VP1851 worksheet reports a WP_005483174.1 PSI-BLAST
query. The pinned DefenseFinder article registry maps VP1851 to the same Getz
et al. paper, and the pinned HMM inventory carries the VP1851__VP1851 custom
profile. The pinned DefenseFinder rules table checked in this curation pass has
no VP1851 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for VP1851 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1044500` is reserved for this one-row class cohort. The v367 cohort used
`METPO:1044400`, so v368 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus, excluding only `.git` and `.venv`. It found no exact same-scope
VP1851 TraitMech, METPO, history, or prior proposal record; no `vp1851_system`
slug; no `VP1851__VP1851`, `WP_005483174`, `ARC19782`, or `VP_RS09000`
mention; no `traitmech:000491`; no `metpo_traitmech_v368`; and no
`METPO:1044500` proposal block. The only pre-curation VP1851 mentions were in
the v362 VP1823, v363 VP1796, v364 VP1817, v365 VP1826, v366 VP1839, and v367
VP1848 proposals, which name VP1851 as a distinct sibling system from the same
Getz et al. integron-cassette branch.

Related records such as VP1796, VP1817, VP1823, VP1826, VP1839, VP1840, and
VP1848 already cover sibling integron-cassette systems from the same Getz et
al. paper; none represents the VP1851 branch.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1044500` | VP1851 system | `METPO:1016300` phage defense system |

VP1851 system captures genome-level possession of a VP1851-family
integron-cassette phage-defense locus represented by a custom DefenseFinder HMM
profile. It excludes the VP_RS09000 source locus tag, the individual
WP_005483174.1 query protein, the individual ARC19782.1 PSI-BLAST hit, the
source Vp1851 cassette label, the VP1851 HMM profile row, VSV105
plasmid-expression assays, bacteriophage fold-change assay rows, PSI-BLAST
homolog rows, the absent VP1851 rule-level DefenseFinder model, unresolved
VP1851 component activity and phage readouts, sibling VP1796, VP1817, VP1823,
VP1826, VP1839, VP1840, VP1848, and VP1853 systems, and other integron-encoded
or phage-defense systems.

`traitmech:000491` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `VP1851` synonym and related `Vp1851` and `VP1851__VP1851` labels.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000491` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000491` as traceability during the migration.

## Change Log

- v368, 2026-09: lifts `traitmech:000491 VP1851 system` into the
  `METPO:1044500` placeholder block.
