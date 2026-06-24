# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** ethanol fermentation
- **METPO identifier:** traitmech:000028
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A fermentation in which pyruvate is decarboxylated to acetaldehyde (releasing CO2) and then reduced by NADH to ethanol, regenerating NAD+ for glycolysis. Characteristic of yeasts and the bacterium Zymomonas mobilis.
- **Parent traits:** METPO:1002005
- **Synonyms:** alcoholic fermentation
- **Existing evidence:** DOI:10.3390/molecules31020333:  (Review of classical fermentations describes the alcoholic (ethanol) pathway in which pyruvate is decarboxylated and reduced to ethanol.) | DOI:10.3389/fmicb.2021.703525:  (Review of fermentative energy conservation supports ethanol as an NADH-reoxidizing fermentation end product.)
- **Existing causal graph summary:** ethanol_fermentation_pyruvate_to_ethanol: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **ethanol fermentation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/ethanol_fermentation.yaml`.

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
**Generated:** 2026-06-18T05:07:43.700233

1. yan2024thebiochemicalbasis pages 2-5
2. ziegler2024structuralcharacterizationand pages 1-3
3. bao2023metabolicengineeringof pages 9-11
4. gao2023rewiringcarbonflow pages 1-2
5. ziegler2024structuralcharacterizationand pages 11-12
6. frohwitter2024anewzymomonas pages 1-2
7. frohwitter2024anewzymomonas pages 5-7
8. hu2023metabolicengineeringof pages 1-2
9. zhang2023characterizationandapplication pages 2-4
10. yan2024thebiochemicalbasis pages 7-9
11. gao2023rewiringcarbonflow pages 6-7
12. geng2023enhancedexpressionof pages 12-14
13. xiufeng2024responsemechanismof pages 13-15
14. bao2023metabolicengineeringof pages 1-2
15. gao2023rewiringcarbonflow pages 2-4
16. xiufeng2024responsemechanismof pages 17-18
17. ahmadpanah2023metabolicregulationboosts pages 2-3
18. vion2024influenceofyeasts pages 6-7
19. gao2023rewiringcarbonflow pages 4-6
20. yan2024thebiochemicalbasis pages 1-2
21. geng2023enhancedexpressionof pages 15-16
22. ziegler2024structuralcharacterizationand pages 6-9
23. xiufeng2024responsemechanismof pages 1-2
24. ziegler2024structuralcharacterizationand pages 3-6
25. ziegler2024structuralcharacterizationand pages 9-11
26. https://doi.org/10.5376/be.2024.14.0025;
27. https://doi.org/10.5376/be.2024.14.0025
28. https://doi.org/10.3390/ijms24065888;
29. https://doi.org/10.1186/s12934-024-02419-9
30. https://doi.org/10.3390/fermentation9020113
31. https://doi.org/10.1101/2024.02.16.580662
32. https://doi.org/10.1101/2024.02.16.580662;
33. https://doi.org/10.3390/microorganisms12010038
34. https://doi.org/10.1186/s12934-024-02419-9;
35. https://doi.org/10.3390/ijms24065888
36. https://doi.org/10.1038/s41598-024-80484-1
37. https://doi.org/10.3389/fmicb.2024.1475567
38. https://doi.org/10.3389/fmicb.2023.1211004
39. https://doi.org/10.3389/fbioe.2023.1135484;
40. https://doi.org/10.20870/oeno-one.2024.58.4.7877
41. https://doi.org/10.3389/fmicb.2024.1475567;
42. https://doi.org/10.1038/s41598-023-47846-7
43. https://doi.org/10.3389/fbioe.2023.1135484
44. https://doi.org/10.5376/be.2024.14.0025,
45. https://doi.org/10.1101/2024.02.16.580662,
46. https://doi.org/10.3390/fermentation9020113,
47. https://doi.org/10.3389/fmicb.2023.1211004,
48. https://doi.org/10.1186/s12934-024-02419-9,
49. https://doi.org/10.3389/fbioe.2023.1135484,
50. https://doi.org/10.3390/ijms24065888,
51. https://doi.org/10.3389/fmicb.2024.1475567,
52. https://doi.org/10.1038/s41598-024-80484-1,
53. https://doi.org/10.3390/microorganisms12010038,
54. https://doi.org/10.20870/oeno-one.2024.58.4.7877,
55. https://doi.org/10.1038/s41598-023-47846-7,