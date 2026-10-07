# Fungal Chlamydospore Formation: METPO Proposal v534

## Context and Novelty

Add `traitmech:000658 fungal chlamydospore formation`, a PROPOSED MORPHOLOGY
class on base `5397e85642f9c16f9c9eff58cde6a3dc554b97c9`. This is an
organismal morphological phenotype, not a material cell, gene or assay column.

Whole-repository searches included ignored and hidden files, labels, synonyms,
source identifiers, likely slugs, GO:0001410 and identifier reservations.
The only chlamydospore/chlamydoconidia hits were four obsolete METPO labels
and their release-delta/generated-OWL copies. No live record, exact causal
node, synonym or local proposal was found. CommunityMech proposals had no
candidate or block collision. Indexed all-state TraitMech issue search
returned no hit; index absence is not proof of no historical discussion.

Fresh seeding produced 399 records, 344 shared with the pre-addition
1,052-record corpus. The 55 absent IDs are 38 supporting fields and 17
reviewed duplicates; all 38 formerly unselected classes are now live.
Structured review covered 1,546 release-delta rows, 153 active-review rows,
the 12,617-triple ontology and pinned upstream templates. The four matching
METPO classes (`0000106`, `000107`, `1000063`, `1000391`) are deprecated
structural labels, not an active formation phenotype. Additional credible
trait leads remain; this is not an exhaustion claim.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | METPO:1000059 phenotype |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

Fungi form enlarged, thick-walled cells called chlamydospores. The definition
does not restrict their formation site or require dormancy, long-term
survival, stress resistance, a particular arrangement, one nucleus, or one
nutrient/light regime. Primary Candida viability results argue against
universal resting-spore assumptions, not against survival roles in all fungi.

Adversarial review found that the initial hypha-only wording excluded a
primary Fusarium observation. [Issue #1772](https://github.com/CultureBotAI/TraitMech/issues/1772)
records the defect: Li et al. (2012) report formation inside conidia as well
as from hyphae and germ tubes under sub-MIC FA17 treatment. The corrected
definition is formation-site-neutral. The paper's separately qualified
chlamydospore-like structures in other fungi are not promoted to confirmed
chlamydospores. Initial CREATE history is preserved; a new EDIT history and
curation event record the correction.

The fungal qualifier is deliberate: the USDA primary proceedings abstract
documents both thick- and thin-walled Phytophthora ramorum chlamydospores.
NCBI confirms that species belongs to Oomycota within Stramenopiles, not
Fungi. That report supplies terminology-boundary evidence, not additional
fungal replication or a canonical example.

Sporulation `METPO:1000870` and spore forming `METPO:1000871` concern
endospores. Pseudohyphal growth `traitmech:000653` is an attached-cell
arrangement, not chlamydospore differentiation. Citiulo et al. (2009) call
Candida budding blastic conidiogenesis and explain chlamydoconidia usage;
this source-attributed statement does not settle placement of the broader
fungal class under fungal conidiation `traitmech:000657`.

All-state upstream search returned closed
[METPO issue #67](https://github.com/berkeleybop/metpo/issues/67), an older
AI-generated hierarchy suggestion placing chlamydospores under resting
spores, not an accepted proposal for this phenotype. Its body and absence
of comments were inspected. That suggestion is not biological evidence and
is not imposed as a universal function. QuickGO resolves `GO:0001410` as a
biological process whose survival/endogenous-formation wording also needs
scope review. No exact xref, synonym or SSSOM alignment is asserted.

Two OPEN discussions preserve hierarchy/mapping and function/mechanism gaps.
No existing record is changed. A causal graph awaits primary perturbation,
supplementary strain-identity and taxon-paired protein-accession review;
gene presence is not treated as a phenotype.

## Evidence and Example

| Reference | Role |
| --- | --- |
| [10.1038/s41467-020-20010-9](https://doi.org/10.1038/s41467-020-20010-9) | Hernandez-Cervantes et al. (2020), PMID:33277479, PMC7718266; Introduction morphology clause, not cross-fungal experimental replication |
| [10.1099/13500872-141-7-1507](https://doi.org/10.1099/13500872-141-7-1507) | Sullivan et al. (1995), PMID:7551019; original species description, primary phenotype and oral-isolate provenance |
| [10.3389/fmicb.2016.01697](https://doi.org/10.3389/fmicb.2016.01697) | Bottcher et al. (2016), PMID:27833594, PMC5081361; directly inspected Figure 1, Methods and Tables 1-2 |
| [10.1111/j.1567-1364.2009.00533.x](https://doi.org/10.1111/j.1567-1364.2009.00533.x) | Citiulo et al. (2009), PMID:19538507; primary viability result and source-attributed conidiogenesis terminology |
| [USDA Treesearch 30277](https://research.fs.usda.gov/treesearch/30277) | Smith and Hansen (2008), pp. 451-454; informally refereed proceedings abstract, nonfungal terminology boundary |
| [10.1007/s10886-012-0171-1](https://doi.org/10.1007/s10886-012-0171-1) | Li et al. (2012), PMID:22932866; directly read primary scientific abstract, conidial-route counterexample with treatment limits |

Six snippets match directly retrieved full-text XML, scientific abstracts
or repository text, not search results. They contain 12, 18, 17, 16, 21 and 17
words respectively. The 2020 and 2009 quotations are complete clauses,
not reconstructed sentences. The 2016 CI 3 is an ordinal chlamydospore
index, not a fraction or percentage of cells. Its Figure 1 conditions are
seven days at 27 C in darkness; the pictured SC5314 and Wu284 (with an
umlaut on u in the source) strains are not substituted for a
provenance-checked canonical strain.

The canonical example is `NCBITaxon:42374 Candida dubliniensis`, confirmed
at species rank by NCBI efetch. The original 1995 scientific abstract
supports naturally recovered oral clinical isolates and abundant
chlamydospore production. It does not establish a named culture, wild-type
or GMO status, observation in patient tissue, or a response of every strain.
Full 1995 Methods/strain tables, 2020 mechanistic panels/supplements and the
2008 full report were not inspected. The 2012 source remains abstract-level;
its full Methods, figures and strain provenance were not inspected. These
limits are retained in the record.

## Allocation and Contract

Reserve fresh block 1061100-1061199, using `METPO:1061100`, after v533's
1061000 block. Local identifier: `traitmech:000658`.
Subset: `metpo_traitmech_2026_10`. Earlier cohorts remain unchanged.

Upstream default-branch HEAD verified at
`Knowledge-Graph-Hub/kg-microbe@1408e7099d039026d7611c240938d8e177753406`.
Inspected canonical class/property blobs match
`b590cf303dc2fbdd57bed021668641cd0c32396d` and
`b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990`.
The class-only template has 11 columns, including three required empty
trailing directive cells. No property or mapping file is appropriate.

The writer defaults to dry run, guards the parent projection and existing
target/template, prevalidates before writing and records LLM-assisted
provenance. It accepts only the exact initial pre-fix draft or corrected
result for migration/replay. The correction preserves the initial event and
canonical example. Repository history is append-only.

## Files

| Artifact | Rows |
| --- | ---: |
| `metpo_proposal_classes_robot.tsv` | 1 class, plus two header rows |
| Properties template | Omitted: no new predicates |
| SSSOM mappings | Omitted: no asserted exact external equivalent |

## Verification

Corrected writer dry run and 21 focused tests passed. All six snippets were
directly exact-matched. The maintained resolver rerun checked five DOI
references: three VERIFIED abstracts and two NOT_IN_ABSTRACT full-text
quotes. The URL-backed
report is not checked by that resolver and was verified directly, without
inventing a resolver verdict. Online canonical taxonomy resolved 735 examples
across 550 records with zero errors and 24 existing label-drift warnings.

The initial full-validation run was deliberately terminated after the
scope defect was confirmed; it is not a completed validation result.
On the corrected record, proposal verification and ROBOT/ELK reasoning passed
without UNSAT. RDF parsing found 15 class, 12,628 merged and 12,632 reasoned
triples; these are graph cardinalities, not physical file-line counts. All
three OWL graphs carry the corrected definition and six-source annotation
and use `https://w3id.org/metpo/` IRIs. The merged and reasoned graphs retain
the phenotype/quality hierarchy.

The 101 focused artifact/rendering tests passed. Playwright checks and visual
inspection passed at 1440- and 390-pixel widths: six quotes, one qualified
example, two discussions, local-ID provenance, hierarchy navigation and the
1,053-record dashboard rendered without horizontal overflow or page errors.
All 1,052 pre-existing YAML records are byte-identical to the base, including
the protected record. Of the old trait pages, 1,051 changed only in their
footer; phenotype additionally gained the new child. The only existing
priority-row change is phenotype's child count, 153 to 154. All 538 historical
TSVs, older proposal narratives and shared discussion templates are unchanged.

The complete corrected validation pipeline exited zero: direct LinkML and
strict checks, history validation (1,135 records, zero invalid), derived
products, corpus QC and Ruff passed. All 2,995 tests passed with two dependency
warnings in 544.13 seconds. The ordinary staged whitespace check flags only
the three required trailing tabs in this cohort's inspected 11-column ROBOT
header; exact-path scoped checks pass. Both exact configured embedding source
paths are absent, so embedding artifacts were not regenerated. The isolated
reviewed claw generator's 139 source blobs were reverified against its pinned
tree.

## Upstream and Round Trip

Submit the class and scope notes to upstream METPO after review. No new
upstream issue is claimed; #67 is historical context, not acceptance.
After acceptance, refresh the ontology, migrate the local identifier and
references to the accepted METPO identifier, retain local-ID traceability
and append-only history, and regenerate without creating a duplicate record.
Scientific discussions remain open.

## Change Log

- v534, 2026-10-07: propose fungal chlamydospore formation with six cited
  snippets and a cohort-qualified natural-isolate example; correct the
  initial hypha-only scope in #1772 without rewriting history.
