# METPO proposal v569: diatom perizonium production

## Context and hierarchy

Lift `traitmech:000693` as `METPO:1064600`: one PHYSIOLOGY CLASS,
kept PROPOSED pending human signoff. Scope A: one class in one record;
B/C: zero. This is production of the siliceous perizonial band system
in a diatom auxospore wall, not a structure or a sequence feature.

Local parent biomineralization `traitmech:000690` entails mineral formation.
The standalone TSV uses its released ancestor phenotype `METPO:1000059`,
below quality `METPO:1000188`. On joint adoption request
`METPO:1064600 SubClassOf METPO:1064300` (v566 biomineralization).
This refinement is explicit in TSV observations; no proposed parent is
silently emitted as a released term. Prior cohorts remain unchanged.

## Boundaries and evidence

Inherited bands, uptake, auxosporulation, incunabular scales, epizonium,
initial valves/girdles and setae alone do not establish this endpoint.
Neither band orientation, both transverse/longitudinal systems, a geometry,
sexual origin, deposition during expansion nor one secretion sequence is
required. Scale-derived bands do not justify universal parenting to scale
production. No organism-level disjointness or fitness effect is inferred.

- [Kaczmarska et al. 2022](https://doi.org/10.1371/journal.pone.0272778),
  PMID:36067191, PMC9447881, is definition authority. Scientific Abstract,
  Introduction, Methods, early Results, Epizonium and perizonium, and
  Discussion: Auxospore structure and development read; actual Figure 11
  inspected. Some layer assignments remain uncertain. Other actual figures
  and S1 Appendix unread.
- [Kaczmarska et al. 2017](https://doi.org/10.1371/journal.pone.0181413),
  PMID:28813426, PMC5558960: scientific Abstract, Methods prose, Auxospore
  wall fine structure, relevant Discussion paragraphs and actual Figure 5
  inspected. Tables 1/2 headers, footnotes and StA:7/8 and Van5:5/6 rows
  read; other rows not fully interpreted. The deposition sequence is
  inferred from fixed stages, not a live time course. Other actual images
  and supplements unread.
- [Mather et al. 2013 online / 2014 issue](https://doi.org/10.1016/j.ejop.2013.06.002),
  PMID:23972513: complete scientific Abstract directly read. Publisher
  full text unavailable; Methods, actual figures and supplements unread.
  Its longitudinal-only interpretation is retained in the 2017 Discussion,
  not one of the other papers' initial-valve interpretations questioned there.

All three official CORE queries used `EXT_ID:<PMID> AND SRC:MED` and
matched ID, source, title and DOI. Each item carries an exact short snippet;
the 2022 Results quote is checked separately from the native abstract
resolver. These primary studies overlap in authorship, not independent-lab
replication. The 2017 paper is already cited for anisogamy terminology,
a different phenotype, not evidence of an exact duplicate.

Canonical taxa are deferred pending taxonomy and exact study-material
assignment, despite having read clone origins. Static structure and
silica labeling do not establish protein causality. Two OPEN discussions
retain exemplar, mechanism and mapping gaps. No exact synonym, xref or
SSSOM mapping is asserted without authority-backed phenotype equivalence;
properizonium terminology remains to be reconciled.

## Allocation and novelty

Reserve `traitmech:000693`, v569, and all of `METPO:1064600-1064699`;
populate only 1064600. Subset `metpo_traitmech_2026_10`. Allocation main:
`33f6efa71a829eac1b54763336057410970c61ff`.

Whole-repository and all 22 pre-existing worktree searches included ignored
and hidden files, identifiers, synonyms, likely slugs, perizoni/perizonal/
properizoni, auxospore band/wall/silica combinations, source species,
all three DOI/PMID values, both PMC values, and broader mineral/diatom/
frustule/scale/reproductive concepts. Relevant hits are neighboring endpoint
boundaries and the anisogamy citation, not exact perizonium traits or unresolved
exact nodes. No existing record requires repair. Whole-block search in
CommunityMech, also ignored-and-hidden, returned no conflicting reservation.

Fresh seeding produced 399 records; 55 IDs absent from 1,087 live records
are 38 supporting properties and 17 previously adjudicated semantic
duplicates. The 12,617-triple ontology, complete 1,546-row release delta,
153-row active-review table and active policy were inspected. No exact
METPO term is available. Neither this bounded search nor seed absence
establishes global exhaustion.

All open PRs, including drafts, were checked using complete paginated changed
files, immutable affected curation blobs and rechecked heads on 2026-10-10:

| PR | Head | Reservation |
| --- | --- | --- |
| #1802 | `a74d9278b3ce5971d773a4e81616373f795f2816` | Existing Shedu 000220; no new allocation |
| #1782 | `35099af2b7d5347f2ca6e418c4a139979071644d` | No curation paths |
| #1476 | `b4b8d1280e25bd3e340241e7ac23b51bbe7aaec3` | No curation paths |
| #973 | `331f9517bbdf4d2c9fa97b338ee59a8986f2f174` | No curation paths |
| #924 (draft) | `e61ce120b8da953da097b9f94bfed7f292e5675a` | No curation paths |

Recheck current main and reservations before publishing. Protected spore
germination and all unowned work are excluded.

## Artifacts and verification

One canonical 11-column class TSV and this narrative; no property/SSSOM
file. The three empty trailing directive cells are intentional. Upstream
contract commit `1408e7099d039026d7611c240938d8e177753406`, class/property
blobs `b590cf303dc2fbdd57bed021668641cd0c32396d` and
`b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990` supply the headers.
CommunityMech's historical 12-column property table is not the canonical
13-column header. Use maintained w3id METPO IRIs, not OBO stubs.

The guarded writer defaults to dry run, checks parent scope, refuses
target/proposal drift, prevalidates and supports exact replay. Require
strict/LinkML, native history/QC/products, proposal/ROBOT/ELK, source/snippet,
focused/full tests, preservation and desktop/mobile rendering checks.
Actual outcomes belong in the PR and immutable review, not assumed here.

## Upstream and round trip

After human signoff submit the TSV and v566 refinement to berkeleybop/metpo.
No upstream acceptance or issue is claimed. After acceptance refresh the
pinned ontology, migrate identifiers and references, preserve minting
provenance and append-only history, and do not retain a duplicate primary.

## Change log

- v569, 2026-10-10: propose diatom perizonium production.
