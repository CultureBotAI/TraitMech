# METPO ROBOT Template Proposal - Kongming System (v378, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Kongming system, the
genome-level possession trait for a dITP-signaling anti-phage locus that
activates a KomBC NADase effector complex. Zeng et al. describe a bacterial
antiphage system in which phage-triggered dITP immune messengers activate NAD
depletion and death of infected cells, Li et al. connect that pathway to the
named Kongming system and the KomBC effector complex, and the pinned
DefenseFinder article registry maps the `Kongming` source key to the Zeng et al.
Science paper.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Kongming system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1045500` is reserved for this one-row class cohort. The v377 cohort used
`METPO:1045400`, so v378 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files outside
`.git` across the curation corpus. It found no exact same-scope Kongming system
record, `kongming_system` slug, `Kongming` label or synonym,
`traitmech:000501`, `metpo_traitmech_v378`, `METPO:1045500`, Zeng DOI
`10.1126/science.ads6055`, PMID `39977546`, or Li DOI
`10.1038/s41467-026-74710-9`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1045500` | Kongming system | `METPO:1016300` phage defense system |

Kongming system captures genome-level possession of a phage defense system in
which phage-induced dITP signaling can activate a KomBC effector complex and
drive NAD depletion-linked infected-cell death. It excludes system-encoded
adenosine deaminases, phage nucleotide kinases, individual KomB or KomC
proteins, the KomBC effector complex, dITP messengers, NAD depletion or
infected-cell death without a Kongming locus, individual DefenseFinder HMM
profiles, and source database rows naming one system model.

`traitmech:000501` is a direct local child of `traitmech:000209` phage defense
system. This proposal uses `METPO:1016300`, the v86 placeholder for
`traitmech:000209`.

## External Mappings

No exact external mapping is proposed. KomB and KomC proteins, the KomBC
complex, dITP, nucleobase modification-based signaling, NAD depletion, and
infected-cell death are shifted from this organism-level GENOMICS possession
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - ROBOT class template with three exact
  synonyms.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000501` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000501` as traceability during the migration.

## Change Log

- v378, 2026-09: lifts `traitmech:000501 Kongming system` into the
  `METPO:1045500` placeholder block.
