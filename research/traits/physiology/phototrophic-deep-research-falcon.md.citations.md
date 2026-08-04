# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** phototrophic
- **METPO identifier:** METPO:1000660
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type characterized by the use of light as the primary energy source for metabolic processes, regardless of carbon source.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_phototroph, aerobic_anoxygenic_phototrophy, phototroph
- **Existing evidence:** DOI:10.3389/fmicb.2011.00165: use light as the energy source (Review supports light-driven ATP and reductant generation by phototrophic bacteria.) | DOI:10.1093/femsre/fuv032: bacteriochlorophyll-containing reaction centers (Review supports bacteriochlorophyll reaction centers in aerobic anoxygenic phototrophs.)
- **Existing causal graph summary:** phototrophic_light_energy_capture: 13 nodes, 12 edges

## Research Objective

Research the microbial trait **phototrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/phototrophic.yaml`.

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
**Generated:** 2026-06-29T14:15:46.669632

1. peterson2023usinglightfor pages 1-5
2. yurkov2025phenomenaldiversityof pages 1-3
3. nishihara2024illuminatingthecoevolution pages 9-9
4. yurkov2025phenomenaldiversityof pages 3-5
5. niederman2024whatweare pages 1-2
6. niederman2024whatweare pages 22-23
7. yurkov2025phenomenaldiversityof pages 21-23
8. yurkov2025phenomenaldiversityof pages 10-12
9. yurkov2025phenomenaldiversityof pages 12-14
10. blankenship2021molecularmechanismsof pages 114-117
11. nishihara2024illuminatingthecoevolution pages 8-9
12. yurkov2025phenomenaldiversityof pages 14-15
13. xie2023cryoemstructureof pages 1-2
14. tinguely2023diurnalcyclesdrive pages 5-8
15. yurkov2025phenomenaldiversityof pages 16-18
16. yurkov2025phenomenaldiversityof pages 18-19
17. peterson2023usinglightfor pages 11-15
18. yurkov2025phenomenaldiversityof pages 19-21
19. yurkov2025phenomenaldiversityof pages 23-24
20. yurkov2025phenomenaldiversityof pages 28-29
21. nishihara2024illuminatingthecoevolution pages 2-3
22. niederman2024whatweare pages 19-20
23. tinguely2023diurnalcyclesdrive pages 1-2
24. yurkov2025phenomenaldiversityof pages 27-28
25. niederman2024whatweare pages 9-11
26. niedzwiedzki2025tripletstatedynamicsof pages 1-2
27. niederman2024whatweare pages 5-7
28. blankenship2021molecularmechanismsof pages 145-148
29. tinguely2023diurnalcyclesdrive pages 9-10
30. Microbial Phototrophy Causal Graph
31. 4Fe-4S
32. https://doi.org/10.1101/2022.12.06.519405,
33. https://doi.org/10.1073/pnas.2322120121,
34. https://doi.org/10.3390/biom14030311,
35. https://doi.org/10.3390/microorganisms13112446,
36. https://doi.org/10.1038/s43705-023-00334-5,
37. https://doi.org/10.1021/acs.jpcb.5c00394,
38. https://doi.org/10.1073/pnas.2216734120,
39. https://doi.org/10.1002/9780470758472,