# METPO proposal v562: haptocyst discharge

## Context and scope

Lift `traitmech:000686` as `METPO:1063900`: one physiological phenotype,
kept `PROPOSED` pending human review. Scope A: one class. Scope B: zero
predicates. Scope C: zero schema enums. This concerns release from haptocysts,
not organelle possession, prey attachment alone or an inferred toxin gene.

## Hierarchy decisions

Parent: phenotype `METPO:1000059`, below quality `METPO:1000188`.
Benwitz reports organelle-plasma-membrane continuity in Ephelota, while
explicitly rejecting predator-prey plasma-membrane fusion in that system.
An exocytotic interpretation there does not establish the fusion-pore
differentia of local exocytosis `traitmech:000637` across the whole class.
That placement is unresolved, not excluded. No v513 dependency is asserted.

Possession, docking, attachment, ingestion and nonspecific cell lysis alone
do not establish discharge. Prey death, complete emptying and one universal
trigger are not required. Toxicyst discharge `traitmech:000685` leaves
historical haptocyst terminology unresolved; this record does not decide
whether broader historical toxicyst classifications encompass haptocysts.
No equivalence to kinetocysts, trichocysts or mucocysts, homology, disjointness,
exact synonyms or xrefs are asserted.

## Evidence and limits

- [Benwitz 1984](https://doi.org/10.1515/znc-1984-7-821): English abstract
  read directly in the [NIES reproduction](https://www.nies.go.jp/chiiki1/protoz/refere/id4999/4538.htm).
  It supports prey-contact discharge and external attachment of internal
  haptocyst structures in Ephelota gemmipara. Crossref confirms the original
  1984 publication, not a later digitization date. The publisher PDF was
  unavailable; no visual full-paper audit is claimed.
- [Bardele and Grell 1967](https://doi.org/10.1007/BF00331480), PMID:4971424:
  publisher English Summary points 1-2 identify haptocysts and describe
  prey attachment in Acineta tuberosa. This is independent identity and
  attachment evidence, not replicate discharge validation. Full text was
  subscription-only and not inspected.

Both snippets are short complete sentences from directly retrieved text,
not search-result quotations. Retain the resolver's actual outcomes.
The evidence does not establish universal cargo chemistry or a conserved
protein pathway. Culture provenance and current strain-level taxonomy remain
unchecked; canonical examples and causal graphs are deferred explicitly.

## Allocation and novelty

Reserve **traitmech:000686**, cohort **v562**, and the whole
**METPO:1063900-1063999** block; only 1063900 is populated. This follows
v561 without overlap with CommunityMech v1 or its extensions.
Subset: `metpo_traitmech_2026_10`.

Allocation main: `1d3950362226bd2780ad3b650f67bf8d930df193`.
Ignored-and-hidden searches covered all 22 existing TraitMech worktrees,
the whole CommunityMech checkout and a fresh complete open-PR snapshot:
24 roots. Haptocyst/haptrocyst/haptocyt/kinetocyst/phialocyst,
missile-like-body and source DOI/PMID queries found 18 boundary mentions
(six distinct lines) in the toxicyst record and its writer/generated copies,
not an exact record, synonymous trait, causal node or same-scope parent TODO.
All 76 allocation matches were unrelated numeric substrings, not reservations.
The pinned METPO RDF has no exact class. Fresh seeding emitted 399 records;
55 exact IDs were absent from the 1,080-record corpus. This is not a missing
work queue or an exhaustion claim.

Complete paginated open-head inventory, including drafts, at allocation:

| PR | Head | Reservation |
| --- | --- | --- |
| #1802 | `a74d9278b3ce5971d773a4e81616373f795f2816` | existing Shedu; no new ID/block |
| #1782 | `35099af2b7d5347f2ca6e418c4a139979071644d` | none in changed curation paths |
| #1476 | `b4b8d1280e25bd3e340241e7ac23b51bbe7aaec3` | none in changed curation paths |
| #973 | `331f9517bbdf4d2c9fa97b338ee59a8986f2f174` | none in changed curation paths |
| #924 (draft) | `e61ce120b8da953da097b9f94bfed7f292e5675a` | none in changed curation paths |

Changed-file counts, immutable curation blobs and head stability checked.
Recheck main and reservations immediately before publication.

## Artifacts and verification

One class TSV contains two 11-column headers and one class row. No property
or SSSOM file is needed. Preserve three empty trailing directive cells.
Upstream skill and templates are pinned at
`1408e7099d039026d7611c240938d8e177753406`. Class blob:
`b590cf303dc2fbdd57bed021668641cd0c32396d`; property blob:
`b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990` (11/13 columns).
CommunityMech v1 supplies the worked convention. Use maintained w3id METPO
expansion, not the upstream legacy OBO example.

```sh
PYTHONPATH=src .venv/bin/python scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v562
PYTHONPATH=src .venv/bin/python scripts/robot_validate_proposal.py proposals/metpo_traitmech_v562
```

Parse RDF to check the labeled parent and chain 1063900 -> 1000059 ->
1000188 under `https://w3id.org/metpo/`. The writer guards the parent-record
identity and scope. Require strict/LinkML/history/QC/products, direct-source
and snippet checks, focused/full tests and desktop/mobile browser QA.
Actual outcomes belong in the PR and structured review, not a pre-execution
assertion.

## Upstream and round trip

After human signoff submit the TSV to berkeleybop/metpo. No upstream issue
or accepted term is claimed. Following release, refresh the pinned ontology,
seed the accepted term and migrate the local identifier while preserving
provenance. Do not present the placeholder as a released ID.

## Change log

- v562, 2026-10-10: initial source-bounded haptocyst-discharge proposal.
