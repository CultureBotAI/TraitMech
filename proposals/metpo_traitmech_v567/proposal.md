# METPO proposal v567: diatom frustule production

## Context and scope

Lift `traitmech:000691` as `METPO:1064400`: one PHYSIOLOGY class,
kept PROPOSED pending human signoff. Scope A: one class; B/C: zero.
The phenotype is formation of the siliceous valve and girdle-band elements
of a diatom cell wall, not a material frustule, organelle, sequence feature
or generic organism-chemical production pair.

## Hierarchy and boundaries

The local direct parent is biomineralization `traitmech:000690`, whose
definition covers mineral formation. Its released METPO ancestor is
phenotype `METPO:1000059`, below quality `METPO:1000188`. The standalone
TSV uses that released ancestor because v566's `METPO:1064300` is only a
proposal, not a class in the pinned ontology. On adoption with v566, also
request `METPO:1064400 SubClassOf METPO:1064300`. This refinement is stated
explicitly in the narrative and TSV observations; it is not emitted by this
standalone template. Do not re-emit or change the historical v566 reservation.

The scope is newly formed wall elements, not an inherited valve, silica
uptake, adsorption, an isolated shell or a preformed particle. It does not
require both valves to be made anew in one division or every wall element
to be produced simultaneously. Scales, auxospore coverings and setae alone
do not establish valve/girdle formation. The existing siliceous-scale
record explicitly distinguishes frustule formation; that historical scope
note is not an unresolved exact graph grounding or synonym to move.
No existing trait YAML changes. No organism-level disjointness, universal
geometry, intracellular route for all diatom silica, cell-cycle schedule
or fitness benefit is asserted. No synonyms, xrefs or SSSOM mappings are
added without authority-backed equivalence review.

## Evidence and limits

- [Bedoshvili et al.](https://doi.org/10.1007/s00709-017-1199-4),
  PMID:29270874: online 2017-12-21, journal issue May 2018. Definition
  authority and pennate-diatom formation evidence. Complete scientific
  Abstract directly read at https://pubmed.ncbi.nlm.nih.gov/29270874/ and
  in source-qualified Europe PMC CORE. It identifies valves and girdle
  bands as frustule components and reports microscopy of morphogenesis in
  Encyonema ventricosum. Full Methods, figures and supplements remain unread;
  cytoskeletal proximity is not evidence of molecular necessity.
- [Aram et al. 2024](https://doi.org/10.1038/s41467-024-52211-x),
  PMID:39251596, PMC11385223: the snippet is from the Introduction, not the
  abstract. Scientific Abstract, Introduction, Results, Discussion and
  Methods directly read in official Europe PMC XML; actual Figure 2
  inspected. Other actual figures and supplements remain unread. Silicon
  starvation/resupply and cryoET support valve formation in CCMP1335.
  Figure 2 is an inferred sequence across cells, not live longitudinal
  imaging. Current strain taxonomy is not assigned from the paper's
  historical Thalassiosira pseudonana/Cyclotella nana naming. Contact-site
  transport and membrane molding remain proposed functions, not established
  universal causal mechanisms.

Both PMID queries used `EXT_ID:<PMID> AND SRC:MED`, with one exact returned
MED record and matching DOI/title. Both evidence items have short contiguous
source snippets. Native abstract-verifier outcomes must remain distinct from
the manual full-text check. No canonical taxon or protein accession is added.
Mappings and exemplar/mechanism work remain in two OPEN discussions.

## Allocation and novelty

Reserve `traitmech:000691`, cohort v567 and the complete
`METPO:1064400-1064499` block; populate only 1064400. Subset:
`metpo_traitmech_2026_10`. Allocation main:
`156c7ea2c30315372d7c5078d0dd578839b12da8`.

Ignored-and-hidden searches covered the entire repository and all 22
pre-existing worktrees. Terms included frustule variants, diatoms,
silicification, siliceous cell walls, girdle bands, valve production/
formation/morphogenesis, both cited DOI/PMID values, the 2024 PMC accession,
and the additional 2021 extracellular-silica research lead. Local ID,
cohort and full numeric block were also checked. Broader hits are existing
scale/mineral production, reproductive traits, feeding on diatoms and
organoheterotrophy research, plus their generated/history representations;
none is the same production endpoint. The 2021 source remains a research
lead and is not counted as cited evidence for this new record.

The complete pinned METPO graph has 12,617 triples; its literal search has
no frustule/diatom/silicification/girdle-band match. Fresh seeding emitted
399 records. Fifty-five seed IDs are absent from 1,085 live records;
the full 1,546-row release delta and 153-row active-review table were parsed
and their policy consulted. Seed absence is not novelty or exhaustion proof.
There is no exact METPO term to reuse for this candidate.

The full candidate block was searched across CommunityMech with ignored
and hidden files included. Two hits are the same decimal measurement
`1064427.411` in a cached supplement and its text representation, not a CURIE
or reservation. The reviewed CommunityMech v1 class/property blocks do not
overlap.

Paginated changed-file lists and immutable curation blobs were checked for
all open PRs, including drafts, on 2026-10-10:

| PR | Head | Reservation |
| --- | --- | --- |
| #1802 | `a74d9278b3ce5971d773a4e81616373f795f2816` | Existing Shedu 000220; no new ID/block |
| #1782 | `35099af2b7d5347f2ca6e418c4a139979071644d` | No curation paths |
| #1476 | `b4b8d1280e25bd3e340241e7ac23b51bbe7aaec3` | No curation paths |
| #973 | `331f9517bbdf4d2c9fa97b338ee59a8986f2f174` | No curation paths |
| #924 (draft) | `e61ce120b8da953da097b9f94bfed7f292e5675a` | No curation paths |

Recheck main and reservations immediately before publishing. The protected
spore-germination record and unrelated work are excluded from curation.

## Artifacts and verification

One 11-column class TSV; no property or SSSOM file. Three trailing empty
ROBOT directive cells are intentional. Upstream contract commit:
`1408e7099d039026d7611c240938d8e177753406`; exact class/property header
blobs `b590cf303dc2fbdd57bed021668641cd0c32396d` and
`b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990` were fetched and verified
(11/13 columns). Use the maintained w3id METPO namespace, not legacy OBO
stubs. The existing CommunityMech 12-column property format is historical,
not the current canonical header.

The writer defaults to dry run, checks the parent's identity projection,
refuses target/proposal drift, prevalidates the new record before either
write and supports exact replay. Tests use controlled temporary preimages.
Require strict/LinkML validation, history, QC, products, proposal/ROBOT/ELK,
snippet checks, focused/full tests, generated-product preservation and
desktop/mobile page inspection. Record actual outcomes in the PR and
immutable adversarial review; no unrun check is claimed here.

## Upstream and round trip

After human signoff submit this TSV plus the biomineralization refinement
with v566 to berkeleybop/metpo. No upstream issue or accepted term is claimed.
On acceptance, refresh the pinned ontology, migrate the local identifier
and references, and preserve minting provenance and append-only history
without retaining a duplicate primary record.

## Change log

- v567, 2026-10-10: propose diatom frustule production.
