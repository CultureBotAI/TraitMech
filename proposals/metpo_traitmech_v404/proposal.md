# METPO ROBOT Template Proposal - Ferrosome (v404, 2026-10)

## Summary

This cohort reserves `METPO:1048100` for `ferrosome`, a morphology trait in
which bacteria form membrane-bound intracellular organelles that store iron as
non-crystalline iron phosphate.

The local TraitMech fallback is `traitmech:000527` in
`data/traits/morphology/ferrosome.yaml`. The proposed METPO class sits under
the earlier proposed intracellular inclusion parent, `METPO:1007665`.

## Scope

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for ferrosome |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no enum lift |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## Duplicate Review

An ignored-and-hidden duplicate search checked the exact local identifier,
proposal placeholder, proposal cohort, slug, label, and ferrosome strings
across the current TraitMech curation corpus. It found no exact identifier,
placeholder, cohort, or slug collision for `traitmech:000527`,
`METPO:1048100`, `metpo_traitmech_v404`, or `ferrosome.yaml`. Exact
`ferrosome` hits were limited to intracellular inclusion and magnetosome
research/page boundary notes plus branch metadata; no same-scope ferrosome
record, METPO term, history record, or prior proposal exists.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1048100` | ferrosome | `METPO:1007665` intracellular inclusion |

Ferrosome captures an organism-level morphology trait in which bacterial
cells form membrane-bound intracellular organelles that store iron as
non-crystalline iron phosphate biomineral. It excludes generic iron
biomineralization, free intracellular iron particles, magnetosomes, ferritin
or encapsulin-like proteinaceous iron-storage compartments, individual Fez
proteins, fez operons outside a complete ferrosome-forming phenotype, and
host-colonization outputs in `Clostridioides difficile`.

## Mappings

No exact external mapping is proposed. The live exact candidates reviewed in
GO are sibling inclusions or organelles, including `GO:0110143` magnetosome,
`GO:0031411` gas vesicle, `GO:0031470` carboxysome, and `GO:0070088` PHA
granule, rather than ferrosome equivalents.

## Verification

- `rg --no-ignore --hidden` found no collision for exact stable identifiers,
  slugs, cohorts, and labels: `traitmech:000527`, `METPO:1048100`,
  `metpo_traitmech_v404`, or `ferrosome.yaml`.
- `rg --no-ignore --hidden` found no same-scope ferrosome record, METPO term,
  history record, or prior proposal among exact `ferrosome` hits.
- `scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v404`
- `scripts/robot_validate_proposal.py proposals/metpo_traitmech_v404`

## Upstream Path

Submit the ROBOT template row to the METPO upstream queue. After METPO mints a
stable replacement for `METPO:1048100`, re-seed TraitMech from the accepted
METPO release, migrate `traitmech:000527` to the upstream CURIE, and retain
`traitmech:000527` as a traceability xref.

## Changelog

- v404, 2026-10: lifts `traitmech:000527 ferrosome` into the METPO
  placeholder block at `METPO:1048100`.
