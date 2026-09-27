# METPO ROBOT Template Proposal - Clover System (v292, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v291 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Clover system, the
genome-level possession trait for a phage-defense system that coordinates
CloA dGTPase activation and CloB/p3diT-dependent suppression of CloA activity.
Yu and Kranzusch experimentally support Clover as a bacterial anti-phage
defence system in which CloA dynamically responds to an activating phage cue
and to an inhibitory nucleotide immune signal produced by CloB. The pinned
DefenseFinder article registry maps the Clover system name to that article.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Clover system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1036900` is reserved for this one-row class cohort. The v291 cohort used
`METPO:1036800`, so v292 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files outside
`.git` across the curation corpus. It found no exact same-scope Clover record,
`clover_system` slug, Yu and Kranzusch DOI, `traitmech:000415`,
`metpo_traitmech_v292`, or `METPO:1036900` / `METPO:10369xx` proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1036900` | Clover system | `METPO:1016300` phage defense system |

Clover system captures genome-level possession of an anti-phage system whose
CloA dGTPase dynamically responds to phage-linked dTTP increases and a
CloB-produced p3diT inhibitory signal. It excludes individual `CloA` or `CloB`
genes or proteins, dGTPase activity as a molecular function, p3diT signalling
as a biological process, source database rows naming one Clover system,
DefenseFinder model rows that are absent from the pinned HMM and rules files,
and other phage-defense systems.

`traitmech:000415` is a direct local child of `traitmech:000209` phage defense
system. This proposal uses `METPO:1016300`, the v86 placeholder for
`traitmech:000209`, as the closest proposed upstream ancestor.

## External Mappings

No exact external mapping is proposed. `Clover` is included as an exact synonym
because Yu and Kranzusch use the token for the characterized anti-phage defence
system and the pinned DefenseFinder article registry uses the same token as a
system name.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with the
  Clover system name as an exact synonym.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000415` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000415` as traceability during the migration.

## Change Log

- v292, 2026-09: lifts `traitmech:000415 Clover system` into the
  `METPO:1036900` block.
