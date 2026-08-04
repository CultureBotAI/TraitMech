# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** propionic acid fermentation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000029
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A fermentation that produces propionate (with acetate and CO2) from sugars or lactate, typically via the Wood-Werkman (methylmalonyl-CoA) pathway. Characteristic of propionibacteria (e.g. Propionibacterium freudenreichii).
- **Parent traits:** METPO:1002005
- **Synonyms:** propionate fermentation
- **Existing evidence:** DOI:10.3390/molecules31020333:  (Review of classical fermentations describes propionic acid fermentation (acetic acid, propionic acid, CO2) and propionibacteria as its agents, including the Wood-Werkman route.) | DOI:10.3389/fmicb.2021.703525:  (Review of fermentative energy conservation supports propionate formation as a redox-balancing, energy-conserving fermentation route.)
- **Existing causal graph summary:** propionic_acid_fermentation_propionate: 15 nodes, 11 edges

## Research Objective

Research the microbial trait **propionic acid fermentation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/propionic_acid_fermentation.yaml`.

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
**Generated:** 2026-08-04T06:56:27.563937

1. gonzalezgarcia2017microbialpropionicacid pages 1-3
2. neves2024expandingpseudomonastaiwanensis pages 1-2
3. bucher2021propionicacidbacteria pages 3-5
4. gonzalezgarcia2017microbialpropionicacid pages 8-10
5. dishisha2024highcelldensity pages 1-2
6. doring2024propionateproductionby pages 1-2
7. gonzalezgarcia2017microbialpropionicacid pages 3-5
8. loivamaa2024aerobicadaptationand pages 6-9
9. dank2021propionibacteriumfreudenreichiithrives pages 3-4
10. gonzalezgarcia2017microbialpropionicacid pages 6-8
11. gonzalezgarcia2017microbialpropionicacid pages 5-6
12. doring2024propionateproductionby pages 4-5
13. gonzalezgarcia2017microbialpropionicacid pages 15-17
14. loivamaa2024aerobicadaptationand pages 1-2
15. 10.3390/fermentation3020021
16. 10.1111/1541-4337.12804
17. 10.1128/msystems.00615-24
18. 10.1111/1462-2920.15532
19. 10.1186/s12934-024-02366-5
20. 10.1186/s13068-024-02539-9
21. EC:5.4.99.2
22. EC:2.1.3.1
23. 10.1111/1751-7915.14309
24. https://doi.org/10.3390/fermentation3020021
25. https://doi.org/10.1111/1541-4337.12804
26. https://doi.org/10.1128/msystems.00615-24
27. https://doi.org/10.1111/1462-2920.15532
28. https://doi.org/10.1186/s12934-024-02366-5
29. https://doi.org/10.1186/s13068-024-02539-9
30. https://doi.org/10.1111/1751-7915.14309
31. https://doi.org/10.1111/1541-4337.12804,
32. https://doi.org/10.3390/fermentation3020021,
33. https://doi.org/10.1128/msystems.00615-24,
34. https://doi.org/10.1111/1462-2920.15532,
35. https://doi.org/10.1186/s13068-024-02539-9,
36. https://doi.org/10.1111/1751-7915.14309,
37. https://doi.org/10.1186/s12934-024-02366-5,