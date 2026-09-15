# METPO ROBOT Template Proposal - Gabija System (v92, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v91 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the Gabija system, the
genome-level possession trait for Gabija GajA/GajB antiphage defenses. The v86
cohort proposed a `phage defense system` parent, v87 through v91 proposed BREX,
DISARM, CBASS, phosphorothioate, and abortive-infection children, and this
cohort adds Gabija as a parallel narrower phage-defense child.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000215` was minted locally because METPO has no active exact Gabija-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1016900` is reserved for this one-row class cohort. The v91 cohort used
`METPO:1016800`, so v92 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v92`, no live record used
`traitmech:000215`, and no prior proposal reserved `METPO:1016900`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1016900` | Gabija system | `METPO:1016300` phage defense system |

Gabija system captures genome-level possession of a Gabija antiphage locus
encoding the GajA and GajB proteins that assemble into a GajAB complex and
inhibit bacteriophage replication. It excludes individual `gajA` or `gajB`
genes, GajA or GajB proteins, the GajAB protein complex, source database rows
naming one Gabija locus, phage-encoded anti-Gabija inhibitors such as Gad1,
mechanistic nucleotide-depletion or DNA-cleavage subactivities, and other
antiphage systems such as BREX, DISARM, CBASS, phosphorothioate defense,
CRISPR-Cas, and abortive-infection families.

## External Mappings

No exact external mapping is proposed. GajA/GajB gene, protein, and protein
complex accessions are shifted from this organism-level GENOMICS possession
trait; nucleotide-depletion and DNA-cleavage processes are mechanistic parts
rather than equivalent classes.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with two
  exact Gabija spelling variants and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000215` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000215` as traceability during the migration.

## Change Log

- v92, 2026-09: lifts `traitmech:000215 Gabija system` into the
  `METPO:1016900` block.
