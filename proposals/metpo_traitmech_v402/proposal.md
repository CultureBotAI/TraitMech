# METPO ROBOT Template Proposal - Brc59 System (v402, 2026-10)

## Summary

This cohort reserves `METPO:1047900` for `Brc59 system`, a genome-level
possession trait for the `brc59` bacteriophage-resistance integron cassette
tested by Kieffer et al. in mobile-integron BRiC phage-resistance panels.

The local TraitMech fallback is `traitmech:000525` in
`data/traits/genomics/brc59_system.yaml`. The proposed METPO class sits
under the earlier proposed phage-defense parent, `METPO:1016300`.

## Scope

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Brc59 system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no enum lift |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## Duplicate Review

An ignored-and-hidden duplicate search checked the exact local identifier,
proposal placeholder, proposal cohort, slug, label, Brc strings, and possible
normalized gcu string across the current TraitMech curation corpus. It found
no exact identifier, placeholder, cohort, slug, or label collision for
`traitmech:000525`, `METPO:1047900`, `metpo_traitmech_v402`,
`brc59_system`, or `Brc59 system`; exact `Brc59`/`brc59`/`gcu59` searches
then ruled out a same-scope Brc59 record, METPO term, history record, or prior
proposal.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1047900` | Brc59 system | `METPO:1016300` phage defense system |

Brc59 system captures genome-level possession of a Brc59
bacteriophage-resistance integron cassette that supports host growth during
phage challenge. It excludes individual Brc59 proteins, `brc59` nucleotide
sequences, `attC` sites, a possible but source-unresolved `gcu59` normalized
key, absent DefenseFinder HMM/article/rules profiles, broad BRiC families, and
other mobile-integron phage-defense cassettes.

`brc59` is proposed as a related synonym because it names the Brc label, not
the full organism-level system-possession trait. `gcu59` is not proposed as a
synonym because the pinned DefenseFinder article registry has no exact `gcu59`
row, unlike `gcu142`, `gcu167`, `gcu233`, `gcu24`, `gcu76`, and `gcuWGS21`.

## Mappings

No exact external mapping is proposed. Individual Brc59 proteins, exact
`brc59` nucleotide sequences, `attC` sites, broad BRiC families, and any
normalized `gcu59` key are narrower or shifted relative to the organism-level
Brc59 system trait.

## Verification

- `rg --no-ignore --hidden` found no collision for exact stable identifiers,
  slugs, cohorts, and labels: `traitmech:000525`, `METPO:1047900`,
  `metpo_traitmech_v402`, `brc59_system`, or `Brc59 system`.
- `rg --no-ignore --hidden` found no exact `Brc59`, `brc59`, or `gcu59`
  hits in `data`, `proposals`, `history`, `scripts`, `research`, or
  `data/raw/metpo.owl`.
- The pinned DefenseFinder article registry, HMM inventory, and rules files
  have no exact `gcu59`, `brc59`, or `Brc59` row.
- `scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v402`
- `scripts/robot_validate_proposal.py proposals/metpo_traitmech_v402`

## Upstream Path

Submit the ROBOT template row to the METPO upstream queue. After METPO mints a
stable replacement for `METPO:1047900`, re-seed TraitMech from the accepted
METPO release, migrate `traitmech:000525` to the upstream CURIE, and retain
`traitmech:000525` as a traceability xref.

## Changelog

- v402, 2026-10: lifts `traitmech:000525 Brc59 system` into the METPO
  placeholder block at `METPO:1047900`.
