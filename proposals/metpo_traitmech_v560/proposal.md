# METPO proposal v560: mucocyst discharge

## Context and scope

Lift `traitmech:000684` as `METPO:1063700`: one physiological phenotype,
kept `PROPOSED` pending human review. Scope A: one class. Scope B: zero
predicates. Scope C: zero schema enums.

Parent: exocytosis `traitmech:000637`, proposed as `METPO:1059000` in v513,
below phenotype `METPO:1000059` and quality `METPO:1000188`. This is
mucocyst cargo release, not organelle possession, biogenesis, docking or
fusion without release. Rapid expansion and complete emptying are not
universal requirements. The 2022 primary Discussion calls Paramecium
trichocysts mucocyst homologs; homology does not establish exact equivalence
of these organelle-specific release phenotypes. Do not assert independent
origins or disjointness from trichocyst discharge `traitmech:000683`.
Historical extrusome terminology remains a curation question. Not all mucus
secretion or capsule formation is mucocyst discharge. No exact synonyms,
xrefs, SSSOM equivalents or universal ecological role are asserted.

## Evidence and limits

- [Kuppannan et al. 2022](https://doi.org/10.1371/journal.pgen.1010194),
  PMID:35587496, PMC9159632: scientific Abstract, relevant Results/Methods
  and Discussion directly read. Figure 1 and caption visually inspected;
  Figure 4 caption, not image, read. Sedimented secretion volume is an
  assay proxy, not an organelle-discharge count. S1 Table DOCX text was
  inspected, not rendered; strain entries do not resolve natural provenance.
- [Satir 1977](https://doi.org/10.1016/0309-1651(77)90012-1), PMID:610868:
  scientific Abstract directly retrieved with `EXT_ID:610868 AND SRC:MED`.
  An unqualified numeric query also matches an unrelated record in a
  different database. DOI, title and MED source were checked together.
  Dibucaine-induced synchronous secretion is assay-specific. Full Methods
  and figures were not inspected; retain source spelling of the organism.
- [Kumar et al. 2015](https://doi.org/10.1128/ec.00058-15), PMID:26092918,
  PMC4519746: scientific Abstract directly retrieved by quoted DOI query.
  CTH4-disrupted cells assemble cores but extrude them inefficiently,
  distinguishing assembly from discharge. Full text access failed; Methods,
  figures and supplements were not inspected. This is not a positive
  mutant exemplar or a claim that every cargo component is retained.

All three stored snippets are contiguous scientific-abstract spans checked
against directly retrieved primary text, not search-result text. Preserve
the maintained resolver's actual outcomes. Natural strain provenance is
unresolved, so no canonical examples are assigned. Mechanism is deferred,
not claimed absent: a protein graph requires accession/taxon anchors and
separation of maturation, docking, fusion and extrusion. Sequence features
alone do not demonstrate discharge.

## Allocation and novelty

Reserve **traitmech:000684**, cohort **v560**, and the entire
**METPO:1063700-1063799** block; only 1063700 is populated. This follows
v559's 1063600-1063699 block without overlapping CommunityMech v1 or its
extensions. Subset: `metpo_traitmech_2026_10`.

Allocation main: `3c559770b471b8a1214dcb946a170987ba1ac69a`.
Ignored-and-hidden searches covered all 20 existing TraitMech worktrees,
the whole CommunityMech checkout and a complete fresh open-PR snapshot:
22 roots. Queries covered mucocyst terminology, DOI/PMID/PMC identifiers,
local ID, cohort and full block. Expanded source queries returned the same
77 novelty matches: broader exocytosis context and unrelated numbers, not
an exact record. All 72 allocation matches were unrelated numbers, not
reservations. Wrapped mucus/capsule terminology was checked separately.
Pinned METPO has no exact class. Fresh seeding emitted 399 records; 55 exact
IDs are absent from the 1,078-record corpus. This is not a missing-work
queue or an exhaustion claim.

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
CommunityMech v1 supplies the worked convention. Use maintained w3id METPO
expansion, not the upstream legacy OBO example.

Compile the proposed exocytosis parent before this dependent cohort:

```sh
PYTHONPATH=src .venv/bin/python scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v560
PYTHONPATH=src .venv/bin/python scripts/robot_validate_proposal.py proposals/metpo_traitmech_v513
PYTHONPATH=src .venv/bin/python scripts/robot_validate_proposal.py proposals/metpo_traitmech_v560 --metpo reports/robot/metpo_traitmech_v513/merged.owl
```

Parse the resulting RDF to confirm the labeled, defined parent and chain
1063700 -> 1059000 -> 1000059 -> 1000188 under `https://w3id.org/metpo/`.
A bare parent stub and a successful ELK exit alone are insufficient.
The writer guards both parent-record scope and its proposal identity.
Do not copy or remint the parent in this cohort.

Also require strict/LinkML/history/QC/products, snippet/direct-source checks,
focused/full tests and desktop/mobile browser QA. Actual outcomes belong
in the PR receipt, not a pre-execution assertion.

## Upstream and round trip

After human signoff submit this TSV with its v513 dependency to
berkeleybop/metpo, or replace the parent placeholder with its accepted ID
if v513 lands first. No upstream issue or accepted term is claimed.
Following release, refresh the pinned ontology, seed the accepted term and
migrate the local identifier while preserving provenance. Do not emit
either placeholder as a released ID.

## Change log

- v560, 2026-10-08: initial proposal with explicit v513 dependency.
