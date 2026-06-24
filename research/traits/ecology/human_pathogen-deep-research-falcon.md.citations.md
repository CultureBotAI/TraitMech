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
- **Existing causal graph summary:** human_pathogen_anthropoid_adaptation: 5 nodes, 4 edges

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
**Generated:** 2026-06-17T20:44:07.341610

1. soni2024understandingbacterialpathogenicity pages 4-5
2. soni2024understandingbacterialpathogenicity pages 2-4
3. barber2024mechanismsofhost pages 1-2
4. barber2024mechanismsofhost pages 3-5
5. barber2024mechanismsofhost pages 6-7
6. dekker2024withinhostevolutionof pages 2-4
7. wu2024thetypeiii pages 1-2
8. zhou2024typeiiisecretion pages 1-2
9. howden2023staphylococcusaureushost pages 1-5
10. rodriguezlucas2023enterococcalphagesfood pages 1-2
11. lazar2023resistancetolerancevirulence pages 1-2
12. barber2024mechanismsofhost pages 2-3
13. costa2024structuralandfunctional pages 1-5
14. costa2024structuralandfunctional pages 9-11
15. dekker2024withinhostevolutionof pages 1-2
16. https://doi.org/10.1093/femsre/fuae019
17. https://doi.org/10.1128/spectrum.02224-23
18. https://doi.org/10.1038/s42003-024-05852-z
19. https://doi.org/10.1371/journal.ppat.1011280
20. https://doi.org/10.1038/s41579-023-00974-3
21. https://doi.org/10.1146/annurev-pathmechdis-051122-111408
22. https://doi.org/10.1038/s41579-023-00852-y
23. https://doi.org/10.3389/fmicb.2024.1370818
24. https://doi.org/10.3390/pathogens12050746
25. https://doi.org/10.3390/antibiotics12050842
26. https://doi.org/10.3389/fmicb.2024.1370818,
27. https://doi.org/10.1093/femsre/fuae019,
28. https://doi.org/10.1038/s42003-024-05852-z,
29. https://doi.org/10.1146/annurev-pathmechdis-051122-111408,
30. https://doi.org/10.1128/spectrum.02224-23,
31. https://doi.org/10.1371/journal.ppat.1011280,
32. https://doi.org/10.1038/s41579-023-00974-3,
33. https://doi.org/10.1038/s41579-023-00852-y,
34. https://doi.org/10.3390/antibiotics12050842,
35. https://doi.org/10.3390/pathogens12050746,