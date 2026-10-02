# METPO ROBOT Template Proposal - Resolvase Schlafen System (v406, 2026-10)

## Summary

This cohort reserves `METPO:1048300` for `Resolvase Schlafen system`, a
phage-defense-system trait in which a genome-encoded prokaryotic Schlafen
nuclease locus is associated with a resolvase architecture. The exact
DefenseFinder source key is `Resolvase_Schlafen`, and the local TraitMech
fallback is `traitmech:000529`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Resolvase Schlafen system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1048300` is reserved for this one-row class cohort. The v405 cohort used
`METPO:1048200`, so v406 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files across
`data/traits`, `history`, `proposals`, `scripts`, `docs`, `reports`, and `pages`,
excluding generated ROBOT outputs and `.venv`. It found no hit for
`Resolvase_Schlafen`, `Resolvase Schlafen`, `resolvase_schlafen_system`,
`traitmech:000529`, `METPO:1048300`, or `metpo_traitmech_v406`. The Perez
Taboada et al. DOI is already used by the sibling Ig-like Schlafen system
record, but the Resolvase Schlafen source key, slug, fallback CURIE, placeholder
CURIE, and proposal cohort were absent.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1048300` | Resolvase Schlafen system | `METPO:1016300` phage defense system |

Resolvase Schlafen system captures organism-level possession of a
resolvase-associated prokaryotic Schlafen nuclease locus. It excludes individual
Schlafen proteins, individual prokaryotic `schlafen` genes, non-resolvase
prokaryotic Schlafen nuclease architectures, general recombinase or resolvase
activities outside a complete anti-phage Schlafen system, and the DefenseFinder
`Resolvase_Schlafen` source key outside a complete organism-level system.

`traitmech:000529` is a direct local child of `traitmech:000209` phage defense
system. This proposal uses `METPO:1016300`, the v86 placeholder for
`traitmech:000209`.

## External Mappings

No exact external mapping is proposed. Individual Schlafen proteins, individual
prokaryotic `schlafen` genes, resolvase-associated component domains, the
broader Schlafen antiviral effector class, and the DefenseFinder
article-registry key are shifted from this organism-level GENOMICS possession
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000529` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000529` as traceability during the migration.

## Change Log

- v406, 2026-10: lifts `traitmech:000529 Resolvase Schlafen system` into the
  `METPO:1048300` placeholder block.
