# METPO ROBOT Template Proposal - NLR-like bNACHT System (v285, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v284 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for NLR-like bNACHT
system, the genome-level possession trait for bacterial NACHT-module
phage-defense loci described by Ofir et al. These loci encode STAND-family
NACHT proteins related to eukaryotic NLR proteins; bNACHT01 from Klebsiella
pneumoniae MGH 35 protected a heterologous Escherichia coli host against
phages T4, T5, and T6, and Ofir et al. observed robust antiphage activity
across multiple bacterial NACHT proteins.

The pinned DefenseFinder commit maps its broad `NLR` family key to the Ofir
et al. preprint, records `NLR_like_bNACHT01` and `NLR_like_bNACHT09` profile
names in its HMM inventory, and models both as single-profile subsystems in
its rules table.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for NLR-like bNACHT system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1036200` is reserved for this one-row class cohort. The v284 cohort
used `METPO:1036100`, so v285 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope NLR-like bNACHT system record,
`bNACHT` label, `NLR_like_bNACHT01` or `NLR_like_bNACHT09` profile, Ofir
Cell or bioRxiv DOI, `traitmech:000408`, `metpo_traitmech_v285`, or
`METPO:1036200`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1036200` | NLR-like bNACHT system | `METPO:1016300` phage defense system |

NLR-like bNACHT system captures genome-level possession of a bacterial
NACHT-module phage-defense locus represented by DefenseFinder as
`NLR_like_bNACHT01` or `NLR_like_bNACHT09`. It excludes animal NLRs,
individual bacterial NACHT genes or proteins, source database rows naming the
broad `NLR` family or one profile, the CARD-NLR model namespace, the P4-like
Rst TIR-NLR locus, bNACHT mutation phenotypes, NACHT signaling as a standalone
mechanism, and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Eukaryotic NLRs, individual bacterial
NACHT proteins, NACHT domains, specific profile rows, and CARD-NLR or Rst
TIR-NLR loci are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  DefenseFinder source labels as related synonyms.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000408` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000408` as traceability during the migration.

## Change Log

- v285, 2026-09: lifts `traitmech:000408 NLR-like bNACHT system` into the
  `METPO:1036200` block.
