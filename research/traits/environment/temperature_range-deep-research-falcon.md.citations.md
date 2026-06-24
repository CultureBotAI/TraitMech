# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature range
- **METPO identifier:** METPO:1000306
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature phenotype with numerical limits that bounds the minimum and maximum ambient temperatures supporting growth of an organism.
- **Parent traits:** METPO:1000533, METPO:1000535
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports the bounded ambient-temperature span over which membrane, enzyme, and bioenergetic adaptations sustain growth as the basis of the temperature-range phenotype.) | DOI:10.1038/sj.embor.7400662: decreased membrane fluidity (Psychrophile review supports cold-end membrane stress as a lower-bound growth constraint that low-temperature tolerance must overcome.)
- **Existing causal graph summary:** temperature_range_bounded_adaptation: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **temperature range** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range.yaml`.

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
**Generated:** 2026-06-18T02:31:41.710846

1. oh2024psychrotrophicbacteriathreatening pages 1-5
2. grunberger2023uncoveringthetemporal pages 1-2
3. dessenne2024lipidomicanalysesreveal pages 1-2
4. christina2024mechanismsofanammox pages 1-5
5. mondal2024aquificaeovercomescompetition pages 1-2
6. moon2023temperaturemattersbacterial pages 7-9
7. chiu2023membranelipidand pages 2-3
8. purwar2024adaptationsofpsychrophilic pages 6-7
9. purwar2024adaptationsofpsychrophilic pages 8-10
10. purwar2024adaptationsofpsychrophilic pages 11-13
11. purwar2024adaptationsofpsychrophilic pages 10-11
12. chiu2023membranelipidand pages 1-2
13. moon2023temperaturemattersbacterial pages 14-15
14. ramon2023ageneraloverview pages 1-2
15. oh2024psychrotrophicbacteriathreatening pages 5-9
16. purwar2024adaptationsofpsychrophilic pages 3-4
17. maiti2024extrememakeoverthe pages 3-4
18. maiti2024extrememakeoverthe pages 4-5
19. chiu2023membranelipidand pages 17-18
20. maiti2024extrememakeoverthe pages 5-6
21. purwar2024adaptationsofpsychrophilic pages 15-16
22. purwar2024adaptationsofpsychrophilic pages 13-15
23. purwar2024adaptationsofpsychrophilic pages 1-3
24. Tmin, Tmax
25. https://doi.org/10.1007/s12275-023-00031-x
26. https://doi.org/10.37256/amtt.5220244537
27. https://doi.org/10.1128/spectrum.00757-24
28. https://doi.org/10.3389/fmicb.2023.1219779
29. https://doi.org/10.1128/mbio.02174-23
30. https://doi.org/10.1007/s42770-023-01057-4
31. https://doi.org/10.5851/kosfa.2024.e70
32. https://doi.org/10.1371/journal.pone.0310595
33. https://doi.org/10.1101/2024.07.23.604647
34. https://doi.org/10.1039/d4cc03114h
35. https://doi.org/10.37256/amtt.5220244537,
36. https://doi.org/10.1128/mbio.02174-23,
37. https://doi.org/10.5851/kosfa.2024.e70,
38. https://doi.org/10.3389/fmicb.2023.1219779,
39. https://doi.org/10.1128/spectrum.00757-24,
40. https://doi.org/10.1007/s12275-023-00031-x,
41. https://doi.org/10.1039/d4cc03114h,
42. https://doi.org/10.1007/s42770-023-01057-4,
43. https://doi.org/10.1101/2024.07.23.604647,
44. https://doi.org/10.1371/journal.pone.0310595,