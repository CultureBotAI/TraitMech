# METPO proposal v564: siliceous scale production

## Context and scope

Lift `traitmech:000688` as `METPO:1064100`: one physiological phenotype,
kept `PROPOSED` pending human review. Scope A: one class in one new record.
Scope B: zero predicates. Scope C: zero schema enums. This is an assayable
cellular production phenotype, not a gene, sequence feature, material entity,
or precomposed growth-on-chemical relation.

## Hierarchy decisions

Parent: phenotype `METPO:1000059`, below quality `METPO:1000188`.
A broader biomineralization phenotype remains a curation TODO. Producing
scales differs from merely possessing, acquiring, reusing, extruding or
arranging them. Shell assembly and scale-layer construction alone cannot
establish production. General silicification, diatom frustule formation,
magnetosome/ferrosome possession and substrate adhesion are not equivalents.
Do not assert a universal geometry, covering architecture, growth dependence,
cell-cycle coupling, fitness effect, molecular mechanism or homology.
No synonyms, xrefs or organism-level disjointness are asserted.

## Evidence and limits

- [Nomura and Ishida 2016](https://doi.org/10.1016/j.protis.2016.05.002),
  PMID:27348459: scientific abstract directly read at
  [NBRP](https://rrc.nbrp.jp/references/56432?lang=en) and source-qualified
  Europe PMC CORE. Supports scale formation in silica deposition vesicles in
  the historically named Paulinella chromatophora. Microtubule involvement in
  scale geometry is proposed, not demonstrated causal necessity.
- [Sandgren, Hall and Barlow 1996](https://doi.org/10.1111/j.0022-3646.1996.00675.x):
  publisher-deposited scientific ABSTRACT directly read in
  [Crossref JATS](https://api.crossref.org/works/10.1111%2Fj.0022-3646.1996.00675.x).
  Silica-limited Synura petersenii cultures resumed scale production after
  silica addition. Recovery timing is experiment-specific. Scale production
  could be uncoupled from division in this system. The print date is August
  1996; June 2008 is its online date, not an independent study.

Both snippets are short contiguous scientific-abstract passages, not titles
or search-result text. Full original Methods and figures were not inspected;
publisher access was unavailable. Preserve actual automated snippet-resolver
outcomes separately from these direct-source checks. These are two independent
primary studies with different methods, not replication of a common mechanism.

Canonical examples await joint verification of assay Methods, strain
provenance and current taxonomy. The NIES-4060 collection association with
the 2016 paper is provenance, not independent experimental evidence or a
general license to rename historical chromatophora observations. Molecular
graphs need production-specific evidence and properly grounded accessions.

## Allocation and novelty

Reserve **traitmech:000688**, cohort **v564**, and the whole
**METPO:1064100-1064199** block; only 1064100 is populated.
Subset: `metpo_traitmech_2026_10`. No CommunityMech v1 overlap.

Allocation main: `6cd0b1df24f87772ef134ed342e5cf90a6ec5006`.
Ignored-and-hidden searches covered all 22 pre-existing TraitMech worktrees,
including records, ontology, history, research, proposals and generated files.
Scale production/formation/biogenesis, siliceous scales, silicification,
frustules, testate amoebae, both primary DOIs, local ID, cohort and whole
block found no exact trait or reservation. Two broad text hits were
commercial-scale and microscale production, not scale biomineralization.
The block was also searched across CommunityMech with ignored/hidden files.
An RDF scan of the pinned METPO found no exact class; existing magnetosome
and ferrosome records concern different structures and mineral products.
No exact unresolved graph node, synonym or parent TODO required an old-record
repair. All old trait YAMLs remain unchanged.

Fresh seeding emitted 399 records, with 55 exact IDs absent from the live
1,082-record corpus. The frozen release-delta and active-review dispositions
were consulted; those absent IDs are duplicate phenotype leads or supporting
relations, not a missing-work queue. This is not an exhaustion claim.

Complete paginated open-head inventory, including drafts, checked on 2026-10-10:

| PR | Head | Reservation |
| --- | --- | --- |
| #1802 | `a74d9278b3ce5971d773a4e81616373f795f2816` | existing Shedu; no new ID/block |
| #1782 | `35099af2b7d5347f2ca6e418c4a139979071644d` | none in changed curation paths |
| #1476 | `b4b8d1280e25bd3e340241e7ac23b51bbe7aaec3` | none in changed curation paths |
| #973 | `331f9517bbdf4d2c9fa97b338ee59a8986f2f174` | none in changed curation paths |
| #924 (draft) | `e61ce120b8da953da097b9f94bfed7f292e5675a` | none in changed curation paths |

Changed-file lists and immutable curation blobs were checked. Recheck main
and reservations immediately before publication.

## Artifacts and verification

One class TSV: two 11-column headers and one class row. No property or SSSOM
file is needed. Preserve the three empty trailing directive cells.
Upstream skill/templates were checked at
`1408e7099d039026d7611c240938d8e177753406`. Class blob:
`b590cf303dc2fbdd57bed021668641cd0c32396d`; property blob:
`b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990` (11/13 columns).
CommunityMech v1 supplies the worked convention. Use maintained w3id METPO
expansion, not the upstream legacy OBO example.

```sh
PYTHONPATH=src .venv/bin/python scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v564
PYTHONPATH=src .venv/bin/python scripts/robot_validate_proposal.py proposals/metpo_traitmech_v564
```

Parse emitted RDF to check 1064100 -> labeled 1000059 -> 1000188 under
`https://w3id.org/metpo/`. The writer guards parent identity and scope,
defaults to dry run and refuses conflicting target/proposal preimages.
Require strict/LinkML/history/QC/products, source/snippet checks, focused/full
tests, immutable adversarial review and desktop/mobile page inspection.
Actual results belong in the PR and structured review, not a pre-execution
success assertion.

## Upstream and round trip

After human signoff submit the TSV to berkeleybop/metpo. No upstream issue
or accepted term is claimed. Following release, refresh the pinned ontology,
seed the accepted term and migrate the local identifier while preserving
provenance. The reserved placeholder is not a released METPO identifier.

## Change log

- v564, 2026-10-10: initial source-bounded scale-production proposal.
