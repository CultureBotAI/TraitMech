# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** human pathogen
- **METPO identifier:** METPO:1004004
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pathogen that infects organisms of the species Homo sapiens.
- **Parent traits:** METPO:1004000
- **Synonyms:** 
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports adaptation of bacterial virulence programs to the human host environment.) | DOI:10.1038/nrmicro1592: secretion systems (Secretion-systems review supports effector delivery as a major mechanism by which bacteria establish human infection.)
- **Existing causal graph summary:** human_pathogen_anthropoid_adaptation: 13 nodes, 12 edges

## Research Objective

Research the microbial trait **human pathogen** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/human_pathogen.yaml`.

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
**Generated:** 2026-08-03T23:35:01.115057

1. barber2024mechanismsofhost pages 1-2
2. barber2024mechanismsofhost pages 3-5
3. barber2024mechanismsofhost pages 5-6
4. barber2024mechanismsofhost pages 8-10
5. moraes2024metabolicreprogrammingof pages 7-9
6. barber2024mechanismsofhost pages 7-8
7. johnson2018bacterialvirulencefactors pages 1-3
8. moraes2024metabolicreprogrammingof pages 2-3
9. moraes2024metabolicreprogrammingof pages 4-5
10. moraes2024metabolicreprogrammingof pages 9-10
11. moraes2024metabolicreprogrammingof pages 1-2
12. chen2025pathogenvirulencegenes pages 1-2
13. zhang2025comparativegenomicsreveals pages 1-2
14. moraes2024metabolicreprogrammingof pages 5-6
15. barber2024mechanismsofhost pages 2-3
16. barber2024mechanismsofhost pages 6-7
17. moraes2024metabolicreprogrammingof pages 6-7
18. s
19. 10.1093/femsre/fuae019
20. 10.1021/acs.jproteome.4c00286
21. 10.1007/978-3-319-67651-7_1
22. 10.3892/ijmm.2025.5614
23. 10.3389/fmicb.2025.1543610
24. https://doi.org/10.1093/femsre/fuae019
25. https://doi.org/10.1021/acs.jproteome.4c00286
26. https://doi.org/10.1007/978-3-319-67651-7_1
27. https://doi.org/10.3892/ijmm.2025.5614
28. https://doi.org/10.3389/fmicb.2025.1543610
29. https://doi.org/10.1093/femsre/fuae019,
30. https://doi.org/10.1021/acs.jproteome.4c00286,
31. https://doi.org/10.1007/978-3-319-67651-7\_1,
32. https://doi.org/10.3892/ijmm.2025.5614,
33. https://doi.org/10.3389/fmicb.2025.1543610,