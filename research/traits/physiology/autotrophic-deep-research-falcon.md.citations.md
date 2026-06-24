# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** autotrophic
- **METPO identifier:** METPO:1000632
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism produces organic compounds from inorganic carbon sources (primarily carbon dioxide or bicarbonate) using energy from light (photoautotrophy) or from the oxidation of inorganic compounds (chemoautotrophy).
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_autotroph, autotroph, autotrophy
- **Existing evidence:** DOI:10.1038/nrmicro.2016.130: require only CO2 as a carbon source (Review defines autotrophic organisms by CO2 use as carbon source for growth.) | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Minireview supports Calvin-Benson and other microbial CO2-fixation pathways.) | PMID:8590279: Synechocystis sp. strain PCC6803 (Organism example: Synechocystis sp. PCC 6803 is a model autotrophic cyanobacterium that fixes CO2 via the Calvin-Benson cycle (Kaneko et al. 1996, DNA Res, full genome).)
- **Existing causal graph summary:** autotrophic_inorganic_carbon_fixation: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **autotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/autotrophic.yaml`.

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
**Generated:** 2026-06-18T10:54:38.209487

1. li2024productionofsuccinate pages 1-2
2. ray2023clearingtheair pages 2-4
3. scott2024widespreaddissolvedinorganic pages 7-10
4. kurkela2024inorganiccarbonsensing pages 1-2
5. scott2024widespreaddissolvedinorganic pages 2-4
6. gruterich2024metagenomicandmetatranscriptomic pages 21-23
7. wieschollek2024anewtype pages 1-2
8. bae2024harnessingacetogenicbacteria pages 1-2
9. moon2024redirectingelectronflow pages 1-2
10. bae2024harnessingacetogenicbacteria pages 10-12
11. liao2023microbialautotrophyexplains pages 9-10
12. liao2023microbialautotrophyexplains pages 6-7
13. lucius2024theprimarycarbon pages 1-2
14. wang2023microbialconversionand pages 7-8
15. scott2024widespreaddissolvedinorganic pages 1-2
16. label-only context
17. family iota-CA label-only
18. iota-CA label-only
19. label if exact CURIE unavailable
20. https://doi.org/10.1128/AEM.01557-23
21. https://doi.org/10.1111/ppl.14140
22. https://doi.org/10.1128/AEM.01075-24
23. https://doi.org/10.1039/D4CB00099D
24. https://doi.org/10.1038/s41467-024-49680-5
25. https://doi.org/10.1128/MMBR.00048-23
26. https://doi.org/10.1111/GCB.16452
27. https://doi.org/10.1186/S12934-024-02470-6
28. https://doi.org/10.1128/aem.01557-23
29. https://doi.org/10.1128/aem.01075-24
30. https://doi.org/10.1128/mmbr.00048-23
31. https://doi.org/10.1039/d4cb00099d
32. https://doi.org/10.1111/gcb.16452
33. https://doi.org/10.1186/s12934-024-02470-6
34. https://doi.org/10.3389/fpls.2024.1417680
35. https://doi.org/10.29328/journal.acee.1001055
36. https://doi.org/10.29328/journal.acee.1001055,
37. https://doi.org/10.1128/aem.01557-23,
38. https://doi.org/10.1186/s12934-024-02470-6,
39. https://doi.org/10.1128/mmbr.00048-23,
40. https://doi.org/10.1111/ppl.14140,
41. https://doi.org/10.1128/aem.01075-24,
42. https://doi.org/10.1039/d4cb00099d,
43. https://doi.org/10.1038/s41467-024-49680-5,
44. https://doi.org/10.1111/gcb.16452,
45. https://doi.org/10.3389/fpls.2024.1417680,