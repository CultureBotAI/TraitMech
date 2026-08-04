# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** endosymbiosis
- **METPO identifier:** traitmech:000045
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A symbiosis in which the microorganism lives inside the cells or tissues of its host. Obligate intracellular endosymbionts (e.g. of insects) frequently undergo extreme genome reduction.
- **Parent traits:** traitmech:000040
- **Synonyms:** endosymbiont
- **Existing evidence:** DOI:10.1038/nrmicro2670:  (McCutcheon & Moran, "Extreme genome reduction in symbiotic bacteria", characterize intracellular endosymbionts and their diminished genomes.) | DOI:10.1038/nrmicro.2017.171:  (Poole et al. describe rhizobia as plant-cell endosymbionts within root nodules, an example of the endosymbiotic lifestyle.)
- **Existing causal graph summary:** endosymbiosis_intracellular_genome_reduction: 10 nodes, 7 edges

## Research Objective

Research the microbial trait **endosymbiosis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/endosymbiosis.yaml`.

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
**Generated:** 2026-08-03T23:21:03.238860

1. wierz2024intracellularsymbiontsymbiodolus pages 9-10
2. cai2024expressionandmutagenesis pages 15-16
3. bai2024endosymbionttremblayaphenacola pages 1-2
4. shang2024micrornamaintainsnutrient pages 8-9
5. ling2024acompletedna pages 10-11
6. ward2024adaptationduringthe pages 1-2
7. wierz2024intracellularsymbiontsymbiodolus pages 1-2
8. wierz2024intracellularsymbiontsymbiodolus pages 10-11
9. https://doi.org/10.1093/ismejo/wrae099
10. https://doi.org/10.1093/ismejo/wrae052
11. https://doi.org/10.1073/pnas.2406925121
12. https://doi.org/10.1073/pnas.2415651121
13. https://doi.org/10.1093/gbe/evae251
14. https://doi.org/10.1002/ece3.11705
15. https://doi.org/10.3389/fpls.2023.1306491
16. https://doi.org/10.1038/nrmicro2670.
17. https://doi.org/10.1002/ece3.11705,
18. https://doi.org/10.1093/ismejo/wrae099,
19. https://doi.org/10.1093/ismejo/wrae052,
20. https://doi.org/10.1073/pnas.2406925121,
21. https://doi.org/10.3389/fpls.2023.1306491,
22. https://doi.org/10.1073/pnas.2415651121,
23. https://doi.org/10.1093/gbe/evae251,