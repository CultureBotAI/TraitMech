# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Fermentation
- **METPO identifier:** METPO:1002005
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A respiration that generates energy through the oxidation of organic compounds without using an external electron acceptor, using organic molecules as both electron donors and final electron acceptors.
- **Parent traits:** METPO:1000800
- **Synonyms:** 
- **Existing evidence:** DOI:10.3389/fmicb.2021.703525: substrate of a fermentation has to serve as electron donor as well as acceptor (Supports donor/acceptor definition of anaerobic bacterial fermentation.) | DOI:10.1111/1751-7915.13746: Substrate-level phosphorylation is one of the main sources of energy (Supports substrate-level phosphorylation as a major fermentative energy-conservation mechanism.)
- **Existing causal graph summary:** fermentation_redox_energy: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **Fermentation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/fermentation.yaml`.

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
**Generated:** 2026-06-18T05:18:45.149511

1. hackmann2024thevastlandscape pages 1-2
2. hackmann2024thevastlandscape pages 2-3
3. hackmann2024thevastlandscape pages 5-6
4. kumar2023moleculararchitectureand pages 1-2
5. taggar2024hydrogenproductionvia pages 5-7
6. tejedorsanz2023extracellularelectronuptake pages 1-2
7. tejedorsanz2023extracellularelectronuptake pages 2-3
8. allaart2023physiologicalandstoichiometric pages 2-3
9. hackmann2024thevastlandscape pages 7-9
10. hackmann2024thevastlandscape pages 4-5
11. hackmann2024thevastlandscape pages 10-11
12. moon2023anewmetabolic pages 1-2
13. hackmann2024thevastlandscape pages 6-7
14. hackmann2024thevastlandscape pages 11-12
15. britton2024thernfcomplex pages 31-35
16. britton2024thernfcomplex pages 27-31
17. davin2024clostridiumautoethanogenumalters pages 7-8
18. britton2024thernfcomplex pages 39-42
19. FeFe
20. https://doi.org/10.1093/femsre/fuae016
21. https://doi.org/10.1093/femsre/fuae016;
22. https://doi.org/10.1111/1758-2229.13160
23. https://doi.org/10.35812/cellulosechemtechnol.2024.58.90
24. https://doi.org/10.1038/s41467-023-41212-x
25. https://doi.org/10.1186/s40168-023-01565-3
26. https://doi.org/10.3389/fmicb.2023.1298023
27. https://doi.org/10.1038/s41598-023-43682-x
28. https://doi.org/10.1186/s13068-024-02554-w
29. https://doi.org/10.1093/femsre/fuae016,
30. https://doi.org/10.1111/1758-2229.13160,
31. https://doi.org/10.35812/cellulosechemtechnol.2024.58.90,
32. https://doi.org/10.3389/fmicb.2023.1298023,
33. https://doi.org/10.1038/s41467-023-41212-x,
34. https://doi.org/10.1186/s40168-023-01565-3,
35. https://doi.org/10.1038/s41598-023-43682-x,
36. https://doi.org/10.1186/s13068-024-02554-w,