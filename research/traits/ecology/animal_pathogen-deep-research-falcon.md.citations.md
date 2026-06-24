# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** animal pathogen
- **METPO identifier:** METPO:1004002
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pathogen that infects organisms in the kingdom Metazoa.
- **Parent traits:** METPO:1004000
- **Synonyms:** 
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports adaptation of bacterial virulence programs to animal hosts.) | DOI:10.1038/nrmicro1592: secretion systems (Secretion-systems review supports T3SS/T6SS effector delivery as a major mechanism by which bacteria infect animal hosts.)
- **Existing causal graph summary:** animal_pathogen_metazoan_adaptation: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **animal pathogen** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/animal_pathogen.yaml`.

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
**Generated:** 2026-06-17T15:51:24.814027

1. barber2024mechanismsofhost pages 8-10
2. barber2024mechanismsofhost pages 3-5
3. lucidi2024pathogenicityandvirulence pages 7-8
4. wimmi2024cytosolicsortingplatform pages 1-2
5. wu2024thetypeiii pages 1-2
6. song2024molecularmechanismof pages 1-2
7. golden2024metalchelationas pages 2-3
8. diamant2024thetranscriptionalregulation pages 8-10
9. costa2024structuralandfunctional pages 1-5
10. diamant2024thetranscriptionalregulation pages 1-2
11. costa2024structuralandfunctional pages 11-13
12. wang2024distributionpatternsand pages 1-2
13. barber2024mechanismsofhost pages 1-2
14. soni2024understandingbacterialpathogenicity pages 2-4
15. alhadlaq2024overviewofpathogenic pages 1-3
16. alhadlaq2024overviewofpathogenic pages 8-10
17. https://doi.org/10.1093/femsre/fuae019
18. https://doi.org/10.1128/spectrum.02224-23
19. https://doi.org/10.1038/s41564-023-01545-1
20. https://doi.org/10.1038/s41579-023-00974-3
21. https://doi.org/10.1038/s42003-024-05995-z
22. https://doi.org/10.1080/19490976.2024.2369339
23. https://doi.org/10.1039/d4cb00175c
24. https://doi.org/10.1080/21505594.2023.2289769
25. https://doi.org/10.1186/s13099-024-00641-9;
26. https://doi.org/10.2147/idr.s470401
27. https://doi.org/10.1186/s13099-024-00641-9
28. https://doi.org/10.1093/femsre/fuae019,
29. https://doi.org/10.3389/fmicb.2024.1370818,
30. https://doi.org/10.1128/spectrum.02224-23,
31. https://doi.org/10.1038/s41564-023-01545-1,
32. https://doi.org/10.1038/s41579-023-00974-3,
33. https://doi.org/10.1080/21505594.2023.2289769,
34. https://doi.org/10.1039/d4cb00175c,
35. https://doi.org/10.1080/19490976.2024.2369339,
36. https://doi.org/10.1038/s42003-024-05995-z,
37. https://doi.org/10.1186/s13099-024-00641-9,
38. https://doi.org/10.2147/idr.s470401,