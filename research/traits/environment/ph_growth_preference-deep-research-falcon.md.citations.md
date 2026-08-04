# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH growth preference
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003000
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that describes how the rate and extent of population growth are affected by environmental pH.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2549: external pH values that are outside the cytoplasmic pH range (Supports environmental pH as a growth-relevant condition requiring pH homeostasis.)
- **Existing causal graph summary:** ph_growth_preference_homeostasis: 12 nodes, 12 edges

## Research Objective

Research the microbial trait **pH growth preference** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_growth_preference.yaml`.

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
**Generated:** 2026-08-04T02:42:21.027427

1. ramoneda2023buildingagenomebased pages 1-2
2. krulwich2011molecularaspectsof pages 1-3
3. poolman2023physicochemicalhomeostasisin pages 1-2
4. krulwich2011molecularaspectsof pages 12-14
5. ramoneda2023buildingagenomebased pages 3-5
6. krulwich2011molecularaspectsof pages 11-12
7. chong2024archaeamembranesin pages 1-2
8. goto2022differencesinbioenergetic pages 1-2
9. krulwich2011molecularaspectsof pages 3-5
10. krulwich2011molecularaspectsof pages 5-6
11. tran2024activephregulation pages 5-7
12. coker2019recentadvancesin pages 1-2
13. tran2024activephregulation pages 2-5
14. tran2024activephregulation pages 7-9
15. tran2024activephregulation pages 1-2
16. 10.1126/sciadv.adf8998
17. 10.1093/femsre/fuad033
18. 10.1128/mbio.03387-23
19. 10.3389/frbis.2023.1338019
20. 10.3389/fmicb.2022.842785
21. 10.1038/nrmicro2549
22. 10.12688/f1000research.20765.1
23. https://doi.org/10.1126/sciadv.adf8998
24. https://doi.org/10.1093/femsre/fuad033
25. https://doi.org/10.1128/mbio.03387-23
26. https://doi.org/10.3389/frbis.2023.1338019
27. https://doi.org/10.3389/fmicb.2022.842785
28. https://doi.org/10.1038/nrmicro2549
29. https://doi.org/10.12688/f1000research.20765.1
30. https://doi.org/10.1126/sciadv.adf8998,
31. https://doi.org/10.1038/nrmicro2549,
32. https://doi.org/10.1093/femsre/fuad033,
33. https://doi.org/10.1128/mbio.03387-23,
34. https://doi.org/10.3389/frbis.2023.1338019,
35. https://doi.org/10.3389/fmicb.2022.842785,
36. https://doi.org/10.12688/f1000research.20765.1,