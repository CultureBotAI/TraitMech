# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** star shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000685
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has multiple radiating projections from a central body.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_star_dumbbell_pleomorphic, star, star-shaped
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: polar growth (Cell-shape review supports multi-pole peptidoglycan growth as the basis for prosthecate or appendaged geometries.) | DOI:10.1146/annurev.micro.061705.103240: prosthecate bacteria (Prosthecate-bacteria review supports star-shaped morphology in Stella/Ancalomicrobium and related stalked lineages.)
- **Existing causal graph summary:** star_shaped_multiple_prosthecae: 12 nodes, 9 edges

## Research Objective

Research the microbial trait **star shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/star_shaped.yaml`.

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
**Generated:** 2026-08-04T10:22:37.064083

1. caccamo2018themolecularbasis pages 6-7
2. williams2019mechanismsofpolar pages 71-76
3. caccamo2018themolecularbasis pages 9-11
4. teeseling2017determinantsofbacterial pages 3-4
5. caccamo2018themolecularbasis pages 7-9
6. teeseling2017determinantsofbacterial pages 1-3
7. williams2019mechanismsofpolar pages 66-71
8. caccamo2018themolecularbasis pages 1-2
9. williams2019mechanismsofpolar pages 32-37
10. 10.1128/MRA.00719-19
11. 10.1016/j.tim.2017.09.012
12. 10.3389/fmicb.2017.01264
13. 10.1128/JB.00896-15
14. 10.32469/10355/79574
15. 10.1099/00207713-35-4-518
16. https://doi.org/10.1128/MRA.00719-19
17. https://doi.org/10.1016/j.tim.2017.09.012
18. https://doi.org/10.3389/fmicb.2017.01264
19. https://doi.org/10.1128/JB.00896-15
20. https://doi.org/10.32469/10355/79574
21. https://doi.org/10.1099/00207713-35-4-518
22. https://doi.org/10.1016/j.tim.2017.09.012,
23. https://doi.org/10.3389/fmicb.2017.01264,
24. https://doi.org/10.32469/10355/79574,