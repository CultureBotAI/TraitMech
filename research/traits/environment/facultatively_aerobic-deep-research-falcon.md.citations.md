# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** facultatively aerobic
- **METPO identifier:** METPO:1000608
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference in which growth can occur without oxygen but is capable of aerobic growth.
- **Parent traits:** METPO:1000601
- **Synonyms:** facultative, facultative aerobe
- **Existing evidence:** PMID:21413255: preferentially utilize oxygen as a terminal electron acceptor (Supports facultative aerobic growth when oxygen is available.) | PMID:16142505: A facultative aerobic, moderately thermophilic, spore forming bacterium (Organism example: Anoxybacillus kamchatkensis strain JW/VK-KG4 is described as facultatively aerobic.)
- **Existing causal graph summary:** facultative_aerobe_oxygen_flexible_growth: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **facultatively aerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultatively_aerobic.yaml`.

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
**Generated:** 2026-06-17T22:33:25.477461

1. lamoureux2023amultiscaleexpression pages 10-12
2. felczak2023respirationisessential pages 2-4
3. butler2023bacteroidesfragilismaintains pages 1-2
4. butler2023bacteroidesfragilismaintains pages 2-5
5. dyksma2023oxygenrespirationand pages 1-2
6. butler2023bacteroidesfragilismaintains pages 5-7
7. nastasi2024membraneboundredoxenzyme pages 4-7
8. nastasi2024membraneboundredoxenzyme pages 13-15
9. nastasi2024cyanideinsensitiveoxidase pages 2-3
10. brown2023conservedmetabolicregulator pages 12-14
11. alleman2023mechanismsforgenerating pages 7-9
12. liu2025crpandarc pages 1-2
13. felczak2023respirationisessential pages 1-2
14. brown2023conservedmetabolicregulator pages 1-3
15. nastasi2024membraneboundredoxenzyme pages 2-4
16. ing
17. 4Fe-4S
18. s
19. 4Fe–4S
20. https://doi.org/10.1128/jb.00389-22;
21. https://doi.org/10.1128/mbio.02043-23;
22. https://doi.org/10.1128/mbio.01448-23;
23. https://doi.org/10.1093/nar/gkad750;
24. https://doi.org/10.1038/s41467-023-42074-z;
25. https://doi.org/10.1128/aem.00378-23;
26. https://doi.org/10.3390/ijms25021277;
27. https://doi.org/10.3390/antiox13030383;
28. https://doi.org/10.1128/jb.00389-22
29. https://doi.org/10.1128/mbio.02043-23
30. https://doi.org/10.1128/mbio.01448-23
31. https://doi.org/10.1093/nar/gkad750
32. https://doi.org/10.1038/s41467-023-42074-z
33. https://doi.org/10.1128/aem.00378-23
34. https://doi.org/10.3390/ijms25021277
35. https://doi.org/10.3390/antiox13030383
36. https://doi.org/10.1128/jb.00389-22,
37. https://doi.org/10.1038/s41467-023-42074-z,
38. https://doi.org/10.1093/nar/gkad750,
39. https://doi.org/10.1128/mbio.02043-23,
40. https://doi.org/10.1128/mbio.01448-23,
41. https://doi.org/10.3390/ijms25021277,
42. https://doi.org/10.3390/antiox13030383,
43. https://doi.org/10.1128/aem.00378-23,
44. https://doi.org/10.1128/spectrum.03324-24,