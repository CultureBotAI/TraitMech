# METPO ROBOT Template Proposal - Brc23 System (v401, 2026-10)

## Summary

This cohort reserves `METPO:1047800` for `Brc23 system`, a genome-level
possession trait for the `gcu23`/`brc23` bacteriophage-resistance integron
cassette tested by Kieffer et al. in mobile-integron BRiC phage-resistance
panels.

The local TraitMech fallback is `traitmech:000524` in
`data/traits/genomics/brc23_system.yaml`. The proposed METPO class sits
under the earlier proposed phage-defense parent, `METPO:1016300`.

## Scope

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Brc23 system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no enum lift |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## Duplicate Review

An ignored-and-hidden duplicate search checked the exact local identifier,
proposal placeholder, proposal cohort, slug, label, Brc strings, and
normalized gcu strings across the current TraitMech curation corpus. It found
no exact identifier, placeholder, cohort, slug, or label collision for
`traitmech:000524`, `METPO:1047800`, `metpo_traitmech_v401`,
`brc23_system`, or `Brc23 system`; exact `Brc23`/`brc23`/`gcu23` hits were
then reviewed to rule out a same-scope Brc23 record, METPO term, history
record, or prior proposal.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1047800` | Brc23 system | `METPO:1016300` phage defense system |

Brc23 system captures genome-level possession of a gcu23/Brc23
bacteriophage-resistance integron cassette that supports host growth during
phage challenge. It excludes individual Brc23 proteins, `brc23` nucleotide
sequences, `attC` sites, absent source database rows naming `gcu23`, absent
DefenseFinder HMM/rules profiles, broad BRiC families, Brc22/Tragantia
homolog-family scope, and other mobile integron phage-defense cassettes.

`gcu23` and `brc23` are proposed as related synonyms because they name the
normalized cassette key and Brc label, not the full organism-level system
possession trait.

## Mappings

No exact external mapping is proposed. Individual Brc23 proteins, exact
`brc23` nucleotide sequences, `attC` sites, broad BRiC families, Brc22/
Tragantia family membership, and the normalized `gcu23` key are narrower or
shifted relative to the organism-level Brc23 system trait.

## Verification

- `rg --no-ignore --hidden` found no collision for exact stable identifiers,
  slugs, cohorts, and labels: `traitmech:000524`,
  `METPO:1047800`, `metpo_traitmech_v401`, `brc23_system`,
  or `Brc23 system`.
- `rg --no-ignore --hidden` found exact `Brc23`, `brc23`, and `gcu23` hits
  only in non-colliding sibling BRiC records, generated pages, and writer
  scripts; manual review found no same-scope Brc23 TraitMech record, METPO
  term, history record, or prior proposal.
- `rg --no-ignore --hidden` over `data/raw/metpo.owl` found no exact upstream
  METPO term for `Brc23`, `brc23`, or `gcu23`.
- The pinned DefenseFinder article registry, HMM inventory, and rules files
  have no exact `gcu23`, `brc23`, or `Brc23` row.
- `scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v401`
- `scripts/robot_validate_proposal.py proposals/metpo_traitmech_v401`

## Upstream Path

Submit the ROBOT template row to the METPO upstream queue. After METPO mints a
stable replacement for `METPO:1047800`, re-seed TraitMech from the accepted
METPO release, migrate `traitmech:000524` to the upstream CURIE, and retain
`traitmech:000524` as a traceability xref.

## Changelog

- v401, 2026-10: lifts `traitmech:000524 Brc23 system` into the METPO
  placeholder block at `METPO:1047800`.
