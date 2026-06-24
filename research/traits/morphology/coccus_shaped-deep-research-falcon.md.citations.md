# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** coccus shaped
- **METPO identifier:** METPO:1000668
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a spherical or nearly spherical morphology, with roughly equal dimensions in all directions.
- **Parent traits:** METPO:1000666
- **Synonyms:** coccus, coccus-shaped
- **Existing evidence:** DOI:10.1038/nrmicro3088: spherical cocci synthesize peptidoglycan only at the division septum (Supports coccus shape as a spherical morphology with septal wall growth rather than lateral elongation.) | PMID:19747126: Staphylococcus aureus is a facultative, Gram-positive coccus (Organism example: Staphylococcus aureus is described as coccus-shaped.)
- **Existing causal graph summary:** coccus_shaped_septal_growth: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **coccus shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/coccus_shaped.yaml`.

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
**Generated:** 2026-06-18T07:35:09.617338

1. pinho2013howtoget pages 1-2
2. pinho2013howtoget pages 3-4
3. pinho2013howtoget pages 2-3
4. murodov2024modernviewson pages 1-3
5. battaje2023modelsversuspathogens pages 3-4
6. schaper2024cellconstrictionrequires pages 1-2
7. costa2024theroleof pages 1-2
8. costa2023newapproachesto pages 248-252
9. whitley2024peptidoglycansynthesisdrives pages 1-2
10. massidda2013frommodelsto pages 1-2
11. massidda2013frommodelsto pages 2-3
12. https://doi.org/10.1038/s41564-024-01629-6
13. https://doi.org/10.1128/mbio.03235-23
14. https://doi.org/10.1126/sciadv.ade9023
15. https://doi.org/10.1038/s41564-024-01650-9
16. https://doi.org/10.1038/nrmicro3088
17. https://doi.org/10.1042/BSR20221664
18. https://doi.org/10.1111/1462-2920.12189
19. https://doi.org/10.1038/nrmicro3088,
20. https://doi.org/10.1042/bsr20221664,
21. https://doi.org/10.1038/s41564-024-01629-6,
22. https://doi.org/10.1128/mbio.03235-23,
23. https://doi.org/10.1038/s41564-024-01650-9,
24. https://doi.org/10.1111/1462-2920.12189,