# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pathogenic to host
- **METPO identifier:** METPO:1004000
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype where a microbe is a pathogen of some host organism.
- **Parent traits:** METPO:1000059
- **Synonyms:** General.keywords, Safety information.risk assessment
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports the encoding of dedicated virulence factors as the molecular basis of host pathogenicity.) | DOI:10.1038/nrmicro1592: secretion systems (Secretion-systems review supports protein secretion machineries as central effectors of host pathogenicity across kingdoms.)
- **Existing causal graph summary:** pathogenic_to_host_virulence_factor_program: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **pathogenic to host** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/pathogenic_to_host.yaml`.

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
**Generated:** 2026-06-17T20:50:29.574052

1. klein2024pathogenicdiversificationof pages 1-2
2. pandey2024bacterialpathogenesis pages 8-10
3. barber2024mechanismsofhost pages 1-2
4. barber2024mechanismsofhost pages 8-10
5. wale2024amasterregulator pages 1-2
6. juszczukkubiak2024molecularaspectsof pages 2-3
7. valik2024genomicvirulencemarkers pages 1-2
8. pandey2024bacterialpathogenesis pages 17-19
9. pandey2024bacterialpathogenesis pages 10-13
10. mitra2024combattingbiofilmmediatedinfections pages 1-2
11. erkihun2024medicalscopeof pages 1-2
12. naga2024aninsighton pages 1-4
13. erkihun2024medicalscopeof pages 2-4
14. juszczukkubiak2024molecularaspectsof pages 8-9
15. https://doi.org/10.1093/femsre/fuae019
16. https://doi.org/10.58532/nbennurmmch1
17. https://doi.org/10.1371/journal.ppat.1012451
18. https://doi.org/10.1128/iai.00314-24
19. https://doi.org/10.1038/s43856-024-00696-4
20. https://doi.org/10.3390/ijms25052655
21. https://doi.org/10.3390/antibiotics13070619
22. https://doi.org/10.1016/j.tcsw.2024.100133
23. https://doi.org/10.3390/bacteria3030008;
24. https://doi.org/10.1007/s10096-024-04920-w
25. https://doi.org/10.3390/bacteria3030008
26. https://doi.org/10.1093/femsre/fuae019,
27. https://doi.org/10.1128/iai.00314-24,
28. https://doi.org/10.58532/nbennurmmch1,
29. https://doi.org/10.3390/antibiotics13070619,
30. https://doi.org/10.3390/ijms25052655,
31. https://doi.org/10.1016/j.tcsw.2024.100133,
32. https://doi.org/10.1371/journal.ppat.1012451,
33. https://doi.org/10.3390/bacteria3030008,
34. https://doi.org/10.1038/s43856-024-00696-4,
35. https://doi.org/10.1007/s10096-024-04920-w,