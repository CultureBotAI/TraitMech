# METPO ROBOT Template Proposal - DS-21 System (v323, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the other TraitMech Scope-A cohorts, requesting a real METPO ID for
> this `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for DS-21 system, the
genome-level possession trait for DefensePredictor-discovered system 21.
DeWeirdt et al. mapped working identifier TOXO to DS-21 and measured reduced
Bas1 bacteriophage plaquing in a heterologous plasmid-expression assay. The
final Science Table S6/S7/S8 files record the TOXO locus, one plaquing readout,
the replicated DS-21 display name, and a PDDEXK HHpred-domain row. The pinned
DefenseFinder article registry maps DS-21 to the DefensePredictor preprint, the
pinned DefenseFinder HMM inventory records three DS-21 custom profiles,
`DS-21__DS-21A`, `DS-21__DS-21B`, and `DS-21__DS-21C`, and the pinned
DefenseFinder rules table checked in this curation pass has no DS-21 row.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-21 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1040000` is reserved for this one-row class cohort. The v322 cohort used
`METPO:1039900`, so v323 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope DS-21 TraitMech, METPO, history,
or prior proposal record, no `DS-21__DS-21A`, `DS-21__DS-21B`, or
`DS-21__DS-21C` profile-key mention, no `WP_001532221.1`, `WP_001557682.1`, or
`WP_021552536.1` product-accession mention, no `NZ_QOXJ01000032.1` contig
mention, no `ds_21_system` slug, no `traitmech:000446`, no
`metpo_traitmech_v323`, and no `METPO:1040000` proposal block. The TOXO working
identifier appeared only in a DS-20 assay filename, not as a same-scope source
working identifier.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1040000` | DS-21 system | `METPO:1016300` phage defense system |

DS-21 system captures genome-level possession of the three-gene
DefensePredictor-discovered system 21 locus cataloged as working identifier
TOXO and represented by the DefenseFinder DS-21 custom HMM-profile rows. It
excludes the TOXO source working identifier, the individual DS-21 genes and
proteins, individual DefenseFinder HMM profile rows, cloned-transcriptional-unit
plaquing assays, the PDDEXK HHpred-domain annotation, the absent DS-21
rule-level DefenseFinder model, unresolved component activity, unresolved phage
breadth, and other DefensePredictor-discovered or phage-defense systems.

`traitmech:000446` is a direct local child of `traitmech:000209` phage defense
system.

## External Mappings

No exact external mapping is proposed. `TOXO` is kept as a related synonym
because it names the source working identifier, and `DS-21__DS-21A`,
`DS-21__DS-21B`, and `DS-21__DS-21C` are kept as related synonyms because they
name DefenseFinder profile keys rather than the genome-level possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with the
  exact `DS-21` synonym and related source/profile keys.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000446` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000446` as traceability during the migration.

## Change Log

- v323, 2026-09: lifts `traitmech:000446 DS-21 system` into the
  `METPO:1040000` placeholder block.
