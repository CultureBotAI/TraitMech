# METPO ROBOT Template Proposal - AbiQ System (v102, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v101 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the AbiQ system, the
genome-level possession trait for an abortive-infection system in which an
organism possesses an AbiQ type III toxin-antitoxin locus whose protein
endoribonuclease and cognate RNA antitoxin module alter early phage mRNA
profiles and restrict phage propagation after adsorption. The v91 cohort
proposed the broader `abortive infection system` parent for Abi defense
families; this cohort splits AbiQ into its own narrower child.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000225` was minted locally because METPO has no active exact AbiQ-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1017900` is reserved for this one-row class cohort. The v101 cohort used
`METPO:1017800`, so v102 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v102`, no live record used
`traitmech:000225`, and no prior proposal reserved `METPO:1017900` beyond the
v101 skill note pointing v102 at this block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1017900` | AbiQ system | `METPO:1016800` abortive infection system |

AbiQ system captures genome-level possession of an AbiQ type III
toxin-antitoxin abortive-infection locus. It excludes individual `abiQ` genes,
AbiQ proteins, type III toxin-antitoxin modules without direct Abi evidence,
ToxIN systems, AbiE systems, source database rows naming one Abi locus, generic
toxin-antitoxin systems, and the broader abortive infection system.

## External Mappings

No exact external mapping is proposed. Individual `abiQ` genes, AbiQ proteins,
source database rows, generic toxin-antitoxin modules, and broader
abortive-infection records are shifted from this organism-level GENOMICS
possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with no
  exact AbiQ-system synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000225` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000225` as traceability during the migration.

## Change Log

- v102, 2026-09: lifts `traitmech:000225 AbiQ system` into the
  `METPO:1017900` block.
