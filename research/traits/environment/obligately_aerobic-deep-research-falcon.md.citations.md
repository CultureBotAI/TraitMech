# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** obligately aerobic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000606
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference that requires molecular oxygen (O₂) for growth.
- **Parent traits:** METPO:1000601
- **Synonyms:** obligate aerobe, obligate aerobic
- **Existing evidence:** https://www.ncbi.nlm.nih.gov/books/NBK482349/: require oxygen as a terminal electron acceptor (Supports the requirement for oxygen in obligately aerobic organisms.) | PMID:27203084: M. tuberculosis is an obligate aerobe (Organism example: Mycobacterium tuberculosis is described as obligately aerobic.)
- **Existing causal graph summary:** obligate_aerobe_oxygen_respiration: 12 nodes, 10 edges

## Research Objective

Research the microbial trait **obligately aerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/obligately_aerobic.yaml`.

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
**Generated:** 2026-08-04T02:14:26.329279

1. mckay2024cytochromeoxidaserequirements pages 1-2
2. andre2021theselectiveadvantage pages 2-4
3. mckay2024cytochromeoxidaserequirements pages 8-10
4. kampers2020microbiallifestyleengineering pages 103-107
5. mckay2024cytochromeoxidaserequirements pages 18-20
6. harrison2024remissionspectroscopyresolves pages 27-29
7. 10.1111/cmi.13338
8. 10.1371/journal.ppat.1012084
9. 10.1186/s12934-019-1227-5
10. 10.1371/journal.pone.0309988
11. 10.1002/1873-3468.14906
12. 10.1101/2024.12.03.626386
13. 10.3390/antibiotics13121169
14. 10.30970/sbi.1702.716
15. 10.18174/516082
16. 10.2217/fmb.10.16
17. https://www.ncbi.nlm.nih.gov/books/NBK482349/:
18. https://doi.org/10.1111/cmi.13338
19. https://doi.org/10.1371/journal.ppat.1012084
20. https://doi.org/10.1186/s12934-019-1227-5
21. https://doi.org/10.1371/journal.pone.0309988
22. https://doi.org/10.1002/1873-3468.14906
23. https://doi.org/10.1101/2024.12.03.626386
24. https://doi.org/10.3390/antibiotics13121169
25. https://doi.org/10.30970/sbi.1702.716
26. https://doi.org/10.18174/516082
27. https://doi.org/10.2217/fmb.10.16
28. https://doi.org/10.1371/journal.ppat.1012084,
29. https://doi.org/10.1111/cmi.13338,
30. https://doi.org/10.18174/516082,
31. https://doi.org/10.1101/2024.12.03.626386,