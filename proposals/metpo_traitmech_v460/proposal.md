# METPO Proposal v460: Gyrotaxis

## Context

Lift `traitmech:000583 gyrotaxis`, a motile phenotype involving gravitational
and viscous torques that bias swimming orientation. Zeng et al.
(DOI:10.1073/pnas.2206738119) provide the definition and a named microbial
culture; Durham et al. (DOI:10.1126/science.1167334) demonstrate a shear-dependent
population consequence. These are primary studies, not profile predictions.

Fresh temporary seeding emitted 399 identifiers: 344 present and 55 absent
from the pre-change 977-record corpus. Both frozen release-review tables were
read and candidate status checked against the live tree. Whole-repository
novelty searches included ignored and hidden files, labels and stems,
gravitaxis/geotaxis alternatives, both primary citation identifiers and
semantic descriptions (gravity-driven orientation, viscous torque and
hydrodynamic focusing). No exact existing record or METPO class was found.
The upstream METPO issue search also returned no gyrotaxis result.

## Scope

| Scope | Rows | Parent | Leaves |
|---|---:|---|---:|
| A: local trait lift | 1 | motile | 1 |
| B: predicates | 0 | None proposed | 0 |
| C: schema enums | 0 | Outside this trait addition | 0 |

## Hierarchy Decisions

| Proposed ID | Local ID | Label | Parent |
|---|---|---|---|
| METPO:1053700 | traitmech:000583 | gyrotaxis | METPO:1000702 |

The parent denotes independent energy-dependent movement. Orientation can
arise physically while locomotion remains actively powered. Passive
sedimentation alone does not establish the trait. PHYSIOLOGY follows the
behavioral scope of neighboring taxis records. Rheotaxis is not the parent:
Zeng et al. explicitly include viscous resistance to gravitational
reorientation in still fluid, without an imposed fluid velocity gradient.
Gravitaxis, gyrotactic trapping and bioconvection are not exact synonyms.
No older trait YAML is edited.

## Evidence And Mapping Boundaries

- Zeng et al.'s full main article was read from the author institution's
  repository, with the definition and culture methods visually checked on
  pages 1 and 9. The GY-H24 canonical example retains the light-phase
  restriction; the species taxon is not asserted to be a strain accession.
- Durham et al.'s main article distinguishes torque-mediated swimming,
  high-shear trapping, observed layers and model predictions for ocean-scale
  layers. Dead-cell controls support the motility requirement. The unverified
  historical C. nivalis culture is not assigned a modern taxon identifier.
- Neither study establishes universal bottom-heaviness, obligatory wall
  contact, one direction across all phases, or a common gravity receptor.
  Supplements and movies were not inspected; no supplement-only claim is used.
- The physical mechanism is supported, but no causal graph is included in
  this identity pass. The current mechanistic coverage audit requires a
  protein node and example. A physical-graph representation TODO records that
  constraint; NONMECHANISTIC is not misused to label physical causation as
  classification, and no protein identity is invented to satisfy the audit.
- NCBI resolves 2829 to Heterosigma akashiwo (species). QuickGO returns zero
  gyrotaxis terms. No exact xref or SSSOM equivalence is asserted.

Authority checks: 2026-10-04. Both sources have contiguous short snippets;
interpretation and access limitations are in evidence notes.

## ID Space And Subset

Reserve `METPO:1053700-1053799`, using only `1053700`, after v459's
`1053600` block. Fresh ignored-and-hidden allocation searches found no local
ID, cohort or block collision. The block does not intersect CommunityMech v1
`1007100-1007220`. Subset: `metpo_traitmech_2026_10`.

## Files

| File | Data rows |
|---|---:|
| metpo_proposal_classes_robot.tsv | 1 |
| proposal.md | Narrative |
| Properties and SSSOM | Omitted: no predicate or equivalent mapping |

The 11-column header follows the refreshed kg-microbe master template,
including the three trailing empty ROBOT header cells.

## Verification

Run `scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v460`,
`scripts/robot_validate_proposal.py proposals/metpo_traitmech_v460` and
`scripts/verify_metpo_proposal.py --coverage`. Actual validation results and
rendered-page checks will be recorded in the PR.

## Upstream Path

Submit the verified TSV to berkeleybop/metpo after TraitMech review. The
proposal placeholder is not a released or accepted METPO identifier.

## Round-Trip Plan

After upstream acceptance, refresh METPO, seed a temporary tree and migrate
to the released identifier while retaining `traitmech:000583` in provenance.
Regenerate affected artifacts; do not publish the placeholder as released.

## Change Log

- v460, 2026-10-04: add gyrotaxis with bounded primary evidence.
