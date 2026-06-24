# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemoheterotrophic
- **METPO identifier:** METPO:1000636
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains both energy and carbon from organic compounds.
- **Parent traits:** METPO:1000631
- **Synonyms:** aerobic_chemo_heterotrophy, chemoheterotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: Chemoheterotroph (chemoorganoheterotroph) (Encyclopedia chapter maps chemoheterotrophy to chemical energy and reduced organic carbon.) | DOI:10.1021/acsomega.3c02205: chemoheterotrophic (Review table supports chemoheterotrophic use of organic molecules as energy and carbon sources.)
- **Existing causal graph summary:** chemoheterotrophic_organic_energy_carbon: 8 nodes, 9 edges

## Research Objective

Research the microbial trait **chemoheterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemoheterotrophic.yaml`.

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
**Generated:** 2026-06-18T11:16:34.651188

1. stebegg2023heterotrophyamongcyanobacteria pages 1-2
2. stebegg2023heterotrophyamongcyanobacteria pages 2-4
3. stebegg2023heterotrophyamongcyanobacteria pages 2-2
4. stebegg2023heterotrophyamongcyanobacteria pages 10-11
5. rakitin2024verrucomicrobiaofthe pages 10-12
6. muramatsu2024nutrientacquisitionstrategies pages 1-2
7. rakitin2024verrucomicrobiaofthe pages 9-10
8. muramatsu2024nutrientacquisitionstrategies pages 2-4
9. stebegg2023heterotrophyamongcyanobacteria pages 9-10
10. su2024genomiccharacterizationof pages 10-12
11. su2024genomiccharacterizationof pages 1-3
12. smorada2024bacterialdegradationof pages 1-3
13. javourez2024ruminationsonsustainable pages 1-2
14. parsons2023suboxicdomis pages 1-2
15. parsons2023suboxicdomis pages 2-3
16. stebegg2023heterotrophyamongcyanobacteria pages 13-14
17. su2024genomiccharacterizationof pages 17-17
18. https://doi.org/10.1021/acsomega.3c02205
19. https://doi.org/10.3390/microorganisms12112271
20. https://doi.org/10.3390/microorganisms12112271;
21. https://doi.org/10.1128/mbio.00992-24
22. https://doi.org/10.1016/j.chom.2024.05.011
23. https://doi.org/10.3389/fmicb.2023.1287477
24. https://doi.org/10.1016/j.copbio.2024.103170
25. https://doi.org/10.1111/1751-7915.14436
26. https://doi.org/10.1021/acsomega.3c02205,
27. https://doi.org/10.3390/microorganisms12112271,
28. https://doi.org/10.1016/j.chom.2024.05.011,
29. https://doi.org/10.1128/mbio.00992-24,
30. https://doi.org/10.3389/fmicb.2023.1287477,
31. https://doi.org/10.1016/j.copbio.2024.103170,
32. https://doi.org/10.1111/1751-7915.14436,