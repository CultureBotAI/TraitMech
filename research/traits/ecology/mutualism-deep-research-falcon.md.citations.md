# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** mutualism
- **METPO identifier:** traitmech:000041
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A symbiosis in which both the microorganism and its host or partner benefit from the association, often through exchange of nutrients or services.
- **Parent traits:** traitmech:000040
- **Synonyms:** mutualist
- **Existing evidence:** DOI:10.1073/pnas.1218525110:  (McFall-Ngai et al. document widespread mutually beneficial host-microbe associations across animals.) | DOI:10.1126/science.1104816:  (Bäckhed et al., "Host-bacterial mutualism in the human intestine", supports reciprocal benefit (nutrient harvest for the host, habitat for the microbes) as the defining feature of mutualism.)
- **Existing causal graph summary:** mutualism_reciprocal_benefit: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **mutualism** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/mutualism.yaml`.

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
**Generated:** 2026-06-17T20:45:21.170691

1. laurich2024communityinteractionsamong pages 1-2
2. peng2024amoleculartoolkit pages 1-2
3. pena2024mycorrhizalsymbiosisand pages 1-3
4. wilde2024hostcontrolof pages 1-5
5. tao2024nitrogenandnod pages 1-2
6. burgunterdelamare2024exchangeoreliminate pages 1-2
7. grzyb2024decipheringmolecularmechanisms pages 24-25
8. zhiyuan2024quinolonemediatedmetaboliccrossfeeding pages 2-3
9. liuxu2024harnessinggreenhelpers pages 7-9
10. zhiyuan2024quinolonemediatedmetaboliccrossfeeding pages 1-2
11. song2024strategiesandtools pages 1-3
12. patil2024flavonoidsinplantenvironment pages 6-8
13. kumar2024recentadvancementsin pages 2-3
14. liuxu2024harnessinggreenhelpers pages 1-3
15. are acquired
16. https://doi.org/10.1007/s00253-024-13298-w;
17. https://doi.org/10.1126/science.adi3338
18. https://doi.org/10.1038/s41564-023-01596-4
19. https://doi.org/10.1007/s44372-024-00063-6;
20. https://doi.org/10.3389/fpls.2023.1297706;
21. https://doi.org/10.1038/s41467-024-47752-0
22. https://doi.org/10.3389/fpls.2023.1297706
23. https://doi.org/10.1007/s44372-024-00063-6
24. https://doi.org/10.1038/s41467-024-47752-0;
25. https://doi.org/10.1128/mbio.00972-24
26. https://doi.org/10.3390/ijms252413601
27. https://doi.org/10.3390/ijms252413601;
28. https://doi.org/10.1038/s41467-024-54616-0;
29. https://doi.org/10.1038/s41467-024-54616-0
30. https://doi.org/10.1007/s00253-024-13298-w
31. https://doi.org/10.3390/plants13060829
32. https://doi.org/10.3390/horticulturae10060621
33. https://doi.org/10.1186/s13068-024-02594-2
34. https://doi.org/10.1126/science.1104816
35. https://doi.org/10.1007/s00253-024-13298-w,
36. https://doi.org/10.3390/plants13060829,
37. https://doi.org/10.1126/science.adi3338,
38. https://doi.org/10.1128/mbio.00972-24,
39. https://doi.org/10.1038/s41564-023-01596-4,
40. https://doi.org/10.1038/s41467-024-47752-0,
41. https://doi.org/10.1038/s41467-024-54616-0,
42. https://doi.org/10.1007/s44372-024-00063-6,
43. https://doi.org/10.3389/fpls.2023.1297706,
44. https://doi.org/10.3390/ijms252413601,
45. https://doi.org/10.3390/horticulturae10060621,
46. https://doi.org/10.1186/s13068-024-02594-2,