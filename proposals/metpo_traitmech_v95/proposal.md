# METPO ROBOT Template Proposal - Wadjet System (v95, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v94 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the Wadjet system, the
genome-level possession trait for Wadjet-family JetABCD, MksBEFG, and EptABCD
SMC systems that restrict circular plasmids by DNA cleavage. The v86 cohort
proposed `phage defense system`, v87 through v94 proposed phage-defense
children, and this cohort adds a plasmid-restriction SMC system as a parallel
GENOMICS trait under `quality`.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000218` was minted locally because METPO has no active exact Wadjet-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1017200` is reserved for this one-row class cohort. The v94 cohort used
`METPO:1017100`, so v95 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v95`, no live record used
`traitmech:000218`, and no prior proposal reserved `METPO:1017200`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1017200` | Wadjet system | `METPO:1000188` quality |

Wadjet system captures genome-level possession of a Wadjet anti-plasmid locus
encoding JetABCD, MksBEFG, EptABCD, or related SMC-family components that
couple plasmid detection to ATPase-dependent DNA cleavage. It excludes
individual `jet`, `mks`, or `ept` genes, JetABCD or MksBEFG protein-complex
activities, PADLOC/DefenseFinder source rows naming one predicted Wadjet locus,
topology-sensing or DNA-cleavage subactivities, other plasmid-defense systems,
plasmid carriage, plasmid-borne anti-restriction systems, CRISPR-Cas,
restriction-modification, and dedicated phage-defense system families.

## External Mappings

No exact external mapping is proposed. Wadjet gene, protein, predicted-domain,
subfamily, PADLOC, and DefenseFinder records are shifted from this
organism-level GENOMICS possession trait, and Wadjet SMC ATPase cycling or
nuclease activity classes are mechanistic parts rather than equivalent classes.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact Wadjet synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000218` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000218` as traceability during the migration.

## Change Log

- v95, 2026-09: lifts `traitmech:000218 Wadjet system` into the
  `METPO:1017200` block.
