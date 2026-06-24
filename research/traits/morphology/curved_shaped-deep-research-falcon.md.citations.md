# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** curved shaped
- **METPO identifier:** METPO:1000670
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a bent or curved cell body rather than a straight rod or sphere.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_curved_spiral, curved-shaped
- **Existing evidence:** DOI:10.1371/journal.pbio.1002565: curved cells appear to be optimized for motility (Supports curved cells as a recognized bacterial morphology with possible functional associations.)
- **Existing causal graph summary:** curved_shaped_scaffolded_curvature: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **curved shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/curved_shaped.yaml`.

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
**Generated:** 2026-06-18T07:38:47.607762

1. pohl2024anoutermembrane pages 1-2
2. banks2022asymmetricpeptidoglycanediting pages 1-2
3. kysela2016diversitytakesshape pages 4-5
4. teeseling2017determinantsofbacterial pages 3-4
5. pohl2024anoutermembrane pages 12-13
6. liu2024filamentstructureand pages 1-2
7. teeseling2017determinantsofbacterial pages 1-3
8. banks2022asymmetricpeptidoglycanediting pages 10-11
9. pohl2024anoutermembrane pages 18-19
10. 0.63, 0.66
11. 0.10, 0.12
12. https://doi.org/10.1038/s41467-024-51790-z
13. https://doi.org/10.1073/pnas.2309984121
14. https://doi.org/10.1038/s41467-022-29007-y
15. https://doi.org/10.1371/journal.pbio.1002565
16. https://doi.org/10.3389/fmicb.2017.01264
17. https://doi.org/10.1038/s41467-024-51790-z,
18. https://doi.org/10.1073/pnas.2309984121,
19. https://doi.org/10.1038/s41467-022-29007-y,
20. https://doi.org/10.1371/journal.pbio.1002565,
21. https://doi.org/10.3389/fmicb.2017.01264,