# METPO ROBOT Template Proposal - Resolvase DUF5677 System (v408, 2026-10)

## Summary

This cohort reserves `METPO:1048500` for `Resolvase DUF5677 system`, a
phage-defense-system trait in which a genome-encoded prokaryotic Schlafen
nuclease locus is associated with a Resolvase_DUF5677 architecture. The exact
DefenseFinder source key is `Resolvase_DUF5677`, and the local TraitMech
fallback is `traitmech:000531`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Resolvase DUF5677 system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1048500` is reserved for this one-row class cohort. The v407 cohort used
`METPO:1048400`, so v408 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files across
`data/traits`, `history`, `proposals`, `scripts`, `docs`, `reports`, and `pages`,
excluding generated ROBOT outputs and `.venv`. It found no hit for
`Resolvase_DUF5677`, `Resolvase DUF5677`, `resolvase_duf5677_system`,
`traitmech:000531`, `METPO:1048500`, or `metpo_traitmech_v408`. The Perez
Taboada et al. DOI is already used by sibling Ig-like Schlafen, Resolvase
Schlafen, and DUF262 Schlafen system records, but the Resolvase DUF5677 source
key, slug, fallback CURIE, placeholder CURIE, and proposal cohort were absent.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1048500` | Resolvase DUF5677 system | `METPO:1016300` phage defense system |

Resolvase DUF5677 system captures organism-level possession of a
Resolvase_DUF5677 prokaryotic Schlafen nuclease locus. It excludes individual
Schlafen proteins, individual prokaryotic `schlafen` genes, non-Resolvase_DUF5677
prokaryotic Schlafen nuclease architectures, general DUF5677-domain activities
outside a complete anti-phage Schlafen system, general resolvase activity, and
the DefenseFinder `Resolvase_DUF5677` source key outside a complete
organism-level system.

`traitmech:000531` is a direct local child of `traitmech:000209` phage defense
system. This proposal uses `METPO:1016300`, the v86 placeholder for
`traitmech:000209`.

## External Mappings

No exact external mapping is proposed. Individual Schlafen proteins, individual
prokaryotic `schlafen` genes, DUF5677-associated component domains, the broader
Schlafen antiviral effector class, and the DefenseFinder article-registry key
are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000531` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000531` as traceability during the migration.

## Change Log

- v408, 2026-10: lifts `traitmech:000531 Resolvase DUF5677 system` into the
  `METPO:1048500` placeholder block.
