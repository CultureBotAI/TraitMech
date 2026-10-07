# Phagotrophy: METPO Proposal v504

## Context

Add `traitmech:000628 phagotrophy`, a PROPOSED PHYSIOLOGY class for microbial
nutrition through ingestion and assimilation of particulate food. Particle
contact or engulfment alone does not establish this trait. The definition
does not require the consumer to kill living prey, depend exclusively on prey,
or obtain all carbon by direct organic assimilation.

Novelty searches included ignored and hidden files across TraitMech, labels
and related terminology, source DOI/PMID identifiers, the local identifier and
the full proposed METPO hundred block. Existing research reports contain
phagotrophy and bacterivory leads, not curated records. The neighboring
phagocytosis discussion deliberately distinguishes nutrition from uptake; it
does not contain an unresolved exact phagotrophy node requiring repair.
Structured examination of all 12,617 pinned METPO triples found no matching
phagotrophy, bacterivory or holozoic assertion.

A fresh 399-record seed shares 344 IDs with the 1,022-record pre-addition
corpus. The 55 absent IDs are 38 supporting-field terms and 17 reviewed
duplicates. The complete 1,546-row release delta and 153-row active review
were reconciled; all 38 formerly unselected classes are now live. This does
not establish exhaustion of literature-based discovery.

All-state exact-term PR searches and refreshed open TraitMech/METPO heads
identified no competing term or allocation. The known open branches were
checked against their complete previously inspected file inventories. This
work was originally developed at phagocytosis commit
`14a06fd42c39dd4d76ae72ab140ee56086ed8333` in #1735. Integrate only the new
phagotrophy commit onto the reviewed predecessor or its merged main tree;
do not merge this work into a feature branch. Record the final base, exact
head, CI and review outcomes in the PR.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | METPO:1000059 phenotype |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

Use the existing phenotype parent. Local trophic type `METPO:1000631` denotes
carbon, energy and electron-donor sources; heterotrophic `METPO:1000644` is an
organic-carbon class, and mixotrophic `METPO:1000652` requires dual carbon use.
Phagotrophy denotes a mode of acquiring nutrients through particulate food,
without fixing those axes or requiring photosynthesis. Nutrient adaptation
`METPO:1000731` addresses nutrient-availability regimes instead of this mode.

The 2001 Introduction discusses carbon, macronutrients and growth factors as
variable, partly speculative benefits across mixotrophic algae. The 2017
Introduction attributes growth-factor cases to earlier papers, not experiments
performed in that study. Preserve those attributions without importing new
examples from unread references or silently narrowing the trait to carbon.
A closer nutritional-mode hierarchy remains an explicit curation question.

Phagocytosis `traitmech:000627` describes uptake; nutritional assimilation is
additional evidence, not an exact synonym. Bacterivory restricts the food type;
the predatory-bacterium class restricts the consumer taxon. Neither is an exact
equivalent. Extracellular digestion without particle ingestion is excluded.
No synonym, xref, SSSOM mapping, protein accession or causal graph is asserted.
No existing TraitRecord is changed.

## Evidence and Exemplar

- `DOI:10.1038/ismej.2017.68`, `PMID:28524870`, `PMC5563956`:
  direct scientific Abstract, Introduction, Methods, Results and Discussion;
  actual Figures 1 and 4 inspected. Triplicate axenic BG-1 cultures received
  labeled heat-killed prey or inorganic substrates with unlabeled controls.
  Growth and isotope incorporation support nutrient acquisition. The source
  fractions are not universal rates or proof that all carbon followed a direct
  organic route: respiration/refixation and pH/gas-exchange limitations remain.
  Actual Figures 2, 3 and 5 and supplements were not visually audited.
- `DOI:10.1007/s00248-001-1024-6`, `PMID:12024234`:
  direct scientific Abstract and full main text from the author-institution
  PDF; actual pages 2 and 7, including Figure 4, inspected. Axenic/bacterized
  nutrient and light treatments support ingestion-based nutrition. Live
  Pasteurella prey differ from the later heat-killed treatment. Growth-factor
  release and recycling remain possible contributions, and published grazing
  estimates have stated tracer/prey-growth limitations. No numerical grazing
  rate, specific MES assimilation or BG-1 cannibalism claim is imported.

The 22-word isotope excerpt uses the directly retrieved Europe PMC scientific
abstract's ASCII range hyphens. The maintained resolver returns VERIFIED for
that form, while the full-text en-dash version was flagged LIKELY_PARAPHRASE
solely for typography; the original outcome is not rewritten. The 17-word
2001 excerpt matches the directly read scientific PDF abstract and returns
VERIFIED. No snippet is synthesized from a research summary.

The single canonical example is `NCBITaxon:1616673 Ochromonas sp. BG-1`.
Independent NCBI ESearch/EFetch resolve the exact name; its rank is species
despite the strain code in the name. The 2001 Methods document natural
Malaysian freshwater-pond isolation after dark organic enrichment and later
single-cell/antibiotic axenization. Provenance URL:
https://dornsife.usc.edu/caron/wp-content/uploads/sites/263/2023/11/2001_Sanders_etal_ME.pdf
This stays in the example note, not an additional counted evidence item.
The two papers study the same strain, not independent taxon replication.

## ID Space and Artifacts

Reserve fresh block `1058100-1058199` and `METPO:1058100`, following v503;
subset `metpo_traitmech_2026_10`. Ignored-and-hidden collision searches included
TraitMech, pinned METPO and CommunityMech proposals. The upstream contract was
retrieved at `ea1c5f15e6c4dba6c72165367162b354e215f018`; use real w3id METPO
IRIs rather than the legacy prefix shown in its example commands. Citation
fields contain publications and local provenance, not ontology mappings.

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 |
| property template | Omitted |
| SSSOM mappings | Omitted |

## Verification

The guarded writer passed dry run and 11 focused tests for apply/replay,
parent preservation and fail-closed drift refusal. An initial test invocation
omitted `PYTHONPATH=src` and failed collection; the corrected environment
passed. Direct LinkML and strict record validation passed. Both actual-record
snippets returned VERIFIED in the maintained resolver, with source-section
and typography checks recorded separately.

The live NCBI audit resolved all 720 examples across 535 records: zero errors,
24 existing warnings and no warning for the new BG-1 example. Proposal
verification, cross-cohort coverage and ROBOT ELK reasoning passed with no
unsatisfiable class. Direct RDF parsing verifies the new child, its exact
definition and the labeled phenotype-to-quality hierarchy under w3id IRIs.
The merged graph has 12,628 triples in 23,322 physical lines; the reasoned
graph has 12,632 triples in 23,326 lines. No legacy METPO IRI stub is present.

Maintained generators refreshed the discussion browser, published QC
dashboard, priority dashboard and trait pages. Playwright passed at 1440- and
390-pixel widths: local identifier provenance, two citations and quotations,
one qualified example, reciprocal parent link, 1,023-record dashboard and
loaded coverage image, without document-level horizontal overflow or
JavaScript errors. Screenshots were inspected. The pre-existing floating
theme button can overlap mobile text; the shared QC table scrolls internally.
Neither existing presentation behavior is claimed fixed by this curation.

A structured comparison of all 1,022 existing trait pages found 1,021 with
footer-only changes; the phenotype parent's child link/count is the sole
substantive existing trait-page delta. Both exact configured DeepWalk inputs
are absent, so embeddings were not regenerated. No existing trait YAML or
repository history record changed, and audit baselines were not expanded.

`just qc`, `just validate-history` and `just validate-products` passed.
All 508 PROPOSED records meet the two-citation gate and all 628 local IDs are
covered by proposals. Full pytest passed: **2,284 tests**, two dependency
deprecation warnings, in 611.56 seconds. README, priority and QC-dashboard
artifact tests are included. Exact-head PR review, fresh CI and native-queue
merge remain separate required steps, not claims made by these local results.

The ordinary staged whitespace check flags only line 2 of the new ROBOT TSV:
three required empty directive cells represented by trailing tabs. Structured
CSV parsing confirms all three rows have 11 columns. The staged check passes
with that exact TSV excluded, and its path-only check passes with
`core.whitespace=-blank-at-eol`; no global whitespace setting is changed.

## Upstream and Round Trip

Submit the cohort for METPO review. After accepted IDs enter a release,
refresh the pinned ontology, migrate the local identifier and references to
the accepted METPO ID, preserve local-ID provenance and append-only history,
and regenerate products without duplicate primary records. Until human
signoff the local TraitRecord remains PROPOSED.

## Change Log

- v504, 2026-10-05: propose phagotrophy with direct growth/isotope evidence,
  a natural strain-qualified example and explicit nutritional-scope limits.
