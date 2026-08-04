# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** extremely halophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000628
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A halophily preference in which an organism requires very high salt concentrations (typically 15-30% NaCl or higher) for optimal growth and cannot grow at salt concentrations below approximately 12%.
- **Parent traits:** METPO:1000629
- **Synonyms:** extreme-halophilic
- **Existing evidence:** PMID:11790755: A cytochrome in an extremely halophilic archaeon, Haloferax volcanii (Organism example: Haloferax volcanii is described as extremely halophilic.)
- **Existing causal graph summary:** extreme_halophile_salt_in_acidic_proteome: 11 nodes, 11 edges

## Research Objective

Research the microbial trait **extremely halophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/extremely_halophilic.yaml`.

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
**Generated:** 2026-08-04T00:35:10.189174

1. baker2024expandedphylogenyof pages 1-4
2. tamir2017nglycosylationisimportant pages 1-3
3. kaminski2013twodistinctnglycosylation pages 1-2
4. oren2008microbiallifeat pages 1-2
5. becker2014phylogeneticallydrivensequencing pages 6-8
6. becker2014phylogeneticallydrivensequencing pages 8-9
7. xing2024thepolyextremophilenatranaerobius pages 1-2
8. gutierrezpreciado2024extremelyacidicproteomes pages 1-4
9. dalmaso2015marineextremophilesa pages 6-8
10. matarredona2020theroleof pages 3-4
11. oren2008microbiallifeat pages 10-11
12. becker2014phylogeneticallydrivensequencing pages 1-2
13. xing2024thepolyextremophilenatranaerobius pages 23-24
14. the
15. https://doi.org/10.1038/s41564-024-01647-4
16. https://doi.org/10.1038/s41559-024-02505-6
17. https://doi.org/10.1128/aem.00145-24
18. https://doi.org/10.1371/journal.pgen.1004784
19. https://doi.org/10.1128/mBio.00716-13
20. https://doi.org/10.1128/AEM.03152-16
21. https://doi.org/10.1186/1746-1448-4-2
22. https://doi.org/10.3390/biom10101390
23. https://doi.org/10.3390/md13041925
24. https://doi.org/10.1186/1746-1448-4-2,
25. https://doi.org/10.3390/md13041925,
26. https://doi.org/10.1038/s41564-024-01647-4,
27. https://doi.org/10.1128/aem.00145-24,
28. https://doi.org/10.1038/s41559-024-02505-6,
29. https://doi.org/10.1371/journal.pgen.1004784,
30. https://doi.org/10.3390/biom10101390,
31. https://doi.org/10.1128/aem.03152-16,
32. https://doi.org/10.1128/mbio.00716-13,