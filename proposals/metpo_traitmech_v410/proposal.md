# METPO ROBOT Template Proposal - Hma System (v410, 2026-10)

## Summary

This cohort reserves `METPO:1048700` for `Hma system`, a
phage-defense-system trait in which a genome-encoded Hma locus carries HmaA,
HmaB, and HmaC components. The local TraitMech fallback is
`traitmech:000533`.

This cohort lifts one local class:

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Hma system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## ID Block

`METPO:1048700` is reserved for this one-row class cohort. The v409 cohort used
`METPO:1048600`, so v410 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation exact candidate search included ignored and hidden files across
`data/traits`, `history`, `proposals`, `research`, `mappings`, `reports`, `app`,
`scripts`, `tests`, `docs`, `README.md`, `.github`, and `.claude`. It found no
hit for `traitmech:000533`, `METPO:1048700`, `metpo_traitmech_v410`,
`hma_system`, or `Hma system`. The prior Hma mentions were contextual references
from Hma-embedded-candidate HEC records and proposals, and no live METPO,
TraitMech, history, or prior proposal record represented the broader Hma system.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1048700` | Hma system | `METPO:1016300` phage defense system |

Hma system captures organism-level possession of the Hma locus that Payne et al.
predicted as a three-gene candidate defense system and that DefenseFinder
represents with the HmaA, HmaB, and HmaC HMM rows. It excludes individual HmaA,
HmaB, and HmaC proteins, individual DefenseFinder Hma profile rows, the Hma
source key outside a complete organism-level system, Hma-embedded candidate
systems HEC-01 through HEC-09, accessory defense systems inserted in the hma
region, unresolved HmaB/HmaC activities, the absent Hma rule-level
DefenseFinder model, direct phage triggers or effector outputs, and other
phage-defense systems.

`traitmech:000533` is a direct local child of `traitmech:000209` phage defense
system. This proposal uses `METPO:1016300`, the v86 placeholder for
`traitmech:000209`.

## External Mappings

No exact external mapping is proposed. Individual Hma proteins, HEC systems, hma
region accessory defenses, predicted PADLOC or DefenseFinder profile rows, and
helicase, methyltransferase, ATPase, or nuclease activities outside complete
Hma-system possession are shifted from this organism-level GENOMICS trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000533` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000533` as traceability during the migration.

## Change Log

- v410, 2026-10: lifts `traitmech:000533 Hma system` into the
  `METPO:1048700` placeholder block.
