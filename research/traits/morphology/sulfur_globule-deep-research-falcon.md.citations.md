# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** sulfur globule
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000069
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An intracellular (or periplasmic) inclusion of elemental sulfur formed as an intermediate during the oxidation of reduced sulfur compounds, characteristic of many sulfur-oxidizing and phototrophic sulfur bacteria.
- **Parent traits:** traitmech:000066
- **Synonyms:** sulfur inclusion
- **Existing evidence:** DOI:10.1016/S0065-2911(08)00002-7:  (Frigaard & Dahl describe sulfur globules as sulfur-storage inclusions formed during oxidative sulfur metabolism in phototrophic sulfur bacteria.) | DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow include sulfur globules among bacterial intracellular storage inclusions/organelles.)
- **Existing causal graph summary:** sulfur_globule_sulfur_oxidation_intermediate: 8 nodes, 6 edges

## Research Objective

Research the microbial trait **sulfur globule** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/sulfur_globule.yaml`.

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
**Generated:** 2026-08-04T10:23:24.427110

1. hanson2016chlorobaculumtepidumgrowth pages 5-6
2. rudenko2024mechanismofintracellular pages 10-12
3. wang2022thepathwayof pages 1-3
4. wang2022thepathwayof pages 3-4
5. kumpel2023cellbiologyof pages 1-3
6. kumpel2023cellbiologyof pages 7-10
7. benisch2024awidespreadbacterial pages 9-10
8. benisch2024awidespreadbacterial pages 1-2
9. benisch2024awidespreadbacterial pages 3-4
10. benisch2024awidespreadbacterial pages 8-9
11. benisch2024awidespreadbacterial pages 6-7
12. benisch2024awidespreadbacterial pages 4-6
13. https://doi.org/10.3390/ijms252010962
14. https://doi.org/10.1126/sciadv.adk9345
15. https://doi.org/10.3390/microorganisms11071792.
16. https://doi.org/10.20944/preprints202306.1429.v1
17. https://doi.org/10.1128/AEM.01941-21
18. https://doi.org/10.1111/1462-2920.12995
19. https://doi.org/10.1128/aem.01941-21,
20. https://doi.org/10.20944/preprints202306.1429.v1,
21. https://doi.org/10.3390/ijms252010962,
22. https://doi.org/10.1111/1462-2920.12995,
23. https://doi.org/10.1126/sciadv.adk9345,