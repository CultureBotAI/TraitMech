# METPO ROBOT Template Proposal - PvuRts1I System (v388, 2026-10)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for PvuRts1I system, the
genome-level possession trait for a PvuRts1I-family Type IV
modification-dependent restriction locus. Wang et al. support PvuRts1I as the
founding member of a family of modification-dependent restriction
endonucleases that recognize 5-hydroxymethylcytosine or
5-glucosylhydroxymethylcytosine in double-stranded DNA and cleave both strands
at a defined offset from the modified cytosine. The pinned DefenseFinder
article registry maps `PvuRts1I` to the Wang et al. DOI, while the pinned HMM
inventory and rules table have no exact PvuRts1I row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for PvuRts1I system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1046500` is reserved for this one-row class cohort. The v387 cohort used
`METPO:1046400`, so v388 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope PvuRts1I record,
`pvurts1i_system` slug, `traitmech:000511`, `METPO:1046500`,
`metpo_traitmech_v388`, Wang et al. DOI `10.1093/nar/gkr607`, title
`Comparative characterization of the PvuRts1I family of restriction enzymes
and their application in mapping genomic 5-hydroxymethylcytosine`, or
DefenseFinder source key `PvuRts1I`.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1046500` | PvuRts1I system | `METPO:1045000` type IV modification-dependent restriction system |

PvuRts1I system captures genome-level possession of a PvuRts1I-family Type IV
modification-dependent restriction locus that recognizes 5hmC- or
5ghmC-modified double-stranded DNA and cleaves both strands on the 3'-side
away from the recognized modified cytosine. It excludes individual PvuRts1I-family
proteins, individual PvuRts1I-family genes, PvuRts1I-family nuclease activity
outside a complete organism-level Type IV anti-phage system, individual
5-hydroxymethylcytosine or 5-glucosylhydroxymethylcytosine DNA substrate
classes, and the DefenseFinder `PvuRts1I` source key outside a complete
organism-level system.

`traitmech:000511` is a direct local child of `traitmech:000496` type IV
modification-dependent restriction system. This proposal uses `METPO:1045000`,
the v373 placeholder for `traitmech:000496`.

## External Mappings

No exact external mapping is proposed. Individual PvuRts1I-family proteins,
individual PvuRts1I-family genes, specific 5hmC or 5ghmC DNA target classes,
and the DefenseFinder article-registry key are shifted from this
organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000511` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000511` as traceability during the migration.

## Change Log

- v388, 2026-10: lifts `traitmech:000511 PvuRts1I system` into the
  `METPO:1046500` placeholder block.
