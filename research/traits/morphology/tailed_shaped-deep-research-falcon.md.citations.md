# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** tailed shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000695
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has an elongated polar appendage or stalk extending from the cell body.
- **Parent traits:** METPO:1000666
- **Synonyms:** tailed
- **Existing evidence:** DOI:10.1146/annurev.micro.061705.103240: prosthecate bacteria (Prosthecate-bacteria review supports tailed/stalked cell morphology in Caulobacter and related lineages.) | DOI:10.1146/annurev-cellbio-101011-155745: polar growth (Cell-shape review supports unipolar peptidoglycan growth as the basis for stalk-like polar appendages.)
- **Existing causal graph summary:** tailed_shaped_polar_stalk_growth: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **tailed shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/tailed_shaped.yaml`.

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
**Generated:** 2026-08-04T10:26:15.851539

1. jacq2024functionalspecializationof pages 6-10
2. pohl2024adynamicbactofilin pages 15-16
3. billini2019aspecializedmrebdependent pages 14-16
4. billini2019aspecializedmrebdependent pages 18-19
5. barrows2023synchronizedswarmersand pages 11-13
6. billini2024thecytoplasmicphosphate pages 1-2
7. billini2019aspecializedmrebdependent pages 2-3
8. billini2019aspecializedmrebdependent pages 19-21
9. jacq2024functionalspecializationof pages 13-17
10. jacq2024functionalspecializationof pages 1-6
11. pohl2024adynamicbactofilin pages 9-10
12. billini2019aspecializedmrebdependent pages 21-22
13. pohl2024adynamicbactofilin pages 1-2
14. lubin2016identificationofthe pages 1-2
15. billini2024thecytoplasmicphosphate pages 10-11
16. billini2024thecytoplasmicphosphate pages 8-9
17. billini2024thecytoplasmicphosphate pages 7-8
18. pohl2024adynamicbactofilin pages 6-7
19. 10.1038/s42003-024-06469-y
20. 10.7554/eLife.86577
21. 10.1101/2024.12.16.628611
22. 10.1128/jb.00384-22
23. 10.1371/journal.pgen.1007897
24. 10.1128/JB.00658-15
25. 10.1038/nature12900
26. 10.1016/j.cell.2012.10.046
27. https://doi.org/10.1038/s42003-024-06469-y
28. https://doi.org/10.7554/eLife.86577
29. https://doi.org/10.1101/2024.12.16.628611
30. https://doi.org/10.1128/jb.00384-22
31. https://doi.org/10.1371/journal.pgen.1007897
32. https://doi.org/10.1128/JB.00658-15
33. https://doi.org/10.1038/nature12900
34. https://doi.org/10.1016/j.cell.2012.10.046
35. https://doi.org/10.1371/journal.pgen.1007897,
36. https://doi.org/10.1038/s42003-024-06469-y,
37. https://doi.org/10.1101/2024.12.16.628611,
38. https://doi.org/10.1128/jb.00384-22,
39. https://doi.org/10.1128/jb.00658-15,
40. https://doi.org/10.7554/elife.86577.2,