# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** peritrichous
- **METPO identifier:** traitmech:000060
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagellar arrangement with flagella distributed over the entire cell surface rather than localized to the poles.
- **Parent traits:** traitmech:000056
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe peritrichous (surface-distributed) flagellation as one of the conserved flagellation patterns.) | DOI:10.3390/biom9070279:  (Flagellum review supports multiple surface flagellar filaments as locomotory organelles, as in peritrichously flagellated enterobacteria.)
- **Existing causal graph summary:** peritrichous_surface_distributed_flagella: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **peritrichous** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/peritrichous.yaml`.

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
**Generated:** 2026-06-18T09:10:32.307483

1. frolov2024constructionofthe pages 1-2
2. rosinke2025characterizinghelicobacterpyloria pages 19-22
3. dunn2025nascentflagellarbasal pages 2-4
4. dunn2025nascentflagellarbasal pages 6-9
5. dornes2024polarconfinementof pages 1-2
6. frolov2024constructionofthe pages 4-5
7. alsenani2024manipulatingflagellargene pages 126-130
8. rosinke2025characterizinghelicobacterpylori pages 19-22
9. lisevich2025physicsofswimming pages 1-2
10. lisevich2025physicsofswimming pages 7-8
11. dunn2025nascentflagellarbasal pages 1-2
12. frolov2024constructionofthe pages 8-10
13. zhang2024biohybridmagneticrobots pages 10-11
14. dunn2025nascentflagellarbasal pages 9-11
15. zhang2024biohybridmagneticrobots pages 11-13
16. dunn2025nascentflagellarbasal pages 4-6
17. zhang2024biohybridmagneticrobots pages 13-15
18. ing
19. https://doi.org/10.3390/fermentation10120606
20. https://doi.org/10.1128/mbio.00530-25
21. https://doi.org/10.1038/s41467-024-50274-4
22. https://doi.org/10.1038/s41467-025-56980-x
23. https://doi.org/10.3390/bioengineering11040311
24. https://doi.org/10.3390/fermentation10120606,
25. https://doi.org/10.1038/s41467-025-56980-x,
26. https://doi.org/10.1128/mbio.00530-25,
27. https://doi.org/10.1038/s41467-024-50274-4,
28. https://doi.org/10.3390/bioengineering11040311,