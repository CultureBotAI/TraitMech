# Coenobium Formation: METPO Proposal v531

## Context and Novelty

Add `traitmech:000655 coenobium formation`, a PROPOSED MORPHOLOGY class on
base `c47ebc92f3330fa694b523bfd25074df6edf0dcd`. It denotes an organismal
developmental phenotype, not an algal taxon, material colony or gene.

Whole-repository searches included ignored and hidden files, terminology,
source identifiers, slugs and reservation blocks. No exact record, synonym,
unresolved causal node or prior proposal was found. CommunityMech proposals
and all-state TraitMech/upstream METPO GitHub searches showed no collision;
search-index absence is not proof that no historical discussion ever occurred.

Fresh seeding produced 399 records, 344 shared with the pre-addition
1,049-record corpus. The 55 absent IDs are 38 supporting fields and 17
reviewed duplicates; all 38 formerly unselected classes are now live.
Structured review covered 1,546 release-delta rows, 153 active-review rows,
the 12,617-triple ontology and pinned upstream templates. No exact term or
block collision was found. Credible uncurated leads remain; this is not
evidence of trait exhaustion.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | METPO:1000059 phenotype |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

The cell complement is established for an individual clonal colony, rather
than enlarged by adding cells during subsequent growth. Reproduction can
make daughter colonies. The definition does not impose a fixed count across
taxa or conditions, a sheet shape, common wall, power-of-two count, motility
state or absence of differentiation. Harvey's extant comparisons include
motile volvocines and Volvox germ-soma differentiation; Chung's introductory
little-or-no-specialization formulation is not imposed universally.

Individual cell shape `METPO:1000666` and macroscopic colony morphology
`METPO:1007062` differ in scope. Obsolete cell arrangement `METPO:1000046`
and aggregate `METPO:1000011` are not active parents. Palmelloid formation
`traitmech:000654` concerns enclosure or extracellular adhesion, not this
developmental criterion. Rosette cell arrangement `traitmech:000652`
requires inward cell poles, and biofilm formation `traitmech:000053`
requires surface attachment. A multinucleate coenocyte is not a multicellular
coenobium. No exact synonym, external equivalence or organism-level
disjointness is asserted. Existing records remain unchanged.

## Evidence and Example

| DOI | Evidence Role |
| --- | --- |
| [10.1098/rspb.2023.1882](https://doi.org/10.1098/rspb.2023.1882) | Harvey's modern-algal terminology comparison; PMID:37876191, PMC10598416 |
| [10.1242/jcs.212233](https://doi.org/10.1242/jcs.212233) | Cardon et al. microscopy and canonical example; PMID:29487180 |
| [10.1038/s41598-018-28627-z](https://doi.org/10.1038/s41598-018-28627-z) | Chung et al. independent culture observations; PMID:29980731, PMC6035231 |

Three short snippets come from directly retrieved scientific abstract or
full text, not search results. Harvey's fossil developmental interpretation
is not presented as an experiment on living algae. Chung's Results supports
coenobia without IAA treatment; no numerical proportion or direct figure
inspection is claimed for that source.

Cardon's primary abstract, Results, Methods and actual Figure 1 were
inspected. The qualified canonical example is `NCBITaxon:113528 Enallax
costatus`, CCAP 276/31. NCBI efetch confirms the species ID, label and rank.
The [collection record](https://www.ccap.ac.uk/catalogue/strain-276-31)
supports natural-isolate provenance and is not counted as independent
trait evidence. Culture and life-stage qualifiers stay in the YAML.
Figure 1 shows joined-cell morphology; Figure 3 does not show release.
Supplementary Figure S1 and movies were not directly inspected: the public
supplement exceeded the web reader's size limit and direct download returned
403. Release remains attributed to the primary Results, not personally
verified movie evidence.

Two OPEN discussions retain hierarchy and developmental-mechanism questions.
No graph is invented from cell rotation, Golgi localization or gene presence;
organism-specific perturbation and protein-accession review remain necessary.

## Allocation and Contract

Reserve fresh block 1060800-1060899, using `METPO:1060800`, after v530's
1060700 block. Local identifier: `traitmech:000655`.
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
full suite (2,934 passed, two dependency warnings).

The online canonical-example audit resolved 732 examples across 547 records
with zero errors and 24 existing label-drift warnings, none concerning the
new example. The snippet resolver reports one VERIFIED scientific-abstract
quote and two NOT_IN_ABSTRACT full-text quotes. All three independently
exact-match the directly retrieved source text (11, 15 and 18 words).

Parsed class, merged and reasoned OWL contain 15, 12,628 and 12,632 triples.
The real w3id parent has the expected phenotype/quality hierarchy; no
legacy-namespace stub exists. ROBOT's physical OWL line counts are not
RDF triple counts.

Artifact comparison confirms all 1,049 pre-existing YAMLs and 535 historical
templates are unchanged. Existing trait pages change only in footer counts,
except phenotype's new child; its priority child count changes 150 to 151.
Historical narratives, shared discussion templates and the protected record
are unchanged. All six desktop/mobile screenshots were inspected; browser
assertions pass at 1440 and 390 pixels with no page errors or horizontal
overflow. The QC coverage image regenerated byte-identically. Both configured
embedding source paths are absent, so embeddings were not regenerated.

The ordinary staged whitespace check flags only the three required trailing
tabs on the ROBOT directive header. The 11-column template verifier and
scoped whitespace checks pass; no global Git setting or QC baseline was
weakened. Existing source-license and audit warnings remain visible.

## Upstream and Round Trip

Submit the class and scope notes to upstream METPO after review. No new
upstream issue is claimed. After acceptance, refresh the ontology, migrate
the local identifier and references to the accepted METPO identifier,
preserve local-ID traceability and append-only history, and regenerate
without creating a duplicate record. Scientific discussions remain open.

## Change Log

- v531, 2026-10-07: propose coenobium formation with three DOI references,
  short snippets and a qualified natural-isolate example.
