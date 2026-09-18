# METPO ROBOT Template Proposal - Hailong System (v119, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v118 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the Hailong system, the
genome-level possession trait for NTase-linked Hailong antiphage loci. Tan et
al. showed that Hailong loci encode HalB NTase signal enzymes and HalA membrane
effectors that are gated by HalB-derived oligodeoxyadenylate signals until viral
DNA exonucleases trigger release of the primed HalA complex and protective host
cell growth arrest.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000242` was minted locally because METPO has no active exact Hailong-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1019600` is reserved for this one-row class cohort. The v118 cohort used
`METPO:1019500`, so v119 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v119`, no live record used
`traitmech:000242`, and no prior proposal reserved `METPO:1019600`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1019600` | Hailong system | `METPO:1016300` phage defense system |

Hailong system captures genome-level possession of a locus encoding a HalB NTase
DNA-signal enzyme and a HalA membrane effector complex that can be held inactive
by HalB-derived oligodeoxyadenylate until viral DNA exonucleases release the
primed HalA complex and induce protective host cell growth arrest. It excludes
individual `halA` and `halB` genes; standalone HalA and HalB proteins; NTase
activity; oligodeoxyadenylate synthesis or cleavage without a complete Hailong
locus; HalA ion-channel activity; viral DNA exonucleases and phage escape
mutants; host ODA-processing factors; DefenseFinder/PADLOC rows naming one
predicted locus; and other antiphage systems such as Hna, Shedu, Hachiman,
SPARTA, AVAST, PARIS, RADAR, Pycsar, Retron, Septu, BREX, DISARM, CBASS,
Gabija, Zorya, phosphorothioate defense, CRISPR-Cas, and abortive infection
families.

## External Mappings

No exact external mapping is proposed. HalA and HalB proteins, NTase molecular
functions, oligodeoxyadenylate products, HalA channel activation, viral DNA
exonucleases, host ODA-processing activities, growth arrest, and locus
prediction rows are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact Hailong long-form synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000242` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000242` as traceability during the migration.

## Change Log

- v119, 2026-09: lifts `traitmech:000242 Hailong system` into the
  `METPO:1019600` block.
