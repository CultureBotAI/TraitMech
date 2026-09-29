# METPO ROBOT Template Proposal - DS-26 System (v349, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-26 system, the
genome-level possession trait for a single-gene anti-phage locus from DeWeirdt
et al.'s final validation set. DeWeirdt et al. mapped the working identifier
`NERD` to DS-26 in final Science supplementary Table S6, marked the cloned
transcriptional unit as defensive, recorded a DefensePredictor-hit source
screen, and recorded the product accession on contig `NZ_QOXL01000006.1`.
Final Science Table S7 reports strong Bas25 and Bas19 reduced-efficiency-of-
plaquing readouts for NERD, and Table S8 maps NERD to the replicated display
name DS-26 plus a PDDEXK/FokI cleavage-domain HHpred row for `WP_054626965.1`.
The first-pass DefenseFinder review found no exact DS-26 row in the pinned
article, HMM, or rules registries.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-26 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1042600` is reserved for this one-row class cohort. The v348 cohort
used `METPO:1042500`, so v349 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-26 TraitMech, METPO, history,
or prior proposal record, no `ds_26_system` slug, no `traitmech:000472`, and
no `METPO:1042600` proposal block. The working identifier `NERD` appeared only
as an unrelated HEC-02 nuclease-related-domain label or in file names for other
DeWeirdt assay plates that included the NERD clone.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1042600` | DS-26 system | `METPO:1016300` phage defense system |

DS-26 system captures genome-level possession of the single-gene DS-26
phage-defense transcriptional unit cataloged as NERD in final Science Table S6.
It excludes the individual `WP_054626965.1` protein, the DefensePredictor and
HHblits screens that nominated the transcriptional unit, cloned-
transcriptional-unit plaquing assays, specific Bas25/Bas19 phage readouts, the
Table S8 PDDEXK/FokI HHpred-domain row, the unrelated UG34__NERD_Helicase
DefenseFinder profile, HEC-02's nuclease-related-domain wording, unresolved
DefenseFinder model coverage, and other DS systems.

`traitmech:000472` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `NERD` is kept as a related synonym
because it names the source working transcriptional-unit identifier rather than
the genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-26` synonym and the related source key.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000472` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000472` as traceability during the migration.

## Change Log

- v349, 2026-09: lifts `traitmech:000472 DS-26 system` into the
  `METPO:1042600` placeholder block.
