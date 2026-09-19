# METPO ROBOT Template Proposal - Dpd System (v155, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v154 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Dpd system, the
genome-level possession trait for a 7-deazaguanine DNA-modification defense
locus. Thiaville et al. named the `dpdA-K` cluster for 7-deazapurine in DNA,
supported its recurrent bacterial DNA-modification activity, and reported
transformation-efficiency evidence suggesting a restriction-modification role.
DefenseFinder models Dpd as a multi-profile system with DpdA-K and optional
FolE/QueC/QueD/QueE profiles.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000278` was minted locally because METPO has no active exact Dpd-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1023200` is reserved for this one-row class cohort. The v154 cohort used
`METPO:1023100`, so v155 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v155`, no live record used
`traitmech:000278`, and no prior proposal reserved `METPO:1023200`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1023200` | Dpd system | `METPO:1016300` phage defense system |

Dpd system captures genome-level possession of a Dpd genomic island whose
`dpdA-K` genes install 7-deazaguanine derivatives into DNA and that
DefenseFinder represents as a multi-profile Dpd model. It excludes individual
`dpdA-K` genes; Dpd proteins; FolE, QueC, QueD, and QueE proteins; generic
7-deazaguanine or preQ0 biosynthesis activities; DefenseFinder HMM profiles;
predicted source-database rows naming one Dpd component; unresolved Dpd
restriction outputs; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. `dpdA-K` genes, Dpd proteins, accessory
profiles, preQ0 derivatives, DefenseFinder HMMs, and unresolved
restriction-modification processes are shifted from this organism-level
GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  exact Dpd synonym, one related locus synonym, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000278` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000278` as traceability during the migration.

## Change Log

- v155, 2026-09: lifts `traitmech:000278 Dpd system` into the
  `METPO:1023200` block.
