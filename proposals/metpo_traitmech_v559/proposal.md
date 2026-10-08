# METPO proposal v559: trichocyst discharge

## Context and scope

Lift `traitmech:000683` as `METPO:1063600`: one physiological phenotype,
kept `PROPOSED` pending human review. Scope A: one class. Scope B: zero
predicates. Scope C: zero schema enums.

Parent: exocytosis `traitmech:000637`, proposed as `METPO:1059000` in v513,
below phenotype `METPO:1000059` and quality `METPO:1000188`. This is a
cargo-specific secretion phenotype, not organelle possession, docking,
fusion without release or in-vitro matrix expansion. Do not require rapid
extrusion, total emptying or a universal calcium threshold. The existing
myzocytosis record's fixation-artifact and prey-capture caveat is not an
equivalent trait or resolved by these experiments. No exact synonym, xref,
SSSOM equivalence, disjointness or universal prey-capture role is asserted.

## Evidence and limits

- [Kerboeuf and Cohen 1990](https://doi.org/10.1083/jcb.111.6.2527),
  PMID:1703537, PMC2116420: scientific abstract and relevant Methods/Results
  OCR directly retrieved from Europe PMC fullTextXML. Figures not inspected.
- [Klauke et al. 1998](https://doi.org/10.1016/s0143-4160(98)90030-6),
  PMID:9681197: [primary PDF](https://d-nb.info/1107191386/34), printed
  pages 351-352 visually checked, including Figures 1-4 and Table 1.
  Wildtype discharge is positive evidence; tnd1 fusion without release
  establishes the boundary. Stored snippet is a contiguous caption span.
- [1993 calcium study](https://doi.org/10.1016/0143-4160(93)90065-e),
  PMID:7684653: scientific abstract directly retrieved by quoted DOI query
  from Europe PMC. Slow extrusion supports omitting a mandatory rapid
  response. Full Methods and figures were not inspected.

Two snippets are scientific-abstract spans, one a visually checked caption,
not search-result text. Preserve the snippet resolver's actual verdicts.
Keep low-calcium injury and fusion/readout distinctions explicit. These
Paramecium experiments do not establish a shared mechanism across all
extrusomes. Natural strain provenance remains unverified: no canonical
examples are assigned. A protein graph is deferred pending direct functional
evidence and taxon-paired accessions, not claimed impossible.

## Allocation and novelty

Reserve **traitmech:000683**, cohort **v559**, and the entire
**METPO:1063600-1063699** block; only 1063600 is populated. This follows
v558's 1063500-1063599 block without overlapping CommunityMech v1 or its
extensions. Subset: `metpo_traitmech_2026_10`.

Allocation main: `a3c8f0ef2a22e0639ca5b24bfe79da4f99f2fafc`.
Ignored-and-hidden searches covered all 20 existing TraitMech worktrees,
the whole CommunityMech checkout and a complete fresh open-PR snapshot:
22 roots. Queries covered trichocyst/extrusome terminology, DOI/PMID/PMC
identifiers, local ID, cohort and full block. The 291 novelty hits reduce
to 17 distinct lines of broader exocytosis and myzocytosis context, not an
equivalent record. All 21 allocation hits were unrelated numbers, not
reservations. Wrapped terminology was also checked. Parsed pinned METPO
has no exact class; obsolete secretion terms are not suitable parents.
Fresh seeding emitted 399 records; 55 exact IDs are absent from the
1,077-record corpus. This is not a missing-work queue or exhaustion proof.

Complete paginated open-head inventory, including drafts, at allocation:

| PR | Head | Reservation |
| --- | --- | --- |
| #1802 | `a74d9278b3ce5971d773a4e81616373f795f2816` | existing Shedu; no new ID/block |
| #1782 | `35099af2b7d5347f2ca6e418c4a139979071644d` | none in changed curation paths |
| #1476 | `a138e46f803b5af9d48969217b86cf7c9a3b61bd` | none in changed curation paths |
| #973 | `331f9517bbdf4d2c9fa97b338ee59a8986f2f174` | none in changed curation paths |
| #924 (draft) | `e61ce120b8da953da097b9f94bfed7f292e5675a` | none in changed curation paths |

Changed-file counts, immutable curation blobs and head stability checked.
Recheck main and reservations before publishing.

## Artifacts and verification

One class TSV has two 11-column headers and one class row. No property or
SSSOM file is needed. Preserve three empty trailing directive cells.
Upstream skill and templates are pinned at
`1408e7099d039026d7611c240938d8e177753406`. Rechecked class blob:
`b590cf303dc2fbdd57bed021668641cd0c32396d`; property blob:
`b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990` (11/13 columns).
CommunityMech v1 provides the worked convention. Use maintained w3id METPO
expansion, not the upstream legacy OBO example.

The pinned ontology does not contain the proposed exocytosis parent.
Compile its existing cohort first, then validate this dependent cohort:

```sh
PYTHONPATH=src .venv/bin/python scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v559
PYTHONPATH=src .venv/bin/python scripts/robot_validate_proposal.py proposals/metpo_traitmech_v513
PYTHONPATH=src .venv/bin/python scripts/robot_validate_proposal.py proposals/metpo_traitmech_v559 --metpo reports/robot/metpo_traitmech_v513/merged.owl
```

Parse the resulting RDF to confirm the labeled, defined parent and chain
1063600 -> 1059000 -> 1000059 -> 1000188 under `https://w3id.org/metpo/`.
A bare parent stub and a successful ELK exit alone are insufficient.
The writer guards both parent-record scope and its proposal identity.
Do not copy or remint the parent in this cohort.

Also require LinkML/strict/history/QC/products, snippet/direct-source checks,
focused/full tests and desktop/mobile browser QA. Record actual outcomes
in the PR receipt rather than asserting success before execution.

## Upstream and round trip

After human signoff submit this TSV together with its v513 dependency to
berkeleybop/metpo, or replace the parent placeholder with its accepted ID
if v513 lands first. No upstream issue or accepted term is claimed.
Following release, refresh the pinned ontology, seed the accepted term and
migrate the local identifier while preserving provenance. Do not emit
either placeholder as a released ID.

## Change log

- v559, 2026-10-08: initial proposal with explicit v513 dependency.
