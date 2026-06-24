# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** amphitrichous
- **METPO identifier:** traitmech:000059
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagellar arrangement with flagella (single filaments or tufts) at both poles of the cell.
- **Parent traits:** traitmech:000056
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe bipolar (amphitrichous) flagellation among the flagellation patterns governed by FlhF/FlhG.) | DOI:10.3390/biom9070279:  (Flagellum review supports polar flagellar filaments as locomotory organelles.)
- **Existing causal graph summary:** amphitrichous_bipolar_flagella: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **amphitrichous** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/amphitrichous.yaml`.

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
**Generated:** 2026-06-18T06:37:27.023897

1. cohen2020campylobacterjejunimotility pages 1-2
2. chu2020phylogeneticdistributionultrastructure pages 1-3
3. arroyoperez2024aconservedcellpole pages 2-3
4. dornes2024polarconfinementof pages 4-6
5. dornes2024polarconfinementof pages 2-4
6. arroyoperez2024aconservedcellpole pages 14-15
7. gibson2023controlofthe pages 2-5
8. dornes2024polarconfinementof pages 1-2
9. arroyoperez2024aconservedcellpole pages 1-2
10. nedeljkovic2021bacterialflagellarfilament pages 1-2
11. grognot2021morethanpropellers pages 4-5
12. grognot2021morethanpropellers pages 1-2
13. gibson2023controlofthe pages 5-7
14. https://doi.org/10.1371/journal.ppat.1008620
15. https://doi.org/10.3390/biom10030363
16. https://doi.org/10.1038/s41467-024-50274-4
17. https://doi.org/10.7554/eLife.93004.3
18. https://doi.org/10.1128/jb.00110-23
19. https://doi.org/10.3390/ijms22147521
20. https://doi.org/10.1016/j.mib.2021.02.005
21. https://doi.org/10.1371/journal.ppat.1008620,
22. https://doi.org/10.3390/biom10030363,
23. https://doi.org/10.3390/ijms22147521,
24. https://doi.org/10.1016/j.mib.2021.02.005,
25. https://doi.org/10.7554/elife.93004.3,
26. https://doi.org/10.1038/s41467-024-50274-4,
27. https://doi.org/10.1128/jb.00110-23,