# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** antibiotic resistance
- **METPO identifier:** traitmech:000088
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A physiological capacity to grow in the presence of antibiotic concentrations that inhibit susceptible cells, mediated by efflux, target modification, drug inactivation, or reduced permeability.
- **Parent traits:** METPO:1000059
- **Synonyms:** antimicrobial resistance
- **Existing evidence:** DOI:10.1038/nrmicro3380:  (Blair et al. review the molecular mechanisms of antibiotic resistance (efflux, target alteration, drug inactivation, reduced uptake).) | DOI:10.1038/s41579-022-00820-y:  (Updated review revisits molecular mechanisms of antibiotic resistance.)
- **Existing causal graph summary:** antibiotic_resistance_mechanisms: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **antibiotic resistance** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/antibiotic_resistance.yaml`.

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
**Generated:** 2026-06-18T10:52:38.077436

1. bollen2023environmentalmechanisticand pages 1-2
2. zhang2024bacterialeffluxpump pages 2-4
3. chiang2024effluxpumpmediatedresistance pages 1-2
4. belay2024mechanismofantibacterial pages 3-4
5. mendelson2024ensuringprogresson pages 1-4
6. klein2024globaltrendsin pages 1-2
7. klein2024globaltrendsin pages 6-7
8. marino2025theglobalburden pages 13-14
9. zhang2024bacterialeffluxpump pages 1-2
10. naghavi2024globalburdenof pages 1-2
11. zhao2024multidrugresistancein pages 1-2
12. galgano2025acquiredbacterialresistance pages 7-8
13. singha2024alternativetherapeuticsto pages 3-4
14. bollen2023environmentalmechanisticand pages 2-3
15. marino2025theglobalburden pages 11-13
16. s
17. https://doi.org/10.3390/pharmaceutics16020170
18. https://doi.org/10.3390/pharmaceutics16020170;
19. https://doi.org/10.1038/s43856-024-00591-y
20. https://doi.org/10.1038/s43856-024-00591-y;
21. https://doi.org/10.3389/fddsv.2024.1385460
22. https://doi.org/10.3389/fphar.2024.1444781
23. https://doi.org/10.3390/antibiotics14030222
24. https://doi.org/10.1186/s43556-024-00221-y
25. https://doi.org/10.1093/femsml/uqad009
26. https://doi.org/10.15252/embr.202357309
27. https://doi.org/10.1016/S0140-6736(24
28. https://doi.org/10.1073/pnas.2411919121
29. https://doi.org/10.3390/epidemiologia6020021
30. https://doi.org/10.3389/fphar.2024.1444781,
31. https://doi.org/10.1038/s43856-024-00591-y,
32. https://doi.org/10.1093/femsml/uqad009,
33. https://doi.org/10.15252/embr.202357309,
34. https://doi.org/10.3390/pharmaceutics16020170,
35. https://doi.org/10.1186/s43556-024-00221-y,
36. https://doi.org/10.1016/s0140-6736(24
37. https://doi.org/10.1073/pnas.2411919121,
38. https://doi.org/10.3390/epidemiologia6020021,
39. https://doi.org/10.3390/antibiotics14030222,
40. https://doi.org/10.3389/fddsv.2024.1385460,