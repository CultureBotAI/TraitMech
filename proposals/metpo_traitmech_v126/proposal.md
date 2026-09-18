# METPO ROBOT Template Proposal - Borvo System (v126, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v125 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the Borvo system, the
genome-level possession trait for Borvo phage-defense loci. Millman et al.
reported the discovery of 21 bacterial defense systems that protect against
phages, and DefenseFinder records Borvo as a BovA system assigned to the
Millman et al. discovery preprint.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000249` was minted locally because METPO has no active exact Borvo-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1020300` is reserved for this one-row class cohort. The v125 cohort used
`METPO:1020200`, so v126 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the source tree,
excluding `.git`, ignored dependency caches, and generated Python bytecode. No
prior proposal reserved `metpo_traitmech_v126`, no live record used
`traitmech:000249`, no exact Borvo record was live or already proposed, and no
prior proposal reserved `METPO:1020300`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1020300` | Borvo system | `METPO:1016300` phage defense system |

Borvo system captures genome-level possession of a Borvo locus represented by
BovA profiles that can protect bacteria from bacteriophage infection. It
excludes individual `bovA` genes; BovA proteins; DefenseFinder HMM profiles or
source-database rows naming one predicted Borvo locus; unresolved Borvo
triggers, enzymatic substrates, and effector outputs; and other phage-defense
systems such as Aditi, Bunzi, Dazbog, Mokosh, CapRel, DarTG, Hailong, Hna,
Shedu, Hachiman, SPARTA, AVAST, PARIS, RADAR, Pycsar, Retron, Septu, BREX,
DISARM, CBASS, Gabija, Zorya, phosphorothioate defense, CRISPR-Cas, and
abortive-infection families.

## External Mappings

No exact external mapping is proposed. BovA component profiles and DefenseFinder
rows are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact Borvo synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000249` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000249` as traceability during the migration.

## Change Log

- v126, 2026-09: lifts `traitmech:000249 Borvo system` into the
  `METPO:1020300` block.
