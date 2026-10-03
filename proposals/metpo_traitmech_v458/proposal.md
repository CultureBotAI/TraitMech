# METPO Proposal v458: Galvanotaxis

## Context

This cohort lifts `traitmech:000581 galvanotaxis`, a motile phenotype defined
by electric-field-guided active movement. Passive electrophoretic drift is
insufficient. Primary sources are Adler and Shi
(DOI:10.1101/sqb.1988.053.01.006), Shi et al.
(DOI:10.1128/jb.178.4.1113-1119.1996), and Sun et al.
(DOI:10.1038/s41564-024-01778-8).

Fresh temporary seeding emitted 399 identifiers: 344 present and 55 absent
from the 975-record pre-change corpus. Both frozen release-review tables were
inspected. Whole-repository novelty and allocation searches included ignored
and hidden files, OWL, history, research, proposals and pages. A cable-bacteria
research report mentions electrotaxis as a lead, not an exact TraitRecord.
No existing exact trait or METPO class was found.

## Scope

| Scope | Rows | Parent | Leaves |
|---|---:|---|---:|
| A: local trait lift | 1 | motile | 1 |
| B: predicates | 0 | Existing relations suffice | 0 |
| C: schema enums | 0 | Not biological trait proposals | 0 |

## Hierarchy Decisions

| Proposed ID | Local ID | Label | Parent |
|---|---|---|---|
| METPO:1053500 | traitmech:000581 | galvanotaxis | METPO:1000702 |

The reviewed `motile` parent denotes independent energy-dependent movement.
An electric field biases that active movement; it need not supply the energy
for locomotion. Chemotaxis and magnetotaxis have different stimuli and are not
parents. PHYSIOLOGY follows the behavioral scope. No older record is edited.

## Evidence And Mapping Boundaries

- The 1988 publisher's free Excerpt supports the definition and either-pole
  direction; its paywalled full text was not accessed. The 1996 primary abstract
  supports anode-directed rough K-12 swimming and surface-composition effects;
  its full text was not accessed either.
- Sun et al.'s publisher Version of Record, dated August 20, 2024, was read,
  including Figure 5, Methods and Extended Data. Supplementary Table 1 was
  rendered and inspected. IR715 is a 14028S derivative; Green ST additionally
  carries pGFT/RalFc. The separate SW473 fliC/fljB double mutant informs the
  graph, not the positive behavioral example. No video was viewed.
- The graph covers a flagellar-motility branch, not a proven electrical sensor
  or a complete orientation mechanism. Deleting both flagellins does not prove
  individual FliC necessity. Host CFTR is not a microbial graph protein.
- InterPro IPR001492 resolves to the Flagellin family, not merely a terminal
  domain. Its [family description](https://www.ebi.ac.uk/interpro/entry/InterPro/IPR001492/)
  supports the structural filament contribution. GO:0071973 resolves at
  QuickGO to bacterial-type flagellum-dependent cell motility.
- EBI's Proteins API resolves A0A0F6B2U2 to unreviewed 14028S FliC, entry
  version 42, sequence version 1. The live UniProt proteome endpoint confirms
  reference proteome UP000002695. UniProtKB REST protein requests failed;
  this alternative authority check is not a successful full REST audit.
- NCBI resolves 83333 to E. coli K-12 and 588858 to Salmonella enterica subsp.
  enterica serovar Typhimurium str. 14028S. Do not substitute LT2.
- QuickGO searches for galvanotaxis and electrotaxis found no exact term.
  MeSH Taxis Response is broader. No exact xref, SSSOM mapping or unsupported
  exact synonym is asserted.
- The source workbook's `Fig. 5d,e` cosine signs differ from the published
  text and Figure 5d, while its direction labels agree. An open discussion
  records this coordinate-convention question; no numerical directedness
  values are imported or correction inferred. Another discussion records
  limits of the proposed charge/orientation mechanism.

Authority checks were performed on October 3, 2026. Each of the seven evidence
items has a contiguous snippet; interpretation is confined to notes.

## ID Space And Subset

Reserve `METPO:1053500-1053599`, using only `1053500`, after v457's
`1053400` block. Ignored-and-hidden collision searches found no prior local
ID, cohort or block allocation. This does not intersect CommunityMech v1
`1007100-1007220`. Subset: `metpo_traitmech_2026_10`. These are proposal
placeholders, not released METPO identities.

## Files

| File | Data rows |
|---|---:|
| metpo_proposal_classes_robot.tsv | 1 |
| proposal.md | Narrative |
| Properties and SSSOM | Omitted: no predicate or equivalent mapping |

The 11-column header follows the live kg-microbe master class template.
Its three trailing empty ROBOT header cells are required.

## Verification

Run `scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v458`,
`scripts/robot_validate_proposal.py proposals/metpo_traitmech_v458` and
`scripts/verify_metpo_proposal.py --coverage`. The PR records actual validation,
direct source matching, authority checks and page inspection results.

## Upstream Path

Submit the verified TSV to berkeleybop/metpo after TraitMech review. The local
proposal does not establish upstream acceptance or a minted METPO identifier.

## Round-Trip Plan

After acceptance, refresh METPO, seed a temporary tree and migrate to the
released identifier. Preserve `traitmech:000581` in provenance, update the
graph trait node and regenerate affected artifacts. Do not emit the placeholder
as a released METPO ID before migration.

## Change Log

- v458, 2026-10-03: add galvanotaxis, qualified canonical examples and a
  source-bounded flagellar-motility graph.
