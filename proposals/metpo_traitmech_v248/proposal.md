# METPO ROBOT Template Proposal - GAPS1 System (v248, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v247 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for GAPS1 system, the
genome-level possession trait for a GAPS1 bacterial phage-defense locus encoded
by Gamma-Mobile-Trio islands. Mahata et al. support GAPS1 as one of four
GMT-island anti-phage defense systems and connect GAPS1 to
phage-capsid-protein-triggered cell dormancy. DefenseFinder maps the `GAPS1`
key to the Mahata et al. preprint in its article registry and models the system
in the pinned rule and HMM tables with a single `GAPS1__GAPS1` profile.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for GAPS1 |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1032500` is reserved for this one-row class cohort. The v247 cohort used
`METPO:1032400`, so v248 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository. It found no exact same-scope GAPS1 system record,
`gaps1_system` slug, Mahata et al. Nature Microbiology DOI, Mahata et al.
preprint DOI, `traitmech:000371`, `metpo_traitmech_v248`, or `METPO:1032500`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1032500` | GAPS1 system | `METPO:1016300` phage defense system |

GAPS1 system captures genome-level possession of a GMT-island-associated GAPS1
locus that can be triggered by a phage capsid protein to induce cell dormancy.
It excludes individual GAPS1 genes or proteins, the DefenseFinder
`GAPS1__GAPS1` profile, the phage capsid-protein trigger, cell dormancy outside
a complete GAPS1 locus, sibling GAPS2, GAPS4, or GAPS6 systems, Gamma-Mobile-Trio
islands as mobile elements, antibacterial type VI secretion effectors, and other
phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual GAPS1 components, the
DefenseFinder GAPS1__GAPS1 profile, phage-capsid-protein sensing, GAPS1-induced
cell dormancy, GMT islands as mobile elements, and source database rows naming
one GAPS1 model are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000371` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000371` as traceability during the migration.

## Change Log

- v248, 2026-09: lifts `traitmech:000371 GAPS1 system` into the
  `METPO:1032500` block.
