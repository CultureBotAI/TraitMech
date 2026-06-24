# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** strictly anaerobic
- **METPO identifier:** METPO:1000611
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An obligately anaerobic oxygen preference in which a microorganism does not grow in the presence of oxygen gas (O₂).
- **Parent traits:** METPO:1000607
- **Synonyms:** strict obligate anaerobe
- **Existing evidence:** https://www.ncbi.nlm.nih.gov/books/NBK482349/: will not survive if there is more than half a percent oxygen (Supports strict anaerobiosis as a highly oxygen-sensitive subtype.) | PMID:39189748: Clostridioides difficile is a strict anaerobic, sporulating Firmicutes (Organism example: Clostridioides difficile is described as strictly anaerobic.)
- **Existing causal graph summary:** strict_anaerobe_oxygen_sensitivity: 5 nodes, 4 edges

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
**Generated:** 2026-06-18T01:53:34.753095

1. okabe2023oxygentoleranceand pages 6-7
2. caulat2024physiologicalroleand pages 2-5
3. zund2025decipheringoxidativestress pages 5-7
4. rose2025commensalresilienceancient pages 7-9
5. caulat2024physiologicalroleand pages 1-2
6. caulat2024physiologicalroleand pages 9-11
7. okabe2023oxygentoleranceand pages 5-6
8. dyksma2024growthofsulfatereducing pages 1-2
9. okabe2023oxygentoleranceand pages 1-2
10. rose2025commensalresilienceancient pages 9-11
11. lotoux2025defensearsenalof pages 1-2
12. xie2024bacteroidesthetaiotaomicronenhances pages 8-9
13. dyksma2024growthofsulfatereducing pages 5-6
14. dyksma2024growthofsulfatereducing pages 6-10
15. lotoux2025defensearsenalof pages 8-10
16. lotoux2025defensearsenalof pages 21-23
17. lotoux2025defensearsenalof pages 15-17
18. okabe2023oxygentoleranceand pages 8-9
19. mcgregor2025fusobacteriumnucleatum pages 10-12
20. bystrom2024couplingbutyrylcoenzymea pages 17-21
21. okabe2023oxygentoleranceand pages 7-8
22. okabe2023oxygentoleranceand pages 2-3
23. 4Fe-4S
24. is specific
25. https://www.ncbi.nlm.nih.gov/books/NBK482349/:
26. https://doi.org/10.1128/iai.00502-24
27. https://doi.org/10.1038/s43705-023-00251-7
28. https://doi.org/10.1128/mbio.03753-24
29. https://doi.org/10.1128/mbio.01591-24
30. https://doi.org/10.1186/s40168-024-01909-7
31. https://doi.org/10.1093/femsec/fiaf054
32. https://doi.org/10.3389/fmicb.2024.1505218
33. https://doi.org/10.1128/iai.00502-24,
34. https://doi.org/10.1093/femsec/fiaf054,
35. https://doi.org/10.1038/s43705-023-00251-7,
36. https://doi.org/10.1128/mbio.01591-24,
37. https://doi.org/10.1128/mbio.03753-24,
38. https://doi.org/10.1186/s40168-024-01909-7,
39. https://doi.org/10.1128/jb.00090-25,
40. https://doi.org/10.14288/1.0447284,
41. https://doi.org/10.3389/fmicb.2024.1505218,