# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** tailed shaped
- **METPO identifier:** METPO:1000695
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has an elongated polar appendage or stalk extending from the cell body.
- **Parent traits:** METPO:1000666
- **Synonyms:** tailed
- **Existing evidence:** DOI:10.1146/annurev.micro.061705.103240: prosthecate bacteria (Prosthecate-bacteria review supports tailed/stalked cell morphology in Caulobacter and related lineages.) | DOI:10.1146/annurev-cellbio-101011-155745: polar growth (Cell-shape review supports unipolar peptidoglycan growth as the basis for stalk-like polar appendages.)
- **Existing causal graph summary:** tailed_shaped_polar_stalk_growth: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **tailed shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/tailed_shaped.yaml`.

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
**Generated:** 2026-06-18T10:24:23.832746

1. barrows2023synchronizedswarmersand pages 5-7
2. richter2023interactingbactofilinsimpact pages 13-15
3. pohl2024adynamicbactofilin pages 2-3
4. barrows2023synchronizedswarmersand pages 11-13
5. north2023thecaulobacterntrbntrc pages 1-2
6. https://doi.org/10.1128/jb.00384-22
7. https://doi.org/10.7554/eLife.86577
8. https://doi.org/10.1371/journal.pgen.1010788
9. https://doi.org/10.1128/jb.00181-23
10. https://doi.org/10.7554/eLife.86577.2
11. https://doi.org/10.1128/jb.00384-22,
12. https://doi.org/10.7554/elife.86577.2,
13. https://doi.org/10.1371/journal.pgen.1010788,
14. https://doi.org/10.1128/jb.00181-23,