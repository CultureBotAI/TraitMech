# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** methylotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000651
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy and carbon from reduced one-carbon compounds.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_methylotroph, methylotroph, methylotrophy
- **Existing evidence:** DOI:10.3389/fbioe.2021.787791: methanol utilization in methylotrophy (Review supports methanol oxidation and formaldehyde assimilation as central methylotrophy mechanisms.)
- **Existing causal graph summary:** methylotrophic_methanol_assimilation: 19 nodes, 15 edges

## Research Objective

Research the microbial trait **methylotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/methylotrophic.yaml`.

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
**Generated:** 2026-08-04T11:32:33.284258

1. nayak2016selectionmaintainsapparently pages 8-9
2. le2021methanoldehydrogenasesas pages 4-6
3. voutsinos2024weatheredgranitesand pages 2-4
4. wegner2019lanthanidedependentmethylotrophsof pages 8-9
5. wegner2019lanthanidedependentmethylotrophsof pages 2-3
6. nayak2016selectionmaintainsapparently pages 3-4
7. samanta2024fromgenometo pages 18-20
8. le2021methanoldehydrogenasesas pages 2-3
9. shao2024transcriptomicdatareveals pages 2-4
10. shao2024transcriptomicdatareveals pages 7-9
11. awala2024nitrousoxiderespiration pages 8-9
12. alessa2021comprehensivecomparativegenomics pages 10-11
13. voutsinos2024weatheredgranitesand pages 10-12
14. samanta2024fromgenometo pages 12-14
15. alessa2021comprehensivecomparativegenomics pages 2-3
16. rocha2024rareearthelements pages 2-5
17. chistoserdova2018currenttrendsin pages 3-4
18. chistoserdova2018currenttrendsin pages 2-3
19. wegner2019lanthanidedependentmethylotrophsof pages 12-13
20. nayak2016selectionmaintainsapparently pages 4-6
21. awala2024nitrousoxiderespiration pages 2-3
22. uses
23. 10.1016/j.tim.2018.01.011
24. 10.1128/msystems.00248-24
25. 10.1186/s12915-024-01841-0
26. 10.1186/s12864-024-10923-w
27. 10.1038/s41467-024-48161-z
28. 10.1111/1751-7915.14503
29. 10.3389/fbioe.2021.787791
30. 10.3389/fmicb.2021.740610
31. 10.1128/AEM.01830-19
32. 10.1016/j.cub.2016.04.029
33. https://doi.org/10.1016/j.tim.2018.01.011
34. https://doi.org/10.1128/msystems.00248-24
35. https://doi.org/10.1186/s12915-024-01841-0
36. https://doi.org/10.1186/s12864-024-10923-w
37. https://doi.org/10.1038/s41467-024-48161-z
38. https://doi.org/10.1111/1751-7915.14503
39. https://doi.org/10.3389/fbioe.2021.787791
40. https://doi.org/10.3389/fmicb.2021.740610
41. https://doi.org/10.1128/AEM.01830-19
42. https://doi.org/10.1016/j.cub.2016.04.029
43. https://doi.org/10.1016/j.tim.2018.01.011,
44. https://doi.org/10.1128/aem.01830-19,
45. https://doi.org/10.1016/j.cub.2016.04.029,
46. https://doi.org/10.1186/s12915-024-01841-0,
47. https://doi.org/10.3389/fbioe.2021.787791,
48. https://doi.org/10.1128/msystems.00248-24,
49. https://doi.org/10.1186/s12864-024-10923-w,
50. https://doi.org/10.1038/s41467-024-48161-z,
51. https://doi.org/10.1111/1751-7915.14503,
52. https://doi.org/10.3389/fmicb.2021.740610,