# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** psychrotolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000618
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference in which growth can occur at low temperatures without an obligate low-temperature preference.
- **Parent traits:** METPO:1000613
- **Synonyms:** 
- **Existing evidence:** DOI:10.1099/ijs.0.65141-0: Pseudomonas guineae sp. nov., a novel psychrotolerant bacterium (Organism example: Pseudomonas guineae is described as psychrotolerant.) | DOI:10.1038/sj.embor.7400662: decreased membrane fluidity (Psychrophile review supports cold-end membrane stress as the challenge that psychrotolerant facultative adaptation overcomes without full psychrophile dedication.)
- **Existing causal graph summary:** psychrotolerant_facultative_cold_adaptation: 12 nodes, 9 edges

## Research Objective

Research the microbial trait **psychrotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/psychrotolerant.yaml`.

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
**Generated:** 2026-08-04T03:25:44.541120

1. ramon2023ageneraloverview pages 1-2
2. moyer2017psychrophilesandpsychrotrophs pages 2-3
3. ramon2023ageneraloverview pages 2-4
4. purwar2024adaptationsofpsychrophilic pages 10-11
5. cybulski2002mechanismofmembrane pages 1-2
6. muchaamba2021listeriamonocytogenescold pages 4-5
7. pavankumar2021molecularinsightsinto pages 7-10
8. cybulski2002mechanismofmembrane pages 4-6
9. hassan2020temperaturedrivenmembrane pages 2-3
10. hassan2020temperaturedrivenmembrane pages 6-7
11. bao2023miningofkey pages 9-11
12. bao2023miningofkey pages 6-7
13. bao2023miningofkey pages 1-2
14. purwar2024adaptationsofpsychrophilic pages 3-4
15. ramon2023ageneraloverview pages 8-9
16. moyer2017psychrophilesandpsychrotrophs pages 3-5
17. 10.1007/s42770-023-01057-4
18. 10.3389/fmicb.2023.1215837
19. 10.37256/amtt.5220244537
20. 10.3390/microorganisms9051061
21. 10.1111/1462-2920.15304
22. 10.3389/fmicb.2020.00824
23. 10.1046/j.1365-2958.2002.03103.x
24. 10.1016/B978-0-12-809633-8.02282-2
25. 10.1038/sj.embor.7400662
26. 10.1099/ijs.0.65141-0
27. https://doi.org/10.1007/s42770-023-01057-4
28. https://doi.org/10.3389/fmicb.2023.1215837
29. https://doi.org/10.37256/amtt.5220244537
30. https://doi.org/10.3390/microorganisms9051061
31. https://doi.org/10.1111/1462-2920.15304
32. https://doi.org/10.3389/fmicb.2020.00824
33. https://doi.org/10.1046/j.1365-2958.2002.03103.x
34. https://doi.org/10.1016/B978-0-12-809633-8.02282-2
35. https://doi.org/10.1038/sj.embor.7400662
36. https://doi.org/10.1099/ijs.0.65141-0
37. https://doi.org/10.1007/s42770-023-01057-4,
38. https://doi.org/10.1016/b978-0-12-809633-8.02282-2,
39. https://doi.org/10.37256/amtt.5220244537,
40. https://doi.org/10.1046/j.1365-2958.2002.03103.x,
41. https://doi.org/10.3389/fmicb.2020.00824,
42. https://doi.org/10.3390/microorganisms9051061,
43. https://doi.org/10.3389/fmicb.2023.1215837,
44. https://doi.org/10.1111/1462-2920.15304,