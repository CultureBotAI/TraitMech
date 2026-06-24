# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** magnetosome
- **METPO identifier:** traitmech:000071
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A membrane-bounded intracellular organelle containing a magnetic iron-mineral crystal (magnetite or greigite); chains of magnetosomes allow magnetotactic bacteria to align with and navigate along geomagnetic field lines.
- **Parent traits:** traitmech:000066
- **Synonyms:** magnetotactic
- **Existing evidence:** DOI:10.1038/nrmicro.2016.99:  (Uebe & Schüler review magnetosome biogenesis as the formation of membrane-bounded magnetic-mineral organelles in magnetotactic bacteria.) | DOI:10.1038/nrmicro842:  (Bazylinski & Frankel, "Magnetosome formation in prokaryotes", describe magnetosomes and the magnetotactic lifestyle they enable.)
- **Existing causal graph summary:** magnetosome_magnetotaxis: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **magnetosome** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/magnetosome.yaml`.

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
**Generated:** 2026-06-18T08:46:07.076151

1. ferrara2024bacterialorganellesin pages 2-4
2. dziuba2023silentgeneclusters pages 1-2
3. ferrara2024bacterialorganellesin pages 4-6
4. awal2023functionalexpressionof pages 1-2
5. martinez2024enhancingmagnetosomebiomanufacturingc pages 29-32
6. sun2024essentialmagnetosomeproteins pages 1-2
7. awal2023experimentalanalysisof pages 7-10
8. chades2024setupofa pages 1-2
9. chades2024setupofa pages 9-11
10. gubieda2024temporalandspatial pages 5-7
11. paulus2024mamflikeproteinsare pages 3-5
12. paulus2024mamflikeproteinsare pages 1-2
13. xie2023linkingmineralsto pages 1-2
14. paulus2024mamflikeproteinsare pages 9-10
15. awal2023experimentalanalysisof pages 1-2
16. martinez2024enhancingmagnetosomebiomanufacturinga pages 29-32
17. awal2023experimentalanalysisof pages 10-12
18. russell2024madformagnetosomes pages 28-30
19. paulus2024mamflikeproteinsare pages 5-6
20. bickley2023thelocalizationof pages 7-10
21. paulus2024mamflikeproteinsare pages 6-8
22. gubieda2024temporalandspatial pages 1-3
23. martinez2024enhancingmagnetosomebiomanufacturing pages 38-41
24. martinez2024enhancingmagnetosomebiomanufacturing pages 29-32
25. gubieda2024temporalandspatial pages 7-9
26. https://doi.org/10.1038/s41467-024-55121-0
27. https://doi.org/10.1111/mmi.15330
28. https://doi.org/10.1038/s41598-024-77591-4
29. https://doi.org/10.1186/s12951-024-02788-8
30. https://doi.org/10.1186/s12934-024-02313-4
31. https://doi.org/10.1128/mbio.03282-22
32. https://doi.org/10.1128/mbio.01649-23
33. https://doi.org/10.1038/s41396-022-01348-y
34. https://doi.org/10.1093/nsr/nwac265
35. https://doi.org/10.1038/s41396-022-01348-y,
36. https://doi.org/10.1111/mmi.15330,
37. https://doi.org/10.1038/s41467-024-55121-0,
38. https://doi.org/10.1128/mbio.01649-23,
39. https://doi.org/10.1128/mbio.03282-22,
40. https://doi.org/10.1093/nsr/nwac265,
41. https://doi.org/10.1038/s41598-024-77591-4,
42. https://doi.org/10.1186/s12951-024-02788-8,
43. https://doi.org/10.1186/s12934-024-02313-4,