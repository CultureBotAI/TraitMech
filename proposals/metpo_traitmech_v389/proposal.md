# METPO ROBOT Template Proposal - ScoMcrA System (v389, 2026-10)

## Summary

This cohort reserves `METPO:1046600` for the `ScoMcrA system`, a
genome-level possession trait for ScoMcrA-family Type IV
modification-dependent restriction loci that recognize phosphorothioated DNA.
Liu et al. support ScoA3McrA as a Type IV McrA homolog that cleaves
phosphorothioated DNA and Dcm-methylated DNA in vitro, and a later Liu et al.
paper supports ScoMcrA as a phosphorothioated-DNA-dependent restriction
endonuclease with a sulfur-binding domain and reports SBD homologs that bind
PT-DNA in vitro and restrict PT-DNA gene transfer in vivo. The pinned
DefenseFinder article registry maps `ScoMcrA` to the sulfur-recognition paper,
while the pinned HMM inventory and rules table have no exact ScoMcrA rows.

The local TraitMech fallback is `traitmech:000512` in
`data/traits/genomics/scomcra_system.yaml`. The proposed METPO class sits under
the earlier proposed Type IV parent, `METPO:1045000`.

## Scope

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for ScoMcrA system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no enum lift |

No SSSOM file is emitted because no exact cross-ontology equivalent is proposed.

## Duplicate Review

An ignored-and-hidden duplicate search checked the exact local identifier,
proposal placeholder, proposal cohort, slug, label, DefenseFinder source key,
and DOI strings across the current TraitMech curation corpus. It found no exact
same-scope ScoMcrA record, METPO term, history record, or prior proposal for
`traitmech:000512`, `METPO:1046600`, `scomcra_system`, `ScoMcrA system`,
`ScoMcrA`, or `Structural basis for the recognition of sulfur in
phosphorothioated DNA`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1046600` | ScoMcrA system | `METPO:1045000` type IV modification-dependent restriction system |

ScoMcrA system captures genome-level possession of a ScoMcrA-family Type IV
modification-dependent restriction locus that restricts phosphorothioated DNA
through a sulfur-binding-domain endonuclease. It excludes the broader McrA
family, `EcoKMcrA`, `McrBC`, `GmrSD`, `MspJI`, `PvuRts1I`, `TagI`, `VcaM4I`,
broad `RM_Type_IV` and `Other_Type_IV` source keys, individual ScoMcrA
proteins, individual sulfur-binding domains, individual `mcrA` genes, ScoMcrA
nuclease activity outside a complete organism-level Type IV restriction system,
individual phosphorothioated DNA substrates, and the DefenseFinder `ScoMcrA`
source key outside a complete organism-level system.

`ScoMcrA` is proposed as a related synonym because it is the source-system
article key and the enzyme name, not by itself the full organism-level system
possession label.

## Mappings

No exact external mapping is proposed. Individual ScoMcrA proteins, individual
`mcrA` genes, the broader McrA family, specific phosphorothioated DNA substrate
classes, and the DefenseFinder `ScoMcrA` source key are narrower or shifted
relative to the organism-level ScoMcrA system trait.

## Verification

- `rg --no-ignore --hidden` found no collision for `traitmech:000512`,
  `METPO:1046600`, `METPO:10466xx`, `metpo_traitmech_v389`,
  `scomcra_system`, `ScoMcrA system`, or DOI
  `10.1038/s41467-018-07093-1`.
- `curl` of the pinned DefenseFinder article registry verified the exact
  `ScoMcrA` row.
- `curl` of the pinned DefenseFinder HMM and rules files found no exact
  `ScoMcrA` row.
- `scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v389`
- `scripts/robot_validate_proposal.py proposals/metpo_traitmech_v389`

## Upstream Path

Submit the ROBOT template row to the METPO upstream queue. After METPO mints a
stable replacement for `METPO:1046600`, re-seed TraitMech from the accepted
METPO release, migrate `traitmech:000512` to the upstream CURIE, and retain
`traitmech:000512` as a traceability xref.

## Changelog

- v389, 2026-10: lifts `traitmech:000512 ScoMcrA system` into the
  METPO placeholder block at `METPO:1046600`.
