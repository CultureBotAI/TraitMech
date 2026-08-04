# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** polyhydroxyalkanoate granule
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000067
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An intracellular storage inclusion composed of polyhydroxyalkanoate (e.g. polyhydroxybutyrate, PHB), a carbon and energy reserve accumulated as cytoplasmic granules.
- **Parent traits:** traitmech:000066
- **Synonyms:** PHB granule, polyhydroxybutyrate inclusion
- **Existing evidence:** DOI:10.1128/mr.54.4.450-472.1990:  (Anderson & Dawes describe polyhydroxyalkanoates (chiefly PHB) as carbon/energy reserves stored as cytoplasmic granules.) | DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow include storage granules such as PHA bodies among bacterial intracellular organelles.)
- **Existing causal graph summary:** pha_granule_carbon_energy_storage: 14 nodes, 10 edges

## Research Objective

Research the microbial trait **polyhydroxyalkanoate granule** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/polyhydroxyalkanoate_granule.yaml`.

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
**Generated:** 2026-08-04T09:42:10.765546

1. santolin2024elucidatingregulationof pages 1-2
2. manoli2023heterologousconstitutiveproduction pages 1-3
3. kelly2024comprehensiveproteomicsanalysis pages 1-3
4. gonzalezrojo2024advancesinmicrobial pages 2-4
5. mezzina2016phasinsmultifacetedpolyhydroxyalkanoate pages 21-24
6. mezzina2021engineeringnativeand pages 16-19
7. santolin2024elucidatingregulationof pages 7-8
8. 10.1016/j.jbc.2024.107523
9. 10.1016/j.mcpro.2024.100765
10. 10.3390/microorganisms12081668
11. 10.3389/fbioe.2023.1275036
12. 10.1038/srep26612
13. 10.1128/AEM.01161-16
14. 10.1111/j.1365-2958.2010.07450.x
15. 10.1002/biot.202000165
16. https://doi.org/10.1016/j.jbc.2024.107523
17. https://doi.org/10.1016/j.mcpro.2024.100765
18. https://doi.org/10.3390/microorganisms12081668
19. https://doi.org/10.3389/fbioe.2023.1275036
20. https://doi.org/10.1038/srep26612
21. https://doi.org/10.1128/AEM.01161-16
22. https://doi.org/10.1111/j.1365-2958.2010.07450.x
23. https://doi.org/10.1002/biot.202000165
24. https://doi.org/10.3390/microorganisms12081668,
25. https://doi.org/10.1038/srep26612,
26. https://doi.org/10.1016/j.jbc.2024.107523,
27. https://doi.org/10.1111/j.1365-2958.2010.07450.x,
28. https://doi.org/10.1016/j.mcpro.2024.100765,
29. https://doi.org/10.3389/fbioe.2023.1275036,
30. https://doi.org/10.1128/aem.01161-16,
31. https://doi.org/10.1002/biot.202000165,