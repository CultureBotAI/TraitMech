# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** nitrogen-fixing symbiosis
- **METPO identifier:** traitmech:000044
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A mutualistic symbiosis in which a diazotrophic bacterium fixes atmospheric N2 for a host plant — classically rhizobia in legume root nodules — in exchange for photosynthate.
- **Parent traits:** traitmech:000041
- **Synonyms:** nitrogen-fixing symbiont, root-nodule symbiosis
- **Existing evidence:** DOI:10.1038/nrmicro.2017.171:  (Poole et al. describe the free-living-to-endosymbiont transition of rhizobia that forms N2-fixing legume root nodules.) | DOI:10.1038/nrmicro2990:  (Oldroyd, "Speak, friend, and enter", supports the symbiotic signalling that establishes beneficial nitrogen-fixing plant-microbe associations.)
- **Existing causal graph summary:** rhizobia_legume_n2_fixation: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **nitrogen-fixing symbiosis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/nitrogen_fixing_symbiosis.yaml`.

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
**Generated:** 2026-06-17T20:47:10.006364

1. zhang2023widelyconservedahl pages 1-2
2. isidraarellano2024understandingthecrucial pages 1-2
3. porter2024hostimposedcontrolmechanisms pages 1-3
4. libourel2023comparativephylotranscriptomicsreveals pages 1-2
5. udvardi2024geneticsandgenomics pages 5-7
6. sexauer2024rootnodulesymbiosis pages 27-30
7. li2024metalnutritionand pages 5-6
8. sexauer2024totheroots pages 27-30
9. lamoureux2024theeffectof pages 23-26
10. sexauer2024rootnodulesymbiosis pages 24-27
11. lamoureux2024theeffectof pages 15-19
12. zhou2024inorganicnitrogeninhibits pages 1-2
13. zhang2023widelyconservedahl pages 2-3
14. udvardi2024geneticsandgenomics pages 7-10
15. libourel2023comparativephylotranscriptomicsreveals pages 5-6
16. sexauer2024rootnodulesymbiosis pages 182-187
17. sexauer2024totheroots pages 182-187
18. lamoureux2024theeffectof pages 29-32
19. patil2024identificationandcharacterization pages 14-18
20. patil2024identificationandcharacterization pages 18-22
21. patil2024identificationandcharacterization pages 35-41
22. lamoureux2024theeffectof pages 19-23
23. https://doi.org/10.3389/fpls.2023.1284720
24. https://doi.org/10.1093/pcp/pcae128
25. https://doi.org/10.1038/s41564-024-01762-2
26. https://doi.org/10.1017/S1062798724000309
27. https://doi.org/10.1038/s41467-024-53325-y
28. https://doi.org/10.1038/s41477-022-01326-4
29. https://doi.org/10.1038/s41477-023-01441-w
30. https://doi.org/10.1016/j.xplc.2024.100829
31. https://doi.org/10.1038/s41564-024-01762-2,
32. https://doi.org/10.1017/s1062798724000309,
33. https://doi.org/10.1038/s41477-022-01326-4,
34. https://doi.org/10.3389/fpls.2023.1284720,
35. https://doi.org/10.1093/pcp/pcae128,
36. https://doi.org/10.1038/s41467-024-53325-y,
37. https://doi.org/10.1038/s41477-023-01441-w,
38. https://doi.org/10.1016/j.xplc.2024.100829,