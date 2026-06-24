# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** proteolysis
- **METPO identifier:** traitmech:000116
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biopolymer-degradation metabolism in which an organism secretes proteases to hydrolyze extracellular proteins and peptides into amino acids and short peptides for nutrition.
- **Parent traits:** traitmech:000110
- **Synonyms:** proteolytic, protein degradation
- **Existing evidence:** DOI:10.1128/mmbr.62.3.597-635.1998:  (Rao et al. review microbial proteases, noting that secreted (extracellular) proteases play a major nutritional role through their depolymerizing activity.) | DOI:10.1093/femsre/fuab046:  (Review of Bacillus proteases covers extracellular protease activities and their functions.)
- **Existing causal graph summary:** proteolysis_extracellular_protease: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **proteolysis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/proteolysis.yaml`.

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
**Generated:** 2026-06-18T05:59:46.100403

1. phupaboon2023molecularandbiotechnological pages 3-5
2. zhao2024decouplingbetweenthe pages 7-9
3. zhao2024decouplingbetweenthe pages 1-2
4. tinta2023jellyfishdetritussupports pages 15-17
5. rizwan2023bioactivepeptidesfrom pages 6-8
6. feliperuiz2024extracellularproteolysisof pages 1-2
7. zhao2024decouplingbetweenthe pages 9-12
8. wasmund2024thepredictedsecreted pages 1-2
9. moyo2024urgingbioactivepeptide pages 8-10
10. wasmund2024thepredictedsecreted pages 10-15
11. feliperuiz2024extracellularproteolysisof pages 5-7
12. feliperuiz2024extracellularproteolysisof pages 11-13
13. feliperuiz2024extracellularproteolysisof pages 22-23
14. ren2024quercetinapromising pages 15-17
15. ren2024quercetinapromising pages 1-2
16. phupaboon2023molecularandbiotechnological pages 1-3
17. GO:0008233 proteinase activity; label-only extracellular protease
18. METPO:traitmech:000116
19. label-only; prtS gene in some taxa
20. CHEBI:36080 protein
21. label-only
22. CHEBI:16670 peptide
23. KEGG:oppABCDF; GO:0015410 ATPase-coupled oligopeptide transmembrane transporter activity
24. CHEBI:25676 oligopeptide
25. label-only; di/tripeptide transporter
26. KEGG:dppABCDF; label-only Dpp
27. label-only aggregate
28. GO:0008238 exopeptidase activity; GO:0004175 endopeptidase activity
29. GO:0008238; GO:0004175
30. CHEBI:33709 amino acid
31. label-only; aminopeptidase N family
32. CHEBI:46761 dipeptide; CHEBI:47923 tripeptide; CHEBI:33709 amino acid
33. GO:0044248 cellular catabolic process; label-only extracellular hydrolysis
34. label-only small molecules
35. label-only; GO:0043190 ATP-binding cassette (ABC) transporter complex
36. GO:0015344 siderophore transmembrane transporter activity or label-only TonB receptor
37. label-only environmental factor
38. label-only secretory peptidases
39. NCBITaxon:186803? label-only family
40. NCBITaxon:641? label-only family
41. ENVO:marine detritus label-only
42. label-only; EC:3.4.24.- metalloprotease families M9A/M9B
43. ENVO:wastewater sludge label-only
44. label-only; GO:0009372 quorum sensing?
45. KEGG:oppABCDF
46. label-only mature pheromone
47. label-only; Bacillus extracellular protease
48. gene/protein label-only; UniProt label-only
49. CHEBI:16243 quercetin
50. label-only experimental factor
51. https://doi.org/10.1186/s43014-023-00165-w
52. https://doi.org/10.1186/s43014-024-00265-1
53. https://doi.org/10.1128/spectrum.03036-23
54. https://doi.org/10.1186/s40168-023-01598-8
55. https://doi.org/10.1128/msystems.00301-24
56. https://doi.org/10.1371/journal.pbio.3002744
57. https://doi.org/10.1007/s00253-023-12890-w
58. https://doi.org/10.3934/microbiol.2023031
59. https://doi.org/10.3390/antibiotics13070619
60. https://doi.org/10.1128/spectrum.03036-23,
61. https://doi.org/10.1186/s40168-023-01598-8,
62. https://doi.org/10.1186/s43014-023-00165-w,
63. https://doi.org/10.1186/s43014-024-00265-1,
64. https://doi.org/10.3934/microbiol.2023031,
65. https://doi.org/10.1007/s00253-023-12890-w,
66. https://doi.org/10.1371/journal.pbio.3002744,
67. https://doi.org/10.1128/msystems.00301-24,
68. https://doi.org/10.3390/antibiotics13070619,