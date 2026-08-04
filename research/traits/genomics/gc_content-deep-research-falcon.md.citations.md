# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** GC content
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000127
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A quality that is describing the percentage of guanine and cytosine nucleotides in genomic DNA, calculated as the ratio of GC base pairs to total base pairs.
- **Parent traits:** METPO:1000188
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrg2358: GC content (Bacterial-genome review supports GC content as a fundamental genome-composition descriptor varying widely across prokaryotic lineages.) | DOI:10.1186/1471-2148-10-374: GC-biased gene conversion (Bacterial-GC-content evolution review supports GC-biased gene conversion and mutation bias as the mechanistic drivers of genomic GC composition.)
- **Existing causal graph summary:** gc_content_composition_drivers: 13 nodes, 12 edges

## Research Objective

Research the microbial trait **GC content** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/gc_content.yaml`.

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
**Generated:** 2026-08-04T04:50:07.963463

1. wu2012onthemolecular pages 2-4
2. fuente2023genomicsignaturein pages 13-15
3. hu2022apositivecorrelation pages 1-2
4. lassalle2015gccontentevolutionin pages 14-16
5. hayek2013lateraltransferand pages 2-3
6. lassalle2015gccontentevolutionin pages 11-14
7. aliperti2023rkselectionof pages 9-11
8. lassalle2015gccontentevolutionin pages 6-9
9. aliperti2023rkselectionof pages 1-3
10. lassalle2015gccontentevolutionin pages 4-6
11. lassalle2015gccontentevolutionin pages 9-11
12. aliperti2023rkselectionof pages 3-6
13. aliperti2023rkselectionof pages 6-9
14. 10.1101/cshperspect.a018077
15. 10.1101/011023
16. 10.1186/1745-6150-7-2
17. 10.3389/fmicb.2013.00041
18. 10.1186/s12864-022-08353-7
19. 10.1111/1462-2920.16511
20. 10.3390/biology12020322
21. https://doi.org/10.1101/cshperspect.a018077
22. https://doi.org/10.1101/011023
23. https://doi.org/10.1186/1745-6150-7-2
24. https://doi.org/10.3389/fmicb.2013.00041
25. https://doi.org/10.1186/s12864-022-08353-7
26. https://doi.org/10.1111/1462-2920.16511
27. https://doi.org/10.3390/biology12020322
28. https://doi.org/10.1186/s12864-022-08353-7,
29. https://doi.org/10.1111/1462-2920.16511,
30. https://doi.org/10.1101/cshperspect.a018077,
31. https://doi.org/10.1101/011023,
32. https://doi.org/10.1186/1745-6150-7-2,
33. https://doi.org/10.3389/fmicb.2013.00041,
34. https://doi.org/10.3390/biology12020322,