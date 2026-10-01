# METPO ROBOT Template Proposal - Brc22 System (v400, 2026-10)

## Summary

This cohort reserves `METPO:1047700` for `Brc22 system`, a genome-level
possession trait for the `gcu22`/`brc22` bacteriophage-resistance integron
cassette tested by Kieffer et al. in mobile-integron BRiC phage-resistance
panels.

The local TraitMech fallback is `traitmech:000523` in
`data/traits/genomics/brc22_system.yaml`. The proposed METPO class sits
under the earlier proposed phage-defense parent, `METPO:1016300`.

## Scope

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Brc22 system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no enum lift |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## Duplicate Review

An ignored-and-hidden duplicate search checked the exact local identifier,
proposal placeholder, proposal cohort, slug, label, Brc strings, and
normalized gcu strings across the current TraitMech curation corpus. It found no exact
same-scope Brc22 record, METPO term, history record, or prior proposal for
`traitmech:000523`, `METPO:1047700`, `metpo_traitmech_v400`,
`brc22_system`, `Brc22 system`, `Brc22`, `brc22`, or `gcu22`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1047700` | Brc22 system | `METPO:1016300` phage defense system |

Brc22 system captures genome-level possession of a gcu22/Brc22
bacteriophage-resistance integron cassette that supports host growth during
phage challenge. It excludes individual Brc22 proteins, `brc22` nucleotide
sequences, `attC` sites, absent source database rows naming `gcu22`, absent
DefenseFinder HMM/rules profiles, broad BRiC families, Brc23/Tragantia
homolog-family scope, and other mobile integron phage-defense cassettes.

`gcu22` and `brc22` are proposed as related synonyms because they name the
normalized cassette key and Brc label, not the full organism-level system
possession trait.

## Mappings

No exact external mapping is proposed. Individual Brc22 proteins, exact
`brc22` nucleotide sequences, `attC` sites, broad BRiC families, Brc23/
Tragantia family membership, and the normalized `gcu22` key are narrower or
shifted relative to the organism-level Brc22 system trait.

## Verification

- `rg --no-ignore --hidden` found no collision for `traitmech:000523`,
  `METPO:1047700`, `metpo_traitmech_v400`, `brc22_system`,
  `Brc22 system`, `Brc22`, `brc22`, or `gcu22`.
- `rg --no-ignore --hidden` over `data/raw/metpo.owl` found no exact upstream
  METPO term for `Brc22`, `brc22`, or `gcu22`.
- The pinned DefenseFinder article registry, HMM inventory, and rules files
  have no exact `gcu22`, `brc22`, or `Brc22` row.
- `scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v400`
- `scripts/robot_validate_proposal.py proposals/metpo_traitmech_v400`

## Upstream Path

Submit the ROBOT template row to the METPO upstream queue. After METPO mints a
stable replacement for `METPO:1047700`, re-seed TraitMech from the accepted
METPO release, migrate `traitmech:000523` to the upstream CURIE, and retain
`traitmech:000523` as a traceability xref.

## Changelog

- v400, 2026-10: lifts `traitmech:000523 Brc22 system` into the METPO
  placeholder block at `METPO:1047700`.
