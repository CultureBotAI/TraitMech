# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** neutrophilic
- **METPO identifier:** METPO:1003001
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference characterized by optimal growth at near-neutral pH values, typically between pH 6.5 and 7.5.
- **Parent traits:** METPO:1003000
- **Synonyms:** neutralophile, neutralophilic, neutrophile
- **Existing evidence:** DOI:10.1038/nrmicro2549: cytoplasmic pH ... must maintain for growth (Supports pH growth preference as tied to cytoplasmic pH requirements.)
- **Existing causal graph summary:** neutrophilic_neutral_ph_homeostasis: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **neutrophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/neutrophilic.yaml`.

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
**Generated:** 2026-06-17T23:44:45.918402

1. rebelo2023unravelingtherole pages 18-20
2. li2024responseofescherichia pages 1-2
3. ramoneda2023buildingagenomebased pages 3-5
4. terradot2024escherichiacolimaintains pages 1-2
5. schumacher2023ribosomeprofilingreveals pages 1-2
6. beetham2024histidinetransportis pages 1-2
7. jiang2024exogenousputrescineplays pages 4-6
8. poolman2023physicochemicalhomeostasisin pages 1-2
9. poolman2023physicochemicalhomeostasisin pages 2-4
10. PhaGF, MnhG, MrpF, and YufB
11. https://doi.org/10.1128/msystems.01037-23
12. https://doi.org/10.3390/antibiotics12091474
13. https://doi.org/10.1093/femsre/fuad033
14. https://doi.org/10.1126/sciadv.adf8998
15. https://doi.org/10.1103/prxlife.2.043015
16. https://doi.org/10.1371/journal.ppat.1011927
17. https://doi.org/10.1128/aem.00569-24
18. https://doi.org/10.3390/microorganisms12091774
19. https://doi.org/10.3390/antibiotics12091474,
20. https://doi.org/10.1103/prxlife.2.043015,
21. https://doi.org/10.1093/femsre/fuad033,
22. https://doi.org/10.3390/microorganisms12091774,
23. https://doi.org/10.1128/msystems.01037-23,
24. https://doi.org/10.1126/sciadv.adf8998,
25. https://doi.org/10.1371/journal.ppat.1011927,
26. https://doi.org/10.1128/aem.00569-24,