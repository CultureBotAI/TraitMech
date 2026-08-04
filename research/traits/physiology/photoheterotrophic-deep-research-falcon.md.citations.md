# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** photoheterotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000657
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses light as the energy source and organic compounds as the primary carbon source for biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** photoheterotroph, photoheterotrophy
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: light and reduced organic compounds (Encyclopedia chapter defines photoheterotrophy by light energy and reduced organic carbon.) | DOI:10.1128/AEM.01747-12: accumulated 25% to 110% more biomass (Experimental AAP study supports light-enhanced assimilation of supplied organic carbon.)
- **Existing causal graph summary:** photoheterotrophic_light_organic_carbon: 16 nodes, 14 edges

## Research Objective

Research the microbial trait **photoheterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/photoheterotrophic.yaml`.

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
**Generated:** 2026-08-04T11:54:07.265167

1. hernandezherreros2024boostinghydrogenproduction pages 1-3
2. dhar2023anoxygenicphototrophicpurple pages 1-3
3. tu2023engineeringartificialphotosynthesis pages 1-2
4. stojan2024ecologyofaerobic pages 1-2
5. johnson2010enhancementofsurvival pages 1-2
6. villenaalemany2024phenologyandecological pages 1-2
7. villenaalemany2025particleattachmentdrives pages 1-4
8. oh2024effectoflight pages 1-2
9. oh2024effectoflight pages 13-14
10. villenaalemany2024phenologyandecological pages 9-11
11. villenaalemany2025particleattachmentdrives pages 8-11
12. villenaalemany2025lineagespecificphototrophyand pages 4-7
13. villenaalemany2025particleattachmentdrives pages 11-15
14. villenaalemany2024phenologyandecological pages 11-12
15. 10.1016/j.biortech.2024.130972
16. 10.1186/s40793-024-00573-6
17. 10.1186/s40168-024-01786-0
18. 10.1101/2025.04.22.649935
19. 10.1128/AEM.02425-09
20. 10.1038/s41467-023-43524-4
21. d
22. 10.4014/jmb.2410.10034
23. 10.1007/s11274-023-03729-7
24. 10.1128/AEM.01747-12
25. https://doi.org/10.1016/j.biortech.2024.130972
26. https://doi.org/10.1186/s40793-024-00573-6
27. https://doi.org/10.1186/s40168-024-01786-0
28. https://doi.org/10.1101/2025.04.22.649935
29. https://doi.org/10.1128/AEM.02425-09
30. https://doi.org/10.1038/s41467-023-43524-4
31. https://doi.org/10.4014/jmb.2410.10034
32. https://doi.org/10.1007/s11274-023-03729-7
33. https://doi.org/10.1128/AEM.01747-12
34. https://doi.org/10.1186/s40168-024-01786-0,
35. https://doi.org/10.1186/s40793-024-00573-6,
36. https://doi.org/10.1038/s41467-023-43524-4,
37. https://doi.org/10.1128/aem.02425-09,
38. https://doi.org/10.1016/j.biortech.2024.130972,
39. https://doi.org/10.1007/s11274-023-03729-7,
40. https://doi.org/10.1186/s44375-025-00005-x,
41. https://doi.org/10.1101/2025.04.22.649935,
42. https://doi.org/10.4014/jmb.2410.10034,