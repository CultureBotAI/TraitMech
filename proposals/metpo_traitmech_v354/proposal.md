# METPO ROBOT Template Proposal - ARMADA System (v354, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for ARMADA system, the
genome-level possession trait for the YprA-like-helicase phage-defense loci
described by Bell et al. The final article defines ARMADA as a broad
disARM-related antiviral defense array class with Type I and Type II subclades,
the full-text preprint links experimentally tested ARMADA Type II loci from
`E. coli` NCTC 12900 and ATCC 8739 to broad phage protection, and the pinned
DefenseFinder article registry maps Armada to the Bell et al. preprint. The
pinned DefenseFinder HMM inventory and rules table checked in this curation
pass have no Armada or ARMADA rows.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for ARMADA system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1043100` is reserved for this one-row class cohort. The v353 cohort used
`METPO:1043000`, so v354 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus, excluding only `.git`. It found no exact same-scope ARMADA
TraitMech, METPO, history, or prior proposal record; no `armada_system` slug;
no final `DOI:10.1016/j.chom.2026.05.015`, `PMID:42276072`, or preprint
`10.1101/2025.09.15.676423` mention; no `traitmech:000477`; no
`metpo_traitmech_v354`; and no `METPO:1043100` proposal block.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1043100` | ARMADA system | `METPO:1016300` phage defense system |

ARMADA system captures genome-level possession of a YprA-like-helicase locus in
the ARMADA clade. It excludes individual ArmA, ArmB, ArmC, and ArmD proteins;
the broader YprA helicase family; ARMADA Type I and Type II as narrower
subtypes; the `E. coli` NCTC 12900 and ATCC 8739 locus instances; the pinned
DefenseFinder article-registry row; absent pinned DefenseFinder HMM-profile
rows; the absent pinned DefenseFinder rule row; exact PADLOC custom model
boundaries; direct phage triggers or effector outputs; SPIDER mobile elements;
co-encoded Druantia and Zorya systems; and other phage-defense systems.

`traitmech:000477` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `ARMADA`, exact `Armada`, and exact
  `disARM-related antiviral defense array` synonyms.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000477` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000477` as traceability during the migration.

## Change Log

- v354, 2026-09: lifts `traitmech:000477 ARMADA system` into the
  `METPO:1043100` placeholder block.
