# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** manganese oxidation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000032
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which bacteria oxidize soluble Mn(II) to insoluble Mn(III/IV) oxides, typically catalyzed by multicopper oxidases. Characteristic of organisms such as Bacillus sp. SG-1, Leptothrix, and Pseudomonas putida.
- **Parent traits:** METPO:1000060
- **Synonyms:** Mn(II) oxidation
- **Existing evidence:** DOI:10.1016/j.tim.2005.07.009:  (Tebo et al., "Geomicrobiology of manganese(II) oxidation", supports bacterial Mn(II) oxidation to Mn oxides via a multicopper-oxidase mechanism.) | DOI:10.1146/annurev.earth.32.101802.120213:  (Tebo et al., "Biogenic manganese oxides", supports the formation and properties of bacterially produced Mn(III/IV) oxides.)
- **Existing causal graph summary:** manganese_oxidation_multicopper_oxidase: 7 nodes, 7 edges

## Research Objective

Research the microbial trait **manganese oxidation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/manganese_oxidation.yaml`.

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
**Generated:** 2026-08-04T06:33:28.519475

1. wu2022manganesepollutionand pages 8-10
2. wu2022manganesepollutionand pages 7-8
3. piazza2022cyclicdigmpsignaling pages 14-15
4. novikova2024cryoemstructureof pages 1-2
5. piazza2022cyclicdigmpsignaling pages 1-2
6. soldatova2012multicopperoxidaseinvolvement pages 1-2
7. jones2024isolationcharacterizationand pages 7-11
8. tebo2004biogenicmanganeseoxides pages 1-3
9. kurdi2023aninsilicostudy pages 9-12
10. tebo2004biogenicmanganeseoxides pages 8-10
11. soldatova2012multicopperoxidaseinvolvement pages 12-16
12. jones2024isolationcharacterizationand pages 13-15
13. jones2024isolationcharacterizationand pages 11-13
14. jones2024isolationcharacterizationand pages 2-5
15. tebo2004biogenicmanganeseoxides pages 19-23
16. tebo2004biogenicmanganeseoxides pages 31-33
17. tebo2004biogenicmanganeseoxides pages 3-6
18. jones2024isolationcharacterizationand pages 1-2
19. 10.1073/pnas.1303677110
20. 10.1007/s00775-012-0928-6
21. 10.1021/jacs.3c06537
22. 10.1128/mbio.02734-22
23. s
24. 10.1128/aem.00510-24
25. 10.3390/microorganisms10122411
26. 10.1146/annurev.earth.32.101802.120213
27. taxon-specific
28. 10.21203/rs.3.rs-2451893/v1
29. https://doi.org/10.1073/pnas.1303677110
30. https://doi.org/10.1007/s00775-012-0928-6
31. https://doi.org/10.1021/jacs.3c06537
32. https://doi.org/10.1128/mbio.02734-22
33. https://doi.org/10.1128/aem.00510-24
34. https://doi.org/10.3390/microorganisms10122411
35. https://doi.org/10.1146/annurev.earth.32.101802.120213
36. https://doi.org/10.21203/rs.3.rs-2451893/v1
37. https://doi.org/10.1007/s00775-012-0928-6,
38. https://doi.org/10.1073/pnas.1303677110,
39. https://doi.org/10.1021/jacs.3c06537,
40. https://doi.org/10.1128/mbio.02734-22,
41. https://doi.org/10.1128/aem.00510-24,
42. https://doi.org/10.3390/microorganisms10122411,
43. https://doi.org/10.1146/annurev.earth.32.101802.120213,
44. https://doi.org/10.21203/rs.3.rs-2451893/v1,