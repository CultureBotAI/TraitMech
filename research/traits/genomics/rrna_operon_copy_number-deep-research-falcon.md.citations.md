# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** rRNA operon copy number
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000101
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A quantitative genomics property describing the number of ribosomal RNA (rrn) operons encoded in a genome, which correlates with maximal growth rate and ecological strategy.
- **Parent traits:** METPO:1000188
- **Synonyms:** rrn copy number
- **Existing evidence:** DOI:10.1128/AEM.66.4.1328-1333.2000:  (Klappenbach, Dunbar & Schmidt show rRNA operon copy number reflects ecological strategies, with fast responders carrying more copies.) | DOI:10.1038/nmicrobiol.2016.160:  (Roller, Stoddard & Schmidt link rrn copy number to bacterial growth rate and growth efficiency.)
- **Existing causal graph summary:** rrn_copy_growth_rate: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **rRNA operon copy number** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/rrna_operon_copy_number.yaml`.

## Required Findings

### 1. Trait Scope
- Clarify what phenotype, physiological capacity, environmental preference, or assay-observed
  property the trait represents.
- Identify boundary cases and distinguish the trait from nearby traits.

### 2. Causal Graph Entities
- Pathways and metabolic modules.
- Environmental factors and experimental factors.
- Genes, proteins, enzymes, transporters, and complexes.
- Chemicals, electron donors, electron acceptors, nutrients, metabolites, and inhibitors.
- Organelles, cellular localizations, molecular functions, and biological processes.

### 3. Evidence-Backed Edges
- Propose causal edges as subject-predicate-object triples.
- For every proposed edge, provide a reference, a short supporting quote/snippet, and notes
  explaining how the source supports the edge.
- Prefer DOI references. Use PMID only when a DOI is not available.
- Mark weak, taxon-specific, assay-specific, or inferred claims as uncertain.

### 4. Ontology Grounding
- Suggest CURIEs where available: METPO, GO, CHEBI, ENVO, NCBITaxon, EC, UniProt, Rhea,
  KEGG, MetaCyc, or other stable identifiers.
- Do not invent identifiers. Label-only candidate nodes are acceptable when grounding is unclear.

## Output Format

Return a curation-focused report with:
- A short scope summary.
- Candidate nodes grouped by type.
- Candidate causal edges in a table with reference, snippet, and notes.
- DOI-first bibliography.
- Warnings for claims that should not yet be curated into TraitMech.

**Provider:** falcon
**Generated:** 2026-08-04T05:21:54.416114

1. roller2016exploitingrrnaoperon pages 5-11
2. fleurier2022rrnaoperonmultiplicity pages 1-2
3. raval2023thelayeredcosts pages 13-14
4. valdiviaanistro2016variabilityofrrna pages 1-2
5. klappenbach2000rrnaoperoncopy pages 1-2
6. hidalgo2022regulatoryperturbationsof pages 2-5
7. hidalgo2022regulatoryperturbationsof pages 1-2
8. klappenbach2000rrnaoperoncopy pages 5-6
9. 10.7554/eLife.81005
10. 10.1093/nar/gkac332
11. 10.1016/j.isci.2022.103879
12. 10.1038/nmicrobiol.2016.160
13. 10.3389/fmicb.2015.01486
14. 10.1128/AEM.66.4.1328-1333.2000
15. https://doi.org/10.7554/eLife.81005
16. https://doi.org/10.1093/nar/gkac332
17. https://doi.org/10.1016/j.isci.2022.103879
18. https://doi.org/10.1038/nmicrobiol.2016.160
19. https://doi.org/10.3389/fmicb.2015.01486
20. https://doi.org/10.1128/AEM.66.4.1328-1333.2000
21. https://doi.org/10.1038/nmicrobiol.2016.160,
22. https://doi.org/10.1093/nar/gkac332,
23. https://doi.org/10.7554/elife.81005,
24. https://doi.org/10.1016/j.isci.2022.103879,
25. https://doi.org/10.1128/aem.66.4.1328-1333.2000,
26. https://doi.org/10.3389/fmicb.2015.01486,