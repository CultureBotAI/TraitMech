# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pangenome openness
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000102
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing the structure of a species' pangenome — the balance of core versus accessory genes and whether the pangenome is open (continually acquiring new genes across genomes) or closed.
- **Parent traits:** METPO:1000188
- **Synonyms:** open pangenome
- **Existing evidence:** DOI:10.1073/pnas.0506758102:  (Tettelin et al. introduced the microbial pan-genome concept, distinguishing core and dispensable genes and open versus closed pangenomes.) | DOI:10.1038/nmicrobiol.2017.40:  (McInerney, McNally & O'Connell review why prokaryotes have pangenomes and what drives their openness.)
- **Existing causal graph summary:** pangenome_openness_hgt: 11 nodes, 9 edges

## Research Objective

Research the microbial trait **pangenome openness** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/pangenome_openness.yaml`.

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
**Generated:** 2026-08-04T05:14:39.178617

1. tonkinhill2023challengesinprokaryote pages 4-6
2. pardeshi2024pangenomicstounderstand pages 3-7
3. whelan2021evidenceforselection pages 1-2
4. mazzamurro2024intragenomicconflictswith pages 8-10
5. lass2024pneumococcalextracellularvesicles pages 1-2
6. dewar2024bacteriallifestyleshapes pages 2-3
7. li2024populationandfunctional pages 9-9
8. medini2020thepangenomea pages 7-10
9. dewar2024bacteriallifestyleshapes pages 5-5
10. dewar2024bacteriallifestyleshapes pages 5-7
11. pardeshi2024pangenomicstounderstand pages 1-3
12. mazzamurro2024intragenomicconflictswith pages 2-3
13. dewar2024bacteriallifestyleshapes pages 3-5
14. *S. pneumoniae*
15. *Pectobacterium*
16. measurement layer
17. 10.1073/pnas.2320170121
18. 10.1371/journal.pbio.3002814
19. 10.1128/msphere.00727-24
20. 10.1101/2024.09.02.610764
21. 10.1002/fft2.321
22. 10.1099/mgen.0.001021
23. 10.1093/molbev/msab139
24. 10.1007/978-3-030-38281-0_1
25. 10.1073/pnas.0506758102
26. 10.1038/nmicrobiol.2017.40
27. https://doi.org/10.1073/pnas.2320170121
28. https://doi.org/10.1371/journal.pbio.3002814
29. https://doi.org/10.1128/msphere.00727-24
30. https://doi.org/10.1101/2024.09.02.610764
31. https://doi.org/10.1002/fft2.321
32. https://doi.org/10.1099/mgen.0.001021
33. https://doi.org/10.1093/molbev/msab139
34. https://doi.org/10.1007/978-3-030-38281-0_1
35. https://doi.org/10.1073/pnas.0506758102
36. https://doi.org/10.1038/nmicrobiol.2017.40
37. https://doi.org/10.1007/978-3-030-38281-0\_1,
38. https://doi.org/10.1099/mgen.0.001021,
39. https://doi.org/10.1101/2024.09.02.610764,
40. https://doi.org/10.1073/pnas.2320170121,
41. https://doi.org/10.1093/molbev/msab139,
42. https://doi.org/10.1371/journal.pbio.3002814,
43. https://doi.org/10.1128/msphere.00727-24,
44. https://doi.org/10.1002/fft2.321,