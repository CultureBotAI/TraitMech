# METPO ROBOT Template Proposal - Cold Shock Response (v83, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v82 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the cold-shock stress
response in which a rapid temperature downshift induces nucleic-acid-binding
cold-shock proteins and RNA-remodeling functions. It only contains obsolete
`METPO:1000068` cold shock response. This cohort lifts the local fallback
record for cold shock response. The local TraitMech record is parented to
`traitmech:000078` stress response. That parent was lifted as `METPO:1007677`
in `metpo_traitmech_v5`, so this proposal uses the same placeholder parent to
preserve the intended hierarchy until the upstream issue is consolidated and
METPO mints permanent IDs.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000206` was minted locally because METPO has no active exact cold shock response class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1016000` is reserved for this one-row class cohort. The v82 cohort used
`METPO:1015900`, so v83 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v83`, no live record used
`traitmech:000206`, and no prior proposal reserved `METPO:1016000`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1016000` | cold shock response | `METPO:1007677` stress response |

Cold shock response is the acute-temperature-downshift branch of stress
response. It captures the organism-level response that induces
nucleic-acid-binding cold-shock proteins and RNA-remodeling functions to
preserve low-temperature gene expression. It excludes cold shock as an
environmental exposure, broader response to cold terms, individual cold-shock
proteins, cold-shock domains, RNA helicases, ribosome-biogenesis factors, and
organism growth traits such as psychrotolerance.

## External Mappings

No exact external mapping is proposed. `GO:0009409` response to cold is useful
for broad biological-process nodes but is broader than this rapid
temperature-downshift cold-shock response. CspA-family, cold-shock-domain, RNA
helicase, nuclease, and ribosome-associated terms describe narrower molecular
machinery rather than the whole response phenotype.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  exact synonym, no exact external xrefs, and no related synonyms.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000206` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000206` as traceability during the migration.

## Change Log

- v83, 2026-09: lifts `traitmech:000206 cold shock response` into the
  `METPO:1016000` block.
