# Fungal Branched Absorbing Structure Formation: METPO Proposal v541

## Context and Novelty

Propose `traitmech:000665 fungal branched absorbing structure formation`, a
PROPOSED MORPHOLOGY class, from main
`8e9a7b7c121e41e595c6161e6c0e925b6b42ec17`. A whole-repository search included
ignored and hidden files, BAS terminology, arbuscule-like variants and the
1998, 2019 and 2020 DOI leads. It found no matches across 37,839 searched
files (1,325,204,330 bytes). This lexical evidence was checked against the
actual scope of neighboring records, not treated as sufficient by itself.

The 12,617-triple pinned ontology has no matching BAS term. Its branched
shape class is not the same differentiated architecture; mycorrhization is
obsolete. A fresh temporary seed emitted 399 records, of which 344 are
already live. The remaining 55 comprise 38 supporting-field terms and 17
reviewed duplicates, reconciled against the 1,546-row release delta and
153-row active-review table. This is not a global exhaustion claim.

## Scope and Hierarchy

| Scope | Count | Parent |
| --- | ---: | --- |
| A: synthetic trait class | 1 | METPO:1000059 phenotype |
| B: causal predicates | 0 | Not applicable |
| C: schema vocabulary | 0 | Not applicable |

The differentia is a localized, differentiated, progressively finer,
dichotomously branched architecture on extraradical runner hyphae of an
arbuscular mycorrhizal fungus. It is not the bare structure, general hyphal
branching, a sequence feature, or a nutrient-uptake assertion.

`METPO:1000687 branched shaped` and `METPO:1000674 filament shaped` concern
cell shape. `traitmech:000074 mycelial growth` is explicitly bacterial.
`traitmech:000664 fungal arbuscule formation` concerns structures within
living plant cells; the old arbuscule-like name does not make BAS arbuscules.
Appressoria (`000659`) concern penetration, hyphal anastomosis (`000605`)
fusion, and pseudohyphal growth (`000653`) budding-cell chains. The 1998
paper also separates pre-infection fan-like structures and aborted short
branches. None supplies an exact duplicate or a settled closer parent.

Use the active phenotype parent and its quality ancestor `METPO:1000188`.
A closer morphological parent remains OPEN. No exact synonyms, structure
xrefs, SSSOM mappings, or organism-level disjointness are asserted. The name
does not make measured absorption, host contact, sporulation, a fixed onset,
or a universal lifespan part of the definition.

## Evidence and Example

- [Bago et al. (1998)](https://doi.org/10.1046/j.1469-8137.1998.00199.x):
  primary Summary, Methods, Results and selected Discussion passages read.
  The snippet is the contiguous defining phrase in the Summary. Actual
  figures were not inspected after download/screenshot failures. Do not
  confuse the publisher's later online date with the 1998 study year.
- [Kameoka et al. (2019)](https://doi.org/10.1093/pcp/pcz122), PMID:31241164:
  primary publisher text and actual Figure 1 inspected. The Introduction
  snippet describes differentiation on runner hyphae. Figure 1C/G and Methods
  directly support the DAOM197198 morphology example. Remaining figure
  images and supplementary spreadsheet contents were not inspected.

The 1998 negative axenic result concerns the media tested. The 2019
transcriptome comparisons support hypotheses, not direct uptake or causal
formation mechanisms; mixed samples and the artificial host culture remain
qualified. Neither a seven-day development observation nor that paper's
historical assessment of uptake evidence becomes a universal/current claim.
The later asymbiotic growth paper DOI:10.1073/pnas.2006948117 is a
BAS-specific full-text/figure follow-up, not counted BAS evidence. A protein
graph is deferred, not claimed absent.

The example is `NCBITaxon:588596 Rhizophagus irregularis`, explicitly
DAOM197198 in a six-week carrot hairy-root coculture, not the plant host.
The [Canadian GINCO collection catalogue](https://agriculture.canada.ca/en/agricultural-science-and-innovation/agriculture-and-agri-food-research-centres-and-collections/glomeromycota-vitro-collection-ginco/catalogue-arbuscular-mycorrhizal-fungi-strains-available-glomeromycetes-vitro-collection)
records Pont-Rouge tree-plantation origin, collectors/isolators C. Plenchette
and V. Furlan, and aliases DAOM181602/MUCL43194. Its separate fields remain
provenance, not a manufactured snippet or independent trait experiment.
Direct NCBI taxonomy XML confirms the species and its strain 747089,
`Rhizophagus irregularis DAOM 181602=DAOM 197198`. Preserve the 1998 paper's
historical Glomus intraradices designation without treating the two species
as synonyms or claiming independent reidentification of the culture.

## Reservations and Templates

Reserve `METPO:1061800` within the whole block `1061800-1061899`, cohort
v541, subset `metpo_traitmech_2026_10`. The local maximum was 664 and the
latest cohort v540, but allocation additionally checked ignored/hidden
current-main files, every local worktree, CommunityMech and all paginated
open PR artifacts, including drafts. No prior ID, cohort or block use was
found across 137,924 searched files (2,529,018,453 bytes). A separate pending
worktree/PR novelty scan covered 18,069 files and found no candidate match.

Immutable-head reservations were inspected for #1782
(`35099af2b7d5347f2ca6e418c4a139979071644d`), #1734
(`ca9b337ec3d24806baf16b42b8f384087701280e`), #1476
(`a138e46f803b5af9d48969217b86cf7c9a3b61bd`), #973
(`331f9517bbdf4d2c9fa97b338ee59a8986f2f174`) and draft #924
(`e61ce120b8da953da097b9f94bfed7f292e5675a`). Only #1734 changes curation
artifacts: 11 existing traits and three history records, no new IDs or
proposals. All downloaded artifact Git blob hashes were verified and the
open-head set remained stable after collection. Remote main and the complete
paginated open-PR head set were rechecked before publication and remained
unchanged; all other local worktrees retained their inspected revisions.

The upstream contract is pinned at kg-microbe
`1408e7099d039026d7611c240938d8e177753406`. Fresh content checks verified
class-template blob `b590cf303dc2fbdd57bed021668641cd0c32396d` (11 columns)
and property-template blob `b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990`
(13 columns). Preserve the class directive row's three empty trailing cells.
Use the maintained ROBOT wrapper's real `https://w3id.org/metpo/` IRIs,
not legacy stubs from older upstream examples.

## Mutation and Verification

The writer defaults to a validated dry run, guards the phenotype projection
and exact target/template replay, and uses `write_validated_trait` plus
`record_curation_event`. All 20 writer tests and the pre-application dry run
passed. No existing trait is edited. Repository history was scaffolded with
the actual Codex actor and remains append-only.

Direct LinkML/strict validation, ROBOT/ELK, proposal verification, repository
history/products, full-tree Ruff and online taxonomy validation passed.
All 742 examples resolved with no errors and 24 pre-existing warnings. The
online snippet audit verified the 1998 Summary phrase; the 2019 Introduction
phrase was not in the abstract and was instead exact-matched in the primary
publisher HTML. Both snippets are contiguous, at 15 and 13 words.

Artifact review preserved all 1,059 prior trait YAMLs, all prior history and
proposal narratives, and all 545 historical class templates byte-for-byte.
Of the existing trait pages, 1,058 changed only their corpus-count footer;
the phenotype page additionally gained the new child. RDF review found 15
proposal, 12,628 merged and 12,632 reasoned triples, with the expected
definition/citations, phenotype/quality ancestry and current METPO IRIs.
Browser checks at 1,440 and 390 pixels passed evidence, example, history,
navigation, browse-search and dashboard checks without overflow or browser
errors. Screenshots were visually inspected. Embedding sources were not
available, so existing embedding products were preserved.

The full record, proposal/RDF, snippet, online taxonomy, history/products,
QC, focused/full test and browser gates are required before merge. Their
outcomes and adversarial review findings must be recorded on the PR; a
writer test pass alone is not that validation. Regenerate affected products
through maintained recipes, preserve historical proposals/history and
protected data, and inspect page churn and identity provenance.

Use the normal native merge queue, confirm actual MERGED state, reconstruct
the landed tree against the reviewed head, then delete the local/remote
feature branch. Independent-review availability and any quota failure must
not be described as review or approval.

## Upstream Round Trip

After TraitMech review, submit this one-class ROBOT template and the open
hierarchy question to METPO or the kg-microbe proposal pipeline. No property
or SSSOM file is emitted without a supported predicate or equivalence. This
placeholder is not a released METPO identifier and is not the live record ID.

After upstream acceptance, refresh the pinned ontology and seed into a
temporary tree. Check the accepted meaning and parent before migrating the
local ID; retain it as provenance rather than a lexical synonym. Reconcile
references, append history, regenerate artifacts and rerun the gates.
