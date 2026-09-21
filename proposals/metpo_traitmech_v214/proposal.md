# METPO ROBOT Template Proposal - CARD-NLR System (v214, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v213 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for CARD-NLR system, the
genome-level possession trait for a CARD-like/NLR-associated bacterial
anti-phage locus. Wein et al. report that bacterial CARD-like domains are
present in phage-defense systems and that multiple such systems use CARD-like
domains to activate cell-death effectors. The pinned DefenseFinder snapshot
contains CARD_NLR in its article registry, records CARD_NLR profiles in its HMM
inventory, and models CARD_NLR_Endonuclease, CARD_NLR_GasderMIN,
CARD_NLR_Phospho, CARD_NLR_Subtilase, and CARD_NLR_like subtypes in its rules
table.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for CARD-NLR |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1029100` is reserved for this one-row class cohort. The v213 cohort used
`METPO:1029000`, so v214 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository for exact TraitMech/METPO records and prior proposal/history
mentions. Separately, the pinned DefenseFinder article registry, HMM inventory,
and rules table supplied the positive CARD_NLR candidate rows used for
candidate discovery. No exact same-scope TraitMech or METPO record,
`card_nlr_system` slug, `CARD-NLR system` label, `traitmech:000337`,
`metpo_traitmech_v214`, `METPO:1029100`, `DOI:10.1101/2023.05.28.542683`, or
`https://europepmc.org/article/PPR/PPR668921` was present in the repository
before this cohort. Preexisting CARD_NLR mentions were confined to the
GasderMIN scope gap and the pinned `CARD_NLR_GasderMIN` DefenseFinder evidence
on `data/traits/genomics/gasdermin_system.yaml`; those are not exact CARD-NLR
system records or prior METPO proposals.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1029100` | CARD-NLR system | `METPO:1016300` phage defense system |

CARD-NLR system captures genome-level possession of a bacterial CARD-like
anti-phage detector locus represented by the DefenseFinder CARD_NLR model
namespace. It excludes individual bacterial CARD-like domains; NLR proteins;
individual gasdermins or GasderMIN system contexts; individual endonuclease,
CARD_NLR_Phospho, or Subtilase effector profiles; CARD-dependent gasdermin
activation; effector-mediated cell death; source database rows naming one
CARD_NLR model; and other bacterial phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual CARD-like domains, NLR
proteins, GasderMIN proteins, proteases, endonucleases, individual DefenseFinder
effector profiles, CARD-dependent activation processes, and cell-death effector
outputs are shifted from this organism-level GENOMICS possession trait.
`CARD_NLR`, `CARD_NLR__CARD_Protease`, and `CARD_NLR__NLR_new` are kept as
related synonyms because they denote DefenseFinder model and profile keys
rather than true labels for the organism-level trait itself.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  three related model/profile synonyms and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000337` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000337` as traceability during the migration.

## Change Log

- v214, 2026-09: lifts `traitmech:000337 CARD-NLR system` into the
  `METPO:1029100` block.
