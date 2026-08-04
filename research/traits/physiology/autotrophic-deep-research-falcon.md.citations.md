# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** autotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000632
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism produces organic compounds from inorganic carbon sources (primarily carbon dioxide or bicarbonate) using energy from light (photoautotrophy) or from the oxidation of inorganic compounds (chemoautotrophy).
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_autotroph, autotroph, autotrophy
- **Existing evidence:** DOI:10.1038/nrmicro.2016.130: require only CO2 as a carbon source (Review defines autotrophic organisms by CO2 use as carbon source for growth.) | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Minireview supports Calvin-Benson and other microbial CO2-fixation pathways.) | PMID:8590279: Synechocystis sp. strain PCC6803 (Organism example: Synechocystis sp. PCC 6803 is a model autotrophic cyanobacterium that fixes CO2 via the Calvin-Benson cycle (Kaneko et al. 1996, DNA Res, full genome).)
- **Existing causal graph summary:** autotrophic_inorganic_carbon_fixation: 18 nodes, 17 edges

## Research Objective

Research the microbial trait **autotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/autotrophic.yaml`.

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
**Generated:** 2026-08-04T10:45:07.811982

1. claassens2016harnessingthepower pages 1-2
2. braun2021reviewsandsyntheses pages 1-2
3. atencio2024metabolicadaptationsunderpin pages 1-2
4. kurkela2024inorganiccarbonsensing pages 1-2
5. huffine2023roleofcarboxysomes pages 1-2
6. li2024productionofsuccinate pages 1-2
7. gupta2020extracellularelectronuptake pages 1-2
8. kim2024recentadvancesin pages 1-2
9. li2024processstudyon pages 1-2
10. berg2010autotrophiccarbonfixation pages 9-10
11. berg2010autotrophiccarbonfixation pages 10-11
12. s
13. 10.1126/sciadv.adk7283
14. 10.1111/ppl.14140
15. 10.1038/s41598-024-68868-9
16. 10.1093/femsec/fiae105
17. 10.1186/s12934-024-02470-6
18. 10.3389/fclim.2024.1412232
19. 10.1111/1462-2920.16283
20. 10.5194/bg-18-3689-2021
21. 10.1007/s10295-020-02309-0
22. 10.1038/nrmicro.2016.130
23. 10.1038/nrmicro2365
24. https://doi.org/10.1126/sciadv.adk7283
25. https://doi.org/10.1111/ppl.14140
26. https://doi.org/10.1038/s41598-024-68868-9
27. https://doi.org/10.1093/femsec/fiae105
28. https://doi.org/10.1186/s12934-024-02470-6
29. https://doi.org/10.3389/fclim.2024.1412232
30. https://doi.org/10.1111/1462-2920.16283
31. https://doi.org/10.5194/bg-18-3689-2021
32. https://doi.org/10.1007/s10295-020-02309-0
33. https://doi.org/10.1038/nrmicro.2016.130
34. https://doi.org/10.1038/nrmicro2365
35. https://doi.org/10.1038/nrmicro.2016.130,
36. https://doi.org/10.5194/bg-18-3689-2021,
37. https://doi.org/10.1038/s41598-024-68868-9,
38. https://doi.org/10.1126/sciadv.adk7283,
39. https://doi.org/10.5376/be.2024.14.0016,
40. https://doi.org/10.1186/s12934-024-02470-6,
41. https://doi.org/10.1111/ppl.14140,
42. https://doi.org/10.1111/1462-2920.16283,
43. https://doi.org/10.1093/femsec/fiae105,
44. https://doi.org/10.1007/s10295-020-02309-0,
45. https://doi.org/10.3389/fclim.2024.1412232,
46. https://doi.org/10.1038/nrmicro2365,