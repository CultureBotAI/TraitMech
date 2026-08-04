# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** twitching motility
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000061
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagella-independent surface motility driven by the extension, attachment, and retraction of type IV pili, producing intermittent, jerky translocation of cells across moist surfaces.
- **Parent traits:** METPO:1000702
- **Synonyms:** twitching
- **Existing evidence:** DOI:10.1146/annurev.micro.56.012302.160938:  (Mattick, "Type IV pili and twitching motility", describes twitching as type-IV-pilus-driven surface translocation operating like a grappling hook.) | DOI:10.1146/annurev.micro.57.030502.091014:  (Harshey, "Bacterial motility on a surface", places twitching among the distinct surface-translocation strategies of bacteria.)
- **Existing causal graph summary:** twitching_type_iv_pilus_retraction: 11 nodes, 7 edges

## Research Objective

Research the microbial trait **twitching motility** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/twitching_motility.yaml`.

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
**Generated:** 2026-08-04T10:30:34.535645

1. mattick2002typeivpili pages 5-7
2. tala2022characterizationofpseudomonas pages 58-61
3. webster2022thepowerof pages 10-12
4. yarrington2024thetypeiv pages 17-18
5. yarrington2024thetypeiv pages 3-5
6. yarrington2024thetypeiv pages 9-11
7. geiger2024abacterialsense pages 3-5
8. tala2022characterizationofpseudomonas pages 21-24
9. yarrington2024thetypeiv pages 16-17
10. singh2022landmarkdiscoveriesand pages 5-7
11. tala2022characterizationofpseudomonas pages 56-58
12. yarrington2024thetypeiv pages 1-2
13. yarrington2024thetypeiv pages 18-20
14. yarrington2024thetypeiv pages 2-3
15. taxon-specific
16. proposed
17. https://doi.org/10.5075/epfl-thesis-8646;
18. https://doi.org/10.1128/jb.00084-22
19. https://doi.org/10.1128/jb.00084-22;
20. https://doi.org/10.5075/epfl-thesis-8646
21. https://doi.org/10.1128/mmbr.00076-22
22. https://doi.org/10.1128/jb.00442-23
23. https://doi.org/10.1371/journal.pgen.1008393;
24. https://doi.org/10.1038/s41564-019-0378-9
25. https://doi.org/10.1146/annurev.micro.56.012302.160938
26. https://doi.org/10.1371/journal.pbio.3002488
27. https://doi.org/10.1128/jb.00442-23;
28. https://doi.org/10.1371/journal.pgen.1008393
29. https://doi.org/10.1146/annurev.micro.56.012302.160938,
30. https://doi.org/10.1128/jb.00084-22,
31. https://doi.org/10.5075/epfl-thesis-8646,
32. https://doi.org/10.1128/jb.00442-23,
33. https://doi.org/10.1128/mmbr.00076-22,
34. https://doi.org/10.1371/journal.pbio.3002488,