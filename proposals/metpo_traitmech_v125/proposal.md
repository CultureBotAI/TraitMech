# METPO ROBOT Template Proposal - Bunzi System (v125, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v124 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the Bunzi system, the
genome-level possession trait for Bunzi phage-defense loci. Millman et al.
reported the discovery of 21 bacterial defense systems that protect against
phages, and DefenseFinder records Bunzi as a BnzA/BnzB system assigned to the
Millman et al. discovery preprint.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000248` was minted locally because METPO has no active exact Bunzi-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1020200` is reserved for this one-row class cohort. The v124 cohort used
`METPO:1020100`, so v125 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the source tree,
excluding `.git`, ignored dependency caches, and generated Python bytecode. No
prior proposal reserved `metpo_traitmech_v125`, no live record used
`traitmech:000248`, no exact Bunzi record was live or already proposed, and no
prior proposal reserved `METPO:1020200`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1020200` | Bunzi system | `METPO:1016300` phage defense system |

Bunzi system captures genome-level possession of a two-component Bunzi locus
represented by BnzA and BnzB profiles that can protect bacteria from
bacteriophage infection. It excludes individual `bnzA` and `bnzB` genes; BnzA
and BnzB proteins; DefenseFinder HMM profiles or source-database rows naming one
predicted Bunzi locus; unresolved Bunzi triggers, enzymatic substrates, and
effector outputs; and other phage-defense systems such as Aditi, Dazbog, Mokosh,
CapRel, DarTG, Hailong, Hna, Shedu, Hachiman, SPARTA, AVAST, PARIS, RADAR,
Pycsar, Retron, Septu, BREX, DISARM, CBASS, Gabija, Zorya,
phosphorothioate defense, CRISPR-Cas, and abortive-infection families.

## External Mappings

No exact external mapping is proposed. BnzA/BnzB component profiles and
DefenseFinder rows are shifted from this organism-level GENOMICS possession
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact Bunzi synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000248` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000248` as traceability during the migration.

## Change Log

- v125, 2026-09: lifts `traitmech:000248 Bunzi system` into the
  `METPO:1020200` block.
