# METPO ROBOT Template Proposal - DdmDE System (v152, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v151 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DdmDE system, the
genome-level possession trait for the bacterial anti-plasmid defense locus whose
DdmE DNA-guided prokaryotic Argonaute and DdmD helicase-nuclease cooperate to
destroy plasmids. Jaskolska et al. identified DdmDE as a plasmid-defense module
from seventh-pandemic `Vibrio cholerae`, and Bravo et al. resolved how DdmE
target recognition and DdmD loading drive processive plasmid destruction.
DefenseFinder maps the DdmDE system to the Jaskolska et al. DOI in its article
registry and records custom DdmD and DdmE profiles.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000275` was minted locally because METPO has no active exact DdmDE-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1022900` is reserved for this one-row class cohort. The v151 cohort used
`METPO:1022800`, so v152 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v152`, no live record used
`traitmech:000275`, and no prior proposal reserved `METPO:1022900`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1022900` | DdmDE system | `METPO:1000188` quality |

DdmDE system captures genome-level possession of a DdmDE anti-plasmid locus
encoding the DNA-guided pAgo DdmE and helicase-nuclease DdmD. It excludes
individual `ddmD` or `ddmE` genes; DdmD or DdmE proteins; DdmDE guide-target
complexes; generic prokaryotic Argonautes; the cooperating DdmABC plasmid-
defense module; plasmid carriage; Wadjet; SPARTA; DefenseFinder HMM profiles;
source database rows naming the DdmDE profile; and dedicated phage-defense-
system families.

## External Mappings

No exact external mapping is proposed. DdmD, DdmE, DdmDE guide-target
complexes, pAgo-family activities, DefenseFinder profiles, and plasmid-
clearance processes are shifted from this organism-level GENOMICS possession
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with
  one exact DdmDE synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000275` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000275` as traceability during the migration.

## Change Log

- v152, 2026-09: lifts `traitmech:000275 DdmDE system` into the
  `METPO:1022900` block.
