# METPO ROBOT Template Proposal - DUF262 Schlafen System (v407, 2026-10)

## Summary

This cohort reserves `METPO:1048400` for `DUF262 Schlafen system`, a
phage-defense-system trait in which a genome-encoded prokaryotic Schlafen
nuclease locus is associated with a DUF262 architecture. The exact
DefenseFinder source key is `DUF262_Shlafen`, and the local TraitMech fallback
is `traitmech:000530`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DUF262 Schlafen system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1048400` is reserved for this one-row class cohort. The v406 cohort used
`METPO:1048300`, so v407 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files across
`data/traits`, `history`, `proposals`, `scripts`, `docs`, `reports`, and `pages`,
excluding generated ROBOT outputs and `.venv`. It found no hit for
`DUF262_Shlafen`, `DUF262 Schlafen`, `duf262_schlafen_system`,
`traitmech:000530`, `METPO:1048400`, or `metpo_traitmech_v407`. The Perez
Taboada et al. DOI is already used by the sibling Ig-like Schlafen and
Resolvase Schlafen system records, but the DUF262 Schlafen source key, slug,
fallback CURIE, placeholder CURIE, and proposal cohort were absent.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1048400` | DUF262 Schlafen system | `METPO:1016300` phage defense system |

DUF262 Schlafen system captures organism-level possession of a
DUF262-associated prokaryotic Schlafen nuclease locus. It excludes individual
Schlafen proteins, individual prokaryotic `schlafen` genes, non-DUF262
prokaryotic Schlafen nuclease architectures, general DUF262-domain activities
outside a complete anti-phage Schlafen system, and the DefenseFinder
`DUF262_Shlafen` source key outside a complete organism-level system.

`traitmech:000530` is a direct local child of `traitmech:000209` phage defense
system. This proposal uses `METPO:1016300`, the v86 placeholder for
`traitmech:000209`.

## External Mappings

No exact external mapping is proposed. Individual Schlafen proteins, individual
prokaryotic `schlafen` genes, DUF262-associated component domains, the broader
Schlafen antiviral effector class, and the DefenseFinder article-registry key
are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000530` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000530` as traceability during the migration.

## Change Log

- v407, 2026-10: lifts `traitmech:000530 DUF262 Schlafen system` into the
  `METPO:1048400` placeholder block.
