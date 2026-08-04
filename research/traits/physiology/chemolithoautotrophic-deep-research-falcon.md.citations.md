# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemolithoautotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000637
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from oxidation of inorganic compounds (lithotrophy) and carbon from carbon dioxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemolithoautotroph
- **Existing evidence:** DOI:10.1146/annurev.micro.52.1.191: physiology ... of chemoautotrophic bacteria (Review supports chemoautotrophic bacterial CO2 fixation.) | DOI:10.1016/B978-0-12-378630-2.00219-X: growth-supporting reductant and energy source (Review supports inorganic reductants as energy sources for chemolithotrophic growth.)
- **Existing causal graph summary:** chemolithoautotrophic_energy_and_fixation: 13 nodes, 14 edges

## Research Objective

Research the microbial trait **chemolithoautotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemolithoautotrophic.yaml`.

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
**Generated:** 2026-08-04T10:56:33.840889

1. tu2023engineeringartificialphotosynthesis pages 1-2
2. wang2024characterizethegrowth pages 22-23
3. wang2024characterizethegrowth pages 1-2
4. ghimirekafle2024competitionbetweenammoniaoxidizing pages 1-2
5. scott2024widespreaddissolvedinorganic pages 2-4
6. prioretti2023carbonfixationin pages 1-2
7. mao2023anaerobicdissimilatoryphosphite pages 1-2
8. deng2023strategiesofchemolithoautotrophs pages 1-2
9. wright2023nitrificationandbeyond pages 1-2
10. laufermeiser2024oxidationofsulfur pages 9-10
11. scott2024widespreaddissolvedinorganic pages 10-13
12. bris2019hydrothermalenergytransfer pages 5-6
13. scott2024widespreaddissolvedinorganic pages 4-7
14. scott2024widespreaddissolvedinorganic pages 15-18
15. prioretti2023carbonfixationin pages 14-16
16. scott2024widespreaddissolvedinorganic pages 18-19
17. 4Fe–4S
18. is
19. https://doi.org/10.1128/aem.01557-23
20. https://doi.org/10.1093/ismejo/wrae173
21. https://doi.org/10.3390/microorganisms12030590
22. https://doi.org/10.1128/aem.01698-23
23. https://doi.org/10.1186/s40168-023-01712-w
24. https://doi.org/10.3390/life13030627
25. https://doi.org/10.1038/s41396-023-01467-0
26. https://doi.org/10.1111/1462-2920.16470
27. https://doi.org/10.1111/1751-7915.14353
28. https://doi.org/10.1038/s41467-023-43524-4
29. https://doi.org/10.3389/fmars.2018.00531
30. https://doi.org/10.1128/aem.01557-23,
31. https://doi.org/10.3390/life13030627,
32. https://doi.org/10.1111/1462-2920.16470,
33. https://doi.org/10.1038/s41467-023-43524-4,
34. https://doi.org/10.3390/microorganisms12030590,
35. https://doi.org/10.1111/1751-7915.14353,
36. https://doi.org/10.1128/aem.01698-23,
37. https://doi.org/10.1186/s40168-023-01712-w,
38. https://doi.org/10.1038/s41396-023-01467-0,
39. https://doi.org/10.1093/ismejo/wrae173,
40. https://doi.org/10.3389/fmars.2018.00531,