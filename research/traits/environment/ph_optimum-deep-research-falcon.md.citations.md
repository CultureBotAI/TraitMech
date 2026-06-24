# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH optimum
- **METPO identifier:** METPO:1000331
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH phenotype with numerical limits that represents the external pH conditions at which an organism exhibits the most efficient growth and reproduction.
- **Parent traits:** METPO:1000531, METPO:1000536
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review supports the external pH at which cytoplasmic pH is best maintained as the operational definition of pH optimum.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports the balanced proton motive force at the optimal external pH as the mechanism enabling maximal growth.)
- **Existing causal graph summary:** ph_optimum_balanced_homeostasis: 6 nodes, 4 edges

## Research Objective

Research the microbial trait **pH optimum** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_optimum.yaml`.

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
**Generated:** 2026-06-18T00:34:10.963069

1. poolman2023physicochemicalhomeostasisin pages 1-2
2. ramoneda2023buildingagenomebased pages 1-2
3. fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 12-13
4. yao2023howmethanotrophsrespond pages 2-4
5. poolman2023physicochemicalhomeostasisin pages 2-4
6. ramoneda2023buildingagenomebased pages 3-5
7. sionek2024theimpactof pages 14-15
8. yao2023howmethanotrophsrespond pages 5-7
9. ianutsevich2023theroleof pages 1-2
10. fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 4-7
11. ramoneda2023buildingagenomebased pages 6-7
12. s
13. PhaGF, MnhG, MrpF, and YufB; (33)
14. https://doi.org/10.1093/femsre/fuad033
15. https://doi.org/10.3389/fmicb.2022.1034164
16. https://doi.org/10.1111/1758-2229.70019
17. https://doi.org/10.3390/microorganisms11071733
18. https://doi.org/10.3390/fermentation10060298
19. https://doi.org/10.1126/sciadv.adf8998
20. https://doi.org/10.3390/jof9060652
21. https://doi.org/10.1093/femsre/fuad033,
22. https://doi.org/10.1111/1758-2229.70019,
23. https://doi.org/10.1126/sciadv.adf8998,
24. https://doi.org/10.3390/jof9060652,
25. https://doi.org/10.3389/fmicb.2022.1034164,
26. https://doi.org/10.3390/fermentation10060298,
27. https://doi.org/10.3390/microorganisms11071733,