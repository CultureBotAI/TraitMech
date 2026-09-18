# METPO ROBOT Template Proposal - DarTG System (v120, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v119 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the DarTG system, the
genome-level possession trait for toxin-antitoxin phage-defense loci whose DarT
toxin ADP-ribosylates viral DNA. LeRoux et al. showed that phage infection can
release DarT to modify viral DNA, block phage genome replication, and prevent
mature virion production; Patel and Seed independently showed that a DarTG
element in clinical Vibrio cholerae isolates inhibits the co-circulating lytic
phage ICP1.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000243` was minted locally because METPO has no active exact DarTG-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1019700` is reserved for this one-row class cohort. The v119 cohort used
`METPO:1019600`, so v120 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v120`, no live record used
`traitmech:000243`, and no prior proposal reserved `METPO:1019700`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1019700` | DarTG system | `METPO:1016300` phage defense system |

DarTG system captures genome-level possession of a toxin-antitoxin locus whose
DarT toxin can be released during bacteriophage infection to ADP-ribosylate
viral DNA, block phage genome replication, and prevent production of mature
virions. It excludes individual `darT` and `darG` genes; standalone DarT and
DarG proteins; DarTG1 and DarTG2 subfamilies; DNA ADP-ribosyltransferase
activity without a complete DarTG locus; viral DNA ADP-ribosylation as a
process; ICP1 anti-defense proteins such as AdfB; RB69 gp61.2 anti-DarT
proteins; DefenseFinder/PADLOC rows naming one predicted locus; generic
toxin-antitoxin systems; and other phage-defense systems such as Hailong, Hna,
Shedu, Hachiman, SPARTA, AVAST, PARIS, RADAR, Pycsar, Retron, Septu, BREX,
DISARM, CBASS, Gabija, Zorya, phosphorothioate defense, CRISPR-Cas, and
abortive infection families.

## External Mappings

No exact external mapping is proposed. DarT and DarG proteins, DarT ADP-ribosyl
transferase activity, viral DNA ADP-ribosylation, phage anti-DarT proteins,
DarTG subfamilies, generic toxin-antitoxin systems, and locus prediction rows
are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact DarTG long-form synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000243` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000243` as traceability during the migration.

## Change Log

- v120, 2026-09: lifts `traitmech:000243 DarTG system` into the
  `METPO:1019700` block.
