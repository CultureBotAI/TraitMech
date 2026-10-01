# METPO ROBOT Template Proposal - Brc167 System (v394, 2026-10)

## Summary

This cohort reserves `METPO:1047100` for `Brc167 system`, a genome-level
possession trait for the `gcu167`/`brc167` bacteriophage-resistance integron
cassette tested by Kieffer et al. in mobile-integron BRiC phage-resistance
panels.

The local TraitMech fallback is `traitmech:000517` in
`data/traits/genomics/brc167_system.yaml`. The proposed METPO class sits under
the earlier proposed phage-defense parent, `METPO:1016300`.

## Scope

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Brc167 system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no enum lift |

No SSSOM file is emitted because no exact cross-ontology equivalent is proposed.

## Duplicate Review

An ignored-and-hidden duplicate search checked the exact local identifier,
proposal placeholder, proposal cohort, placeholder block, slug, label,
DefenseFinder source key, and Brc/gcu strings across the current TraitMech
curation corpus. It found no exact same-scope Brc167 record, METPO term,
history record, or prior proposal for `traitmech:000517`, `METPO:1047100`,
`METPO:10471xx`, `metpo_traitmech_v394`, `brc167_system`, `Brc167 system`,
`Brc167`, `brc167`, or `gcu167`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1047100` | Brc167 system | `METPO:1016300` phage defense system |

Brc167 system captures genome-level possession of a gcu167/Brc167
bacteriophage-resistance integron cassette that supports host growth during
phage challenge. It excludes individual Brc167 proteins, `brc167` nucleotide
sequences, `attC` sites, source database rows naming one `gcu167` model,
DefenseFinder HMM or rules profiles absent from the pinned snapshot, the
broader class of Bacteriophage Resistance integron Cassettes, and other mobile
integron phage-defense cassettes.

`gcu167` and `brc167` are proposed as related synonyms because they name the
source cassette and DefenseFinder article key, not the full organism-level
system possession trait.

## Mappings

No exact external mapping is proposed. Individual Brc167 proteins, exact
`brc167` nucleotide sequences, `attC` sites, broad BRiC families, and the
DefenseFinder `gcu167` source key are narrower or shifted relative to the
organism-level Brc167 system trait.

## Verification

- `rg --no-ignore --hidden` found no collision for `traitmech:000517`,
  `METPO:1047100`, `METPO:10471xx`, `metpo_traitmech_v394`,
  `brc167_system`, `Brc167 system`, `Brc167`, `brc167`, or `gcu167`.
- `rg --no-ignore --hidden` over `data/raw/metpo.owl` found no exact upstream
  METPO term for `Brc167`, `brc167`, or `gcu167`.
- `curl` of the pinned DefenseFinder article registry verified the exact
  `gcu167` row.
- `curl` of the pinned DefenseFinder HMM and rules files found no exact
  `gcu167`, `brc167`, or `Brc167` row.
- `scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v394`
- `scripts/robot_validate_proposal.py proposals/metpo_traitmech_v394`

## Upstream Path

Submit the ROBOT template row to the METPO upstream queue. After METPO mints a
stable replacement for `METPO:1047100`, re-seed TraitMech from the accepted
METPO release, migrate `traitmech:000517` to the upstream CURIE, and retain
`traitmech:000517` as a traceability xref.

## Changelog

- v394, 2026-10: lifts `traitmech:000517 Brc167 system` into the METPO
  placeholder block at `METPO:1047100`.
