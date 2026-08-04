# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemoautolithotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000634
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses chemical oxidation of inorganic compounds as the energy source and carbon dioxide as the primary carbon source for biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemoautolithotroph
- **Existing evidence:** DOI:10.1016/B978-0-12-378630-2.00219-X: oxidize inorganic atoms or molecules (Review supports inorganic compound oxidation as lithotrophic energy metabolism.) | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Minireview supports microbial carbon dioxide fixation pathways.) | DOI:10.1146/annurev.micro.55.1.485: Chemolitho-autotrophic ammonia-oxidizing bacteria (Review supports ammonia oxidation as a chemolithoautotrophic example.)
- **Existing causal graph summary:** chemoautolithotrophic_inorganic_energy_co2_fixation: 11 nodes, 12 edges

## Research Objective

Research the microbial trait **chemoautolithotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemoautolithotrophic.yaml`.

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
**Generated:** 2026-08-04T10:51:16.452711

1. taubert2022bolsteringfitnessvia pages 6-7
2. deng2023strategiesofchemolithoautotrophs pages 1-2
3. wang2024characterizethegrowth pages 1-2
4. prioretti2023carbonfixationin pages 16-17
5. mao2023anaerobicdissimilatoryphosphite pages 5-5
6. wang2024novelisolatesof pages 12-15
7. mao2023anaerobicdissimilatoryphosphite pages 4-5
8. schwander2023serpentinizationasthe pages 8-9
9. wang2024characterizethegrowth pages 22-23
10. schwander2023serpentinizationasthe pages 10-11
11. NiFe
12. 10.1111/1751-7915.14353
13. https://doi.org/10.3390/microorganisms12030590
14. https://doi.org/10.1128/msystems.00148-24
15. https://doi.org/10.1186/s40168-023-01712-w
16. https://doi.org/10.3390/life13030627
17. https://doi.org/10.1111/1462-2920.16470
18. https://doi.org/10.3389/fmicb.2023.1257597
19. https://doi.org/10.1111/1751-7915.14353
20. https://doi.org/10.1038/s41396-021-01163-x
21. https://doi.org/10.1038/s41396-023-01467-0
22. https://doi.org/10.1093/ismejo/wrae173
23. https://doi.org/10.3390/microorganisms12030590](https://doi.org/10.3390/microorganisms12030590
24. https://doi.org/10.1128/msystems.00148-24](https://doi.org/10.1128/msystems.00148-24
25. https://doi.org/10.1186/s40168-023-01712-w](https://doi.org/10.1186/s40168-023-01712-w
26. https://doi.org/10.3390/life13030627](https://doi.org/10.3390/life13030627
27. https://doi.org/10.1111/1462-2920.16470](https://doi.org/10.1111/1462-2920.16470
28. https://doi.org/10.3389/fmicb.2023.1257597](https://doi.org/10.3389/fmicb.2023.1257597
29. https://doi.org/10.1111/1751-7915.14353](https://doi.org/10.1111/1751-7915.14353
30. https://doi.org/10.1038/s41396-021-01163-x](https://doi.org/10.1038/s41396-021-01163-x
31. https://doi.org/10.1038/s41396-023-01467-0](https://doi.org/10.1038/s41396-023-01467-0
32. https://doi.org/10.1093/ismejo/wrae173](https://doi.org/10.1093/ismejo/wrae173
33. https://doi.org/10.1128/msystems.00148-24,
34. https://doi.org/10.1186/s40168-023-01712-w,
35. https://doi.org/10.1038/s41396-021-01163-x,
36. https://doi.org/10.3390/microorganisms12030590,
37. https://doi.org/10.3390/life13030627,
38. https://doi.org/10.1111/1462-2920.16470,
39. https://doi.org/10.3389/fmicb.2023.1257597,