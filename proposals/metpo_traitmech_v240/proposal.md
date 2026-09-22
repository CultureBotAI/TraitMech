# METPO ROBOT Template Proposal - Lit System (v240, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v239 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Lit system, the
genome-level possession trait for a `Lit` phage-exclusion locus modeled by
DefenseFinder as a single-profile system requiring `Lit__Lit`. Copeland et al.
show that T4 bacteriophage exclusion can be mediated by the host-encoded Lit
peptidase in Escherichia coli K-12, and Uzan et al. describe Gol-Lit as one of
the T4 phage-exclusion systems mediated by activation of EF-Tu proteolysis.
DefenseFinder maps the `Lit` key to that review while pinning the custom
`Lit__Lit` profile for this system.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Lit |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1031700` is reserved for this one-row class cohort. The v239 cohort used
`METPO:1031600`, so v240 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository. It found no exact same-scope record, `lit_system` slug,
`Lit__Lit` profile, `Gol-Lit` system label, source PMIDs/DOIs,
`traitmech:000363`, `metpo_traitmech_v240`, or `METPO:1031700`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1031700` | Lit system | `METPO:1016300` phage defense system |

Lit system captures genome-level possession of a `Lit` locus represented by
DefenseFinder as a single-profile model requiring `Lit__Lit`. It excludes the
individual Lit peptidase, the `Lit__Lit` HMM profile, the E. coli K-12 e14
defective prophage, the bacteriophage T4 Gol peptide and gp23 major-head-protein
context, Lit-mediated EF-Tu cleavage, Gol-activated cell death, source database
rows naming one Lit model, and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Lit peptidases, the Gol peptide,
EF-Tu cleavage, and cell death after T4 infection are shifted from this
organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact synonyms, three related shifted labels, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000363` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000363` as traceability during the migration.

## Change Log

- v240, 2026-09: lifts `traitmech:000363 Lit system` into the
  `METPO:1031700` block.
