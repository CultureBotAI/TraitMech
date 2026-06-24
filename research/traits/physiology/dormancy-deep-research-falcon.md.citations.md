# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** dormancy
- **METPO identifier:** traitmech:000080
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A reversible physiological state of greatly reduced metabolic activity that allows a cell to survive unfavorable conditions and later resuscitate, generating a microbial seed bank.
- **Parent traits:** METPO:1000059
- **Synonyms:** dormant state
- **Existing evidence:** DOI:10.1038/nrmicro2504:  (Lennon & Jones review microbial seed banks and the mechanisms by which microorganisms enter and exit dormancy; parent of VBNC and persister sub-variants.) | DOI:10.1038/nrmicro1557:  (Lewis links dormancy to persister-cell survival and infectious disease.)
- **Existing causal graph summary:** dormancy_seed_bank: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **dormancy** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/dormancy.yaml`.

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
**Generated:** 2026-06-18T11:40:32.868388

1. yuan2024molecularmechanismand pages 3-6
2. helenabueno2024ripplinglifeon pages 1-3
3. imminger2024survivalandrapid pages 3-4
4. imminger2024survivalandrapid pages 1-2
5. imminger2024survivalandrapid pages 2-3
6. yuan2024molecularmechanismand pages 6-7
7. leinberger2024proteinaggregationis pages 1-2
8. helenabueno2024ripplinglifeon pages 11-12
9. li2024resuscitationpromotionfactor pages 1-3
10. hou2024exploringthedistribution pages 1-2
11. prosdocimi2023cellphenotypechanges pages 7-10
12. imminger2024survivalandrapid pages 7-8
13. prosdocimi2023cellphenotypechanges pages 1-2
14. fernandezgarcia2024toxinantitoxinsystemsinduce pages 13-14
15. helenabueno2024ripplinglifeon pages 3-4
16. imminger2024survivalandrapid pages 8-9
17. yang2024resuscitationofviable pages 9-10
18. yang2024resuscitationofviable pages 6-9
19. imminger2024survivalandrapid pages 11-12
20. yuan2024molecularmechanismand pages 15-16
21. helenabueno2024ripplinglifeon pages 6-8
22. yuan2024molecularmechanismand pages 7-9
23. helenabueno2024ripplinglifeon pages 8-9
24. li2024resuscitationpromotionfactor pages 3-6
25. NiFe
26. https://doi.org/10.1186/s12866-024-03628-3;
27. https://doi.org/10.3389/fmicb.2024.1386179
28. https://doi.org/10.1186/s12866-024-03628-3
29. https://doi.org/10.1038/s41467-024-46920-6;
30. https://doi.org/10.3390/microorganisms12081528
31. https://doi.org/10.1038/s41467-024-46920-6
32. https://doi.org/10.1128/msystems.01060-24;
33. https://doi.org/10.1186/s13213-022-01703-6
34. https://doi.org/10.1128/msystems.01060-24
35. https://doi.org/10.1128/spectrum.03388-23
36. https://doi.org/10.1016/j.jare.2023.08.002
37. https://doi.org/10.3389/fmicb.2024.1433046
38. https://doi.org/10.1186/s12866-024-03628-3,
39. https://doi.org/10.1186/s13213-022-01703-6,
40. https://doi.org/10.3389/fmicb.2024.1386179,
41. https://doi.org/10.1038/s41467-024-46920-6,
42. https://doi.org/10.1128/msystems.01060-24,
43. https://doi.org/10.1016/j.jare.2023.08.002,
44. https://doi.org/10.3390/microorganisms12081528,
45. https://doi.org/10.3389/fmicb.2024.1433046,
46. https://doi.org/10.1128/spectrum.03388-23,