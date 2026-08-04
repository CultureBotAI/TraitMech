# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** host-associated
- **METPO identifier:** traitmech:000049
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A habitat association in which an organism lives persistently on or in a plant or animal host (e.g. as a member of a host microbiome), spanning commensal, mutualistic, and pathogenic relationships.
- **Parent traits:** traitmech:000047
- **Synonyms:** 
- **Existing evidence:** DOI:10.1073/pnas.1218525110:  (McFall-Ngai et al. document the ubiquity of host-associated microbial communities across the animal kingdom.) | DOI:10.1126/science.1104816:  (Bäckhed et al. characterize the host-associated gut microbiota as a dense, coevolved community.)
- **Existing causal graph summary:** host_associated_microbiome: 11 nodes, 11 edges

## Research Objective

Research the microbial trait **host-associated** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/host_associated.yaml`.

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
**Generated:** 2026-08-03T23:30:42.121807

1. wiesmann2023originsofsymbiosis pages 1-2
2. wilde2024hostcontrolof pages 1-5
3. liu2024rootcolonizationby pages 1-2
4. lin2024areviewof pages 19-20
5. wiesmann2023originsofsymbiosis pages 3-4
6. wiesmann2023originsofsymbiosis pages 4-5
7. tiwari2023genomewideassociationreveals pages 7-9
8. torres2024sheddinglighton pages 11-13
9. caballeroflores2023microbiotamediatedcolonizationresistance pages 30-30
10. torres2024sheddinglighton pages 3-5
11. tiwari2023genomewideassociationreveals pages 1-2
12. tiwari2023genomewideassociationreveals pages 5-7
13. krzyzanowska2023hostadaptivetraitsin pages 1-2
14. levy2018genomicfeaturesof pages 1-2
15. 10.1093/femsre/fuac048
16. 10.1126/science.adi3338
17. 10.1128/mbio.00390-24
18. 10.1186/s12915-023-01562-w
19. 10.1093/femsre/fuad066
20. 10.1038/s41598-023-36494-6
21. 10.1038/s41579-022-00833-7
22. 10.3390/microorganisms12051026
23. 10.1038/s41588-017-0012-9
24. 10.1073/pnas.1218525110
25. 10.1126/science.1104816
26. https://doi.org/10.1093/femsre/fuac048
27. https://doi.org/10.1126/science.adi3338
28. https://doi.org/10.1128/mbio.00390-24
29. https://doi.org/10.1186/s12915-023-01562-w
30. https://doi.org/10.1093/femsre/fuad066
31. https://doi.org/10.1038/s41598-023-36494-6
32. https://doi.org/10.1038/s41579-022-00833-7
33. https://doi.org/10.3390/microorganisms12051026
34. https://doi.org/10.1038/s41588-017-0012-9
35. https://doi.org/10.1073/pnas.1218525110
36. https://doi.org/10.1126/science.1104816
37. https://doi.org/10.1093/femsre/fuac048,
38. https://doi.org/10.1126/science.adi3338,
39. https://doi.org/10.1093/femsre/fuad066,
40. https://doi.org/10.3390/microorganisms12051026,
41. https://doi.org/10.1186/s12915-023-01562-w,
42. https://doi.org/10.1128/mbio.00390-24,
43. https://doi.org/10.1038/s41579-022-00833-7,
44. https://doi.org/10.1038/s41598-023-36494-6,
45. https://doi.org/10.1038/s41588-017-0012-9,