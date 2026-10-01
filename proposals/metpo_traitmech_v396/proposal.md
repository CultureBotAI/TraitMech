# METPO ROBOT Template Proposal - Brc76 System (v396, 2026-10)

## Summary

This cohort reserves `METPO:1047300` for `Brc76 system`, a genome-level
possession trait for the `gcu76`/`brc76` bacteriophage-resistance integron
cassette tested by Kieffer et al. in mobile-integron BRiC phage-resistance
panels.

The local TraitMech fallback is `traitmech:000519` in
`data/traits/genomics/brc76_system.yaml`. The proposed METPO class sits under
the earlier proposed phage-defense parent, `METPO:1016300`.

## Scope

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Brc76 system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no enum lift |

No SSSOM file is emitted because no exact cross-ontology equivalent is proposed.

## Duplicate Review

An ignored-and-hidden duplicate search checked the exact local identifier,
proposal placeholder, proposal cohort, placeholder block, slug, label,
DefenseFinder source key, and Brc/gcu strings across the current TraitMech
curation corpus. It found no exact same-scope Brc76 record, METPO term,
history record, or prior proposal for `traitmech:000519`, `METPO:1047300`,
`METPO:10473xx`, `metpo_traitmech_v396`, `brc76_system`, `Brc76 system`,
`Brc76`, `brc76`, or `gcu76`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1047300` | Brc76 system | `METPO:1016300` phage defense system |

Brc76 system captures genome-level possession of a gcu76/Brc76
bacteriophage-resistance integron cassette that supports host growth during
phage challenge. It excludes individual Brc76 proteins, `brc76` nucleotide
sequences, `attC` sites, source database rows naming one `gcu76` model,
DefenseFinder HMM or rules profiles absent from the pinned snapshot, the
broader class of Bacteriophage Resistance integron Cassettes, and other mobile
integron phage-defense cassettes.

`gcu76` and `brc76` are proposed as related synonyms because they name the
source cassette and DefenseFinder article key, not the full organism-level
system possession trait.

## Mappings

No exact external mapping is proposed. Individual Brc76 proteins, exact `brc76`
nucleotide sequences, `attC` sites, broad BRiC families, and the DefenseFinder
`gcu76` source key are narrower or shifted relative to the organism-level Brc76
system trait.

## Verification

- `rg --no-ignore --hidden` found no collision for `traitmech:000519`,
  `METPO:1047300`, `METPO:10473xx`, `metpo_traitmech_v396`, `brc76_system`,
  `Brc76 system`, `Brc76`, `brc76`, or `gcu76`.
- `rg --no-ignore --hidden` over `data/raw/metpo.owl` found no exact upstream
  METPO term for `Brc76`, `brc76`, or `gcu76`.
- `curl` of the pinned DefenseFinder article registry verified the exact
  `gcu76` row.
- `curl` of the pinned DefenseFinder HMM and rules files found no exact
  `gcu76`, `brc76`, or `Brc76` row.
- `scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v396`
- `scripts/robot_validate_proposal.py proposals/metpo_traitmech_v396`

## Upstream Path

Submit the ROBOT template row to the METPO upstream queue. After METPO mints a
stable replacement for `METPO:1047300`, re-seed TraitMech from the accepted
METPO release, migrate `traitmech:000519` to the upstream CURIE, and retain
`traitmech:000519` as a traceability xref.

## Changelog

- v396, 2026-10: lifts `traitmech:000519 Brc76 system` into the METPO
  placeholder block at `METPO:1047300`.
