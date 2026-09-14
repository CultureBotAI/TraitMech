# METPO ROBOT Template Proposal - Arsenite Oxidation (v66, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v65 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the microbial
metabolism trait in which arsenite is enzymatically oxidized to arsenate. This
cohort lifts the local fallback record for arsenite oxidation and keeps it
separate from the neighboring arsenic-tolerance records, which model ArsC
arsenate reduction and arsenite efflux as cytosolic detoxification routes.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000189` was minted locally because METPO has no active equivalent arsenite oxidation class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1014300` is reserved for this one-row class cohort. The v65 cohort used
`METPO:1014200`, so v66 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `.claude/`, generated pages, scripts,
tests, and ignored/hidden files. `METPO:1014300` appeared only in the v65
next-block reservation note and its matching history record, no prior proposal
reserved `metpo_traitmech_v66`, and no `traitmech:000189` or exact live
`arsenite oxidation` TraitRecord/proposal row existed before this addition. The
search found only the deprecated `METPO:1000840 obsolete Arsenite oxidation`
class in the pinned METPO snapshot plus arsenite-oxidation boundary notes in
arsenic- and metal-tolerance research artifacts.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1014300` | arsenite oxidation | `METPO:1000060` metabolism |

Arsenite oxidation is a metabolism in which an organism enzymatically oxidizes
arsenite to arsenate as an energy-generating electron donor or detoxification
substrate. The class is parented to metabolism because arsenite oxidation can
support chemolithoautotrophic growth in some taxa and detoxification in others.

## External Mappings

No exact external mapping is proposed. Candidate arsenite oxidase molecular
function terms are narrower than the organism-level arsenite oxidation
metabolism, and the pinned METPO snapshot contains only the obsolete
`METPO:1000840` class.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with an
  exact As(III)-oxidation synonym, one related microbial-arsenite-oxidation
  label, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000189` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000189` as traceability during the migration.

## Change Log

- v66, 2026-09: lifts `traitmech:000189 arsenite oxidation` into the
  `METPO:1014300` block.
