# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** saprotrophy
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000055
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic-ecology lifestyle in which an organism feeds on dead or decaying organic matter, mineralizing it and driving carbon and nutrient cycling (decomposition).
- **Parent traits:** METPO:1000059
- **Synonyms:** decomposer, saprophytic
- **Existing evidence:** DOI:10.3389/fmicb.2012.00348:  (Schimel & Schaeffer, "Microbial control over carbon cycling in soil", support microbial decomposition of organic matter as a central ecosystem process.) | DOI:10.1038/nrmicro.2017.87:  (Fierer supports decomposer/saprotrophic activity as a key function of soil microbial communities.)
- **Existing causal graph summary:** saprotrophy_decomposition_cycling: 14 nodes, 9 edges

## Research Objective

Research the microbial trait **saprotrophy** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/saprotrophy.yaml`.

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
**Generated:** 2026-08-03T23:50:00.978925

1. zanne2020fungalfunctionalecology pages 15-16
2. christian2024plantendophytecommunicationscaling pages 12-13
3. shabaev2024saprotrophicwooddecay pages 14-16
4. gurovic2023regulationoflignocellulose pages 2-3
5. wunderlich2023understandingthemicrobial pages 4-6
6. elias2024microbialandmineral pages 1-2
7. elias2024microbialandmineral pages 12-13
8. wunderlich2023understandingthemicrobial pages 11-12
9. 10.3390/jof11010021
10. 10.1038/s41467-024-54446-0
11. 10.1080/00275514.2023.2299658
12. 10.1093/jambio/lxac002
13. 10.1186/s42523-022-00224-6
14. 10.1111/brv.12570
15. 10.1038/nrmicro.2017.87
16. https://doi.org/10.3390/jof11010021
17. https://doi.org/10.1038/s41467-024-54446-0
18. https://doi.org/10.1080/00275514.2023.2299658
19. https://doi.org/10.1093/jambio/lxac002
20. https://doi.org/10.1186/s42523-022-00224-6
21. https://doi.org/10.1111/brv.12570
22. https://doi.org/10.1038/nrmicro.2017.87
23. https://doi.org/10.1111/brv.12570,
24. https://doi.org/10.1080/00275514.2023.2299658,
25. https://doi.org/10.1093/jambio/lxac002,
26. https://doi.org/10.1038/s41467-024-54446-0,
27. https://doi.org/10.3390/jof11010021,
28. https://doi.org/10.1186/s42523-022-00224-6,