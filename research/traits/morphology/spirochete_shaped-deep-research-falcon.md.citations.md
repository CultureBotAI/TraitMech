# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** spirochete shaped
- **METPO identifier:** METPO:1000693
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has an elongated, tightly coiled helical morphology with periplasmic flagella (endoflagella) located between the cell wall and outer membrane.
- **Parent traits:** METPO:1000666
- **Synonyms:** spirochete
- **Existing evidence:** DOI:10.1073/pnas.200221797: periplasmic flagella ... confer in part its flat-wave morphology (Supports spirochete morphology as a cell-cylinder and periplasmic-flagella interaction.)
- **Existing causal graph summary:** spirochete_shaped_periplasmic_flagella: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **spirochete shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/spirochete_shaped.yaml`.

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
**Generated:** 2026-06-18T09:56:18.611630

1. lynch2023lysinoalaninecrosslinkingis pages 1-2
2. nakamura2024structureanddynamics pages 17-18
3. halte2024flhefunctionsas pages 2-3
4. zambacampero2024broadlyconservedflgv pages 7-10
5. abe2023machinelearningbasedmotion pages 1-2
6. zambacampero2024broadlyconservedflgv pages 4-6
7. abe2023machinelearningbasedmotion pages 4-5
8. zambacampero2024broadlyconservedflgv pages 6-7
9. zambacampero2024broadlyconservedflgv pages 13-14
10. zambacampero2024broadlyconservedflgv pages 1-2
11. zambacampero2024broadlyconservedflgv pages 14-15
12. GO:0009288
13. NCBITaxon:139
14. label-only
15. GO:0042597
16. GO:0019867
17. NCBITaxon:171
18. GO:0009288 or label-only for PF filament
19. PATO label-only
20. CHEBI:73703 if accepted, otherwise label-only
21. GO:0009289
22. GO:0048870
23. GO:0009274-related label-only
24. GO:0009252
25. METPO parent label-only
26. GO:0001893
27. GO:0009420
28. GO:0051301
29. GO:0008360
30. GO:0019867-related label-only
31. GO:0007155
32. GO:0007155-related label-only
33. https://doi.org/10.1038/s41467-024-54806-w
34. https://doi.org/10.1093/pnasnexus/pgad349
35. https://doi.org/10.1038/s41467-023-43366-0
36. https://doi.org/10.1038/s41467-024-50278-0
37. https://doi.org/10.3390/biom14121488
38. https://doi.org/10.3390/ijms24065594
39. https://doi.org/10.1093/pnasnexus/pgad349,
40. https://doi.org/10.1038/s41467-023-43366-0,
41. https://doi.org/10.3390/biom14121488,
42. https://doi.org/10.1038/s41467-024-50278-0,
43. https://doi.org/10.1038/s41467-024-54806-w,