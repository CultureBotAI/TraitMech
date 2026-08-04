# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** mycelial growth
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000074
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait in which a bacterium grows as branching, filamentous hyphae that form a mycelium, often with subsequent differentiation into aerial hyphae and spores, as in Streptomyces.
- **Parent traits:** METPO:1000059
- **Synonyms:** mycelium-forming, hyphal growth
- **Existing evidence:** DOI:10.1038/nrmicro1968:  (Flärdh & Buttner describe Streptomyces growth as a branching hyphal mycelium with subsequent morphological differentiation.) | DOI:10.1038/nrmicro3178:  (Claessen et al. treat filamentous/mycelial growth as a bacterial solution to multicellularity.)
- **Existing causal graph summary:** mycelial_branching_hyphal_growth: 13 nodes, 9 edges

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
**Generated:** 2026-08-04T09:34:25.989824

1. sen2024adispensablesepiva pages 1-2
2. schlimpert2023thebestof pages 8-10
3. bhowmick2024cellshapeand pages 1-2
4. sen2024adispensablesepiva pages 8-10
5. bhowmick2023osmoticstressresponses pages 1-2
6. bhowmick2024cellshapeand pages 10-12
7. bhowmick2024cellshapeand pages 5-8
8. gallagher2024howcdigmpcontrols pages 1-3
9. kato2023redoxactivecompoundgenerated pages 1-7
10. dinius2023morphologyengineeringfor pages 1-2
11. dinius2024intensificationofbioprocesses pages 14-16
12. kato2023redoxactivecompoundgenerated pages 15-20
13. dinius2024intensificationofbioprocesses pages 26-29
14. 10.1186/s12866-024-03625-6
15. forming
16. 10.1128/mbio.01492-24
17. 10.1093/femsml/uqad020
18. 10.1073/pnas.1207409109
19. ed
20. 10.1016/j.mib.2024.102516
21. 10.1101/2023.01.12.523877
22. 10.1128/jb.00153-23
23. 10.3389/fbioe.2023.1171055
24. 10.1515/psr-2022-0112
25. https://doi.org/10.1186/s12866-024-03625-6
26. https://doi.org/10.1128/mbio.01492-24
27. https://doi.org/10.1093/femsml/uqad020
28. https://doi.org/10.1073/pnas.1207409109
29. https://doi.org/10.1016/j.mib.2024.102516
30. https://doi.org/10.1101/2023.01.12.523877
31. https://doi.org/10.1128/jb.00153-23
32. https://doi.org/10.3389/fbioe.2023.1171055
33. https://doi.org/10.1515/psr-2022-0112
34. https://doi.org/10.1128/jb.00153-23,
35. https://doi.org/10.1093/femsml/uqad020,
36. https://doi.org/10.1186/s12866-024-03625-6,
37. https://doi.org/10.1016/j.mib.2024.102516,
38. https://doi.org/10.1128/mbio.01492-24,
39. https://doi.org/10.1101/2023.01.12.523877,
40. https://doi.org/10.3389/fbioe.2023.1171055,
41. https://doi.org/10.1515/psr-2022-0112,