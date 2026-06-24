# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** host-associated
- **METPO identifier:** traitmech:000049
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A habitat association in which an organism lives persistently on or in a plant or animal host (e.g. as a member of a host microbiome), spanning commensal, mutualistic, and pathogenic relationships.
- **Parent traits:** traitmech:000047
- **Synonyms:** 
- **Existing evidence:** DOI:10.1073/pnas.1218525110:  (McFall-Ngai et al. document the ubiquity of host-associated microbial communities across the animal kingdom.) | DOI:10.1126/science.1104816:  (Bäckhed et al. characterize the host-associated gut microbiota as a dense, coevolved community.)
- **Existing causal graph summary:** host_associated_microbiome: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **host-associated** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/host_associated.yaml`.

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
**Generated:** 2026-06-17T20:30:49.103181

1. liu2024rootcolonizationby pages 1-2
2. buzun2024abacterialsialidase pages 1-3
3. schaus2024ruminococcustorquesis pages 1-2
4. law2024lifeatthe pages 7-8
5. meng2024identificationofthe pages 1-2
6. doranga2024nutritionofescherichia pages 1-2
7. chen2024thefunctionof pages 1-3
8. liu2024rootcolonizationby pages 2-3
9. ganesan2024dynamicsandmolecular pages 43-47
10. yang2024mechanismsofrhizosphere pages 4-5
11. chen2024thefunctionof pages 10-12
12. yang2024mechanismsofrhizosphere pages 1-3
13. chen2024thefunctionof pages 9-10
14. https://doi.org/10.1016/j.chom.2023.12.014
15. https://doi.org/10.1152/ajpgi.00261.2022
16. https://doi.org/10.1128/mbio.00039-24
17. https://doi.org/10.1093/femsre/fuae008
18. https://doi.org/10.3390/biology13020095
19. https://doi.org/10.3389/fpls.2024.1491495
20. https://doi.org/10.1093/femsre/fuad066
21. https://doi.org/10.1186/s40168-024-01813-0
22. https://doi.org/10.1128/ecosalplus.esp-0006-2023
23. https://doi.org/10.1016/j.chom.2023.12.014,
24. https://doi.org/10.1128/ecosalplus.esp-0006-2023,
25. https://doi.org/10.1093/femsre/fuad066,
26. https://doi.org/10.3389/fpls.2024.1491495,
27. https://doi.org/10.3390/biology13020095,
28. https://doi.org/10.1186/s40168-024-01813-0,
29. https://doi.org/10.1128/mbio.00039-24,
30. https://doi.org/10.1093/femsre/fuae008,