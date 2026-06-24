# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** photoheterotrophic
- **METPO identifier:** METPO:1000657
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses light as the energy source and organic compounds as the primary carbon source for biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** photoheterotroph, photoheterotrophy
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: light and reduced organic compounds (Encyclopedia chapter defines photoheterotrophy by light energy and reduced organic carbon.) | DOI:10.1128/AEM.01747-12: accumulated 25% to 110% more biomass (Experimental AAP study supports light-enhanced assimilation of supplied organic carbon.)
- **Existing causal graph summary:** photoheterotrophic_light_organic_carbon: 8 nodes, 7 edges

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
**Generated:** 2026-06-18T12:31:35.896969

1. oh2024effectoflight pages 13-14
2. stojan2024ecologyofaerobic pages 1-2
3. lee2024effectsoflight pages 1-2
4. tzlil2024lightharvestingbyantennacontaining pages 17-21
5. oh2024effectoflight pages 1-2
6. oh2024effectoflight pages 8-9
7. li2023globallydistributedmyxococcota pages 4-5
8. stojan2024ecologyofaerobic pages 6-8
9. millette2024recommendationsforadvancing pages 1-2
10. millette2024recommendationsforadvancing pages 11-12
11. stojan2024ecologyofaerobic pages 16-17
12. stojan2024ecologyofaerobic pages 5-6
13. li2023globallydistributedmyxococcota pages 8-9
14. but
15. https://doi.org/10.1007/s12275-024-00125-0
16. https://doi.org/10.4014/jmb.2410.10034
17. https://doi.org/10.1186/s40793-024-00573-6
18. https://doi.org/10.1038/s41467-023-42193-7
19. https://doi.org/10.1101/2024.09.18.613612
20. https://doi.org/10.3389/fmars.2024.1392673
21. https://doi.org/10.4014/jmb.2410.10034,
22. https://doi.org/10.1186/s40793-024-00573-6,
23. https://doi.org/10.3389/fmars.2024.1392673,
24. https://doi.org/10.1007/s12275-024-00125-0,
25. https://doi.org/10.1038/s41467-023-42193-7,
26. https://doi.org/10.1101/2024.09.18.613612,