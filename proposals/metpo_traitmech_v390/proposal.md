# METPO ROBOT Template Proposal - TagI System (v390, 2026-10)

## Summary

This cohort reserves `METPO:1046700` for the `TagI system`, a
genome-level possession trait for TagI-family Type IV
modification-dependent restriction loci that encode SRA-HNH endonucleases
recognizing 5mC/5hmC-modified DNA. Kisiala et al. support TagI as a member
of the SRA-HNH modification-dependent restriction endonuclease family,
report dimeric TagI structure with nuclease and modified-base-binding sites,
and connect TagI modified-base preference to biochemical modification
dependence and phage restriction assays. The pinned DefenseFinder article
registry maps `TagI` to that structural paper, while the pinned HMM inventory
and rules table have no exact TagI rows.

The local TraitMech fallback is `traitmech:000513` in
`data/traits/genomics/tagi_system.yaml`. The proposed METPO class sits under
the earlier proposed Type IV parent, `METPO:1045000`.

## Scope

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for TagI system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no enum lift |

No SSSOM file is emitted because no exact cross-ontology equivalent is proposed.

## Duplicate Review

An ignored-and-hidden duplicate search checked the exact local identifier,
proposal placeholder, proposal cohort, slug, label, DefenseFinder source key,
and DOI/PMID strings across the current TraitMech curation corpus. It found no
exact same-scope TagI record, METPO term, history record, or prior proposal for
`traitmech:000513`, `METPO:1046700`, `tagi_system`, `TagI system`,
`TagI`, `10.1093/nar/gky781`, or `PMID:30202937`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1046700` | TagI system | `METPO:1045000` type IV modification-dependent restriction system |

TagI system captures genome-level possession of a TagI-family Type IV
modification-dependent restriction locus that restricts 5mC/5hmC-modified DNA
through an SRA-HNH endonuclease. It excludes the broader McrA family, `VcaM4I`,
`EcoKMcrA`, `McrBC`, `GmrSD`, `MspJI`, `PvuRts1I`, `ScoMcrA`, broad
`RM_Type_IV` and `Other_Type_IV` source keys, individual TagI proteins,
individual SRA or HNH domains, TagI nuclease activity outside a complete
organism-level Type IV restriction system, individual 5mC/5hmC DNA substrates,
and the DefenseFinder `TagI` source key outside a complete organism-level
system.

`TagI` is proposed as a related synonym because it is the source-system article
key and the enzyme name, not by itself the full organism-level system
possession label.

## Mappings

No exact external mapping is proposed. Individual TagI proteins, individual SRA
or HNH domains, specific methylated DNA substrate classes, and the
DefenseFinder `TagI` source key are narrower or shifted relative to the
organism-level TagI system trait.

## Verification

- `rg --no-ignore --hidden` found no collision for `traitmech:000513`,
  `METPO:1046700`, `METPO:10467xx`, `metpo_traitmech_v390`, `tagi_system`,
  `TagI system`, DOI `10.1093/nar/gky781`, or `PMID:30202937`.
- `rg --no-ignore --hidden` over `data/raw/metpo.owl` found no exact upstream
  METPO term for `TagI` or `SRA-HNH`.
- `curl` of the pinned DefenseFinder article registry verified the exact
  `TagI` row.
- `curl` of the pinned DefenseFinder HMM and rules files found no exact `TagI`
  row.
- `scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v390`
- `scripts/robot_validate_proposal.py proposals/metpo_traitmech_v390`

## Upstream Path

Submit the ROBOT template row to the METPO upstream queue. After METPO mints a
stable replacement for `METPO:1046700`, re-seed TraitMech from the accepted
METPO release, migrate `traitmech:000513` to the upstream CURIE, and retain
`traitmech:000513` as a traceability xref.

## Changelog

- v390, 2026-10: lifts `traitmech:000513 TagI system` into the METPO
  placeholder block at `METPO:1046700`.
