# METPO ROBOT Template Proposal - Lanthivirin System (v293, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v292 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for lanthivirin system, the
genome-level possession trait for lanthipeptide biosynthetic gene clusters with
anti-phage activity. Serra et al. support lanthivirins as anti-phage systems,
and the pinned DefenseFinder article registry maps its Lanthiphage source key
to the lanthipeptide anti-phage preprint.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for lanthivirin system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1037000` is reserved for this one-row class cohort. The v292 cohort used
`METPO:1036900`, so v293 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files outside
`.git` across the curation corpus. It found no exact same-scope Lanthiphage or
lanthivirin record, `lanthivirin_system` slug, Serra et al. DOI,
`traitmech:000416`, `metpo_traitmech_v293`, or `METPO:1037000` /
`METPO:10370xx` proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1037000` | lanthivirin system | `METPO:1016300` phage defense system |

Lanthivirin system captures genome-level possession of a lanthipeptide
biosynthetic gene cluster that confers anti-phage activity. It excludes
individual lanthivirin genes or Lph proteins, isolated lanthipeptide
biosynthesis proteins, anti-phage activity outside a complete lanthivirin
biosynthetic gene cluster, source database rows naming one Lanthiphage model,
DefenseFinder HMM profile rows, the absent DefenseFinder Lanthiphage rules row,
unresolved mature lanthivirin effector chemistry, and other phage-defense
systems.

`traitmech:000416` is a direct local child of `traitmech:000209` phage defense
system. This proposal uses `METPO:1016300`, the v86 placeholder for
`traitmech:000209`, as the closest proposed upstream ancestor.

## External Mappings

No exact external mapping or exact synonym is proposed. `lanthivirin BGC` is
included as a related synonym because it names the genetic element rather than
the possession trait. `Lanthiphage` is included as a related synonym because it
is the DefenseFinder source key and not the peer-reviewed label for the same
class.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  `lanthivirin BGC` and `Lanthiphage` related synonyms.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000416` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000416` as traceability during the migration.

## Change Log

- v293, 2026-09: lifts `traitmech:000416 lanthivirin system` into the
  `METPO:1037000` block.
