# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** parasitism
- **METPO identifier:** traitmech:000043
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A symbiosis in which the microorganism benefits at the expense of its host's fitness, deriving resources from the host while causing it harm.
- **Parent traits:** traitmech:000040
- **Synonyms:** parasitic
- **Existing evidence:** DOI:10.1038/s41579-021-00550-7:  (Drew et al. define parasitism as the harmful pole of the parasite-mutualist continuum and describe evolutionary transitions along it.) | DOI:10.1073/pnas.1218525110:  (McFall-Ngai et al. support host-exploitative associations as one outcome of the shared host-colonization toolkit.)
- **Existing causal graph summary:** parasitism_host_fitness_cost: 12 nodes, 11 edges

## Research Objective

Research the microbial trait **parasitism** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/parasitism.yaml`.

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
**Generated:** 2026-08-03T23:42:17.342793

1. drew2021microbialevolutionand pages 11-12
2. mandel2024metabolismandphysiology pages 1-2
3. wenbo2024hijackinghostcell pages 1-2
4. wenbo2024hijackinghostcell pages 3-4
5. wenbo2024hijackinghostcell pages 6-8
6. wenbo2024hijackinghostcell pages 9-11
7. mandel2024metabolismandphysiology pages 5-6
8. mandel2024metabolismandphysiology pages 2-4
9. mandel2024metabolismandphysiology pages 8-9
10. mandel2024metabolismandphysiology pages 14-15
11. mandel2024metabolismandphysiology pages 9-10
12. barber2024mechanismsofhost pages 3-5
13. barber2024mechanismsofhost pages 10-11
14. ewald2024theintersectionof pages 19-21
15. ewald2024theintersectionof pages 2-4
16. barber2024mechanismsofhost pages 5-6
17. barber2024mechanismsofhost pages 6-7
18. ewald2024theintersectionof pages 7-9
19. barber2024mechanismsofhost pages 2-3
20. label-only
21. CHEBI:15422
22. CHEBI:16761
23. CHEBI:15351
24. GO:0006096
25. CHEBI:18050
26. is
27. 10.3389/fcimb.2024.1284701
28. 10.1128/mmbr.00164-22
29. 10.1080/21505594.2024.2351234
30. 10.1093/femsre/fuae019
31. 10.1038/s41579-021-00550-7
32. https://doi.org/10.3389/fcimb.2024.1284701
33. https://doi.org/10.1128/mmbr.00164-22
34. https://doi.org/10.1080/21505594.2024.2351234
35. https://doi.org/10.1093/femsre/fuae019
36. https://doi.org/10.1038/s41579-021-00550-7
37. https://doi.org/10.1038/s41579-021-00550-7,
38. https://doi.org/10.3389/fcimb.2024.1284701,
39. https://doi.org/10.1080/21505594.2024.2351234,
40. https://doi.org/10.1093/femsre/fuae019,
41. https://doi.org/10.1128/mmbr.00164-22,