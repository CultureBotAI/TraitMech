# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** genome size
- **METPO identifier:** traitmech:000098
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A quantitative genomics property describing the total length of an organism's genome (typically expressed in megabase pairs), which varies widely across prokaryotes and reflects lifestyle and evolutionary forces.
- **Parent traits:** METPO:1000188
- **Synonyms:** genome length
- **Existing evidence:** DOI:10.1038/nrmicro3331:  (Batut et al. review reductive genome evolution, linking genome size to population size and lifestyle across prokaryotes.) | DOI:10.1038/ismej.2014.60:  (Giovannoni et al. discuss streamlining theory and the small genomes of abundant free-living microbes.)
- **Existing causal graph summary:** genome_size_population_lifestyle: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **genome size** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/genome_size.yaml`.

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
**Generated:** 2026-06-18T03:34:40.781535

1. ngugi2023abioticselectionof pages 7-8
2. eisenhofer2024quantifyingmicrobialdna pages 1-5
3. wang2023bacterialgenomesize pages 2-3
4. dmitrijeva2024aglobalsurvey pages 1-2
5. giordano2024genomescalecommunitymodelling pages 1-2
6. ngugi2023abioticselectionof pages 4-4
7. ngugi2023abioticselectionof pages 1-2
8. dong2024ecoevolutionarystrategiesfor pages 1-2
9. chuckran2023edaphiccontrolson pages 1-6
10. dong2024ecoevolutionarystrategiesfor pages 5-5
11. kogay2024defencesystemsand pages 1-2
12. kogay2024defencesystemsand pages 4-5
13. piton2023lifehistorystrategies pages 1-5
14. ngugi2023abioticselectionof pages 9-10
15. dong2024ecoevolutionarystrategiesfor pages 2-3
16. rodriguezgijon2023linkingprokaryoticgenome pages 1-2
17. dong2024ecoevolutionarystrategiesfor pages 4-5
18. wang2023bacterialgenomesize pages 6-7
19. dong2024ecoevolutionarystrategiesfor pages 5-7
20. chuckran2023edaphiccontrolson pages 6-10
21. dong2024ecoevolutionarystrategiesfor pages 3-4
22. kogay2024defencesystemsand pages 6-7
23. https://doi.org/10.1038/s41467-023-36988-x
24. https://doi.org/10.1101/2021.11.17.469016
25. https://doi.org/10.1101/2024.06.20.599828
26. https://doi.org/10.1038/s41467-024-50368-z
27. https://doi.org/10.1038/s41559-024-02357-0
28. https://doi.org/10.1111/1462-2920.16630
29. https://doi.org/10.1038/s41564-023-01465-0
30. https://doi.org/10.1038/s41467-023-43297-w
31. https://doi.org/10.1038/s43705-023-00231-x
32. https://doi.org/10.1038/s41467-023-36988-x,
33. https://doi.org/10.1101/2024.06.20.599828,
34. https://doi.org/10.1038/s41564-023-01465-0,
35. https://doi.org/10.1101/2021.11.17.469016,
36. https://doi.org/10.1038/s41467-023-43297-w,
37. https://doi.org/10.1038/s41467-024-50368-z,
38. https://doi.org/10.1038/s41559-024-02357-0,
39. https://doi.org/10.1111/1462-2920.16630,
40. https://doi.org/10.1038/s41467-024-46374-w,
41. https://doi.org/10.1038/s43705-023-00231-x,