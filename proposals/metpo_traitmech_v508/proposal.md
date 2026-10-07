# Pallium Feeding: METPO Proposal v508

## Context

Add `traitmech:000632 pallium feeding`, a PROPOSED PHYSIOLOGY class for
enveloping particulate food in a pallium and digesting it outside the main
cell body. This is an organismal feeding phenotype, not a literal apparatus
or sequence feature.

Ignored-and-hidden searches across TraitMech and CommunityMech proposals
found no exact record, prior proposal, same-scope unresolved mention or ID
collision. Searches included pallium, pallial, feeding veil, the evidence
DOIs and the entire prospective ID block. Structured inspection of the
12,617 pinned METPO triples found no exact term or occupied w3id/legacy
1058500-1058599 IRI. All-state TraitMech/METPO PR searches returned no
pallium proposal or 1058500 reservation. Base main is
`f10002e27edb565dd851088c172c3ab98e3e96f0`.

A fresh 399-record seed shares 344 IDs with the 1,026-record pre-addition
corpus. The 55 absent IDs reconcile to 38 supporting-field terms and 17
reviewed duplicates with live replacements. The complete 1,546-row release
delta and 153-row active review were parsed against the live inventory;
all 38 formerly unselected classes are now live. This is not a claim that
the microbial trait literature is exhausted.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | METPO:1000059 phenotype |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

Retain phenotype pending a closer feeding hierarchy. The 1986 Discussion
uses intracellular digestion for complete enclosure outside the theca and
extracellular digestion for partial enclosure, questioning the distinction.
Its engulfment terminology must not silently become whole-particle entry
into the main cell body. Local phagocytosis `traitmech:000627` requires
enclosure/internalization; phagotrophy `traitmech:000628` requires
particulate ingestion and assimilation. Myzocytosis `traitmech:000631`
instead denotes aspiration through a localized feeding connection.

Keep all-or-part enclosure and particulate-food scope. Do not require
living prey, diatoms, particular prey size, capture filament or digestion
time. Generic extracellular digestion and attachment are insufficient.
No organism-level disjointness, exact synonym, ontology xref, protein
accession or causal graph is asserted. No existing YAML needs an exact
mention repaired. Apparatus morphology alone does not establish genes,
protein function, membrane dynamics or a complete causal mechanism.

## Evidence and Example

- `DOI:10.1111/j.1529-8817.1986.tb00021.x`: definition authority and
  direct scientific-Abstract snippet (p. 249). The institutional scan at
  https://www.whoi.edu/cms/files/Jacobson_%26_Anderson_1986_JP_feeding_30828.pdf
  contains only printed pages 249-252 and 256-258. All seven were inspected,
  including Table 1 and actual Figures 1, 2 and 23. Pages 253-255 and
  Figures 3-22 were unavailable, not silently treated as audited.
- `DOI:10.1111/j.0022-3646.1992.00069.x`: complete 14-page institutional
  scan and actual Figures 1-46 inspected at
  https://www.whoi.edu/cms/files/Jacobson%26Anderson_1992_Proto-ultrastructrure_31161.pdf.
  The snippet is from the Introduction (p. 69), not the abstract. Figures
  9-12 support apparatus and food localization; Figures 1 and 46 are
  reconstructions. Inner-membrane loss during fixation versus biological
  reorganization remains unresolved. No canonical taxon is assigned from
  the study's culture named Protoperidinium spinulosum.
- `DOI:10.4319/lo.1993.38.5.0965`: direct publisher scientific-Abstract
  quote supports the feeding name and growth on phytoplankton foods.
  https://aslopubs.onlinelibrary.wiley.com/doi/10.4319/lo.1993.38.5.0965
  was inspected, but Methods, figures and culture provenance were not.

The qualified canonical example is `NCBITaxon:402581 Oblea rotunda`, the
natural field specimens in the 1986 study (Table 1 and Figure 2B), not all
isolates and not the separate 1993 laboratory culture. Its provenance URL
is retained in the example note. NCBI ESearch/EFetch verified scientific
name, species rank and Peridiniopsis rotunda synonym. No strain identifier
or choice between the two collection sites is invented.

## ID Space and Files

Reserve `METPO:1058500` in the fresh 1058500-1058599 block after v507's
1058400 block, subset `metpo_traitmech_2026_10`. The next local ID is
`traitmech:000632`. The kg-microbe contract and class/property templates
were read at `1408e7099d039026d7611c240938d8e177753406`; the class header
remains 11 columns. Its newer 13-column property template is irrelevant
to this class-only cohort. CommunityMech v1 and TraitMech v507 were also
read. Expand METPO to the pinned ontology's w3id namespace, not legacy
example IRIs. No collision with CommunityMech's reviewed blocks was found.

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 |
| property template | Omitted |
| SSSOM mappings | Omitted; no equivalence asserted |

Definition provenance is publication citations plus the local minting
record, not ontology mappings. Both header rows retain 11 cells.

## Verification

- Guarded dry run, application and 12 focused tests passed, including replay,
  drift refusal and parent preservation. LinkML and strict record validation
  passed. The initial test invocation omitted `PYTHONPATH=src` and failed
  collection; an append-only AUDIT corrects the CREATE history entry's
  premature test-timing statement. The refreshed history audit validates all
  1,099 history records, including the skill-guidance correction below.
- The maintained snippet resolver returned three `UNRESOLVED` verdicts.
  The three spans were directly checked against the stated PDF or publisher
  sections; those manual checks do not replace the resolver outcomes or
  establish a reason for its missing abstracts. The NCBI audit resolved all
  724 examples across 539 records with zero errors and 24 existing warnings.
- Proposal verification and ROBOT/ELK passed. RDF parsing measured 15 triples
  in classes.owl, 12,628 in merged.owl and 12,632 in reasoned.owl. The new
  w3id class has phenotype as its parent; the pinned phenotype label and
  quality hierarchy remain intact, without legacy METPO stubs.
- `just validate-history`, `just validate-products`, `just qc` and Ruff passed.
  The full suite passed 2,330 tests with two dependency deprecation warnings
  in 1,152.97 seconds.
  Graph findings remain 74 baselined, zero new or blocking; snippet findings
  remain 2,419 baselined, zero new or blocking. No baseline, existing
  TraitRecord, existing history, schema or protected record was changed.
- Maintained generators produced 1,027 trait pages, current priority data,
  555 discussions and a 1,027-record QC dashboard with zero failing slots.
  The reviewed claw source matched all 139 archive source files byte-for-byte.
  All 1,025 unrelated existing pages differ only in footer counts; phenotype
  additionally gains the child link. Its child count (139 to 140) is the
  only changed existing priority row. The regenerated QC coverage image is
  byte-identical, so only its changed HTML is staged.
- Chromium checks at 1440 and 390 pixels passed identity, all three quotes,
  the qualified example, parent navigation, dashboard counts, image loading
  and document-overflow checks, with no page errors. Screenshots were
  inspected. Both exact configured embedding paths are absent; embedding
  artifacts were not regenerated. Existing floating theme controls were
  not redesigned.
- Ordinary staged whitespace checking flags only the ROBOT directive row's
  three required trailing tabs. Both headers were parsed as 11 cells. The
  documented exact-TSV `core.whitespace=-blank-at-eol` check and the ordinary
  check on every other path passed; no global Git setting was changed.

The record remains PROPOSED pending human signoff. Local checks do not
substitute for exact-head review, CI or the native merge queue.

PR #1740's local review identified the direct-command environment guidance
gap filed as #1741. The add-trait skill now documents a conditional source
path fallback that preserves existing import paths. Skill validation, path
preservation, the guarded dry run and all 12 focused tests passed after
that documentation-only fix; separate infrastructure history records it.

## Upstream and Round Trip

Submit the cohort for METPO review. After acceptance into a release,
refresh the pinned ontology, migrate the local identifier and references
to the accepted METPO ID, preserve minting provenance and append-only
history, and regenerate artifacts without a duplicate primary record.
Feeding hierarchy and native molecular mechanism remain open discussions.

## Change Log

- v508, 2026-10-06: propose pallium feeding with three DOI-backed snippets,
  a qualified natural example and explicit topology and access limits.
