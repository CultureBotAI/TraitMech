# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** flask shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000675
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a bulbous body with a narrower neck-like extension at one pole.
- **Parent traits:** METPO:1000666
- **Synonyms:** flask, flask-shaped
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: polar growth (Cell-shape review supports polarized peptidoglycan growth as a mechanism producing asymmetric flask-like morphology.)
- **Existing causal graph summary:** flask_shaped_asymmetric_polar_growth: 12 nodes, 7 edges

## Research Objective

Research the microbial trait **flask shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/flask_shaped.yaml`.

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
**Generated:** 2026-08-04T08:34:38.282569

1. cserti2017dynamicsofthe pages 7-9
2. wiegand2020cultivationandfunctional pages 5-6
3. jeske2015planctomycetesdopossess pages 1-2
4. cserti2017dynamicsofthe pages 4-7
5. cserti2017dynamicsofthe pages 9-11
6. hashimi2024cellenvelopediversity pages 1-2
7. boedeker2017determiningthebacterial pages 6-7
8. cserti2017dynamicsofthe pages 1-4
9. wiegand2020cultivationandfunctional pages 6-8
10. https://doi.org/10.1111/mmi.13593
11. https://doi.org/10.1038/ncomms8116
12. https://doi.org/10.1038/s41564-019-0588-1
13. https://doi.org/10.1038/ncomms14853
14. https://doi.org/10.1038/s41564-024-01812-9
15. https://doi.org/10.1371/journal.pbio.1002565
16. https://doi.org/10.3389/fmicb.2017.01264
17. https://doi.org/10.3389/fmicb.2015.00580
18. https://doi.org/10.1111/mmi.13593,
19. https://doi.org/10.1038/s41564-019-0588-1,
20. https://doi.org/10.1038/ncomms8116,
21. https://doi.org/10.1038/s41564-024-01812-9,
22. https://doi.org/10.1038/ncomms14853,