# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cellulolysis
- **METPO identifier:** traitmech:000111
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biopolymer-degradation metabolism in which an organism hydrolyzes cellulose to cellodextrins and glucose using cellulase systems, sometimes organized into cellulosomes.
- **Parent traits:** traitmech:000110
- **Synonyms:** cellulolytic, cellulose degradation
- **Existing evidence:** DOI:10.1128/MMBR.66.3.506-577.2002:  (Lynd et al. review microbial cellulose utilization, its enzymology, and cellulosome systems.) | DOI:10.1016/j.cbpa.2015.10.018:  (Cragg et al. place cellulose deconstruction within lignocellulose degradation across diverse organisms.)
- **Existing causal graph summary:** cellulolysis_cellulase_systems: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **cellulolysis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/cellulolysis.yaml`.

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
**Generated:** 2026-06-18T04:39:56.549964

1. gurovic2023regulationoflignocellulose pages 2-3
2. salgado2024unveilinglignocellulolyticpotential pages 1-2
3. datta2024enzymaticdegradationof pages 10-12
4. minor2024agenomicanalysis pages 1-2
5. raheja2024transcriptionalandsecretome pages 1-2
6. gurovic2023regulationoflignocellulose pages 5-7
7. zhang2024transcriptionalregulationof pages 1-2
8. zhang2024unveilingaclassical pages 1-2
9. zhang2024transcriptionalregulationof pages 4-5
10. raheja2024transcriptionalandsecretome pages 12-13
11. gurovic2023regulationoflignocellulose pages 7-7
12. you2024comprehensivetranscriptomicanalysis pages 7-10
13. gurovic2023regulationoflignocellulose pages 3-4
14. you2023insightsintolignocellulose pages 1-2
15. zhang2024transcriptionalregulationof pages 6-8
16. datta2024enzymaticdegradationof pages 16-17
17. https://doi.org/10.1093/jambio/lxac002
18. https://doi.org/10.1186/s13568-023-01658-0
19. https://doi.org/10.3389/fmicb.2023.1288286
20. https://doi.org/10.1016/j.heliyon.2024.e24022
21. https://doi.org/10.1007/s00253-024-13240-0
22. https://doi.org/10.3389/fmicb.2024.1160472
23. https://doi.org/10.21203/rs.3.rs-5487263/v1
24. https://doi.org/10.1186/s40168-024-01917-7
25. https://doi.org/10.3389/fmicb.2024.1473396
26. https://doi.org/10.1093/jambio/lxac002,
27. https://doi.org/10.3389/fmicb.2024.1160472,
28. https://doi.org/10.1186/s13568-023-01658-0,
29. https://doi.org/10.1186/s40168-024-01917-7,
30. https://doi.org/10.3389/fmicb.2023.1288286,
31. https://doi.org/10.1016/j.heliyon.2024.e24022,
32. https://doi.org/10.3389/fmicb.2024.1473396,
33. https://doi.org/10.1007/s00253-024-13240-0,
34. https://doi.org/10.21203/rs.3.rs-5487263/v1,