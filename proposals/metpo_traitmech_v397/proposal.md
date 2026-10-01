# METPO ROBOT Template Proposal - BrcWGS21 System (v397, 2026-10)

## Summary

This cohort reserves `METPO:1047400` for `BrcWGS21 system`, a genome-level
possession trait for the `gcuWGS21`/`brcWGS21` bacteriophage-resistance
integron cassette tested by Kieffer et al. in mobile-integron BRiC
phage-resistance panels.

The local TraitMech fallback is `traitmech:000520` in
`data/traits/genomics/brcwgs21_system.yaml`. The proposed METPO class sits
under the earlier proposed phage-defense parent, `METPO:1016300`.

## Scope

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for BrcWGS21 system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no enum lift |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## Duplicate Review

An ignored-and-hidden duplicate search checked the exact local identifier,
proposal placeholder, proposal cohort, slug, label, DefenseFinder source key,
and Brc/gcu strings across the current TraitMech curation corpus. It found no
exact same-scope BrcWGS21 record, METPO term, history record, or prior proposal
for `traitmech:000520`, `METPO:1047400`, `metpo_traitmech_v397`,
`brcwgs21_system`, `BrcWGS21 system`, `BrcWGS21`, `brcWGS21`, or `gcuWGS21`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1047400` | BrcWGS21 system | `METPO:1016300` phage defense system |

BrcWGS21 system captures genome-level possession of a gcuWGS21/BrcWGS21
bacteriophage-resistance integron cassette that supports host growth during
phage challenge. It excludes individual BrcWGS21 proteins, `brcWGS21`
nucleotide sequences, `attC` sites, source database rows naming one
`gcuWGS21` model, absent DefenseFinder HMM/rules profiles, broad BRiC
families, and other mobile integron phage-defense cassettes.

`gcuWGS21` and `brcWGS21` are proposed as related synonyms because they name
the source cassette and DefenseFinder article key, not the full organism-level
system possession trait.

## Mappings

No exact external mapping is proposed. Individual BrcWGS21 proteins, exact
`brcWGS21` nucleotide sequences, `attC` sites, broad BRiC families, and the
DefenseFinder `gcuWGS21` source key are narrower or shifted relative to the
organism-level BrcWGS21 system trait.

## Verification

- `rg --no-ignore --hidden` found no collision for `traitmech:000520`,
  `METPO:1047400`, `metpo_traitmech_v397`, `brcwgs21_system`,
  `BrcWGS21 system`, `BrcWGS21`, `brcWGS21`, or `gcuWGS21`.
- `rg --no-ignore --hidden` over `data/raw/metpo.owl` found no exact upstream
  METPO term for `BrcWGS21`, `brcWGS21`, or `gcuWGS21`.
- The pinned DefenseFinder article registry contains the exact `gcuWGS21` row.
- The pinned DefenseFinder HMM and rules files have no exact `gcuWGS21`,
  `brcWGS21`, or `BrcWGS21` row.
- `scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v397`
- `scripts/robot_validate_proposal.py proposals/metpo_traitmech_v397`

## Upstream Path

Submit the ROBOT template row to the METPO upstream queue. After METPO mints a
stable replacement for `METPO:1047400`, re-seed TraitMech from the accepted
METPO release, migrate `traitmech:000520` to the upstream CURIE, and retain
`traitmech:000520` as a traceability xref.

## Changelog

- v397, 2026-10: lifts `traitmech:000520 BrcWGS21 system` into the METPO
  placeholder block at `METPO:1047400`.
