# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** non motile
- **METPO identifier:** METPO:1000703
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A motility in which an organism lacks the ability to move independently under its own power.
- **Parent traits:** METPO:1000701
- **Synonyms:** no, non-motile
- **Existing evidence:** DOI:10.3389/fmicb.2025.1514643: They are Gram-negative, non-motile rods (Organism example: Klebsiella pneumoniae is described as non-motile.) | DOI:10.1146/annurev.micro.57.030502.090832: flagellum (Bacterial flagellum review supports the absence or non-expression of the flagellar apparatus as the basis for non-motile phenotypes.)
- **Existing causal graph summary:** non_motile_absent_motility_apparatus: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **non motile** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/non_motile.yaml`.

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
**Generated:** 2026-06-18T08:55:43.581707

1. carter2024conditionalexpressionof pages 1-2
2. esteves2023phagesonfilaments pages 9-11
3. cohen2023evolutionofa pages 9-12
4. oladosu2024fliptheswitch pages 4-7
5. zhang2024anovelregulator pages 1-2
6. ramoneda2024ecologicalrelevanceof pages 5-6
7. ramoneda2024ecologicalrelevanceof pages 2-3
8. liu2024counterclockwiserotationof pages 1-2
9. hu2024rolesofresponse pages 1-2
10. guan2024flhfaffectsthe pages 1-2
11. wang2024argrregulatesmotility pages 1-2
12. dai2024acdigmpbinding pages 1-2
13. dai2024acdigmpbinding pages 8-10
14. guan2024flhfaffectsthe pages 2-6
15. dai2024acdigmpbinding pages 5-8
16. zhang2024anovelregulator pages 4-6
17. esteves2023phagesonfilaments pages 16-18
18. oladosu2024fliptheswitch pages 3-4
19. https://doi.org/10.3389/fmicb.2024.1456637
20. https://doi.org/10.1371/journal.ppat.1011537
21. https://doi.org/10.1101/2023.09.08.556628
22. https://doi.org/10.1128/aem.01548-23
23. https://doi.org/10.1186/s12866-024-03387-1
24. https://doi.org/10.1128/jb.00365-23
25. https://doi.org/10.1080/21505594.2024.2331265
26. https://doi.org/10.1038/s42003-024-07392-y
27. https://doi.org/10.1038/s41598-024-76694-2
28. https://doi.org/10.1038/s41598-024-76694-2;
29. https://doi.org/10.3390/foods13223709
30. https://doi.org/10.1093/ismejo/wrae067
31. https://doi.org/10.1128/mbio.00440-24
32. https://doi.org/10.3389/fmicb.2024.1456637,
33. https://doi.org/10.1186/s12866-024-03387-1,
34. https://doi.org/10.1093/ismejo/wrae067,
35. https://doi.org/10.1128/mbio.00440-24,
36. https://doi.org/10.1038/s42003-024-07392-y,
37. https://doi.org/10.1371/journal.ppat.1011537,
38. https://doi.org/10.1101/2023.09.08.556628,
39. https://doi.org/10.1128/jb.00365-23,
40. https://doi.org/10.1080/21505594.2024.2331265,
41. https://doi.org/10.1038/s41598-024-76694-2,
42. https://doi.org/10.1128/aem.01548-23,
43. https://doi.org/10.3390/foods13223709,