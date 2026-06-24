# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** hydrogenotrophic
- **METPO identifier:** METPO:1000646
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses molecular hydrogen as an electron donor for energy generation and carbon dioxide as the primary carbon source.
- **Parent traits:** METPO:1000631
- **Synonyms:** 
- **Existing evidence:** DOI:10.21775/cimb.006.159: reversible oxidation of hydrogen gas (Review supports hydrogenase-catalyzed H2 oxidation and microbial energy metabolism.) | DOI:10.1128/AEM.02473-10: assimilation of CO2 (Review supports CO2 assimilation into cellular carbon in autotrophic metabolism.)
- **Existing causal graph summary:** hydrogenotrophic_hydrogen_oxidation_fixation: 9 nodes, 7 edges

## Research Objective

Research the microbial trait **hydrogenotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/hydrogenotrophic.yaml`.

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
**Generated:** 2026-06-18T11:45:24.113025

1. menez2020abiotichydrogenand pages 5-8
2. gregory2019subsurfacemicrobialhydrogen pages 5-8
3. lappan2023molecularhydrogenin pages 1-2
4. szuhaj2023regulationofthe pages 1-2
5. tyne2023identifyingandunderstanding pages 1-3
6. kremp2022athirdway pages 1-2
7. islam2023microbialhydrogencycling pages 2-4
8. kremp2022athirdway pages 2-5
9. pichechoquette2019molecularhydrogena pages 6-8
10. katsyv2023molecularbasisof pages 1-2
11. katsyv2023molecularbasisof pages 2-3
12. jain2023microbialconversionof pages 1-2
13. pichechoquette2019molecularhydrogena pages 8-9
14. menez2020abiotichydrogenand pages 8-11
15. NiFe
16. e
17. FeFe
18. Fe
19. fefe
20. https://doi.org/10.2138/gselements.16.1.39
21. https://doi.org/10.1038/s41564-023-01322-0
22. https://doi.org/10.1128/AEM.02418-18
23. https://doi.org/10.1128/spectrum.01385-22
24. https://doi.org/10.3390/microorganisms7020053
25. https://doi.org/10.1007/s00253-023-12700-3
26. https://doi.org/10.1002/cplu.202300270
27. https://doi.org/10.1021/jacs.2c11683
28. https://doi.org/10.1111/1751-7915.14300
29. https://doi.org/10.1021/acs.est.2c08652
30. https://doi.org/10.5713/ab.23.0294
31. https://doi.org/10.1071/MA23007
32. https://doi.org/10.3390/microorganisms7020053;
33. https://doi.org/10.1038/s41564-023-01322-0,
34. https://doi.org/10.1111/1751-7915.14300,
35. https://doi.org/10.1021/acs.est.2c08652,
36. https://doi.org/10.2138/gselements.16.1.39,
37. https://doi.org/10.3390/microorganisms7020053,
38. https://doi.org/10.1007/s00253-023-12700-3,
39. https://doi.org/10.1128/spectrum.01385-22,
40. https://doi.org/10.1021/jacs.2c11683,
41. https://doi.org/10.1128/aem.02418-18,
42. https://doi.org/10.1002/cplu.202300270,
43. https://doi.org/10.5713/ab.23.0294,
44. https://doi.org/10.1071/ma23007,