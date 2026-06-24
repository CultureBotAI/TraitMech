# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** photolithoautotrophic
- **METPO identifier:** METPO:1000665
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from light and carbon from carbon dioxide using inorganic electron donors.
- **Parent traits:** METPO:1000631
- **Synonyms:** photolithoautotroph
- **Existing evidence:** DOI:10.3389/fmicb.2011.00165: oxidize sulfide (Review supports sulfide oxidation coupled to phototrophic central carbon and energy metabolism.) | DOI:10.3390/antiox10060829: reduced sulfur compounds as an electron donor (Review supports reduced sulfur electron donors in photolithotrophic sulfur bacteria.) | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Review supports CO2 fixation as the autotrophic carbon-assimilation process.)
- **Existing causal graph summary:** photolithoautotrophic_light_inorganic_donor_fixation: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **photolithoautotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/photolithoautotrophic.yaml`.

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
**Generated:** 2026-06-18T12:34:16.674043

1. kushkevych2024anoxygenicphotosynthesiswith pages 1-2
2. lawrence2023rewiringphotosyntheticelectron pages 4-7
3. scott2024widespreaddissolvedinorganic pages 1-2
4. nikeleit2024inhibitionofphototrophic pages 1-2
5. scott2024widespreaddissolvedinorganic pages 4-7
6. scott2024widespreaddissolvedinorganic pages 2-4
7. kushkevych2024anoxygenicphotosynthesiswith pages 16-17
8. scott2024widespreaddissolvedinorganic pages 7-10
9. tu2023engineeringartificialphotosynthesis pages 3-4
10. tu2024engineeringrhodopsinbasedartificial pages 51-55
11. kushkevych2024anoxygenicphotosynthesiswith pages 15-16
12. nikeleit2024inhibitionofphototrophic pages 2-3
13. tu2024engineeringrhodopsinbasedartificial pages 9-14
14. tu2024engineeringrhodopsinbasedartificial pages 21-24
15. scott2024widespreaddissolvedinorganic pages 10-13
16. nikeleit2024inhibitionofphototrophic pages 3-4
17. nikeleit2024inhibitionofphototrophic pages 9-11
18. nikeleit2024inhibitionofphototrophic pages 17-17
19. nikeleit2024inhibitionofphototrophic pages 4-5
20. lawrence2023rewiringphotosyntheticelectron pages 9-11
21. scott2024widespreaddissolvedinorganic pages 13-15
22. scott2024widespreaddissolvedinorganic pages 15-18
23. Fe(II)
24. https://doi.org/10.3389/fmicb.2024.1417714;
25. https://doi.org/10.1038/s41467-023-43524-4
26. https://doi.org/10.3389/fmicb.2024.1417714
27. https://doi.org/10.1038/s41561-024-01560-9
28. https://doi.org/10.1038/s44222-023-00093-x
29. https://doi.org/10.1128/aem.01557-23
30. https://doi.org/10.1038/s44222-023-00093-x;
31. https://doi.org/10.5287/ora-8jgz2nrvd
32. https://doi.org/10.3389/fmicb.2024.1417714,
33. https://doi.org/10.1038/s41467-023-43524-4,
34. https://doi.org/10.1128/aem.01557-23,
35. https://doi.org/10.1038/s44222-023-00093-x,
36. https://doi.org/10.1038/s41561-024-01560-9,