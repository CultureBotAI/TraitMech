# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** thermophilic
- **METPO identifier:** METPO:1000616
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference in which growth is favored at elevated temperatures, typically ≥45 °C.
- **Parent traits:** METPO:1000613
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Supports thermophilic growth as adaptation to elevated temperature.) | PMID:24058645: Geobacillus stearothermophilus is a gram-positive, thermophilic bacterium (Organism example: Geobacillus stearothermophilus is described as thermophilic.)
- **Existing causal graph summary:** thermophilic_heat_adaptation: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **thermophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/thermophilic.yaml`.

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
**Generated:** 2026-06-18T02:55:01.676025

1. lehmann2023adaptivelaboratoryevolution pages 1-2
2. rekadwad2023extremophilesthespecies pages 2-4
3. baes2023transcriptionalandtranslational pages 1-2
4. furr2024structuralstabilitycomparisons pages 1-2
5. takemata2024howdothermophiles pages 1-2
6. takemata2024howdothermophiles pages 4-5
7. chong2024archaeamembranesin pages 1-2
8. li2024biosynthesisofgmgt pages 1-2
9. finore2023thermophilicbacteriaand pages 5-7
10. burkhardt2024miningthermophilesfor pages 1-2
11. garcia2024identificationoftwo pages 1-2
12. garcia2024identificationoftwo pages 6-7
13. garcia2024identificationoftwo pages 2-2
14. gallo2024theundeniablepotential pages 7-8
15. mondal2024aquificaeovercomescompetition pages 28-30
16. gallo2024theundeniablepotential pages 1-3
17. lehmann2023adaptivelaboratoryevolution pages 2-3
18. garcia2024identificationoftwo pages 2-3
19. garcia2024identificationoftwo pages 3-4
20. li2024biosynthesisofgmgt pages 3-4
21. gallo2024theundeniablepotential pages 5-7
22. gallo2024theundeniablepotential pages 4-5
23. not ideal, label-only preferred
24. environmental context
25. not specific
26. https://doi.org/10.1128/mbio.03593-22
27. https://doi.org/10.3390/microorganisms12112348
28. https://doi.org/10.1264/jsme2.me23087
29. https://doi.org/10.3389/frbis.2023.1338019
30. https://doi.org/10.1073/pnas.2318761121
31. https://doi.org/10.1038/s41467-024-49650-x
32. https://doi.org/10.1007/s13205-023-03733-6
33. https://doi.org/10.1186/s40538-023-00381-z
34. https://doi.org/10.3390/ijms25147685
35. https://doi.org/10.1007/s00792-023-01321-3
36. https://doi.org/10.3389/fmicb.2023.1265216
37. https://doi.org/10.1101/2023.07.10.548480
38. https://doi.org/10.3389/fmicb.2023.1265216,
39. https://doi.org/10.3390/ijms25147685,
40. https://doi.org/10.1007/s13205-023-03733-6,
41. https://doi.org/10.1264/jsme2.me23087,
42. https://doi.org/10.1128/mbio.03593-22,
43. https://doi.org/10.3390/microorganisms12112348,
44. https://doi.org/10.3389/frbis.2023.1338019,
45. https://doi.org/10.1073/pnas.2318761121,
46. https://doi.org/10.1038/s41467-024-49650-x,
47. https://doi.org/10.1186/s40538-023-00381-z,
48. https://doi.org/10.1007/s00792-023-01321-3,
49. https://doi.org/10.1101/2023.07.10.548480,