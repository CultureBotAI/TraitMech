# METPO ROBOT Template Proposal - DS-18 System (v318, 2026-09)

## Scope

The pinned METPO snapshot has no active exact class for DS-18 system, the
DefensePredictor-discovered system 18 phage-defense locus. In the final Science
supplement, DeWeirdt et al. mapped working identifier 6602 to DS-18 and
measured reduced phage plaquing for a cloned 6602 transcriptional unit in
E. coli MG1655. The Science supplementary workbooks also record a replicated
DS-18 display name and a PDDEXK HHpred-domain row. The pinned DefenseFinder
article registry maps DS-18 to the DefensePredictor preprint, the pinned
DefenseFinder HMM inventory records one DS-18 custom profile,
`DS-18__DS-18`, and the pinned DefenseFinder rules table checked in this
curation pass has no DS-18 row.

| Proposal scope | Count | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for DS-18 system |
| B - causal predicate lift | 0 | no new ungrounded causal predicates |
| C - schema enum lift | 0 | no schema enum is in scope |

## Identifier Block

`METPO:1039500` is reserved for this one-row class cohort. The v317 cohort used
`METPO:1039400`; no previously merged proposal or vendored METPO class uses the
1039500 block.

## Duplicate Review

The pre-mint duplicate search covered ignored and hidden files in the live
curation corpus. It found no exact same-scope DS-18 TraitMech, METPO, history,
or prior proposal record, no `DS-18__DS-18` profile-key mention, no `6602`
working-id mention, no `WP_021529611.1` product-accession mention, no
`ds_18_system` slug, no `traitmech:000441`, no `metpo_traitmech_v318`, and no
`METPO:1039500` proposal block.

## Proposed Classes

| METPO placeholder | Label | Parent |
|---|---|---|
| `METPO:1039500` | DS-18 system | `METPO:1016300` phage defense system |

DS-18 system captures genome-level possession of the single-gene
DefensePredictor-discovered system 18 locus, cataloged as working identifier
6602 and represented by the DefenseFinder DS-18 custom HMM-profile row. It
excludes the 6602 source working identifier, the individual DS-18 gene and
protein, cloned-transcriptional-unit plaquing assays, the PDDEXK HHpred-domain
annotation, the absent DS-18 rule-level DefenseFinder model, unresolved
component chemistry, native host breadth, and phage breadth.

## Hierarchy and Synonyms

`traitmech:000441` is a direct local child of `traitmech:000209` phage defense
system, whose upstream placeholder is `METPO:1016300`. DS-18 is another
DefensePredictor-discovered system in the phage-defense branch.

`DS-18` is exact because the Science paper names validated DefensePredictor
transcriptional units as DSs and its supplementary tables use DS-18 as the
display name. `6602` is kept as a related synonym because it names the numeric
source working identifier, and `DS-18__DS-18` is kept as a related synonym
because it is a DefenseFinder HMM profile key rather than an ordinary trait
label.

## Verification

- The new TraitRecord validates against the closed TraitMech LinkML schema.
- The METPO proposal verifies with `scripts/verify_metpo_proposal.py
  proposals/metpo_traitmech_v318`.
- The ROBOT template validates with `scripts/robot_validate_proposal.py
  proposals/metpo_traitmech_v318`.
- `scripts/audit_proposals.py` sees the new record as proposed, cited, and
  backed by stable DOI/OpenData/DefenseFinder references.

## Upstream Round-Trip

1. Submit this ROBOT template to METPO maintainers.
2. On mint, replace local `traitmech:000441` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000441` as traceability during the migration.

## Changelog

- v318, 2026-09: lifts `traitmech:000441 DS-18 system` into the
  `METPO:1039500` placeholder block.
