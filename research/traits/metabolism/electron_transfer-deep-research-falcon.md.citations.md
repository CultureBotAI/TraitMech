# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Electron transfer
- **METPO identifier:** METPO:1000805
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which electrons are transferred from an electron donor to an electron acceptor.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/j.bbabio.2008.09.008: electron transfer process (Review supports electron donor-to-acceptor flow in membrane respiratory chains.) | DOI:10.1038/nrmicro.2016.93: c-type cytochromes and microbial nanowires (Review supports extracellular electron-transfer mechanisms.)
- **Existing causal graph summary:** electron_transfer_redox_carriers: 9 nodes, 7 edges

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
**Generated:** 2026-06-18T05:11:04.420004

1. ford2024theelectrontransport pages 1-2
2. hazzan2023strategiesforenhancing pages 2-3
3. zhuang2024electrontransferin pages 10-11
4. trani2023structureofthe pages 1-2
5. ford2024theelectrontransport pages 2-5
6. baquero2023extracellularcytochromenanowires pages 10-11
7. uriberamirez2024modificationsofthe pages 11-12
8. mouhib2023engineeringextracellularelectron pages 20-23
9. hou2024biologicalandchemical pages 1-2
10. donald2023decipheringtheenergetics pages 35-40
11. mouhib2023engineeringextracellularelectron pages 72-74
12. mouhib2023engineeringextracellularelectron pages 17-20
13. giordano2024nitricoxideand pages 8-13
14. walters2024spectroscopicinvestigationsof pages 21-25
15. mouhib2023engineeringextracellularelectron pages 74-77
16. mouhib2023engineeringextracellularelectron pages 44-48
17. s
18. terminal oxidases
19. involve
20. https://doi.org/10.1038/s41522-024-00490-z
21. https://doi.org/10.3390/ijms252413421
22. https://doi.org/10.1073/pnas.2307093120
23. https://doi.org/10.1007/s10863-024-10041-y
24. https://doi.org/10.1128/aem.01387-23
25. https://doi.org/10.1016/j.cell.2023.05.012
26. https://doi.org/10.3390/microorganisms12122454
27. https://doi.org/10.3390/life14050591
28. https://doi.org/10.3390/app132312760
29. https://doi.org/10.1128/aem.01387-23,
30. https://doi.org/10.1073/pnas.2307093120,
31. https://doi.org/10.3390/app132312760,
32. https://doi.org/10.3390/life14050591,
33. https://doi.org/10.3390/ijms252413421,
34. https://doi.org/10.1016/j.cell.2023.05.012,
35. https://doi.org/10.1007/s10863-024-10041-y,
36. https://doi.org/10.5075/epfl-thesis-10049,
37. https://doi.org/10.3390/microorganisms12122454,