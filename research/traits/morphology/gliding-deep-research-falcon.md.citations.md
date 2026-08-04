# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** gliding
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000706
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A motile in which an organism moves smoothly along solid surfaces without flagella or pili.
- **Parent traits:** METPO:1000702
- **Synonyms:** 
- **Existing evidence:** DOI:10.1146/annurev.micro.55.1.49: move actively over surfaces (Supports gliding as active surface movement without flagella.)
- **Existing causal graph summary:** gliding_surface_motility: 10 nodes, 10 edges

## Research Objective

Research the microbial trait **gliding** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/gliding.yaml`.

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
**Generated:** 2026-08-04T08:41:52.945772

1. chen2022flagellarmotortransformed pages 1-2
2. sato2021colonyspreadingof pages 1-3
3. vincent2022dynamicprotondependentmotors pages 1-2
4. jolivet2023integrinlikeadhesincgld pages 1-3
5. thunes2024glidingmotilityproteins pages 1-2
6. thunes2024glidingmotilityproteins pages 2-5
7. zhu2016comparativeanalysisof pages 21-26
8. thunes2024glidingmotilityproteins pages 16-18
9. thunes2024glidingmotilityproteins pages 9-12
10. 10.1128/jb.00068-24
11. 10.1101/2023.10.19.562135
12. 10.1371/journal.pbio.3001443
13. 10.3389/fmicb.2022.891694
14. 10.1038/s41598-020-79762-5
15. 10.1128/JB.01020-15
16. 10.1146/annurev.micro.55.1.49
17. https://doi.org/10.1128/jb.00068-24
18. https://doi.org/10.1101/2023.10.19.562135
19. https://doi.org/10.1371/journal.pbio.3001443
20. https://doi.org/10.3389/fmicb.2022.891694
21. https://doi.org/10.1038/s41598-020-79762-5
22. https://doi.org/10.1128/JB.01020-15
23. https://doi.org/10.1146/annurev.micro.55.1.49
24. https://doi.org/10.1371/journal.pbio.3001443,
25. https://doi.org/10.1128/jb.00068-24,
26. https://doi.org/10.1101/2023.10.19.562135,
27. https://doi.org/10.3389/fmicb.2022.891694,
28. https://doi.org/10.1038/s41598-020-79762-5,
29. https://doi.org/10.1128/jb.01020-15,