# METPO ROBOT Template Proposal - MspJI System (v387, 2026-10)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for MspJI system, the
genome-level possession trait for an MspJI-family Type IV
modification-dependent restriction locus. Cohen-Karni et al. support MspJI
homologs as C5-modified-cytosine-dependent restriction endonucleases that
cleave at a constant distance from the modified cytosine; Zheng et al. support
MspJI recognition of 5-methylcytosine and 5-hydroxymethylcytosine. The pinned
DefenseFinder article registry maps `MspJI` to the Cohen-Karni et al. DOI,
while the pinned HMM inventory and rules table have no exact MspJI row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for MspJI system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1046400` is reserved for this one-row class cohort. The v386 cohort used
`METPO:1046300`, so v387 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope MspJI record, `mspji_system`
slug, `traitmech:000510`, `METPO:1046400`, `metpo_traitmech_v387`,
Cohen-Karni et al. DOI `10.1073/pnas.1018448108`, Zheng et al. DOI
`10.1093/nar/gkq327`, title `The MspJI family of modification-dependent
restriction endonucleases for epigenetic studies`, or DefenseFinder source key
`MspJI`.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1046400` | MspJI system | `METPO:1045000` type IV modification-dependent restriction system |

MspJI system captures genome-level possession of an MspJI-family Mrr-like Type
IV modification-dependent restriction locus that recognizes methylcytosine- or
hydroxymethylcytosine-modified DNA and cleaves both strands at a fixed
distance from the modified cytosine. It excludes the broader Mrr superfamily,
individual MspJI-family proteins, individual MspJI-family genes, MspJI-family
nuclease activity outside a complete organism-level Type IV anti-phage system,
individual modified-cytosine DNA substrate classes, and the DefenseFinder
`MspJI` source key outside a complete organism-level system.

`traitmech:000510` is a direct local child of `traitmech:000496` type IV
modification-dependent restriction system. This proposal uses `METPO:1045000`,
the v373 placeholder for `traitmech:000496`.

## External Mappings

No exact external mapping is proposed. Individual MspJI-family proteins,
individual MspJI-family genes, the broader Mrr superfamily, specific
modified-cytosine DNA target classes, and the DefenseFinder article-registry
key are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000510` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000510` as traceability during the migration.

## Change Log

- v387, 2026-10: lifts `traitmech:000510 MspJI system` into the
  `METPO:1046400` placeholder block.
