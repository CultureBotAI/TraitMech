# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** twitching motility
- **METPO identifier:** traitmech:000061
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagella-independent surface motility driven by the extension, attachment, and retraction of type IV pili, producing intermittent, jerky translocation of cells across moist surfaces.
- **Parent traits:** METPO:1000702
- **Synonyms:** twitching
- **Existing evidence:** DOI:10.1146/annurev.micro.56.012302.160938:  (Mattick, "Type IV pili and twitching motility", describes twitching as type-IV-pilus-driven surface translocation operating like a grappling hook.) | DOI:10.1146/annurev.micro.57.030502.091014:  (Harshey, "Bacterial motility on a surface", places twitching among the distinct surface-translocation strategies of bacteria.)
- **Existing causal graph summary:** twitching_type_iv_pilus_retraction: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **twitching motility** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/twitching_motility.yaml`.

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
**Generated:** 2026-06-18T10:33:52.780788

1. geiger2024abacterialsense pages 1-3
2. geiger2024abacterialsense pages 3-5
3. zheng2024thesurfaceinterface pages 1-2
4. costin2023themovementbehaviour pages 23-27
5. charlesorszag2024adhesionpilusretraction pages 1-2
6. pelicic2023mechanismofassembly pages 3-5
7. cont2023materialsubstratephysical pages 4-6
8. cont2023materialsubstratephysical pages 6-8
9. cont2023materialsubstratephysical pages 2-4
10. cont2023materialsubstratephysical pages 8-10
11. zheng2024thesurfaceinterface pages 10-11
12. pull
13. pulls
14. https://doi.org/10.1128/jb.00359-24,
15. https://doi.org/10.1128/jb.00442-23,
16. https://doi.org/10.1038/s41467-024-53638-y,
17. https://doi.org/10.1099/mic.0.001311,
18. https://doi.org/10.1073/pnas.2411981121,
19. https://doi.org/10.1128/mbio.03518-22,
20. https://doi.org/10.1038/s41467-024-49101-7,
21. https://doi.org/10.1128/jb.00442-23
22. https://doi.org/10.1128/jb.00359-24
23. https://doi.org/10.1038/s41467-024-53638-y
24. https://doi.org/10.1073/pnas.2411981121
25. https://doi.org/10.1038/s41467-024-49101-7
26. https://doi.org/10.1128/mbio.03518-22
27. https://doi.org/10.1099/mic.0.001311