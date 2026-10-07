# Fungal Conidiation: METPO Proposal v533

## Context and Novelty

Add `traitmech:000657 fungal conidiation`, a PROPOSED MORPHOLOGY class on
base `704a81cd3a3ce28e1cae857bd3c10b6acecd00c0`. This is a reproductive
phenotype, not a material spore, taxon, gene or assay column.

Whole-repository searches included ignored and hidden files, terminology,
source identifiers, slugs and reservation blocks. Existing evidence mentions
in heterokaryon incompatibility, autophagic glycogen degradation and synnema
formation were inspected; none is an exact TraitRecord or unresolved exact
causal node. The sporulation research report explicitly distinguishes fungal
conidiation from bacterial endospore formation. No exact local proposal or
block collision was found. CommunityMech proposals and indexed all-state
upstream METPO work showed no collision. TraitMech's GitHub search returned
the related synnema PR #1770, not a conidiation record; index absence is not
proof of no historical discussion.

Fresh seeding produced 399 records, 344 shared with the pre-addition
1,051-record corpus. The 55 absent IDs are 38 supporting fields and 17
reviewed duplicates; all 38 formerly unselected classes are now live.
Structured review covered 1,546 release-delta rows, 153 active-review rows,
the 12,617-triple ontology and pinned upstream templates. The four matching
conidium/conidia classes (`METPO:0000102`, `METPO:000103`, `METPO:1000080`,
`METPO:1000390`) are deprecated material terms, not an active phenotype.
Credible additional leads remain; this is not a claim of trait exhaustion.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | METPO:1000059 phenotype |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

Fungi produce nonmotile asexual propagules called conidia through outgrowth
from conidiogenous cells or conversion of existing hyphal cells. The class
does not require one conidiophore architecture, an aerial stalk, detached
spores, a particular pigmentation, cell/nucleus count or a universal stress
trigger. Cole's historical Deuteromycetes classification is not imposed.

The fungal qualifier is deliberate: the directly retrieved primary abstract
for PMID:9199700 uses conidium for Streptomyces reproductive cells. That
bacterial terminology does not establish the same fungal developmental mechanism.
No unqualified exact synonym is asserted.

Sporulation `METPO:1000870` and spore forming `METPO:1000871` explicitly
concern endospores. Mycelial growth `traitmech:000074` concerns bacterial
hyphae. Synnema formation `traitmech:000656` denotes stalk aggregation and
includes documented sporeless forms, so neither class is made the other's
is-a parent. Pseudohyphal growth `traitmech:000653` is an attached-cell
arrangement, not equivalent to conidial production. Existing records remain
unchanged. Two OPEN discussions retain hierarchy/mapping and developmental
mechanism questions; no exact xref, synonym or causal graph is invented.

## Evidence and Example

| Reference | Evidence Role |
| --- | --- |
| [10.2336/nishinihonhifu.40.1083](https://doi.org/10.2336/nishinihonhifu.40.1083) | Cole (1978), directly read publisher abstract; terminology from a Mini Review, not experimental replication |
| [10.1101/gad.3.4.559](https://doi.org/10.1101/gad.3.4.559) | Springer and Yanofsky (1989), primary Neurospora developmental observations; PMID:2524423 |
| [10.1016/j.simyco.2017.09.001](https://doi.org/10.1016/j.simyco.2017.09.001) | Woudenberg et al. (2017), primary morphology and isolate provenance; PMID:29158610, PMC5679026 |
| [PMID:9199700](https://pubmed.ncbi.nlm.nih.gov/9199700/) | Szabo et al. (1997), bacterial terminology boundary, not positive fungal evidence |

Four short snippets directly match publisher HTML, primary scientific
abstracts or primary figure-caption XML, not search results. Cole's
[publisher abstract](https://www.jstage.jst.go.jp/article/nishinihonhifu/40/6/40_6_1083/_article/-char/en)
was read directly; the exact DOI query returned no Europe PMC record.
The 1989 snippet retains the source spelling dessication. Its mutant and
wild-type observations remain abstract-level: full Methods, figures and
independent strain provenance were not inspected. No canonical Neurospora
strain or universal molecular/nutritional requirement is asserted.

The qualified canonical example is `NCBITaxon:2041050 Cephalotrichum
lignatile`, ex-type CBS 209.63. NCBI efetch confirms ID, label and species
rank. The [primary taxonomic account](https://pmc.ncbi.nlm.nih.gov/articles/PMC5679026/),
Specimen examined and Table 1, identifies Hennebert's 1959 Belgian
cave-timber isolate. This is primary isolate provenance without an inferred
wild-type or GMO status. Actual Figure 7H-J and the description show
conidiogenous structures and conidia in basipetal chains. Microscopic
descriptions use SNA after 14 days at 25 C in darkness; Figure 7A-C instead
shows OA, MEA and DG18 colonies. Static morphology is not claimed as
time-lapse proof of each transition.

## Allocation and Contract

Reserve fresh block 1061000-1061099, using `METPO:1061000`, after v532's
1060900 block. Local identifier: `traitmech:000657`.
Subset: `metpo_traitmech_2026_10`. Earlier cohorts remain unchanged.

Upstream contract checked at
`Knowledge-Graph-Hub/kg-microbe@1408e7099d039026d7611c240938d8e177753406`.
Inspected canonical class/property blobs match
`b590cf303dc2fbdd57bed021668641cd0c32396d` and
`b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990`.
The class-only template has 11 columns, including three required empty
trailing directive cells. No property or SSSOM mapping file is appropriate.

| File | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 class plus two header rows |
| proposal.md | Reviewer narrative |

The writer defaults to dry run, guards the parent projection and existing
target/template, prevalidates before writing and records LLM-assisted
provenance. Repository history is append-only.

## Verification

The writer dry run and 20 focused tests passed. LinkML, strict corpus
validation, history/product validation, `just qc` and Ruff passed. The full
regression suite passed: 2,974 tests with two dependency deprecation warnings.

All four snippets exact-match the directly retrieved sources (21, 17, 6 and
12 words). The maintained resolver returned two VERIFIED abstracts, one
NOT_IN_ABSTRACT figure caption and one UNRESOLVED Cole citation. Both exact
DOI and title queries returned no Europe PMC record for Cole; its publisher
abstract was checked directly without relabeling the resolver outcome.
The snippet audit has no findings for this new record. Online canonical
taxonomy validation resolved 734 examples across 549 records with zero errors
and 24 existing label-drift warnings.

Proposal verification and ROBOT reasoning passed. Parsed RDF cardinalities
are 15, 12,628 and 12,632 triples for the class, merged and reasoned graphs.
The new class and parent use `https://w3id.org/metpo/`; the merged parent
retains its phenotype label and quality parent. All 537 historical TSVs and
earlier proposal narratives remain unchanged.

All 101 artifact/rendering tests passed. Playwright checks and six inspected
screenshots at 1440- and 390-pixel widths confirmed four visible evidence
quotes, local-ID provenance, the qualified canonical example, two OPEN
discussions, working parent/child navigation, a current dashboard and no
horizontal overflow or page errors. All 1,051 existing YAML records are
byte-identical, including the protected spore-germination record. Of the old
trait pages, 1,050 changed only in corpus footers; phenotype additionally
gained the child link. Its priority row changed only from 152 to 153 children.
Shared discussion templates remain unchanged. The regenerated coverage image
is byte-identical. Embedding artifacts were not regenerated because both
exact configured input paths are absent.

The ordinary staged whitespace check flags only the three required trailing
tabs on the ROBOT directive row. Structured parsing confirms 11 columns in
all three rows. Checks excluding that exact TSV, and the TSV-only check with
`core.whitespace=-blank-at-eol`, both pass; no global setting was changed.

## Upstream and Round Trip

Submit the class and scope notes to upstream METPO after review. No new
upstream issue is claimed. After acceptance, refresh the ontology, migrate
the local identifier and references to the accepted METPO identifier,
preserve local-ID traceability and append-only history, and regenerate
without creating a duplicate record. Scientific discussions remain open.

## Change Log

- v533, 2026-10-07: propose fungal conidiation with three DOI references,
  a PMID-backed terminology boundary, four short snippets and a qualified example.
