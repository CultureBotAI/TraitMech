# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** polyhydroxyalkanoate granule
- **METPO identifier:** traitmech:000067
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An intracellular storage inclusion composed of polyhydroxyalkanoate (e.g. polyhydroxybutyrate, PHB), a carbon and energy reserve accumulated as cytoplasmic granules.
- **Parent traits:** traitmech:000066
- **Synonyms:** PHB granule, polyhydroxybutyrate inclusion
- **Existing evidence:** DOI:10.1128/mr.54.4.450-472.1990:  (Anderson & Dawes describe polyhydroxyalkanoates (chiefly PHB) as carbon/energy reserves stored as cytoplasmic granules.) | DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow include storage granules such as PHA bodies among bacterial intracellular organelles.)
- **Existing causal graph summary:** pha_granule_carbon_energy_storage: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **polyhydroxyalkanoate granule** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/polyhydroxyalkanoate_granule.yaml`.

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
**Generated:** 2026-06-18T09:20:25.034557

1. martinez2023polyhydroxybutyratemetabolismin pages 2-5
2. reusch1992biologicalcomplexesof pages 1-3
3. santolin2024elucidatingregulationof pages 1-2
4. koning2023thephbgranule pages 1-4
5. martinez2023polyhydroxybutyratemetabolismin pages 5-6
6. anderson1990occurrencemetabolismmetabolic pages 15-16
7. koning2023thephbgranule pages 15-18
8. label
9. PHA synthase label
10. https://doi.org/10.1007/s13205-024-04048-w
11. https://doi.org/10.3390/molecules29102293
12. https://doi.org/10.1016/j.jbc.2024.107523
13. https://doi.org/10.3390/polym15143027
14. https://doi.org/10.1101/2023.07.06.548030
15. https://doi.org/10.1111/j.1574-6968.1992.tb05829.x
16. https://doi.org/10.1128/mr.54.4.450-472.1990
17. https://doi.org/10.3390/molecules29102293,
18. https://doi.org/10.1101/2023.07.06.548030,
19. https://doi.org/10.3390/polym15143027,
20. https://doi.org/10.1111/j.1574-6968.1992.tb05829.x,
21. https://doi.org/10.1016/j.jbc.2024.107523,
22. https://doi.org/10.1128/mr.54.4.450-472.1990,