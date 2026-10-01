# METPO ROBOT Template Proposal - Brc217 System (v398, 2026-10)

## Summary

This cohort reserves `METPO:1047500` for `Brc217 system`, a genome-level
possession trait for the `gcu217`/`brc217` bacteriophage-resistance integron
cassette tested by Kieffer et al. in mobile-integron BRiC phage-resistance
panels.

The local TraitMech fallback is `traitmech:000521` in
`data/traits/genomics/brc217_system.yaml`. The proposed METPO class sits
under the earlier proposed phage-defense parent, `METPO:1016300`.

## Scope

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Brc217 system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no enum lift |

No SSSOM file is emitted because no exact cross-ontology equivalent is
proposed.

## Duplicate Review

An ignored-and-hidden duplicate search checked the exact local identifier,
proposal placeholder, proposal cohort, slug, label, Kieffer source keys, and
Brc/gcu strings across the current TraitMech curation corpus. It found no exact
same-scope Brc217 record, METPO term, history record, or prior proposal for
`traitmech:000521`, `METPO:1047500`, `metpo_traitmech_v398`,
`brc217_system`, `Brc217 system`, `Brc217`, `brc217`, or `gcu217`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1047500` | Brc217 system | `METPO:1016300` phage defense system |

Brc217 system captures genome-level possession of a gcu217/Brc217
bacteriophage-resistance integron cassette that supports host growth during
phage challenge. It excludes individual Brc217 proteins, `brc217` nucleotide
sequences, `attC` sites, absent source database rows naming `gcu217`, absent
DefenseFinder HMM/rules profiles, broad BRiC families, and other mobile
integron phage-defense cassettes.

`gcu217` and `brc217` are proposed as related synonyms because they name the
source cassette and Brc key, not the full organism-level system possession
trait.

## Mappings

No exact external mapping is proposed. Individual Brc217 proteins, exact
`brc217` nucleotide sequences, `attC` sites, broad BRiC families, and the raw
`gcu217` source key are narrower or shifted relative to the organism-level
Brc217 system trait.

## Verification

- `rg --no-ignore --hidden` found no collision for `traitmech:000521`,
  `METPO:1047500`, `metpo_traitmech_v398`, `brc217_system`,
  `Brc217 system`, `Brc217`, `brc217`, or `gcu217`.
- `rg --no-ignore --hidden` over `data/raw/metpo.owl` found no exact upstream
  METPO term for `Brc217`, `brc217`, or `gcu217`.
- The pinned DefenseFinder article registry, HMM inventory, and rules files
  have no exact `gcu217`, `brc217`, or `Brc217` row.
- `scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v398`
- `scripts/robot_validate_proposal.py proposals/metpo_traitmech_v398`

## Upstream Path

Submit the ROBOT template row to the METPO upstream queue. After METPO mints a
stable replacement for `METPO:1047500`, re-seed TraitMech from the accepted
METPO release, migrate `traitmech:000521` to the upstream CURIE, and retain
`traitmech:000521` as a traceability xref.

## Changelog

- v398, 2026-10: lifts `traitmech:000521 Brc217 system` into the METPO
  placeholder block at `METPO:1047500`.
