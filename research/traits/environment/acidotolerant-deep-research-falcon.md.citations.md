# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** acidotolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003008
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference characterized by the ability to tolerate acidic environments (typically pH below 5.5) while maintaining optimal growth near neutral pH.
- **Parent traits:** METPO:1003000
- **Synonyms:** aciduric
- **Existing evidence:** DOI:10.1038/nrmicro2549: tolerate and grow at external pH values (Supports acidotolerance as growth or survival under otherwise stressful external pH conditions.)
- **Existing causal graph summary:** acidotolerant_acid_stress_homeostasis: 9 nodes, 9 edges

## Research Objective

Research the microbial trait **acidotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/acidotolerant.yaml`.

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
**Generated:** 2026-08-04T00:00:12.633084

1. rebelo2023unravelingtherole pages 18-20
2. lund2014copingwithlow pages 1-2
3. schumacher2023ribosomeprofilingreveals pages 1-2
4. liu2023molecularmechanismof pages 12-15
5. liu2023molecularmechanismof pages 9-12
6. li2024responseofescherichia pages 5-7
7. schumacher2023ribosomeprofilingreveals pages 21-23
8. gao2024theeffectof pages 13-14
9. yan2024engineeringquorumsensingbased pages 10-10
10. cotter2003survivingtheacid pages 13-14
11. lund2014copingwithlow pages 6-6
12. li2024responseofescherichia pages 12-12
13. 10.3390/microorganisms12091774
14. 10.3390/foods13101533
15. 10.1186/s12934-024-02524-9
16. 10.1186/s12934-024-02565-0
17. 10.1128/msystems.01037-23
18. 10.1128/spectrum.00022-23
19. 10.1101/2023.07.13.548807
20. 10.1016/j.lwt.2024.115760
21. 10.3390/antibiotics12091474
22. 10.1111/1574-6976.12076
23. 10.1038/nrmicro2549
24. 10.1111/mmi.12020
25. 10.1128/MMBR.67.3.429-453.2003
26. https://doi.org/10.3390/microorganisms12091774
27. https://doi.org/10.3390/foods13101533
28. https://doi.org/10.1186/s12934-024-02524-9
29. https://doi.org/10.1186/s12934-024-02565-0
30. https://doi.org/10.1128/msystems.01037-23
31. https://doi.org/10.1128/spectrum.00022-23
32. https://doi.org/10.1101/2023.07.13.548807
33. https://doi.org/10.1016/j.lwt.2024.115760
34. https://doi.org/10.3390/antibiotics12091474
35. https://doi.org/10.1111/1574-6976.12076
36. https://doi.org/10.1038/nrmicro2549
37. https://doi.org/10.1111/mmi.12020
38. https://doi.org/10.1128/MMBR.67.3.429-453.2003
39. https://doi.org/10.3390/antibiotics12091474,
40. https://doi.org/10.1111/1574-6976.12076,
41. https://doi.org/10.1101/2023.07.13.548807,
42. https://doi.org/10.3390/foods13101533,
43. https://doi.org/10.1128/msystems.01037-23,
44. https://doi.org/10.3390/microorganisms12091774,
45. https://doi.org/10.1186/s12934-024-02524-9,
46. https://doi.org/10.1128/mmbr.67.3.429-453.2003,