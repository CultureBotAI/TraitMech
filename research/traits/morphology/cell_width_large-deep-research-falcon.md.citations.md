# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell width large
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000890
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-width phenotype in which the shorter cell dimension exceeds approximately 0.9 micrometers.
- **Parent traits:** METPO:1000882
- **Synonyms:** W_>0.9
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan synthesis (Supports MreB/Rod-complex activity as the control point governing wide rod radii.) | DOI:10.1126/science.aaa1313: cell size scales with growth rate (Growth-rate-dependent size law supports widening of cells at fast growth rates or under nutrient-rich conditions.)
- **Existing causal graph summary:** cell_width_large_setpoint_increase: 15 nodes, 10 edges

## Research Objective

Research the microbial trait **cell width large** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_width_large.yaml`.

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
**Generated:** 2026-08-04T07:53:37.932493

1. ojima2024buddingandexplosive pages 1-2
2. ouzounov2016mreborientationcorrelates pages 1-2
3. tesson2022magnesiumrescuesthe pages 1-2
4. fivenson2023arolefor pages 1-2
5. gilman2024mrecmredstructurereveals pages 1-2
6. middlemiss2024molecularmotortugofwar pages 1-2
7. buss2019pathwaydirectedscreenfor pages 1-2
8. juillot2021ahighcontentmicroscopy pages 5-8
9. shi2017deepphenotypicmapping pages 1-3
10. dion2018celldiameterin pages 18-19
11. juillot2021ahighcontentmicroscopy pages 2-4
12. ago2023relationshipbetweenthe pages 1-3
13. dion2018celldiameterin pages 3-6
14. dion2018celldiameterin pages 8-10
15. dion2018celldiameterin pages 1-3
16. dion2018celldiameterin pages 10-12
17. juillot2021ahighcontentmicroscopy pages 10-11
18. juillot2021ahighcontentmicroscopy pages 8-10
19. juillot2021ahighcontentmicroscopy pages 4-5
20. https://doi.org/10.1038/s41467-024-49785-x
21. https://doi.org/10.3389/fmicb.2024.1400434
22. https://doi.org/10.1101/2024.10.08.617240
23. https://doi.org/10.1002/mbo3.1385
24. https://doi.org/10.1073/pnas.2301987120
25. https://doi.org/10.1038/s41598-021-04294-5
26. https://doi.org/10.1128/msystems.01017-21
27. https://doi.org/10.1038/s41564-019-0439-0.
28. https://doi.org/10.1101/392837
29. https://doi.org/10.1128/AAC.01530-18
30. https://doi.org/10.1016/j.cub.2017.09.065
31. https://doi.org/10.1016/j.bpj.2016.07.017
32. https://doi.org/10.1101/392837,
33. https://doi.org/10.1016/j.bpj.2016.07.017,
34. https://doi.org/10.1016/j.cub.2017.09.065,
35. https://doi.org/10.1128/aac.01530-18,
36. https://doi.org/10.3389/fmicb.2024.1400434,
37. https://doi.org/10.1038/s41598-021-04294-5,
38. https://doi.org/10.1073/pnas.2301987120,
39. https://doi.org/10.1101/2024.10.08.617240,
40. https://doi.org/10.1038/s41467-024-49785-x,
41. https://doi.org/10.1128/msystems.01017-21,
42. https://doi.org/10.1002/mbo3.1385,