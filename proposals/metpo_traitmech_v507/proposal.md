# Myzocytosis: METPO Proposal v507

## Context

Add `traitmech:000631 myzocytosis`, a PROPOSED PHYSIOLOGY class for feeding
by aspiration of prey cell contents through a localized connection, rather
than whole-prey engulfment. This is an organismal phenotype, not a literal
feeding apparatus or a sequence feature.

Ignored-and-hidden searches across TraitMech and CommunityMech proposals
found no exact record, prior proposal, same-scope unresolved mention or ID
collision. Searches covered lexical variants, peduncle/tube feeding,
cytoplasm aspiration and the evidence DOIs. Structured inspection of the
12,617 pinned METPO triples found no exact term or collision in either
w3id or legacy METPO IRIs. All-state TraitMech/METPO PR searches found no
myzocytosis proposal or reservation of 1058400; open PR heads are unchanged
from their previously inspected inventories. Base main is
`5263a12db15cd8bc3f00cb70b66f97c6895f63fc`.

A fresh 399-record seed shares 344 IDs with the 1,025-record pre-addition
corpus. Its 55 absent IDs reconcile to 38 supporting-field terms and 17
reviewed duplicates, all with live replacements. The complete 1,546-row
release delta and 153-row active review were parsed and compared with live
records and history; all 38 formerly unselected classes are now live.
This reconciliation does not establish literature exhaustion.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | METPO:1000059 phenotype |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

The 2023 Discussion uses apical phagotrophy and endocytosis while arguing
against phagocytosis and trogocytosis for its system. The 2012 Introduction
uses phagocytise for tube-mediated uptake; the 2024 paper contrasts
myzocytosis with conventional phagocytosis. These are source-attributed
usages, not an established universal subclass relationship under the local
operational definitions. Phagocytosis `traitmech:000627` requires particle
enclosure/internalization; phagotrophy `traitmech:000628` requires
particulate ingestion and nutrient assimilation. Keep phenotype as the
parent pending closer feeding-mode hierarchy review.

Mere attachment, free-particle endocytosis, extracellular digestion, an
apparatus-like sequence or inferred homology is insufficient. Do not require
mechanical piercing, unicellular prey, prey death, encystation or a posterior
food vacuole. A microbe may use multiple modes, so possession traits are not
declared disjoint. No exact synonym, ontology xref, protein accession or
causal graph is asserted. No existing YAML requires an exact-mention repair.

## Evidence and Example

- `DOI:10.3390/microorganisms11081945`, `PMID:37630505`, `PMC10458597`:
  directly retrieved scientific Abstract and main text, with actual Figures
  7-9 inspected. The Introduction/Conclusions support aspiration; fixed-cell
  TEM does not establish every transition by live observation. Free bead
  uptake is separate from prey feeding. Figures 1-6 were not visually audited.
- `DOI:10.1111/jeu.13050`, `PMID:39019843`, `PMC11603288`: scientific
  Abstract, culture and fluorescence Methods, feeding Results/Discussion,
  and actual supplementary Figure S6 with its caption were inspected.
  The quote is from Results, not the abstract. SPMC98 supplied imaging;
  SPMC100 supplied molecular data. S6D shows deformed prey material in the
  peduncle; S6E attachment alone is not uptake. Other supplementary figures,
  molecular datasets and movies were not audited.
- `DOI:10.1038/ismej.2012.29`, `PMID:22513533`, `PMC3446796`: main text and
  actual Figure 2 inspected. The snippet is an Introduction terminology
  span, not an independent naming experiment. Results support metazoan
  prey scope, but nematode feeding was not directly observed. K-0688 in the
  abstract conflicts with K-0668 in initial Methods/Table 1; no canonical
  strain is assigned from this paper. Other figures and supplementary movies
  were not visually audited. No toxin or statistical-significance claim is
  imported from its proposed mechanism or Figure 4 caption.

The qualified canonical example is `NCBITaxon:160603 Oxytoxum lohmannii`,
imaged isolate SPMC98. NCBI independently resolves the scientific name,
species rank and Amphidinium longum synonym. The 2024 Methods document
natural isolation near Anacortes in 1993; the same DOI provides the
provenance URL, not an extra evidence publication. The strain was lost in
2004 and is not silently replaced by SPMC100. Feeding mode varies with prey.

The original 1984 naming article (`DOI:10.1007/BF00490442`) was available
only as metadata/preview. It is an unread lead, not counted evidence or
definition authority. Primary morphology does not establish homologous
protein function or a universal apicomplexan invasion mechanism.

## ID Space and Files

Reserve `METPO:1058400` in the fresh 1058400-1058499 block after v506's
1058300 block. Use subset `metpo_traitmech_2026_10`. One local record uses
the next available `traitmech:000631` ID. The canonical kg-microbe contract
and class/property templates at `ea1c5f15e6c4dba6c72165367162b354e215f018`,
CommunityMech v1 and TraitMech v506 informed this cohort. Use the pinned
ontology's w3id METPO IRIs, not the legacy example prefix.

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 |
| property template | Omitted |
| SSSOM mappings | Omitted; no equivalence asserted |

Definition provenance contains publications and the local minting record,
not an ontology mapping. Both template header rows retain 11 cells.

## Verification

- Guarded dry run, application and 12 focused tests passed, including replay,
  preimage drift refusal and parent preservation. LinkML and strict record
  validation passed; 1,096 repository history records have valid links.
- The snippet resolver returned one `VERIFIED` scientific-abstract quote
  and two `NOT_IN_ABSTRACT` full-text quotes. All three spans were directly
  exact-matched to their stated source sections; the manual checks do not
  replace the resolver verdicts. The NCBI audit resolved all 723 examples
  across 538 records, with zero errors and 24 pre-existing warnings.
- Proposal verification and ROBOT/ELK passed. RDF parsing counted 15 triples
  in classes.owl, 12,628 in merged.owl and 12,632 in reasoned.owl. The new
  w3id class has phenotype as its parent, with the pinned phenotype label
  and quality hierarchy intact; no legacy METPO stub is introduced.
- `just validate-history`, `just validate-products`, `just qc` and Ruff
  passed; the full test suite passed 2,318 tests with two dependency
  deprecation warnings. Graph findings remain 74 baselined, zero new or blocking; snippet
  findings remain 2,419 baselined, zero new or blocking. No baseline,
  existing TraitRecord, existing history or protected record was changed.
- Maintained generators produced 1,026 pages, current priority artifacts,
  553 discussions and a 1,026-record QC dashboard with zero failing slots.
  The reviewed claw source matched its pinned archive byte-for-byte.
  All 1,024 unrelated existing trait pages differ only in footer counts;
  phenotype additionally gains the expected child link. Priority's only
  existing-row change is phenotype's child count, 138 to 139.
- Chromium checks at 1440 and 390 pixels passed identity, three quotations,
  the strain-qualified example, parent navigation, dashboard counts, image
  loading and document-overflow assertions, with no page errors. Screenshots
  were inspected; the existing floating theme control is not redesigned.
  Embeddings were not regenerated because both exact configured source
  paths are absent.
- Both TSV header rows retain 11 cells. The directive header's three required
  trailing tabs use the documented exact-path whitespace exception, not a
  global Git setting or weakened template.

Local validation does not substitute for exact-head review, CI or the native
merge queue. The record remains PROPOSED pending human signoff.

## Upstream and Round Trip

Submit this cohort for METPO review. After the accepted term enters a
release, refresh the ontology, migrate the local identifier and references
to the accepted METPO ID, preserve the minting provenance and append-only
history, and regenerate artifacts without creating a duplicate primary
record. Parent interpretation and molecular mechanism remain explicit TODOs.

## Change Log

- v507, 2026-10-06: propose myzocytosis with three DOI-backed snippets,
  one natural strain-qualified example and explicit scope/mechanism limits.
