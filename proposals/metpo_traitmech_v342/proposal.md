# METPO ROBOT Template Proposal - HEC-04 System (v342, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for HEC-04 system, the
genome-level possession trait for the single-gene Hma-embedded candidate locus
from Payne et al.'s preprint on phage-defense systems embedded within Hma
immune systems. Payne et al. describe HEC-04 as encoding an ATPase fused to a
TOPRIM domain, include HEC-04 in the active Hma-embedded candidate systems that
reduced bacteriophage plaquing, and show that intact ABC ATPase and nuclease
active-site residues are required for HEC-04-mediated defense. The pinned
DefenseFinder article registry maps HEC-04 to the same
Hma-embedded-candidate preprint, the pinned DefenseFinder HMM inventory records
one HEC-04 custom profile, `HEC-04__HEC-04`, and the pinned DefenseFinder
rules table checked in this curation pass has no HEC-04 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for HEC-04 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1041900` is reserved for this one-row class cohort. The v341 cohort
used `METPO:1041800`, so v342 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope HEC-04 TraitMech, METPO,
history, or prior proposal record, no `HEC-04__HEC-04` profile-key mention, no
`hec_04_system` slug, no `traitmech:000465`, no `metpo_traitmech_v342`, and no
`METPO:1041900` proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1041900` | HEC-04 system | `METPO:1016300` phage defense system |

HEC-04 system captures genome-level possession of the single-gene
Hma-embedded candidate phage-defense locus represented by the
`HEC-04__HEC-04` DefenseFinder custom HMM-profile row. It excludes individual
ABC ATPase or TOPRIM-family nuclease domains, the source database row naming
one HEC-04 model, the DefenseFinder HEC-04 HMM profile row, the absent HEC-04
rule-level DefenseFinder model, unresolved HEC-04 component activity and phage
readouts, and other Hma-embedded candidate or phage-defense systems.

`traitmech:000465` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `HEC-04__HEC-04` is kept as a related
synonym because it names a DefenseFinder profile key rather than the
genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `HEC-04` synonym and related source/profile key.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000465` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000465` as traceability during the migration.

## Change Log

- v342, 2026-09: lifts `traitmech:000465 HEC-04 system` into the
  `METPO:1041900` placeholder block.
