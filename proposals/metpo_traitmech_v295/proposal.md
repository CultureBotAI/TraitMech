# METPO ROBOT Template Proposal - HEC-03 System (v295, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v294 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for HEC-03 system, the
genome-level possession trait for the two-gene Hma-embedded candidate locus
whose complete gene set was required for phage defense in the Payne et al.
candidate-system study. The pinned DefenseFinder article registry maps HEC-03
to the same Hma-embedded-candidate preprint, and the pinned HMM inventory
records HEC-03A and HEC-03B custom profile rows.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for HEC-03 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1037200` is reserved for this one-row class cohort. The v294 cohort used
`METPO:1037100`, so v295 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files outside
`.git` across the curation corpus. It found no exact same-scope HEC-03 record,
`hec_03_system` slug, Payne et al. DOI except existing HEC-02 citations,
`traitmech:000418`, `metpo_traitmech_v295`, or `METPO:1037200` /
`METPO:10372xx` proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1037200` | HEC-03 system | `METPO:1016300` phage defense system |

HEC-03 system captures genome-level possession of a two-gene
Hma-embedded candidate locus that reduces bacteriophage plaquing when both
HEC-03 genes are present. It excludes individual HEC-03A or HEC-03B genes,
individual ABC ATPase or PilT N-terminal-domain proteins, unresolved HEC-03
effector chemistry, source database rows naming one HEC-03 model,
DefenseFinder HEC-03 HMM profile rows, the absent DefenseFinder HEC-03 rules
row, and other Hma-embedded candidate or phage-defense systems.

`traitmech:000418` is a direct local child of `traitmech:000209` phage defense
system. This proposal uses `METPO:1016300`, the v86 placeholder for
`traitmech:000209`, as the closest proposed upstream ancestor.

## External Mappings

No exact external mapping is proposed. `HEC-03` is included as an exact synonym
because Payne et al. explicitly name it as one of the two-gene systems whose
complete gene set was required for defense.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with the
  `HEC-03` exact synonym.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000418` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000418` as traceability during the migration.

## Change Log

- v295, 2026-09: lifts `traitmech:000418 HEC-03 system` into the
  `METPO:1037200` block.
