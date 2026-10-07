# Fungal Sclerotium Formation: METPO Proposal v536

## Context and Novelty

Add `traitmech:000660 fungal sclerotium formation`, a PROPOSED MORPHOLOGY
class on base `af119ee7fe04090ba73519ccacd9ef0e8e99463e`. This is an
organismal formation phenotype, not a material structure, gene, transcript
profile or assay column.

Whole-repository searches included ignored and hidden files, labels,
sclerotial/sclerotogenesis/pseudo-/microsclerotial variants, resting-body and
hyphal-knot phrases, source identifiers, GO:1990045 and allocation reservations.
The six non-ROBOT sclerotium hits are three deprecated ontology labels and
three release-review rows. Ignored ROBOT copies repeat those labels. No live
exact formation record, synonym, causal node or earlier proposal was found.
Existing trait YAMLs and research provenance remain unchanged.

Fresh seeding produced 399 records, 344 shared with the pre-addition
1,054-record corpus. The 55 absent IDs are 38 supporting fields and 17
reviewed duplicates; all 38 formerly unselected classes are now live.
Structured review covered 1,546 release-delta rows, 153 active-review rows,
the 12,617-triple ontology and pinned upstream templates. No active exact
formation class or conflicting 1061300-block allocation was found.
Ignored-and-hidden CommunityMech proposal search found no collision.
All-state GitHub queries for sclerotium, sclerotia and sclerotial each returned
zero indexed results in TraitMech and upstream METPO, with incomplete-results
flags false; index absence alone is not conclusive historical proof.
Credible additional trait leads remain; no exhaustion is claimed.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | METPO:1000059 phenotype |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

The phenotype is formation of compact mycelial resting bodies called
sclerotia. Fungal scope is explicit because the Fuligo source uses the same
structure name for a dormant plasmodial state. That nonfungal state is not
an exact synonym or exemplar. Formation is separate from initiation timing,
maturation, later germination, viability and survival duration. Neither
melanization, plant pathogenicity, aflatoxin production, a sexual/asexual
reproductive mode nor one environmental regime is universally required.

Use phenotype rather than plant pathogen, black pigmented, fungal conidiation
`traitmech:000657` or chlamydospore formation `traitmech:000658`.
The 2022 source distinguishes true, small, pseudo- and microsclerotial
structures. Its Introduction is an attributed terminology classification,
not an independent experimental observation. Do not flatten these names into
exact synonyms or impose one size, three-layer anatomy or host-material
exclusion across every usage. Their subclass/equivalence scope remains OPEN.

The pinned ontology has deprecated bare labels at `METPO:0000117`,
`METPO:000118` and `METPO:1000398`. All three are deprecated subclasses of
ObsoleteClass without definitions or replacement links. These labels do not
establish exact equivalence to this organismal phenotype, and their original
scope remains unresolved. No reason-code meaning is inferred without resolving
the referenced authority. Upstream review must reconcile this legacy rather
than silently reactivating a class. QuickGO resolves active `GO:1990045
sclerotium development` as a biological process, not an exact organismal
phenotype. No xrefs, exact synonyms or SSSOM mapping are asserted.

Two OPEN discussions preserve identity/mapping and function/mechanism gaps.
No causal graph is added: taxon-specific perturbation/complementation evidence,
remaining figures/supplements and authority-verified protein accessions still
need review. Gene possession or expression alone does not establish the trait.

## Evidence and Example

| Reference | Directly Inspected Evidence |
| --- | --- |
| [10.1128/AEM.00565-08](https://doi.org/10.1128/AEM.00565-08) | Horowitz Brown et al. (2008), PMID:18658287, PMC2547031; scientific abstract, Introduction, growth/density Methods, first Results subsection, Table 1 and actual Figure 1 |
| [10.3390/jof9070737](https://doi.org/10.3390/jof9070737) | Wang et al. (2023), PMID:37504726, PMC10381867; scientific abstract, Introduction, Methods 2.1/2.6, Results 3.3, Discussion, figure captions and actual Figures 3-4 |
| [10.1016/j.micres.2019.126326](https://doi.org/10.1016/j.micres.2019.126326) | PMID:31493702; directly retrieved Europe PMC scientific abstract only, not full text, figures, supplements or strain provenance |
| [10.1128/spectrum.02084-21](https://doi.org/10.1128/spectrum.02084-21) | PMID:35080446, PMC8791194; Introduction terminology only, not experimental Results, figures, supplements or strain provenance |
| [10.2478/s11658-007-0047-5](https://doi.org/10.2478/s11658-007-0047-5) | Krzywda et al. (2008; online 2007), PMID:17965965, PMC6275577; scientific abstract only, not Methods, figures or natural-isolate provenance |

All five snippets were exact-matched as contiguous spans to directly
retrieved scientific abstracts or full-text XML, not search-result text.
Their word counts are 15, 18, 16, 21 and 13. The second quote is Results 3.3;
the fourth is the Introduction terminology passage. Full-text XML retrieval
failed for the 2008 Aspergillus study; its full text was read as publisher/PMC
HTML instead. No successful XML retrieval is claimed for that source.

The Aspergillus Figure 1A reports log10 sclerotial dry mass per plate, not
literal body numbers despite the abstract's wording. The proposed quorum
factor is not identified. In Wang et al., maturation photographs are Figure
3A; Results pointers to Figure 3B are misplaced because 3B plots growth.
Figure 4C/D report body counts and total air-dried mass per flask, not mass
per body. Delayed maturation is not complete loss of formation, and the
complement does not restore every cortex measure to wild type. The three
inspected images match the PMC metadata MD5 prefixes; full metadata checksum
equality is not claimed. Other actual figures and supplements were not read.

The 2019 abstract's microscopy comparison does not establish identical
composition or preserved function in every respect. The treatment producing
non-melanized bodies was not inspected. Fuligo starvation/drying conditions
and pigment/viability observations are not transferred to fungi.

The canonical example is `NCBITaxon:5180 Sclerotinia sclerotiorum`, with
species label and rank checked by NCBI efetch. It is qualified to wild-type
strain 1980 under the 2023 study's PDA/carrot conditions, not the engineered
SSA deletion or complement. Independent primary Methods at
[10.1128/AEM.67.1.75-81.2001](https://doi.org/10.1128/AEM.67.1.75-81.2001),
PMID:11133430, PMC92519, explicitly identify isolate 1980 as originating from
dry bean culls in western Nebraska and supplied by J. R. Steadman. That
passage was read directly in PMC HTML; the cited original 1990 study was not
retrieved. The provenance URL stays in the example note and is not a sixth
independent formation evidence item. No claim covers every strain or condition.
NRRL 3357, Macrophomina and Fuligo are not additional canonical examples.

## Allocation and Contract

Reserve block 1061300-1061399, using `METPO:1061300`, after v535's 1061200
block. Local identifier: `traitmech:000660`. Subset: `metpo_traitmech_2026_10`.
The block does not overlap CommunityMech v1's 1007100-1007220 allocation.
Earlier cohorts remain unchanged.

Upstream default-branch HEAD was freshly verified at
`Knowledge-Graph-Hub/kg-microbe@1408e7099d039026d7611c240938d8e177753406`.
Canonical class/property blobs were rehashed to
`b590cf303dc2fbdd57bed021668641cd0c32396d` and
`b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990`.
The class template retains 11-column headers, including three trailing empty
directive cells. The writer defaults to dry run, guards eight parent scope
fields and exact target/template preimages, prevalidates before writing and
supports idempotent replay. Curation is LLM-assisted; history is append-only.

## Files

| Artifact | Rows |
| --- | ---: |
| `metpo_proposal_classes_robot.tsv` | 1 class plus two header rows |
| Properties template | Omitted: no new predicates |
| SSSOM mappings | Omitted: no asserted exact external equivalence |

## Verification

The writer dry run, guarded application/replay and 20 focused writer tests
passed. The combined writer/README/priority/dashboard run passed 65 tests.
`just qc` and Ruff passed, with no new blocking corpus audit findings.
Strict corpus validation passed for all 1,055 records. LinkML validation,
proposal verification, ROBOT/ELK, product validation and
the add-trait skill validator passed. Repository history validates 1,139
records with zero invalid links. Review issue
[#1776](https://github.com/CultureBotAI/TraitMech/issues/1776) corrects the
scaffolder's default actor attribution via a second append-only AUDIT record;
the original history remains intact and no trait content was changed by that
correction. The skill now explains the default-actor trap.

All five snippets have direct source matches. The maintained resolver returned
three VERIFIED and two NOT_IN_ABSTRACT rows; the latter two are the directly
checked Results and Introduction spans. Online taxonomy audit resolved all
737 examples across 552 records: zero errors and 24 existing label warnings.

RDF parsing measured 15 class, 12,628 merged and 12,632 reasoned triples, with
canonical w3id METPO IRIs and phenotype-to-quality hierarchy intact. All
1,054 prior YAMLs, 540 historical proposal TSVs, historical proposal narratives
and discussion templates are unchanged. Of the prior trait pages, 1,053 have
footer-only changes; phenotype also gains the child link. The only old
priority-row change is phenotype's child count from 155 to 156.

Desktop/mobile browser checks at 1,440 and 390 pixels passed for identity,
five quotes, the qualified example, two OPEN discussions, source-limit
visibility, hierarchy navigation, dashboard totals, image loading and absence
of overflow or JavaScript errors. Screenshots were visually inspected.

Both exact configured embedding inputs are absent, so embedding artifacts
are not regenerated. All 139 source blobs in the isolated reviewed claw
generator were reverified against its pinned tree; the unrelated shared
checkout is not modified. Final full-suite and CI results are recorded in
the PR validation receipt before merge.

The ordinary staged whitespace check flags only the template directive row's
three required trailing tabs. All three rows have 11 cells and both headers
match the pinned upstream template. Scoped checks pass with that exact path
excluded from ordinary checking and checked with blank-at-eol disabled.

## Upstream and Round Trip

Submit the class, scope notes and legacy-ID reconciliation question to METPO
after review. No new upstream issue or acceptance is claimed. On acceptance,
refresh the ontology, migrate the local identifier and references to the
accepted METPO ID, preserve local-ID traceability and append-only history,
and regenerate without creating a duplicate. Scientific discussions remain
OPEN until their evidence and mapping questions are resolved.

## Change Log

- v536, 2026-10-07: propose fungal sclerotium formation with five directly
  checked source snippets and a provenance-qualified strain 1980 example.
- Address #1776 with append-only actor-attribution correction and a focused
  add-trait skill warning.
