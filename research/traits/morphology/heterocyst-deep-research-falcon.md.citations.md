# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** heterocyst
- **METPO identifier:** traitmech:000073
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait in which a filamentous cyanobacterium differentiates specialized, thick-walled cells (heterocysts) that create a microoxic interior for oxygen-sensitive nitrogen fixation.
- **Parent traits:** METPO:1000059
- **Synonyms:** heterocyst-forming
- **Existing evidence:** DOI:10.1101/cshperspect.a000315:  (Kumar, Mella-Herrera & Golden describe heterocysts as differentiated cells whose structure and metabolism accommodate oxygen-sensitive nitrogen fixation.) | DOI:10.1093/femsre/fuw029:  (Herrero, Stavans & Flores describe heterocysts within the multicellular filament of heterocyst-forming cyanobacteria.)
- **Existing causal graph summary:** heterocyst_microoxic_nitrogen_fixation: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **heterocyst** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/heterocyst.yaml`.

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
**Generated:** 2026-06-18T08:27:26.299384

1. sarasabuisan2023expandingthefurc pages 14-16
2. sarasabuisan2023expandingthefurc pages 10-12
3. kolan2024tradeoffsbetweenphage pages 6-9
4. kolan2024tradeoffsbetweenphage pages 9-10
5. uesaka2024restorationofthe pages 5-6
6. kolan2024tradeoffsbetweenphage pages 1-2
7. werner2025theroleof pages 12-13
8. uesaka2024restorationofthe pages 1-2
9. uesaka2024restorationofthe pages 4-5
10. sarasabuisan2023expandingthefurc pages 1-2
11. s
12. e
13. https://doi.org/10.1371/journal.pone.0289761
14. https://doi.org/10.1101/2023.10.04.560878
15. https://doi.org/10.1093/pcp/pcae011
16. https://doi.org/10.1093/pcp/pcae011,
17. https://doi.org/10.1371/journal.pone.0289761,
18. https://doi.org/10.1101/2023.10.04.560878,
19. https://doi.org/10.1111/ppl.70248,