# METPO ROBOT Template Proposal - SOS Response (v84, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v83 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the bacterial
DNA-damage SOS response in which RecA/LexA-mediated sensing of DNA damage
derepresses the SOS regulon. This cohort lifts the local fallback record for
SOS response. The local TraitMech record is parented to `traitmech:000078`
stress response. That parent was lifted as `METPO:1007677` in
`metpo_traitmech_v5`, so this proposal uses the same placeholder parent to
preserve the intended hierarchy until the upstream issue is consolidated and
METPO mints permanent IDs.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000207` was minted locally because METPO has no exact SOS response class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1016100` is reserved for this one-row class cohort. The v83 cohort used
`METPO:1016000`, so v84 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v84`, no live record used
`traitmech:000207`, and no prior proposal reserved `METPO:1016100`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1016100` | SOS response | `METPO:1007677` stress response |

SOS response is the DNA-damage-inducible branch of stress response. It captures
the organism-level capacity to sense DNA damage through the classical
RecA/LexA cascade and derepress an SOS regulon that coordinates DNA repair,
damage tolerance, transient division arrest, and mutagenic survival functions.
It excludes DNA damage as a trigger, broader DNA-damage-response terms,
individual RecA, LexA, SulA, and translesion-polymerase proteins, DNA-repair
processes outside SOS control, and downstream prophage-induction events.

## External Mappings

No exact external mapping is proposed. `GO:0009432` SOS response is useful for
biological-process nodes in causal graphs but is shifted from this
organism-level stress-response trait. RecA, LexA, SulA,
translesion-synthesis, error-prone polymerase, prophage-induction, DNA-repair,
and DNA-damage terms describe narrower machinery, downstream processes, or
related triggers rather than the whole phenotype.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact synonyms, no exact external xrefs, and one related synonym.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000207` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000207` as traceability during the migration.

## Change Log

- v84, 2026-09: lifts `traitmech:000207 SOS response` into the
  `METPO:1016100` block.
