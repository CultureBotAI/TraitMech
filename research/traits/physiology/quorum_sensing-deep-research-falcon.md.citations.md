# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** quorum sensing
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000084
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-density-dependent regulatory physiology in which cells produce, release, and detect diffusible autoinducer signals to coordinate gene expression across a population.
- **Parent traits:** METPO:1000059
- **Synonyms:** autoinduction
- **Existing evidence:** DOI:10.1146/annurev.cellbio.21.012704.131001:  (Waters & Bassler review quorum sensing as autoinducer-mediated cell-to-cell communication coordinating population-wide behavior.) | DOI:10.1146/annurev.micro.55.1.165:  (Miller & Bassler review quorum sensing across bacteria and its regulatory logic.)
- **Existing causal graph summary:** quorum_sensing_autoinducer: 7 nodes, 6 edges

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
**Generated:** 2026-08-04T12:07:15.468506

1. ostovar2024phenotypicmemoryin pages 1-2
2. juszczukkubiak2024molecularaspectsof pages 2-3
3. walker2023asimplemechanism pages 1-2
4. juszczukkubiak2024molecularaspectsof pages 5-7
5. green2023modelledmicrogravityreducesvirulence pages 1-2
6. eickhoff2021luxtcontrolsspecific pages 1-2
7. hu2024nanomaterialsregulatebacterial pages 1-2
8. chan2015inhibitingnacylhomoserinelactone pages 1-2
9. liu2025quorumsensingnot pages 2-6
10. juszczukkubiak2024molecularaspectsof pages 16-18
11. juszczukkubiak2024molecularaspectsof pages 40-40
12. liu2025quorumsensingnot pages 14-15
13. 10.3390/ijms25052655
14. 10.1002/advs.202306070
15. 10.3389/fmicb.2015.01173
16. 10.1002/mbo3.70016
17. 10.1371/journal.pgen.1009336
18. 10.7554/eLife.86699
19. 10.3390/ijms242115997
20. 10.3389/fpls.2022.1063393
21. 10.1371/journal.pcbi.1011696
22. 10.1111/raq.12787
23. https://doi.org/10.1002/advs.202306070
24. https://doi.org/10.3390/ijms25052655
25. https://doi.org/10.1371/journal.pcbi.1011696
26. https://doi.org/10.7554/eLife.86699
27. https://doi.org/10.3390/ijms242115997
28. https://doi.org/10.1111/raq.12787
29. https://doi.org/10.3389/fpls.2022.1063393
30. https://doi.org/10.1371/journal.pgen.1009336
31. https://doi.org/10.3389/fmicb.2015.01173
32. https://doi.org/10.1146/annurev.cellbio.21.012704.131001
33. https://doi.org/10.1146/annurev.micro.55.1.165
34. https://doi.org/10.1002/mbo3.70016
35. https://doi.org/10.1002/advs.202306070](https://doi.org/10.1002/advs.202306070
36. https://doi.org/10.3390/ijms25052655](https://doi.org/10.3390/ijms25052655
37. https://doi.org/10.1371/journal.pcbi.1011696](https://doi.org/10.1371/journal.pcbi.1011696
38. https://doi.org/10.7554/eLife.86699](https://doi.org/10.7554/eLife.86699
39. https://doi.org/10.3390/ijms242115997](https://doi.org/10.3390/ijms242115997
40. https://doi.org/10.1111/raq.12787](https://doi.org/10.1111/raq.12787
41. https://doi.org/10.3389/fpls.2022.1063393](https://doi.org/10.3389/fpls.2022.1063393
42. https://doi.org/10.1371/journal.pgen.1009336](https://doi.org/10.1371/journal.pgen.1009336
43. https://doi.org/10.3389/fmicb.2015.01173](https://doi.org/10.3389/fmicb.2015.01173
44. https://doi.org/10.1146/annurev.cellbio.21.012704.131001](https://doi.org/10.1146/annurev.cellbio.21.012704.131001
45. https://doi.org/10.1146/annurev.micro.55.1.165](https://doi.org/10.1146/annurev.micro.55.1.165
46. https://doi.org/10.3390/ijms25052655,
47. https://doi.org/10.1371/journal.pcbi.1011696,
48. https://doi.org/10.1002/advs.202306070,
49. https://doi.org/10.3389/fmicb.2015.01173,
50. https://doi.org/10.1371/journal.pgen.1009336,
51. https://doi.org/10.7554/elife.86699,
52. https://doi.org/10.3390/ijms242115997,
53. https://doi.org/10.1002/mbo3.70016,
54. https://doi.org/10.1111/raq.12787,