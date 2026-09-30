# METPO ROBOT Template Proposal - HEC-08 System (v356, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for HEC-08 system, the
genome-level possession trait for the HEPN-domain Hma-embedded candidate
anti-phage locus described by Payne et al. Payne et al. selected HEC-08 among
nine Hma-embedded candidate systems and reported that the seven active systems
remaining after HEC-01 and HEC-09 were excluded reduced the efficiency of
plaquing of at least two phages by several orders of magnitude. The pinned
DefenseFinder article registry maps HEC-08 to the same Payne preprint, and the
pinned HMM inventory carries one HEC-08 custom profile. The pinned DefenseFinder
rules table checked in this curation pass has no HEC-08 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for HEC-08 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1043300` is reserved for this one-row class cohort. The v355 cohort used
`METPO:1043200`, so v356 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus, excluding only `.git` and `.venv`. It found no exact same-scope
HEC-08 TraitMech, METPO, history, or prior proposal record; no `hec_08_system`
or `HEC-08__HEC-08` mention; no `traitmech:000479`; no
`metpo_traitmech_v356`; and no `METPO:1043300` proposal block.

The only live HEC-08 mentions before this proposal were sibling-boundary text in
the HEC-07 proposal and HEC-07's Payne et al. domain-list snippet, which names
HEC-08 only to distinguish HEC-07's RelE-domain branch from HEC-08's
HEPN-domain branch.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1043300` | HEC-08 system | `METPO:1016300` phage defense system |

HEC-08 system captures genome-level possession of the single-gene HEPN-domain
Hma-embedded candidate locus. It excludes the broader Hma systems that can embed
HEC loci, the broader set of Hma-embedded candidates, inactive HEC-01 and
HEC-09 candidates, sibling HEC-02 through HEC-07 systems, the HEC-08 protein
product, individual HEPN-domain proteins, the DefenseFinder HEC-08 profile row,
the absent pinned DefenseFinder rule row, direct phage triggers or effector
outputs, exact natural hosts or sensitive phages, and other phage-defense
systems.

`traitmech:000479` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `HEC-08` synonym and the related `HEC-08__HEC-08` DefenseFinder profile
  label.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000479` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000479` as traceability during the migration.

## Change Log

- v356, 2026-09: lifts `traitmech:000479 HEC-08 system` into the
  `METPO:1043300` placeholder block.
