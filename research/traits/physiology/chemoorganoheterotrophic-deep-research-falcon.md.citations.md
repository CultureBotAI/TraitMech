# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemoorganoheterotrophic
- **METPO identifier:** METPO:1000640
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains both energy and carbon from organic compounds through oxidation.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemoorganoheterotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: Chemoheterotroph (chemoorganoheterotroph) (Encyclopedia chapter maps chemical energy, reduced organic electron source, and reduced organic carbon source to chemoorganoheterotrophy.) | DOI:10.1021/acsomega.3c02205: chemoorganoheterotrophic (Review table supports organic molecules as energy, electron, and carbon sources in chemoorganoheterotrophy.)
- **Existing causal graph summary:** chemoorganoheterotrophic_organic_energy_carbon: 8 nodes, 10 edges

## Research Objective

Research the microbial trait **chemoorganoheterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemoorganoheterotrophic.yaml`.

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
**Generated:** 2026-06-18T11:19:21.462949

1. stebegg2023heterotrophyamongcyanobacteria pages 1-2
2. stebegg2023heterotrophyamongcyanobacteria pages 2-4
3. stebegg2023heterotrophyamongcyanobacteria pages 2-2
4. dang2017ecologicalenergeticperspectives pages 1-2
5. stebegg2023heterotrophyamongcyanobacteria pages 10-11
6. wang2023energyuseefficiency pages 1-2
7. liew2024integratingmultiplatformassembly pages 11-15
8. pavlova2024anaerobicoxidationof pages 1-2
9. li2017theecologyof pages 1-2
10. li2017theecologyof pages 11-12
11. stebegg2023heterotrophyamongcyanobacteria pages 9-10
12. wang2023energyuseefficiency pages 4-4
13. sogin2021lifeinthe pages 9-11
14. carini2013nutrientrequirementsfor pages 1-2
15. wang2023energyuseefficiency pages 14-15
16. li2017theecologyof pages 4-6
17. li2017theecologyof pages 7-8
18. wang2023energyuseefficiency pages 14-14
19. https://doi.org/10.1021/acsomega.3c02205
20. https://doi.org/10.1111/gcb.16925
21. https://doi.org/10.1186/s40793-024-00572-7
22. https://doi.org/10.1134/s0026261724605608
23. https://doi.org/10.3389/fmicb.2017.00683
24. https://doi.org/10.1146/annurev-micro-051021-123130
25. https://doi.org/10.1021/acsomega.3c02205,
26. https://doi.org/10.3389/fmicb.2017.01246,
27. https://doi.org/10.1038/ismej.2012.122,
28. https://doi.org/10.1111/gcb.16925,
29. https://doi.org/10.1186/s40793-024-00572-7,
30. https://doi.org/10.1134/s0026261724605608,
31. https://doi.org/10.3389/fmicb.2017.00683,
32. https://doi.org/10.1146/annurev-micro-051021-123130,