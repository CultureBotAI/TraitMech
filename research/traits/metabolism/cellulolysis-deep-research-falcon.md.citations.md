# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cellulolysis
- **METPO identifier:** traitmech:000111
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biopolymer-degradation metabolism in which an organism hydrolyzes cellulose to cellodextrins and glucose using cellulase systems, sometimes organized into cellulosomes.
- **Parent traits:** traitmech:000110
- **Synonyms:** cellulolytic, cellulose degradation
- **Existing evidence:** DOI:10.1128/MMBR.66.3.506-577.2002:  (Lynd et al. review microbial cellulose utilization, its enzymology, and cellulosome systems.) | DOI:10.1016/j.cbpa.2015.10.018:  (Cragg et al. place cellulose deconstruction within lignocellulose degradation across diverse organisms.)
- **Existing causal graph summary:** cellulolysis_cellulase_systems: 14 nodes, 10 edges

## Research Objective

Research the microbial trait **cellulolysis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/cellulolysis.yaml`.

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
**Generated:** 2026-07-30T18:24:01.860017

1. schiml2024microbialconsortiadriving pages 13-14
2. bautistacruz2024cellulolyticaerobicbacteria pages 5-6
3. rocha2024ecologicalbeneficialand pages 2-4
4. hsin2024lignocellulosedegradationin pages 11-15
5. minor2024agenomicanalysis pages 2-3
6. cerisy2019abctransportersrequired pages 9-10
7. nogueira2024proteomeprofilingof pages 6-8
8. bautistacruz2024cellulolyticaerobicbacteria pages 1-2
9. bautistacruz2024cellulolyticaerobicbacteria pages 3-5
10. minor2024agenomicanalysis pages 1-2
11. bissaro2023lyticpolysaccharidemonooxygenases pages 4-6
12. christopher2023earlycellularevents pages 15-15
13. bissaro2018oxidoreductasesandreactive pages 5-6
14. minor2024agenomicanalysis pages 13-14
15. minor2024agenomicanalysis pages 3-4
16. nogueira2024proteomeprofilingof pages 1-2
17. bissaro2023lyticpolysaccharidemonooxygenases pages 1-2
18. bissaro2023lyticpolysaccharidemonooxygenases pages 2-4
19. bissaro2018oxidoreductasesandreactive pages 6-8
20. bissaro2023lyticpolysaccharidemonooxygenases pages 6-7
21. paula2018newgenomicapproaches pages 3-4
22. minor2024agenomicanalysis pages 11-13
23. label
24. 10.3389/fmicb.2024.1473396
25. 10.1128/aem.01742-24
26. 10.3390/biology13020102
27. 10.1186/s12934-023-02279-9
28. 10.1111/1751-7915.14516
29. 10.1042/EBC20220250
30. 10.1038/s41598-023-32340-x
31. 10.1128/JB.00241-19
32. 10.1128/MMBR.00029-18
33. https://doi.org/10.3389/fmicb.2024.1473396
34. https://doi.org/10.1128/aem.01742-24
35. https://doi.org/10.3390/biology13020102
36. https://doi.org/10.1186/s12934-023-02279-9
37. https://doi.org/10.1111/1751-7915.14516
38. https://doi.org/10.1042/EBC20220250
39. https://doi.org/10.1038/s41598-023-32340-x
40. https://doi.org/10.1128/JB.00241-19
41. https://doi.org/10.1128/MMBR.00029-18
42. https://doi.org/10.3390/biology13020102,
43. https://doi.org/10.3389/fmicb.2024.1473396,
44. https://doi.org/10.1128/aem.01742-24,
45. https://doi.org/10.1101/2024.11.06.622210,
46. https://doi.org/10.1186/s12934-023-02279-9,
47. https://doi.org/10.1042/ebc20220250,
48. https://doi.org/10.1128/mmbr.00029-18,
49. https://doi.org/10.1128/jb.00241-19,
50. https://doi.org/10.1155/2018/1974151,
51. https://doi.org/10.1111/1751-7915.14516,
52. https://doi.org/10.1038/s41598-023-32340-x,