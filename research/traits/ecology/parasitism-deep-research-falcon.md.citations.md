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
- **Existing causal graph summary:** parasitism_host_fitness_cost: 3 nodes, 2 edges

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
**Generated:** 2026-06-17T20:43:34.349000

1. rozsa2023definitionsofparasitism pages 1-2
2. rozsa2023definitionsofparasitism pages 2-3
3. barber2024mechanismsofhost pages 3-5
4. barber2024mechanismsofhost pages 5-6
5. reyeslopez2023hemoglobinuptakeand pages 1-2
6. wehrmann2023theemergingrole pages 1-2
7. krishnamurthy2023crisprscreensidentify pages 1-2
8. grondin2024interactionbetweenintestinal pages 2-3
9. shi2024copperstressshapes pages 1-2
10. price2024amoebaeastraining pages 1-2
11. s
12. https://doi.org/10.1093/femsre/fuae019
13. https://doi.org/10.3389/fcimb.2023.1111502
14. https://doi.org/10.3389/fimmu.2023.1303072
15. https://doi.org/10.1128/mbio.00060-23
16. https://doi.org/10.3389/fcimb.2023.1150054
17. https://doi.org/10.3390/pathogens13080608
18. https://doi.org/10.1002/ece3.11705
19. https://doi.org/10.1093/ismejo/wrae100
20. https://doi.org/10.1017/S0031182023000598
21. https://doi.org/10.1080/1040841x.2022.2083939
22. https://doi.org/10.1128/mbio.00827-24
23. https://doi.org/10.1017/s0031182023000598,
24. https://doi.org/10.1002/ece3.11705,
25. https://doi.org/10.1093/femsre/fuae019,
26. https://doi.org/10.3389/fcimb.2023.1150054,
27. https://doi.org/10.3389/fimmu.2023.1303072,
28. https://doi.org/10.1128/mbio.00060-23,
29. https://doi.org/10.3389/fcimb.2023.1111502,
30. https://doi.org/10.3390/pathogens13080608,
31. https://doi.org/10.1093/ismejo/wrae100,
32. https://doi.org/10.1080/1040841x.2022.2083939,
33. https://doi.org/10.1128/mbio.00827-24,