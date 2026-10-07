# Fungal Arbuscule Formation: METPO Proposal v540

## Context and Novelty

Propose `traitmech:000664 fungal arbuscule formation`, a PROPOSED
MORPHOLOGY class, from main `76e2f1f663517f46c255d138d0e9782bce15a946`.
Whole-repository searches included ignored and hidden files, arbuscule labels,
likely slugs, both primary DOIs, candidate taxon and identifier reservations.
Existing mutualism research describes related interfaces, not a dedicated
formation phenotype. Mutualism `traitmech:000041` requires reciprocal benefit.
The new record links the exact boundary mention in microbial haustorium
formation `traitmech:000663`, without resolving its open hierarchy question.

Structured inspection of the 12,617-triple pinned METPO found no arbuscule
term. Related mycorrhization `METPO:1000198` is deprecated. A fresh temporary
seed produced 399 records, 344 already live by exact ID. The remaining 55
are 38 supporting-field terms and 17 previously reviewed duplicates, as
reconciled against the 1,546-row release delta and 153-row active review.
This finite frontier check does not establish global trait exhaustion.

## Scope and Hierarchy

| Scope | Classes or Predicates | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | METPO:1000059 phenotype |
| B: causal predicates | 0 | Not applicable |
| C: schema vocabulary | 0 | Not applicable |

This is a fungal formation phenotype, not a plant trait, structure, gene or
nutrient-transport process. Its plant-cell scope includes root cortex and
liverwort thallus parenchyma. It does not require measured nutrient flux,
reciprocal benefit, a universal onset or a fixed lifespan. Host membrane
markers are not fungal protein anchors. Within-cell location does not imply
free access to host cytoplasm.

Use the active phenotype class, whose quality ancestor is `METPO:1000188`.
Direct QuickGO authority checks resolve `GO:0085041 arbuscule` as a cellular
component below `GO:0085035 haustorium`. Preserve that attributed umbrella
usage rather than silently declaring the interfaces disjoint. A structural
ontology hierarchy does not automatically settle the organism-level formation
phenotypes: no subclass, equivalence or disjointness between this record and
`traitmech:000663` is asserted. GO's root-cortex wording is also narrower
than the directly observed liverwort scope. No exact synonyms, xrefs or
SSSOM mappings are proposed. A closer parent remains OPEN.

## Evidence and Example

| Reference | Direct Evidence |
| --- | --- |
| [10.1104/pp.109.141879](https://doi.org/10.1104/pp.109.141879) | Primary microscopy study; scientific abstract and main text, actual Figures 1-7 and supplementary Figures S1-S9 inspected; supplementary movie not viewed |
| [10.3390/plants8060142](https://doi.org/10.3390/plants8060142) | Primary liverwort study; pages 1-11, main Figures 1-4 and all four supplementary pages inspected; Results 2.2, Methods 3.2 and actual S1 support the culture-qualified example |

The record contains contiguous 19- and 12-word snippets, respectively from
the scientific abstract and Results 2.2. The first experiment used transgenic
Medicago roots and lacks verified fungal-isolate provenance for a natural
canonical example. The second supports the definition beyond roots, but its
DAOM197198 onset descriptions conflict between main text and S2 captions.
The record preserves this disagreement, the 4B/4C panel-pointer mismatch,
dps/dpi discrepancy and phylogenetic-method inconsistency. Pigmentation and
mixed field rDNA are not substitutes for observed arbuscules or species IDs.

The example is specifically MAFF520053 (H1-1), not the plant host. Its
[NARO collection record](https://www.gene.affrc.go.jp/databases-micro_search_detail_en.php?maff=520053)
establishes soybean-field origin in Tokyo in October 1987. Collection fields
remain example provenance, not a synthesized snippet or independent trait
experiment. The paper's Claroideoglomus etunicatum is a homotypic synonym
under the current [NCBI species record](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=937382)
for `NCBITaxon:937382 Entrophospora etunicata`. This is name correspondence,
not independent culture reidentification. The protein-resolved formation
graph is deferred pending appropriate perturbation and protein evidence.

## ID Space and Subset

Reserve `METPO:1061700` in the whole block `1061700-1061799`, cohort v540,
subset `metpo_traitmech_2026_10`. The preceding v539 block is not reused.
Ignored-and-hidden reservation checks included main, every listed local
worktree, CommunityMech proposals and downloaded immutable-head curation
artifacts from all paginated open PRs, including drafts. No prior use of
the new local ID, cohort or whole block was found before allocation.

The exact-head snapshot contained #1782 (`35099af2b7d5347f2ca6e418c4a139979071644d`),
#1734 (`ca9b337ec3d24806baf16b42b8f384087701280e`),
#1476 (`a138e46f803b5af9d48969217b86cf7c9a3b61bd`),
#973 (`331f9517bbdf4d2c9fa97b338ee59a8986f2f174`) and draft
#924 (`e61ce120b8da953da097b9f94bfed7f292e5675a`). Only #1734 changes
curation artifacts: 11 existing traits and three history records, without
a new trait ID or proposal reservation. Artifact blob SHAs and PR head
stability were checked. Immediately before the first publication, fetched
main remained at the branch base and the complete paginated open-PR head
set and local worktree inventory were unchanged.

The kg-microbe upstream contract is pinned at
`1408e7099d039026d7611c240938d8e177753406`. Canonical class-header blob
`b590cf303dc2fbdd57bed021668641cd0c32396d` has 11 columns; property-header
blob `b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990` has 13. The class directive
row retains its three required trailing blank cells. The maintained wrapper
must emit `https://w3id.org/metpo/` IRIs, not legacy METPO stubs.

## Files and Mutation

| Artifact | Rows |
| --- | ---: |
| `metpo_proposal_classes_robot.tsv` | One class plus two headers |
| `metpo_proposal_properties_robot.tsv` | Not emitted; no predicates |
| `metpo_proposal_mappings.sssom.tsv` | Not emitted; no exact mapping |

The writer is dry-run by default and guards the phenotype parent projection,
the full haustorium semantic preimage and exact new-record/template replay.
Both records are prevalidated before application. The haustorium edit appends
only a boundary reference and curation event; the discussion stays OPEN.
Both changes use `write_validated_trait` and `record_curation_event`, with
separate append-only repository history. No protected record is modified.

## Verification

The writer dry run and all 27 focused tests passed. LinkML/strict record
validation, proposal verification, ROBOT/ELK, `just validate-history` and
`just validate-products` passed. Full QC and focused/full test-suite runs
remain in progress; no independent approval or merged state is claimed.

The maintained snippet resolver reports one VERIFIED scientific-abstract
quote and one NOT_IN_ABSTRACT full-text quote. Both are exact contiguous
matches in directly retrieved primary text. The initial sandbox DNS failure
was not counted as a pass; the network-enabled rerun produced these verdicts.
The online taxonomy audit resolved 741 examples across 556 records with no
errors and 24 existing warnings, none on the new example.

Maintained recipes regenerated discussion data, both dashboards, pages and
grounding/coverage reports. A parsed audit confirmed 1,057 existing YAMLs
are byte-identical; the haustorium record differs only by its appended link
and event. All historical history, 544 prior proposal TSVs and prior proposal
narratives are unchanged. Of 1,058 old trait pages, 1,056 differ only in the
footer; the other two show the intended haustorium discussion and phenotype
child. The only old priority-row delta is phenotype's child count, 159 to 160.
The corpus has 1,059 unique records. The protected YAML is unchanged.

RDF inspection counted 15 class, 12,628 merged and 12,632 reasoned triples,
with the expected definition, citations and phenotype-to-quality hierarchy
under `https://w3id.org/metpo/`; no legacy METPO stub is introduced.
Headless Chrome checks and inspected screenshots passed at 1,440 and
390 pixels: identity provenance, both snippets, qualified example, two OPEN
discussions, history, parent navigation, browse search and dashboard counts
and image loading, without horizontal overflow or JavaScript errors.
Neither exact configured embedding source exists, so embedding products
were not regenerated. Both history actors are explicitly Codex:
`history/records/fungal_arbuscule_formation/2026-10-07T132515Z-codex-7af269.yaml`
and `history/records/microbial_haustorium_formation/2026-10-07T132517Z-codex-b76f8d.yaml`.

## Upstream Path and Round Trip

After TraitMech review, submit the class template and hierarchy questions to
berkeleybop/metpo or the kg-microbe proposal pipeline. The placeholder is not
a released identifier and is not the live TraitRecord ID.

After upstream accepts an equivalent class, update the pinned ontology and
seed into a temporary tree. Inspect the accepted scope and hierarchy before
migrating the local identifier. Preserve the old local ID as provenance,
not a lexical synonym; reconcile references, append history, regenerate
derived artifacts and rerun the gates.

## Change Log

- 2026-10-07: Propose fungal arbuscule formation with root and thallus evidence,
  a culture-qualified example and an unresolved haustorium boundary link.
