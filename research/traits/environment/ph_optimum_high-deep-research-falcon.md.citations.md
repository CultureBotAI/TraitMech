# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH optimum high
- **METPO identifier:** METPO:1000458
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH optimum phenotype with the best-growth external pH above approximately 8, corresponding to alkaliphilic or extreme-alkaliphilic physiology.
- **Parent traits:** METPO:1000331
- **Synonyms:** Alkali Tolerant, Alkaliphile, Extreme Alkaliphile, pHO_8_to_14
- **Existing evidence:** DOI:10.1038/nrmicro2549: alkaliphiles (pH-homeostasis review supports alkaliphile and extreme-alkaliphile physiology growing at high external pH.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports Na+/H+ antiporters re-importing protons as the alkaliphile mechanism sustaining the proton motive force at high external pH.)
- **Existing causal graph summary:** ph_optimum_high_alkaliphile_setpoint: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **pH optimum high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_optimum_high.yaml`.

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
**Generated:** 2026-06-18T00:53:39.497965

1. adetunji2024unravelingthepotentials pages 3-4
2. kim2024lineagespecificevolutionof pages 9-12
3. mao2024enzymeengineeringperformance pages 17-18
4. xing2024thepolyextremophilenatranaerobius pages 19-21
5. xing2024thepolyextremophilenatranaerobius pages 1-2
6. brandt2015hybridrotorsin pages 4-6
7. jong2024quantitativeproteomicsreveals pages 1-2
8. adetunji2024unravelingthepotentials pages 6-7
9. pawar2023fungalalkalineproteases pages 1-2
10. zainuddin2024isolationscreeningand pages 11-15
11. hossain2023industrialenzymeproduction pages 1-2
12. hafeez2024insilicosafety pages 22-23
13. xing2024thepolyextremophilenatranaerobius pages 24-25
14. H+
15. https://doi.org/10.1128/AEM.02091-23
16. https://doi.org/10.1128/AEM.00145-24
17. https://doi.org/10.1515/hsz-2015-0137
18. https://doi.org/10.3389/fmicb.2024.1468929
19. https://doi.org/10.3390/min14090861
20. https://doi.org/10.1128/aem.00145-24
21. https://doi.org/10.1128/aem.02091-23
22. https://doi.org/10.3390/ijms25010666
23. https://doi.org/10.3389/fmicb.2023.1138401
24. https://doi.org/10.3329/ajmbr.v9i4.69395
25. https://doi.org/10.1515/gps-2023-0153
26. https://doi.org/10.3390/foods13233846
27. https://doi.org/10.3390/min14090861,
28. https://doi.org/10.1128/aem.02091-23,
29. https://doi.org/10.3390/foods13233846,
30. https://doi.org/10.1128/aem.00145-24,
31. https://doi.org/10.1515/hsz-2015-0137,
32. https://doi.org/10.3389/fmicb.2024.1468929,
33. https://doi.org/10.3389/fmicb.2023.1138401,
34. https://doi.org/10.1515/gps-2023-0153,
35. https://doi.org/10.3329/ajmbr.v9i4.69395,
36. https://doi.org/10.3390/ijms25010666,