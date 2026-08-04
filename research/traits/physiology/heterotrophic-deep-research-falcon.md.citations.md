# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** heterotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000644
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains carbon from organic compounds rather than from carbon dioxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_heterotroph, aerobic_heterotrophy, heterotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: organic compounds as the primary sources of carbon (Encyclopedia chapter supports organic compounds as heterotrophic carbon sources.) | DOI:10.1021/acsomega.3c02205: organic molecules ... carbon source (Review table supports organic molecules as carbon sources in heterotrophic growth modes.) | PMID:9278503: Escherichia coli K-12 (Organism example: Escherichia coli K-12 (MG1655) is the canonical chemoorganoheterotrophic model bacterium that grows on diverse organic substrates (Blattner et al. 1997, Science, complete genome).)
- **Existing causal graph summary:** heterotrophic_organic_carbon_assimilation: 12 nodes, 12 edges

## Research Objective

Research the microbial trait **heterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/heterotrophic.yaml`.

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
**Generated:** 2026-08-04T11:17:50.568286

1. braun2021reviewsandsyntheses pages 1-2
2. carreonrodriguez2023glucosetransportin pages 5-7
3. zhang2024metagenomiccharacterizationof pages 8-11
4. zhang2024metagenomiccharacterizationof pages 1-2
5. carreonrodriguez2023glucosetransportin pages 1-2
6. carreonrodriguez2023glucosetransportin pages 3-4
7. tothero2024leptothrixochraceagenomes pages 13-15
8. tothero2024leptothrixochraceagenomes pages 9-13
9. dong2019metabolicpotentialof pages 4-5
10. tothero2024leptothrixochraceagenomes pages 1-2
11. stegemuller2024synergisticeffectsof pages 1-2
12. yan2024carbonandenergy pages 8-9
13. tocca2024mixotrophicandheterotrophic pages 1-2
14. tocca2024mixotrophicandheterotrophic pages 7-9
15. 10.1186/s40168-023-01728-2
16. 10.3390/microorganisms11061588
17. 10.1128/aem.00599-24
18. 10.3389/fmicb.2023.1049579
19. 10.1038/s41467-019-09747-0
20. 10.5194/bg-18-3689-2021
21. 10.3389/fbioe.2023.1296216
22. 10.1007/s11157-024-09682-7
23. 10.1007/s10811-024-03322-x
24. 10.3389/fmicb.2024.1436264
25. 10.1007/s11306-017-1302-z
26. https://doi.org/10.1186/s40168-023-01728-2
27. https://doi.org/10.3390/microorganisms11061588
28. https://doi.org/10.1128/aem.00599-24
29. https://doi.org/10.3389/fmicb.2023.1049579
30. https://doi.org/10.1038/s41467-019-09747-0
31. https://doi.org/10.5194/bg-18-3689-2021
32. https://doi.org/10.3389/fbioe.2023.1296216
33. https://doi.org/10.1007/s11157-024-09682-7
34. https://doi.org/10.1007/s10811-024-03322-x
35. https://doi.org/10.3389/fmicb.2024.1436264
36. https://doi.org/10.1007/s11306-017-1302-z
37. https://doi.org/10.5194/bg-18-3689-2021,
38. https://doi.org/10.1128/aem.00599-24,
39. https://doi.org/10.1007/s11306-017-1302-z,
40. https://doi.org/10.3389/fbioe.2023.1296216,
41. https://doi.org/10.1186/s40168-023-01728-2,
42. https://doi.org/10.3389/fmicb.2023.1049579,
43. https://doi.org/10.3390/microorganisms11061588,
44. https://doi.org/10.1038/s41467-019-09747-0,
45. https://doi.org/10.1007/s10811-024-03322-x,
46. https://doi.org/10.1007/s11157-024-09682-7,
47. https://doi.org/10.3389/fmicb.2024.1436264,