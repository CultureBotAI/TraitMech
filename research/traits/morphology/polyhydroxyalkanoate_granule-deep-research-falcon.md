---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T09:34:32.119853'
end_time: '2026-08-04T09:42:10.765546'
duration_seconds: 458.65
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: polyhydroxyalkanoate granule
  trait_identifier: traitmech:000067
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: polyhydroxyalkanoate_granule
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An intracellular storage inclusion composed of polyhydroxyalkanoate
    (e.g. polyhydroxybutyrate, PHB), a carbon and energy reserve accumulated as cytoplasmic
    granules.
  parent_traits: traitmech:000066
  synonyms: PHB granule, polyhydroxybutyrate inclusion
  evidence_summary: 'DOI:10.1128/mr.54.4.450-472.1990:  (Anderson & Dawes describe
    polyhydroxyalkanoates (chiefly PHB) as carbon/energy reserves stored as cytoplasmic
    granules.) | DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow include storage
    granules such as PHA bodies among bacterial intracellular organelles.)'
  causal_graph_summary: 'pha_granule_carbon_energy_storage: 14 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** polyhydroxyalkanoate granule
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000067
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An intracellular storage inclusion composed of polyhydroxyalkanoate (e.g. polyhydroxybutyrate, PHB), a carbon and energy reserve accumulated as cytoplasmic granules.
- **Parent traits:** traitmech:000066
- **Synonyms:** PHB granule, polyhydroxybutyrate inclusion
- **Existing evidence:** DOI:10.1128/mr.54.4.450-472.1990:  (Anderson & Dawes describe polyhydroxyalkanoates (chiefly PHB) as carbon/energy reserves stored as cytoplasmic granules.) | DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow include storage granules such as PHA bodies among bacterial intracellular organelles.)
- **Existing causal graph summary:** pha_granule_carbon_energy_storage: 14 nodes, 10 edges

## Research Objective

Research the microbial trait **polyhydroxyalkanoate granule** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/polyhydroxyalkanoate_granule.yaml`.

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


## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** polyhydroxyalkanoate granule
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000067
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An intracellular storage inclusion composed of polyhydroxyalkanoate (e.g. polyhydroxybutyrate, PHB), a carbon and energy reserve accumulated as cytoplasmic granules.
- **Parent traits:** traitmech:000066
- **Synonyms:** PHB granule, polyhydroxybutyrate inclusion
- **Existing evidence:** DOI:10.1128/mr.54.4.450-472.1990:  (Anderson & Dawes describe polyhydroxyalkanoates (chiefly PHB) as carbon/energy reserves stored as cytoplasmic granules.) | DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow include storage granules such as PHA bodies among bacterial intracellular organelles.)
- **Existing causal graph summary:** pha_granule_carbon_energy_storage: 14 nodes, 10 edges

## Research Objective

Research the microbial trait **polyhydroxyalkanoate granule** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/polyhydroxyalkanoate_granule.yaml`.

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


# Curation-focused research report: polyhydroxyalkanoate granule

## 1. Trait record and scope

- **Trait label:** polyhydroxyalkanoate granule
- **Trait identifier:** `traitmech:000067`
- **Category / kind / status:** MORPHOLOGY / CLASS / REVIEWED
- **Parent:** `traitmech:000066`
- **Synonyms:** PHB granule; polyhydroxybutyrate inclusion

### Recommended operational definition

An intracellular, usually approximately spherical inclusion containing an amorphous polyhydroxyalkanoate (PHA) polymer core and a surface enriched in granule-associated proteins. It functions principally as a dynamic carbon, energy, and reducing-equivalent reservoir. “Carbonosome” is used for the organelle-like granule-plus-protein complex. In *Ralstonia eutropha*/*Cupriavidus necator*, typical granules are reported as approximately **0.2–0.5 µm in diameter**. PHA accumulation is commonly induced when carbon remains available while another nutrient—especially nitrogen or phosphorus—limits growth. (gonzalezrojo2024advancesinmicrobial pages 2-4, bresan2016polyhydroxyalkanoate(pha)granules pages 1-2, santolin2024elucidatingregulationof pages 1-2)

The morphological trait should mean **presence or formation of the intracellular granule**, not merely possession of `pha` genes, detectable PHA monomers, or production of purified polymer. PHA synthesis is the causal process; the granule is its cellular morphological outcome.

### Boundaries

**Include:**

1. Intracellular PHB, PHBV, short-chain-length PHA, or medium-chain-length PHA inclusions.
2. Native and engineered granules when an intracellular inclusion is demonstrated.
3. Granule number, size, localization, protein coating, nucleoid association, and partitioning mechanisms.
4. Carbonosomes containing synthases, depolymerases, phasins, and regulatory/localization proteins.

**Exclude or model separately:**

1. Soluble 3-hydroxyacyl-CoA precursors without polymer or granules.
2. Bulk PHA concentration or extracted bioplastic without evidence of intracellular inclusions.
3. Extracellular polymer, generic protein inclusion bodies, glycogen granules, sulfur globules, lipid droplets, and magnetosomes.
4. Polymer composition—PHB versus PHBV or medium-chain-length PHA—as a material/compositional attribute rather than a separate granule-presence phenotype.
5. “Membrane-bounded organelle” as a defining property. In vivo analysis in three proteobacterial representatives found no phospholipid layer around PHA granules; the observed surface was consistent with proteins rather than a canonical membrane. (bresan2016polyhydroxyalkanoate(pha)granules pages 1-2)

## 2. Current mechanistic model

Under excess carbon and growth limitation, metabolism channels carbon into hydroxyacyl-CoA precursors. In the canonical PHB route, PhaA condenses two acetyl-CoA molecules, PhaB reduces acetoacetyl-CoA, and PhaC polymerizes (R)-3-hydroxybutyryl-CoA. Hydrophobic polymer accumulates as a cytoplasmic core whose interface is populated by phasins and metabolic/regulatory proteins. Phasins constrain coalescence and surface-to-volume ratio, while taxon-specific systems such as PhaM–nucleoid coupling in *C. necator* and PhaF–nucleoid coupling in *P. putida* position and partition granules. PhaZ depolymerases mobilize stored polymer when carbon or energy is required. (gonzalezrojo2024advancesinmicrobial pages 2-4, galan2011nucleoid‐associatedphafphasin pages 1-2, santolin2024elucidatingregulationof pages 1-2, kelly2024comprehensiveproteomicsanalysis pages 1-3)

This model is better supported than older “membrane budding” cartoons. Micelle, budding, and scaffold/mediation-element models have all been proposed, but granule initiation is not sufficiently universal to curate one of them as the general bacterial mechanism. The phospholipid-free in vivo result directly contradicts treating a lipid monolayer as universal. (bresan2016polyhydroxyalkanoate(pha)granules pages 1-2, galan2011nucleoid‐associatedphafphasin pages 9-10)

## 3. Candidate nodes

### Environmental and experimental factors

- Excess or surplus carbon source
- Nitrogen limitation
- Phosphorus limitation
- Sulfur limitation — candidate, less universal
- Oxygen limitation — context-dependent; PHA can act as an electron sink
- Nutrient imbalance / growth limitation
- Carbon starvation or renewed growth, promoting reserve mobilization
- Fed-batch fermentation
- Engineered high PhaC dosage
- Renewable or waste-derived carbon feedstock

Candidate grounding includes **ENVO** terms for the specific culture environment when available; otherwise retain label-only experimental-condition nodes. Do not collapse nitrogen, phosphorus, sulfur, and oxygen limitation into one causal edge because their effects and taxonomic scope differ. Nitrogen limitation is the most commonly applied experimental induction condition. (santolin2024elucidatingregulationof pages 1-2, manoli2023heterologousconstitutiveproduction pages 1-3, kelly2024comprehensiveproteomicsanalysis pages 1-3)

### Chemicals and metabolites

- Acetyl-CoA — `CHEBI:15351`
- Acetoacetyl-CoA — `CHEBI:15345`
- NADPH — `CHEBI:16474`
- (R)-3-hydroxybutanoyl-CoA — use a verified ChEBI record during implementation; do not assign an unverified CURIE
- Poly(3-hydroxybutyrate), PHB — label-only pending exact ontology verification
- Polyhydroxyalkanoate — label-only pending exact polymer-class mapping
- 3-hydroxyacyl-CoA
- Crotonyl-CoA
- Carbon source; nitrogen source; phosphorus source

### Genes, proteins, and enzymes

- **PhaA / PhbA:** acetyl-CoA acetyltransferase, EC `2.3.1.9`
- **PhaB / PhbB:** acetoacetyl-CoA reductase, EC `1.1.1.36`
- **PhaC / PhaC1:** PHA synthase; use organism-specific UniProt and EC records after sequence-level verification
- **PhaZ family:** intracellular PHA depolymerases
- **PhaP1–PhaP8:** phasins in *C. necator*; paralog number and function are taxon-specific
- **PhaR:** granule-responsive transcriptional repressor in *C. necator*
- **PhaM:** PhaC1 activator and nucleoid/granule-associated partitioning protein in *C. necator*
- **PhaF and PhaI:** principal phasins in *P. putida*
- **PhaD:** transcriptional regulator in pseudomonads
- **OprL:** newly supported carbonosome-localized phasin-like component in *P. putida* KT2440
- **PhaJ:** (R)-specific enoyl-CoA hydratase linking β-oxidation to PHA precursors
- **PhaG:** links fatty-acid biosynthesis to hydroxyacyl-CoA precursor supply
- **PhaY hydrolases:** candidate PHA-homeostasis components in *C. necator*
- **H16_B1672, H16_B0227, PpiB:** recently identified candidate regulators of phasin/depolymerase promoters in *R. eutropha*; retain strain-qualified labels
- **IbpA:** provisional engineered-host modifier of heterologous PHA inclusion formation

Use organism-specific UniProt accessions rather than assigning one universal protein identifier to divergent PhaP, PhaZ, PhaM, or PhaF families.

### Processes, structures, and localizations

- PHA biosynthetic process
- PHB biosynthetic process
- PHA depolymerization / reserve mobilization
- PHA granule assembly
- PHA granule localization
- Granule segregation during cell division
- Cytoplasm — `GO:0005737`
- Nucleoid — `GO:0009295`
- PHA granule surface / carbonosome — label-only candidate
- Carbon and energy storage
- Response to nutrient limitation
- Daughter cell

## 4. Candidate causal edges

The following table is the recommended starting set. Direct biochemical and mutant-supported edges are strongest; “moderate” entries should carry taxon or assay qualifiers.

| subject | predicate | object | taxon/context | evidence strength | DOI |
|---|---|---|---|---|---|
| excess carbon plus nitrogen or phosphorus limitation | promotes accumulation of | polyhydroxyalkanoate granules | broad microbial context; adverse conditions with excess C and N/P limitation | strong review-supported, broad but not direct single-taxon experiment (gonzalezrojo2024advancesinmicrobial pages 2-4, bresan2016polyhydroxyalkanoate(pha)granules pages 1-2) | 10.3390/microorganisms12081668 |
| acetyl-CoA + acetyl-CoA | is condensed by PhaA to form | acetoacetyl-CoA | classical PHB biosynthesis pathway | strong review-supported biochemical pathway (gonzalezrojo2024advancesinmicrobial pages 2-4, santolin2024elucidatingregulationof pages 1-2, manoli2023heterologousconstitutiveproduction pages 1-3) | 10.3390/microorganisms12081668 |
| acetoacetyl-CoA | is reduced by PhaB to form | (R)-3-hydroxybutyryl-CoA | classical PHB biosynthesis pathway | strong review-supported biochemical pathway (gonzalezrojo2024advancesinmicrobial pages 2-4, santolin2024elucidatingregulationof pages 1-2, manoli2023heterologousconstitutiveproduction pages 1-3) | 10.3390/microorganisms12081668 |
| (R)-3-hydroxybutyryl-CoA | is polymerized by PhaC/PhaC1 into | PHB/PHA polymer that forms granules | classical PHB biosynthesis pathway; Ralstonia/Cupriavidus and broad producers | strong review-supported biochemical pathway (gonzalezrojo2024advancesinmicrobial pages 2-4, santolin2024elucidatingregulationof pages 1-2, manoli2023heterologousconstitutiveproduction pages 1-3) | 10.3390/microorganisms12081668 |
| phasins (PhaPs) | coat/control surface-to-volume ratio of | PHA granule | Ralstonia eutropha/Cupriavidus necator carbonosomes | strong direct primary evidence for role statement (santolin2024elucidatingregulationof pages 1-2) | 10.1016/j.jbc.2024.107523 |
| phaP1 knockout | causes | less PHB and one very big PHB granule | Ralstonia eutropha | strong direct primary evidence summarized in 2024 primary article intro; taxon-specific (santolin2024elucidatingregulationof pages 1-2) | 10.1016/j.jbc.2024.107523 |
| PhaR | represses transcription of | phaP1 and phaP3 | Ralstonia eutropha; pre-accumulation state | strong direct primary evidence summarized in 2024 primary article intro; taxon-specific (santolin2024elucidatingregulationof pages 1-2) | 10.1016/j.jbc.2024.107523 |
| nascent PHA granules | sequester/recruit | PhaR | Ralstonia eutropha during PHA synthesis | strong direct primary evidence summarized in 2024 primary article intro; taxon-specific (santolin2024elucidatingregulationof pages 1-2) | 10.1016/j.jbc.2024.107523 |
| PhaR binding nascent granules | relieves repression of | phaP1 and phaP3 transcription | Ralstonia eutropha during granule growth | strong direct primary evidence summarized in 2024 primary article intro; taxon-specific (santolin2024elucidatingregulationof pages 1-2) | 10.1016/j.jbc.2024.107523 |
| PhaM | forms initiation complex with | PhaC1 | Ralstonia eutropha; granule biogenesis | moderate: primary-study summary in 2024 article, taxon-specific (santolin2024elucidatingregulationof pages 1-2) | 10.1016/j.jbc.2024.107523 |
| PhaM | attaches | PHA granules to nucleoid region | Ralstonia eutropha | moderate: primary-study summary in 2024 article, taxon-specific (santolin2024elucidatingregulationof pages 1-2) | 10.1016/j.jbc.2024.107523 |
| PhaM-mediated nucleoid attachment | promotes equal segregation of | PHA granules to daughter cells | Ralstonia eutropha | moderate: primary-study summary in 2024 article, taxon-specific (santolin2024elucidatingregulationof pages 1-2) | 10.1016/j.jbc.2024.107523 |
| PhaF N-terminal domain | binds | PHA granules | Pseudomonas putida KT2442 | strong direct primary evidence; taxon-specific (galan2011nucleoid‐associatedphafphasin pages 1-2, galan2011nucleoid‐associatedphafphasin pages 9-10) | 10.1111/j.1365-2958.2010.07450.x |
| PhaF C-terminal domain | binds | DNA/nucleoid non-specifically | Pseudomonas putida KT2442 | strong direct primary evidence; taxon-specific (galan2011nucleoid‐associatedphafphasin pages 1-2, galan2011nucleoid‐associatedphafphasin pages 9-10) | 10.1111/j.1365-2958.2010.07450.x |
| PhaF | localizes | PHA granules to cell center/needle array | Pseudomonas putida KT2442 early growth stage | strong direct primary evidence; taxon-specific (galan2011nucleoid‐associatedphafphasin pages 1-2) | 10.1111/j.1365-2958.2010.07450.x |
| loss of PhaF | causes unbalanced segregation of | PHA granules during cell division | Pseudomonas putida KT2442 | strong direct primary evidence; taxon-specific (galan2011nucleoid‐associatedphafphasin pages 1-2, galan2011nucleoid‐associatedphafphasin pages 9-10) | 10.1111/j.1365-2958.2010.07450.x |
| PhaZ/PHA depolymerases | depolymerize/mobilize | stored PHA/PHB granule polymer | broad PHA producers; multiple phaZ genes in Ralstonia eutropha | moderate: direct role broadly established, retrieved text mainly background/review framing (bresan2016polyhydroxyalkanoate(pha)granules pages 1-2, santolin2024elucidatingregulationof pages 1-2) | 10.1038/srep26612 |
| PHA granule surface | lacks in vivo phospholipid | phospholipid layer | Ralstonia eutropha, Pseudomonas putida, Magnetospirillum gryphiswaldense; in vivo localization assay | strong direct primary evidence across taxa (bresan2016polyhydroxyalkanoate(pha)granules pages 1-2) | 10.1038/srep26612 |
| high PhaC synthase dosage | inversely correlates with | granule size distribution | heterologous scl-PHA production in Pseudomonas putida KT2440 | strong direct primary evidence; engineered/assay-specific, provisional for broad curation (manoli2023heterologousconstitutiveproduction pages 1-3) | 10.3389/fbioe.2023.1275036 |
| OprL | localizes to | carbonosome/PHA granule | Pseudomonas putida KT2440 proteomics and localization study | strong direct primary evidence; taxon-specific and newly proposed phasin (kelly2024comprehensiveproteomicsanalysis pages 1-3) | 10.1016/j.mcpro.2024.100765 |
| OprL perturbation | causes | PHA-related phenotype consistent with phasin function | Pseudomonas putida KT2440 | moderate-to-strong direct primary evidence; provisional until independently replicated (kelly2024comprehensiveproteomicsanalysis pages 1-3) | 10.1016/j.mcpro.2024.100765 |


*Table: This table summarizes strong, curation-ready causal edges for the polyhydroxyalkanoate granule trait, emphasizing mechanistic links, taxon specificity, and provisional findings. It is useful as a starting edge set for TraitMech graph construction and review.*

### Supporting snippets and interpretation

1. **Carbon excess plus nutrient limitation → granule accumulation.** A 2024 review states that PHAs are produced “as an energy reserve in the form of granules” mainly under excess carbon with nitrogen or phosphorus limitation. The 2016 in vivo structural study similarly reports accumulation with surplus carbon and limitation of a non-carbon nutrient. This is a robust broad edge, but individual organisms may accumulate PHA under balanced growth or other stresses. (gonzalezrojo2024advancesinmicrobial pages 2-4, bresan2016polyhydroxyalkanoate(pha)granules pages 1-2)

2. **PhaA → acetoacetyl-CoA.** The canonical route is explicitly described as condensation of two acetyl-CoA molecules by PhaA/3-ketothiolase. Curate as a biochemical conversion, not as PhaA directly “creating a granule.” (gonzalezrojo2024advancesinmicrobial pages 2-4, santolin2024elucidatingregulationof pages 1-2, manoli2023heterologousconstitutiveproduction pages 1-3)

3. **PhaB → (R)-3-hydroxybutyryl-CoA.** PhaB is described as the NADPH-dependent reduction step. This supplies the immediate PHB synthase substrate. (gonzalezrojo2024advancesinmicrobial pages 2-4, manoli2023heterologousconstitutiveproduction pages 1-3)

4. **PhaC → PHB polymerization.** PhaC/PhaC1 polymerizes hydroxybutyryl-CoA into PHB. Polymerization is necessary for the granule phenotype, but the number and dimensions of granules also depend on protein dosage and surface factors. (gonzalezrojo2024advancesinmicrobial pages 2-4, santolin2024elucidatingregulationof pages 1-2)

5. **Phasins → granule surface organization.** Phasins are amphiphilic proteins that control granule surface-to-volume ratio. In a *R. eutropha* `phaP1` knockout, cells produced less PHB and “only one very big PHB granule,” supporting a causal role in limiting coalescence and controlling morphology. This edge is strong but the specific paralog is taxon-dependent. (santolin2024elucidatingregulationof pages 1-2)

6. **PhaR feedback regulation.** PhaR binds the `phaP1` and `phaP3` promoters and represses transcription. During synthesis, PhaR binds nascent granules, relieving repression; when phasins occupy the mature surface, free PhaR again represses transcription. This is a mechanistically attractive granule-sensing feedback loop, but it should be restricted to *R. eutropha/C. necator* unless demonstrated elsewhere. (santolin2024elucidatingregulationof pages 7-8, santolin2024elucidatingregulationof pages 1-2)

7. **PhaM → nucleoid attachment and partitioning.** PhaM forms an initiation complex with PhaC1, attaches granules to the nucleoid region, and supports equal daughter-cell distribution. Curate as a *C. necator*-specific branch rather than a universal bacterial mechanism. (santolin2024elucidatingregulationof pages 1-2)

8. **PhaF → localization and segregation.** In *P. putida* KT2442, PhaF has an N-terminal granule-binding domain and C-terminal nonspecific DNA-binding region. Deletion produced cells with and without PHA, whereas complementation restored balanced segregation; the study concludes that PhaF directs granules to the cell center and supports distribution to daughter cells. The exact physical positioning mechanism remains unresolved. (galan2011nucleoid‐associatedphafphasin pages 1-2, galan2011nucleoid‐associatedphafphasin pages 9-10)

9. **PhaZ → reserve mobilization.** PHA depolymerases are granule-associated catabolic enzymes that mediate polymer depolymerization. Because retrieved passages chiefly provide system-level background rather than one definitive deletion experiment, curate the general biochemical edge, but avoid assigning every annotated `phaZ` paralog the same in vivo role. (bresan2016polyhydroxyalkanoate(pha)granules pages 1-2, santolin2024elucidatingregulationof pages 1-2)

10. **Granule surface ┤ phospholipid layer.** Fluorescent phospholipid-binding probes localized to cytoplasmic membranes and magnetosomes but not PHB/PHA granules in *R. eutropha*, *P. putida*, or *Magnetospirillum gryphiswaldense*. The authors conclude that these granules have no phospholipids in vivo and propose a protein-only surface. This is strong negative evidence across three taxa, although it does not formally exclude unusual lipid-associated granules in every prokaryote. (bresan2016polyhydroxyalkanoate(pha)granules pages 1-2)

11. **PhaC dosage → granule size.** A 2023 engineered *P. putida* study found an inverse relationship between PhaC dosage and granule-size distribution. It also obtained **23–84% PHA/cell dry weight** across constructs and **68% PHA/CDW** with a chromosomally integrated, high-PhaC system. This edge is useful for an experimental-factor branch but should not be generalized to native physiology. (manoli2023heterologousconstitutiveproduction pages 1-3)

12. **OprL → carbonosome association.** A 2024 proteomics/localization study identified OprL at the carbonosome and reported a PHA-related perturbation phenotype, supporting its classification as a new phasin. Because OprL is also the Pal component of the Tol–Pal envelope system, its granule role should be qualified as *P. putida* KT2440-specific and provisional pending independent replication. (kelly2024comprehensiveproteomicsanalysis pages 1-3)

13. **New transcriptional regulators.** A 2024 JBC study showed that H16_B1672 binds the `phaP1` promoter with **KD 175 nM** and represses expression in vivo; interactions with `phaZ3` and `phaZ5` promoters suggest broader homeostatic regulation. H16_B0227 and PpiB affected `PphaP1` and `PphaZ3`, respectively, but some DNA-binding mechanisms remain incompletely demonstrated. These should enter an extension graph with evidence-method qualifiers, not the minimal conserved graph. (santolin2024elucidatingregulationof pages 7-8, santolin2024elucidatingregulationof pages 1-2)

## 5. Recent developments, applications, and quantitative context

### 2023–2024 mechanistic advances

- **Programmable granule morphology:** Modular expression of heterologous short-chain-length PHA pathways in *P. putida* demonstrated that synthase dosage can tune granule-size distribution and produce 23–84% PHA/CDW. This links pathway engineering directly to an observable morphological parameter. (manoli2023heterologousconstitutiveproduction pages 1-3)
- **Expanded carbonosome proteome:** Multi-layer proteomics in *P. putida* generated a 434-protein interaction network and identified OprL as a carbonosome-localized phasin candidate. The same study compared 0.1 g/L versus 6 g/L nitrogen conditions, illustrating how nutrient-state proteomics can identify causal graph components. (kelly2024comprehensiveproteomicsanalysis pages 1-3)
- **Regulatory network expansion:** The 2024 JBC study moved beyond the classical PhaR model by identifying H16_B1672, H16_B0227, and PpiB as candidate regulators of phasin/depolymerase expression. Its authors emphasize that PHA homeostasis is integrated with central metabolism and stress responses rather than being a simple on/off storage pathway. (santolin2024elucidatingregulationof pages 7-8, santolin2024elucidatingregulationof pages 1-2)

### Real-world and emerging applications

1. **Bioplastic cell factories:** *C. necator*, *P. putida*, *Halomonas*, recombinant *E. coli*, and *Bacillus* are major production chassis. A 2024 source estimates that *R. eutropha/C. necator* accounts for approximately **40% of annual PHA production**, although this is an industrial estimate and should not be represented as a biological graph edge. (gonzalezrojo2024advancesinmicrobial pages 2-4, santolin2024elucidatingregulationof pages 1-2)
2. **Waste valorization:** Current development emphasizes agricultural wastes and industrial by-products as renewable carbon sources, coupled with fed-batch or continuous cultivation. These are production-context nodes, not intrinsic causes of the morphology unless the substrate-to-granule link is experimentally measured in a specified strain. (gonzalezrojo2024advancesinmicrobial pages 2-4)
3. **Tailored materials:** Altering precursor pathways and synthase specificity enables PHB, PHBV, and medium-chain-length polymers with different crystallinity, melting behavior, flexibility, and biomedical or packaging utility. Polymer chemistry should be downstream of granule formation in the graph. (gonzalezrojo2024advancesinmicrobial pages 2-4, manoli2023heterologousconstitutiveproduction pages 1-3)
4. **Granule surface engineering:** Phasin-mediated display can immobilize proteins on intracellular granules, creating affinity, vaccine, or biocatalytic particles. Such engineered display is an application of the granule scaffold and should not be conflated with the native morphological definition.
5. **Stress resilience:** Recent authoritative analysis describes PHA reservoirs as supporting resistance to UV, oxidative, osmotic, and temperature stresses and, under oxygen limitation, acting as electron sinks. These are plausible downstream consequences of PHA homeostasis, but many are taxon- and assay-specific and need primary-study support before inclusion in the core graph. (santolin2024elucidatingregulationof pages 1-2, kelly2024comprehensiveproteomicsanalysis pages 1-3)

## 6. Recommended minimal TraitMech graph

For a conservative first revision of `polyhydroxyalkanoate_granule.yaml`, prioritize:

1. `excess carbon` + `nitrogen or phosphorus limitation` → **promotes** → `PHA accumulation`.
2. `acetyl-CoA` → **PhaA-catalyzed conversion** → `acetoacetyl-CoA`.
3. `acetoacetyl-CoA` → **PhaB-catalyzed conversion** → `(R)-3-hydroxybutyryl-CoA`.
4. `(R)-3-hydroxybutyryl-CoA` → **PhaC-catalyzed polymerization** → `PHB polymer`.
5. `PHB/PHA polymer accumulation` → **forms** → `traitmech:000067`.
6. `phasin binding` → **organizes/stabilizes** → `PHA granule surface and size`.
7. `PhaZ activity` → **mobilizes/depolymerizes** → `PHA granule polymer`.
8. Taxon-qualified branches for `PhaM` in *C. necator* and `PhaF` in *P. putida* → **nucleoid coupling/localization/segregation**.
9. `PHA granule` → **has component** → `PHA polymer core` and `granule-associated proteins`.
10. Encode “no phospholipid layer detected in vivo” as a negative compositional assertion only if the YAML schema supports negation and taxonomic/evidence qualifiers.

## 7. Warnings: claims not yet ready for broad curation

- **Do not curate a universal phospholipid monolayer.** Older diagrams and the 2011 PhaF paper reproduce this model, but the 2016 in vivo study found no phospholipids. (bresan2016polyhydroxyalkanoate(pha)granules pages 1-2, galan2011nucleoid‐associatedphafphasin pages 1-2)
- **Do not universalize PhaF or PhaM.** They are analogous partitioning solutions in different taxa, not demonstrated orthologous universal machinery.
- **Do not equate a `phaC` gene with the phenotype.** Functional expression, precursor supply, and polymer accumulation are required.
- **Do not treat nitrogen limitation as necessary.** It is a common experimental trigger, not an absolute requirement in all organisms or engineered strains.
- **Do not merge PHB, PHBV, and mcl-PHA chemistry.** They share granule morphology but use partly different precursor pathways and synthases.
- **Keep OprL and IbpA provisional.** OprL has strong 2024 evidence but a newly assigned dual role; IbpA involvement was proposed in a heterologous engineered system. (manoli2023heterologousconstitutiveproduction pages 1-3, kelly2024comprehensiveproteomicsanalysis pages 1-3)
- **Qualify new regulators.** H16_B1672 has direct binding and reporter evidence, whereas some H16_B0227/PpiB mechanisms are partly inferred or lack direct DNA-binding confirmation. (santolin2024elucidatingregulationof pages 7-8, santolin2024elucidatingregulationof pages 1-2)
- **Avoid broad stress-protection edges** until the specific stress, organism, perturbation, and phenotype are supported by primary evidence.
- **Verify all ontology identifiers at implementation time.** In particular, polymer entities, individual PhaC/PhaZ families, and organism-specific proteins require database and sequence-specific grounding.

## 8. DOI-first bibliography

1. Santolin L. et al. **Elucidating regulation of polyhydroxyalkanoate metabolism in *Ralstonia eutropha*.** *Journal of Biological Chemistry* 300, 107523. Published online **4 July 2024**. DOI: [10.1016/j.jbc.2024.107523](https://doi.org/10.1016/j.jbc.2024.107523). (santolin2024elucidatingregulationof pages 7-8, santolin2024elucidatingregulationof pages 1-2)
2. Kelly S. et al. **Comprehensive Proteomics Analysis of PHA Biology in *Pseudomonas putida* KT2440: OprL is a Newly Identified Phasin.** *Molecular & Cellular Proteomics* 23, 100765. **May 2024**. DOI: [10.1016/j.mcpro.2024.100765](https://doi.org/10.1016/j.mcpro.2024.100765). (kelly2024comprehensiveproteomicsanalysis pages 1-3)
3. González-Rojo S. et al. **Advances in Microbial Biotechnology for Sustainable Alternatives to Petroleum-Based Plastics.** *Microorganisms* 12, 1668. **August 2024**. DOI: [10.3390/microorganisms12081668](https://doi.org/10.3390/microorganisms12081668). (gonzalezrojo2024advancesinmicrobial pages 2-4)
4. Manoli M.-T. et al. **Heterologous constitutive production of short-chain-length PHAs in *P. putida* KT2440.** *Frontiers in Bioengineering and Biotechnology* 11, 1275036. Published **1 November 2023**. DOI: [10.3389/fbioe.2023.1275036](https://doi.org/10.3389/fbioe.2023.1275036). (manoli2023heterologousconstitutiveproduction pages 1-3)
5. Bresan S. et al. **Polyhydroxyalkanoate (PHA) Granules Have no Phospholipids.** *Scientific Reports* 6, 26612. Published **25 May 2016**. DOI: [10.1038/srep26612](https://doi.org/10.1038/srep26612). (bresan2016polyhydroxyalkanoate(pha)granules pages 1-2)
6. Mezzina M.P., Pettinari M.J. **Phasins, Multifaceted Polyhydroxyalkanoate Granule-Associated Proteins.** *Applied and Environmental Microbiology* 82, 5060–5067. **September 2016**. DOI: [10.1128/AEM.01161-16](https://doi.org/10.1128/AEM.01161-16). (mezzina2016phasinsmultifacetedpolyhydroxyalkanoate pages 21-24)
7. Galán B. et al. **Nucleoid-associated PhaF phasin drives intracellular location and segregation of PHA granules in *P. putida* KT2442.** *Molecular Microbiology* 79, 402–418. First published **16 November 2010**; issue **2011**. DOI: [10.1111/j.1365-2958.2010.07450.x](https://doi.org/10.1111/j.1365-2958.2010.07450.x). (galan2011nucleoid‐associatedphafphasin pages 1-2, galan2011nucleoid‐associatedphafphasin pages 9-10)
8. Mezzina M.P. et al. **Engineering Native and Synthetic Pathways in *Pseudomonas putida* for Tailored PHAs.** *Biotechnology Journal* 16. **2021**. DOI: [10.1002/biot.202000165](https://doi.org/10.1002/biot.202000165). (mezzina2021engineeringnativeand pages 16-19)

References

1. (gonzalezrojo2024advancesinmicrobial pages 2-4): Silvia González-Rojo, Ana Isabel Paniagua-García, and Rebeca Díez-Antolínez. Advances in microbial biotechnology for sustainable alternatives to petroleum-based plastics: a comprehensive review of polyhydroxyalkanoate production. Microorganisms, 12:1668, Aug 2024. URL: https://doi.org/10.3390/microorganisms12081668, doi:10.3390/microorganisms12081668. This article has 36 citations.

2. (bresan2016polyhydroxyalkanoate(pha)granules pages 1-2): Stephanie Bresan, Anna Sznajder, Waldemar Hauf, Karl Forchhammer, Daniel Pfeiffer, and Dieter Jendrossek. Polyhydroxyalkanoate (pha) granules have no phospholipids. Scientific Reports, May 2016. URL: https://doi.org/10.1038/srep26612, doi:10.1038/srep26612. This article has 169 citations and is from a peer-reviewed journal.

3. (santolin2024elucidatingregulationof pages 1-2): Lara Santolin, Rosalie Sandra Josianne Eichenroth, Paul Cornehl, Henrike Wortmann, Christian Forbrig, Anne Schulze, Inam Ul Haq, Sabine Brantl, Juri Rappsilber, Sebastian Lothar Riedel, Peter Neubauer, and Matthias Gimpel. Elucidating regulation of polyhydroxyalkanoate metabolism in ralstonia eutropha: identification of transcriptional regulators from phasin and depolymerase genes. Journal of Biological Chemistry, 300:107523, Aug 2024. URL: https://doi.org/10.1016/j.jbc.2024.107523, doi:10.1016/j.jbc.2024.107523. This article has 9 citations and is from a domain leading peer-reviewed journal.

4. (galan2011nucleoid‐associatedphafphasin pages 1-2): B. Galán, N. Dinjaski, B. Maestro, L. I. de Eugenio, I. F. Escapa, J. M. Sanz, J. L. García, and M. A. Prieto. Nucleoid‐associated phaf phasin drives intracellular location and segregation of polyhydroxyalkanoate granules in pseudomonas putida kt2442. Molecular Microbiology, 79:402-418, Jan 2011. URL: https://doi.org/10.1111/j.1365-2958.2010.07450.x, doi:10.1111/j.1365-2958.2010.07450.x. This article has 164 citations and is from a domain leading peer-reviewed journal.

5. (kelly2024comprehensiveproteomicsanalysis pages 1-3): Siobhán Kelly, Jia-Lynn Tham, Kate McKeever, Eugène Dillon, David J. O’Connell, Dimitri Scholz, Jeremy C. Simpson, Kevin E O'Connor, T. Narančić, and Gerard Cagney. Comprehensive proteomics analysis of polyhydroxyalkanoate (pha) biology in pseudomonas putida kt2440: the outer membrane lipoprotein oprl is a newly identified phasin. Molecular &amp; Cellular Proteomics, 23:100765, May 2024. URL: https://doi.org/10.1016/j.mcpro.2024.100765, doi:10.1016/j.mcpro.2024.100765. This article has 13 citations and is from a domain leading peer-reviewed journal.

6. (galan2011nucleoid‐associatedphafphasin pages 9-10): B. Galán, N. Dinjaski, B. Maestro, L. I. de Eugenio, I. F. Escapa, J. M. Sanz, J. L. García, and M. A. Prieto. Nucleoid‐associated phaf phasin drives intracellular location and segregation of polyhydroxyalkanoate granules in pseudomonas putida kt2442. Molecular Microbiology, 79:402-418, Jan 2011. URL: https://doi.org/10.1111/j.1365-2958.2010.07450.x, doi:10.1111/j.1365-2958.2010.07450.x. This article has 164 citations and is from a domain leading peer-reviewed journal.

7. (manoli2023heterologousconstitutiveproduction pages 1-3): Maria-Tsampika Manoli, Francisco G. Blanco, Virginia Rivero-Buceta, Ryan Kniewel, Sandra Herrera Alarcon, Sergio Salgado, and M. Auxiliadora Prieto. Heterologous constitutive production of short-chain-length polyhydroxyalkanoates in pseudomonas putida kt2440: the involvement of ibpa inclusion body protein. Frontiers in Bioengineering and Biotechnology, Nov 2023. URL: https://doi.org/10.3389/fbioe.2023.1275036, doi:10.3389/fbioe.2023.1275036. This article has 13 citations.

8. (santolin2024elucidatingregulationof pages 7-8): Lara Santolin, Rosalie Sandra Josianne Eichenroth, Paul Cornehl, Henrike Wortmann, Christian Forbrig, Anne Schulze, Inam Ul Haq, Sabine Brantl, Juri Rappsilber, Sebastian Lothar Riedel, Peter Neubauer, and Matthias Gimpel. Elucidating regulation of polyhydroxyalkanoate metabolism in ralstonia eutropha: identification of transcriptional regulators from phasin and depolymerase genes. Journal of Biological Chemistry, 300:107523, Aug 2024. URL: https://doi.org/10.1016/j.jbc.2024.107523, doi:10.1016/j.jbc.2024.107523. This article has 9 citations and is from a domain leading peer-reviewed journal.

9. (mezzina2016phasinsmultifacetedpolyhydroxyalkanoate pages 21-24): Mariela P. Mezzina and M. Julia Pettinari. Phasins, multifaceted polyhydroxyalkanoate granule-associated proteins. Applied and Environmental Microbiology, 82:5060-5067, Sep 2016. URL: https://doi.org/10.1128/aem.01161-16, doi:10.1128/aem.01161-16. This article has 152 citations and is from a peer-reviewed journal.

10. (mezzina2021engineeringnativeand pages 16-19): Mariela P. Mezzina, María Tsampika Manoli, M. Auxiliadora Prieto, and Pablo I. Nikel. Engineering native and synthetic pathways in <i>pseudomonas putida</i> for the production of tailored polyhydroxyalkanoates. Biotechnology Journal, Nov 2021. URL: https://doi.org/10.1002/biot.202000165, doi:10.1002/biot.202000165. This article has 155 citations and is from a peer-reviewed journal.