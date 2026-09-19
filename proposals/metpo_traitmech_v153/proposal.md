# METPO ROBOT Template Proposal - dGTPase System (v153, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v152 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for dGTPase system, the
genome-level possession trait for the bacterial dGTP-depletion anti-phage
defense system. Tal et al. reported that phage-resistance genes encode dGTPase
enzymes that degrade dGTP into phosphate-free deoxy-guanosine, eliminate dGTP
from the nucleotide pool during phage infection, and halt phage replication by
starving the phage of an essential DNA building block. DefenseFinder models
dGTPase as a single-profile system and maps it to that DOI in its article
registry.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000276` was minted locally because METPO has no active exact dGTPase-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1023000` is reserved for this one-row class cohort. The v152 cohort used
`METPO:1022900`, so v153 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v153`, no live record used
`traitmech:000276`, and no prior proposal reserved `METPO:1023000`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1023000` | dGTPase system | `METPO:1016300` phage defense system |

dGTPase system captures genome-level possession of the anti-phage defense
system whose defensive dGTPase enzyme degrades dGTP into phosphate-free
deoxy-guanosine during phage infection. It excludes generic nucleotide
triphosphatases; SAMHD1-family enzymes not shown to define bacterial dGTPase
systems; individual DefenseFinder HMM profiles; source database rows naming the
profile; dGTP-depletion processes; the dCTPdeaminase system; the Gabija
nucleotide-depletion output; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Generic dGTPase enzymes, dGTP depletion
as a process, SAMHD1-family homologs, and the custom DefenseFinder HMM profile
are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with
  one exact dGTPase synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000276` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000276` as traceability during the migration.

## Change Log

- v153, 2026-09: lifts `traitmech:000276 dGTPase system` into the
  `METPO:1023000` block.
