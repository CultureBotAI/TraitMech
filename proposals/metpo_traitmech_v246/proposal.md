# METPO ROBOT Template Proposal - Bil System (v246, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v245 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Bil system, the
genome-level possession trait for a bacterial ubiquitin-like conjugation
phage-defense locus. Hor et al. support Bil as an antiphage system that
covalently attaches a ubiquitin-like protein to the bacteriophage central tail
fibre and impairs phage infectivity. DefenseFinder maps the `Bil` key to the
Millman et al. bacterial antiphage-system discovery preprint in its article
registry, but the pinned HMM inventory and rules table have no exact `Bil` row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Bil |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1032300` is reserved for this one-row class cohort. The v245 cohort used
`METPO:1032200`, so v246 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository. It found no exact same-scope Bil system record, `bil_system`
slug, Hor et al. Nature DOI, `traitmech:000369`, `metpo_traitmech_v246`, or
`METPO:1032300`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1032300` | Bil system | `METPO:1016300` phage defense system |

Bil system captures genome-level possession of a bacterial ubiquitin-like
conjugation phage-defense locus that can covalently attach a ubiquitin-like
protein to the bacteriophage central tail fibre and impair phage infectivity. It
excludes individual ubiquitin-like proteins, E1 and E2 conjugating enzymes,
deubiquitinases, central-tail-fibre modification, impaired phage infectivity,
source database rows naming one Bil model, the unresolved Bil HMM or rule rows,
and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual Bil components, the
ubiquitin-like-protein conjugation process, the phage central tail fibre target,
and the DefenseFinder article-registry row are shifted from this organism-level
GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with two
  exact synonyms and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000369` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000369` as traceability during the migration.

## Change Log

- v246, 2026-09: lifts `traitmech:000369 Bil system` into the
  `METPO:1032300` block.
