# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** mycelial growth
- **METPO identifier:** traitmech:000074
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait in which a bacterium grows as branching, filamentous hyphae that form a mycelium, often with subsequent differentiation into aerial hyphae and spores, as in Streptomyces.
- **Parent traits:** METPO:1000059
- **Synonyms:** mycelium-forming, hyphal growth
- **Existing evidence:** DOI:10.1038/nrmicro1968:  (Flärdh & Buttner describe Streptomyces growth as a branching hyphal mycelium with subsequent morphological differentiation.) | DOI:10.1038/nrmicro3178:  (Claessen et al. treat filamentous/mycelial growth as a bacterial solution to multicellularity.)
- **Existing causal graph summary:** mycelial_branching_hyphal_growth: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **mycelial growth** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/mycelial_growth.yaml`.

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
**Generated:** 2026-06-18T08:59:29.640432

1. schlimpert2023thebestof pages 8-10
2. bhowmick2023osmoticstressresponses pages 1-2
3. bhowmick2024cellshapeand pages 1-2
4. bhowmick2024cellshapeand pages 8-10
5. falguera2024stressresponsesaffectinga pages 16-22
6. bhowmick2023osmoticstressresponses pages 2-3
7. bhowmick2023osmoticstressresponses pages 7-8
8. bhowmick2023osmoticstressresponses pages 6-7
9. claessen2024thestomatinlikeprotein pages 5-7
10. kato2023redoxactivecompoundgenerated pages 1-7
11. sen2024adispensablesepiva pages 1-2
12. yague2023ftszphosphorylationpleiotropically pages 16-17
13. claessen2024thestomatinlikeprotein pages 1-5
14. claessen2024thestomatinlikeprotein pages 7-9
15. falguera2024stressresponsesaffectinga pages 22-26
16. schlimpert2023thebestof pages 1-2
17. song2023methylhalidetransferasebased pages 1-2
18. bhowmick2024cellshapeand pages 5-8
19. yague2023ftszphosphorylationpleiotropically pages 8-10
20. yague2023ftszphosphorylationpleiotropically pages 10-13
21. claessen2024thestomatinlikeprotein pages 17-20
22. yague2023ftszphosphorylationpleiotropically pages 13-15
23. kato2023redoxactivecompoundgenerated pages 15-20
24. song2023methylhalidetransferasebased pages 4-7
25. that
26. https://doi.org/10.1128/jb.00153-23;
27. https://doi.org/10.1093/femsml/uqad020;
28. https://doi.org/10.21203/rs.3.rs-3811693/v1;
29. https://doi.org/10.1128/mbio.01492-24;
30. https://doi.org/10.1007/s10482-022-01778-w;
31. https://doi.org/10.1101/2023.01.12.523877;
32. https://doi.org/10.1038/s41467-023-37087-7;
33. https://doi.org/10.1128/jb.00153-23
34. https://doi.org/10.1093/femsml/uqad020
35. https://doi.org/10.1128/mbio.01492-24
36. https://doi.org/10.1186/s12866-024-03625-6
37. https://doi.org/10.1007/s10482-022-01778-w
38. https://doi.org/10.1038/s41467-023-37087-7
39. https://doi.org/10.1128/aem.00764-23
40. https://doi.org/10.21203/rs.3.rs-3811693/v1
41. https://doi.org/10.1101/2023.01.12.523877
42. https://doi.org/10.1128/jb.00153-23,
43. https://doi.org/10.1093/femsml/uqad020,
44. https://doi.org/10.1128/mbio.01492-24,
45. https://doi.org/10.1007/s10482-022-01778-w,
46. https://doi.org/10.21203/rs.3.rs-3811693/v1,
47. https://doi.org/10.1101/2023.01.12.523877,
48. https://doi.org/10.1186/s12866-024-03625-6,
49. https://doi.org/10.1128/aem.00764-23,