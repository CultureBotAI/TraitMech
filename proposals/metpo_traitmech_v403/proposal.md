# METPO ROBOT Template Proposal - MksBEFG System (v403, 2026-10)

## Summary

This cohort reserves `METPO:1048000` for `MksBEFG system`, a
genome-level possession trait for the Wadjet-family MksBEFG derivative SMC
plasmid-defense system.

The local TraitMech fallback is `traitmech:000526` in
`data/traits/genomics/mksbefg_system.yaml`. The proposed METPO class sits
under the earlier proposed Wadjet parent, `METPO:1017200`.

## Scope

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for MksBEFG system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no enum lift |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## Duplicate Review

An ignored-and-hidden duplicate search checked the exact local identifier,
proposal placeholder, proposal cohort, slug, label, MksBEFG strings, and the
MksG/MksBEF source phrases across the current TraitMech curation corpus. It
found no exact identifier, placeholder, cohort, slug, or label collision for
`traitmech:000526`, `METPO:1048000`, `metpo_traitmech_v403`,
`mksbefg_system`, or `MksBEFG system`. Exact `MksBEFG`, `MksBEF`, and `MksG`
hits were limited to the broad Wadjet parent, the Wadjet writer, generated
Wadjet pages, generated reports, and `metpo_traitmech_v95`; no same-scope
MksBEFG record, METPO term, history record, or prior proposal exists.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1048000` | MksBEFG system | `METPO:1017200` Wadjet system |

MksBEFG system captures genome-level possession of an MksBEFG
derivative-SMC locus in which the MksBEF ATPase core and MksG nuclease mediate
plasmid DNA degradation. It excludes individual `mks` genes or proteins,
isolated MksBEFG protein complexes, MksG nuclease activity outside a complete
organism-level system, broad Wadjet systems, JetABCD, EptABCD, source detector
boundaries such as DefenseFinder Wadjet I-III, plasmid transformation itself,
and other anti-plasmid systems.

`MksBEFG` is proposed as a related synonym because it names the source
component set, not the full organism-level system-possession trait.

## Mappings

No exact external mapping is proposed. Individual MksB, MksE, MksF, and MksG
proteins, `mks` genes, the MksBEFG protein complex, MksG nuclease activity,
Wadjet detector subtype rows, and broad plasmid-defense phenotypes are shifted
relative to the organism-level MksBEFG system trait.

## Verification

- `rg --no-ignore --hidden` found no collision for exact stable identifiers,
  slugs, cohorts, and labels: `traitmech:000526`, `METPO:1048000`,
  `metpo_traitmech_v403`, `mksbefg_system`, or `MksBEFG system`.
- `rg --no-ignore --hidden` found no same-scope MksBEFG record, METPO term,
  history record, or prior proposal among exact `MksBEFG`, `MksBEF`, and
  `MksG` hits.
- `scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v403`
- `scripts/robot_validate_proposal.py proposals/metpo_traitmech_v403`

## Upstream Path

Submit the ROBOT template row to the METPO upstream queue. After METPO mints a
stable replacement for `METPO:1048000`, re-seed TraitMech from the accepted
METPO release, migrate `traitmech:000526` to the upstream CURIE, and retain
`traitmech:000526` as a traceability xref.

## Changelog

- v403, 2026-10: lifts `traitmech:000526 MksBEFG system` into the METPO
  placeholder block at `METPO:1048000`.
