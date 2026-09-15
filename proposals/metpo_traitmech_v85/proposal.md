# METPO ROBOT Template Proposal - Homeoviscous Adaptation (v85, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v84 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for homeoviscous
adaptation, the membrane-acclimation stress response in which microbes remodel
lipid composition to maintain membrane viscosity and fluidity when temperature
changes perturb lipid packing. This cohort lifts the local fallback record for
homeoviscous adaptation. The local TraitMech record is parented to
`traitmech:000078` stress response. That parent was lifted as `METPO:1007677`
in `metpo_traitmech_v5`, so this proposal uses the same placeholder parent to
preserve the intended hierarchy until the upstream issue is consolidated and
METPO mints permanent IDs.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000208` was minted locally because METPO has no exact homeoviscous adaptation class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1016200` is reserved for this one-row class cohort. The v84 cohort used
`METPO:1016100`, so v85 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v85`, no live record used
`traitmech:000208`, and no prior proposal reserved `METPO:1016200`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1016200` | homeoviscous adaptation | `METPO:1007677` stress response |

Homeoviscous adaptation is the membrane-fluidity branch of stress response. It
captures the organism-level capacity to vary membrane lipid composition, such
as fatty-acid unsaturation, branching, or chain length, to maintain functional
membrane viscosity under temperature-driven bilayer-ordering stress. It
excludes the physical membrane-fluidity quality itself, individual Fab, Des, or
other lipid-metabolism proteins, and narrower lipid desaturation or fatty-acid
biosynthesis subprocesses.

## External Mappings

No exact external mapping is proposed. Existing membrane-fluidity,
fatty-acid-desaturation, membrane-lipid-biosynthesis, cold-response, and
temperature-response terms are narrower, broader, or shifted from this
organism-level membrane-acclimation trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  exact synonym, no exact external xrefs, and one related synonym.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000208` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000208` as traceability during the migration.

## Change Log

- v85, 2026-09: lifts `traitmech:000208 homeoviscous adaptation` into the
  `METPO:1016200` block.
