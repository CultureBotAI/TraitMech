# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature delta
- **METPO identifier:** METPO:1000303
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature phenotype with numerical limits expressing the breadth (maximum minus minimum, in °C) of ambient temperatures supporting growth of an organism.
- **Parent traits:** METPO:1000533, METPO:1000534
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports the breadth of the temperature-tolerance span as a derived descriptor reflecting overall thermal-adaptation flexibility.) | DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports homoviscous remodeling capacity as the basis of broad versus narrow temperature tolerance.)
- **Existing causal graph summary:** temperature_delta_thermal_flexibility: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature delta** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_delta.yaml`.

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
**Generated:** 2026-06-18T01:46:01.672700

1. kontopoulos2024nouniversalmathematical pages 1-2
2. ramon2023ageneraloverview pages 1-2
3. valenzuela2024isolationofthermophilic pages 2-4
4. ramon2023ageneraloverview pages 2-4
5. moon2023temperaturemattersbacterial pages 6-7
6. grunberger2023uncoveringthetemporal pages 2-4
7. moon2023temperaturemattersbacterial pages 3-5
8. grunberger2023uncoveringthetemporal pages 1-2
9. mendoza2014temperaturesensingby pages 5-6
10. mendoza2014temperaturesensingby pages 6-8
11. purwar2024adaptationsofpsychrophilic pages 10-11
12. mendoza2014temperaturesensingby pages 2-4
13. mendoza2014temperaturesensingby pages 1-2
14. gupta2023psychrophilesasa pages 1-2
15. purwar2024adaptationsofpsychrophilic pages 1-3
16. purwar2024adaptationsofpsychrophilic pages 3-4
17. gupta2023psychrophilesasa pages 9-10
18. valenzuela2024isolationofthermophilic pages 1-2
19. mendoza2014temperaturesensingby pages 4-5
20. mendoza2014temperaturesensingby pages 15-16
21. \Delta T = T_{max, growth} - T_{min, growth}\
22. s
23. which
24. https://doi.org/10.1146/annurev-micro-091313-103612
25. https://doi.org/10.1007/s42770-023-01057-4
26. https://doi.org/10.1128/mbio.02174-23
27. https://doi.org/10.1007/s12275-023-00031-x
28. https://doi.org/10.1038/s41467-024-53046-2
29. https://doi.org/10.3390/microorganisms12030473
30. https://doi.org/10.37256/amtt.5220244537
31. https://doi.org/10.52679/tabcj.2023.0006
32. https://doi.org/10.1038/s41467-024-53046-2,
33. https://doi.org/10.1007/s42770-023-01057-4,
34. https://doi.org/10.3390/microorganisms12030473,
35. https://doi.org/10.1146/annurev-micro-091313-103612,
36. https://doi.org/10.1128/mbio.02174-23,
37. https://doi.org/10.1007/s12275-023-00031-x,
38. https://doi.org/10.37256/amtt.5220244537,
39. https://doi.org/10.52679/tabcj.2023.0006,