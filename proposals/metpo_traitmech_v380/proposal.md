# METPO ROBOT Template Proposal - ENDPaCF1 System (v380, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for ENDPaCF1 system, the
genome-level possession trait for a Type IIS restriction endonuclease-like
anti-phage locus with an inactive Endonuclease III sensing domain that can
recognize diverse DNA hypermodifications. Yee et al. describe ENDPaCF1 as the
causal Pseudomonas antiphage system in a defense island whose deletion
sensitizes a clinical isolate to Pbunavirus phages, and the pinned
DefenseFinder article registry maps the `ENDPaCF1` source key to the Yee et al.
bioRxiv preprint.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for ENDPaCF1 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1045700` is reserved for this one-row class cohort. The v379 cohort used
`METPO:1045600`, so v380 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files outside
`.git` and ROBOT outputs across the curation corpus. It found no exact
same-scope ENDPaCF1 system record, `endpacf1_system` slug, `END PaCF1` label or
synonym, `traitmech:000503`, `metpo_traitmech_v380`, `METPO:1045700`, DOI
`10.1101/2025.03.31.646159`, the numeric DOI suffix `646159`, or the Yee
preprint title.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1045700` | ENDPaCF1 system | `METPO:1016300` phage defense system |

ENDPaCF1 system captures genome-level possession of an anti-phage locus
encoding a Type IIS restriction endonuclease-like protein with an inactive
Endonuclease III sensing domain. It excludes individual Type IIS restriction
endonuclease-like proteins, iEndoIII domains, Type IIS
restriction-modification systems with cognate methyltransferases, Type IV
restriction endonuclease systems, hypermodified DNA sensing by itself,
phage-encoded END nuclease inhibitors, individual DefenseFinder HMM profiles,
and source database rows naming one ENDPaCF1 model.

`traitmech:000503` is a direct local child of `traitmech:000209` phage defense
system. This proposal uses `METPO:1016300`, the v86 placeholder for
`traitmech:000209`.

## External Mappings

No exact external mapping is proposed. Type IIS restriction enzymes, inactive
Endonuclease III domains, Type IV restriction endonucleases, hypermodified
phage genomes, Pseudomonas hosts, and END nuclease inhibitors are shifted from
this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with one exact
  synonym.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000503` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000503` as traceability during the migration.

## Change Log

- v380, 2026-09: lifts `traitmech:000503 ENDPaCF1 system` into the
  `METPO:1045700` placeholder block.
