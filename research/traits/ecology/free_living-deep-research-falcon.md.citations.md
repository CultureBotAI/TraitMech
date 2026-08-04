# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** free-living
- **METPO identifier:** traitmech:000048
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A habitat association in which an organism lives independently in the environment, not obligately associated with a host.
- **Parent traits:** traitmech:000047
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro1341:  (Martiny et al. support biogeographic patterning of free-living microbial taxa across environments.) | DOI:10.1038/nrmicro.2017.171:  (Poole et al. describe rhizobia in their free-living soil phase, contrasting it with the host-associated endosymbiotic phase.)
- **Existing causal graph summary:** free_living_environmental_habitat: 9 nodes, 7 edges

## Research Objective

Research the microbial trait **free-living** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/free_living.yaml`.

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
**Generated:** 2026-08-03T23:24:02.911877

1. jaffe2023habitattransitionin pages 4-6
2. jaffe2023habitattransitionin pages 6-8
3. krol2020cyclicdigmpsignaling pages 3-5
4. obeng2023bacterialcdigmphas pages 1-2
5. hollensteiner2023pangenomeanalysisof pages 1-2
6. dewar2024bacteriallifestyleshapes pages 1-2
7. dewar2024bacteriallifestyleshapes pages 3-5
8. krol2020cyclicdigmpsignaling pages 1-2
9. 10.1073/pnas.2320170121
10. 10.1038/s41564-023-01468-x
11. 10.1371/journal.pone.0287947
12. 10.48550/arXiv.2302.00582
13. 10.1515/hsz-2020-0232
14. 10.1038/nrmicro1341
15. https://doi.org/10.1073/pnas.2320170121
16. https://doi.org/10.1038/s41564-023-01468-x
17. https://doi.org/10.1371/journal.pone.0287947
18. https://doi.org/10.48550/arxiv.2302.00582
19. https://doi.org/10.1515/hsz-2020-0232
20. https://doi.org/10.1038/nrmicro1341
21. https://doi.org/10.48550/arxiv.2302.00582,
22. https://doi.org/10.1515/hsz-2020-0232,
23. https://doi.org/10.1038/s41564-023-01468-x,
24. https://doi.org/10.1073/pnas.2320170121,
25. https://doi.org/10.1371/journal.pone.0287947,