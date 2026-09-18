# METPO ROBOT Template Proposal - Mokosh System (v123, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v122 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the Mokosh system, the
genome-level possession trait for Mokosh phage-defense loci. Millman et al.
reported the discovery of 21 bacterial defense systems that protect against
phages, and DefenseFinder records Mokosh as type I MkoA/MkoB profiles and a
type II MkoC profile assigned to the Millman et al. discovery preprint.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000246` was minted locally because METPO has no active exact Mokosh-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1020000` is reserved for this one-row class cohort. The v122 cohort used
`METPO:1019900`, so v123 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v123`, no live record used
`traitmech:000246`, no exact Mokosh record was live or already proposed, and no
prior proposal reserved `METPO:1020000`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1020000` | Mokosh system | `METPO:1016300` phage defense system |

Mokosh system captures genome-level possession of a Mokosh locus represented by
MkoA/MkoB type I or MkoC type II components that can protect bacteria from
bacteriophage infection. It excludes individual `mkoA`, `mkoB`, and `mkoC`
genes; MkoA, MkoB, and MkoC proteins; DefenseFinder HMM profiles or
source-database rows naming one predicted Mokosh locus; unresolved Mokosh
triggers, enzymatic substrates, and effector outputs; Mokosh type I or type II
subtypes; and other phage-defense systems such as Dazbog, CapRel, DarTG,
Hailong, Hna, Shedu, Hachiman, SPARTA, AVAST, PARIS, RADAR, Pycsar, Retron,
Septu, BREX, DISARM, CBASS, Gabija, Zorya, phosphorothioate defense,
CRISPR-Cas, and abortive-infection families.

## External Mappings

No exact external mapping is proposed. MkoA/MkoB/MkoC component profiles and
DefenseFinder rows are shifted from this organism-level GENOMICS possession
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact Mokosh synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000246` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000246` as traceability during the migration.

## Change Log

- v123, 2026-09: lifts `traitmech:000246 Mokosh system` into the
  `METPO:1020000` block.
