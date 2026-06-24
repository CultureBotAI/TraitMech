# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** propionic acid fermentation
- **METPO identifier:** traitmech:000029
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A fermentation that produces propionate (with acetate and CO2) from sugars or lactate, typically via the Wood-Werkman (methylmalonyl-CoA) pathway. Characteristic of propionibacteria (e.g. Propionibacterium freudenreichii).
- **Parent traits:** METPO:1002005
- **Synonyms:** propionate fermentation
- **Existing evidence:** DOI:10.3390/molecules31020333:  (Review of classical fermentations describes propionic acid fermentation (acetic acid, propionic acid, CO2) and propionibacteria as its agents, including the Wood-Werkman route.) | DOI:10.3389/fmicb.2021.703525:  (Review of fermentative energy conservation supports propionate formation as a redox-balancing, energy-conserving fermentation route.)
- **Existing causal graph summary:** propionic_acid_fermentation_propionate: 3 nodes, 2 edges

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
**Generated:** 2026-06-18T05:54:11.089981

1. rymuszka2026classicalfoodfermentations pages 19-20
2. doring2024propionateproductionby pages 1-2
3. loivamaa2024aerobicadaptationand pages 9-12
4. kim2023genomescalemetabolicmodeling pages 7-10
5. hackmann2024thevastlandscape pages 10-11
6. rymuszka2026classicalfoodfermentations pages 20-23
7. hackmann2024thevastlandscape pages 9-10
8. doring2024propionateproductionby pages 12-13
9. dishisha2024highcelldensity pages 1-2
10. neves2024expandingpseudomonastaiwanensis pages 7-10
11. rymuszka2026classicalfoodfermentations pages 24-25
12. dishisha2024highcelldensity pages 2-4
13. facchin2025rethinkingshortchainfatty pages 2-4
14. kim2023genomescalemetabolicmodeling pages 10-11
15. neves2024expandingpseudomonastaiwanensis pages 1-2
16. https://doi.org/10.1186/s12934-024-02366-5
17. https://doi.org/10.1186/s13068-024-02539-9
18. https://doi.org/10.1111/1751-7915.14309
19. https://doi.org/10.3389/fcimb.2023.1099314
20. https://doi.org/10.1093/femsre/fuae016
21. https://doi.org/10.1128/msystems.00615-24
22. https://doi.org/10.3390/molecules31020333
23. https://doi.org/10.3390/molecules31020333,
24. https://doi.org/10.1186/s13068-024-02539-9,
25. https://doi.org/10.1128/msystems.00615-24,
26. https://doi.org/10.3389/fcimb.2023.1099314,
27. https://doi.org/10.1093/femsre/fuae016,
28. https://doi.org/10.1186/s12934-024-02366-5,
29. https://doi.org/10.1111/1751-7915.14309,
30. https://doi.org/10.3390/cells14151130,