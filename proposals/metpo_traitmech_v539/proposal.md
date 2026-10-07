# Microbial Haustorium Formation: METPO Proposal v539

## Context and Novelty

Propose `traitmech:000663 microbial haustorium formation`, a PROPOSED
MORPHOLOGY class. This branch starts from main
`6c9911a8ab8b0ba61a5b1b4b65d7300594a5d066`, independently of the pending
rhizomorph PR #1783. Its `traitmech:000662`, v538 and `1061500-1061599`
reservation are deliberately not reused. Each branch adds only its own trait;
generated artifacts must be regenerated after either branch merges first.

Whole-repository searches included ignored and hidden files, haustorium and
arbuscule variants, source DOIs, GO candidates, proposed IDs and cohort names.
Mentions in plant-pathogen and mutualism research are evidence leads, not
existing TraitRecords. The appressorium record's statement that penetration
does not prove a functional haustorium remains true and is not an unresolved
exact grounding. No exact existing record or proposal was found. CommunityMech
proposals were included in the ID-block search.

Structured inspection of the pinned 12,617-triple METPO ontology found no
haustorium or arbuscule annotation. The related `METPO:1000198 mycorrhization`
is explicitly deprecated and is not a usable parent. A fresh temporary seeder
emitted 399 records with 344 exact IDs shared with the live corpus. The 55
absent IDs are 38 supporting fields and 17 previously reviewed duplicates.
The 153-row active-review table and 1,546-row release delta were read
structurally; every formerly unselected class is now live. The new branch has
1,057 records after this addition. These checks do not establish global
exhaustion; credible microbial traits remain.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | METPO:1000059 phenotype |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

This is an organism-level formation phenotype, not a structure identifier,
gene or host observation. It covers fungal and oomycete hyphal host-interface
outgrowths. It does not require a plant host, lifelong obligate biotrophy,
fixed shape, pathogenicity, demonstrated nutrient flux or one membrane topology.
Parasitic-plant haustorial organs are outside its microbial hyphal scope.

`traitmech:000659 fungal appressorium formation` concerns surface-associated
penetration structures, not the intimate host-cell interface. Plant pathogen
`METPO:1004003` cannot be a required parent because mycoparasitic fungal hosts
are directly supported. The active phenotype parent has the expected quality
ancestor `METPO:1000188`. Existing records are unchanged.

Direct QuickGO JSON resolves `GO:0085035 haustorium` and
`GO:0085041 arbuscule` as cellular components, and `GO:0052094 formation of
haustorium for nutrient acquisition` as a biological process. None is an
exact organism-level phenotype. GO places arbuscule below haustorium, while
literature contrasts these named interfaces: the Introduction of
[Huisman et al. (2015)](https://doi.org/10.1094/MPMI-06-15-0130-R), read in the
[institutional primary PDF](https://dspace.library.uu.nl/bitstream/handle/1874/324900/mpmi-06-15-0130-r.pdf?sequence=2),
compares arbuscules and haustoria and their respective membrane interfaces.
This terminology check is not a fifth formation experiment or an assertion of
ontological disjointness. That umbrella usage remains
explicit: this definition is not parasitism-only, but no arbuscule synonym,
subclass or equivalence is invented. GO's invagination definition also differs
from the direct tremelloid cytoplasmic connections. No xrefs, exact synonyms
or SSSOM mappings are asserted; a closer parent and boundaries remain OPEN.

## Evidence and Example

| Reference | Directly Inspected Material |
| --- | --- |
| [10.1016/j.fgb.2014.08.006](https://doi.org/10.1016/j.fgb.2014.08.006) | Primary Podosphaera microscopy paper, PMID:25151531; abstract, Introduction, Methods and main text; actual Figures 2-4 and complete pages 24-26 |
| [10.1080/00275514.1994.12026373](https://doi.org/10.1080/00275514.1994.12026373) | Primary Tremella study; all eight pages and actual Figures 1-16 visually inspected; Crossref DOI metadata checked |
| [10.1111/mpp.13072](https://doi.org/10.1111/mpp.13072) | Primary Phytophthora study, PMID:34018655, PMC8295517; scientific abstract, Results 2.1, Figure 1 caption and Methods 4.1/4.6/4.7 from full-text XML |
| [10.1104/pp.18.00979](https://doi.org/10.1104/pp.18.00979) | Judelson and Ah-Fong review, PMID:30538168, PMC6446794; publisher HTML interface and nutrient-acquisition passages, not a new experiment |

The four contiguous snippets contain 14, 16, 21 and 12 words. The Podosphaera
source supplies fungal definition authority; the other sources establish the
mycoparasitic and oomycete scope and its limits. Its Figure 3 caption describes
a separated plant interface, which is not universalized. Callose correlation
and proposed lobe functions are not a complete formation mechanism.

The strongest fully inspected natural example is `NCBITaxon:5217 Tremella
mesenterica`. Methods identify field collections on Carpinus betulus adjacent
to Peniophora laeta at Haldenwald near Sonnenberg, Stuttgart, on 8 June 1987
and 20 November 1989 (W. Zugmaier 97 and 158). Field Results and images
demonstrate haustorial cells and filaments. Individual figures are not assigned
to one voucher. The separate crossed monospore culture is not presented as
an unmodified field isolate, nor is field material equated to NCBI type strain
CBS 6973. Direct NCBI Taxonomy resolves ID, current label and species rank.
The 1994 print date differs from the 2018 online-publication date.

Tremelloid micropore observations show why cytoplasmic separation cannot be a
universal criterion. Some attached filaments lacked an observed continuous
micropore; static images do not measure feeding flux. The Phytophthora study
used engineered PkGFP8 and a transgenic host membrane marker. Its Results say
likely and its natural-host caption says appeared; natural host does not mean
unmodified pathogen. It is not used as a natural canonical example.

The 2019 review separates established effector secretion from the nutritional
role then unresolved in oomycetes. That is a dated review assessment, not a
present-day absence claim. No shared protein-resolved formation graph is
asserted without primary perturbation evidence and verified protein examples.
Uninspected figures, Methods portions and supplements remain identified in
each evidence note rather than being implied as reviewed.

## ID Space and Subset

Reserve `METPO:1061600` within fresh block `1061600-1061699`, cohort v539.
Pending v538 holds the preceding block. Ignored-and-hidden searches found no
prior use of this ID, local identifier, cohort or block, including CommunityMech
proposals. Subset: `metpo_traitmech_2026_10`.

The pinned kg-microbe `master` commit was rechecked as
`1408e7099d039026d7611c240938d8e177753406`. The canonical headers were
retrieved and decoded: class blob `b590cf303dc2fbdd57bed021668641cd0c32396d`
(11 columns) and property blob `b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990`
(13 columns). Preserve the three trailing blank class directive cells and
use the pinned ontology's `https://w3id.org/metpo/` IRIs, not legacy stubs.

## Files and Mutation

| Artifact | Rows |
| --- | ---: |
| `metpo_proposal_classes_robot.tsv` | 1 class plus two headers |
| `metpo_proposal_properties_robot.tsv` | Not emitted; no predicates |
| `metpo_proposal_mappings.sssom.tsv` | Not emitted; no asserted equivalence |

The writer defaults to dry-run, guards the eight-field parent projection and
exact target/template preimages, prevalidates through `write_validated_trait`
and records an LLM-assisted mint event. Exact replay is idempotent. Twenty
focused tests passed before application. Append-only repository history:
`history/records/microbial_haustorium_formation/2026-10-07T105906Z-codex-95ae40.yaml`.
Both history layers explicitly attribute Codex.

## Verification

Twenty writer tests and dry-run passed. LinkML and strict record validation,
`just qc` (including strict corpus validation), `just validate-history`,
`just validate-products`, proposal verification and ROBOT/ELK validation passed.
All 65 focused writer, README, priority and QC-dashboard regression tests passed.
The full pytest run passed all 3,085 collected tests with two dependency
deprecation warnings. That run collected before the #1785 regression was added;
all nine guidance tests, including the new regression, passed separately.
Final writer dry-run, full-tree Ruff and PR sanity also passed. Ordinary staged whitespace checking flags
only the class directive header's three required trailing blank cells. Both
scoped checks passed: ordinary checking excluding that exact TSV, and checking
that TSV with `core.whitespace=-blank-at-eol`. No global setting was changed.

The online NCBI audit resolved all 739 examples across 554 records with zero
errors and 24 pre-existing label warnings. The maintained snippet resolver
reported one VERIFIED scientific-abstract quote, one NOT_IN_ABSTRACT Figure 3
quote and two UNRESOLVED quotes. All four were checked in directly retrieved
sources. The 2019 review's exact PMID resolves with its matching DOI in Europe
PMC but no `abstractText`; that is not an unindexed-paper claim. The 1994
primary PDF and Crossref DOI were independently checked. Manual full-text
confirmation does not change either UNRESOLVED verdict.

Maintained recipes regenerated discussions, both dashboards, pages and
grounding/coverage reports. A parsed artifact audit confirmed all 1,056 old
TraitRecord YAML files, 542 historical TSVs, historical proposal narratives and
discussion templates are byte-identical. Of the old trait pages, 1,055 differ
only in their footer; the phenotype page additionally lists the new child.
The only existing priority-row change is that parent's child count, 157 to 158.
RDF parsing counted 15 class, 12,628 merged and 12,632 reasoned triples and
verified the new label, definition, citations and active phenotype-to-quality
hierarchy under `https://w3id.org/metpo/`, without legacy METPO stubs.

Headless Chrome checks passed at 1,440- and 390-pixel viewport widths:
local-identifier provenance, four quotes, qualified example, two OPEN
discussions, history link, parent navigation, browse search, dashboard counts
and image loading, without horizontal overflow or JavaScript errors. Desktop
and mobile screenshots were visually inspected. Neither exact configured
embedding source exists in the main checkout or isolated worktree, so embeddings
were not regenerated; the existing tracked embedding products were retained.
GitHub review, required CI, actual merge and post-merge cleanup remain pending.

## Adversarial Review Follow-Up

Local review identified workflow issue #1785: the identifier skill's
checkout-only next-number recipe could reuse a pending PR's reservation. This
branch already avoided #1783's IDs. The add-trait, identifier and proposal
skills now require fresh main, local-worktree and paginated open-PR checks,
including drafts and exact-head proposal narratives for whole reserved blocks.
Unavailable remote state is not treated as availability, and publication needs
a fresh recheck. The documented API inventory command was exercised; nine
guidance regression tests and Ruff passed. No TraitRecord or allocation changed
in this follow-up. Local review is not an independent review.

## Upstream Path and Round Trip

After TraitMech review, submit the class template and the explicit boundary
questions to berkeleybop/metpo or the kg-microbe proposal pipeline. This
same-PR proposal is not an upstream release or an equivalence decision.

When an upstream release accepts an equivalent class, update the ontology,
seed into a temporary tree and inspect the exact accepted scope and hierarchy.
Migrate only after equivalence review; retain `traitmech:000663` as provenance,
not an exact lexical synonym. Reconcile references, append history and
regenerate all derived artifacts and gates. Do not emit the unreleased
placeholder as the live record identifier.

## Change Log

- 2026-10-07: Propose microbial haustorium formation with source-qualified
  fungal and oomycete interfaces and a field-observed canonical example.
- 2026-10-07: Address #1785 with pending-reservation checks in the curation
  skills and focused guidance regression coverage.
