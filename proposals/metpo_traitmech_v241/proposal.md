# METPO ROBOT Template Proposal - PrrC System (v241, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v240 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for PrrC system, the
genome-level possession trait for a `PrrC` phage-exclusion locus modeled by
DefenseFinder as a two-profile system requiring `PrrC__EcoprrI` and
`PrrC__PrrC`, with type I restriction-modification components accepted as
accessory markers. Uzan et al. describe PrrC as one of the T4 phage-exclusion
systems mediated by activation of a latent endoribonuclease, and Blanga-Kanfi
et al. support PrrC proteins linked with EcoprrI homologs as a family of
restriction RNases. DefenseFinder maps the `PrrC` key to the Uzan et al. review
while pinning custom `PrrC__EcoprrI` and `PrrC__PrrC` profiles for this system.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for PrrC |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1031800` is reserved for this one-row class cohort. The v240 cohort used
`METPO:1031700`, so v241 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository. It found prior Lit-system review snippets mentioning PrrC and
Uzan et al., but no exact same-scope PrrC-system record, `prrc_system` slug,
`PrrC__EcoprrI` or `PrrC__PrrC` profile row, Blanga-Kanfi DOI or PMID,
`traitmech:000364`, `metpo_traitmech_v241`, or `METPO:1031800`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1031800` | PrrC system | `METPO:1016300` phage defense system |

PrrC system captures genome-level possession of a `PrrC` locus represented by
DefenseFinder as a two-profile model requiring `PrrC__EcoprrI` and
`PrrC__PrrC`, with type I restriction-modification components accepted as
accessory markers. It excludes the individual PrrC anticodon nuclease, the
EcoprrI type Ic restriction endonuclease, the `PrrC__EcoprrI` and `PrrC__PrrC`
HMM profiles, generic type I restriction-modification systems, T4-encoded
EcoprrI inhibitors, PrrC-mediated tRNA cleavage, source database rows naming
one PrrC model, and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. PrrC-family RNases, EcoprrI homologs,
Type I restriction-modification systems, and T4-mediated PrrC activation are
shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact synonyms, four related shifted labels, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000364` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000364` as traceability during the migration.

## Change Log

- v241, 2026-09: lifts `traitmech:000364 PrrC system` into the
  `METPO:1031800` block.
