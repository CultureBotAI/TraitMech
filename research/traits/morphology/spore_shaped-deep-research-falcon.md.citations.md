# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** spore shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000682
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism or differentiated cell has an endospore-like morphology, reflecting a dormant spore body with specialized protective layers.
- **Parent traits:** METPO:1000666
- **Synonyms:** spore-shaped
- **Existing evidence:** DOI:10.1038/nrmicro2921: structure of the endospore coat (Supports endospore morphology as a differentiated structure with specialized surface layers.)
- **Existing causal graph summary:** spore_shaped_endospore_layers: 18 nodes, 13 edges

## Research Objective

Research the microbial trait **spore shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/spore_shaped.yaml`.

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
**Generated:** 2026-08-04T10:10:10.533596

1. kuwana2024spoivaisan pages 8-9
2. khanna2020shapinganendospore pages 2-4
3. mckenney2013thebacillussubtilis pages 2-4
4. mckenney2013thebacillussubtilis pages 24-26
5. voitsekhovsky2024peculiaritiesofthe pages 1-3
6. khanna2019themoleculararchitecture pages 13-14
7. khanna2020shapinganendospore pages 9-11
8. bauda2024ultrastructureofmacromolecular pages 5-7
9. khanna2020shapinganendospore pages 1-2
10. kuwana2024spoivaisan pages 1-2
11. khanna2019themoleculararchitecture pages 10-12
12. khanna2019themoleculararchitecture pages 4-5
13. mckenney2013thebacillussubtilis pages 11-13
14. bauda2024ultrastructureofmacromolecular pages 7-9
15. bauda2024ultrastructureofmacromolecular pages 1-2
16. 10.1038/s41467-024-45770-6
17. 10.3389/fmicb.2024.1338751
18. 10.15407/microbiolj86.04.091
19. 10.1146/annurev-micro-022520-074650
20. 10.7554/eLife.45257
21. 10.1038/nrmicro2921
22. https://doi.org/10.1038/s41467-024-45770-6
23. https://doi.org/10.3389/fmicb.2024.1338751
24. https://doi.org/10.15407/microbiolj86.04.091
25. https://doi.org/10.1146/annurev-micro-022520-074650
26. https://doi.org/10.7554/eLife.45257
27. https://doi.org/10.1038/nrmicro2921
28. https://doi.org/10.1146/annurev-micro-022520-074650,
29. https://doi.org/10.1038/nrmicro2921,
30. https://doi.org/10.3389/fmicb.2024.1338751,
31. https://doi.org/10.7554/elife.45257,
32. https://doi.org/10.15407/microbiolj86.04.091,
33. https://doi.org/10.1038/s41467-024-45770-6,