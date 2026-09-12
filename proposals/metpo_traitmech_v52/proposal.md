# METPO ROBOT Template Proposal - Type IV Pilus (v52, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v51 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The morphology gap sweep left cell-surface appendages as reusable morphology
candidates not yet represented as standalone TraitMech records. METPO's local
snapshot has an obsolete generic `pilus` term but no live exact `type IV pilus`
class, while TraitMech already uses the GO cellular-component concept as a
causal-graph node in `motile`, `motility`, `twitching motility`, and
`predatory bacterium`.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000175` was minted locally because METPO has no equivalent live type IV pilus class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1012900` is reserved for this one-row class cohort. The v51 cohort used
`METPO:1012800`, so v52 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included `data/raw/metpo.owl`, `proposals/`, `data/traits/`,
`reports/`, `research/`, `history/`, `mappings/`, `.claude/`, generated pages,
scripts, tests, and ignored/hidden files. `METPO:1012900` appeared only in
the v51 next-block reservation note, no prior proposal reserved
`metpo_traitmech_v52`, and no `traitmech:000175` or type IV pilus
TraitRecord/proposal row existed before this addition.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1012900` | type IV pilus | `METPO:1000059` phenotype |

Type IV pili are dynamic extracellular cell-surface filaments assembled from
type IV pilins. The proposed term captures the organismal morphology phenotype
where a cell produces this appendage; behaviors such as twitching motility,
natural competence, prey attachment, and biofilm formation can continue to use
type IV pilus nodes as causal machinery without making those behaviors
duplicates of the morphology trait.

## External Mappings

`GO:0044096` names the cellular component `type IV pilus` and is an appropriate
structural xref for the proposed organism-level morphology phenotype. The
record does not assert a separate SSSOM equivalence because the GO term denotes
the appendage itself rather than the phenotype of producing it.

The plural label `type IV pili` and the abbreviation `T4P` are true exact
synonyms in the cited reviews and are therefore proposed as exact synonyms.
`type IV pilus filament` is included only as a related synonym because it names
the structural fiber rather than the organism-level phenotype.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000175` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000175` as traceability during the migration.

## Change Log

- v52, 2026-09: lifts `traitmech:000175 type IV pilus` into the
  `METPO:1012900` block.
