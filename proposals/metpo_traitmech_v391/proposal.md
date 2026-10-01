# METPO ROBOT Template Proposal - VcaM4I System (v391, 2026-10)

## Summary

This cohort reserves `METPO:1046800` for the `VcaM4I system`, a
genome-level possession trait for VcaM4I-family Type IV
modification-dependent restriction loci that encode EVE-HNH endonucleases
recognizing 5mC/5hmC-modified DNA. Mierzejewska et al. support VcaM4I as an
EVE-HNH modification-dependent restriction endonuclease, report structures of
the apo enzyme and modified-DNA-bound complexes, and validate EVE and HNH
residue roles through digestion and restriction assays. The pinned
DefenseFinder article registry maps `VcaM4I` to that structural paper, while
the pinned HMM inventory and rules table have no exact VcaM4I rows.

The local TraitMech fallback is `traitmech:000514` in
`data/traits/genomics/vcam4i_system.yaml`. The proposed METPO class sits under
the earlier proposed Type IV parent, `METPO:1045000`.

## Scope

| Scope | Rows | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for VcaM4I system |
| B - causal-graph predicate lift | 0 | no new predicate |
| C - schema enum lift | 0 | no enum lift |

No SSSOM file is emitted because no exact cross-ontology equivalent is proposed.

## Duplicate Review

An ignored-and-hidden duplicate search checked the exact local identifier,
proposal placeholder, proposal cohort, placeholder block, slug, label,
DefenseFinder source key, DOI, and PMID strings across the current TraitMech
curation corpus. It found no exact same-scope VcaM4I record, METPO term,
history record, or prior proposal for `traitmech:000514`, `METPO:1046800`,
`METPO:10468xx`, `vcam4i_system`, `VcaM4I system`, `VcaM4I`,
`10.1093/nar/gkaa1218`, or `PMID:33450012`.

## Proposed Class

| Proposed ID | Label | Parent |
|---|---|---|
| `METPO:1046800` | VcaM4I system | `METPO:1045000` type IV modification-dependent restriction system |

VcaM4I system captures genome-level possession of a VcaM4I-family Type IV
modification-dependent restriction locus that restricts 5mC/5hmC-modified DNA
through an EVE-HNH endonuclease. It excludes the broader McrA family,
`EcoKMcrA`, `McrBC`, `GmrSD`, `MspJI`, `PvuRts1I`, `ScoMcrA`, `TagI`, broad
`RM_Type_IV` and `Other_Type_IV` source keys, individual VcaM4I proteins,
individual EVE or HNH domains, VcaM4I nuclease activity outside a complete
organism-level Type IV restriction system, individual 5mC/5hmC DNA substrates,
and the DefenseFinder `VcaM4I` source key outside a complete organism-level
system.

`VcaM4I` is proposed as a related synonym because it is the source-system
article key and the enzyme name, not by itself the full organism-level system
possession label.

## Mappings

No exact external mapping is proposed. Individual VcaM4I proteins, individual
EVE or HNH domains, specific methylated DNA substrate classes, and the
DefenseFinder `VcaM4I` source key are narrower or shifted relative to the
organism-level VcaM4I system trait.

## Verification

- `rg --no-ignore --hidden` found no collision for `traitmech:000514`,
  `METPO:1046800`, `METPO:10468xx`, `metpo_traitmech_v391`,
  `vcam4i_system`, `VcaM4I system`, DOI `10.1093/nar/gkaa1218`, or
  `PMID:33450012`.
- `rg --no-ignore --hidden` over `data/raw/metpo.owl` found no exact upstream
  METPO term for `VcaM4I` or `EVE-HNH`.
- `curl` of the pinned DefenseFinder article registry verified the exact
  `VcaM4I` row.
- `curl` of the pinned DefenseFinder HMM and rules files found no exact
  `VcaM4I` row.
- `scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v391`
- `scripts/robot_validate_proposal.py proposals/metpo_traitmech_v391`

## Upstream Path

Submit the ROBOT template row to the METPO upstream queue. After METPO mints a
stable replacement for `METPO:1046800`, re-seed TraitMech from the accepted
METPO release, migrate `traitmech:000514` to the upstream CURIE, and retain
`traitmech:000514` as a traceability xref.

## Changelog

- v391, 2026-10: lifts `traitmech:000514 VcaM4I system` into the METPO
  placeholder block at `METPO:1046800`.
