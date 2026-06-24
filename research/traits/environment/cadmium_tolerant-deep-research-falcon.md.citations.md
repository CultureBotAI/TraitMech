# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cadmium tolerant
- **METPO identifier:** traitmech:000013
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metal tolerance in which an organism grows in the presence of elevated cadmium (Cd2+) concentrations, typically via cation-efflux resistance systems such as the czc determinant.
- **Parent traits:** traitmech:000012
- **Synonyms:** 
- **Existing evidence:** DOI:10.1111/j.1365-2958.2009.06792.x: CzcP exports transition metals Zn(2+), Cd(2+) and Co(2+) (The cobalt-zinc-cadmium (czc) efflux system of Cupriavidus metallidurans confers cadmium resistance.) | DOI:10.3389/fmicb.2020.00047: C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+ (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates cadmium to a MIC of 2.5 mM.)
- **Existing causal graph summary:** cadmium_tolerance_czc_efflux: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **cadmium tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/cadmium_tolerant.yaml`.

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
**Generated:** 2026-06-17T21:46:24.131235

1. chatterjee2024multimodalcadmiumresistance pages 1-2
2. hovorukha2024metalresistanceof pages 2-3
3. zhu2024thecaddxoperon pages 1-2
4. wang2024surfacedisplayof pages 1-2
5. wang2024surfacedisplayof pages 2-5
6. chatterjee2024multimodalcadmiumresistance pages 6-7
7. sharma2024mechanismsofmicrobial pages 12-13
8. chatterjee2024multimodalcadmiumresistance pages 16-17
9. chatterjee2024multimodalcadmiumresistance pages 17-19
10. chatterjee2024multimodalcadmiumresistance pages 12-14
11. chatterjee2024pseudomonasaeruginosastrain pages 1-4
12. chatterjee2024multimodalcadmiumresistance pages 5-6
13. chatterjee2024multimodalcadmiumresistance pages 3-4
14. chatterjee2024pseudomonasaeruginosastrain pages 4-7
15. chatterjee2024multimodalcadmiumresistance pages 14-15
16. chatterjee2024multimodalcadmiumresistance pages 15-16
17. zhu2024thecaddxoperon pages 3-5
18. chatterjee2024pseudomonasaeruginosastrain pages 21-23
19. https://doi.org/10.1038/s41598-024-80754-y
20. https://doi.org/10.1007/s40201-023-00887-6
21. https://doi.org/10.1007/s40201-023-00887-6;
22. https://doi.org/10.1186/s13567-024-01371-1
23. https://doi.org/10.3390/su16229655
24. https://doi.org/10.3390/ijms252312570
25. https://doi.org/10.1038/s41598-024-80754-y,
26. https://doi.org/10.21203/rs.3.rs-4733845/v1,
27. https://doi.org/10.3390/su16229655,
28. https://doi.org/10.1007/s40201-023-00887-6,
29. https://doi.org/10.1186/s13567-024-01371-1,
30. https://doi.org/10.3390/ijms252312570,