# METPO ROBOT Template Proposal - Magnetotaxis (v53, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v52 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The earlier morphology sweep intentionally left magnetotaxis as a behavioral
follow-up distinct from the `magnetosome` intracellular-organelle record.
TraitMech already uses `magnetotaxis` as the downstream
`BIOLOGICAL_PROCESS` node in `magnetosome`'s causal graph, but it had no
standalone record for the behavior itself. The local METPO snapshot carries
only an obsolete `magnetotaxis` class, so there is no live upstream class to
seed.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000176` was minted locally because METPO has no equivalent live magnetotaxis class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1013000` is reserved for this one-row class cohort. The v52 cohort used
`METPO:1012900`, so v53 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `mappings/`, `.claude/`, generated pages,
scripts, tests, and ignored/hidden files. `METPO:1013000` appeared only in the
v52 next-block reservation note, no prior proposal reserved
`metpo_traitmech_v53`, and no `traitmech:000176` or exact magnetotaxis
TraitRecord/proposal row existed before this addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1013000` | magnetotaxis | `METPO:1000059` phenotype |

Magnetotaxis is a behavioral physiology rather than a structural organelle:
magnetosomes make the cell into a magnetic dipole, while magnetotaxis is the
resulting geomagnetic-field-aligned navigation behavior. Keeping the behavior
as its own class lets the existing `magnetosome` graph point to the behavioral
outcome without making the magnetosome structure and the motility phenotype
duplicates.

## External Mappings

No exact external ontology mapping is asserted. `magnetoaerotaxis` is included
as a related synonym because it names oxygen/redox-zone navigation assisted by
magnetic alignment rather than the exact generic alignment behavior.
`GO:0110143` names the magnetosome cellular component and already belongs on
the `magnetosome` record; the local METPO snapshot's `METPO:1000180`
`magnetotaxis` class is obsolete.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000176` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000176` as traceability during the migration.

## Change Log

- v53, 2026-09: lifts `traitmech:000176 magnetotaxis` into the
  `METPO:1013000` block.
