# Phagocytosis: METPO Proposal v503

## Context

Add `traitmech:000627 phagocytosis`, a PROPOSED PHYSIOLOGY class for the
microbial organism's capacity to engulf extracellular particles into
membrane-bound intracellular compartments. This is not a claim that a microbe
elicits host immune phagocytosis, possesses a particular sequence annotation,
or assimilates nutrients from every ingested particle.

Novelty searches included ignored and hidden files throughout TraitMech,
labels and related terminology, source DOI/PMID/PMC identifiers, the proposed
local ID and the complete new METPO hundred block. Existing capsule and
pathogenic-to-host mentions concern host immune evasion, not an unresolved
same-scope microbial trait node. A trophic-type research report supplies a
phagotrophy lead, not an existing primary record or independent evidence.
Structured examination of pinned METPO found no matching assertion.

The fresh 399-record seed shares 344 IDs with the 1,021-record pre-addition
working corpus. Its 55 absent IDs comprise 38 supporting-field terms and 17
duplicates. The complete 1,546-row release delta and 153-row active-review
table contain no matching candidate; all 38 formerly unselected classes are
now live. Seed depletion is not evidence that discovery is exhausted.

All-state upstream searches for phagocytosis, phagotrophy and endocytosis
returned no proposal on 2026-10-05. The open TraitMech and METPO PR heads were
rechecked against their inspected file inventories; no competing allocation
was found. This branch starts from the reviewed cannibalism commit in #1732
and must preserve that PR's separate review and merge lifecycle.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | METPO:1000059 phenotype |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

The phenotype parent is deliberately broader than trophic type. Uptake of
inert particles does not require the carbon, energy or electron-donor use in
`METPO:1000631 trophic type` or `METPO:1000644 heterotrophic`. The existing
predatory bacterium class is bacteria-specific and is not a parent for the
observed microbial eukaryotes. No existing parent or neighboring record is
changed, and no extra grouping class is minted.

Phagocytosis is not declared an exact synonym of phagotrophy, all endocytosis,
pinocytosis or bacterial predation. The coccolithophore paper uses phagotrophy
for its nutritional interpretation; the record preserves that attribution
without converting uptake images or calculated nutrient quotas into direct
assimilation measurements. Process-level ontology terms are not automatically
equivalent to an organismal phenotype. No xref or SSSOM mapping is asserted.

## Evidence and Exemplar

- `DOI:10.1371/journal.pone.0095577`, `PMID:24806026`, `PMC4012994`:
  scientific Abstract and main Results, Discussion and Methods directly read
  from Europe PMC XML and the publisher. Actual Figures 1 and 4 were inspected.
  The images support collar-associated engulfment and internalization in
  Salpingoeca rosetta, not merely particle contact. The culture-provenance
  references were not followed, so no canonical strain is assigned from this
  paper.
- `DOI:10.1111/nph.20388`, `PMID:40035416`, `PMC11982794`:
  scientific Summary and full Results, Discussion and Methods directly read.
  Actual Figures 5, 6, 9 and 10 were inspected. Distinguish pHrodo bacterial
  BioParticles, Acridine Orange-labeled marine bacteria and inert beads.
  Lysotracker positivity alone is insufficient for ingestion; some imaging
  uses EGTA decalcification. No comparator-species absence, plastic-degrading
  enzyme, figure-scale measurement or nutrient-quota estimate is imported.

Both evidence entries contain contiguous 17-word excerpts, checked against
the directly retrieved scientific sections with whitespace normalization.
The micrometre symbol in the second quote is retained from the source rather
than replaced with a fabricated ASCII quotation. Actual supplements and
movies were not inspected; unique claims from them are not imported.

The single canonical example is strain-qualified Scyphosphaera apsteinii
RCC1456 (AC504/TW15/NIES-3344), supported by the 2025 uptake experiments.
NCBI ESearch and EFetch independently resolve `NCBITaxon:418940` to the species
name and eukaryotic haptophyte lineage. That species ID is not presented as a
strain ID or an assertion about all isolates.

The collection's actual HTML was directly retrieved and read at
https://www.roscoff-culture-collection.org/rcc-strain-details/1456 : it records
natural single-cell isolation from the Spanish coast of the Balearic Sea on
2001-02-01. Provenance stays in the exemplar note and does not count as a third
independent trait-evidence citation. Blank text extractions of icon-based
collection status fields are not interpreted as biological assertions.

The transcript-source RCC1455 (AC505/TW16; independently checked at its own
collection page) is a different strain. The paper's Figure 10 is conceptual:
RCC1455 transcript annotations and Gephyrocapsa huxleyi gene models do not
validate native RCC1456 proteins. Collar-link identity in the choanoflagellate
is also unresolved. No protein accession or causal graph is inferred.

## ID Space and Artifacts

Reserve fresh block `1058000-1058099` and class `METPO:1058000`, following v502;
subset `metpo_traitmech_2026_10`. Ignored-and-hidden searches found no collision
with TraitMech, pinned METPO or CommunityMech proposal allocations.
The class template follows the upstream contract pinned at
`ea1c5f15e6c4dba6c72165367162b354e215f018`, using the w3id IRIs of the actual
vendored ontology. Citation fields contain publications, not ontology mappings.

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 |
| property template | Omitted |
| SSSOM mappings | Omitted |

## Verification

The guarded writer passed dry run and 11 focused tests, including replay,
preimage drift refusal and preservation of the parent. Direct LinkML and
strict validation passed. Both excerpts returned `VERIFIED` in the maintained
snippet resolver, separately from direct scientific-section inspection.
The live NCBI canonical-example audit resolved all 719 examples across 534
records with zero errors and 24 existing warnings; the new example resolves
without a warning.

Proposal verification and ROBOT ELK reasoning passed with no unsatisfiable
class. RDF parsing independently confirms the proposed child, its definition,
the real labeled phenotype parent and that parent's quality ancestor using
`https://w3id.org/metpo/` IRIs. `merged.owl` contains 12,628 RDF triples in
23,322 physical lines; `reasoned.owl` contains 12,632 triples in 23,326 lines.
These graph cardinalities are distinct from the wrapper's line counts.

Maintained generators refreshed the discussion browser, published QC
dashboard, priority dashboard and trait pages. Playwright checks passed at
1440- and 390-pixel widths for local identifier provenance, the two citations,
the strain-qualified example, reciprocal parent link, 1,022-record dashboard,
loaded coverage image, no document-level horizontal overflow and no JavaScript
errors. Screenshots were inspected; the existing floating mobile theme button
can overlap text, and the shared QC table has its own horizontal scroll area.
Neither pre-existing presentation behavior is claimed fixed here.

The complete base comparison found 1,020 existing trait pages changed only in
their footers; the phenotype parent's child count and new child link are the
sole substantive existing trait-page changes. Both exact configured DeepWalk
input paths are absent; embeddings were not regenerated. Existing trait YAML
and repository history are unchanged.

`just qc`, `just validate-history` and `just validate-products` passed. All
507 PROPOSED records meet the two-citation gate, and all 627 local identifiers
are covered by proposals. Existing audit baselines were not expanded. The
full test suite passed: 2,273 tests, with two dependency deprecation warnings,
in 1,276.05 seconds. This includes the README, priority and QC-dashboard tests.

The ordinary staged whitespace check flags only the three required trailing
empty ROBOT directive cells in the class template's second header. Both
headers and the data row parse as 11 columns. The exact-path scoped checks
passed with that narrow exception; no global whitespace setting was changed.

## Upstream and Round Trip

Submit the cohort for METPO review. After accepted IDs enter a release,
refresh the pinned ontology, migrate the local identifier and any references
to its accepted METPO ID, preserve local-ID provenance and append-only history,
and regenerate products without duplicate primary records. Until then the
TraitRecord uses its local ID and remains PROPOSED pending human signoff.

## Change Log

- v503, 2026-10-05: propose microbial phagocytosis with direct uptake evidence,
  a natural strain-qualified exemplar and explicit sequence-interpretation limits.
