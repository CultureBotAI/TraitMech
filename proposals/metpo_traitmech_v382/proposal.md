# METPO ROBOT Template Proposal - McrBC System (v382, 2026-10)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for McrBC system, the
genome-level possession trait for the mcrBC type IV modification-dependent
restriction system whose McrB and McrC subunits assemble into a restriction
endonuclease complex targeting methylated cytosine-containing DNA. Panne et al.
support McrBC from Escherichia coli K-12 as a restriction enzyme that cuts DNA
containing modified cytosines and uses McrB for DNA binding while McrC is
essential for DNA cleavage. Loenen and Raleigh place mcrBC in the
modified-cytosine restriction branch that helped define the Type IV class.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for McrBC system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1045900` is reserved for this one-row class cohort. The v381 cohort used
`METPO:1045800`, so v382 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope McrBC system record,
`mcrbc_system` slug, `traitmech:000505`, `METPO:1045900`, or
`metpo_traitmech_v382`; it also found no prior local use of the Panne DOI
`10.1093/emboj/20.12.3210` or PMID `11406597`.

Subset tag: `metpo_traitmech_2026_10`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1045900` | McrBC system | `METPO:1045000` type IV modification-dependent restriction system |

McrBC system captures genome-level possession of an mcrBC Type IV
modification-dependent restriction locus encoding McrB DNA-binding and McrC
cleavage-associated subunits that assemble into a restriction endonuclease complex
targeting methylated cytosine-containing DNA. It excludes individual McrB or
McrC proteins, the mcrBC locus outside a complete organism-level McrBC system,
McrA, GmrSD, MspJI, PvuRts1I, EcoKMcrA, ScoMcrA, TagI, VcaM4I, broad
`RM_Type_IV` and `Other_Type_IV` source keys, generic modified-cytosine
restriction, and individual methylated-cytosine DNA substrate classes.

`traitmech:000505` is a direct local child of `traitmech:000496` type IV
modification-dependent restriction system. This proposal uses `METPO:1045000`,
the v373 placeholder for `traitmech:000496`.

## External Mappings

No exact external mapping is proposed. Individual McrB and McrC proteins,
individual mcrBC loci, Escherichia coli strains, methylated DNA substrates, and
the DefenseFinder article-registry key are shifted from this organism-level
GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one class.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000505` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000505` as traceability during the migration.

## Change Log

- v382, 2026-10: lifts `traitmech:000505 McrBC system` into the
  `METPO:1045900` placeholder block.
