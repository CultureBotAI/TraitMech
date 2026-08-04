# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature range mid4
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000453
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range spans approximately 34–40 °C, characteristic of warm-mesophilic physiology (including many mammalian host-associated bacteria).
- **Parent traits:** METPO:1000306
- **Synonyms:** Mesophilie, TR_34_to_40
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports the 34–40 °C range as the warm-mesophile (mammalian-host) growth range.)
- **Existing causal graph summary:** temperature_range_mid4_warm_mesophile: 17 nodes, 11 edges

## Research Objective

Research the microbial trait **temperature range mid4** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_mid4.yaml`.

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
**Generated:** 2026-08-04T04:32:05.767175

1. lehmann2023adaptivelaboratoryevolution pages 6-7
2. samtani2022microbialmechanismsof pages 1-3
3. mendoza2014temperaturesensingby pages 5-6
4. christina2024mechanismsofanammox pages 22-26
5. 10.1146/annurev-micro-091313-103612
6. 10.1046/j.1365-2958.2002.03103.x
7. 10.1007/s12275-023-00031-x
8. 10.3389/fmicb.2023.1265216
9. 10.1101/2024.07.23.604647
10. 10.1007/s12088-022-01009-w
11. https://doi.org/10.1146/annurev-micro-091313-103612
12. https://doi.org/10.1046/j.1365-2958.2002.03103.x
13. https://doi.org/10.1007/s12275-023-00031-x
14. https://doi.org/10.3389/fmicb.2023.1265216
15. https://doi.org/10.1101/2024.07.23.604647
16. https://doi.org/10.1007/s12088-022-01009-w
17. https://doi.org/10.3389/fmicb.2023.1265216,
18. https://doi.org/10.1007/s12088-022-01009-w,
19. https://doi.org/10.1146/annurev-micro-091313-103612,
20. https://doi.org/10.1101/2024.07.23.604647,