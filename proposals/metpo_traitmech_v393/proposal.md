# METPO ROBOT Template Proposal - Brc24 System (v393, 2026-10)

## Summary

This cohort reserves `METPO:1047000` for `Brc24 system`, a genome-level
possession trait for the `gcu24`/`brc24` bacteriophage-resistance integron
cassette identified by Kieffer et al. in a mobile-integron phage-resistance
screen.

The local TraitMech fallback is `traitmech:000516` in
`data/traits/genomics/brc24_system.yaml`. The proposed METPO class sits under
the earlier proposed phage-defense parent, `METPO:1016300`.

## Scope

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Brc24 system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no enum lift |

No SSSOM file is emitted because no exact cross-ontology equivalent is proposed.

## Duplicate Review

An ignored-and-hidden duplicate search checked the exact local identifier,
proposal placeholder, proposal cohort, placeholder block, slug, label,
DefenseFinder source key, and Brc/gcu strings across the current TraitMech
curation corpus. It found no exact same-scope Brc24 record, METPO term, history
record, or prior proposal for `traitmech:000516`, `METPO:1047000`,
`METPO:10470xx`, `metpo_traitmech_v393`, `brc24_system`, `Brc24 system`,
`Brc24`, or `brc24`. The exact `gcu24` search found only the pinned
DefenseFinder row and Brc142 source snippets that name the shared first screen;
those are not same-scope Brc24 records.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1047000` | Brc24 system | `METPO:1016300` phage defense system |

Brc24 system captures genome-level possession of a gcu24/Brc24
bacteriophage-resistance integron cassette that supports host growth during
phage challenge. It excludes individual Brc24 proteins, `brc24` nucleotide
sequences, `attC` sites, source database rows naming one `gcu24` model,
DefenseFinder HMM or rules profiles absent from the pinned snapshot, the
broader class of Bacteriophage Resistance integron Cassettes, and other mobile
integron phage-defense cassettes.

`gcu24` and `brc24` are proposed as related synonyms because they name the
source cassette and DefenseFinder article key, not the full organism-level
system possession trait.

## Mappings

No exact external mapping is proposed. Individual Brc24 proteins, exact
`brc24` nucleotide sequences, `attC` sites, broad BRiC families, and the
DefenseFinder `gcu24` source key are narrower or shifted relative to the
organism-level Brc24 system trait.

## Verification

- `rg --no-ignore --hidden` found no collision for `traitmech:000516`,
  `METPO:1047000`, `METPO:10470xx`, `metpo_traitmech_v393`,
  `brc24_system`, `Brc24 system`, `Brc24`, or `brc24`.
- `rg --no-ignore --hidden` over `data/raw/metpo.owl` found no exact upstream
  METPO term for `Brc24`, `brc24`, or `gcu24`.
- `curl` of the pinned DefenseFinder article registry verified the exact
  `gcu24` row.
- `curl` of the pinned DefenseFinder HMM and rules files found no exact
  `gcu24`, `brc24`, or `Brc24` row.
- `scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v393`
- `scripts/robot_validate_proposal.py proposals/metpo_traitmech_v393`

## Upstream Path

Submit the ROBOT template row to the METPO upstream queue. After METPO mints a
stable replacement for `METPO:1047000`, re-seed TraitMech from the accepted
METPO release, migrate `traitmech:000516` to the upstream CURIE, and retain
`traitmech:000516` as a traceability xref.

## Changelog

- v393, 2026-10: lifts `traitmech:000516 Brc24 system` into the METPO
  placeholder block at `METPO:1047000`.
