# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** piezophilic
- **METPO identifier:** traitmech:000001
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An environmental growth preference in which an organism grows optimally at hydrostatic pressures substantially above atmospheric pressure (0.1 MPa), characteristic of deep-sea and deep-subsurface microorganisms.
- **Parent traits:** METPO:1000059
- **Synonyms:** barophilic, piezophile
- **Existing evidence:** DOI:10.3389/fmolb.2022.1058381: Microorganisms adapted to HHP are usually known as piezophiles, referring to their preference for high pressure (Membrane-lipid adaptation review supports the definition of piezophiles as high-hydrostatic-pressure-adapted organisms, with adaptation involving unsaturated and branched-chain fatty acids.) | DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum, 120 MPa) at 6 degrees C (Organism example: Colwellia marinimaniae strain MTCD1, the most piezophilic organism described, grows optimally at 120 MPa.)
- **Existing causal graph summary:** piezophilic_hhp_membrane_adaptation: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **piezophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/piezophilic.yaml`.

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
**Generated:** 2026-06-18T01:03:40.606156

1. malas2024biologicalfunctionsat pages 1-2
2. scheffer2023themysteryof pages 1-2
3. tamby2023microbialmembranelipid pages 1-2
4. qiu2024metabolicadaptationsof pages 1-2
5. tamby2023microbialmembranelipid pages 2-4
6. malas2024biologicalfunctionsat pages 6-9
7. scheffer2023themysteryof pages 6-7
8. scheffer2023themysteryof pages 7-9
9. scheffer2023themysteryof pages 9-10
10. scheffer2023themysteryof pages 15-16
11. tamby2023microbialmembranelipid pages 6-7
12. scheffer2023themysteryof pages 10-12
13. label-only
14. CHEBI candidate
15. CHEBI:15891 for TMAO
16. s
17. CHEBI:29985
18. CHEBI:17750
19. CHEBI:15973
20. CHEBI:15891
21. https://doi.org/10.3389/fmolb.2022.1058381
22. https://doi.org/10.3390/microorganisms11071629
23. https://doi.org/10.3390/microorganisms11071629;
24. https://doi.org/10.3389/fmicb.2024.1467153
25. https://doi.org/10.3389/fmicb.2024.1293928
26. https://doi.org/10.3389/fmicb.2024.1293928,
27. https://doi.org/10.3390/microorganisms11071629,
28. https://doi.org/10.3389/fmolb.2022.1058381,
29. https://doi.org/10.3389/fmicb.2024.1467153,