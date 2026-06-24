# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** arsenic tolerant
- **METPO identifier:** traitmech:000017
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metalloid tolerance in which an organism grows in the presence of elevated arsenic (arsenite/arsenate) concentrations, typically via the ars operon, whose ArsB pump extrudes arsenite from the cytoplasm.
- **Parent traits:** traitmech:000012
- **Synonyms:** arsenic resistant
- **Existing evidence:** DOI:10.3389/fmicb.2018.02473: ArsB is an integral membrane protein able to extrude arsenite from the cell cytoplasm, thus diminishing arsenite accumulation (Review supports the ars operon as a near-ubiquitous arsenic-resistance determinant, "more common than genes for tryptophan biosynthesis".) | DOI:10.3389/fmicb.2020.00047: C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+ (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates arsenite (As3+) to a MIC of 3.5 mM.)
- **Existing causal graph summary:** arsenic_tolerance_ars_efflux: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **arsenic tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/arsenic_tolerant.yaml`.

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
**Generated:** 2026-06-17T21:46:22.165402

1. haghi2023arsenicpollutionand pages 3-4
2. rebelo2023unravelingtherole pages 11-13
3. zhuang2023biogeochemicalbehaviorand pages 5-6
4. william2023arsenicandmicroorganisms pages 4-6
5. rueangmongkolrat2024theroleof pages 18-19
6. zhang2024wholecellbioreportertechnology pages 2-3
7. rueangmongkolrat2024theroleof pages 2-4
8. rueangmongkolrat2024theroleof pages 1-2
9. diba2023metagenomicandculturedependent pages 1-2
10. rueangmongkolrat2024theroleof pages 10-14
11. naiel2024thearsenicbioremediation pages 6-7
12. william2023arsenicandmicroorganisms pages 8-9
13. haghi2023arsenicpollutionand pages 7-9
14. and
15. https://doi.org/10.3389/fmicb.2024.1494872
16. https://doi.org/10.3390/antibiotics12091474
17. https://doi.org/10.3390/microorganisms12010074
18. https://doi.org/10.7717/peerj.18383
19. https://doi.org/10.3389/fmicb.2023.1043024
20. https://doi.org/10.3389/fenvs.2023.1195643
21. https://doi.org/10.1016/j.heliyon.2024.e36314
22. https://doi.org/10.1186/s12866-023-02980-0
23. https://doi.org/10.3389/fenvs.2023.1195643,
24. https://doi.org/10.3390/antibiotics12091474,
25. https://doi.org/10.3390/microorganisms12010074,
26. https://doi.org/10.7717/peerj.18383,
27. https://doi.org/10.3389/fmicb.2024.1494872,
28. https://doi.org/10.3389/fmicb.2023.1043024,
29. https://doi.org/10.1186/s12866-023-02980-0,
30. https://doi.org/10.1016/j.heliyon.2024.e36314,