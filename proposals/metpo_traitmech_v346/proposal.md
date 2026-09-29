# METPO ROBOT Template Proposal - DS-45 System (v346, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-45 system, the
genome-level possession trait for the single-gene DefensePredictor-discovered
anti-phage locus from DeWeirdt et al.'s machine-learning search. DeWeirdt et
al. mapped the working identifier `2971` to DS-45, marked the cloned
transcriptional unit as defensive, and measured smaller Bas50 bacteriophage
plaques plus reduced efficiency of plating. The final Science Table S8 maps
`2971` to the replicated DS-45 display name and records a DUF2971 HHpred-domain
row for the only Table S6 product accession. The pinned DefenseFinder article
registry maps DS-45 to the DefensePredictor preprint, the pinned DefenseFinder
HMM inventory records one DS-45 custom profile, `DS-45__DS-45`, and the pinned
DefenseFinder rules table checked in this curation pass has no DS-45 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-45 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1042300` is reserved for this one-row class cohort. The v345 cohort
used `METPO:1042200`, so v346 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-45 TraitMech, METPO, history,
or prior proposal record, no `DS-45__DS-45` profile-key mention, no
`WP_223151192.1` product-accession mention, no `NZ_QOYQ01000002.1` accession
mention, no `ds_45_system` slug, no `traitmech:000469`, and no `METPO:1042300`
proposal block. It found `2971` only in a DS-29 assay plate-image filename,
not as a same-scope source working identifier.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1042300` | DS-45 system | `METPO:1016300` phage defense system |

DS-45 system captures genome-level possession of the single-gene
DefensePredictor-discovered phage-defense transcriptional unit cataloged as
2971 and represented by one DefenseFinder DS-45 custom HMM-profile row. It
excludes the 2971 source working identifier, the individual DS-45 gene or
protein, the DS-45 HMM profile row, cloned-transcriptional-unit plaquing
assays, the high-probability DUF2971 HHpred-domain annotation, the absent
DS-45 rule-level DefenseFinder model, unresolved DS-45 component activity and
phage readouts, and other DefensePredictor-discovered or phage-defense systems.

`traitmech:000469` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `2971` is kept as a related synonym
because it names the source working identifier, and `DS-45__DS-45` is kept as a
related synonym because it names a DefenseFinder profile key rather than the
genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-45` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000469` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000469` as traceability during the migration.

## Change Log

- v346, 2026-09: lifts `traitmech:000469 DS-45 system` into the
  `METPO:1042300` placeholder block.
