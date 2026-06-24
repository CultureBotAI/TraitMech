# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** methanotrophic
- **METPO identifier:** METPO:1000650
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses methane as the primary carbon and energy source through oxidation of methane to carbon dioxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** methanotroph
- **Existing evidence:** DOI:10.1039/D3CY00737E: convert methane to methanol using methane monooxygenase (Review supports methane monooxygenase as the first aerobic methanotrophy step.)
- **Existing causal graph summary:** methanotrophic_methane_oxidation: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **methanotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/methanotrophic.yaml`.

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
**Generated:** 2026-06-18T11:54:52.500626

1. ahmadi2024recentfindingsin pages 1-2
2. wissink2024probingdenitrifyinganaerobic pages 1-2
3. yao2024methanedependentcompletedenitrification pages 1-3
4. tucci2024directmethaneoxidation pages 3-5
5. ahmadi2024recentfindingsin pages 9-11
6. lidstrom2024directmethaneremoval pages 2-4
7. sina2024persistentactivityof pages 1-2
8. tucci2024directmethaneoxidation pages 1-3
9. molinamacias2024implementationofan pages 1-2
10. samanta2024geneticalandbiochemical pages 16-17
11. yao2024methanedependentcompletedenitrification pages 8-9
12. ahmadi2024recentfindingsin pages 7-9
13. samanta2024geneticalandbiochemical pages 1-2
14. https://doi.org/10.1021/acs.chemrev.3c00727
15. https://doi.org/10.1039/d3cy00737e
16. https://doi.org/10.1021/acs.est.3c07197
17. https://doi.org/10.1007/s11270-024-07555-x
18. https://doi.org/10.1101/cshperspect.a041671
19. https://doi.org/10.1039/D3CY00737E
20. https://doi.org/10.1007/s00253-023-12978-3
21. https://doi.org/10.1038/s41564-023-01578-6
22. https://doi.org/10.1038/s41467-024-49602-5
23. https://doi.org/10.3390/methane3010007
24. https://doi.org/10.1039/d3cy00737e,
25. https://doi.org/10.1021/acs.chemrev.3c00727,
26. https://doi.org/10.1007/s00253-023-12978-3,
27. https://doi.org/10.1021/acs.est.3c07197,
28. https://doi.org/10.1038/s41467-024-49602-5,
29. https://doi.org/10.3390/methane3010007,
30. https://doi.org/10.1038/s41564-023-01578-6,
31. https://doi.org/10.1007/s11270-024-07555-x,
32. https://doi.org/10.1101/cshperspect.a041671,