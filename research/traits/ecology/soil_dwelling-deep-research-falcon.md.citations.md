# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** soil-dwelling
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000050
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A habitat association in which an organism's primary environment is soil, a complex and highly diverse microbial habitat central to terrestrial biogeochemical cycling.
- **Parent traits:** traitmech:000047
- **Synonyms:** soil-associated
- **Existing evidence:** DOI:10.1038/nrmicro.2017.87:  (Fierer, "Embracing the unknown", characterizes the soil microbiome as a distinct, complex microbial habitat.) | DOI:10.1038/nrmicro1341:  (Martiny et al. support soil communities as biogeographically structured microbial habitats.)
- **Existing causal graph summary:** soil_dwelling_biogeochemistry: 14 nodes, 8 edges

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
**Generated:** 2026-08-03T23:56:34.207750

1. fierer2017embracingtheunknown pages 1-2
2. nicolas2023asubsetof pages 1-2
3. imminger2024survivalandrapid pages 1-2
4. fierer2017embracingtheunknown pages 5-6
5. pomerleau2024adaptivelaboratoryevolution pages 1-2
6. piton2023lifehistorystrategies pages 1-5
7. krysenko2024roleofcarbon pages 1-2
8. andreanigerard2024biosyntheticgeneclusters pages 1-2
9. liu2024organicfertilizationcoselects pages 1-2
10. piton2023lifehistorystrategies pages 8-11
11. osburn2024globalpatternsin pages 1-2
12. novello2024theimpactof pages 1-2
13. berg2020microbiomedefinitionrevisited pages 4-5
14. piton2023lifehistorystrategies pages 11-14
15. chandrakasan2024mappingdistributionfunction pages 9-11
16. chandrakasan2024mappingdistributionfunction pages 2-3
17. fierer2017embracingtheunknown pages 8-9
18. 10.1038/s41564-023-01465-0
19. 10.1038/s41467-024-50382-1
20. 10.1038/s41467-024-46920-6
21. 10.1038/s41467-023-40835-4
22. 10.1128/msystems.00843-23
23. s
24. 10.3390/microorganisms12081571
25. 10.1128/msphere.00192-24
26. 10.1038/s41467-024-49165-5
27. 10.3390/biology13060400
28. 10.3389/sjss.2024.12080
29. 10.1038/nrmicro.2017.87
30. 10.1186/s40168-020-00875-0
31. https://doi.org/10.1038/s41564-023-01465-0
32. https://doi.org/10.1038/s41467-024-50382-1
33. https://doi.org/10.1038/s41467-024-46920-6
34. https://doi.org/10.1038/s41467-023-40835-4
35. https://doi.org/10.1128/msystems.00843-23
36. https://doi.org/10.3390/microorganisms12081571
37. https://doi.org/10.1128/msphere.00192-24
38. https://doi.org/10.1038/s41467-024-49165-5
39. https://doi.org/10.3390/biology13060400
40. https://doi.org/10.3389/sjss.2024.12080
41. https://doi.org/10.1038/nrmicro.2017.87
42. https://doi.org/10.1186/s40168-020-00875-0
43. https://doi.org/10.1038/nrmicro.2017.87,
44. https://doi.org/10.1038/s41564-023-01465-0,
45. https://doi.org/10.1038/s41467-023-40835-4,
46. https://doi.org/10.1038/s41467-024-46920-6,
47. https://doi.org/10.1128/msystems.00843-23,
48. https://doi.org/10.3390/microorganisms12081571,
49. https://doi.org/10.1128/msphere.00192-24,
50. https://doi.org/10.1038/s41467-024-49165-5,
51. https://doi.org/10.1038/s41467-024-50382-1,
52. https://doi.org/10.3390/biology13060400,
53. https://doi.org/10.3389/sjss.2024.12080,
54. https://doi.org/10.1186/s40168-020-00875-0,