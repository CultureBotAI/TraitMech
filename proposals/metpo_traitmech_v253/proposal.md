# METPO ROBOT Template Proposal - Rst Gop-Beta-CII System (v253, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v252 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Rst gop-beta-cII
system, the genome-level possession trait for a P4-like gop-beta-cII
anti-phage locus. Rousset et al. experimentally linked the canonical P4
`gop-β-cII` locus to protection against lambda and P1 phages, and DefenseFinder
models the locus as the three-profile `Rst_gop_beta_cll` system in its pinned
rule and HMM tables.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Rst gop-beta-cII system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1033000` is reserved for this one-row class cohort. The v252 cohort used
`METPO:1032900`, so v253 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope Rst gop-beta-cII system record,
`rst_gop_beta_cll` slug, `Rst_gop_beta_cll` source key,
`traitmech:000376`, `metpo_traitmech_v253`, or `METPO:1033000`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1033000` | Rst gop-beta-cII system | `METPO:1016300` phage defense system |

Rst gop-beta-cII system captures genome-level possession of a P4-like
gop-beta-cII locus represented by DefenseFinder as the Rst_gop_beta_cll
three-profile model. It excludes individual gop, beta, or cII genes, individual
Gop, beta, or CII proteins, the DefenseFinder `Rst_gop_beta_cll__gop`,
`Rst_gop_beta_cll__beta`, and `Rst_gop_beta_cll__cll` profiles, the source key
`Rst_gop_beta_cll`, P4 satellites as mobile genetic elements, lambda or P1
resistance outside a complete gop-beta-cII locus, and other Rst or
phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual P4 genes or proteins, source
database rows naming the DefenseFinder model, gop or beta toxin-antitoxin
activity, and lambda or P1 resistance are shifted from this organism-level
GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  one exact literature synonym, no exact external xrefs, and one related
  DefenseFinder source-key synonym.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000376` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000376` as traceability during the migration.

## Change Log

- v253, 2026-09: lifts `traitmech:000376 Rst gop-beta-cII system` into the
  `METPO:1033000` block.
