# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH delta
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000232
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH phenotype with numerical limits expressing the breadth (maximum minus minimum) of external pH supporting growth of an organism.
- **Parent traits:** METPO:1000531, METPO:1000534
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports the breadth of the pH-tolerance span as a derived descriptor reflecting overall pH-homeostasis flexibility.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports the proton motive force as the energetic constraint underlying broad versus narrow pH tolerance.)
- **Existing causal graph summary:** ph_delta_homeostasis_flexibility: 12 nodes, 9 edges

## Research Objective

Research the microbial trait **pH delta** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta.yaml`.

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
**Generated:** 2026-08-04T02:24:05.231762

1. ramoneda2023buildingagenomebased pages 1-1
2. krulwich2011molecularaspectsof pages 1-3
3. krulwich2011molecularaspectsof pages 5-6
4. rebelo2023unravelingtherole pages 18-20
5. dubinkina2024atranscriptomicatlas pages 1-2
6. krulwich2011molecularaspectsof pages 11-12
7. krulwich2011molecularaspectsof pages 27-28
8. maksimova2024metabolicandmorphological pages 1-2
9. krulwich2011molecularaspectsof pages 12-14
10. krulwich2011molecularaspectsof pages 15-17
11. krulwich2011molecularaspectsof pages 20-22
12. krulwich2011molecularaspectsof pages 22-23
13. \mathrm{pH\ delta}=\mathrm{maximum\ growth\ pH}-\mathrm{minimum\ growth\ pH}.
\
14. 10.1038/nrmicro2549
15. s
16. 10.3390/antibiotics12091474
17. 10.1155/2024/3087296
18. 10.1128/spectrum.02536-23
19. 10.1126/sciadv.adf8998
20. 10.1016/j.tim.2007.02.005
21. https://doi.org/10.1038/nrmicro2549
22. https://doi.org/10.3390/antibiotics12091474
23. https://doi.org/10.1155/2024/3087296
24. https://doi.org/10.1128/spectrum.02536-23
25. https://doi.org/10.1126/sciadv.adf8998
26. https://doi.org/10.1016/j.tim.2007.02.005
27. https://doi.org/10.1126/sciadv.adf8998,
28. https://doi.org/10.1038/nrmicro2549,
29. https://doi.org/10.3390/antibiotics12091474,
30. https://doi.org/10.1155/2024/3087296,
31. https://doi.org/10.1128/spectrum.02536-23,