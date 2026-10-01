# METPO ROBOT Template Proposal - Brc142 System (v392, 2026-10)

## Summary

This cohort reserves `METPO:1046900` for `Brc142 system`, a genome-level
possession trait for the `gcu142`/`brc142` bacteriophage-resistance integron
cassette identified by Kieffer et al. in a mobile-integron phage-resistance
screen.

The local TraitMech fallback is `traitmech:000515` in
`data/traits/genomics/brc142_system.yaml`. The proposed METPO class sits under
the earlier proposed phage-defense parent, `METPO:1016300`.

## Scope

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Brc142 system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no enum lift |

No SSSOM file is emitted because no exact cross-ontology equivalent is proposed.

## Duplicate Review

An ignored-and-hidden duplicate search checked the exact local identifier,
proposal placeholder, proposal cohort, placeholder block, slug, label,
DefenseFinder source key, DOI, and Brc/gcu strings across the current TraitMech
curation corpus. It found no exact same-scope Brc142 record, METPO term,
history record, or prior proposal for `traitmech:000515`, `METPO:1046900`,
`METPO:10469xx`, `metpo_traitmech_v392`, `brc142_system`, `Brc142 system`,
`Brc142`, `brc142`, `gcu142`, or `10.1126/science.ads0915`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1046900` | Brc142 system | `METPO:1016300` phage defense system |

Brc142 system captures genome-level possession of a gcu142/Brc142
bacteriophage-resistance integron cassette that supports host growth during
phage challenge. It excludes individual Brc142 proteins, `brc142` nucleotide
sequences, `attC` sites, source database rows naming one `gcu142` model,
DefenseFinder HMM or rules profiles absent from the pinned snapshot, the
broader class of Bacteriophage Resistance integron Cassettes, and other mobile
integron phage-defense cassettes.

`gcu142` and `brc142` are proposed as related synonyms because they name the
source cassette and DefenseFinder article key, not the full organism-level
system possession trait.

## Mappings

No exact external mapping is proposed. Individual Brc142 proteins, exact
`brc142` nucleotide sequences, `attC` sites, broad BRiC families, and the
DefenseFinder `gcu142` source key are narrower or shifted relative to the
organism-level Brc142 system trait.

## Verification

- `rg --no-ignore --hidden` found no collision for `traitmech:000515`,
  `METPO:1046900`, `METPO:10469xx`, `metpo_traitmech_v392`,
  `brc142_system`, `Brc142 system`, `Brc142`, `brc142`, `gcu142`, or DOI
  `10.1126/science.ads0915`.
- `rg --no-ignore --hidden` over `data/raw/metpo.owl` found no exact upstream
  METPO term for `Brc142`, `brc142`, or `gcu142`.
- `curl` of the pinned DefenseFinder article registry verified the exact
  `gcu142` row.
- `curl` of the pinned DefenseFinder HMM and rules files found no exact
  `gcu142`, `brc142`, or `Brc142` row.
- `scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v392`
- `scripts/robot_validate_proposal.py proposals/metpo_traitmech_v392`

## Upstream Path

Submit the ROBOT template row to the METPO upstream queue. After METPO mints a
stable replacement for `METPO:1046900`, re-seed TraitMech from the accepted
METPO release, migrate `traitmech:000515` to the upstream CURIE, and retain
`traitmech:000515` as a traceability xref.

## Changelog

- v392, 2026-10: lifts `traitmech:000515 Brc142 system` into the METPO
  placeholder block at `METPO:1046900`.
