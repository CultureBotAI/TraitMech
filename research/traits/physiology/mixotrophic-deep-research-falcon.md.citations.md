# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** mixotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000652
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism can use both organic and inorganic carbon sources for growth.
- **Parent traits:** METPO:1000631
- **Synonyms:** mixotroph
- **Existing evidence:** DOI:10.1128/AEM.01559-06: Evidence for the ubiquity of mixotrophic bacteria (Review supports bacterial mixotrophy as combined metabolic modes in marine systems.) | DOI:10.1073/pnas.1305998110: combination of modes by which an organism can obtain its energy and carbon (Perspective supports mixotrophy as combined energy and carbon acquisition modes.)
- **Existing causal graph summary:** mixotrophic_dual_carbon_energy_use: 14 nodes, 13 edges

## Research Objective

Research the microbial trait **mixotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/mixotrophic.yaml`.

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
**Generated:** 2026-08-04T11:33:49.982765

1. braun2021reviewsandsyntheses pages 1-2
2. li2024arcobacteraceaeareubiquitous pages 10-12
3. srivastava2023interplaybetweenautotrophic pages 1-2
4. munozmarin2020mixotrophyinmarine pages 5-7
5. li2024arcobacteraceaeareubiquitous pages 1-2
6. taubert2022bolsteringfitnessvia pages 1-2
7. taubert2022bolsteringfitnessvia pages 5-6
8. parada2023constrainingthecomposition pages 1-6
9. parada2023constrainingthecomposition pages 17-19
10. li2024arcobacteraceaeareubiquitous pages 7-10
11. taubert2022bolsteringfitnessvia pages 6-7
12. taubert2022bolsteringfitnessvia pages 7-8
13. munozmarin2020mixotrophyinmarine pages 1-2
14. braun2021reviewsandsyntheses pages 4-5
15. es
16. 10.1128/msystems.00513-24
17. 10.1111/1462-2920.16299
18. 10.1186/s40168-023-01688-7
19. 10.1038/s41396-021-01163-x
20. 10.5194/bg-18-3689-2021
21. 10.1038/s41396-020-0603-9
22. 10.1093/femsle/fny039
23. 10.1073/pnas.1305998110
24. https://doi.org/10.1128/msystems.00513-24
25. https://doi.org/10.1111/1462-2920.16299
26. https://doi.org/10.1186/s40168-023-01688-7
27. https://doi.org/10.1038/s41396-021-01163-x
28. https://doi.org/10.5194/bg-18-3689-2021
29. https://doi.org/10.1038/s41396-020-0603-9
30. https://doi.org/10.1093/femsle/fny039
31. https://doi.org/10.1073/pnas.1305998110
32. https://doi.org/10.1128/msystems.00513-24,
33. https://doi.org/10.1038/s41396-020-0603-9,
34. https://doi.org/10.1038/s41396-021-01163-x,
35. https://doi.org/10.5194/bg-18-3689-2021,
36. https://doi.org/10.1111/1462-2920.16299,
37. https://doi.org/10.1186/s40168-023-01688-7,
38. https://doi.org/10.1093/femsle/fny039,