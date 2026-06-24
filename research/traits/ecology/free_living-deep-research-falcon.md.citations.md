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
- **Existing causal graph summary:** free_living_environmental_habitat: 3 nodes, 2 edges

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
**Generated:** 2026-06-17T20:25:25.721076

1. dewar2024bacteriallifestyleshapes pages 7-8
2. jaffe2023habitattransitionin pages 4-6
3. wisniewska2024expandedgeneand pages 1-3
4. wang2024comparativegenomicanalysis pages 5-7
5. wang2023biofilmformationstabilizes pages 5-7
6. hollensteiner2023pangenomeanalysisof pages 11-13
7. agudelo2023theroleof pages 2-3
8. wang2023biofilmformationstabilizes pages 2-5
9. agudelo2023theroleof pages 1-2
10. agudelo2023theroleof pages 10-11
11. grzyb2024decipheringmolecularmechanisms pages 24-25
12. jaffe2023habitattransitionin pages 8-11
13. wang2024comparativegenomicanalysis pages 1-2
14. dewar2024bacteriallifestyleshapes pages 1-2
15. wang2023biofilmformationstabilizes pages 1-2
16. jaffe2023habitattransitionin pages 6-8
17. agudelo2023theroleof pages 6-7
18. are
19. https://doi.org/10.1073/pnas.2320170121
20. https://doi.org/10.1371/journal.pone.0287947
21. https://doi.org/10.1186/s12915-024-02013-w
22. https://doi.org/10.48550/arxiv.2302.00582
23. https://doi.org/10.1128/aem.00601-23
24. https://doi.org/10.1111/1755-0998.13889
25. https://doi.org/10.3389/fmicb.2023.1113412
26. https://doi.org/10.1128/aem.01900-23
27. https://doi.org/10.3389/fpls.2023.1277262
28. https://doi.org/10.3390/microorganisms11061454
29. https://doi.org/10.3390/ijms252413601
30. https://doi.org/10.1073/pnas.2320170121,
31. https://doi.org/10.48550/arxiv.2302.00582,
32. https://doi.org/10.3389/fmicb.2023.1113412,
33. https://doi.org/10.1186/s12915-024-02013-w,
34. https://doi.org/10.1111/1755-0998.13889,
35. https://doi.org/10.1128/aem.01900-23,
36. https://doi.org/10.1128/aem.00601-23,
37. https://doi.org/10.1371/journal.pone.0287947,
38. https://doi.org/10.3389/fpls.2023.1277262,
39. https://doi.org/10.3390/microorganisms11061454,
40. https://doi.org/10.3390/ijms252413601,