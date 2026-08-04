# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** lithoautotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000647
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from inorganic electron donors and carbon from carbon dioxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** lithoautotroph
- **Existing evidence:** DOI:10.1016/B978-0-12-378630-2.00219-X: inorganic atoms or molecules (Review supports inorganic compounds as reductants for lithotrophic growth.) | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Review supports CO2 fixation as the autotrophic carbon-assimilation process.)
- **Existing causal graph summary:** lithoautotrophic_inorganic_donor_co2_fixation: 15 nodes, 12 edges

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
**Generated:** 2026-08-04T11:22:06.139541

1. guzman2019phototrophicextracellularelectron pages 12-12
2. pillot2023sparkoflife pages 9-11
3. gupta2020extracellularelectronuptake pages 8-9
4. jahn2024theenergymetabolism pages 1-2
5. laufermeiser2024oxidationofsulfur pages 6-8
6. laufermeiser2024oxidationofsulfur pages 8-9
7. laufermeiser2024oxidationofsulfur pages 1-2
8. laufermeiser2024oxidationofsulfur pages 3-4
9. wang2024novelisolatesof pages 12-15
10. wang2024novelisolatesof pages 7-9
11. gupta2020extracellularelectronuptake pages 9-10
12. laufermeiser2024oxidationofsulfur pages 4-6
13. laufermeiser2024oxidationofsulfur pages 9-10
14. NiFe
15. 10.1007/s10295-020-02309-0
16. 10.1128/aem.00748-24
17. 10.1093/ismejo/wrae173
18. 10.1128/msystems.00148-24
19. 10.3390/life13020356
20. 10.1038/s41467-019-09377-6
21. https://doi.org/10.1007/s10295-020-02309-0
22. https://doi.org/10.1128/aem.00748-24
23. https://doi.org/10.1093/ismejo/wrae173
24. https://doi.org/10.1128/msystems.00148-24
25. https://doi.org/10.3390/life13020356
26. https://doi.org/10.1038/s41467-019-09377-6
27. https://doi.org/10.1038/s41467-019-09377-6,
28. https://doi.org/10.3390/life13020356,
29. https://doi.org/10.1007/s10295-020-02309-0,
30. https://doi.org/10.1093/ismejo/wrae173,
31. https://doi.org/10.1128/aem.00748-24,
32. https://doi.org/10.1128/msystems.00148-24,