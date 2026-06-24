# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** spindle shaped
- **METPO identifier:** METPO:1000692
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape that is widest at the middle and tapers symmetrically toward pointed poles.
- **Parent traits:** METPO:1000666
- **Synonyms:** spindle
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports symmetric tapered shapes as a genetically determined outcome of polar wall patterning.)
- **Existing causal graph summary:** spindle_shaped_symmetric_taper: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **spindle shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/spindle_shaped.yaml`.

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
**Generated:** 2026-06-18T09:58:16.574180

1. barrows2023synchronizedswarmersand pages 1-3
2. teeseling2017determinantsofbacterial pages 3-4
3. pohl2024adynamicbactofilin pages 3-4
4. pohl2024adynamicbactofilin pages 4-6
5. pohl2024adynamicbactofilin pages 13-15
6. pohl2024adynamicbactofilin pages 19-21
7. richter2023interactingbactofilinsimpact pages 1-2
8. richter2023interactingbactofilinsimpact pages 15-16
9. billini2024thecytoplasmicphosphate pages 1-2
10. pohl2024adynamicbactofilin pages 1-2
11. pohl2023adynamicbactofilin pages 9-12
12. s
13. https://doi.org/10.7554/eLife.86577
14. https://doi.org/10.3389/fmicb.2017.01264
15. https://doi.org/10.1371/journal.pgen.1010788
16. https://doi.org/10.1128/jb.00384-22
17. https://doi.org/10.1038/s42003-024-06469-y
18. https://doi.org/10.1128/jb.00384-22,
19. https://doi.org/10.1371/journal.pgen.1010788,
20. https://doi.org/10.3389/fmicb.2017.01264,
21. https://doi.org/10.7554/elife.86577.2,
22. https://doi.org/10.1038/s42003-024-06469-y,
23. https://doi.org/10.1101/2023.02.27.530196,