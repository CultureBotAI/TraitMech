# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemotaxis
- **METPO identifier:** traitmech:000086
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A behavioral physiology in which cells bias their movement toward attractants or away from repellents by modulating flagellar motor switching in response to chemical gradients.
- **Parent traits:** METPO:1000059
- **Synonyms:** chemotactic
- **Existing evidence:** DOI:10.1038/nrm1524:  (Wadhams & Armitage review bacterial chemotaxis as gradient-guided movement controlled by a histidine-aspartate phosphorelay.) | DOI:10.1038/nrmicro2505:  (Porter, Wadhams & Armitage review signal processing in complex chemotaxis pathways.)
- **Existing causal graph summary:** chemotaxis_gradient_response: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **chemotaxis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemotaxis.yaml`.

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
**Generated:** 2026-06-18T11:25:38.376285

1. muok2024unpackingalternativefeatures pages 2-4
2. muok2024unpackingalternativefeatures pages 13-15
3. cassidy2023structureofthe pages 1-2
4. wheeler2024individualbacterialcells pages 8-9
5. fu2024decipheringbacterialchemorepulsion pages 3-4
6. stehnach2024multiplexedmicrofluidicplatform pages 1-4
7. scheidweiler2024spatialstructurechemotaxis pages 7-8
8. liu2024counterclockwiserotationof pages 1-2
9. soriano2023chemotaxisinpectobacterium pages 30-33
10. https://doi.org/10.1146/annurev-micro-032421-110850
11. https://doi.org/10.1002/prot.26430
12. https://doi.org/10.1128/mbio.00793-23
13. https://doi.org/10.1038/s41467-023-44267-y
14. https://doi.org/10.1128/mbio.00440-24
15. https://doi.org/10.1007/s00248-024-02366-3
16. https://doi.org/10.21769/BioProtoc.5062
17. https://doi.org/10.3390/microorganisms12081706
18. https://doi.org/10.21769/bioprotoc.5062
19. https://doi.org/10.1038/s41564-024-01729-3
20. https://doi.org/10.1146/annurev-micro-032421-110850,
21. https://doi.org/10.1038/s41564-024-01729-3,
22. https://doi.org/10.1128/mbio.00793-23,
23. https://doi.org/10.1002/prot.26430,
24. https://doi.org/10.3390/microorganisms12081706,
25. https://doi.org/10.21769/bioprotoc.5062,
26. https://doi.org/10.1038/s41467-023-44267-y,
27. https://doi.org/10.1128/mbio.00440-24,