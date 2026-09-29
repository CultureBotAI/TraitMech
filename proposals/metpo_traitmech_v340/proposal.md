# METPO ROBOT Template Proposal - DS-41 System (v340, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-41 system, the
genome-level possession trait for the single-gene
DefensePredictor-discovered anti-phage locus from DeWeirdt et al.'s
machine-learning search. DeWeirdt et al. mapped the working identifier `AAA2`
to DS-41, marked the cloned transcriptional unit as defensive, and measured
reduced Bas1 and T4 bacteriophage plaquing. The final Science Table S8 maps
`AAA2` to the replicated DS-41 display name and reports a high-probability
AAA+ ATPase HHpred row for the AAA2 product. The pinned DefenseFinder article
registry maps DS-41 to the DefensePredictor preprint, the pinned DefenseFinder
HMM inventory records one DS-41 custom profile, `DS-41__DS-41`, and the pinned
DefenseFinder rules table checked in this curation pass has no DS-41 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-41 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1041700` is reserved for this one-row class cohort. The v339 cohort
used `METPO:1041600`, so v340 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-41 TraitMech, METPO, history,
or prior proposal record, no `DS-41__DS-41` profile-key mention, no
`NZ_QOYD01000024.1` contig mention, no `WP_033812887.1` product-accession
mention, no `ds_41_system` slug, no `traitmech:000463`, no
`metpo_traitmech_v340`, and no `METPO:1041700` proposal block. It found `AAA2`
only as a July 17 screen filename fragment in unrelated DS records and
`GCF_003333765.1` only as the assembly accession for the same-assembly but
different DS-16 locus.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1041700` | DS-41 system | `METPO:1016300` phage defense system |

DS-41 system captures genome-level possession of the single-gene
DefensePredictor-discovered phage-defense transcriptional unit cataloged as
AAA2 and represented by one DefenseFinder DS-41 custom HMM-profile row. It
excludes the AAA2 source working identifier, the individual DS-41 gene or
protein, the DS-41 HMM profile row, cloned-transcriptional-unit plaquing
assays, the high-probability AAA+ ATPase HHpred-domain annotation, the absent
DS-41 rule-level DefenseFinder model, unresolved DS-41 component activity and
phage readouts, and other DefensePredictor-discovered or phage-defense
systems.

`traitmech:000463` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `AAA2` is kept as a related synonym
because it names the source working identifier, and `DS-41__DS-41` is kept as a
related synonym because it names a DefenseFinder profile key rather than the
genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-41` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000463` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000463` as traceability during the migration.

## Change Log

- v340, 2026-09: lifts `traitmech:000463 DS-41 system` into the
  `METPO:1041700` placeholder block.
