# METPO ROBOT Template Proposal - CapRel System (v121, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v120 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the CapRel system, the
genome-level possession trait for fused toxSAS toxin-antitoxin phage-defense
loci. Zhang et al. showed that CapRelSJ46 protects *Escherichia coli* against
diverse phages, and directly connected characterized CapRelSJ46 triggers to
relief of N-terminal toxSAS-domain autoinhibition, tRNA
pyrophosphorylation, and translation blockade.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000244` was minted locally because METPO has no active exact CapRel-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1019800` is reserved for this one-row class cohort. The v120 cohort used
`METPO:1019700`, so v121 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v121`, no live record used
`traitmech:000244`, and no prior proposal reserved `METPO:1019800`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1019800` | CapRel system | `METPO:1016300` phage defense system |

CapRel system captures genome-level possession of a fused CapRel
toxin-antitoxin locus encoding an N-terminal toxSAS toxin domain and a
C-terminal antitoxin sensor domain that together can restrict bacteriophage
propagation. It
excludes individual `capRel` genes; standalone CapRel proteins, toxSAS domains,
and C-terminal antitoxin domains; phage trigger proteins such as major capsid
protein or Gp54; tRNA pyrophosphorylation, translation blockade, or phage
escape as process-level activities; DefenseFinder/PADLOC rows naming one
predicted locus; generic toxin-antitoxin systems; and other phage-defense
systems such as DarTG, Hailong, Hna, Shedu, Hachiman, SPARTA, AVAST, PARIS,
RADAR, Pycsar, Retron, Septu, BREX, DISARM, CBASS, Gabija, Zorya,
phosphorothioate defense, CRISPR-Cas, and abortive-infection families.

## External Mappings

No exact external mapping is proposed. CapRel proteins, toxSAS domains,
antitoxin sensor domains, phage trigger proteins, tRNA pyrophosphorylation,
translation blockade, abortive-infection cell death, and locus prediction rows
are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with two
  exact CapRel synonyms and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000244` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000244` as traceability during the migration.

## Change Log

- v121, 2026-09: lifts `traitmech:000244 CapRel system` into the
  `METPO:1019800` block.
