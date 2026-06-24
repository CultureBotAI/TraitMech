# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** psychrotolerant
- **METPO identifier:** METPO:1000618
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference in which growth can occur at low temperatures without an obligate low-temperature preference.
- **Parent traits:** METPO:1000613
- **Synonyms:** 
- **Existing evidence:** DOI:10.1099/ijs.0.65141-0: Pseudomonas guineae sp. nov., a novel psychrotolerant bacterium (Organism example: Pseudomonas guineae is described as psychrotolerant.) | DOI:10.1038/sj.embor.7400662: decreased membrane fluidity (Psychrophile review supports cold-end membrane stress as the challenge that psychrotolerant facultative adaptation overcomes without full psychrophile dedication.)
- **Existing causal graph summary:** psychrotolerant_facultative_cold_adaptation: 5 nodes, 4 edges

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
**Generated:** 2026-06-18T01:28:39.254085

1. ramon2023ageneraloverview pages 1-2
2. moyer2017psychrophilesandpsychrotrophs pages 1-2
3. ponder2005characterizationofpotential pages 1-2
4. sidarta2024lipidphaseseparation pages 1-2
5. barbotin2024quantificationofmembrane pages 10-11
6. ramon2023ageneraloverview pages 4-5
7. sidarta2024lipidphaseseparation pages 2-5
8. purwar2024adaptationsofpsychrophilic pages 10-11
9. li2024mechanismsunderlyingthe pages 10-12
10. purwar2024adaptationsofpsychrophilic pages 8-10
11. moyer2017psychrophilesandpsychrotrophs pages 2-3
12. ponder2005characterizationofpotential pages 10-11
13. oh2024psychrotrophicbacteriathreatening pages 1-5
14. ramon2023ageneraloverview pages 2-4
15. kovacova2024effectofselected pages 1-2
16. oh2024psychrotrophicbacteriathreatening pages 29-34
17. oh2024psychrotrophicbacteriathreatening pages 13-17
18. subramanian2011psychrotolerancemechanismsin pages 4-5
19. sidarta2024lipidphaseseparation pages 12-14
20. sidarta2024lipidphaseseparation pages 5-9
21. sidarta2024lipidphaseseparation pages 14-16
22. purwar2024adaptationsofpsychrophilic pages 6-7
23. oh2024psychrotrophicbacteriathreatening pages 5-9
24. oh2024psychrotrophicbacteriathreatening pages 9-13
25. kovacova2024effectofselected pages 9-10
26. https://doi.org/10.1007/s42770-023-01057-4
27. https://doi.org/10.1016/j.femsec.2004.12.003
28. https://doi.org/10.1128/spectrum.03925-23
29. https://doi.org/10.1101/2023.10.13.562271
30. https://doi.org/10.37256/amtt.5220244537
31. https://doi.org/10.3389/fmicb.2024.1465627
32. https://doi.org/10.24425/pjvs.2024.149353
33. https://doi.org/10.5851/kosfa.2024.e70
34. https://doi.org/10.1016/B978-0-12-809633-8.02282-2
35. https://doi.org/10.7745/kjssf.2011.44.4.625
36. https://doi.org/10.1007/s42770-023-01057-4,
37. https://doi.org/10.1016/b978-0-12-809633-8.02282-2,
38. https://doi.org/10.1016/j.femsec.2004.12.003,
39. https://doi.org/10.1128/spectrum.03925-23,
40. https://doi.org/10.1101/2023.10.13.562271,
41. https://doi.org/10.37256/amtt.5220244537,
42. https://doi.org/10.3389/fmicb.2024.1465627,
43. https://doi.org/10.5851/kosfa.2024.e70,
44. https://doi.org/10.24425/pjvs.2024.149353,
45. https://doi.org/10.7745/kjssf.2011.44.4.625,