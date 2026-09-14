# METPO ROBOT Template Proposal - Anaerobic Ammonium Oxidation (v65, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v64 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the microbial metabolism
trait in which ammonium is anaerobically oxidized with nitrite as the electron
acceptor to form dinitrogen. This cohort lifts the local fallback record for
anaerobic ammonium oxidation and keeps it separate from neighboring nitrogen
transformations such as nitrification, denitrification, and dissimilatory
nitrate reduction to ammonium.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000188` was minted locally because METPO has no active equivalent anaerobic ammonium oxidation class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1014200` is reserved for this one-row class cohort. The v64 cohort used
`METPO:1014100`, so v65 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `.claude/`, generated pages, scripts,
tests, and ignored/hidden files. `METPO:1014200` appeared only in the v64
next-block reservation note and its matching history record, no prior proposal
reserved `metpo_traitmech_v65`, and no `traitmech:000188` or exact live
`anaerobic ammonium oxidation` TraitRecord/proposal row existed before this
addition. The search found only the deprecated `METPO:1000812 obsolete
Anaerobic ammonium oxidation` and `METPO:1002010 obsolete Anaerobic
ammonium-oxidizing` classes in the pinned METPO snapshot plus anammox research
leads in broader nitrogen-cycling and environmental records.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1014200` | anaerobic ammonium oxidation | `METPO:1008800` nitrogen respiration |

Anaerobic ammonium oxidation is an anaerobic nitrogen metabolism in which
ammonium is oxidized with nitrite as the electron acceptor to form dinitrogen.
The class is parented to nitrogen respiration because nitrite is the oxidized
nitrogen electron acceptor for this energy-conserving metabolism.

## External Mappings

No exact external mapping is proposed. The pinned METPO snapshot contains only
obsolete anammox classes, and candidate GO classes should be checked against
the primary Gene Ontology release before proposing an exact xref because
component ammonium- or nitrite-oxidation processes are narrower than the whole
anammox metabolism.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with an
  exact anammox synonym, one related anaerobic-ammonia-oxidation label, and no
  exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000188` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000188` as traceability during the migration.

## Change Log

- v65, 2026-09: lifts `traitmech:000188 anaerobic ammonium oxidation` into the
  `METPO:1014200` block.
