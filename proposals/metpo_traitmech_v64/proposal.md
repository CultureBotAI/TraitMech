# METPO ROBOT Template Proposal - Complete Ammonia Oxidation (v64, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v63 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the microbial
metabolism trait in which a single organism performs both nitrification steps,
oxidizing ammonia via nitrite to nitrate. This cohort lifts the local fallback
record for complete ammonia oxidation and keeps it separate from the broader
`METPO:1005001` nitrification class, which does not require both steps to occur
inside the same organism.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000187` was minted locally because METPO has no active equivalent complete ammonia oxidation class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1014100` is reserved for this one-row class cohort. The v63 cohort used
`METPO:1014000`, so v64 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `.claude/`, generated pages, scripts,
tests, and ignored/hidden files. `METPO:1014100` appeared only in the v63
next-block reservation note and its matching history record, no prior proposal
reserved `metpo_traitmech_v64`, and no `traitmech:000187` or exact live
`complete ammonia oxidation` TraitRecord/proposal row existed before this
addition. The search found only the deprecated `METPO:1000862 obsolete Complete
ammonia oxidation` class in the pinned METPO snapshot plus complete
ammonia-oxidation research leads in broader nitrogen-cycling and environmental
records.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1014100` | complete ammonia oxidation | `METPO:1005001` nitrification |

Complete ammonia oxidation is a nitrification metabolism in which a single
organism oxidizes ammonia via nitrite to nitrate. The class is parented to the
active METPO nitrification process but is narrower because both oxidation steps
are catalyzed by the same organism.

## External Mappings

No exact external mapping is proposed. `GO:0019329` denotes ammonia oxidation,
`GO:0019332` denotes nitrite oxidation, and `METPO:1005001` denotes the broader
complete nitrification process without the one-organism constraint.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with an
  exact comammox synonym, one related complete-nitrification label, and no exact
  external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000187` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000187` as traceability during the migration.

## Change Log

- v64, 2026-09: lifts `traitmech:000187 complete ammonia oxidation` into the
  `METPO:1014100` block.
