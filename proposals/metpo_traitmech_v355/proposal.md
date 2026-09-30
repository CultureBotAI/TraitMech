# METPO ROBOT Template Proposal - HEC-07 System (v355, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for HEC-07 system, the
genome-level possession trait for the RelE-domain Hma-embedded candidate
anti-phage locus described by Payne et al. Payne et al. selected HEC-07 among
nine Hma-embedded candidate systems and reported that the seven active systems
remaining after HEC-01 and HEC-09 were excluded reduced the efficiency of
plaquing of at least two phages by several orders of magnitude. The pinned
DefenseFinder article registry maps HEC-07 to the same Payne preprint, and the
pinned HMM inventory carries one HEC-07 custom profile. The pinned DefenseFinder
rules table checked in this curation pass has no HEC-07 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for HEC-07 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1043200` is reserved for this one-row class cohort. The v354 cohort used
`METPO:1043100`, so v355 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus, excluding only `.git` and `.venv`. It found no exact same-scope
HEC-07 TraitMech, METPO, history, or prior proposal record; no `hec_07_system`
or `HEC-07__HEC-07` mention; no `traitmech:000478`; no
`metpo_traitmech_v355`; and no `METPO:1043200` proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1043200` | HEC-07 system | `METPO:1016300` phage defense system |

HEC-07 system captures genome-level possession of the single-gene RelE-domain
Hma-embedded candidate locus. It excludes the broader Hma systems that can embed
HEC loci, the broader set of Hma-embedded candidates, inactive HEC-01 and
HEC-09 candidates, sibling HEC-02 through HEC-06 and HEC-08 systems, the
HEC-07 protein product, individual RelE proteins or RelE-family toxin domains,
the pinned DefenseFinder HEC-07 profile row, the absent pinned DefenseFinder
rule row, direct phage triggers or effector outputs, exact natural hosts or
sensitive phages, and other phage-defense systems.

`traitmech:000478` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `HEC-07` synonym and the related `HEC-07__HEC-07` DefenseFinder profile
  label.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000478` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000478` as traceability during the migration.

## Change Log

- v355, 2026-09: lifts `traitmech:000478 HEC-07 system` into the
  `METPO:1043200` placeholder block.
