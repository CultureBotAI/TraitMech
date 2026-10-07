# Synnema Formation: METPO Proposal v532

## Context and Novelty

Add `traitmech:000656 synnema formation`, a PROPOSED MORPHOLOGY class on
base `036d34d2c980227bedfa34f24790f70848ae016b`. This is a fungal
developmental phenotype, not a taxon, material structure or gene.

Whole-repository searches included ignored and hidden files, synonyms,
source identifiers, slugs and reservation blocks. No exact record, synonym,
unresolved causal node or prior proposal was found. CommunityMech proposals
and all-state TraitMech/upstream METPO GitHub searches showed no collision;
search-index absence does not prove no historical discussion ever occurred.

Fresh seeding produced 399 records, 344 shared with the pre-addition
1,050-record corpus. The 55 absent IDs are 38 supporting fields and 17
reviewed duplicates; all 38 formerly unselected classes are now live.
Structured review covered 1,546 release-delta rows, 153 active-review rows,
the 12,617-triple ontology and pinned upstream templates. No exact term or
block collision was found. Other credible leads remain; this is not a
claim of trait exhaustion.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | METPO:1000059 phenotype |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

Aggregated fungal hyphae form an erect stalk bearing conidiogenous elements
in its fertile form. The qualifier preserves documented sporeless synnemata;
completed conidiation is not required at every developmental stage. Neither
cytoplasmic fusion, particular dimensions, pigmentation, spore wetness nor
one nutritional trigger defines the class.

Sporulation `METPO:1000870` and spore forming `METPO:1000871` explicitly
concern bacterial endospores. Mycelial growth `traitmech:000074` explicitly
concerns bacterial hyphae. Hyphal anastomosis `traitmech:000605` requires
cytoplasmic continuity, whereas pseudohyphal growth `traitmech:000653`
concerns attached budding yeast cells. None is an exact duplicate or
appropriate parent. Obsolete conidium classes do not supply an active
phenotype parent. Existing records remain unchanged.

The cited papers use coremia and synnemata with different developmental
emphases. No exact synonym, xref, external equivalence or organism-level
disjointness is asserted. A more specific fungal reproductive morphology
parent remains an OPEN curation discussion.

## Evidence and Example

| DOI | Evidence Role |
| --- | --- |
| [10.1016/j.simyco.2017.09.001](https://doi.org/10.1016/j.simyco.2017.09.001) | Woudenberg et al. morphology and primary isolate provenance; PMID:29158610, PMC5679026 |
| [10.3390/ijms21186660](https://doi.org/10.3390/ijms21186660) | Zetina-Serrano et al. stage-specific brlA perturbation; PMID:32932988, PMC7555563 |
| [10.1099/00221287-87-2-292](https://doi.org/10.1099/00221287-87-2-292) | Watkinson's coremium developmental stages; PMID:1141857 |

Three short snippets come from directly retrieved full text or scientific
abstract, not search results. Woudenberg's microscopic measurements concern
SNA cultures after 14 days at 25 C in darkness; Figure 7A-C instead shows
OA, MEA and DG18 colonies. Actual Figure 7D-I was inspected for stalks and
conidiogenous structures. Its species-specific dimensions are not universal.
The paper also describes loosely attached hyphae in C. domesticum.

The qualified canonical example is `NCBITaxon:2041050 Cephalotrichum
lignatile`, ex-type CBS 209.63. NCBI efetch confirms ID, label and species
rank. The [primary taxonomic account](https://pmc.ncbi.nlm.nih.gov/articles/PMC5679026/),
Specimen examined and Table 1, identifies a 1959 Belgian cave-timber isolate.
This supports provenance without inferring wild-type or GMO status.
Older erroneous sequences attributed to CBS 159.66 are not transferred.

Zetina-Serrano's directly inspected Results 2.2.3 and actual Figure 4 show
sporeless synnemata in engineered brlA-null P. expansum, versus conidiophores
clustered in wild-type coremia. The mutant is qualified evidence, not a
natural canonical example. BrlA is not asserted necessary for stalk formation.
No mechanism is transferred to Cephalotrichum and no graph is invented.

Watkinson is used only at abstract level; full text and figures were not
inspected. Its Europe PMC scientific abstract uses a semicolon in the
quoted first sentence, while the directly read publisher abstract uses a
colon. The stored quote retains the API's exact wording. Later malformed
publisher text is neither quoted nor silently repaired.

## Allocation and Contract

Reserve fresh block 1060900-1060999, using `METPO:1060900`, after v531's
1060800 block. Local identifier: `traitmech:000656`.
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

Local validation passed: direct LinkML and strict validation, writer dry
run and 20 focused tests, proposal verification and ROBOT/ELK,
`just validate-history`, `just validate-products`, `just qc`, Ruff,
45 artifact-focused tests, 56 identity/evidence rendering tests, and the
full suite (2,954 passed, two dependency warnings).

The online canonical-example audit resolved 733 examples across 548 records
with zero errors and 24 existing label-drift warnings, none concerning the
new example. The snippet resolver reports one VERIFIED scientific-abstract
quote and two NOT_IN_ABSTRACT full-text quotes. All three independently
exact-match the directly retrieved source text (10, 19 and 13 words).

Parsed class, merged and reasoned OWL contain 15, 12,628 and 12,632 triples.
The real w3id parent has the expected phenotype/quality hierarchy; no
legacy-namespace stub exists. ROBOT's physical OWL line counts are not
RDF triple counts.

Artifact comparison confirms all 1,050 pre-existing YAMLs and 536 historical
templates are unchanged. Existing trait pages change only in footer counts,
except phenotype's new child; its priority child count changes 151 to 152.
Historical narratives, shared discussion templates and the protected record
are unchanged. All six desktop/mobile screenshots were inspected; browser
assertions pass at 1440 and 390 pixels with no page errors or horizontal
overflow. The QC dashboard and coverage image were regenerated. Both
configured embedding source paths are absent, so embeddings were not regenerated.

The ordinary staged whitespace check flags only the ROBOT directive
header's three required trailing tabs; both template headers have 11 columns.
Scoped checks pass for all other paths and for that exact TSV with only
blank-at-end-of-line checking disabled. No global Git setting or QC baseline
was weakened. Existing source-license and audit warnings remain visible.

## Upstream and Round Trip

Submit the class and scope notes to upstream METPO after review. No new
upstream issue is claimed. After acceptance, refresh the ontology, migrate
the local identifier and references to the accepted METPO identifier,
preserve local-ID traceability and append-only history, and regenerate
without creating a duplicate record. Scientific discussions remain open.

## Change Log

- v532, 2026-10-07: propose synnema formation with three DOI references,
  short snippets and a qualified natural-isolate example.
