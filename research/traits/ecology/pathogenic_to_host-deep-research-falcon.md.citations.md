# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pathogenic to host
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1004000
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype where a microbe is a pathogen of some host organism.
- **Parent traits:** METPO:1000059
- **Synonyms:** General.keywords, Safety information.risk assessment
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports the encoding of dedicated virulence factors as the molecular basis of host pathogenicity.) | DOI:10.1038/nrmicro1592: secretion systems (Secretion-systems review supports protein secretion machineries as central effectors of host pathogenicity across kingdoms.)
- **Existing causal graph summary:** pathogenic_to_host_virulence_factor_program: 14 nodes, 12 edges

## Research Objective

Research the microbial trait **pathogenic to host** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/pathogenic_to_host.yaml`.

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
**Generated:** 2026-08-03T23:47:02.173815

1. barber2024mechanismsofhost pages 1-2
2. sangiorgio2024theimpactof pages 7-9
3. wu2024thetypeiii pages 1-2
4. lazar2023resistancetolerancevirulence pages 10-11
5. caballeroflores2023microbiotamediatedcolonizationresistance pages 30-30
6. vonaesch2018pathogensmicrobiomeand pages 14-16
7. fitzgerald2024proteusmirabilisurer pages 1-2
8. fitzgerald2024proteusmirabilisurer pages 2-5
9. wang2024distributionpatternsand pages 1-2
10. zhao2024mortalityandgenetic pages 1-2
11. 10.3390/pathogens12050746
12. 10.1128/mmbr.00034-23
13. 10.1038/s41579-022-00833-7
14. 10.1093/femsre/fuy003
15. 10.3390/pathogens13050409
16. 10.1128/spectrum.02224-23
17. 10.1128/jb.00031-24
18. 10.1093/femsre/fuae019
19. 10.1038/s41541-024-00953-6
20. 10.1186/s12879-024-10274-7
21. 10.2147/IDR.S470401
22. https://doi.org/10.3390/pathogens12050746
23. https://doi.org/10.1128/mmbr.00034-23
24. https://doi.org/10.1038/s41579-022-00833-7
25. https://doi.org/10.1093/femsre/fuy003
26. https://doi.org/10.3390/pathogens13050409
27. https://doi.org/10.1128/spectrum.02224-23
28. https://doi.org/10.1128/jb.00031-24
29. https://doi.org/10.1093/femsre/fuae019
30. https://doi.org/10.1038/s41541-024-00953-6
31. https://doi.org/10.1186/s12879-024-10274-7
32. https://doi.org/10.2147/IDR.S470401
33. https://doi.org/10.1093/femsre/fuae019,
34. https://doi.org/10.3390/pathogens13050409,
35. https://doi.org/10.3390/pathogens12050746,
36. https://doi.org/10.1128/spectrum.02224-23,
37. https://doi.org/10.1128/jb.00031-24,
38. https://doi.org/10.1038/s41579-022-00833-7,
39. https://doi.org/10.1093/femsre/fuy003,
40. https://doi.org/10.2147/idr.s470401,
41. https://doi.org/10.1038/s41541-024-00953-6,
42. https://doi.org/10.1186/s12879-024-10274-7,