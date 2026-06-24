# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** fusiform shaped
- **METPO identifier:** METPO:1000690
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape that is wide in the middle and tapers at both ends.
- **Parent traits:** METPO:1000666
- **Synonyms:** fusiform
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports tapered cell ends as a genetically determined geometry maintained by graded wall synthesis.) | DOI:10.1111/1462-2920.13731: Fusobacterium nucleatum (Fusobacterium-genome review supports fusiform morphology in the Fusobacterium genus.)
- **Existing causal graph summary:** fusiform_shaped_tapered_polar_growth: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **fusiform shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/fusiform_shaped.yaml`.

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
**Generated:** 2026-06-18T08:13:31.669827

1. egan2020regulationofpeptidoglycan pages 8-9
2. lim2025characterizationofclinical pages 9-12
3. lartigue2022cytoskeletalcomponentscan pages 7-8
4. krieger2024reexaminingtherole pages 1-2
5. zhang2024outermembranevesicles pages 1-2
6. fan2023fusobacteriumnucleatumand pages 1-2
7. connolly2025thephysicalbiogeography pages 3-5
8. ducret2021recentprogressin pages 6-6
9. lim2025characterizationofclinical pages 1-6
10. connolly2025thephysicalbiogeography pages 1-3
11. nyongesa2022evolutionofmulticellular pages 10-12
12. wang2025mrebunravelingthe pages 11-12
13. lim2025characterizationofclinical pages 18-22
14. muchova2022fusobacteriumnucleatumsubspecies pages 2-3
15. wang2025mrebunravelingthe pages 21-21
16. egan2020regulationofpeptidoglycan pages 4-5
17. egan2020regulationofpeptidoglycan pages 7-8
18. lim2025characterizationofclinical pages 12-18
19. groeger2022pathogenicmechanismsof pages 1-2
20. lim2025characterizationofclinical pages 6-9
21. https://doi.org/10.1038/s41579-020-0366-3
22. https://doi.org/10.1186/s12964-025-02373-y
23. https://doi.org/10.1016/j.mib.2021.01.011
24. https://doi.org/10.1007/978-3-030-18768-2_5
25. https://doi.org/10.1038/s41467-022-34478-0
26. https://doi.org/10.1080/19490976.2024.2415490
27. https://doi.org/10.1002/advs.202400882
28. https://doi.org/10.1101/2025.01.08.631950
29. https://doi.org/10.1080/20002297.2022.2145729
30. https://doi.org/10.3389/froh.2022.831607
31. https://doi.org/10.1128/mbio.02989-24
32. https://doi.org/10.1002/advs.202400882,
33. https://doi.org/10.1080/19490976.2024.2415490,
34. https://doi.org/10.1038/s41467-022-34478-0,
35. https://doi.org/10.1038/s41579-020-0366-3,
36. https://doi.org/10.1101/2025.01.08.631950,
37. https://doi.org/10.1007/978-3-030-18768-2\_5,
38. https://doi.org/10.1080/20002297.2022.2145729,
39. https://doi.org/10.3389/froh.2022.831607,
40. https://doi.org/10.1128/mbio.02989-24,
41. https://doi.org/10.1016/j.mib.2021.01.011,
42. https://doi.org/10.1186/s12964-025-02373-y,
43. https://doi.org/10.21203/rs.3.rs-1200288/v1,
44. https://doi.org/10.3389/froh.2022.853618,