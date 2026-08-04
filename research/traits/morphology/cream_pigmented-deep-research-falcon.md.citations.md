# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cream pigmented
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003024
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which colony or cell coloration is a pale, off-white or cream hue, typically reflecting low-density carotenoid or other light-absorbing pigments.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_cream
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162844: bacterial carotenoid pigments (Bacterial-carotenoid review supports low-abundance carotenoids as the basis for cream/pale coloration in many bacterial taxa.)
- **Existing causal graph summary:** cream_pigmented_low_carotenoid_density: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **cream pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cream_pigmented.yaml`.

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
**Generated:** 2026-08-04T08:08:05.648611

1. tran2020broughttoyou pages 7-9
2. siems2023identificationofstaphyloxanthin pages 4-6
3. sandmann2023genesandpathway pages 5-6
4. sandmann2023genesandpathway pages 3-5
5. siems2023identificationofstaphyloxanthin pages 1-2
6. siems2023identificationofstaphyloxanthin pages 3-4
7. https://doi.org/10.3389/fmicb.2023.1272734
8. https://doi.org/10.3390/biology12101346
9. https://doi.org/10.3934/microbiol.2020026
10. https://doi.org/10.1146/annurev.micro.62.081307.162844.
11. https://doi.org/10.3934/microbiol.2020026,
12. https://doi.org/10.3389/fmicb.2023.1272734,
13. https://doi.org/10.3390/biology12101346,