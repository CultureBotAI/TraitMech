# METPO proposal v563: kinetocyst discharge

## Context and scope

Lift `traitmech:000687` as `METPO:1064000`: one physiological phenotype,
kept `PROPOSED` pending human review. Scope A: one class. Scope B: zero
predicates. Scope C: zero schema enums. This concerns material release from
kinetocysts, not organelle possession or a sequence-feature interpretation.

## Hierarchy decisions

Parent: phenotype `METPO:1000059`, below quality `METPO:1000188`.
Bardele 1976 interprets kinetocysts as compound motile mucocysts. Preserve
that source-attributed umbrella; the membrane-fusion definition of existing
mucocyst discharge `traitmech:000684` is supported in Tetrahymena and leaves
historical terminology unresolved. Neither exact equivalence nor a mucocyst
parent is established here. Exocytosis `traitmech:000637` requires a fusion
pore; its class-wide placement also remains unresolved, not excluded.

Possession, docking, axopodial movement or contraction, prey adhesion,
ingestion and nonspecific lysis alone do not establish release. Complete
emptying, prey death and a universal trigger are not required. No equivalence
with haptocyst discharge `traitmech:000686`, homology, organism-level
disjointness, exact synonym or xref is asserted. Historical conicyst naming
of an organelle does not automatically establish an exact phenotype synonym.

## Evidence and limits

- [Sakaguchi et al. 2002](https://doi.org/10.1078/0932-4739-00847):
  scientific abstract read directly at
  [ResearchGate](https://www.researchgate.net/publication/222864147).
  Supports discharge during food capture in Raphidiophrys contractilis.
  The proposed scaffold role is not demonstrated causality. Publisher access
  returned 403; full Methods and figures remain unread.
- [Bardele 1976](https://doi.org/10.1515/znc-1976-3-418), PMID:134561:
  abstract and primary full-text OCR read at
  [ResearchGate](https://www.researchgate.net/publication/22999924).
  The snippet supports identity and attachment; the body, pp191-193, reports
  induced release and expelled jacket material. This is distinct from a
  natural-trigger assay. No visual PDF audit or normalized OCR quote is claimed.
- [Wan and Suzaki 2020](https://protistology.jp/journal/congress_ab/53th_kobe/Abstract%20Book%20Kobe2020):
  primary conference abstract O-BPA06/P-1A01, printed pp11-12, visually
  inspected. The snippet gives assay context; the following results describe
  structural extension after discharge. This is not a peer-reviewed full
  article. Protein localization does not establish release-specific necessity.

Short snippets are contiguous source passages, not search-result quotations.
Keep actual automated resolver outcomes distinct from direct-source checks.
Canonical examples await assay-strain provenance verification. No conserved
toxin chemistry or causal protein graph is inferred. These are differently
scoped observations, not three equivalent discharge replications.

## Allocation and novelty

Reserve **traitmech:000687**, cohort **v563**, and the whole
**METPO:1064000-1064099** block; only 1064000 is populated.
Subset: `metpo_traitmech_2026_10`. No CommunityMech v1 overlap.

Allocation main: `3eae095010e35c9773de7f79a3456bd0e48360d0`.
Ignored-and-hidden searches covered all 22 pre-existing TraitMech worktrees.
Kinetocyst, conicyst, variant spellings and both source DOIs found only
haptocyst boundary mentions and their generated/review copies, not an exact
record, exact graph node or same-scope parent TODO. The new ID, cohort and
whole block were also checked across these worktrees and CommunityMech.
Five exact numeric matches were unrelated Science DOI suffixes, not
reservations. The pinned METPO has no exact class. Fresh seeding emitted
399 records, with 55 exact IDs absent from the live 1,081-record corpus;
this is neither a missing-work queue nor an exhaustion claim.

Complete paginated open-head inventory, including drafts, rechecked before
allocation on 2026-10-10:

| PR | Head | Reservation |
| --- | --- | --- |
| #1802 | `a74d9278b3ce5971d773a4e81616373f795f2816` | existing Shedu; no new ID/block |
| #1782 | `35099af2b7d5347f2ca6e418c4a139979071644d` | none in changed curation paths |
| #1476 | `b4b8d1280e25bd3e340241e7ac23b51bbe7aaec3` | none in changed curation paths |
| #973 | `331f9517bbdf4d2c9fa97b338ee59a8986f2f174` | none in changed curation paths |
| #924 (draft) | `e61ce120b8da953da097b9f94bfed7f292e5675a` | none in changed curation paths |

Changed-file lists and immutable curation content were inspected. Recheck
main and reservations immediately before publication.

## Artifacts and verification

One class TSV: two 11-column headers and one class row. No property or SSSOM
file is needed. Preserve the three empty trailing directive cells.
Upstream skill/templates are pinned at
`1408e7099d039026d7611c240938d8e177753406`. Class blob:
`b590cf303dc2fbdd57bed021668641cd0c32396d`; property blob:
`b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990` (11/13 columns).
CommunityMech v1 supplies the worked convention. Use the maintained w3id
METPO expansion, not the upstream legacy OBO example.

```sh
PYTHONPATH=src .venv/bin/python scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v563
PYTHONPATH=src .venv/bin/python scripts/robot_validate_proposal.py proposals/metpo_traitmech_v563
```

Parse RDF to check the labeled parent and chain 1064000 -> 1000059 ->
1000188 under `https://w3id.org/metpo/`. The writer guards the parent-record
identity and scope. Require strict/LinkML/history/QC/products, direct-source
and snippet checks, focused/full tests and desktop/mobile browser QA.
Actual results belong in the PR and structured review, not a pre-execution
success assertion.

## Upstream and round trip

After human signoff submit the TSV to berkeleybop/metpo. No upstream issue
or accepted term is claimed. Following release, refresh the pinned ontology,
seed the accepted term and migrate the local identifier while preserving
provenance. Do not present the placeholder as a released ID.

## Change log

- v563, 2026-10-10: initial source-bounded kinetocyst-discharge proposal.
