# METPO ROBOT Template Proposal - CBASS System (v89, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v88 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for a CBASS system, the
genome-level possession trait for cyclic-oligonucleotide-based antiphage
signaling loci that pair an oligonucleotide cyclase with a cyclic
oligonucleotide-activated effector. The v86 cohort proposed a `phage defense
system` parent, v87 proposed its BREX child, v88 proposed its DISARM child, and
this cohort adds CBASS as a parallel narrower phage-defense child.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000212` was minted locally because METPO has no active exact CBASS-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1016600` is reserved for this one-row class cohort. The v88 cohort used
`METPO:1016500`, so v89 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v89`, no live record used
`traitmech:000212`, and no prior proposal reserved `METPO:1016600`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1016600` | CBASS system | `METPO:1016300` phage defense system |

CBASS system captures genome-level possession of a
cyclic-oligonucleotide-based antiphage signaling locus whose oligonucleotide
cyclase generates a cyclic oligonucleotide second messenger after phage
infection. It excludes individual CD-NTase, CapV, SAVED, TIR, HORMA, and JAB
genes or proteins; cGAMP, cAAA, and other cyclic oligonucleotides as chemical
entities; source database rows that merely identify one candidate locus; the
broader cGAS-STING family; and other antiphage systems such as BREX, DISARM,
restriction-modification, CRISPR-Cas, and phosphorothioate defense.

## External Mappings

No exact external mapping is proposed. Several InterPro families and GO terms
can ground causal graph nodes for CBASS components, but those are shifted from
this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with two
  exact synonyms and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000212` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000212` as traceability during the migration.

## Change Log

- v89, 2026-09: lifts `traitmech:000212 CBASS system` into the
  `METPO:1016600` block.
