# METPO ROBOT Template Proposal - Cellular Buoyancy (v405, 2026-10)

## Summary

This cohort reserves `METPO:1048200` for `cellular buoyancy`, a physiology
trait in which intracellular gas vesicles reduce a microbial cell's effective
density enough to provide buoyancy and vertical positioning in the water
column.

The local TraitMech fallback is `traitmech:000528` in
`data/traits/physiology/cellular_buoyancy.yaml`. The proposed METPO class sits
under the phenotype parent, `METPO:1000059`.

## Scope

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for cellular buoyancy |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no enum lift |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## Duplicate Review

An ignored-and-hidden duplicate search checked the exact local identifier,
proposal placeholder, proposal cohort, slug, label, and buoyancy terms across
the current TraitMech curation corpus. It found no exact identifier,
placeholder, cohort, or slug collision for `traitmech:000528`,
`METPO:1048200`, `metpo_traitmech_v405`, or `cellular_buoyancy.yaml`. Exact
`cellular buoyancy` and `buoyancy` hits were limited to existing causal-graph
nodes in the gas-vesicle and intracellular-inclusion records, rendered page
derivatives, and source research notes; no same-scope cellular-buoyancy record,
METPO term, history record, or prior proposal exists.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1048200` | cellular buoyancy | `METPO:1000059` phenotype |

Cellular buoyancy captures an organism-level physiology trait in which
gas-vesicle-containing cells gain flotation capacity by reducing effective
cellular density. It excludes the gas vesicle organelle itself, generic
physical mass density, gas-vesicle shell assembly outside an intact cell,
downstream ultrasound scattering phenotypes, and water-column positioning
processes that are not asserted to be gas-vesicle mediated.

## Mappings

No exact external mapping is proposed. The live exact candidate reviewed in GO,
`GO:0031411` gas vesicle, is the intracellular gas-filled organelle that
confers the physiology rather than the cellular-buoyancy disposition itself.
The only local METPO buoyancy hit is obsolete `buoyancy structure`, not an
active physiology trait.

## Verification

- `rg --no-ignore --hidden` found no collision for exact stable identifiers,
  slugs, and cohorts: `traitmech:000528`, `METPO:1048200`,
  `metpo_traitmech_v405`, or `cellular_buoyancy.yaml`.
- `rg --no-ignore --hidden` found no same-scope cellular-buoyancy record,
  METPO term, history record, or prior proposal among exact `cellular
  buoyancy`, `buoyancy`, flotation, and water-column-positioning hits.
- `scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v405`
- `scripts/robot_validate_proposal.py proposals/metpo_traitmech_v405`

## Upstream Path

Submit the ROBOT template row to the METPO upstream queue. After METPO mints a
stable replacement for `METPO:1048200`, re-seed TraitMech from the accepted
METPO release, migrate `traitmech:000528` to the upstream CURIE, and retain
`traitmech:000528` as a traceability xref.

## Changelog

- v405, 2026-10: lifts `traitmech:000528 cellular buoyancy` into the METPO
  placeholder block at `METPO:1048200`.
