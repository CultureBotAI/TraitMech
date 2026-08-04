# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** polyphosphate granule
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000068
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An intracellular storage inclusion of inorganic polyphosphate (a polymer of many phosphate residues), historically called a volutin or metachromatic granule, serving as a phosphate and energy reserve.
- **Parent traits:** traitmech:000066
- **Synonyms:** volutin granule, metachromatic granule
- **Existing evidence:** DOI:10.1146/annurev.biochem.77.083007.093039:  (Rao, Gómez-García & Kornberg review inorganic polyphosphate, accumulated as granules, as a phosphate/energy reserve essential for growth and survival.) | DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow include polyphosphate bodies among bacterial intracellular inclusions.)
- **Existing causal graph summary:** polyphosphate_granule_storage: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **polyphosphate granule** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/polyphosphate_granule.yaml`.

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
**Generated:** 2026-08-04T09:47:47.705591

1. rao2009inorganicpolyphosphateessential pages 5-6
2. racki2017polyphosphategranulebiogenesis pages 1-3
3. omelon2013areviewof pages 6-8
4. corrales2025polyphosphatefromlactic pages 6-9
5. sebesta2024polyphosphatekinasedeletion pages 4-6
6. racki2017polyphosphategranulebiogenesis pages 4-4
7. racki2017polyphosphategranulebiogenesis pages 7-8
8. schoeppe2024anupdateon pages 15-16
9. camejo2016candidatusaccumulibacterphosphatis pages 6-8
10. sebesta2024polyphosphatekinasedeletion pages 6-8
11. racki2017polyphosphategranulebiogenesis pages 6-7
12. rao2009inorganicpolyphosphateessential pages 4-5
13. moreno2013polyphosphateandits pages 1-2
14. kornberg2003inorganicpolyphosphatea pages 2-4
15. schoeppe2024anupdateon pages 2-4
16. racki2017polyphosphategranulebiogenesis pages 1-1
17. tumlirsch2015formationofpolyphosphate pages 1-4
18. tumlirsch2015formationofpolyphosphate pages 12-15
19. tumlirsch2015formationofpolyphosphate pages 7-10
20. racki2017polyphosphategranulebiogenesis pages 3-4
21. camejo2016candidatusaccumulibacterphosphatis pages 6-6
22. camejo2016candidatusaccumulibacterphosphatis pages 1-2
23. camejo2016candidatusaccumulibacterphosphatis pages 12-12
24. sebesta2024polyphosphatekinasedeletion pages 1-2
25. schoeppe2024anupdateon pages 16-17
26. 10.3390/foods14132211
27. 10.1128/AEM.02279-15
28. 10.3389/fpls.2024.1342496
29. es
30. 10.1073/pnas.1615575114
31. 10.1146/annurev.biochem.77.083007.093039
32. 10.3390/biom14080937
33. 10.1016/j.watres.2016.06.033
34. 10.1371/journal.ppat.1003230
35. 10.1007/s00223-013-9784-9
36. 10.1146/annurev.biochem.68.1.89
37. https://doi.org/10.3390/foods14132211;
38. https://doi.org/10.1128/AEM.02279-15
39. https://doi.org/10.1073/pnas.1615575114
40. https://doi.org/10.3390/foods14132211
41. https://doi.org/10.1146/annurev.biochem.77.083007.093039;
42. https://doi.org/10.1371/journal.ppat.1003230;
43. https://doi.org/10.3390/biom14080937
44. https://doi.org/10.1016/j.watres.2016.06.033
45. https://doi.org/10.3389/fpls.2024.1342496
46. https://doi.org/10.1146/annurev.biochem.77.083007.093039
47. https://doi.org/10.1371/journal.ppat.1003230
48. https://doi.org/10.1007/s00223-013-9784-9
49. https://doi.org/10.1146/annurev.biochem.68.1.89
50. https://doi.org/10.1371/journal.ppat.1003230,
51. https://doi.org/10.3390/biom14080937,
52. https://doi.org/10.1007/s00223-013-9784-9,
53. https://doi.org/10.1073/pnas.1615575114,
54. https://doi.org/10.1146/annurev.biochem.68.1.89,
55. https://doi.org/10.1146/annurev.biochem.77.083007.093039,
56. https://doi.org/10.3390/foods14132211,
57. https://doi.org/10.1128/aem.02279-15,
58. https://doi.org/10.1016/j.watres.2016.06.033,
59. https://doi.org/10.3389/fpls.2024.1342496,