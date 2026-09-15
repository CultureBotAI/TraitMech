# METPO ROBOT Template Proposal - Phosphorothioate Defense System (v90, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v89 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for a phosphorothioate
defense system, the genome-level possession trait for DNA
phosphorothioation-dependent antiphage restriction systems. The v86 cohort
proposed a `phage defense system` parent, v87 proposed its BREX child, v88
proposed its DISARM child, v89 proposed its CBASS child, and this cohort adds
phosphorothioate defense as a parallel narrower phage-defense child.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000213` was minted locally because METPO has no active exact phosphorothioate-defense-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1016700` is reserved for this one-row class cohort. The v89 cohort used
`METPO:1016600`, so v90 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v90`, no live record used
`traitmech:000213`, and no prior proposal reserved `METPO:1016700`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1016700` | phosphorothioate defense system | `METPO:1016300` phage defense system |

Phosphorothioate defense system captures genome-level possession of a DNA
phosphorothioation-dependent restriction locus whose Dnd- or Ssp-family
components couple host DNA phosphorothioate modification to restriction of
invading DNA. It excludes phosphorothioate modifications as chemical entities;
DndABCDE, DndFGH, SspABCD, SspE, SspFGH, and individual `dnd` or `ssp` genes
or proteins; narrower Dnd and Ssp subfamilies; source database rows naming one
PT locus; restriction-modification in general; and other antiphage systems such
as BREX, DISARM, CBASS, CRISPR-Cas, and abortive infection.

## External Mappings

No exact external mapping is proposed. Dnd and Ssp component families may be
groundable as narrower causal graph nodes, but those protein, complex, and
subfamily entities are shifted from this organism-level GENOMICS possession
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with
  PT-related exact synonyms and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000213` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000213` as traceability during the migration.

## Change Log

- v90, 2026-09: lifts `traitmech:000213 phosphorothioate defense system` into
  the `METPO:1016700` block.
