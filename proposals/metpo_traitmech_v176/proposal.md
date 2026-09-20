# METPO ROBOT Template Proposal - Butters gp57r System (v176, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v175 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Butters gp57r system,
the genome-level possession trait for a Butters gp57r anti-phage locus.
Mohammed et al. support Butters gp57r as necessary and sufficient to inhibit
Island3 and other phages, and DefenseFinder catalogs Butters_gp57r with a gp57r
HMM profile entry plus a one-profile system rule.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Butters gp57r |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1025300` is reserved for this one-row class cohort. The v175 cohort used
`METPO:1025200`, so v176 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v176`, no live record used
`traitmech:000299`, and no prior proposal reserved `METPO:1025300`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1025300` | Butters gp57r system | `METPO:1016300` phage defense system |

Butters gp57r system captures genome-level possession of a Butters gp57r locus
cataloged by DefenseFinder under a Butters_gp57r model namespace with a gp57r
HMM profile entry. It excludes the individual gp57r gene; the Gp57r protein;
the DefenseFinder HMM profile; the Butters prophage as a viral genome;
recombinant Mycobacterium smegmatis strains expressing Butters gene 57r;
clinical Mycobacterium abscessus strains with gp57r orthologs; the HEPN domain;
the RX4-6H motif; PurpleHaze defense-escape minor-tail alleles; the unresolved
post-DNA-injection mechanism; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. The Butters prophage, gp57r gene, Gp57r
protein, DefenseFinder HMM, gp57r orthologs, recombinant gp57r-expressing
strains, candidate HEPN/RX4-6H motifs, PurpleHaze defense-escape alleles, and
unresolved Butters gp57r activation outputs are shifted from this
organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  related DefenseFinder source label and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000299` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000299` as traceability during the migration.

## Change Log

- v176, 2026-09: lifts `traitmech:000299 Butters gp57r system` into the
  `METPO:1025300` block.
