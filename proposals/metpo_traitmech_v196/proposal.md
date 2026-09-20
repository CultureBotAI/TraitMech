# METPO ROBOT Template Proposal - AbiB System (v196, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v195 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for AbiB system, the
genome-level possession trait for an `abiB` abortive-infection locus.
Parreira et al. showed that the abortive-infection determinant AbiB blocks
growth of sensitive bIL170 phage on Lactococcus lactis IL1403, promotes rapid
degradation of sensitive phage transcripts 10 to 15 minutes after infection,
and probably arrests sensitive phage development by that transcript decay.
DefenseFinder models AbiB with one required `AbiB__AbiB` profile.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for AbiB |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1027300` is reserved for this one-row class cohort. The v195 cohort used
`METPO:1027200`, so v196 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository, plus the pinned DefenseFinder registries used for candidate
discovery. AbiB occurred only in neighboring Rhea, Kamadhenu, Rugutis, and
Audmula evidence snippets as a same-source comparator, not as an AbiB record or
proposal; no exact same-scope record, `abib_system` slug, `AbiB system` label,
`AbiB__AbiB` model row, `traitmech:000319`, `metpo_traitmech_v196`,
`METPO:1027300`, `DOI:10.1046/j.1365-2958.1996.371896.x`, or `PMID:8825768`
was present before this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1027300` | AbiB system | `METPO:1016800` abortive infection system |

AbiB system captures genome-level possession of an `abiB` locus represented by
DefenseFinder's `AbiB__AbiB` HMM profile and exemplified by the lactococcal
IL1403 determinant that prevents growth of sensitive phage bIL170. It excludes
the individual `abiB` gene; AbiB proteins; phage bIL170 or bIL41 host-range
outcomes; the individual DefenseFinder HMM profile; source database rows naming
one AbiB locus; unresolved AbiB-triggered RNase mechanisms; and other
abortive-infection systems.

## External Mappings

No exact external mapping is proposed. AbiB, the DefenseFinder HMM, individual
phage-resistance outcomes, and downstream phage-transcript decay processes are
shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  related shifted label, no exact synonyms, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000319` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000319` as traceability during the migration.

## Change Log

- v196, 2026-09: lifts `traitmech:000319 AbiB system` into the
  `METPO:1027300` block.
