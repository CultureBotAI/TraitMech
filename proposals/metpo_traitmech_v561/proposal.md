# METPO proposal v561: toxicyst discharge

## Context and scope

Lift `traitmech:000685` as `METPO:1063800`: one physiological phenotype,
kept `PROPOSED` pending human review. Scope A: one class. Scope B: zero
predicates. Scope C: zero schema enums. This is release from toxicysts,
not mere possession of an offensive organelle or a predicted toxin gene.

## Hierarchy decisions

Parent: phenotype `METPO:1000059`, below quality `METPO:1000188`.
The exocytosis placement (`traitmech:000637`, v513) is unresolved, not
excluded: the 2024 Background describes telescopic discharge and/or
membrane fusion, whereas its Discussion reports fusion observations.
Those statements do not establish the local fusion-pore differentia
throughout this class. No v513 dependency is asserted.

Prey injury, cell lysis, docking and generic predation alone are insufficient.
Neither prey killing nor complete emptying is required. No equivalence to
mucocyst or trichocyst discharge, pexicysts or haptocysts is asserted.
Historical extrusome terminology remains an explicit curation question;
no exact synonyms, xrefs, SSSOM equivalents or disjointness are assigned.

## Evidence and limits

- [Buonanno et al. 2014](https://doi.org/10.1111/jeu.12106), PMID:24512001:
  direct scientific Abstract supports discharge collected from living
  Coleps. Full Methods and figures were not inspected. Author postprint
  https://hdl.handle.net/11393/192287 is restricted, not a full-text check.
- [Iwadate et al. 1999](https://doi.org/10.1007/BF01279249): publisher Summary
  and author-upload Methods/Results transcript distinguish localized
  calcium-induced discharge from injection damage. Figures were not visually
  inspected. The exact DOI query did not resolve a PMID.
- [Li et al. 2024](https://doi.org/10.1186/s12915-024-01904-2), PMID:38715037,
  PMC11077807: primary text and Figure 1 inspected. A-C are drawings, not
  discharge micrographs. Genomic associations do not establish causality.
  Supplements were not inspected or used for accession-level claims.

All three snippets come from directly retrieved scientific Abstract/Summary
text, not search results. Retain the snippet resolver's actual outcomes.
Natural provenance of positive experimental cultures remains unresolved,
so no canonical examples are assigned. No protein graph is asserted from
gene-family expansion or predicted toxins; mechanism is deferred, not absent.

## Allocation and novelty

Reserve **traitmech:000685**, cohort **v561**, and the whole
**METPO:1063800-1063899** block; only 1063800 is populated. This follows
v560's block without overlap with CommunityMech v1 or its extensions.
Subset: `metpo_traitmech_2026_10`.

Allocation main: `3db67c7159c102e394d2531c7c3866a2d20f03f1`.
Ignored-and-hidden searches covered all 20 existing TraitMech worktrees,
the whole CommunityMech checkout and a fresh complete open-PR snapshot:
22 roots. Toxicyst/toxocyst/pexicyst/haptocyst and all three source
DOI/PMID/PMC queries returned zero matches. All 110 allocation matches
were unrelated numbers, not reservations. Related extrusome mentions in
the two neighboring discharge records do not denote this organelle.
Pinned METPO has no exact class. Fresh seeding emitted 399 records;
55 exact IDs were absent from the 1,079-record corpus. That is not a
missing-work queue or an exhaustion claim.

Complete paginated open-head inventory, including drafts, at allocation:

| PR | Head | Reservation |
| --- | --- | --- |
| #1802 | `a74d9278b3ce5971d773a4e81616373f795f2816` | existing Shedu; no new ID/block |
| #1782 | `35099af2b7d5347f2ca6e418c4a139979071644d` | none in changed curation paths |
| #1476 | `a138e46f803b5af9d48969217b86cf7c9a3b61bd` | none in changed curation paths |
| #973 | `331f9517bbdf4d2c9fa97b338ee59a8986f2f174` | none in changed curation paths |
| #924 (draft) | `e61ce120b8da953da097b9f94bfed7f292e5675a` | none in changed curation paths |

Changed-file counts, immutable curation blobs and head stability checked.
Recheck main and reservations immediately before publication.

## Artifacts and verification

One class TSV contains two 11-column headers and one class row. No property
or SSSOM file is needed. Preserve three empty trailing directive cells.
Upstream skill and templates are pinned at
`1408e7099d039026d7611c240938d8e177753406`. Rechecked class blob:
`b590cf303dc2fbdd57bed021668641cd0c32396d`; property blob:
`b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990` (11/13 columns).
CommunityMech v1 supplies the worked convention. Use maintained w3id METPO
expansion, not the upstream legacy OBO example.

```sh
PYTHONPATH=src .venv/bin/python scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v561
PYTHONPATH=src .venv/bin/python scripts/robot_validate_proposal.py proposals/metpo_traitmech_v561
```

Parse RDF to check the labeled parent and chain 1063800 -> 1000059 ->
1000188 under `https://w3id.org/metpo/`. The writer guards the parent-record
identity and scope. Require strict/LinkML/history/QC/products, direct-source
and snippet checks, focused/full tests and desktop/mobile browser QA.
Actual outcomes belong in the PR receipt, not a pre-execution assertion.

## Upstream and round trip

After human signoff submit the TSV to berkeleybop/metpo. No upstream issue
or accepted term is claimed. Following release, refresh the pinned ontology,
seed the accepted term and migrate the local identifier while preserving
provenance. Do not present the placeholder as a released ID.

## Change log

- v561, 2026-10-08: initial source-bounded toxicyst-discharge proposal.
