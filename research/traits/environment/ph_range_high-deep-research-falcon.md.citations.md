# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH range high
- **METPO identifier:** METPO:1000464
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which the growth-supporting external pH range spans approximately 10–14, characteristic of extreme-alkaliphile physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Alkali Tolerant, Alkaliphile, Extreme Alkaliphile, 10_to_14
- **Existing evidence:** DOI:10.1038/nrmicro2549: alkaliphiles (pH-homeostasis review supports extreme-alkaliphile physiology growing at external pH above 10.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports robust Na+/H+ antiporter activity as the extreme-alkaliphile mechanism sustaining the proton motive force above pH 10.)
- **Existing causal graph summary:** ph_range_high_extreme_alkaliphile: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH range high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range_high.yaml`.

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
**Generated:** 2026-06-18T00:56:06.665152

1. krulwich2011molecularaspectsof pages 12-14
2. wang2023characterizationoftwo pages 7-8
3. xing2024thepolyextremophilenatranaerobius pages 1-2
4. colman2024themicrobialecology pages 14-18
5. krulwich2011molecularaspectsof pages 6-8
6. scott2024widespreaddissolvedinorganic pages 7-10
7. colman2024themicrobialecology pages 18-21
8. krulwich2011molecularaspectsof pages 27-28
9. colman2024themicrobialecology pages 21-24
10. krulwich2011molecularaspectsof pages 5-6
11. and
12. https://doi.org/10.1038/nrmicro2549
13. https://doi.org/10.1074/jbc.M116.751016
14. https://doi.org/10.3390/ijms241310786
15. https://doi.org/10.1128/AEM.00145-24
16. https://doi.org/10.1128/AEM.01557-23
17. https://doi.org/10.1101/2024.11.10.622848
18. https://doi.org/10.1128/aem.00145-24
19. https://doi.org/10.1128/aem.01557-23
20. https://doi.org/10.1038/nrmicro2549,
21. https://doi.org/10.3390/ijms241310786,
22. https://doi.org/10.1128/aem.01557-23,
23. https://doi.org/10.1101/2024.11.10.622848,
24. https://doi.org/10.1128/aem.00145-24,
25. https://doi.org/10.1074/jbc.m116.751016,