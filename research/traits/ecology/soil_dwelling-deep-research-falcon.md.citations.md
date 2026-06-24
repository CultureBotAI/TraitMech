# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** soil-dwelling
- **METPO identifier:** traitmech:000050
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A habitat association in which an organism's primary environment is soil, a complex and highly diverse microbial habitat central to terrestrial biogeochemical cycling.
- **Parent traits:** traitmech:000047
- **Synonyms:** soil-associated
- **Existing evidence:** DOI:10.1038/nrmicro.2017.87:  (Fierer, "Embracing the unknown", characterizes the soil microbiome as a distinct, complex microbial habitat.) | DOI:10.1038/nrmicro1341:  (Martiny et al. support soil communities as biogeographically structured microbial habitats.)
- **Existing causal graph summary:** soil_dwelling_biogeochemistry: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **soil-dwelling** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/soil_dwelling.yaml`.

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
**Generated:** 2026-06-17T21:09:22.973765

1. ramoneda2024ecologicalrelevanceof pages 8-9
2. rodriguezramos2024environmentalmatrixand pages 14-16
3. piton2023lifehistorystrategies pages 5-8
4. dragone2024taxonomicandgenomic pages 1-2
5. knight2024soilmicrobiomesshow pages 4-5
6. knight2024soilmicrobiomesshow pages 3-4
7. marschmann2024predictionsofrhizosphere pages 7-8
8. malik2024bacterialpopulationleveltradeoffs pages 6-9
9. piton2023lifehistorystrategies pages 8-11
10. zhou2024thebiogeographyof pages 1-2
11. jansson2023soilmicrobiomeengineering pages 9-10
12. clagnan2024culturomicsandmetagenomicsbased pages 3-4
13. knight2024soilmicrobiomesshow pages 1-2
14. ramoneda2024ecologicalrelevanceof pages 4-5
15. knight2024soilmicrobiomesshow pages 6-6
16. ed
17. https://doi.org/10.1038/s41564-023-01465-0
18. https://doi.org/10.1093/ismeco/ycae081
19. https://doi.org/10.1038/s41467-024-53753-w
20. https://doi.org/10.1093/ismejo/wrae067
21. https://doi.org/10.1038/s41586-024-08185-3
22. https://doi.org/10.1101/2024.06.22.600187
23. https://doi.org/10.1101/2024.10.02.616266
24. https://doi.org/10.1038/s41564-023-01582-w
25. https://doi.org/10.1038/s41587-023-01932-3
26. https://doi.org/10.3389/fmicb.2024.1473666
27. https://doi.org/10.1038/s41564-023-01465-0,
28. https://doi.org/10.1093/ismejo/wrae067,
29. https://doi.org/10.1038/s41586-024-08185-3,
30. https://doi.org/10.1101/2024.10.02.616266,
31. https://doi.org/10.1093/ismeco/ycae081,
32. https://doi.org/10.1038/s41564-023-01582-w,
33. https://doi.org/10.1038/s41467-024-53753-w,
34. https://doi.org/10.1101/2024.06.22.600187,
35. https://doi.org/10.1038/s41587-023-01932-3,
36. https://doi.org/10.3389/fmicb.2024.1473666,