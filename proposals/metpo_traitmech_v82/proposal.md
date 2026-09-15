# METPO ROBOT Template Proposal - Heat Shock Response (v82, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v81 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the heat-shock stress
response in which acute heat stress induces heat-shock proteins to restore
protein homeostasis. It only contains obsolete `METPO:1000154` heat shock
response. This cohort lifts the local fallback record for heat shock response.
The local TraitMech record is parented to `traitmech:000078` stress response.
That parent was lifted as `METPO:1007677` in `metpo_traitmech_v5`, so this
proposal uses the same placeholder parent to preserve the intended hierarchy
until the upstream issue is consolidated and METPO mints permanent IDs.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000205` was minted locally because METPO has no active exact heat shock response class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1015900` is reserved for this one-row class cohort. The v81 cohort used
`METPO:1015800`, so v82 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v82`, no live record used
`traitmech:000205`, and no prior proposal reserved `METPO:1015900`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1015900` | heat shock response | `METPO:1007677` stress response |

Heat shock response is the acute-temperature-upshift branch of stress response.
It captures the organism-level response that induces heat-shock proteins to
refold or degrade denatured proteins and restore protein homeostasis. It
excludes heat shock as an environmental exposure, individual heat-shock
proteins, chaperones, proteases, sigma factors, and organism growth traits such
as thermotolerance.

## External Mappings

No exact external mapping is proposed. `GO:0009408` response to heat is useful
for biological-process nodes but is broader than this organism-level
TraitRecord. Heat-shock protein, chaperone, and ATP-dependent-protease terms
describe narrower molecular machinery rather than the whole response phenotype.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  exact synonym, no exact external xrefs, and one related abbreviation.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000205` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000205` as traceability during the migration.

## Change Log

- v82, 2026-09: lifts `traitmech:000205 heat shock response` into the
  `METPO:1015900` block.
