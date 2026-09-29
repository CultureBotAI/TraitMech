# METPO ROBOT Template Proposal - HEC-06 System (v344, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for HEC-06 system, the
genome-level possession trait for the single-gene Hma-embedded candidate locus
from Payne et al.'s preprint on phage-defense systems embedded within Hma
immune systems. Payne et al. describe HEC-06 as one of the GmrSD-like HEC
candidates and include HEC-06 in the active Hma-embedded candidate systems
that reduced bacteriophage plaquing. The pinned DefenseFinder article registry
maps HEC-06 to the same Hma-embedded-candidate preprint, the pinned
DefenseFinder HMM inventory records one HEC-06 custom profile,
`HEC-06__HEC-06`, and the pinned DefenseFinder rules table checked in this
curation pass has no HEC-06 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for HEC-06 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1042100` is reserved for this one-row class cohort. The v343 cohort
used `METPO:1042000`, so v344 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope HEC-06 TraitMech, METPO,
history, or prior proposal record, no `HEC-06__HEC-06` profile-key mention, no
`hec_06_system` slug, no `traitmech:000467`, no `metpo_traitmech_v344`, and no
`METPO:1042100` proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1042100` | HEC-06 system | `METPO:1016300` phage defense system |

HEC-06 system captures genome-level possession of the single-gene
Hma-embedded candidate phage-defense locus represented by the
`HEC-06__HEC-06` DefenseFinder custom HMM-profile row. It excludes individual
GmrSD-like proteins, the source database row naming one HEC-06 model, the
DefenseFinder HEC-06 HMM profile row, the absent HEC-06 rule-level
DefenseFinder model, unresolved HEC-06 component activity and phage readouts,
and other Hma-embedded candidate or phage-defense systems.

`traitmech:000467` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `HEC-06__HEC-06` is kept as a related
synonym because it names a DefenseFinder profile key rather than the
genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `HEC-06` synonym and related source/profile key.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000467` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000467` as traceability during the migration.

## Change Log

- v344, 2026-09: lifts `traitmech:000467 HEC-06 system` into the
  `METPO:1042100` placeholder block.
