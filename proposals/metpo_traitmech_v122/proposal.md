# METPO ROBOT Template Proposal - Dazbog System (v122, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v121 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the Dazbog system, the
genome-level possession trait for DzbA/DzbB phage-defense loci. Millman et al.
reported the discovery of 21 bacterial defense systems that protect against
phages, and DefenseFinder records Dazbog as a two-component DzbA/DzbB system
assigned to the Millman et al. discovery preprint.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000245` was minted locally because METPO has no active exact Dazbog-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1019900` is reserved for this one-row class cohort. The v121 cohort used
`METPO:1019800`, so v122 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v122`, no live record used
`traitmech:000245`, no exact Dazbog record was live or already proposed, and no
prior proposal reserved `METPO:1019900`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1019900` | Dazbog system | `METPO:1016300` phage defense system |

Dazbog system captures genome-level possession of a two-component Dazbog locus
encoding DzbA and DzbB components that can protect bacteria from bacteriophage
infection. It excludes individual `dzbA` and `dzbB` genes; DzbA and DzbB
proteins; DefenseFinder HMM profiles or source-database rows naming one
predicted Dazbog locus; unresolved Dazbog triggers, enzymatic substrates, and
effector outputs; and other phage-defense systems such as CapRel, DarTG,
Hailong, Hna, Shedu, Hachiman, SPARTA, AVAST, PARIS, RADAR, Pycsar, Retron,
Septu, BREX, DISARM, CBASS, Gabija, Zorya, phosphorothioate defense,
CRISPR-Cas, and abortive-infection families.

## External Mappings

No exact external mapping is proposed. DzbA/DzbB component profiles and
DefenseFinder rows are shifted from this organism-level GENOMICS possession
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact Dazbog synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000245` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000245` as traceability during the migration.

## Change Log

- v122, 2026-09: lifts `traitmech:000245 Dazbog system` into the
  `METPO:1019900` block.
