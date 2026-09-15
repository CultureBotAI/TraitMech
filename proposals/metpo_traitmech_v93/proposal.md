# METPO ROBOT Template Proposal - Thoeris System (v93, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v92 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the Thoeris system, the
genome-level possession trait for Thoeris TIR/ThsA antiphage defenses. The v86
cohort proposed a `phage defense system` parent, v87 through v92 proposed BREX,
DISARM, CBASS, phosphorothioate, abortive-infection, and Gabija children, and
this cohort adds Thoeris as a parallel narrower phage-defense child.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000216` was minted locally because METPO has no active exact Thoeris-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1017000` is reserved for this one-row class cohort. The v92 cohort used
`METPO:1016900`, so v93 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v93`, no live record used
`traitmech:000216`, and no prior proposal reserved `METPO:1017000`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1017000` | Thoeris system | `METPO:1016300` phage defense system |

Thoeris system captures genome-level possession of a Thoeris antiphage locus
encoding a ThsA NADase effector and one or more TIR-domain sensor proteins
that produce a cyclic-ADP-ribose-like signal during phage infection to activate
NAD depletion and inhibit bacteriophage replication. It excludes individual
`thsA` or `thsB` genes, ThsA effector proteins, ThsB and other Thoeris
TIR-domain proteins, cyclic-ADP-ribose isomers as small molecules, source
database rows naming one Thoeris locus, phage-encoded anti-Thoeris inhibitors,
mechanistic NADase or TIR-signalling subactivities, and other antiphage systems
such as BREX, DISARM, CBASS, Gabija, phosphorothioate defense, CRISPR-Cas, and
abortive-infection families.

## External Mappings

No exact external mapping is proposed. Thoeris gene, protein, TIR-domain, and
small-molecule-signal accessions are shifted from this organism-level GENOMICS
possession trait; TIR-domain signalling and NAD depletion are mechanistic parts
rather than equivalent classes.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with two
  exact Thoeris spelling variants and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000216` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000216` as traceability during the migration.

## Change Log

- v93, 2026-09: lifts `traitmech:000216 Thoeris system` into the
  `METPO:1017000` block.
