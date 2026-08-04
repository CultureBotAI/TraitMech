# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** facultative psychrophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000720
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference characterized by the ability to grow at low temperatures (typically below 20 degrees C) while maintaining optimal growth at moderate temperatures.
- **Parent traits:** METPO:1000613
- **Synonyms:** facultative psychrophile
- **Existing evidence:** DOI:10.1111/j.1574-6941.2009.00727.x: optimum temperatures >20 °C and are capable of growth around 0 °C (Supports facultative psychrophiles as cold-growing organisms with higher temperature optima.)
- **Existing causal graph summary:** facultative_psychrophilic_cold_tolerance: 13 nodes, 11 edges

## Research Objective

Research the microbial trait **facultative psychrophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultative_psychrophilic.yaml`.

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
**Generated:** 2026-08-04T00:44:06.951831

1. purwar2024adaptationsofpsychrophilic pages 1-3
2. ramle2016psychrophiliclipasefrom pages 1-4
3. purwar2024adaptationsofpsychrophilic pages 10-11
4. xiong2023wholegenomeanalysis pages 1-2
5. ramasamy2023comprehensiveinsightson pages 4-6
6. phadtare2004genomewidetranscriptionalanalysis pages 1-2
7. phadtare2010rnaremodelingand pages 5-6
8. owttrim2013rnahelicases pages 3-4
9. kuhn2012towardunderstandinglife pages 2-3
10. yuan2024investigationofcoldresistance pages 1-2
11. lemos2023molecularcharacterizationof pages 1-2
12. purwar2024adaptationsofpsychrophilic pages 3-4
13. turchetti2020dnamethylationchanges pages 1-3
14. cavicchioli2016ontheconcept pages 1-2
15. cavicchioli2016ontheconcept pages 2-3
16. cavicchioli2016ontheconcept pages 3-3
17. owttrim2013rnahelicases pages 5-6
18. https://doi.org/10.1038/ismej.2015.160
19. https://doi.org/10.3390/microorganisms8020296
20. https://doi.org/10.1007/s42770-023-01057-4
21. https://doi.org/10.1038/s41598-023-41323-x
22. https://doi.org/10.3389/fmicb.2023.1142582
23. https://doi.org/10.3389/fmicb.2023.1197797
24. https://doi.org/10.3389/fmicb.2024.1476087
25. https://doi.org/10.37256/amtt.5220244537
26. https://doi.org/10.1128/JB.01377-08
27. https://doi.org/10.1128/JB.186.20.7007-7014.2004
28. https://doi.org/10.4161/rna.7.6.13482
29. https://doi.org/10.4161/rna.22638
30. https://doi.org/10.1089/ast.2012.0858
31. https://doi.org/10.21315/tlsr2016.27.3.21
32. https://doi.org/10.21315/tlsr2016.27.3.21,
33. https://doi.org/10.3390/microorganisms8020296,
34. https://doi.org/10.37256/amtt.5220244537,
35. https://doi.org/10.1038/ismej.2015.160,
36. https://doi.org/10.3389/fmicb.2023.1197797,
37. https://doi.org/10.1038/s41598-023-41323-x,
38. https://doi.org/10.1128/jb.186.20.7007-7014.2004,
39. https://doi.org/10.4161/rna.7.6.13482,
40. https://doi.org/10.4161/rna.22638,
41. https://doi.org/10.1128/jb.01377-08,
42. https://doi.org/10.1089/ast.2012.0858,
43. https://doi.org/10.3389/fmicb.2024.1476087,
44. https://doi.org/10.3389/fmicb.2023.1142582,