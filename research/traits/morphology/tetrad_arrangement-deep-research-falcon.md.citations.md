# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** tetrad arrangement
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000119
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell arrangement in which cocci divide in two perpendicular planes and remain attached as groups of four (tetrads).
- **Parent traits:** METPO:1000666
- **Synonyms:** tetrad-forming cocci
- **Existing evidence:** DOI:10.1128/MMBR.00001-06:  (Young's review treats the tetrad as a division-plane-determined coccal arrangement.) | DOI:10.1038/ncomms4842:  (Two-plane division with incomplete daughter-cell separation yields four-cell tetrads.)
- **Existing causal graph summary:** tetrad_two_plane_division: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **tetrad arrangement** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/tetrad_arrangement.yaml`.

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
**Generated:** 2026-08-04T10:28:09.748023

1. zapun2008thedifferentshapes pages 2-3
2. turner2010peptidoglycanarchitecturecan pages 4-6
3. turner2010peptidoglycanarchitecturecan pages 1-2
4. pinho2013howtoget pages 10-11
5. pinho2013howtoget pages 9-10
6. 10.1111/j.1574-6976.2007.00098.x
7. 10.1038/s41467-019-11725-5
8. 10.1038/ncomms1025
9. 10.1128/JB.00163-21
10. 10.1038/nrmicro3088
11. 10.3389/fmicb.2014.00019
12. https://doi.org/10.1111/j.1574-6976.2007.00098.x
13. https://doi.org/10.1038/s41467-019-11725-5
14. https://doi.org/10.1038/ncomms1025
15. https://doi.org/10.1128/JB.00163-21
16. https://doi.org/10.1038/nrmicro3088
17. https://doi.org/10.3389/fmicb.2014.00019
18. https://doi.org/10.1038/s41467-019-11725-5,
19. https://doi.org/10.1111/j.1574-6976.2007.00098.x,
20. https://doi.org/10.1038/ncomms1025,
21. https://doi.org/10.1038/nrmicro3088,