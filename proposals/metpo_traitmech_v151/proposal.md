# METPO ROBOT Template Proposal - dCTPdeaminase System (v151, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v150 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for dCTPdeaminase system,
the genome-level possession trait for the bacterial dCTP-depletion anti-phage
defense system. Bernier et al. reported that defensive dCTP deaminase proteins
convert dCTP into deoxy-uracil nucleotides in response to phage infection,
deplete dCTP from the nucleotide pool, and halt phage replication by starving
the phage of an essential DNA building block. DefenseFinder models
dCTPdeaminase as a single-profile system and maps it to that DOI in its article
registry.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000274` was minted locally because METPO has no active exact dCTPdeaminase-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1022800` is reserved for this one-row class cohort. The v150 cohort used
`METPO:1022700`, so v151 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v151`, no live record used
`traitmech:000274`, and no prior proposal reserved `METPO:1022800`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1022800` | dCTPdeaminase system | `METPO:1016300` phage defense system |

dCTPdeaminase system captures genome-level possession of the anti-phage defense
system whose defensive dCTP deaminase protein converts dCTP into deoxy-uracil
nucleotides during phage infection. It excludes generic dCTP deaminase enzymes;
dcd or dCMP deaminase genes; individual DefenseFinder HMM profiles; source
database rows naming the profile; deoxy-uracil nucleotide products; nucleotide-
depletion processes; the dGTPase system; the Gabija nucleotide-depletion output;
and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Generic dCTP deaminase enzymes,
deoxy-uracil nucleotide products, dCTP depletion as a process, and the custom
DefenseFinder HMM profile are shifted from this organism-level GENOMICS
possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with
  no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000274` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000274` as traceability during the migration.

## Change Log

- v151, 2026-09: lifts `traitmech:000274 dCTPdeaminase system` into the
  `METPO:1022800` block.
