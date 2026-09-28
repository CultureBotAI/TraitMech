# METPO ROBOT Template Proposal - CoCoNuT System (v299, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v298 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for CoCoNuT system, the
genome-level possession trait for the coiled-coil nuclease tandem branch of
McrBC Type IV restriction systems. Bell et al. identify CoCoNuTs as a previously
uncharacterized McrBC/Type IV branch, predict RNA targeting and possible DNA
targeting from component domains and genomic context, and the pinned
DefenseFinder HMM inventory records CoCoNut custom profile rows for CoCoNut-I,
CoCoNut-II, and CoCoNut-III namespaces.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for CoCoNuT system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1037600` is reserved for this one-row class cohort. The v298 cohort used
`METPO:1037500`, so v299 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope CoCoNuT TraitMech, METPO,
history, or prior proposal record, no `coconut_system` slug, no
`traitmech:000422`, no `metpo_traitmech_v299`, and no `METPO:1037600` /
`METPO:10376xx` proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1037600` | CoCoNuT system | `METPO:1016300` phage defense system |

CoCoNuT system captures genome-level possession of a coiled-coil nuclease
tandem Type IV restriction-system locus represented by DefenseFinder CoCoNut
HMM-profile namespaces. It excludes individual `Cnu*` genes and proteins,
GTPase, HEPN, McrC, OB-fold, CARF, and RtcR-like domains, individual
DefenseFinder HMM profile rows, pseudo-CoCoNuT models pending scope review,
CARF-regulated superoperons, unresolved RNA and DNA substrate predictions, the
absent DefenseFinder rule-level model, and other McrBC, restriction, or
phage-defense systems.

`traitmech:000422` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `CoCoNut` and representative
`CoCoNut-*__*_Cnu*` HMM row names are kept as related synonyms because they name
DefenseFinder source and profile keys rather than the genome-level possession
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `CoCoNuT` synonym and related DefenseFinder source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000422` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000422` as traceability during the migration.

## Change Log

- v299, 2026-09: lifts `traitmech:000422 CoCoNuT system` into the
  `METPO:1037600` block.
