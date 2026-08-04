# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** photoautotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000656
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type characterized by the use of light as the energy source and carbon dioxide as the primary carbon source for biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** anoxygenic_photoautotrophy, anoxygenic_photoautotrophy_hydrogen_oxidation, anoxygenic_photoautotrophy_iron_oxidation, anoxygenic_photoautotrophy_sulfur_oxidation, photoautotroph, photoautotrophy
- **Existing evidence:** DOI:10.3390/life10050071: capture solar energy (Review supports cyanobacterial photoautotrophic use of solar energy and CO2 fixation.) | DOI:10.1128/AEM.02473-10: Calvin-Benson reductive pentose phosphate cycle (Review supports the Calvin-Benson cycle as a microbial autotrophic CO2-fixation pathway.) | PMID:8590279: Synechocystis sp. strain PCC6803 (Organism example: Synechocystis sp. PCC 6803 is a model photoautotrophic cyanobacterium that uses oxygenic photosynthesis to drive Calvin-Benson CO2 fixation (Kaneko et al. 1996, DNA Res, full genome).)
- **Existing causal graph summary:** photoautotrophic_cyanobacterial_carbon_fixation: 16 nodes, 12 edges

## Research Objective

Research the microbial trait **photoautotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/photoautotrophic.yaml`.

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
**Generated:** 2026-08-04T12:03:39.928908

1. kushkevych2024anoxygenicphotosynthesiswith pages 1-2
2. grettenberger2024limitingfactorsin pages 2-4
3. lucius2024theprimarycarbon pages 1-2
4. kupriyanova2023adaptingfromlow pages 1-2
5. kurkela2024inorganiccarbonsensing pages 8-8
6. mantovani2023rolesofsecond pages 1-2
7. nikeleit2024inhibitionofphototrophic pages 1-2
8. kurkela2024inorganiccarbonsensing pages 3-3
9. alarcon2024evidenceforautotrophic pages 1-2
10. conners2024thephototrophicpurple pages 1-2
11. alarcon2024evidenceforautotrophic pages 22-24
12. 10.1126/sciadv.adk7283
13. 10.1111/ppl.14140
14. 10.3389/fpls.2024.1417680
15. 10.1111/1751-7915.14519
16. 10.3389/fmicb.2024.1417714
17. 10.1128/aem.00863-24
18. 10.1038/s41561-024-01560-9
19. 10.1111/1751-7915.14552
20. 10.1093/femsml/uqad008
21. 10.3390/plants12071569
22. https://doi.org/10.1126/sciadv.adk7283
23. https://doi.org/10.1111/ppl.14140
24. https://doi.org/10.3389/fpls.2024.1417680
25. https://doi.org/10.1111/1751-7915.14519
26. https://doi.org/10.3389/fmicb.2024.1417714
27. https://doi.org/10.1128/aem.00863-24
28. https://doi.org/10.1038/s41561-024-01560-9
29. https://doi.org/10.1111/1751-7915.14552
30. https://doi.org/10.1093/femsml/uqad008
31. https://doi.org/10.3390/plants12071569
32. https://doi.org/10.3389/fmicb.2024.1417714,
33. https://doi.org/10.1093/femsml/uqad008,
34. https://doi.org/10.3389/fpls.2024.1417680,
35. https://doi.org/10.1111/1751-7915.14519,
36. https://doi.org/10.1111/ppl.14140,
37. https://doi.org/10.3390/plants12071569,
38. https://doi.org/10.1126/sciadv.adk7283,
39. https://doi.org/10.1128/aem.00863-24,
40. https://doi.org/10.1038/s41561-024-01560-9,
41. https://doi.org/10.1111/1751-7915.14552,