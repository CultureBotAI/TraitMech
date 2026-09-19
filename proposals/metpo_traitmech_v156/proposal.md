# METPO ROBOT Template Proposal - DRT System (v156, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v155 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DRT system, the
genome-level possession trait for defense-associated reverse transcriptase
antiphage loci. Gao et al. discovered that several uncharacterized
reverse-transcriptase candidates protect bacteria from dsDNA phages, named those
genes defense-associated RTs, and showed that conserved RT active-site residues
are required for activity. DefenseFinder models DRT as a group of DRT_1 through
DRT9 subtype models.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000279` was minted locally because METPO has no active exact DRT-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1023300` is reserved for this one-row class cohort. The v155 cohort used
`METPO:1023200`, so v156 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v156`, no live record used
`traitmech:000279`, and no prior proposal reserved `METPO:1023300`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1023300` | DRT system | `METPO:1016300` phage defense system |

DRT system captures genome-level possession of a defense-associated reverse
transcriptase locus whose RT-domain component or components can confer
bacteriophage defense and that DefenseFinder represents as a DRT subtype. It
excludes individual `drt` genes; DRT proteins; generic reverse transcriptases;
reverse-transcriptase active-site motifs; DRT_1 through DRT9 HMM profiles;
standalone nitrilase or membrane-protein partners; unresolved DRT-associated
non-coding RNAs; predicted source-database rows naming one DRT component; the
separate Retron and AbiK families; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Defense-associated RT genes, DRT
proteins, DRT-associated non-coding RNAs, reverse-transcriptase catalytic
activity, nitrilase activity, DefenseFinder HMM profiles, and unresolved DRT
antiviral outputs are shifted from this organism-level GENOMICS possession
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  exact DRT synonym, two related gene/protein-family labels, and no exact
  external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000279` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000279` as traceability during the migration.

## Change Log

- v156, 2026-09: lifts `traitmech:000279 DRT system` into the
  `METPO:1023300` block.
