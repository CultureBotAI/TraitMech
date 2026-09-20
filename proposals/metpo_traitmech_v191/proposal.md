# METPO ROBOT Template Proposal - 6A-MBL System (v191, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v190 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for 6A-MBL system, the
genome-level possession trait for a 6A-MBL anti-phage locus. van den Berg et
al. reported a search over bacterial homologs of innate eukaryotic antiviral
defense genes, deposited a stable record that names 6A-MBL as a putative
MBL-nuclease system candidate, and validated six phage defense systems.
DefenseFinder catalogs 6A-MBL with `6A_MBL__cap2_3` and `6A_MBL__MblB` HMM
profile entries.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for 6A-MBL |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1026800` is reserved for this one-row class cohort. The v190 cohort used
`METPO:1026700`, so v191 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository
working tree outside `.git` and `.venv`. No exact search hit was found for
`6A_MBL`, `6A-MBL`, `6A MBL`, `cap2_3`, `MblB`, `six_a_mbl`,
`traitmech:000314`, `metpo_traitmech_v191`, or `METPO:1026800`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1026800` | 6A-MBL system | `METPO:1016300` phage defense system |

6A-MBL system captures genome-level possession of a 6A-MBL locus cataloged by
DefenseFinder under the 6A_MBL model namespace with `6A_MBL__cap2_3` and
`6A_MBL__MblB` HMM profile entries. It excludes individual cap2_3 or mblB
genes; Cap2-3 or MblB proteins; DefenseFinder HMM profiles; source-database
rows naming one 6A-MBL locus; unresolved 6A-MBL trigger or effector activities;
and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. The 6A_MBL model namespace,
`6A_MBL__cap2_3` HMM, `6A_MBL__MblB` HMM, individual component genes, their
corresponding proteins, and unresolved 6A-MBL molecular outputs are shifted
from this organism-level GENOMICS possession trait.

`6A_MBL`, `cap2_3`, and `MblB` are proposed as related synonyms, not exact
synonyms, because they are source-profile labels or source-system keys rather
than lexical names for the organism-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  exact 6A-MBL synonym sourced to stable naming evidence, three related
  non-exact DefenseFinder labels, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000314` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000314` as traceability during the migration.

## Change Log

- v191, 2026-09: lifts `traitmech:000314 6A-MBL system` into the
  `METPO:1026800` block.
- PR #1147 review, 2026-09: resolves issue #1148 by adding exact 6A-MBL
  naming evidence from van den Berg et al.'s stable Zenodo record.
