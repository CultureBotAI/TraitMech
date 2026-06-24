# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pangenome openness
- **METPO identifier:** traitmech:000102
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing the structure of a species' pangenome — the balance of core versus accessory genes and whether the pangenome is open (continually acquiring new genes across genomes) or closed.
- **Parent traits:** METPO:1000188
- **Synonyms:** open pangenome
- **Existing evidence:** DOI:10.1073/pnas.0506758102:  (Tettelin et al. introduced the microbial pan-genome concept, distinguishing core and dispensable genes and open versus closed pangenomes.) | DOI:10.1038/nmicrobiol.2017.40:  (McInerney, McNally & O'Connell review why prokaryotes have pangenomes and what drives their openness.)
- **Existing causal graph summary:** pangenome_openness_hgt: 3 nodes, 2 edges

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
**Generated:** 2026-06-18T03:47:20.574546

1. parmigiani2024revisitingpangenomeopenness pages 1-3
2. wang2024comparativegenomicsunveils pages 12-15
3. carhuaricrahuaman2024stepbystepbacterialgenome pages 9-12
4. parmigiani2024revisitingpangenomeopenness pages 10-12
5. parmigiani2024revisitingpangenomeopenness pages 5-7
6. tonkinhill2023robustanalysisof pages 1-2
7. liu2024integrativegenomicswould pages 7-8
8. golchha2024bacterialpangenomea pages 5-6
9. golchha2024bacterialpangenomea pages 6-7
10. le2024efficientinferenceof pages 14-15
11. tonkinhill2023challengesinprokaryote pages 1-2
12. wang2024comparativegenomicsunveils pages 15-17
13. wang2024comparativegenomicsunveils pages 1-2
14. golchha2024bacterialpangenomea pages 1-2
15. tonkinhill2023challengesinprokaryote pages 4-6
16. tonkinhill2023robustanalysisof pages 16-17
17. tonkinhill2023robustanalysisof pages 10-11
18. parmigiani2024revisitingpangenomeopenness pages 14-16
19. parmigiani2024revisitingpangenomeopenness pages 12-14
20. agarwal2023pangenomeinsightsinto pages 4-5
21. parmigiani2024revisitingpangenomeopenness pages 7-8
22. tonkinhill2023robustanalysisof pages 7-8
23. f_{new}(m) = K m^{-\alpha}
\
24. order-independent
25. https://doi.org/10.1099/mgen.0.001021
26. https://doi.org/10.1101/2022.04.23.489244
27. https://doi.org/10.3390/microorganisms12050986
28. https://doi.org/10.1007/978-1-0716-3838-5_5
29. https://doi.org/10.24072/pcjournal.415
30. https://doi.org/10.47852/bonviewmedin42022496
31. https://doi.org/10.1186/s13059-024-03362-z
32. https://doi.org/10.1016/j.heliyon.2024.e34719
33. https://doi.org/10.3389/fmicb.2023.1213261
34. https://doi.org/10.24072/pcjournal.415,
35. https://doi.org/10.1007/978-1-0716-3838-5\_5,
36. https://doi.org/10.3390/microorganisms12050986,
37. https://doi.org/10.1099/mgen.0.001021,
38. https://doi.org/10.1101/2022.04.23.489244,
39. https://doi.org/10.1016/j.heliyon.2024.e34719,
40. https://doi.org/10.47852/bonviewmedin42022496,
41. https://doi.org/10.1186/s13059-024-03362-z,
42. https://doi.org/10.3389/fmicb.2023.1213261,