# METPO ROBOT Template Proposal - DS-42 System (v341, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-42 system, the
genome-level possession trait for the three-gene DefensePredictor-discovered
anti-phage locus from DeWeirdt et al.'s machine-learning search. DeWeirdt et
al. mapped the working identifier `PRO1` to DS-42, marked the cloned
transcriptional unit as defensive, and measured reduced Bas1 bacteriophage
plaquing. The final Science Table S8 maps `PRO1` to the replicated DS-42
display name and reports high-probability MBL hydrolase and
moderate-probability CHS5_N/Dimerization HHpred rows for two PRO1 products.
The pinned DefenseFinder article registry maps DS-42 to the DefensePredictor
preprint, the pinned DefenseFinder HMM inventory records three DS-42 custom
profiles, `DS-42__DS-42A`, `DS-42__DS-42B`, and `DS-42__DS-42C`, and the
pinned DefenseFinder rules table checked in this curation pass has no DS-42
row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-42 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1041800` is reserved for this one-row class cohort. The v340 cohort
used `METPO:1041700`, so v341 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-42 TraitMech, METPO, history,
or prior proposal record, no `DS-42__DS-42A`, `DS-42__DS-42B`, or
`DS-42__DS-42C` profile-key mention, no `WP_001198055.1`,
`WP_001024069.1`, or `WP_249925928.1` product-accession mention, no
`ds_42_system` slug, no `traitmech:000464`, no `metpo_traitmech_v341`, and no
`METPO:1041800` proposal block. It found `NZ_QOXO01000016.1` and
`GCF_003334005.1` only on the same contig and assembly as the separate DS-35
system locus.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1041800` | DS-42 system | `METPO:1016300` phage defense system |

DS-42 system captures genome-level possession of the three-gene
DefensePredictor-discovered phage-defense transcriptional unit cataloged as
PRO1 and represented by three DefenseFinder DS-42 custom HMM-profile rows. It
excludes the PRO1 source working identifier, individual DS-42 genes and
proteins, the DS-42A through DS-42C HMM profile rows,
cloned-transcriptional-unit plaquing assays, the MBL hydrolase and CHS5_N
HHpred-domain annotations, the absent DS-42 rule-level DefenseFinder model,
unresolved DS-42 component activity and phage readouts, and other
DefensePredictor-discovered or phage-defense systems.

`traitmech:000464` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `PRO1` is kept as a related synonym
because it names the source working identifier, and `DS-42__DS-42A`,
`DS-42__DS-42B`, and `DS-42__DS-42C` are kept as related synonyms because
they name DefenseFinder profile keys rather than the genome-level possession
trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-42` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000464` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000464` as traceability during the migration.

## Change Log

- v341, 2026-09: lifts `traitmech:000464 DS-42 system` into the
  `METPO:1041800` placeholder block.
