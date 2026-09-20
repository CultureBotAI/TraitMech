# METPO ROBOT Template Proposal - AbiI System (v193, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v192 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for AbiI system, the
genome-level possession trait for an `abiI` abortive-infection locus. Su et al.
cloned the pND852-derived Lactococcus lactis M138 locus, showed that the
pND817 clone encoded abortive infection and reduced lactococcal phage burst
size, localized the phenotype to a single `abiI` open reading frame, and
DefenseFinder models AbiI with one required `AbiI__AbiI` profile.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for AbiI |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1027000` is reserved for this one-row class cohort. The v192 cohort used
`METPO:1026900`, so v193 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files under
`data/traits`, `history`, `proposals`, `scripts`, the pinned local METPO
snapshot, and the pinned DefenseFinder registries used for candidate discovery.
AbiI occurred only in the pinned DefenseFinder article, rules, and HMM
registries; no exact same-scope record, `abii_system` slug, `traitmech:000316`,
`metpo_traitmech_v193`, or `METPO:1027000` was present before this cohort. A
follow-up ignored-and-hidden whole-repository search outside `.git` and `.venv`,
excluding this AbiI patch set, found no additional same-scope AbiI hits.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1027000` | AbiI system | `METPO:1016800` abortive infection system |

AbiI system captures genome-level possession of a single-ORF `abiI` locus
represented by DefenseFinder's `AbiI__AbiI` HMM profile and exemplified by the
lactococcal pND852/pND817 locus. It excludes the individual `abiI` gene; AbiI
protein; pND852 and pND817 plasmids; the individual DefenseFinder HMM profile;
source database rows naming one AbiI locus; individual lactococcal phage
host-range outcomes; and other abortive-infection systems.

## External Mappings

No exact external mapping is proposed. AbiI, pND852, pND817, the DefenseFinder
HMM, and downstream phage-restriction or burst-size phenotypes are shifted from
this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  related shifted label, no exact synonyms, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000316` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000316` as traceability during the migration.

## Change Log

- v193, 2026-09: lifts `traitmech:000316 AbiI system` into the
  `METPO:1027000` block.
