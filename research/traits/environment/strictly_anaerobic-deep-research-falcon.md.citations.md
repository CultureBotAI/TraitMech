# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** strictly anaerobic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000611
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An obligately anaerobic oxygen preference in which a microorganism does not grow in the presence of oxygen gas (O₂).
- **Parent traits:** METPO:1000607
- **Synonyms:** strict obligate anaerobe
- **Existing evidence:** https://www.ncbi.nlm.nih.gov/books/NBK482349/: will not survive if there is more than half a percent oxygen (Supports strict anaerobiosis as a highly oxygen-sensitive subtype.) | PMID:39189748: Clostridioides difficile is a strict anaerobic, sporulating Firmicutes (Organism example: Clostridioides difficile is described as strictly anaerobic.)
- **Existing causal graph summary:** strict_anaerobe_oxygen_sensitivity: 8 nodes, 7 edges

## Research Objective

Research the microbial trait **strictly anaerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/strictly_anaerobic.yaml`.

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
**Generated:** 2026-08-04T03:35:58.300637

1. butler2023bacteroidesfragilismaintains pages 1-2
2. caulat2024physiologicalroleand pages 5-7
3. okabe2023oxygentoleranceand pages 1-2
4. caulat2024physiologicalroleand pages 1-2
5. khademian2020doreactiveoxygen pages 1-2
6. butler2023bacteroidesfragilismaintains pages 5-7
7. lu2021whenanaerobesencounter pages 4-6
8. khademian2020doreactiveoxygen pages 9-10
9. lu2021whenanaerobesencounter pages 11-13
10. caulat2024physiologicalroleand pages 9-11
11. caulat2024physiologicalroleand pages 13-15
12. lu2021whenanaerobesencounter pages 13-15
13. lotoux2025defensearsenalof pages 1-2
14. lu2021whenanaerobesencounter pages 8-9
15. lu2021whenanaerobesencounter pages 9-11
16. lu2021whenanaerobesencounter pages 22-27
17. okabe2023oxygentoleranceand pages 11-12
18. 4Fe–4S
19. 4Fe-4S
20. s
21. acts at
22. 10.1128/mbio.01591-24
23. 10.1128/jb.00389-22
24. 10.1038/s43705-023-00251-7
25. 10.1111/mmi.14516
26. 10.1038/s41579-021-00583-y
27. 10.1073/pnas.1800120115
28. 10.1128/mbio.03753-24
29. https://www.ncbi.nlm.nih.gov/books/NBK482349/:
30. https://doi.org/10.1128/mbio.01591-24
31. https://doi.org/10.1128/jb.00389-22
32. https://doi.org/10.1038/s43705-023-00251-7
33. https://doi.org/10.1111/mmi.14516
34. https://doi.org/10.1038/s41579-021-00583-y
35. https://doi.org/10.1073/pnas.1800120115
36. https://doi.org/10.1128/mbio.03753-24
37. https://doi.org/10.1111/mmi.14516,
38. https://doi.org/10.1038/s41579-021-00583-y,
39. https://doi.org/10.1128/jb.00389-22,
40. https://doi.org/10.1128/mbio.01591-24,
41. https://doi.org/10.1038/s43705-023-00251-7,
42. https://doi.org/10.1128/mbio.03753-24,