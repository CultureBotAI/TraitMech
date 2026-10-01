# METPO ROBOT Template Proposal - Dag System (v384, 2026-10)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Dag system, the
genome-level possession trait for a Dag-family DNA-glycosylase phage-defense
system. Getz et al. support Dag1 and Dag2 as widespread anti-phage
DNA-glycosylase families whose antiviral effectors selectively target phages
carrying modified guanine bases. The pinned DefenseFinder article registry maps
`Dag` to the Getz et al. bioRxiv DOI, while the pinned HMM inventory and rules
table have no exact Dag row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Dag system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1046100` is reserved for this one-row class cohort. The v383 cohort used
`METPO:1046000`, so v384 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope Dag system record, `dag_system`
slug, `traitmech:000507`, `METPO:1046100`, `metpo_traitmech_v384`, Getz et al.
Nature DOI `10.1038/s41564-026-02441-0`, Getz et al. bioRxiv DOI
`10.1101/2025.10.29.685425`, or title `Antiviral defence is a conserved
function of diverse bacterial DNA glycosylases`.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1046100` | Dag system | `METPO:1016300` phage defense system |

Dag system captures genome-level possession of a Dag-family DNA-glycosylase
phage-defense system with Dag1 or Dag2 antiviral effectors that selectively
target phages carrying modified guanine bases. It excludes individual Dag1 or
Dag2 protein families, individual `dag1` or `dag2` genes, DNA glycosylase
activity outside a complete Dag anti-phage system, individual modified-guanine
phage targets, other defense-associated DNA glycosylases, and the DefenseFinder
`Dag` source key outside a complete organism-level system.

`traitmech:000507` is a direct local child of `traitmech:000209` phage defense
system. This proposal uses `METPO:1016300`, the v86 placeholder for
`traitmech:000209`.

## External Mappings

No exact external mapping is proposed. Individual Dag1 or Dag2 proteins,
individual `dag1` or `dag2` loci, modified-guanine phage substrates, the broader
DNA-glycosylase antiviral effector class, and the DefenseFinder article-registry
key are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000507` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000507` as traceability during the migration.

## Change Log

- v384, 2026-10: lifts `traitmech:000507 Dag system` into the
  `METPO:1046100` placeholder block.
