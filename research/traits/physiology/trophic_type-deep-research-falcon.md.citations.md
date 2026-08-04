# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** trophic type
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000631
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that is describing how an organism obtains carbon, energy, and electron donors for growth and metabolism.
- **Parent traits:** METPO:1000059
- **Synonyms:** Physiology and metabolism.nutrition type.type, nutritional type, pathways
- **Existing evidence:** DOI:10.1146/annurev.micro.61.080706.093130: carbon source, energy source, and electron donor (Microbial physiology review frames trophic type as the joint classification by carbon, energy, and electron-donor source.) | DOI:10.1073/pnas.0903507106: molecular mechanisms of adaptation (Comparative genomics supports the classification of bacteria by trophic strategy from genome-encoded pathways.)
- **Existing causal graph summary:** trophic_type_classification_axes: 14 nodes, 13 edges

## Research Objective

Research the microbial trait **trophic type** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/trophic_type.yaml`.

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
**Generated:** 2026-08-04T12:11:30.312862

1. weissbrodt2023basicmicrobiologyand pages 19-22
2. schenone2024mixotrophicprotistsand pages 2-3
3. li2024insitucommunity pages 1-2
4. atencio2024metabolicadaptationsunderpin pages 1-2
5. jahn2024theenergymetabolism pages 1-2
6. yang2024metagenomicsandstable pages 1-2
7. tothero2024leptothrixochraceagenomes pages 13-15
8. tothero2024leptothrixochraceagenomes pages 1-2
9. li2024arcobacteraceaeareubiquitous pages 1-2
10. li2024arcobacteraceaeareubiquitous pages 10-12
11. conners2024thephototrophicpurple pages 1-2
12. millette2024recommendationsforadvancing pages 11-12
13. NiFe
14. 10.2166/9781789062304_0009
15. 10.1128/aem.00748-24
16. 10.1128/aem.00599-24
17. 10.1128/msystems.00513-24
18. 10.1038/s41598-024-68868-9
19. 10.1093/femsec/fiae105
20. 10.1021/acs.est.4c00248
21. 10.1128/spectrum.02177-23
22. 10.1111/1751-7915.14552
23. 10.3389/fevo.2024.1505037
24. 10.3389/fmars.2024.1392673
25. https://m-jahn.shinyapps.io/ShinyLib/.
26. https://doi.org/10.2166/9781789062304_0009
27. https://doi.org/10.1128/aem.00748-24
28. https://doi.org/10.1128/aem.00599-24
29. https://doi.org/10.1128/msystems.00513-24
30. https://doi.org/10.1038/s41598-024-68868-9
31. https://doi.org/10.1093/femsec/fiae105
32. https://doi.org/10.1021/acs.est.4c00248
33. https://doi.org/10.1128/spectrum.02177-23
34. https://doi.org/10.1111/1751-7915.14552
35. https://doi.org/10.3389/fevo.2024.1505037
36. https://doi.org/10.3389/fmars.2024.1392673
37. https://doi.org/10.2166/9781789062304\_0009,
38. https://doi.org/10.1128/aem.00599-24,
39. https://doi.org/10.1128/msystems.00513-24,
40. https://doi.org/10.3389/fevo.2024.1505037,
41. https://doi.org/10.1128/spectrum.02177-23,
42. https://doi.org/10.1038/s41598-024-68868-9,
43. https://doi.org/10.1093/femsec/fiae105,
44. https://doi.org/10.1128/aem.00748-24,
45. https://doi.org/10.1021/acs.est.4c00248,
46. https://doi.org/10.1111/1751-7915.14552,
47. https://doi.org/10.3389/fmars.2024.1392673,