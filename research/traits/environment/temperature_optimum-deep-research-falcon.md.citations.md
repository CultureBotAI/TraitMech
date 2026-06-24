# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature optimum
- **METPO identifier:** METPO:1000304
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature phenotype with numerical limits that represents the ambient-temperature conditions at which an organism exhibits the most efficient growth and reproduction.
- **Parent traits:** METPO:1000533, METPO:1000536
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports the ambient temperature at which membrane and enzyme function are best maintained as the operational definition of temperature optimum.) | DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports homoviscous membrane composition as a key mechanism setting the temperature optimum.)
- **Existing causal graph summary:** temperature_optimum_balanced_adaptation: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **temperature optimum** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum.yaml`.

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
**Generated:** 2026-06-18T02:08:21.464204

1. ramon2023ageneraloverview pages 1-2
2. moon2023temperaturemattersbacterial pages 1-3
3. purwar2024adaptationsofpsychrophilic pages 8-10
4. ramoneda2024leveraginggenomicinformation pages 2-4
5. lee2024theintricatelink pages 8-8
6. sidarta2024lipidphaseseparation pages 1-2
7. sidarta2024lipidphaseseparation pages 12-14
8. chong2024archaeamembranesin pages 1-2
9. li2024biosynthesisofgmgt pages 1-2
10. dessenne2024lipidomicanalysesreveal pages 8-12
11. ramon2023ageneraloverview pages 2-4
12. garcia2024identificationoftwo pages 6-7
13. garcia2024identificationoftwo pages 1-2
14. ramoneda2024leveraginggenomicinformation pages 4-6
15. ramoneda2024leveraginggenomicinformation pages 1-2
16. dessenne2024lipidomicanalysesreveal pages 1-2
17. garcia2024identificationoftwo pages 4-6
18. ramoneda2024leveraginggenomicinformation pages 6-7
19. ramoneda2024leveraginggenomicinformation pages 7-7
20. maiti2024extrememakeoverthe pages 1-2
21. maiti2024extrememakeoverthe pages 3-4
22. sidarta2024lipidphaseseparation pages 18-19
23. ramon2023ageneraloverview pages 4-5
24. garcia2024identificationoftwo pages 3-4
25. garcia2024identificationoftwo pages 2-2
26. li2024biosynthesisofgmgt pages 6-7
27. maiti2024extrememakeoverthe pages 4-5
28. https://doi.org/10.1007/s42770-023-01057-4
29. https://doi.org/10.1039/d3sc04523d
30. https://doi.org/10.1128/spectrum.03925-23
31. https://doi.org/10.1111/mmi.15323
32. https://doi.org/10.1073/pnas.2318761121
33. https://doi.org/10.3389/frbis.2023.1338019
34. https://doi.org/10.37256/amtt.5220244537
35. https://doi.org/10.1093/ismejo/wrae195
36. https://doi.org/10.1128/spectrum.00757-24
37. https://doi.org/10.1038/s41467-024-49650-x
38. https://doi.org/10.1039/d4cc03114h
39. https://doi.org/10.1007/s12275-023-00031-x
40. https://doi.org/10.1093/ismejo/wrae195,
41. https://doi.org/10.1007/s42770-023-01057-4,
42. https://doi.org/10.1007/s12275-023-00031-x,
43. https://doi.org/10.37256/amtt.5220244537,
44. https://doi.org/10.1039/d3sc04523d,
45. https://doi.org/10.1111/mmi.15323,
46. https://doi.org/10.1128/spectrum.03925-23,
47. https://doi.org/10.1128/spectrum.00757-24,
48. https://doi.org/10.3389/frbis.2023.1338019,
49. https://doi.org/10.1073/pnas.2318761121,
50. https://doi.org/10.1038/s41467-024-49650-x,
51. https://doi.org/10.1039/d4cc03114h,