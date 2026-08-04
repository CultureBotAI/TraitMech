# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** acidophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003003
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference in which an organism grows optimally at pH values below 5.
- **Parent traits:** METPO:1003000
- **Synonyms:** acidophil, acidophile
- **Existing evidence:** DOI:10.1038/nrmicro2549: growing at pH 1.0-3.0 (Supports acidophilic growth at strongly acidic external pH.)
- **Existing causal graph summary:** acidophilic_ph_homeostasis: 13 nodes, 11 edges

## Research Objective

Research the microbial trait **acidophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/acidophilic.yaml`.

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
**Generated:** 2026-08-04T00:01:02.033139

1. krulwich2011molecularaspectsof pages 3-5
2. chong2024archaeamembranesin pages 3-4
3. chong2024archaeamembranesin pages 1-2
4. chong2024archaeamembranesin pages 2-3
5. vergara2020evolutionofpredicted pages 1-3
6. gonzalezrosales2022integrativegenomicssheds pages 1-2
7. gonzalezrosales2022integrativegenomicssheds pages 4-6
8. riveraaraya2019osmoticimbalancecytoplasm pages 1-2
9. barnum2024predictingmicrobialgrowth pages 9-11
10. vergara2020evolutionofpredicted pages 16-17
11. uncertain; bacterial/archaeal subsets
12. taxon-specific
13. negative modifier
14. 10.3389/frbis.2023.1338019
15. 10.1111/1758-2229.70019
16. 10.1101/2024.03.22.586313
17. 10.3389/fmicb.2021.822229
18. 10.3390/genes11040389
19. 10.3389/fmicb.2019.02455
20. 10.1038/nrmicro2549
21. https://doi.org/10.3389/frbis.2023.1338019
22. https://doi.org/10.1111/1758-2229.70019
23. https://doi.org/10.1101/2024.03.22.586313
24. https://doi.org/10.3389/fmicb.2021.822229
25. https://doi.org/10.3390/genes11040389
26. https://doi.org/10.3389/fmicb.2019.02455
27. https://doi.org/10.1038/nrmicro2549
28. https://doi.org/10.1038/nrmicro2549,
29. https://doi.org/10.3389/fmicb.2021.822229,
30. https://doi.org/10.3389/frbis.2023.1338019,
31. https://doi.org/10.3390/genes11040389,
32. https://doi.org/10.3389/fmicb.2019.02455,
33. https://doi.org/10.1111/1758-2229.70019,
34. https://doi.org/10.1101/2024.03.22.586313,