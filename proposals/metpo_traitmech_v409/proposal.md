# METPO ROBOT Template Proposal - Resolvase KAP NTPase System (v409, 2026-10)

## Summary

This cohort reserves `METPO:1048600` for `Resolvase KAP NTPase system`, a
phage-defense-system trait in which a genome-encoded prokaryotic Schlafen
nuclease locus is associated with a Resolvase_KAP_NTPase architecture. The exact
DefenseFinder source key is `Resolvase_KAP_NTPase`, and the local TraitMech
fallback is `traitmech:000532`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Resolvase KAP NTPase system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1048600` is reserved for this one-row class cohort. The v408 cohort used
`METPO:1048500`, so v409 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files across
`data/traits`, `history`, `proposals`, `scripts`, `docs`, `reports`, and `pages`,
excluding generated ROBOT outputs and `.venv`. It found no hit for
`Resolvase_KAP_NTPase`, `Resolvase KAP NTPase`,
`resolvase_kap_ntpase_system`, `traitmech:000532`, `METPO:1048600`, or
`metpo_traitmech_v409`. The Perez Taboada et al. DOI is already used by sibling
Ig-like Schlafen, Resolvase Schlafen, DUF262 Schlafen, and Resolvase DUF5677
system records, but the Resolvase KAP NTPase source key, slug, fallback CURIE,
placeholder CURIE, and proposal cohort were absent.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1048600` | Resolvase KAP NTPase system | `METPO:1016300` phage defense system |

Resolvase KAP NTPase system captures organism-level possession of a
Resolvase_KAP_NTPase prokaryotic Schlafen nuclease locus. It excludes individual
Schlafen proteins, individual prokaryotic `schlafen` genes,
non-Resolvase_KAP_NTPase prokaryotic Schlafen nuclease architectures, general
KAP NTPase-domain activities outside a complete anti-phage Schlafen system,
general resolvase activity, and the DefenseFinder `Resolvase_KAP_NTPase` source
key outside a complete organism-level system.

`traitmech:000532` is a direct local child of `traitmech:000209` phage defense
system. This proposal uses `METPO:1016300`, the v86 placeholder for
`traitmech:000209`.

## External Mappings

No exact external mapping is proposed. Individual Schlafen proteins, individual
prokaryotic `schlafen` genes, KAP NTPase-associated component domains, the
broader Schlafen antiviral effector class, and the DefenseFinder
article-registry key are shifted from this organism-level GENOMICS possession
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000532` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000532` as traceability during the migration.

## Change Log

- v409, 2026-10: lifts `traitmech:000532 Resolvase KAP NTPase system` into the
  `METPO:1048600` placeholder block.
