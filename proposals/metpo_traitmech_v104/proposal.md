# METPO ROBOT Template Proposal - AbiE System (v104, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v103 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the AbiE system, the
genome-level possession trait for an abortive-infection system in which an
organism possesses an `abiE` bicistronic locus whose AbiEii DUF1814-family
bacteriostatic toxin and AbiEi COG5340-family antitoxin constitute a
non-interacting type IV toxin-antitoxin module that supports phage resistance.
The v91 cohort proposed the broader `abortive infection system` parent for Abi
defense families; v102 split AbiQ into its own narrower child; v103 split ToxIN
into its own narrower child; and this cohort splits AbiE into its own narrower
child.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000227` was minted locally because METPO has no active exact AbiE-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1018100` is reserved for this one-row class cohort. The v103 cohort used
`METPO:1018000`, so v104 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v104`, no live record used
`traitmech:000227`, and no prior proposal reserved `METPO:1018100` beyond the
v103 skill note pointing v104 at this block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1018100` | AbiE system | `METPO:1016800` abortive infection system |

AbiE system captures genome-level possession of an `abiE` bicistronic type IV
toxin-antitoxin abortive-infection locus. It excludes individual `abiEi` or
`abiEii` genes, AbiEi antitoxins, AbiEii toxins, DUF1814-COG5340 pairs without
direct Abi evidence, AbiQ systems, ToxIN systems, source database rows naming
one Abi locus, generic toxin-antitoxin systems, and the broader abortive
infection system.

## External Mappings

No exact external mapping is proposed. Individual `abiEi` or `abiEii` genes,
AbiEi antitoxins, AbiEii toxins, DUF1814-COG5340 pairs that have not been
directly shown to act as Abi modules, generic toxin-antitoxin modules, and
broader abortive-infection records are shifted from this organism-level
GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with no
  exact AbiE-system synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000227` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000227` as traceability during the migration.

## Change Log

- v104, 2026-09: lifts `traitmech:000227 AbiE system` into the
  `METPO:1018100` block.
