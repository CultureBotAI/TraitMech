# METPO ROBOT Template Proposal - Brc113 System (v399, 2026-10)

## Summary

This cohort reserves `METPO:1047600` for `Brc113 system`, a genome-level
possession trait for the `gcu113`/`brc113` bacteriophage-resistance integron
cassette tested by Kieffer et al. in mobile-integron BRiC phage-resistance
panels.

The local TraitMech fallback is `traitmech:000522` in
`data/traits/genomics/brc113_system.yaml`. The proposed METPO class sits
under the earlier proposed phage-defense parent, `METPO:1016300`.

## Scope

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Brc113 system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no enum lift |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## Duplicate Review

An ignored-and-hidden duplicate search checked the exact local identifier,
proposal placeholder, proposal cohort, slug, label, Brc strings, and
normalized gcu strings across the current TraitMech curation corpus. It found no exact
same-scope Brc113 record, METPO term, history record, or prior proposal for
`traitmech:000522`, `METPO:1047600`, `metpo_traitmech_v399`,
`brc113_system`, `Brc113 system`, `Brc113`, `brc113`, or `gcu113`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1047600` | Brc113 system | `METPO:1016300` phage defense system |

Brc113 system captures genome-level possession of a gcu113/Brc113
bacteriophage-resistance integron cassette that supports host growth during
phage challenge. It excludes individual Brc113 proteins, `brc113` nucleotide
sequences, `attC` sites, absent source database rows naming `gcu113`, absent
DefenseFinder HMM/rules profiles, broad BRiC families, and other mobile
integron phage-defense cassettes.

`gcu113` and `brc113` are proposed as related synonyms because they name the
normalized cassette key and Brc label, not the full organism-level system possession
trait.

## Mappings

No exact external mapping is proposed. Individual Brc113 proteins, exact
`brc113` nucleotide sequences, `attC` sites, broad BRiC families, and the
normalized `gcu113` key are narrower or shifted relative to the organism-level
Brc113 system trait.

## Verification

- `rg --no-ignore --hidden` found no collision for `traitmech:000522`,
  `METPO:1047600`, `metpo_traitmech_v399`, `brc113_system`,
  `Brc113 system`, `Brc113`, `brc113`, or `gcu113`.
- `rg --no-ignore --hidden` over `data/raw/metpo.owl` found no exact upstream
  METPO term for `Brc113`, `brc113`, or `gcu113`.
- The pinned DefenseFinder article registry, HMM inventory, and rules files
  have no exact `gcu113`, `brc113`, or `Brc113` row.
- `scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v399`
- `scripts/robot_validate_proposal.py proposals/metpo_traitmech_v399`

## Upstream Path

Submit the ROBOT template row to the METPO upstream queue. After METPO mints a
stable replacement for `METPO:1047600`, re-seed TraitMech from the accepted
METPO release, migrate `traitmech:000522` to the upstream CURIE, and retain
`traitmech:000522` as a traceability xref.

## Changelog

- v399, 2026-10: lifts `traitmech:000522 Brc113 system` into the METPO
  placeholder block at `METPO:1047600`.
