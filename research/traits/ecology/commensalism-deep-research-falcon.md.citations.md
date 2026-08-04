# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** commensalism
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000042
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A symbiosis in which the microorganism benefits from the association (e.g. resources, shelter, transport) while the host's fitness remains essentially unaffected.
- **Parent traits:** traitmech:000040
- **Synonyms:** commensal
- **Existing evidence:** DOI:10.1038/s41579-021-00550-7:  (Drew et al. place commensalism on the parasite-mutualist continuum as a near-neutral host interaction.) | DOI:10.1073/pnas.1218525110:  (McFall-Ngai et al. support commensal colonization as a major class of host-associated microbial lifestyles.)
- **Existing causal graph summary:** commensalism_neutral_host: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **commensalism** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/commensalism.yaml`.

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
**Generated:** 2026-08-04T14:55:16.876254

1. drew2021microbialevolutionand pages 1-2
2. muramatsu2024nutrientacquisitionstrategies pages 2-4
3. chen2024themicrobiotaa pages 3-5
4. doranga2024nutritionofescherichia pages 2-4
5. muramatsu2024nutrientacquisitionstrategies pages 6-7
6. froismartins2024candidaalbicansvirulence pages 2-4
7. furuichi2024commensalconsortiadecolonize pages 1-2
8. torres2024sheddinglighton pages 9-10
9. froismartins2024candidaalbicansvirulence pages 1-2
10. furuichi2024commensalconsortiadecolonize pages 3-4
11. doranga2024nutritionofescherichia pages 6-8
12. mcfallngai2013animalsina pages 3-4
13. torres2024sheddinglighton pages 3-5
14. wilde2024hostcontrolof pages 15-17
15. wilde2024hostcontrolof pages 21-24
16. drew2021microbialevolutionand pages 3-4
17. 10.1128/ecosalplus.esp-0006-2023
18. 10.1016/j.chom.2024.05.011
19. 10.1126/science.adi3338
20. 10.1007/s40588-024-00235-8
21. 10.1038/s41586-024-07960-6
22. 10.1128/mbio.00390-24
23. 10.3389/fmicb.2024.1417864
24. 10.1038/s41579-021-00550-7
25. 10.1073/pnas.1218525110
26. https://doi.org/10.1128/ecosalplus.esp-0006-2023
27. https://doi.org/10.1016/j.chom.2024.05.011
28. https://doi.org/10.1126/science.adi3338
29. https://doi.org/10.1007/s40588-024-00235-8
30. https://doi.org/10.1038/s41586-024-07960-6
31. https://doi.org/10.1128/mbio.00390-24
32. https://doi.org/10.3389/fmicb.2024.1417864
33. https://doi.org/10.1038/s41579-021-00550-7
34. https://doi.org/10.1073/pnas.1218525110
35. https://doi.org/10.1038/s41579-021-00550-7,
36. https://doi.org/10.1007/s40588-024-00235-8,
37. https://doi.org/10.1016/j.chom.2024.05.011,
38. https://doi.org/10.3389/fmicb.2024.1417864,
39. https://doi.org/10.1128/ecosalplus.esp-0006-2023,
40. https://doi.org/10.1126/science.adi3338,
41. https://doi.org/10.1038/s41586-024-07960-6,
42. https://doi.org/10.1128/mbio.00390-24,
43. https://doi.org/10.1073/pnas.1218525110,