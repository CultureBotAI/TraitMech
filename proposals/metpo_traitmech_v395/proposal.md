# METPO ROBOT Template Proposal - Brc233 System (v395, 2026-10)

## Summary

This cohort reserves `METPO:1047200` for `Brc233 system`, a genome-level
possession trait for the `gcu233`/`brc233` bacteriophage-resistance integron
cassette tested by Kieffer et al. in mobile-integron BRiC phage-resistance
panels.

The local TraitMech fallback is `traitmech:000518` in
`data/traits/genomics/brc233_system.yaml`. The proposed METPO class sits under
the earlier proposed phage-defense parent, `METPO:1016300`.

## Scope

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Brc233 system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no enum lift |

No SSSOM file is emitted because no exact cross-ontology equivalent is proposed.

## Duplicate Review

An ignored-and-hidden duplicate search checked the exact local identifier,
proposal placeholder, proposal cohort, placeholder block, slug, label,
DefenseFinder source key, and Brc/gcu strings across the current TraitMech
curation corpus. It found no exact same-scope Brc233 record, METPO term,
history record, or prior proposal for `traitmech:000518`, `METPO:1047200`,
`METPO:10472xx`, `metpo_traitmech_v395`, `brc233_system`, `Brc233 system`,
`Brc233`, `brc233`, or `gcu233`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1047200` | Brc233 system | `METPO:1016300` phage defense system |

Brc233 system captures genome-level possession of a gcu233/Brc233
bacteriophage-resistance integron cassette that supports host growth during
phage challenge. It excludes individual Brc233 proteins, `brc233` nucleotide
sequences, `attC` sites, source database rows naming one `gcu233` model,
DefenseFinder HMM or rules profiles absent from the pinned snapshot, the
broader class of Bacteriophage Resistance integron Cassettes, and other mobile
integron phage-defense cassettes.

`gcu233` and `brc233` are proposed as related synonyms because they name the
source cassette and DefenseFinder article key, not the full organism-level
system possession trait.

## Mappings

No exact external mapping is proposed. Individual Brc233 proteins, exact
`brc233` nucleotide sequences, `attC` sites, broad BRiC families, and the
DefenseFinder `gcu233` source key are narrower or shifted relative to the
organism-level Brc233 system trait.

## Verification

- `rg --no-ignore --hidden` found no collision for `traitmech:000518`,
  `METPO:1047200`, `METPO:10472xx`, `metpo_traitmech_v395`,
  `brc233_system`, `Brc233 system`, `Brc233`, `brc233`, or `gcu233`.
- `rg --no-ignore --hidden` over `data/raw/metpo.owl` found no exact upstream
  METPO term for `Brc233`, `brc233`, or `gcu233`.
- `curl` of the pinned DefenseFinder article registry verified the exact
  `gcu233` row.
- `curl` of the pinned DefenseFinder HMM and rules files found no exact
  `gcu233`, `brc233`, or `Brc233` row.
- `scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v395`
- `scripts/robot_validate_proposal.py proposals/metpo_traitmech_v395`

## Upstream Path

Submit the ROBOT template row to the METPO upstream queue. After METPO mints a
stable replacement for `METPO:1047200`, re-seed TraitMech from the accepted
METPO release, migrate `traitmech:000518` to the upstream CURIE, and retain
`traitmech:000518` as a traceability xref.

## Changelog

- v395, 2026-10: lifts `traitmech:000518 Brc233 system` into the METPO
  placeholder block at `METPO:1047200`.
