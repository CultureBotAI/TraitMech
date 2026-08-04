# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Electron transfer
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000805
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which electrons are transferred from an electron donor to an electron acceptor.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/j.bbabio.2008.09.008: electron transfer process (Review supports electron donor-to-acceptor flow in membrane respiratory chains.) | DOI:10.1038/nrmicro.2016.93: c-type cytochromes and microbial nanowires (Review supports extracellular electron-transfer mechanisms.)
- **Existing causal graph summary:** electron_transfer_redox_carriers: 17 nodes, 13 edges

## Research Objective

Research the microbial trait **Electron transfer** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/electron_transfer.yaml`.

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
**Generated:** 2026-08-04T06:25:15.012543

1. edwards2020roleofmultiheme pages 1-2
2. buckel2018flavinbasedelectronbifurcation pages 1-2
3. zhong2018genomicanalysesof pages 1-2
4. burton2025electrontransportacross pages 3-4
5. borisov2021bacterialoxidasesof pages 1-2
6. xie2021themechanismand pages 12-14
7. gu2023structureofgeobacter pages 6-8
8. jiang2023thevariedroles pages 1-2
9. almegbl2024biogasenhancementin pages 1-2
10. ma2024synergisticpromotionof pages 1-2
11. portela2024widespreadextracellularelectron pages 7-9
12. gu2023structureofgeobacter pages 1-2
13. wang2024electrocatalyticnanomaterialsimprove pages 1-2
14. jiang2023thevariedroles pages 5-8
15. portela2024widespreadextracellularelectron pages 1-2
16. gu2023structureofgeobacter pages 29-30
17. shaw2025independentlyevolvedextracellular pages 1-2
18. shaw2025independentlyevolvedextracellular pages 12-14
19. shaw2025independentlyevolvedextracellular pages 14-15
20. https://doi.org/10.1038/s41564-022-01315-5.
21. https://doi.org/10.3389/fmicb.2023.1251346.
22. https://doi.org/10.1038/s41467-024-46192-0.
23. https://doi.org/10.3390/app14156733.
24. https://doi.org/10.3389/fceng.2024.1419770.
25. https://doi.org/10.3390/fermentation10120656.
26. https://doi.org/10.1089/ars.2020.8039.
27. https://doi.org/10.1002/pro.3787.
28. https://doi.org/10.3389/fmicb.2018.03029.
29. https://doi.org/10.1021/acs.chemrev.7b00707.
30. https://doi.org/10.1038/nrmicro.2016.93.
31. https://doi.org/10.1080/10643389.2020.1773728.
32. https://doi.org/10.1002/pro.3787,
33. https://doi.org/10.1021/acs.chemrev.7b00707,
34. https://doi.org/10.3389/fmicb.2018.03029,
35. https://doi.org/10.1146/annurev-biochem-052621-092202,
36. https://doi.org/10.1089/ars.2020.8039,
37. https://doi.org/10.1080/10643389.2020.1773728,
38. https://doi.org/10.1038/s41467-024-46192-0,
39. https://doi.org/10.1038/s41564-022-01315-5,
40. https://doi.org/10.3389/fmicb.2023.1251346,
41. https://doi.org/10.3389/fceng.2024.1419770,
42. https://doi.org/10.3390/fermentation10120656,
43. https://doi.org/10.1093/ismejo/wraf097,
44. https://doi.org/10.3390/app14156733,