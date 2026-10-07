# Fungal Appressorium Formation: METPO Proposal v535

## Context and Novelty

Add `traitmech:000659 fungal appressorium formation`, a PROPOSED MORPHOLOGY
class on base `fe2f17ca4436575f71ef102b7643ebaa18a6dd1c`. This is an
organismal formation phenotype, not a material structure, gene, transcript
profile or assay column.

Whole-repository searches included ignored and hidden files, labels, aliases,
likely slugs, source identifiers, GO:0075016 and allocation reservations.
Appressorium/penetration-structure hits were seven lines in two existing
research reports: plant-pathogen and black-pigmentation research leads,
not a live record, exact formation node, synonym or earlier proposal. The
material appressorium candidates in those reports are not equivalent to this
organismal formation phenotype and are not blindly regrounded. Existing
research provenance and trait YAMLs remain unchanged.

Fresh seeding produced 399 records, 344 shared with the pre-addition
1,053-record corpus. The 55 absent IDs are 38 supporting fields and 17
reviewed duplicates; all 38 formerly unselected classes are now live.
Structured review covered 1,546 release-delta rows, 153 active-review rows,
the 12,617-triple ontology and pinned upstream templates. None contains an
exact appressorium formation class or a conflicting 1061200-block allocation.
Ignored-and-hidden CommunityMech proposal search also found no collision.
All-state GitHub searches for both appressorium and appressoria returned zero
indexed results in TraitMech and upstream METPO, with incomplete-results
flags false; index absence alone is not conclusive historical proof.
Further credible microbial trait leads remain; no exhaustion is claimed.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | METPO:1000059 phenotype |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

The phenotype is formation of specialized surface-associated penetration
structures called appressoria. It does not require plant pathogenicity,
successful penetration, one shape or cell number, melanization, a fixed
turgor, one nutritional regime or a universal cell-cycle/Pmk1 mechanism.
Fungal scope is explicit; the name does not claim such structures occur
only in fungi.

Demoor et al. (2019) deliberately apply a broad appressorium umbrella to
structures previously called appressorium-like in saprotrophs, and include
unicellular structures and compound infection cushions. Their cellophane
assay is not a natural-host infection assay. Mere contact or growth
reorientation without penetration was distinguished from the appressoria
identified in that survey. Negative assay results are not clade-wide absence
claims, and the paper's strain counts are not used to calculate prevalence.

Becker et al. (2016) call the internal leaf-exit structure an expressorium,
while acknowledging an intrinsecus-appressorium convention. This is retained
as a source-attributed terminology boundary, not an exact synonym or an
unqualified new exemplar. Whether that structure belongs under this broad
class, and whether narrower subclasses are warranted, remain OPEN.

Use phenotype rather than plant pathogen `METPO:1004003`, black pigmented
`METPO:1003022` or thigmotropism `traitmech:000594`. Disease causation,
pigmentation, contact-directed growth and differentiation are not the same
trait. QuickGO resolves active `GO:0075016 appressorium formation` as a
host-associated biological process with swollen/flattened filament wording.
That is not an exact organismal-phenotype mapping covering saprotrophic
observations. No xrefs, exact synonyms or SSSOM mapping are asserted.

Two OPEN discussions preserve scope/mapping and function/mechanism questions.
No causal graph is added: remaining primary perturbation/complementation
figures, supplements and taxon-paired protein accessions need review.
Expression association and gene possession alone do not establish the trait.

## Evidence and Example

| Reference | Directly Inspected Evidence |
| --- | --- |
| [10.3390/jof5030072](https://doi.org/10.3390/jof5030072) | Demoor, Silar and Brun (2019), PMID:31382649, PMC6787622; scientific abstract, Introduction, Methods, Results, broad-definition Discussion paragraph, actual Figures 2 and 6, supplementary Table S1 |
| [10.1371/journal.ppat.1002514](https://doi.org/10.1371/journal.ppat.1002514) | Soanes et al. (2012), PMID:22346750, PMC3276559; scientific abstract, selected Introduction/Results, actual Figure 1 and fungal-strain/growth Methods |
| [10.1186/1741-7007-6-9](https://doi.org/10.1186/1741-7007-6-9) | Nesher, Barhoom and Sharon (2008), PMID:18275611, PMC2276476; scientific abstract and strain/germination Methods, not full result figures |
| [10.1111/nph.13931](https://doi.org/10.1111/nph.13931) | Becker et al. (2016), PMID:26991322, PMC5069595; scientific Summary and expressorium terminology Results paragraph, not figures, movies or supplements |

All four snippets are contiguous, directly exact-matched full-text XML spans,
not search-result text. Their word counts are 20, 19, 13 and 11. The Guy11
quote is from Results, not the Author Summary or scientific abstract.
The expressorium quote retains the source's hyphen character. The 2019
supplement is a single-page strain table; no supplementary microscopy is
claimed. Publisher PDF bytes match the repository metadata checksum
`c201f2d723c17dff6854acbfac7c85b6`. The three inspected main figures also
match their repository image checksums.

The canonical example is `NCBITaxon:318829 Pyricularia oryzae`, species rank
and synonym `Magnaporthe oryzae` confirmed by NCBI efetch. It is qualified to
wild-type Guy11 in the 2012 study, not its engineered deletion mutant or
strain 70-15. Formation was directly observed under inductive in-vitro
conditions, at the reported time points; RNA profiles are not used as a
substitute for the morphology. The Methods describe plastic coverslips with
1,16-hexadecanediol, whereas Results describing Figure 1A name a hydrophobic
glass slide. This within-article discrepancy remains unresolved; neither
surface description is silently substituted for the other. Review issue
[#1774](https://github.com/CultureBotAI/TraitMech/issues/1774) corrects the
initial unqualified surface claim without changing the formation phenotype.

Independent primary population-study Methods at
[10.5423/PPJ.NT.04.2013.0042](https://doi.org/10.5423/PPJ.NT.04.2013.0042),
PMID:25288972, PMC4174813, explicitly identify Guy11 as a rice-pathogenic
isolate from French Guiana and distinguish laboratory crossing derivatives.
That passage was read directly; its cited original 1988 study was not
retrieved. This reference remains in the example note as provenance, not a
fifth independent appressorium evidence item. No claim extends to every
strain or condition. Other survey strains and the unresolved 3.1.3
provenance/species-complex assignment are not canonical examples.

## Allocation and Contract

Reserve fresh block 1061200-1061299, using `METPO:1061200`, after v534's
1061100 block. Local identifier: `traitmech:000659`.
Subset: `metpo_traitmech_2026_10`. Earlier cohorts remain unchanged.

Upstream default-branch HEAD was freshly verified at
`Knowledge-Graph-Hub/kg-microbe@1408e7099d039026d7611c240938d8e177753406`.
Canonical class/property blobs were rehashed to
`b590cf303dc2fbdd57bed021668641cd0c32396d` and
`b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990`.
The class-only template retains the 11-column headers, including three
required trailing empty directive cells.

The writer defaults to dry run, guards eight parent identity/scope fields
and exact initial/final target and template preimages, prevalidates before writing,
and supports idempotent replay. Curation provenance is LLM-assisted and
repository history is append-only.

## Files

| Artifact | Rows |
| --- | ---: |
| `metpo_proposal_classes_robot.tsv` | 1 class plus two header rows |
| Properties template | Omitted: no new predicates |
| SSSOM mappings | Omitted: no asserted exact external equivalence |

## Verification

The writer dry run, guarded application and 22 focused tests passed, including
the #1774 migration, unchanged prior history and refusal of altered evidence.
LinkML, strict corpus validation (1,054 records), proposal verification,
ROBOT/ELK, product validation and Ruff passed. Repository history validates
1,137 records with zero invalid links. The add-trait skill validator passed.

All four snippets were directly exact-matched to full-text XML. The maintained
resolver returned two VERIFIED and two NOT_IN_ABSTRACT rows. The Guy11 quote
is from Results; the expressorium scientific-Summary quote differs from the
API abstract only in its hyphen character. Replacing the source U+2010 with
ASCII matches that API passage, but the stored verbatim quote and actual
NOT_IN_ABSTRACT verdict are preserved. Online taxonomy audit resolved all
736 examples across 551 records: zero errors and 24 existing label warnings.

RDF parsing measured 15 class, 12,628 merged and 12,632 reasoned triples,
with canonical w3id METPO IRIs and the phenotype-to-quality hierarchy intact.
All 1,053 prior YAMLs, 539 historical proposal TSVs, prior proposal narratives
and discussion templates are unchanged. Of the prior trait pages, 1,052
have footer-only changes; phenotype also gains the child link. The only old
priority-row change is phenotype's child count from 154 to 155.

Desktop/mobile browser checks at 1,440 and 390 pixels passed for identity,
four quotes, the qualified example, two OPEN discussions, correction visibility,
hierarchy navigation, dashboard totals, image loading and absence of overflow
or JavaScript errors. Screenshots were visually inspected, including the final
surface correction and regenerated dashboard. The 101 focused artifact tests
passed before the correction; the post-correction full-suite result is recorded
in the PR validation receipt before merge. The initial full run passed 3,015
tests with two dependency warnings, but does not replace that final rerun.

The ordinary staged whitespace check flags only the template directive row's
three required trailing tabs. All three rows have 11 cells and both headers
match the pinned upstream template. Scoped checks pass with that exact path
excluded from ordinary checking and checked with blank-at-eol disabled.

Both exact configured embedding inputs are absent, so embedding artifacts
are not regenerated. All 139 source blobs of the isolated reviewed claw
generator were freshly reverified against its pinned tree; the unrelated
shared checkout is not modified.

## Upstream and Round Trip

Submit the class and explicit scope notes to upstream METPO after review.
No new upstream issue or acceptance is claimed. After acceptance, refresh
the ontology, migrate the local identifier and references to the accepted
METPO identifier, preserve local-ID traceability and append-only history,
and regenerate without creating a duplicate record. Scientific discussions
remain open until their evidence and mapping questions are resolved.

## Change Log

- v535, 2026-10-07: propose fungal appressorium formation with four directly
  checked primary-source snippets and a provenance-qualified Guy11 example.
- Address #1774 with section-attributed, unresolved assay-surface descriptions,
  guarded migration, append-only correction history and regression coverage.
