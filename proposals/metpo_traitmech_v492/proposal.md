# Tetrapolar Mating System: METPO Proposal v492

## Context

Lift `traitmech:000615 tetrapolar mating system`, a PROPOSED PHYSIOLOGY class.
Novelty and allocation searches included ignored and hidden files throughout
TraitMech and the sibling CommunityMech proposals, including labels, likely
slugs, synonyms, citations, discussions, graphs, history and generated pages.
No exact record or identifier collision was found before writing.

The pinned 12,617-triple METPO graph has no exact class. A fresh 399-record
seed compared with the live 1,009-record pre-addition corpus has 344 present
and 55 absent IDs. The two frozen release-review tables classify those 55 as
38 supporting-field rows and 17 duplicates, not missing primary records.
An all-state upstream issue search for tetrapolar returned no results on
2026-10-05. Paginated file lists of open local PRs #1477, #1476, #973 and
#924 contain no competing trait or proposal allocation. This establishes
candidate novelty, not exhaustion of microbial trait discovery.

## Scope

| Scope | Count | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: synthetic trait | 1 | METPO:1000059 phenotype | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

## Hierarchy Decisions

The definition denotes functional compatibility governed by two independently
segregating mating-type factors, with different specificities required at
both. It is not a MAT-locus inventory or a fixed count of mating types in a
species. Multiallelic factors, infertility and biased progeny ratios are
compatible with this classification. Different specificities are necessary,
not a sufficient guarantee of fertility under every condition.

Findley calls the observed Cryptococcus amylolentus cycle heterothallic.
That source-attributed example does not establish that the compatibility
axis always entails separate-partner dependence as defined by local
`traitmech:000610 heterothallism`. That record already distinguishes nuclear
recognition from organism-level self-fertility. Both this record and its
standalone proposal therefore use released `METPO:1000059 phenotype`, under
`METPO:1000188 quality`, rather than assume universal self-sterility. No
disjointness, universal A/B naming or fixed protein architecture is asserted.
PHYSIOLOGY is a filesystem category. Bifactorial synonymy, narrower hierarchy
and external equivalences remain review questions; no xrefs or SSSOM rows
are asserted.

## Evidence and Limitations

- `DOI:10.1371/journal.pgen.1002528`, `PMID:22359516`, `PMC3280970`:
  the Introduction supplies the defining distinction; a contiguous Results
  s2g snippet concerns recombinant mating. Actual Figures 8/9 support sexual
  structures and complementary compatibility. The conceptual Figure 9A is
  not empirical equal segregation. Selected Results and Methods were read,
  including natural provenance for CBS6039 and CBS6273 in Strains and media.
  Text S1 (`10.1371/journal.pgen.1002528.s018`) was fully text-extracted,
  not page-rendered; its sterile designation for F1S2 #16 must not replace
  the main text's partner-specific outcomes. Tables 1/2, other figures and
  other supplements remain uninspected.
- `DOI:10.1534/genetics.115.177717`, `PMID:26178967`, `PMC4566278`:
  a contiguous scientific-abstract clause records independent MAT assortment
  in a Leucosporidium scottii test cross. The abstract was directly obtained
  from Europe PMC and checked against NCBI front matter. Natural-population
  linkage disequilibrium is not genetic linkage in this cross; the abstract
  also qualifies progeny ploidy. Full-text endpoints returned HTTP 500/403,
  and NCBI supplied no body. Methods, figures, supplements and natural strain
  provenance remain uninspected; no second canonical taxon is asserted.

`NCBITaxon:104669 Cryptococcus amylolentus` is qualified to natural CBS6039
and CBS6273, not laboratory-derived progeny or every strain. Methods report
insect-frass provenance in South Africa and mating on V8 pH 5 in darkness
at 24 C. Actual Figure 8 shows two-week structures; Figure 9 and progeny
analysis distinguish mating from filamentation. Current NCBI taxonomy was
resolved on 2026-10-05.

Two CURATION_TODOs retain scope and mechanistic gaps. No protein accession or
causal graph is asserted, and no NONMECHANISTIC workaround is used. Manual
full-text checks remain separate from actual abstract-resolver verdicts.
PROPOSED status awaits human curator signoff.

## ID Space and Subset

Reserve `METPO:1056900` in `1056900-1056999`, after v491's block.
Subset: `metpo_traitmech_2026_10`. Keep `traitmech:000615` until upstream
acceptance and release; reservation is not acceptance.

## Files

| Artifact | Rows | Purpose |
| --- | ---: | --- |
| `metpo_proposal_classes_robot.tsv` | 1 class + 2 headers | Scope-A lift |
| `proposal.md` | Not applicable | Scope, evidence and migration |

No property or SSSOM template is needed. The 11-column class header follows
Knowledge-Graph-Hub/kg-microbe commit
`ea1c5f15e6c4dba6c72165367162b354e215f018`, including three trailing empty
directive cells. The pinned contract was reused because the expected local
copy is absent. CommunityMech v1 provides the reference proposal structure.
Legacy OBO-prefix examples do not override the pinned ontology's w3id IRIs.

## Verification

```bash
just verify-proposal metpo_traitmech_v492
just robot-validate-proposal metpo_traitmech_v492
just audit-proposal-coverage
just qc
```

Check record/template identity and parent parity, and inspect the actual OWL
for `https://w3id.org/metpo/` identifiers and phenotype/quality ancestry.
ELK success with an unlabeled parent is not sufficient.

## Upstream Path

Submit the validated class template to `berkeleybop/metpo` after local review.

## Round-Trip Plan

After acceptance and release, refresh the ontology and migrate the identifier
to the accepted METPO CURIE. Preserve the local ID in an explicit migration
artifact and append-only history, regenerate dependent artifacts and avoid
creating a duplicate primary record.

## Change Log

- v492, 2026-10-05: propose tetrapolar mating with two DOI-backed snippets,
  a qualified natural example and explicit functional/readout limitations.
