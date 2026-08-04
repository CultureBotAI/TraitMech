# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** heterocyst
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000073
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait in which a filamentous cyanobacterium differentiates specialized, thick-walled cells (heterocysts) that create a microoxic interior for oxygen-sensitive nitrogen fixation.
- **Parent traits:** METPO:1000059
- **Synonyms:** heterocyst-forming
- **Existing evidence:** DOI:10.1101/cshperspect.a000315:  (Kumar, Mella-Herrera & Golden describe heterocysts as differentiated cells whose structure and metabolism accommodate oxygen-sensitive nitrogen fixation.) | DOI:10.1093/femsre/fuw029:  (Herrero, Stavans & Flores describe heterocysts within the multicellular filament of heterocyst-forming cyanobacteria.)
- **Existing causal graph summary:** heterocyst_microoxic_nitrogen_fixation: 14 nodes, 10 edges

## Research Objective

Research the microbial trait **heterocyst** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/heterocyst.yaml`.

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
**Generated:** 2026-08-04T08:56:39.421940

1. pernil2019metalloproteinsinthe pages 6-8
2. arbelgoren2024spatiotemporalcoherenceof pages 10-13
3. herrero2019geneticresponsesto pages 12-14
4. herrero2019geneticresponsesto pages 32-38
5. herrero2019geneticresponsesto pages 14-17
6. kolan2024tradeoffsbetweenphage pages 1-2
7. kolan2024tradeoffsbetweenphage pages 10-11
8. arbelgoren2024spatiotemporalcoherenceof pages 2-4
9. kolan2024tradeoffsbetweenphage pages 11-12
10. gerdtzen2009modelingheterocystpattern pages 1-2
11. s
12. 10.1128/msystems.00700-23
13. 10.1093/ismejo/wrad008
14. 10.1101/2023.10.04.560878
15. 10.1021/acsomega.3c02205
16. 10.1111/1462-2920.14370
17. 10.3390/life9020032
18. 10.1101/cshperspect.a000315
19. 10.1186/1471-2105-10-S6-S16
20. https://doi.org/10.1128/msystems.00700-23
21. https://doi.org/10.1093/ismejo/wrad008
22. https://doi.org/10.1101/2023.10.04.560878
23. https://doi.org/10.1021/acsomega.3c02205
24. https://doi.org/10.1111/1462-2920.14370
25. https://doi.org/10.3390/life9020032
26. https://doi.org/10.1101/cshperspect.a000315
27. https://doi.org/10.1186/1471-2105-10-S6-S16
28. https://doi.org/10.3390/life9020032,
29. https://doi.org/10.1128/msystems.00700-23,
30. https://doi.org/10.1111/1462-2920.14370,
31. https://doi.org/10.1186/1471-2105-10-s6-s16,
32. https://doi.org/10.1101/2023.10.04.560878,