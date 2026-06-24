# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** trophic type
- **METPO identifier:** METPO:1000631
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that is describing how an organism obtains carbon, energy, and electron donors for growth and metabolism.
- **Parent traits:** METPO:1000059
- **Synonyms:** Physiology and metabolism.nutrition type.type, nutritional type, pathways
- **Existing evidence:** DOI:10.1146/annurev.micro.61.080706.093130: carbon source, energy source, and electron donor (Microbial physiology review frames trophic type as the joint classification by carbon, energy, and electron-donor source.) | DOI:10.1073/pnas.0903507106: molecular mechanisms of adaptation (Comparative genomics supports the classification of bacteria by trophic strategy from genome-encoded pathways.)
- **Existing causal graph summary:** trophic_type_classification_axes: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **trophic type** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/trophic_type.yaml`.

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
**Generated:** 2026-06-18T12:55:12.026997

1. lauro2009thegenomicbasis pages 1-2
2. laderriere2026bactotraitsatrait pages 5-6
3. jahn2024theenergymetabolism pages 1-2
4. tothero2024leptothrixochraceagenomes pages 13-15
5. wang2024novelisolatesof pages 12-15
6. tothero2024leptothrixochraceagenomes pages 9-13
7. gellermcgrath2024predictingmetabolicmodules pages 4-6
8. giordano2024genomescalecommunitymodelling pages 7-9
9. tothero2024leptothrixochraceagenomes pages 1-2
10. tothero2024leptothrixochraceagenomes pages 15-16
11. ramoneda2024leveraginggenomicinformation pages 1-2
12. gellermcgrath2024predictingmetabolicmodules pages 2-4
13. giordano2024genomescalecommunitymodelling pages 1-2
14. giordano2024genomescalecommunitymodelling pages 9-9
15. ramoneda2024leveraginggenomicinformation pages 4-6
16. ramoneda2024leveraginggenomicinformation pages 7-7
17. bergo2026microbialsignaturesdefine pages 32-33
18. gellermcgrath2024predictingmetabolicmodules pages 6-9
19. NiFe
20. https://doi.org/10.1128/AEM.00599-24;
21. https://doi.org/10.1128/mSystems.00148-24;
22. https://doi.org/10.1128/AEM.00748-24;
23. https://doi.org/10.7554/eLife.85749;
24. https://doi.org/10.1038/s41467-024-46374-w;
25. https://doi.org/10.1128/aem.00599-24
26. https://doi.org/10.1128/aem.00748-24
27. https://doi.org/10.1128/msystems.00148-24
28. https://doi.org/10.7554/eLife.85749
29. https://doi.org/10.1038/s41467-024-46374-w
30. https://doi.org/10.1093/ismejo/wrae195
31. https://doi.org/10.1038/s41597-026-06652-2
32. https://doi.org/10.1073/pnas.0903507106
33. https://doi.org/10.1038/s41597-026-06652-2,
34. https://doi.org/10.1128/aem.00599-24,
35. https://doi.org/10.1128/aem.00748-24,
36. https://doi.org/10.1093/ismejo/wrae195,
37. https://doi.org/10.1073/pnas.0903507106,
38. https://doi.org/10.7554/elife.85749,
39. https://doi.org/10.1038/s41467-024-46374-w,
40. https://doi.org/10.1101/2025.03.17.643744,
41. https://doi.org/10.1128/msystems.00148-24,