# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** commensalism
- **METPO identifier:** traitmech:000042
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A symbiosis in which the microorganism benefits from the association (e.g. resources, shelter, transport) while the host's fitness remains essentially unaffected.
- **Parent traits:** traitmech:000040
- **Synonyms:** commensal
- **Existing evidence:** DOI:10.1038/s41579-021-00550-7:  (Drew et al. place commensalism on the parasite-mutualist continuum as a near-neutral host interaction.) | DOI:10.1073/pnas.1218525110:  (McFall-Ngai et al. support commensal colonization as a major class of host-associated microbial lifestyles.)
- **Existing causal graph summary:** commensalism_neutral_host: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **commensalism** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/commensalism.yaml`.

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
**Generated:** 2026-06-17T20:18:25.260265

1. drew2021microbialevolutionand pages 1-2
2. srinivasan2024modelingmicrobialcommunity pages 1-2
3. dziuba2024phylogenymorphologyvirulence pages 1-2
4. lengrand2024bacterialendophytomesources pages 2-3
5. wilde2024hostcontrolof pages 8-10
6. carretobinaghi2024roleofcellular pages 9-10
7. huang2024themycobiomeas pages 1-2
8. ambat2024emergentmetabolicinteractions pages 1-2
9. wilde2024hostcontrolof pages 1-5
10. bloch2024oralstreptococcimodulators pages 2-3
11. wilde2024hostcontrolof pages 24-26
12. wilde2024hostcontrolof pages 15-17
13. wilde2024hostcontrolof pages 5-8
14. wilde2024hostcontrolof pages 26-28
15. srinivasan2024modelingmicrobialcommunity pages 2-3
16. https://doi.org/10.1126/science.adi3338
17. https://doi.org/10.3389/fimmu.2024.1446072
18. https://doi.org/10.1080/19490976.2024.2440111
19. https://doi.org/10.3389/fcimb.2024.1357631
20. https://doi.org/10.1101/2024.08.29.610284
21. https://doi.org/10.1038/s41579-021-00550-7
22. https://doi.org/10.1128/mbio.00582-24
23. https://doi.org/10.1007/s00248-024-02370-7
24. https://doi.org/10.3389/fsufs.2024.1378436
25. https://doi.org/10.1038/s41579-021-00550-7,
26. https://doi.org/10.1007/s00248-024-02370-7,
27. https://doi.org/10.1128/mbio.00582-24,
28. https://doi.org/10.3389/fsufs.2024.1378436,
29. https://doi.org/10.1126/science.adi3338,
30. https://doi.org/10.3389/fimmu.2024.1446072,
31. https://doi.org/10.1080/19490976.2024.2440111,
32. https://doi.org/10.1101/2024.08.29.610284,
33. https://doi.org/10.3389/fcimb.2024.1357631,