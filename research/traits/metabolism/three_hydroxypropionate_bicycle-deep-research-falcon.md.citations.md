# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** 3-hydroxypropionate bicycle
- **METPO identifier:** traitmech:000023
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway in which two molecules of bicarbonate are fixed via 3-hydroxypropionate and converted to glyoxylate and pyruvate. It is characteristic of the filamentous anoxygenic phototroph Chloroflexus aurantiacus.
- **Parent traits:** traitmech:000019
- **Synonyms:** 3-hydroxypropionate cycle
- **Existing evidence:** DOI:10.1128/AEM.02473-10:  (Berg review describes the 3-hydroxypropionate bicycle and its association with Chloroflexus.) | DOI:10.1146/annurev-marine-120709-142712:  (Hügler & Sievert include the 3-hydroxypropionate pathway among autotrophic carbon-fixation strategies.)
- **Existing causal graph summary:** three_hp_bicycle_chloroflexus: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **3-hydroxypropionate bicycle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/three_hydroxypropionate_bicycle.yaml`.

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
**Generated:** 2026-06-18T06:16:32.601386

1. mclean2022invitrorealisation pages 22-29
2. hugler2011beyondthecalvin pages 9-10
3. kang2023insightsintoenzyme pages 2-4
4. grundling2020propionylcoasynthasecharacterization pages 21-24
5. garritano2022carbonfixationpathways pages 2-3
6. hugler2011beyondthecalvin pages 7-9
7. zarzycki2011coassimilationoforganic pages 1-2
8. freches2024thebiotechnologicalpotential pages 14-15
9. zarzycki2011coassimilationoforganic pages 5-7
10. mclean2023exploringalternativepathways pages 2-3
11. mclean2023exploringalternativepathways pages 1-2
12. garritano2022carbonfixationpathways pages 1-2
13. zarzycki2011coassimilationoforganic pages 2-3
14. mclean2023exploringalternativepathways pages 7-10
15. mclean2022invitrorealisation pages 29-35
16. tommasi2024thebiochemistryof pages 12-14
17. wang2023microbialconversionand pages 3-5
18. freches2024thebiotechnologicalpotential pages 17-18
19. mclean2023exploringalternativepathways pages 6-7
20. tommasi2024thebiochemistryof pages 10-12
21. garritano2022carbonfixationpathways pages 9-10
22. mclean2022invitrorealisation pages 88-91
23. candidate context only
24. https://doi.org/10.1146/annurev-marine-120709-142712
25. https://doi.org/10.17192/z2022.0467
26. https://doi.org/10.1126/sciadv.adh4299
27. https://doi.org/10.1128/AEM.00705-11
28. https://doi.org/10.17192/z2020.0502
29. https://doi.org/10.4014/jmb.2306.06005
30. https://doi.org/10.1128/AEM.01756-23
31. https://doi.org/10.1093/pnasnexus/pgac226
32. https://doi.org/10.1128/aem.01756-23
33. https://doi.org/10.3390/catal14100679
34. https://doi.org/10.1146/annurev-marine-120709-142712,
35. https://doi.org/10.1128/aem.00705-11,
36. https://doi.org/10.17192/z2022.0467,
37. https://doi.org/10.4014/jmb.2306.06005,
38. https://doi.org/10.1128/aem.01756-23,
39. https://doi.org/10.17192/z2020.0502,
40. https://doi.org/10.1093/pnasnexus/pgac226,
41. https://doi.org/10.1126/sciadv.adh4299,
42. https://doi.org/10.3390/catal14100679,
43. https://doi.org/10.29328/journal.acee.1001055,