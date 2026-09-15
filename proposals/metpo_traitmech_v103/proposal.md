# METPO ROBOT Template Proposal - ToxIN System (v103, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v102 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the ToxIN system, the
genome-level possession trait for an abortive-infection system in which an
organism possesses a toxIN type III protein-RNA toxin-antitoxin locus whose
ToxN toxin and tandem ToxI RNA antitoxins constitute a two-component Abi module
that inhibits bacterial growth and restricts phage propagation. The v91 cohort
proposed the broader `abortive infection system` parent for Abi defense
families; v102 split AbiQ into its own narrower child; and this cohort splits
ToxIN into its own narrower child.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000226` was minted locally because METPO has no active exact ToxIN-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1018000` is reserved for this one-row class cohort. The v102 cohort used
`METPO:1017900`, so v103 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v103`, no live record used
`traitmech:000226`, and no prior proposal reserved `METPO:1018000` beyond the
v102 skill note pointing v103 at this block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1018000` | ToxIN system | `METPO:1016800` abortive infection system |

ToxIN system captures genome-level possession of a toxIN type III
toxin-antitoxin abortive-infection locus. It excludes individual `toxI` or
`toxN` genes, ToxI RNA antitoxins, ToxN toxins, type III toxin-antitoxin modules
without direct Abi evidence, AbiQ systems, AbiE systems, source database rows
naming one Abi locus, generic toxin-antitoxin systems, and the broader
abortive infection system.

## External Mappings

No exact external mapping is proposed. Individual `toxI` or `toxN` genes, ToxI
RNA antitoxins, ToxN toxins, source database rows, generic toxin-antitoxin
modules, and broader abortive-infection records are shifted from this
organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with no
  exact ToxIN-system synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000226` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000226` as traceability during the migration.

## Change Log

- v103, 2026-09: lifts `traitmech:000226 ToxIN system` into the
  `METPO:1018000` block.
