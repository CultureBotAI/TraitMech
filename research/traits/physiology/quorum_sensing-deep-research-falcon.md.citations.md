# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** quorum sensing
- **METPO identifier:** traitmech:000084
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-density-dependent regulatory physiology in which cells produce, release, and detect diffusible autoinducer signals to coordinate gene expression across a population.
- **Parent traits:** METPO:1000059
- **Synonyms:** autoinduction
- **Existing evidence:** DOI:10.1146/annurev.cellbio.21.012704.131001:  (Waters & Bassler review quorum sensing as autoinducer-mediated cell-to-cell communication coordinating population-wide behavior.) | DOI:10.1146/annurev.micro.55.1.165:  (Miller & Bassler review quorum sensing across bacteria and its regulatory logic.)
- **Existing causal graph summary:** quorum_sensing_autoinducer: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **quorum sensing** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/quorum_sensing.yaml`.

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
**Generated:** 2026-06-18T13:00:39.383808

1. rajkhowa2024advancingantibioticresistantmicrobe pages 4-5
2. fang2024determinantsofmaturation pages 1-2
3. juszczukkubiak2024molecularaspectsof pages 2-3
4. zhu2023innovativemicrobialdisease pages 1-2
5. li2024anengineeredescherichia pages 9-13
6. rimi2024biofilmformationagr pages 1-2
7. erkihun2024medicalscopeof pages 6-8
8. li2024anengineeredescherichia pages 23-26
9. podkowik2024quorumsensingagrsystem pages 1-2
10. li2024anengineeredescherichia pages 17-20
11. podkowik2024quorumsensingagrsystem pages 10-12
12. sedarat2024quorumsensingin pages 1-3
13. li2024anengineeredescherichia pages 1-5
14. hetta2024quorumsensinginhibitors pages 4-6
15. kuai2024roleofsara pages 6-9
16. madarova2024noveltherapeutictargeting pages 18-21
17. simpson2024quorumsensingin pages 25-26
18. podkowik2024quorumsensingagrsystem pages 12-14
19. hetta2024quorumsensinginhibitors pages 2-4
20. https://doi.org/10.3390/synbio1020010
21. https://doi.org/10.3390/ijms25052655
22. https://doi.org/10.1128/jb.00195-24
23. https://doi.org/10.3390/bacteria3030008
24. https://doi.org/10.7554/eLife.89098
25. https://doi.org/10.1371/journal.pone.0308282
26. https://doi.org/10.3390/pharmaceutics16091160
27. https://doi.org/10.3390/molecules29153466
28. https://doi.org/10.5772/intechopen.113338
29. https://doi.org/10.5713/ab.23.0374
30. https://doi.org/10.3389/fpls.2022.1063393
31. https://doi.org/10.5772/intechopen.113338,
32. https://doi.org/10.3390/ijms25052655,
33. https://doi.org/10.3390/synbio1020010,
34. https://doi.org/10.1128/jb.00195-24,
35. https://doi.org/10.3390/pharmaceutics16091160,
36. https://doi.org/10.3390/bacteria3030008,
37. https://doi.org/10.7554/elife.89098,
38. https://doi.org/10.3389/fpls.2022.1063393,
39. https://doi.org/10.1371/journal.pone.0308282,
40. https://doi.org/10.3390/molecules29153466,
41. https://doi.org/10.5713/ab.23.0374,
42. https://doi.org/10.36877/pmmb.a0000444,
43. https://doi.org/10.1371/journal.pbio.3002891,