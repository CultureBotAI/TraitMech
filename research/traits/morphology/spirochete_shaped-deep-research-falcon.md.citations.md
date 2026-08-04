# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** spirochete shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000693
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has an elongated, tightly coiled helical morphology with periplasmic flagella (endoflagella) located between the cell wall and outer membrane.
- **Parent traits:** METPO:1000666
- **Synonyms:** spirochete
- **Existing evidence:** DOI:10.1073/pnas.200221797: periplasmic flagella ... confer in part its flat-wave morphology (Supports spirochete morphology as a cell-cylinder and periplasmic-flagella interaction.)
- **Existing causal graph summary:** spirochete_shaped_periplasmic_flagella: 11 nodes, 11 edges

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
**Generated:** 2026-08-04T10:05:45.877709

1. nakamura2020spirocheteflagellaand pages 1-3
2. sal2008borreliaburgdorferiuniquely pages 1-2
3. liu2010cellulararchitectureof pages 8-9
4. wunder2018fcpbisa pages 6-7
5. wunder2016anovelflagellar pages 7-8
6. zambacampero2024broadlyconservedflgv pages 4-6
7. krusenstjerna2024dnaamodulatesthe pages 10-13
8. zambacampero2024broadlyconservedflgv pages 7-10
9. zambacampero2024broadlyconservedflgv pages 1-2
10. gibson2020anasymmetricsheath pages 11-13
11. sal2008borreliaburgdorferiuniquely pages 2-2
12. wunder2016anovelflagellar pages 8-9
13. gibson2020anasymmetricsheath pages 10-11
14. was
15. 10.1038/s41467-024-54806-w
16. 10.1101/2024.06.08.598065
17. 10.3390/biom14121488
18. 10.1016/j.tim.2022.09.010
19. 10.7554/eLife.53672
20. 10.3390/biom10040550
21. 10.3389/fcimb.2018.00130
22. 10.1111/mmi.13403
23. 10.1016/j.jmb.2010.09.020
24. 10.1128/JB.01421-07
25. 10.1073/pnas.200221797
26. https://doi.org/10.1038/s41467-024-54806-w
27. https://doi.org/10.1101/2024.06.08.598065
28. https://doi.org/10.3390/biom14121488
29. https://doi.org/10.1016/j.tim.2022.09.010
30. https://doi.org/10.7554/eLife.53672
31. https://doi.org/10.3390/biom10040550
32. https://doi.org/10.3389/fcimb.2018.00130
33. https://doi.org/10.1111/mmi.13403
34. https://doi.org/10.1016/j.jmb.2010.09.020
35. https://doi.org/10.1128/JB.01421-07
36. https://doi.org/10.1073/pnas.200221797
37. https://doi.org/10.3390/biom10040550,
38. https://doi.org/10.1128/jb.01421-07,
39. https://doi.org/10.1016/j.jmb.2010.09.020,
40. https://doi.org/10.3389/fcimb.2018.00130,
41. https://doi.org/10.1111/mmi.13403,
42. https://doi.org/10.7554/elife.53672,
43. https://doi.org/10.1038/s41467-024-54806-w,
44. https://doi.org/10.1101/2024.06.08.598065,