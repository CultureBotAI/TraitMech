# METPO ROBOT Template Proposal - Rst TIR-NLR System (v254, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v253 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Rst TIR-NLR system,
the genome-level possession trait for a P4-like TIR-NLR anti-phage locus.
Rousset et al. experimentally linked a cloned TIR-NLR system to broad
virulent-phage and P2-like phage protection, and DefenseFinder models the
locus as the single-profile `Rst_TIR-NLR` system in its pinned rule and HMM
tables.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Rst TIR-NLR system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1033100` is reserved for this one-row class cohort. The v253 cohort
used `METPO:1033000`, so v254 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope Rst TIR-NLR system record,
`rst_tir_nlr` slug, `Rst_TIR-NLR` source key, `traitmech:000377`,
`metpo_traitmech_v254`, or `METPO:1033100`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1033100` | Rst TIR-NLR system | `METPO:1016300` phage defense system |

Rst TIR-NLR system captures genome-level possession of a P4-like TIR-NLR locus
represented by DefenseFinder as the Rst_TIR-NLR single-profile model. It
excludes individual TIR/STAND/TPR genes, individual TIR/STAND/TPR proteins, the
DefenseFinder `Rst_TIR-NLR__TIR` profile, the source key `Rst_TIR-NLR`, P4
satellites as mobile genetic elements, TIR-domain signaling outside a complete
TIR-NLR locus, P2-like phage restriction outside a complete TIR-NLR locus, and
other Rst or phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual P4 genes or proteins, source
database rows naming the DefenseFinder model, TIR-domain profiles, STAND or TPR
annotations, and P2-like phage resistance are shifted from this organism-level
GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  no exact external xrefs and related DefenseFinder and article-label synonyms.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000377` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000377` as traceability during the migration.

## Change Log

- v254, 2026-09: lifts `traitmech:000377 Rst TIR-NLR system` into the
  `METPO:1033100` block.
