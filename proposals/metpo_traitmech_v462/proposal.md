# METPO Proposal v462: Gravikinesis

## Context

Lift `traitmech:000585 gravikinesis`, a motile phenotype involving modulation
of active propulsion speed according to orientation relative to gravity.
Primary sources are Takeda et al. (DOI:10.2187/bss.20.44) and Gebauer et al.
(DOI:10.1007/s001140050634; PMID:11536922).

Temporary seeding emitted 399 identifiers: 344 present and 55 absent from
the pre-change 979-record corpus. Both frozen release-review tables were
checked against live records. Whole-repository searches included ignored
and hidden files, gravikinesis/geokinesis alternatives, active-propulsion
phrases, citations, and the proposed ID block. The substantive hits were
gravitaxis boundary notes, not an exact record, METPO class or unresolved
exact graph node. The upstream METPO issue search returned no gravikinesis
result. Existing boundary notes remain correct; no older trait is edited.

## Scope

| Scope | Rows | Parent | Leaves |
|---|---:|---|---:|
| A: local trait lift | 1 | motile | 1 |
| B: predicates | 0 | None proposed | 0 |
| C: schema enums | 0 | Outside this addition | 0 |

## Hierarchy Decisions

| Proposed ID | Local ID | Label | Parent |
|---|---|---|---|
| METPO:1053900 | traitmech:000585 | gravikinesis | METPO:1000702 |

The parent denotes energy-dependent locomotion. The new trait concerns
active propulsion rather than passive settling or flotation. Directional
bias (gravitaxis) and torque-mediated orientation (gyrotaxis) may coexist
with it, but neither equivalence nor disjointness nor a parent-child
relation among those traits is asserted. PHYSIOLOGY follows the neighboring
motility records. The definition does not require faster upward swimming
in every medium or one universal receptor.

## Evidence And Mapping Boundaries

- Both primary DOI evidence items carry short contiguous abstract snippets.
  Takeda's four-page publisher PDF was inspected, with visual checks of
  methods and Table 1. Gebauer's publisher and Europe PMC abstracts agree;
  its subscription full text was not inspected.
- Takeda measured swimming before immobilizing the same cell with nickel
  to estimate passive drift. The Paramecium caudatum example retains the
  culture, selection, medium and curved-swimming qualifiers. Nickel is
  a later control, not the condition under which active swimming occurred.
- The curved-swimmer response reverses in the hyper-density Percoll medium;
  straight-swimmer responses were not significant. Results N=55 and the
  Table 1 straight-swimmer N=57 are unreconciled. No aggregate sample count
  or universal cell-state phenotype is asserted.
- NCBI resolves 5885 to Paramecium caudatum at species rank, not a strain.
- Orientation-dependent membrane potential and ciliary control support a
  physiological mechanism. The inspected sources do not identify an exact
  sequence-resolved gravity receptor. Hydraulic pressure is discussed as
  a candidate stimulus requiring amplification, not a complete proved
  molecular pathway. A protein-grounded graph is deferred explicitly; no
  unrelated channel or NONMECHANISTIC workaround is introduced.
- Two open discussions preserve propulsion/direction boundaries and the
  exact protein/taxon grounding gap. No external equivalent xref or SSSOM
  mapping is asserted.

Authority checks: 2026-10-04. No new protein instance is asserted.

## ID Space And Subset

Reserve `METPO:1053900-1053999`, using only `1053900`, after v461's
`1053800` block. Ignored-and-hidden searches found no collision with the
local identifier, cohort or block before writing. The block does not
intersect the inspected CommunityMech v1 class or property identifiers.
Subset: `metpo_traitmech_2026_10`.

## Files

| File | Data rows |
|---|---:|
| metpo_proposal_classes_robot.tsv | 1 |
| proposal.md | Narrative |
| Properties and SSSOM | Omitted: no predicate or equivalent mapping |

The 11-column header matches the refreshed kg-microbe class template,
including three trailing empty cells in the ROBOT directive row.

## Verification

Run `scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v462`,
`scripts/robot_validate_proposal.py proposals/metpo_traitmech_v462` and
`scripts/verify_metpo_proposal.py --coverage`. Actual validation results and
rendered-page checks are recorded in the PR.

## Upstream Path

Submit the verified TSV to berkeleybop/metpo after TraitMech review.
The reserved placeholder is not an accepted or released METPO identifier.

## Round-Trip Plan

After upstream acceptance, refresh METPO, seed a temporary tree and migrate
to the released identifier while retaining `traitmech:000585` in provenance.
Regenerate affected artifacts; do not publish the placeholder as released.

## Change Log

- v462, 2026-10-04: add gravikinesis with source-qualified propulsion evidence.
