# METPO ROBOT Template Proposal - DISARM System (v88, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v87 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for a DISARM system, the
genome-level possession trait for Defense Island System Associated with
Restriction-Modification loci that pair DNA methyltransferase activity with
DrmAB-mediated recognition of invading phage DNA. The v86 cohort proposed a
`phage defense system` parent, v87 proposed its BREX child, and this cohort
adds DISARM as a parallel narrower phage-defense child.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000211` was minted locally because METPO has no active exact DISARM-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1016500` is reserved for this one-row class cohort. The v87 cohort used
`METPO:1016400`, so v88 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v88`, no live record used
`traitmech:000211`, and no prior proposal reserved `METPO:1016500`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1016500` | DISARM system | `METPO:1016300` phage defense system |

DISARM system captures genome-level possession of a
methyltransferase-associated antiphage locus whose DrmAB core responds to
invading phage DNA. It excludes the individual `drmA`, `drmB`, `drmC`,
`drmD`, `drmE`, `drmMI`, and `drmMII` genes and proteins, DUF1998 proteins
outside the DISARM locus context, source database rows that merely identify one
candidate locus, and other antiphage systems such as BREX, CBASS, abortive
infection, and phosphorothioate defense.

## External Mappings

No exact external mapping is proposed. Several Pfam/InterPro families and GO
terms can ground causal graph nodes for DISARM components, but those are
shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with two
  exact synonyms and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000211` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000211` as traceability during the migration.

## Change Log

- v88, 2026-09: lifts `traitmech:000211 DISARM system` into the
  `METPO:1016500` block.
