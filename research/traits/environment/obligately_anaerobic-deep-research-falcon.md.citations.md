# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** obligately anaerobic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000607
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference in which molecular oxygen (O₂) inhibits or prevents growth.
- **Parent traits:** METPO:1000601
- **Synonyms:** obligate anaerobe, obligate anaerobic
- **Existing evidence:** https://www.ncbi.nlm.nih.gov/books/NBK482349/: Oxygen is toxic to anaerobes (Supports oxygen inhibition/toxicity for obligately anaerobic organisms.) | PMID:22778399: obligate anaerobe Bacteroides fragilis (Organism example: Bacteroides fragilis is described as an obligate anaerobe.)
- **Existing causal graph summary:** obligate_anaerobe_oxygen_toxicity: 14 nodes, 12 edges

## Research Objective

Research the microbial trait **obligately anaerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/obligately_anaerobic.yaml`.

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
**Generated:** 2026-08-04T02:20:51.163549

1. khademian2020doreactiveoxygen pages 1-2
2. lu2021whenanaerobesencounter pages 6-8
3. botin2023thetoleranceof pages 2-5
4. lu2021whenanaerobesencounter pages 9-11
5. lu2021whenanaerobesencounter pages 22-27
6. caulat2024physiologicalroleand pages 1-2
7. botin2023thetoleranceof pages 1-2
8. caulat2024physiologicalroleand pages 13-15
9. xie2024bacteroidesthetaiotaomicronenhances pages 6-8
10. ostos2024ametagenomicapproach pages 9-10
11. lu2021whenanaerobesencounter pages 1-3
12. lu2021whenanaerobesencounter pages 3-4
13. caulat2024physiologicalroleand pages 2-5
14. lu2021whenanaerobesencounter pages 17-19
15. xie2024bacteroidesthetaiotaomicronenhances pages 1-2
16. caulat2024physiologicalroleand pages 5-7
17. caulat2024physiologicalroleand pages 11-13
18. xie2024bacteroidesthetaiotaomicronenhances pages 8-9
19. xie2024bacteroidesthetaiotaomicronenhances pages 11-12
20. xie2024bacteroidesthetaiotaomicronenhances pages 9-11
21. yaekob2026currentadvancementsof pages 6-6
22. yaekob2026currentadvancementsof pages 6-7
23. ostos2024ametagenomicapproach pages 22-22
24. 4Fe–4S
25. 3Fe–4S
26. 4Fe-4S
27. 3Fe-4S
28. 10.1128/mbio.01591-24
29. 10.3389/fmicb.2024.1505218
30. 10.3389/fmicb.2024.1437098
31. 10.1128/aem.00606-23
32. 10.1038/s41579-021-00583-y
33. 10.1111/mmi.14516
34. 10.1111/mmi.12438
35. 10.1128/JB.184.4.895-903.2002
36. https://www.ncbi.nlm.nih.gov/books/NBK482349/:
37. https://doi.org/10.1128/mbio.01591-24
38. https://doi.org/10.3389/fmicb.2024.1505218
39. https://doi.org/10.3389/fmicb.2024.1437098
40. https://doi.org/10.1128/aem.00606-23
41. https://doi.org/10.1038/s41579-021-00583-y
42. https://doi.org/10.1111/mmi.14516
43. https://doi.org/10.1111/mmi.12438
44. https://doi.org/10.1128/JB.184.4.895-903.2002
45. https://doi.org/10.1038/s41579-021-00583-y,
46. https://doi.org/10.1111/mmi.14516,
47. https://doi.org/10.1128/mbio.01591-24,
48. https://doi.org/10.1128/aem.00606-23,
49. https://doi.org/10.3389/fmicb.2024.1505218,
50. https://doi.org/10.1002/fbe2.70046,
51. https://doi.org/10.3389/fmicb.2024.1437098,