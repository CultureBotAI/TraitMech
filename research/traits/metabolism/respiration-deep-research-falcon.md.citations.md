# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** respiration
- **METPO identifier:** METPO:1000800
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism that is characterized by the method of performing cellular respiration, distinguished primarily by the specific terminal electron acceptor utilized for producing cellular energy.
- **Parent traits:** METPO:1000060
- **Synonyms:** pathways
- **Existing evidence:** DOI:10.1016/j.bbabio.2008.09.008: membrane-bound electron transport chain (Review supports respiratory redox chains producing ion gradients and ATP.) | DOI:10.1128/mmbr.61.4.533-616.1997: oxygen as terminal electron acceptor (Review contrasts aerobic respiration with anaerobic use of alternative acceptors.)
- **Existing causal graph summary:** respiration_electron_acceptor_energy_conservation: 9 nodes, 7 edges

## Research Objective

Research the microbial trait **respiration** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/respiration.yaml`.

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
**Generated:** 2026-06-18T06:04:25.807228

1. alves2024potentialofelectrogenic pages 31-35
2. roothans2024aerobicdenitrificationas pages 1-2
3. roothans2024aerobicdenitrificationas pages 5-6
4. gupta2024mmcaisan pages 3-4
5. gupta2024mmcaisan pages 1-2
6. lacroix2023considertheanoxic pages 6-7
7. lacroix2023considertheanoxic pages 2-4
8. lacroix2023considertheanoxic pages 7-8
9. hamdan2023sedimentmicrobialfuel pages 5-6
10. roothans2024aerobicdenitrificationas pages 2-3
11. harrison2024developmentanduse pages 32-36
12. giordano2024nitricoxideand pages 8-13
13. alves2024potentialofelectrogenic pages 27-31
14. donald2023decipheringtheenergetics pages 35-40
15. roothans2024aerobicdenitrificationas pages 8-9
16. lacroix2023considertheanoxic pages 1-2
17. zhuang2024electrontransferin pages 16-18
18. hsu2024isolationandgenomic pages 17-18
19. hamdan2023sedimentmicrobialfuel pages 2-3
20. gupta2024mmcaisan pages 4-5
21. roothans2024aerobicdenitrificationas pages 6-8
22. roothans2024aerobicdenitrificationas pages 9-11
23. hamdan2023sedimentmicrobialfuel pages 10-11
24. lacroix2023considertheanoxic pages 10-11
25. lacroix2023considertheanoxic pages 11-12
26. slobodkin2023compositionandmetabolic pages 9-11
27. alves2024potentialofelectrogenic pages 57-60
28. gupta2024mmcaisan pages 2-3
29. hsu2024isolationandgenomic pages 18-18
30. donald2023decipheringtheenergetics pages 29-32
31. gupta2024mmcaisan pages 5-6
32. donald2023decipheringtheenergetics pages 147-151
33. fernandes2024structuralandfunctional pages 68-71
34. gupta2024mmcaisan pages 6-7
35. lacroix2023considertheanoxic pages 4-5
36. lacroix2023considertheanoxic pages 5-6
37. hamdan2023sedimentmicrobialfuel pages 23-24
38. zhuang2024electrontransferin pages 14-15
39. https://doi.org/10.1128/spectrum.02282-23
40. https://doi.org/10.3390/ijms252413421,
41. https://doi.org/10.1093/ismejo/wrae116,
42. https://doi.org/10.1021/acsearthspacechem.3c00032,
43. https://doi.org/10.1007/s10311-023-01625-y,
44. https://doi.org/10.1038/s41467-024-47564-2,
45. https://doi.org/10.1093/ismejo/wrae116
46. https://doi.org/10.1038/s41467-024-47564-2
47. https://doi.org/10.1021/acsearthspacechem.3c00032
48. https://doi.org/10.1007/s10311-023-01625-y
49. https://doi.org/10.3390/life14050591
50. https://doi.org/10.1007/s10533-024-01186-4
51. https://doi.org/10.1128/aem.00044-24
52. https://doi.org/10.3390/microorganisms11030555,
53. https://doi.org/10.3390/life14050591,
54. https://doi.org/10.1007/s10533-024-01186-4,
55. https://doi.org/10.1128/aem.00044-24,