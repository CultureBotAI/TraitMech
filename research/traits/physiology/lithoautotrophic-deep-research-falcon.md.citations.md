# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** lithoautotrophic
- **METPO identifier:** METPO:1000647
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from inorganic electron donors and carbon from carbon dioxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** lithoautotroph
- **Existing evidence:** DOI:10.1016/B978-0-12-378630-2.00219-X: inorganic atoms or molecules (Review supports inorganic compounds as reductants for lithotrophic growth.) | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Review supports CO2 fixation as the autotrophic carbon-assimilation process.)
- **Existing causal graph summary:** lithoautotrophic_inorganic_donor_co2_fixation: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **lithoautotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/lithoautotrophic.yaml`.

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
**Generated:** 2026-06-18T11:46:23.971861

1. jahn2024theenergymetabolism pages 1-2
2. seah2019sulfuroxidizingsymbiontswithout pages 2-4
3. gupta2020extracellularelectronuptake pages 4-5
4. scott2024widespreaddissolvedinorganic pages 1-2
5. prioretti2023carbonfixationin pages 1-2
6. seah2019sulfuroxidizingsymbiontswithout pages 16-16
7. gupta2020extracellularelectronuptake pages 8-9
8. twible2024phandthiosulfate pages 1-2
9. zhang2024accumulatedcoppertailing pages 1-2
10. cozma2024biorecoveryofmetals pages 22-24
11. nastro2025bioelectrosynthesisofpolyhydroxybutyrate pages 1-2
12. mura2024experimentalsimulationof pages 1-2
13. gupta2020extracellularelectronuptake pages 5-6
14. gupta2020extracellularelectronuptake pages 1-2
15. S2O32−
16. https://doi.org/10.1128/aem.00748-24
17. https://doi.org/10.1007/s10295-020-02309-0
18. https://doi.org/10.3390/life13030627
19. https://doi.org/10.1128/aem.01557-23
20. https://doi.org/10.1038/s41467-023-37426-8
21. https://doi.org/10.3389/fmicb.2024.1426584
22. https://doi.org/10.1128/mbio.01112-19
23. https://doi.org/10.3389/fmicb.2024.1439866
24. https://doi.org/10.3390/min14101051
25. https://doi.org/10.3390/pr12091793
26. https://doi.org/10.3389/fmicb.2025.1372302
27. https://doi.org/10.1128/aem.00748-24,
28. https://doi.org/10.1128/aem.01557-23,
29. https://doi.org/10.1128/mbio.01112-19,
30. https://doi.org/10.1007/s10295-020-02309-0,
31. https://doi.org/10.3390/life13030627,
32. https://doi.org/10.1038/s41467-023-37426-8,
33. https://doi.org/10.3390/microorganisms11061436,
34. https://doi.org/10.3389/fmicb.2024.1426584,
35. https://doi.org/10.3390/min14101051,
36. https://doi.org/10.3390/pr12091793,
37. https://doi.org/10.3389/fmicb.2025.1372302,
38. https://doi.org/10.3389/fmicb.2024.1439866,