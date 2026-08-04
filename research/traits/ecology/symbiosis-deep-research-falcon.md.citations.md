# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** symbiosis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000040
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An ecological lifestyle in which a microorganism lives in persistent physical association with a host or partner organism. It encompasses mutualism, commensalism, and parasitism, which form an evolutionary continuum.
- **Parent traits:** METPO:1000059
- **Synonyms:** symbiotic
- **Existing evidence:** DOI:10.1073/pnas.1218525110:  (McFall-Ngai et al., "Animals in a bacterial world", supports persistent host-microbe association (symbiosis) as a pervasive microbial lifestyle; parent of the mutualism/commensalism/parasitism sub-variants.) | DOI:10.1038/s41579-021-00550-7:  (Drew et al. frame symbioses as a parasite-mutualist continuum, supporting symbiosis as the umbrella lifestyle for these interaction modes.)
- **Existing causal graph summary:** symbiosis_host_interaction: 13 nodes, 11 edges

## Research Objective

Research the microbial trait **symbiosis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/symbiosis.yaml`.

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
**Generated:** 2026-08-03T23:57:55.701900

1. meng2024identificationofthe pages 1-2
2. lepetit2023controlofthe pages 1-2
3. duncan2023cooptionofa pages 7-8
4. wiesmann2023originsofsymbiosis pages 1-2
5. wiesmann2023originsofsymbiosis pages 6-8
6. gutierrezgarcia2024aconservedbacterial pages 6-7
7. gutierrezgarcia2024aconservedbacterial pages 9-13
8. gutierrezgarcia2024aconservedbacterial pages 3-4
9. tao2024nitrogenandnod pages 1-2
10. tao2024nitrogenandnod pages 9-11
11. grzyb2024decipheringmolecularmechanisms pages 20-21
12. gutierrezgarcia2024aconservedbacterial pages 1-3
13. gutierrezgarcia2024aconservedbacterial pages 7-9
14. 10.1093/femsre/fuac048
15. 10.1126/science.adp7748
16. 10.1186/s40168-024-01813-0
17. 10.1038/s41467-024-47752-0
18. 10.3389/fpls.2023.1114840
19. 10.1073/pnas.2308448120
20. 10.3390/ijms252413601
21. https://doi.org/10.1093/femsre/fuac048
22. https://doi.org/10.1126/science.adp7748
23. https://doi.org/10.1186/s40168-024-01813-0
24. https://doi.org/10.1038/s41467-024-47752-0
25. https://doi.org/10.3389/fpls.2023.1114840
26. https://doi.org/10.1073/pnas.2308448120
27. https://doi.org/10.3390/ijms252413601
28. https://doi.org/10.1093/femsre/fuac048,
29. https://doi.org/10.1126/science.adp7748,
30. https://doi.org/10.1186/s40168-024-01813-0,
31. https://doi.org/10.1073/pnas.2308448120,
32. https://doi.org/10.1038/s41467-024-47752-0,
33. https://doi.org/10.3389/fpls.2023.1114840,
34. https://doi.org/10.3390/ijms252413601,