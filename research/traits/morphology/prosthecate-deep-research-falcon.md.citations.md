# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** prosthecate
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000065
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait in which the cell bears one or more prosthecae — tubular extensions of the cell envelope (stalks) — that increase nutrient-uptake surface area or mediate attachment, as in Caulobacter.
- **Parent traits:** METPO:1000059
- **Synonyms:** stalked, prostheca
- **Existing evidence:** DOI:10.1111/j.1365-2958.2007.05633.x:  (Wagner & Brun describe the Caulobacter stalk (prostheca) as a cell-envelope extension and a specialized form of cell elongation aiding nutrient uptake.) | DOI:10.1128/MMBR.00040-09:  (Curtis & Brun's review of Caulobacter development supports the stalk as a regulated developmental appendage.)
- **Existing causal graph summary:** prosthecate_stalk_nutrient_uptake: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **prosthecate** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/prosthecate.yaml`.

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
**Generated:** 2026-08-04T09:45:52.015807

1. kysela2016diversitytakesshape pages 7-9
2. hao2018novelprosthecatebacteria pages 9-10
3. barrows2023synchronizedswarmersand pages 5-7
4. jacq2024functionalspecializationof pages 1-6
5. caccamo2018themolecularbasis pages 4-6
6. barrows2023synchronizedswarmersand pages 9-11
7. billini2019aspecializedmrebdependent pages 2-3
8. billini2019aspecializedmrebdependent pages 7-8
9. billini2019aspecializedmrebdependent pages 18-19
10. billini2019aspecializedmrebdependent pages 14-16
11. billini2019aspecializedmrebdependent pages 8-10
12. billini2019aspecializedmrebdependent pages 19-21
13. jacq2024functionalspecializationof pages 6-10
14. randich2015molecularmechanismsfor pages 7-9
15. curtis2010gettinginthe pages 2-3
16. *C. crescentus*, condition-specific
17. 10.1128/jb.00384-22
18. 10.1101/2024.12.16.628611
19. 10.1371/journal.pgen.1007897
20. 10.1038/s41396-018-0187-9
21. 10.1016/j.tim.2017.09.012
22. 10.1371/journal.pbio.1002565
23. 10.3389/fmicb.2015.00580
24. 10.1128/MMBR.00040-09
25. 10.1111/j.1365-2958.2007.05633.x
26. https://doi.org/10.1128/jb.00384-22
27. https://doi.org/10.1101/2024.12.16.628611
28. https://doi.org/10.1371/journal.pgen.1007897
29. https://doi.org/10.1038/s41396-018-0187-9
30. https://doi.org/10.1016/j.tim.2017.09.012
31. https://doi.org/10.1371/journal.pbio.1002565
32. https://doi.org/10.3389/fmicb.2015.00580
33. https://doi.org/10.1128/MMBR.00040-09
34. https://doi.org/10.1111/j.1365-2958.2007.05633.x
35. https://doi.org/10.1371/journal.pgen.1007897,
36. https://doi.org/10.1128/mmbr.00040-09,
37. https://doi.org/10.1128/jb.00384-22,
38. https://doi.org/10.1101/2024.12.16.628611,
39. https://doi.org/10.1038/s41396-018-0187-9,
40. https://doi.org/10.1371/journal.pbio.1002565,
41. https://doi.org/10.1016/j.tim.2017.09.012,
42. https://doi.org/10.3389/fmicb.2015.00580,