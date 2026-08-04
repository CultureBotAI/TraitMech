# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** ethanol fermentation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000028
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A fermentation in which pyruvate is decarboxylated to acetaldehyde (releasing CO2) and then reduced by NADH to ethanol, regenerating NAD+ for glycolysis. Characteristic of yeasts and the bacterium Zymomonas mobilis.
- **Parent traits:** METPO:1002005
- **Synonyms:** alcoholic fermentation
- **Existing evidence:** DOI:10.3390/molecules31020333:  (Review of classical fermentations describes the alcoholic (ethanol) pathway in which pyruvate is decarboxylated and reduced to ethanol.) | DOI:10.3389/fmicb.2021.703525:  (Review of fermentative energy conservation supports ethanol as an NADH-reoxidizing fermentation end product.)
- **Existing causal graph summary:** ethanol_fermentation_pyruvate_to_ethanol: 10 nodes, 9 edges

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
**Generated:** 2026-08-04T06:15:54.339789

1. pfeiffer2014anevolutionaryperspective pages 1-2
2. gutierrezcorona2023fungalalcoholdehydrogenases pages 3-5
3. eram2013decarboxylationofpyruvate pages 1-3
4. pronk1996pyruvatemetabolismin pages 6-8
5. frohwitter2024anewzymomonas pages 1-2
6. eram2013decarboxylationofpyruvate pages 3-6
7. pronk1996pyruvatemetabolismin pages 5-6
8. jouhten2008oxygendependenceof pages 1-2
9. yang2009transcriptomicandmetabolomic pages 1-2
10. xiufeng2024responsemechanismof pages 1-2
11. gutierrezcorona2023fungalalcoholdehydrogenases pages 8-10
12. aminian2023investigatingethanolproduction pages 1-2
13. 10.3389/fmolb.2014.00017
14. 10.3390/biom3030578
15. 10.1002/(SICI)1097-0061(199612)12:16%3C1607::AID-YEA70%3E3.0.CO;2-4
16. 10.1186/1752-0509-2-60
17. 10.1186/s12934-024-02419-9
18. 10.1186/1471-2164-10-34
19. 10.1038/s41598-024-80484-1
20. 10.1038/s41598-023-28396-4
21. 10.3390/cells12182239
22. https://doi.org/10.3389/fmolb.2014.00017
23. https://doi.org/10.3390/biom3030578
24. https://doi.org/10.1002/(SICI
25. https://doi.org/10.1186/1752-0509-2-60
26. https://doi.org/10.1186/s12934-024-02419-9
27. https://doi.org/10.1186/1471-2164-10-34
28. https://doi.org/10.1038/s41598-024-80484-1
29. https://doi.org/10.1038/s41598-023-28396-4
30. https://doi.org/10.3390/cells12182239
31. https://doi.org/10.1002/(sici
32. https://doi.org/10.3390/biom3030578,
33. https://doi.org/10.3389/fmolb.2014.00017,
34. https://doi.org/10.3390/cells12182239,
35. https://doi.org/10.1186/1752-0509-2-60,
36. https://doi.org/10.1186/s12934-024-02419-9,
37. https://doi.org/10.1186/1471-2164-10-34,
38. https://doi.org/10.1038/s41598-024-80484-1,
39. https://doi.org/10.1038/s41598-023-28396-4,