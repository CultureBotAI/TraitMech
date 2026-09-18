# METPO ROBOT Template Proposal - Aditi System (v124, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v123 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the Aditi system, the
genome-level possession trait for Aditi phage-defense loci. Millman et al.
reported the discovery of 21 bacterial defense systems that protect against
phages, and DefenseFinder records Aditi as a DitA/DitB system assigned to the
Millman et al. discovery preprint.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000247` was minted locally because METPO has no active exact Aditi-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1020100` is reserved for this one-row class cohort. The v123 cohort used
`METPO:1020000`, so v124 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v124`, no live record used
`traitmech:000247`, no exact Aditi record was live or already proposed, and no
prior proposal reserved `METPO:1020100`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1020100` | Aditi system | `METPO:1016300` phage defense system |

Aditi system captures genome-level possession of a two-component Aditi locus
represented by DitA and DitB profiles that can protect bacteria from
bacteriophage infection. It excludes individual `ditA` and `ditB` genes; DitA
and DitB proteins; DefenseFinder HMM profiles or source-database rows naming one
predicted Aditi locus; unresolved Aditi triggers, enzymatic substrates, and
effector outputs; and other phage-defense systems such as Dazbog, Mokosh,
CapRel, DarTG, Hailong, Hna, Shedu, Hachiman, SPARTA, AVAST, PARIS, RADAR,
Pycsar, Retron, Septu, BREX, DISARM, CBASS, Gabija, Zorya,
phosphorothioate defense, CRISPR-Cas, and abortive-infection families.

## External Mappings

No exact external mapping is proposed. DitA/DitB component profiles and
DefenseFinder rows are shifted from this organism-level GENOMICS possession
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact Aditi synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000247` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000247` as traceability during the migration.

## Change Log

- v124, 2026-09: lifts `traitmech:000247 Aditi system` into the
  `METPO:1020100` block.
