# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** swarming motility
- **METPO identifier:** traitmech:000062
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagella-dependent, multicellular surface motility in which cells move rapidly and coordinately across a surface, typically accompanied by hyperflagellation and secretion of a wetting surfactant.
- **Parent traits:** METPO:1000702
- **Synonyms:** swarming
- **Existing evidence:** DOI:10.1038/nrmicro2405:  (Kearns, "A field guide to bacterial swarming motility", defines swarming via increased flagella per cell, surfactant secretion, and movement in multicellular groups.) | DOI:10.1146/annurev.micro.57.030502.091014:  (Harshey, "Bacterial motility on a surface", places swarming among the surface-motility modes of bacteria.)
- **Existing causal graph summary:** swarming_hyperflagellation_surfactant: 6 nodes, 6 edges

## Research Objective

Research the microbial trait **swarming motility** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/swarming_motility.yaml`.

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
**Generated:** 2026-06-30T01:03:49.163805

1. partridge2022surveyingaswarm pages 5-7
2. partridge2013swarmingflexibleroaming pages 5-6
3. yang2024unveilingthehidden pages 6-7
4. kuchma2025geneticanalysisof pages 1-2
5. partridge2013swarmingflexibleroaming pages 6-7
6. daniels2004quorumsensingand pages 11-12
7. daniels2004quorumsensingand pages 6-7
8. deziel2003rhlaisrequired pages 1-2
9. caiazza2005rhamnolipidsmodulateswarming pages 5-6
10. lee2015lossofflil pages 12-13
11. mordini2013theroleof pages 1-2
12. yang2017influenceofphysical pages 3-4
13. partridge2013swarmingflexibleroaming pages 4-4
14. lee2015lossofflil pages 1-2
15. kohler2000swarmingofpseudomonas pages 3-6
16. daniels2004quorumsensingand pages 8-11
17. mordini2013theroleof pages 2-3
18. hwang2025cdigmpisrequired pages 1-2
19. yang2017influenceofphysical pages 1-2
20. hwang2025cdigmpisrequired pages 8-11
21. partridge2013swarmingflexibleroaming pages 1-2
22. partridge2013swarmingflexibleroaming pages 2-4
23. partridge2022surveyingaswarm pages 3-5
24. partridge2013swarmingflexibleroaming pages 4-5
25. wu2024torquespeedrelationshipof pages 13-15
26. deziel2003rhlaisrequired pages 8-9
27. kohler2000swarmingofpseudomonas pages 6-6
28. mordini2013theroleof pages 5-7
29. mordini2013theroleof pages 9-10
30. mordini2013theroleof pages 3-5
31. hwang2025cdigmpisrequired pages 2-5
32. hwang2025cdigmpisrequired pages 11-14
33. liu2022theeffectof pages 1-2
34. hwang2025cdigmpisrequired pages 5-8
35. partridge2013swarmingflexibleroaming pages 7-8
36. yang2017influenceofphysical pages 6-8
37. mordini2013theroleof pages 7-9
38. https://doi.org/10.1128/jb.02063-12,
39. https://doi.org/10.1128/aem.01853-21,
40. https://doi.org/10.3389/fcimb.2024.1465460,
41. https://doi.org/10.1128/jb.02235-14,
42. https://doi.org/10.1128/mbio.00745-24,
43. https://doi.org/10.1128/jb.00520-24,
44. https://doi.org/10.1128/mbio.03322-23,
45. https://doi.org/10.1099/mic.0.26154-0,
46. https://doi.org/10.1128/jb.182.21.5990-5996.2000,
47. https://doi.org/10.1016/j.femsre.2003.09.004,
48. https://doi.org/10.1371/journal.pone.0085065,
49. https://doi.org/10.1128/mbio.00916-25,
50. https://doi.org/10.1128/aem.00373-22,
51. https://doi.org/10.1128/jb.187.21.7351-7361.2005,
52. https://doi.org/10.1016/j.bpj.2017.02.019,