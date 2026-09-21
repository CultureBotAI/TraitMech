# METPO ROBOT Template Proposal - CmdTAC System (v212, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v211 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for CmdTAC system, the
genome-level possession trait for a toxin-antitoxin-chaperone
abortive-infection locus. Goesswein et al. characterize CmdTAC as an
anti-phage defense system in which CmdC senses viral capsid proteins, CmdA is
degraded, and the liberated CmdT ADP-ribosyltransferase modifies mRNA to block
translation and abort phage infection. The pinned DefenseFinder article
registry maps CmdTAC to that Nature paper; the pinned DefenseFinder HMM
inventory and rules table do not yet list CmdTAC.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for CmdTAC |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1028900` is reserved for this one-row class cohort. The v211 cohort used
`METPO:1028800`, so v212 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository, plus the pinned DefenseFinder article registry that supplied
the positive CmdTAC row used for candidate discovery. No exact same-scope
TraitMech or METPO record, `cmdtac_system` slug, `CmdTAC system` label,
`traitmech:000335`, `metpo_traitmech_v212`, `METPO:1028900`, `CmdTAC`,
`cmdTAC`, `DOI:10.1038/s41586-024-08102-8`, or
`https://pmc.ncbi.nlm.nih.gov/articles/PMC11618068/` was present before this
cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1028900` | CmdTAC system | `METPO:1016800` abortive infection system |

CmdTAC system captures genome-level possession of a cmdTAC
toxin-antitoxin-chaperone locus. It excludes individual `cmdT`, `cmdA`, or
`cmdC` genes; individual CmdT, CmdA, or CmdC proteins; CmdT mRNA
ADP-ribosyltransferase activity; CmdC viral-capsid sensing; CmdA degradation;
Tevenvirinae phage restriction as an outcome; source database rows naming a
CmdTAC system; and other abortive-infection or phage-defense systems.

## External Mappings

No exact external mapping is proposed. CmdT, CmdA, CmdC, CmdT mRNA
ADP-ribosyltransferase activity, CmdC viral-capsid sensing, CmdA degradation,
and Tevenvirinae phage restriction are shifted from this organism-level
GENOMICS possession trait. `cmdTAC toxin-antitoxin-chaperone locus` is kept as
a related synonym because the locus label denotes the genomic determinant, not
the organism-level possession trait itself.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with two
  exact synonyms, one related locus synonym, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000335` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000335` as traceability during the migration.

## Change Log

- v212, 2026-09: lifts `traitmech:000335 CmdTAC system` into the
  `METPO:1028900` block.
