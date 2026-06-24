# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cream pigmented
- **METPO identifier:** METPO:1003024
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which colony or cell coloration is a pale, off-white or cream hue, typically reflecting low-density carotenoid or other light-absorbing pigments.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_cream
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162844: bacterial carotenoid pigments (Bacterial-carotenoid review supports low-abundance carotenoids as the basis for cream/pale coloration in many bacterial taxa.)
- **Existing causal graph summary:** cream_pigmented_low_carotenoid_density: 4 nodes, 3 edges

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
**Generated:** 2026-06-18T07:36:36.386825

1. janisch2023geneticunderpinningsof pages 4-5
2. janisch2023geneticunderpinningsof pages 10-12
3. gottl2021crisprilibraryguidedtargetidentification pages 8-10
4. janisch2023geneticunderpinningsof pages 17-19
5. nosair2026staphylococcusaureussgoldenyellow pages 16-20
6. janisch2023geneticunderpinningsof pages 12-14
7. janisch2023geneticunderpinningsof pages 5-8
8. https://doi.org/10.3390/pathogens12010086
9. https://doi.org/10.3390/microorganisms9040670
10. https://doi.org/10.1186/s12934-025-02919-2
11. https://doi.org/10.3390/pathogens12010086,
12. https://doi.org/10.3390/microorganisms9040670,
13. https://doi.org/10.1186/s12934-025-02919-2\_reference,