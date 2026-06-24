# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Homoacetogenesis
- **METPO identifier:** METPO:1000846
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which acetate is produced as the sole reduced end product from reduction of CO2 via the acetyl-CoA pathway.
- **Parent traits:** METPO:1000060
- **Synonyms:** Reductive acetyl-CoA pathway, Wood-Ljungdahl pathway
- **Existing evidence:** DOI:10.1016/j.tibtech.2019.05.008: two mol of carbon dioxide are reduced to one mol of acetyl-CoA (Review supports Wood-Ljungdahl reduction of CO2 to acetyl-CoA and acetate.) | DOI:10.1016/j.bbapap.2008.08.012: Wood-Ljungdahl Pathway of CO2 Fixation (Review supports acetogens using the Wood-Ljungdahl pathway for CO2 fixation.)
- **Existing causal graph summary:** homoacetogenesis_wood_ljungdahl_acetate: 9 nodes, 9 edges

## Research Objective

Research the microbial trait **Homoacetogenesis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/homoacetogenesis.yaml`.

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
**Generated:** 2026-06-18T05:09:17.135849

1. frolov2023obligateautotrophyat pages 1-2
2. ferretti2025bioelectrochemicalconversionof pages 19-23
3. boer2024isolationandcharacterization pages 1-2
4. davin2024clostridiumautoethanogenumalters pages 1-2
5. bae2024harnessingacetogenicbacteria pages 2-3
6. zeldes2024knockdownofgenes pages 1-4
7. bae2024harnessingacetogenicbacteria pages 1-2
8. https://doi.org/10.1039/d4cb00099d
9. https://doi.org/10.1101/2024.06.18.598388
10. https://doi.org/10.1186/s13068-024-02554-w
11. https://doi.org/10.3389/fmicb.2023.1185739
12. https://doi.org/10.3389/fmicb.2024.1426882
13. https://doi.org/10.3389/fmicb.2023.1185739,
14. https://doi.org/10.3389/fmicb.2024.1426882,
15. https://doi.org/10.1039/d4cb00099d,
16. https://doi.org/10.1186/s13068-024-02554-w,
17. https://doi.org/10.1101/2024.06.18.598388,