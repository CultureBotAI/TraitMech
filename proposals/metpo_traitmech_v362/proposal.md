# METPO ROBOT Template Proposal - VP1823 System (v362, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for VP1823 system, the
genome-level possession trait for one of the nine newly discovered Vibrio
parahaemolyticus integron-cassette anti-phage systems described by Getz et al.
Getz et al. cloned integron gene cassettes into VSV105 and identified nine
previously unrecognized systems that reduced bacteriophage plaquing. Their
supplementary tables map VP1823 to a cloned RIMD 2210633 integron cassette,
VSV105-vp1823, and VP1823 phage-plating readouts against Bas30 and T4, and
Supplementary Data 1's VP1823 worksheet reports a BAC60086.1 PSI-BLAST query.
The pinned DefenseFinder article registry maps VP1823 to the same Getz et al.
paper, and the pinned HMM inventory carries the VP1823__VP1823 custom profile.
The pinned DefenseFinder rules table checked in this curation pass has no VP1823
row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for VP1823 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1043900` is reserved for this one-row class cohort. The v361 cohort used
`METPO:1043800`, so v362 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus, excluding only `.git`, `.venv`, and generated trait pages. It
found no exact same-scope VP1823 TraitMech, METPO, history, or prior proposal
record; no `vp1823_system` slug; no `VP1823`, `VP1823__VP1823`,
`WP_079749463.1`, `BAC60086`, or `VP_RS08795` mention; no `traitmech:000485`;
no `metpo_traitmech_v362`; and no `METPO:1043900` proposal block.

Related records such as VP1840 already cover sibling integron-cassette systems
from the same Getz et al. paper; none represents the VP1823 branch.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1043900` | VP1823 system | `METPO:1016300` phage defense system |

VP1823 system captures genome-level possession of a VP1823-family
integron-cassette phage-defense locus represented by a custom DefenseFinder HMM
profile. It excludes the VP_RS08795 source locus tag, the individual
WP_079749463.1 protein, the VP1823 HMM profile row, VSV105
plasmid-expression assays, bacteriophage fold-change assay rows, PSI-BLAST
homolog rows, the absent VP1823 rule-level DefenseFinder model, unresolved
VP1823 component activity and phage readouts, sibling VP1796, VP1817, VP1826,
VP1839, VP1840, VP1848, VP1851, and VP1853 systems, and other integron-encoded
or phage-defense systems.

`traitmech:000485` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `VP1823` synonym and related `VP1823__VP1823` DefenseFinder profile
  label.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000485` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000485` as traceability during the migration.

## Change Log

- v362, 2026-09: lifts `traitmech:000485 VP1823 system` into the
  `METPO:1043900` placeholder block.
