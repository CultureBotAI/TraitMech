# METPO ROBOT Template Proposal - AbiD System (v195, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v194 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for AbiD system, the
genome-level possession trait for an `abiD` abortive-infection locus.
McLandsborough et al. cloned the pBF61 determinant from Lactococcus lactis
subsp. lactis KR5, showed that it conferred an abortive phage infection
phenotype that reduced plating efficiency, plaque size, and c2 phage burst
size, and verified by Tn5 insertion that the sequenced `abiD` open reading
frame was required for that phenotype. DefenseFinder models AbiD with one
required `AbiD__AbiD` profile.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for AbiD |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1027200` is reserved for this one-row class cohort. The v194 cohort used
`METPO:1027100`, so v195 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository outside `.git`, plus the pinned DefenseFinder registries used
for candidate discovery. AbiD occurred only in neighboring Rhea, Kamadhenu,
Rugutis, and Audmula evidence snippets as a same-source comparator, not as an
AbiD record or proposal; no exact same-scope record, `abid_system` slug,
`AbiD system` label, `AbiD__AbiD` model row, `traitmech:000318`,
`metpo_traitmech_v195`, or `METPO:1027200` was present before this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1027200` | AbiD system | `METPO:1016800` abortive infection system |

AbiD system captures genome-level possession of an `abiD` locus represented by
DefenseFinder's `AbiD__AbiD` HMM profile and exemplified by the lactococcal
pBF61 determinant. It excludes the individual `abiD` gene; AbiD proteins; the
pBF61 plasmid; the individual DefenseFinder HMM profile; source database rows
naming one AbiD locus; individual lactococcal phage host-range outcomes; and
other abortive-infection systems.

## External Mappings

No exact external mapping is proposed. AbiD, pBF61, the DefenseFinder HMM, and
downstream phage-restriction or burst-size phenotypes are shifted from this
organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  related shifted label, no exact synonyms, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000318` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000318` as traceability during the migration.

## Change Log

- v195, 2026-09: lifts `traitmech:000318 AbiD system` into the
  `METPO:1027200` block.
