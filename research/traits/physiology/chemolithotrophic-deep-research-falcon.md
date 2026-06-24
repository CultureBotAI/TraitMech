---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T11:01:30.568522'
end_time: '2026-06-18T11:24:42.811514'
duration_seconds: 1392.24
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: chemolithotrophic
  trait_identifier: METPO:1000639
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: chemolithotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type characterized by the use of inorganic chemical compounds
    as electron donors and carbon dioxide as the primary carbon source for energy
    generation and biosynthesis.
  parent_traits: METPO:1000631
  synonyms: chemolithotroph
  evidence_summary: "DOI:10.1016/B978-0-12-378630-2.00219-X: chemolithotrophic bacteria\
    \ and archaea (Review supports inorganic compound oxidation as chemolithotrophic\
    \ growth.) | DOI:10.1146/annurev.micro.55.1.485: Chemolitho-autotrophic ammonia-oxidizing\
    \ bacteria (Review supports ammonia oxidation as an example chemolithoautotrophic\
    \ process.) | PMID:12700255: Nitrosomonas europaea (Organism example: Nitrosomonas\
    \ europaea is the model chemolithotrophic ammonia-oxidizing bacterium, conserving\
    \ energy from NH3 \u2192 NO2- oxidation (Chain et al. 2003, J Bacteriol, complete\
    \ genome).)"
  causal_graph_summary: 'chemolithotrophic_inorganic_oxidation: 10 nodes, 7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 62
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemolithotrophic
- **METPO identifier:** METPO:1000639
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type characterized by the use of inorganic chemical compounds as electron donors and carbon dioxide as the primary carbon source for energy generation and biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemolithotroph
- **Existing evidence:** DOI:10.1016/B978-0-12-378630-2.00219-X: chemolithotrophic bacteria and archaea (Review supports inorganic compound oxidation as chemolithotrophic growth.) | DOI:10.1146/annurev.micro.55.1.485: Chemolitho-autotrophic ammonia-oxidizing bacteria (Review supports ammonia oxidation as an example chemolithoautotrophic process.) | PMID:12700255: Nitrosomonas europaea (Organism example: Nitrosomonas europaea is the model chemolithotrophic ammonia-oxidizing bacterium, conserving energy from NH3 → NO2- oxidation (Chain et al. 2003, J Bacteriol, complete genome).)
- **Existing causal graph summary:** chemolithotrophic_inorganic_oxidation: 10 nodes, 7 edges

## Research Objective

Research the microbial trait **chemolithotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemolithotrophic.yaml`.

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
- **Trait label:** chemolithotrophic
- **METPO identifier:** METPO:1000639
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type characterized by the use of inorganic chemical compounds as electron donors and carbon dioxide as the primary carbon source for energy generation and biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemolithotroph
- **Existing evidence:** DOI:10.1016/B978-0-12-378630-2.00219-X: chemolithotrophic bacteria and archaea (Review supports inorganic compound oxidation as chemolithotrophic growth.) | DOI:10.1146/annurev.micro.55.1.485: Chemolitho-autotrophic ammonia-oxidizing bacteria (Review supports ammonia oxidation as an example chemolithoautotrophic process.) | PMID:12700255: Nitrosomonas europaea (Organism example: Nitrosomonas europaea is the model chemolithotrophic ammonia-oxidizing bacterium, conserving energy from NH3 → NO2- oxidation (Chain et al. 2003, J Bacteriol, complete genome).)
- **Existing causal graph summary:** chemolithotrophic_inorganic_oxidation: 10 nodes, 7 edges

## Research Objective

Research the microbial trait **chemolithotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemolithotrophic.yaml`.

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


## Chemolithotrophic (METPO:1000639) TraitMech Causal-Graph Research Report

### Trait metadata
- **Trait label:** chemolithotrophic
- **METPO identifier:** METPO:1000639
- **Trait category:** PHYSIOLOGY
- **Definition (curation target):** trophic type using **inorganic chemical compounds as electron donors** and **CO2 as primary carbon source** for energy generation and biosynthesis.

---

## 1) Trait scope (key concepts, definitions, boundary cases)

### 1.1 Working curation scope
Chemolithotrophy in the broader literature is often defined by **inorganic electron donors** but can include organisms that assimilate **organic carbon** (mixotrophy). For METPO:1000639, the curatable scope should align with the reviewed definition: **inorganic electron donors + CO2 (or HCO3−) as the primary carbon source**—i.e., operationally close to *chemolithoautotrophy*. This distinction matters because several organisms possess lithotrophy-related genes but use them for **detoxification** or as a **supplementary** energy source during heterotrophy.

### 1.2 Boundary cases that should constrain curation
- **Chemolithotroph vs chemoautotroph terminology mismatch:** A recent genome/physiology study explicitly distinguishes the two: “chemolithotrophs obtain energy from inorganic sources while taking carbon from organic or inorganic sources; chemoautotrophs obtain both energy and carbon from inorganic sources.” (Alcanivorax study) (chen2024adaptationmechanismsof pages 1-2). This is a key warning that “chemolithotroph” may not imply CO2 fixation in every paper.
- **Sulfur oxidation genes used for detoxification (do not curate as positive evidence of chemolithotrophy):** In *Alcanivorax*, “Adding thiosulfate enhanced … growth,” but “Sqr functions primarily in sulfide detoxification rather than in energy conservation.” (chen2024adaptationmechanismsof pages 1-2). This is a clear example where **sqr/tsdA presence ≠ chemolithotrophy**.
- **Marker-gene decoupling for ammonia oxidizers (AOA):** AOA genomes encode amo and CO2 fixation genes and can grow autotrophically, but environmental observations can decouple amoA transcripts/abundance from ammonia oxidation and/or bicarbonate assimilation (e.g., abundance increases even under acetylene inhibition; bicarbonate assimilation absent in some WWTP biofilms) (cornell2024genomeencodedmetabolicpotential pages 15-18). These are reasons to **avoid trait assertion from amoA alone**.

**Curation implication:** prefer evidence from (i) demonstrated growth with inorganic donor + CO2/HCO3−, (ii) inhibitor/perturbation tests linking donor oxidation to CO2 fixation, or (iii) complete pathway modules plus context-appropriate expression/flux evidence.

---

## 2) Current mechanistic understanding (entities and modules)

### 2.1 Candidate nodes for a TraitMech causal graph
A curation-oriented node inventory with suggested ontology grounding is provided here:

| Node category | Label | Node type | Suggested ontology CURIE(s) | Supporting citations |
|---|---|---|---|---|
| Electron donors | ammonia (NH3) | chemical | CHEBI:16134 | (zhou2023effectsofacidification pages 1-2, han2024adaptivetraitsof pages 9-11) |
| Electron donors | ammonium (NH4+) | chemical | CHEBI:28938 | (zhou2023effectsofacidification pages 1-2, han2024adaptivetraitsof pages 9-11) |
| Electron donors | ferrous iron [Fe(II)] | chemical | CHEBI:29033 | (wang2024characterizethegrowth pages 1-2, jung2024crisprdcas12aknockdownof pages 1-2) |
| Electron donors | thiosulfate | chemical | CHEBI:30085 | (twible2024phandthiosulfate pages 1-2, chen2024adaptationmechanismsof pages 1-2) |
| Electron donors | sulfide | chemical | CHEBI:18421 | (chen2024adaptationmechanismsof pages 1-2, li2024arcobacteraceaeareubiquitous pages 1-2) |
| Electron donors | hydrogen (H2) | chemical | CHEBI:18276 | (beaver2024microbialecologyof pages 2-3, shoemaker2024wood–ljungdahlpathwayencoding pages 1-2) |
| Electron acceptors | oxygen (O2) | chemical | CHEBI:15379 | (wang2024characterizethegrowth pages 1-2, beaver2024microbialecologyof pages 2-3) |
| Electron acceptors | nitrate | chemical | CHEBI:17632 | (li2024arcobacteraceaeareubiquitous pages 1-2, barla2024sustainablesynergisticapproach pages 7-8) |
| Electron acceptors | nitrite | chemical | CHEBI:16301 | (bayer2024contributionofammonia pages 1-4, han2024adaptivetraitsof pages 9-11) |
| Carbon source & fixation pathways | carbon dioxide (CO2) | chemical | CHEBI:16526 | (wang2024characterizethegrowth pages 1-2, barla2024sustainablesynergisticapproach pages 1-2) |
| Carbon source & fixation pathways | bicarbonate (HCO3−) | chemical | CHEBI:17544 | (cornell2024genomeencodedmetabolicpotential pages 13-15, barla2024sustainablesynergisticapproach pages 7-8) |
| Carbon source & fixation pathways | Calvin–Benson–Bassham cycle | pathway | GO:0015977 | (wang2024characterizethegrowth pages 1-2, zhou2023effectsofacidification pages 6-7) |
| Carbon source & fixation pathways | 3-hydroxypropionate/4-hydroxybutyrate cycle | pathway | label-only candidate | (cornell2024genomeencodedmetabolicpotential pages 13-15, zhou2023effectsofacidification pages 6-7) |
| Carbon source & fixation pathways | Wood–Ljungdahl pathway | pathway | GO:0019685 | (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2, beaver2024microbialecologyof pages 2-3) |
| Carbon source & fixation pathways | reverse tricarboxylic acid cycle (rTCA) | pathway | GO:0071941 | (shoemaker2024wood–ljungdahlpathwayencoding pages 9-11, li2024arcobacteraceaeareubiquitous pages 1-2) |
| Carbon source & fixation pathways | dark dissolved inorganic carbon fixation | process | label-only candidate | (bayer2024contributionofammonia pages 1-4, shoemaker2024wood–ljungdahlpathwayencoding pages 1-2) |
| Sulfur oxidation modules | complete Sox pathway (soxXA-soxYZ-soxB-soxCD) | pathway/module | label-only candidate | (twible2024phandthiosulfate pages 1-2, yan2024characterizationofsulfur pages 59-63) |
| Sulfur oxidation modules | incomplete Sox pathway | pathway/module | label-only candidate | (twible2024phandthiosulfate pages 5-6, rudenko2024mechanismofintracellular pages 10-12) |
| Sulfur oxidation modules | SoxAX | enzyme complex | label-only candidate | (twible2024phandthiosulfate pages 1-2, rudenko2024mechanismofintracellular pages 10-12) |
| Sulfur oxidation modules | SoxYZ | sulfur carrier complex | label-only candidate | (twible2024phandthiosulfate pages 1-2, yan2024characterizationofsulfur pages 59-63) |
| Sulfur oxidation modules | SoxB | enzyme | label-only candidate | (twible2024phandthiosulfate pages 1-2, rudenko2024mechanismofintracellular pages 12-13) |
| Sulfur oxidation modules | SoxCD | enzyme complex | label-only candidate | (twible2024phandthiosulfate pages 1-2, twible2024phandthiosulfate pages 5-6) |
| Sulfur oxidation modules | tsdA | enzyme/gene | label-only candidate | (twible2024phandthiosulfate pages 1-2, chen2024adaptationmechanismsof pages 1-2) |
| Sulfur oxidation modules | tetH | enzyme/gene | label-only candidate | (twible2024phandthiosulfate pages 1-2, twible2024phandthiosulfate pages 5-6) |
| Sulfur oxidation modules | reverse dissimilatory sulfite reductase (rDsr) | pathway/module | label-only candidate | (twible2024phandthiosulfate pages 1-2, yan2024characterizationofsulfur pages 59-63) |
| Sulfur oxidation modules | sulfide:quinone oxidoreductase (Sqr) | enzyme/gene | label-only candidate | (chen2024adaptationmechanismsof pages 1-2, rudenko2024mechanismofintracellular pages 10-12) |
| Sulfur oxidation modules | persulfide dioxygenase (PDO) | enzyme/gene | label-only candidate | (rudenko2024mechanismofintracellular pages 12-13, rudenko2024mechanismofintracellular pages 10-12) |
| Sulfur oxidation modules | SoeABC sulfite:quinone oxidoreductase | enzyme complex | label-only candidate | (rudenko2024mechanismofintracellular pages 12-13, cornell2024genomeencodedmetabolicpotential pages 86-89) |
| Nitrogen oxidation modules | ammonia monooxygenase (AMO) | enzyme complex | label-only candidate | (han2024adaptivetraitsof pages 9-11, cornell2024genomeencodedmetabolicpotential pages 13-15) |
| Nitrogen oxidation modules | amoA | gene | label-only candidate | (han2024adaptivetraitsof pages 9-11, cornell2024genomeencodedmetabolicpotential pages 15-18) |
| Nitrogen oxidation modules | amoB | gene | label-only candidate | (zhou2023effectsofacidification pages 6-7, cornell2024genomeencodedmetabolicpotential pages 13-15) |
| Nitrogen oxidation modules | amoC | gene | label-only candidate | (zhou2023effectsofacidification pages 6-7, cornell2024genomeencodedmetabolicpotential pages 13-15) |
| Nitrogen oxidation modules | nirK | gene/enzyme | label-only candidate | (zhou2023effectsofacidification pages 6-7, zhou2023effectsofacidification pages 5-6) |
| Nitrogen oxidation modules | Cu-HAO candidate | enzyme | label-only candidate | (zhou2023effectsofacidification pages 6-7, zhou2023effectsofacidification pages 5-6) |
| Nitrogen oxidation modules | nitrification | process | GO:0038165 | (zhou2023effectsofacidification pages 1-2, bayer2024contributionofammonia pages 1-4) |
| Iron oxidation modules | Cyc2 | cytochrome/protein | label-only candidate | (wang2024characterizethegrowth pages 1-2, zhang2023microbedrivenelementalcycling pages 4-6) |
| Iron oxidation modules | rusticyanin (Rus) | copper protein | label-only candidate | (wang2024characterizethegrowth pages 1-2, jung2024crisprdcas12aknockdownof pages 1-2) |
| Iron oxidation modules | Cyc1 | cytochrome/protein | label-only candidate | (wang2024characterizethegrowth pages 1-2, jung2024crisprdcas12aknockdownof pages 1-2) |
| Iron oxidation modules | cytochrome aa3 oxidase (Cox) | terminal oxidase complex | label-only candidate | (wang2024characterizethegrowth pages 1-2, jung2024crisprdcas12aknockdownof pages 1-2) |
| Iron oxidation modules | bc1 complex | respiratory complex | label-only candidate | (jung2024crisprdcas12aknockdownof pages 1-2, wang2024characterizethegrowth pages 13-15) |
| Iron oxidation modules | petI operon | operon | label-only candidate | (jung2024crisprdcas12aknockdownof pages 1-2, wang2024characterizethegrowth pages 13-15) |
| Iron oxidation modules | petII operon | operon | label-only candidate | (jung2024crisprdcas12aknockdownof pages 1-2, wang2024characterizethegrowth pages 13-15) |
| Transport/regulation | SoxT1A | transporter | label-only candidate | (li2024yeeelikebacterialsoxt pages 1-2, li2024yeeelikebacterialsoxt pages 7-8) |
| Transport/regulation | SoxT1B | transporter/sensor | label-only candidate | (li2024yeeelikebacterialsoxt pages 1-2, li2024yeeelikebacterialsoxt pages 7-8) |
| Transport/regulation | SoxR | transcriptional repressor | label-only candidate | (li2024yeeelikebacterialsoxt pages 1-2, li2024yeeelikebacterialsoxt pages 7-8) |
| Transport/regulation | Amt ammonium transporter | transporter | label-only candidate | (han2024adaptivetraitsof pages 9-11) |
| Transport/regulation | V-type ATPase | ATPase/ion transporter | label-only candidate | (cornell2024genomeencodedmetabolicpotential pages 13-15) |
| Transport/regulation | ABC transporters | transporter class | label-only candidate | (zhou2023effectsofacidification pages 5-6, wang2024characterizethegrowth pages 22-23) |
| Environmental/expt factors | acidification / low pH | environmental factor | ENVO:01001564 | (zhou2023effectsofacidification pages 1-2, zhou2023effectsofacidification pages 6-7) |
| Environmental/expt factors | thiosulfate availability | environmental factor | CHEBI:30085 | (twible2024phandthiosulfate pages 1-2, twible2024phandthiosulfate media 3cab23b0) |
| Environmental/expt factors | sediment depth | environmental gradient | ENVO:01000406 | (shoemaker2024wood–ljungdahlpathwayencoding pages 11-12, beaver2024microbialecologyof pages 2-3) |
| Environmental/expt factors | phenylacetylene | inhibitor | CHEBI:52997 | (bayer2024contributionofammonia pages 1-4) |
| Environmental/expt factors | acetylene | inhibitor | CHEBI:22157 | (cornell2024genomeencodedmetabolicpotential pages 15-18) |
| Environmental/expt factors | electrode-derived electrons | experimental energy source | label-only candidate | (wang2024characterizethegrowth pages 1-2, wang2024characterizethegrowth pages 22-23) |
| Environmental/expt factors | oxygen limitation / dark conditions | habitat condition | ENVO:00001837 | (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2, beaver2024microbialecologyof pages 2-3) |
| Applications/contexts | bioleaching of low-grade copper ores | application | label-only candidate | (wang2024characterizethegrowth pages 1-2, jung2024crisprdcas12aknockdownof pages 1-2) |
| Applications/contexts | chalcopyrite oxidation | application/process | CHEBI:30417 | (jung2024crisprdcas12aknockdownof pages 1-2) |
| Applications/contexts | pyrite oxidation | application/process | CHEBI:46661 | (jung2024crisprdcas12aknockdownof pages 1-2) |
| Applications/contexts | acid mine drainage | environmental/industrial context | ENVO:01000266 | (wang2024characterizethegrowth pages 1-2) |
| Applications/contexts | flue gas and wastewater bubble-column bioreactor | application system | label-only candidate | (barla2024sustainablesynergisticapproach pages 1-2, barla2024sustainablesynergisticapproach pages 2-3) |
| Applications/contexts | rapid sand filters treating groundwater | application system | label-only candidate | (boersma2024metagenomicanalysisof pages 1-4) |
| Applications/contexts | deep terrestrial subsurface | environment/context | ENVO:01000211 | (beaver2024microbialecologyof pages 2-3) |
| Applications/contexts | deep-ocean dark water column | environment/context | ENVO:00002149 | (bayer2024contributionofammonia pages 1-4, li2024arcobacteraceaeareubiquitous pages 10-12) |


*Table: This table lists candidate nodes for curating a causal graph of the chemolithotrophic trait, organized by mechanistic and environmental category. It highlights grounded chemicals, pathways, genes, complexes, and application contexts supported by the current evidence set.*

Key mechanistic pillars supported in the 2023–2024 evidence set include:

#### A) Sulfur chemolithotrophy modules
- **Complete Sox system (csox):** Seven structural genes encode SoxXA, SoxYZ, SoxB, SoxCD; csox oxidizes thiosulfate without releasing free sulfur intermediates (twible2024phandthiosulfate pages 1-2). 
- **Tetrathionate-intermediate (S4I) pathway:** *tsdA* catalyzes S2O3^2− → S4O6^2− across pH; *tetH* mediates tetrathionate disproportionation but is restricted to certain taxa (e.g., *Thiobacillus*) (twible2024phandthiosulfate pages 1-2, twible2024phandthiosulfate pages 5-6).
- **Cytoplasmic sulfur processing (Beggiatoa example):** PDO oxidizes sulfane sulfur to sulfite; sulfite reacts with sulfane sulfur to yield thiosulfate, linking intracellular sulfur cycling to periplasmic Sox oxidation (rudenko2024mechanismofintracellular pages 12-13).
- **Transport and regulation:** SoxT1A delivers sulfur into the cytoplasm for oxidation and is required for sulfur oxidation; SoxT1B functions in signaling to SoxR, a repressor that shuts down sox transcription when sulfur is absent (li2024yeeelikebacterialsoxt pages 1-2).

#### B) Nitrification (ammonia oxidation / nitrite oxidation) as chemolithotrophic energy metabolism
- Acidification experiments in estuarine/coastal systems connect ammonia/nitrite oxidation to cellular energy budgets and CO2 fixation gene expression, showing CO2 fixation pathways (Calvin in *Nitrosomonas*, rTCA in *Nitrospira*) are downregulated under acidification (zhou2023effectsofacidification pages 6-7).
- AOA-specific carbon fixation via the **3HP/4HB cycle** is generally upregulated under acidification (zhou2023effectsofacidification pages 6-7).

#### C) Iron chemolithotrophy (acidophilic Fe(II) oxidizers)
- A detailed mechanistic chain for *Acidithiobacillus ferrooxidans* is described: Fe2+ oxidation via outer membrane cytochrome **Cyc2**, electrons to **rusticyanin (Rus)**, branching into uphill/downhill paths, with a common chain “Fe2+ → Cyc2 → Rus → Cyc1 → Cox” and ~95% of electrons through the downhill path (wang2024characterizethegrowth pages 1-2).
- The **bc1 complex** encoded by **petI/petII operons** participates in uphill electron transfer and is differentially expressed depending on iron vs sulfur growth conditions (wang2024characterizethegrowth pages 13-15, jung2024crisprdcas12aknockdownof pages 1-2).

#### D) CO2 fixation pathways beyond Calvin
- **Wood–Ljungdahl pathway** predicted as the primary autotrophy mode in dark, hypersaline sediments; prevalence increases with sediment depth; pathway is low-ATP-cost and oxygen sensitive (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2, shoemaker2024wood–ljungdahlpathwayencoding pages 11-12).
- **rTCA** carbon fixation is present in marine Arcobacteraceae clade C and is widespread in ocean metatranscriptomes (li2024arcobacteraceaeareubiquitous pages 1-2, li2024arcobacteraceaeareubiquitous pages 10-12).

---

## 3) Evidence-backed candidate causal edges (triples)

A curation-ready edge set with snippets and curator notes is provided here:

| Subject | Subject type | Subject CURIE | Predicate | Object | Object type | Object CURIE | Reference (DOI/URL, year) | Citation id | Supporting snippet | Curator notes |
|---|---|---|---|---|---|---|---|---|---|---|
| complete Sox pathway (soxXA-soxYZ-soxB-soxCD) | pathway | label-only candidate | enables oxidation of | thiosulfate to sulfate without free sulfur intermediates | process | CHEBI:30085 / CHEBI:16189 | https://doi.org/10.3389/fmicb.2024.1426584 (2024) | (twible2024phandthiosulfate pages 1-2) | "in the complete sox (csox) form no free sulfur intermediates are released" | Core sulfur-oxidation edge for SOB; pathway-level, not universal to all chemolithotrophs. |
| csox-dominant sulfur oxidizers | microbial community/process | label-only candidate | associated with | thiosulfate consumption | chemical process | CHEBI:30085 | https://doi.org/10.3389/fmicb.2024.1426584 (2024) | (twible2024phandthiosulfate pages 1-2) | "csox-dominant SOB (e.g., Halothiobacillus, Thiomonas) are associated with S2O32- consumption" | Community-level association from environmental metagenomics; not a single-organism causal proof. |
| csox-dominant sulfur oxidizers | microbial community/process | label-only candidate | associated with | acidity generation | environmental process | label-only candidate | https://doi.org/10.3389/fmicb.2024.1426584 (2024) | (twible2024phandthiosulfate pages 1-2) | "csox-dominant SOB ... are associated with S2O32- consumption and acidity generation at lower pH" | Environment-specific; useful environmental edge rather than trait-defining mechanism. |
| tsdA | gene/enzyme | label-only candidate | catalyzes | thiosulfate to tetrathionate conversion | reaction | CHEBI:30085 / CHEBI:30858 | https://doi.org/10.3389/fmicb.2024.1426584 (2024) | (twible2024phandthiosulfate pages 1-2) | "tsdA (S2O32- to S4O62-) operates across pH" | Strong candidate sulfur-oxidation edge; tetrathionate-intermediate pathway specific. |
| tetH | gene/enzyme | label-only candidate | mediates | tetrathionate disproportionation | reaction | CHEBI:30858 | https://doi.org/10.3389/fmicb.2024.1426584 (2024) | (twible2024phandthiosulfate pages 1-2) | "tetH (S4O62- disproportionation) is restricted to Thiobacillus spp." | Taxon-specific; mark uncertain for general chemolithotrophy graph. |
| incomplete sox + rdsr communities | microbial community/process | label-only candidate | associated with | higher thiosulfate concentrations | environmental state | CHEBI:30085 | https://doi.org/10.3389/fmicb.2024.1426584 (2024) | (twible2024phandthiosulfate pages 1-2) | "communities hosting incomplete sox and rdsr ... correlate with higher thiosulfate" | Environmental association; useful contextual edge. |
| incomplete sox + rdsr communities | microbial community/process | label-only candidate | associated with | limited acidity generation | environmental process | label-only candidate | https://doi.org/10.3389/fmicb.2024.1426584 (2024) | (twible2024phandthiosulfate pages 1-2) | "communities hosting incomplete sox and rdsr ... correlate with ... limited acidification at circumneutral pH" | pH-dependent ecological edge; not universal. |
| PDO (persulfide dioxygenase) | enzyme | label-only candidate | oxidizes | sulfane sulfur to sulfite | reaction | CHEBI:26896 | https://doi.org/10.3390/ijms252010962 (2024) | (rudenko2024mechanismofintracellular pages 12-13) | "producing sulfane sulfur that is metabolized to sulfite by persulfide dioxygenase (PDO)" | Strong mechanistic edge in Beggiatoa; taxon-specific but clear. |
| GSSH (glutathione persulfide) | metabolite | label-only candidate | serves as substrate for | PDO | enzyme | label-only candidate | https://doi.org/10.3390/ijms252010962 (2024) | (rudenko2024mechanismofintracellular pages 12-13) | "GSH non-enzymatically forms glutathione persulfide (GSSH), a PDO substrate" | Metabolite-level edge; valuable if metabolite nodes are allowed. |
| sulfite | metabolite | CHEBI:26896 | reacts with | sulfane sulfur to yield thiosulfate | reaction | CHEBI:30085 | https://doi.org/10.3390/ijms252010962 (2024) | (rudenko2024mechanismofintracellular pages 12-13) | "producing sulfite that chemically reacts with sulfane sulfur to yield thiosulfate" | Chemical step rather than enzyme-mediated; still mechanistically relevant. |
| branched Sox system lacking SoxCD | pathway | label-only candidate | oxidizes | thiosulfate in periplasm to sulfate and elemental sulfur | process | CHEBI:30085 / CHEBI:16189 / CHEBI:18422 | https://doi.org/10.3390/ijms252010962 (2024) | (rudenko2024mechanismofintracellular pages 12-13) | "The branched Sox-system ... likely oxidizes thiosulfate in the periplasm to sulfate and elemental sulfur" | Author inference; mark uncertain. |
| pdo expression | gene expression process | label-only candidate | increases during | intracellular sulfur consumption | biological process | label-only candidate | https://doi.org/10.3390/ijms252010962 (2024) | (rudenko2024mechanismofintracellular pages 10-12) | "pdo expression peaks at day 7 when intracellular sulfur is consumed" | Supportive regulatory edge, taxon-specific to Beggiatoa. |
| SoxT1A | transporter | label-only candidate | required for | sulfur import to cytoplasm for further oxidation | transport/process | label-only candidate | https://doi.org/10.1038/s42003-024-07270-7 (2024) | (li2024yeeelikebacterialsoxt pages 1-2) | "SoxT1A is required to deliver sulfur into the cytoplasm for further oxidation" | Strong transporter edge from mutant phenotype; Hyphomicrobium-specific. |
| loss of SoxT1A | perturbation | label-only candidate | causes | sulfur oxidation-negative phenotype | phenotype | label-only candidate | https://doi.org/10.1038/s42003-024-07270-7 (2024) | (li2024yeeelikebacterialsoxt pages 1-2) | "SoxT1A mutants are sulfur oxidation-negative despite high transcription of sulfur oxidation genes" | Strong genetic causality; taxon-specific. |
| SoxT1B | transporter/sensor | label-only candidate | functions in | signal transduction to SoxR | regulatory process | label-only candidate | https://doi.org/10.1038/s42003-024-07270-7 (2024) | (li2024yeeelikebacterialsoxt pages 1-2) | "SoxT1B functions in signal transduction to the transcriptional repressor SoxR" | Good regulatory edge. |
| SoxR | transcriptional repressor | label-only candidate | represses | sox promoter/operator transcription when sulfur is absent | regulatory process | label-only candidate | https://doi.org/10.1038/s42003-024-07270-7 (2024) | (li2024yeeelikebacterialsoxt pages 1-2) | "SoxR binds the sox promoter-operator and represses transcription when sulfur is absent" | Regulatory edge, not directly trait-defining but useful. |
| tsdA | gene/enzyme | label-only candidate | contributes to | thiosulfate-stimulated growth | phenotype | label-only candidate | https://doi.org/10.3389/fmars.2024.1491690 (2024) | (chen2024adaptationmechanismsof pages 1-2) | "Addition of thiosulfate stimulated Alcanivorax growth" | Weak for TraitMech because organism not confirmed chemoautotroph; likely supplemental heterotrophy. |
| sqr | gene/enzyme | label-only candidate | mediates | sulfide detoxification | process | CHEBI:18422 | https://doi.org/10.3389/fmars.2024.1491690 (2024) | (chen2024adaptationmechanismsof pages 1-2) | "Sqr functions primarily in sulfide detoxification rather than in energy conservation" | Boundary-case exclusion edge; do not use as positive chemolithotrophy evidence. |
| AMO (amoA/amoB/amoC) | enzyme complex | label-only candidate | catalyzes first step of | ammonia oxidation | process | GO:0004096 / CHEBI:16134 | https://doi.org/10.1128/mbio.02169-24 (2024) | (han2024adaptivetraitsof pages 9-11) | "the first step of ammonia oxidation is carried out by an ammonia monooxygenase (AMO) enzyme" | Canonical nitrification edge; complex-level node preferable. |
| ammonia oxidation | metabolic process | GO:0004096 | supports | chemolithoautotrophic growth with CO2 fixation in AOA | phenotype/process | METPO:1000639 | https://doi.org/10.21203/rs.3.rs-4032669/v1? / Cornell thesis-like source unavailable DOI metadata unclear (2024) | (cornell2024genomeencodedmetabolicpotential pages 13-15) | "they oxidize NH3 to NO2– to conserve energy and fix bicarbonate (HCO3–) via a modified 3-hydroxypropionate/4-hydroxybutyrate (3-HP/4-HB) cycle" | Useful but source metadata incomplete; retain with caution. |
| amo genes | gene set | label-only candidate | support | ammonia oxidation potential | process | GO:0004096 | https://doi.org/10.21203/rs.3.rs-4032669/v1? / Cornell thesis-like source unavailable DOI metadata unclear (2024) | (cornell2024genomeencodedmetabolicpotential pages 13-15) | "Genes contain the necessary carbon-fixation genes and genes 'coding for the three subunits of Amo'" | Genomic-potential edge only. |
| phenylacetylene | inhibitor | CHEBI:52997 | inhibits | ammonia monooxygenase | enzyme | label-only candidate | https://doi.org/10.1101/2024.11.16.623942 (2024) | (bayer2024contributionofammonia pages 1-4) | "We applied phenylacetylene as a specific inhibitor of the ammonia monooxygenase" | Strong assay edge; preprint. |
| ammonia oxidizers | microbial functional group | label-only candidate | contribute to | dark DIC fixation | process | label-only candidate | https://doi.org/10.1101/2024.11.16.623942 (2024) | (bayer2024contributionofammonia pages 1-4) | "ammonia oxidizers accounted for only 2–22% of depth-integrated dark DIC fixation" | Quantitative ecological edge; contribution lower than often assumed. |
| acidification | environmental factor | ENVO:01001564 | decreases | nitrification rate | process | GO:0038165 | https://doi.org/10.1038/s41467-023-37104-9 (2023) | (zhou2023effectsofacidification pages 1-2) | "a 5.8–18.1% drop ... and ~11.1–34.1% decline when pCO2 was doubled" | Strong environmental edge. |
| acidification | environmental factor | ENVO:01001564 | stimulates | N2O generation during nitrification | process | CHEBI:33101 | https://doi.org/10.1038/s41467-023-37104-9 (2023) | (zhou2023effectsofacidification pages 1-2) | "Acidification also 'stimulate[s] generation of byproduct nitrous oxide (N2O)'" | Important outcome edge for nitrifier physiology. |
| acidification | environmental factor | ENVO:01001564 | downregulates | bacterial CO2 fixation pathways (Calvin, rTCA) | pathway | GO:0015977 / GO:0071941 | https://doi.org/10.1038/s41467-023-37104-9 (2023) | (zhou2023effectsofacidification pages 6-7) | "bacterial CO2-fixation pathways (Calvin cycle in Nitrosomonas and rTCA in Nitrospira) were ubiquitously down-regulated" | Good pathway-environment edge; coastal/estuarine context. |
| acidification | environmental factor | ENVO:01001564 | upregulates | archaeal 3HP/4HB pathway | pathway | label-only candidate | https://doi.org/10.1038/s41467-023-37104-9 (2023) | (zhou2023effectsofacidification pages 6-7) | "the archaeal 3-hydroxypropionate/4-hydroxybutyrate (3HP/4HB) pathway in AOA was generally up-regulated" | AOA-specific and context-specific. |
| Fe2+ oxidation via Cyc2 | pathway step | CHEBI:29033 | transfers electrons to | rusticyanin | protein | label-only candidate | https://doi.org/10.3390/microorganisms12030590 (2024) | (wang2024characterizethegrowth pages 1-2) | "Fe2+ is oxidized to Fe3+ via outer-membrane cytochrome c (Cyc2) with electron flow toward rusticyanin (Rus)" | Core iron-oxidation edge in Acidithiobacillus. |
| rusticyanin | protein | label-only candidate | transfers electrons to | Cyc1 | protein | label-only candidate | https://doi.org/10.3390/microorganisms12030590 (2024) | (wang2024characterizethegrowth pages 1-2) | "Fe2+ → Cyc2 → Rus → Cyc1 → Cox" | Pathway-specific edge. |
| petI operon (bc1 complex) | operon/complex | label-only candidate | participates in | uphill electron transfer during Fe2+ oxidation | process | label-only candidate | https://doi.org/10.3390/microorganisms12030590 (2024) | (wang2024characterizethegrowth pages 13-15) | "The pet I and pet II operons encode the bc1 complex, implicated in the uphill electron transfer of Fe2+ oxidation" | Strong mechanistic edge. |
| Fe2+ as electron donor | chemical | CHEBI:29033 | upregulates | rusticyanin / cytochrome c552 / rus operon / Rubisco subunits | gene/protein set | label-only candidate | https://doi.org/10.3390/microorganisms12030590 (2024) | (wang2024characterizethegrowth pages 13-15) | "Known Fe2+-linked proteins (rusticyanin, cytochrome c552, PstS, CbbQ, and Rubisco subunits) are up-regulated when Fe2+ is the electron donor" | Combined edge; could be split during formal curation. |
| petB2 knockdown | genetic perturbation | label-only candidate | enhances | iron oxidation | process | GO:0016491 | https://doi.org/10.1016/j.jbc.2024.107703 (2024) | (jung2024crisprdcas12aknockdownof pages 1-2) | "petB2 knockdown enhanced iron oxidation" | Strong perturbation edge, Acidithiobacillus-specific. |
| petB2 knockdown | genetic perturbation | label-only candidate | increases | pyrite and chalcopyrite oxidation | process | CHEBI:46661 / CHEBI:30417 | https://doi.org/10.1016/j.jbc.2024.107703 (2024) | (jung2024crisprdcas12aknockdownof pages 1-2) | "increased pyrite and chalcopyrite oxidation" | Applied bioleaching edge. |
| petB2 knockdown | genetic perturbation | label-only candidate | reduces | biofilm formation and surface passivation | phenotype/process | label-only candidate | https://doi.org/10.1016/j.jbc.2024.107703 (2024) | (jung2024crisprdcas12aknockdownof pages 1-2) | "while reducing biofilm formation and surface passivation" | Useful engineering edge. |
| Calvin-Benson-Bassham cycle | carbon fixation pathway | GO:0015977 | mediates | CO2 fixation in A. ferrooxidans | process | CHEBI:16526 | https://doi.org/10.3390/microorganisms12030590 (2024) | (wang2024characterizethegrowth pages 1-2) | "fixes atmospheric CO2 via the Calvin–Benson–Bassham (CBB) cycle" | Clear positive carbon-fixation edge. |
| Wood-Ljungdahl pathway | carbon fixation pathway | GO:0019685 | predicted primary mode of | dark autotrophy in hypersaline sediments | process | ENVO:00002007 | https://doi.org/10.1093/femsec/fiae105 (2024) | (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2) | "the primary mode of autotrophy was predicted to be via the Wood–Ljungdahl pathway" | Habitat-specific but high-value for dark chemolithotrophy. |
| Wood-Ljungdahl pathway | carbon fixation pathway | GO:0019685 | increases in prevalence with | sediment depth | environmental gradient | ENVO:01000406 | https://doi.org/10.1093/femsec/fiae105 (2024) | (shoemaker2024wood–ljungdahlpathwayencoding pages 11-12) | "The WL pathway is ... prevalent ... with increasing prevalence with depth in the sediment column" | Ecological edge; may be represented as abundance association. |
| rTCA pathway | carbon fixation pathway | GO:0071941 | supports carbon fixation in | marine Arcobacteraceae clade C | taxon/pathway context | NCBITaxon:Campylobacterota | https://doi.org/10.1128/msystems.00513-24 (2024) | (li2024arcobacteraceaeareubiquitous pages 1-2) | "genes putatively for the reverse tricarboxylic acid (rTCA) pathway were identified" | Genomic/transcriptomic inference; mixotrophic lineage, not obligate chemolithotroph universally. |
| sulfur oxidation + denitrification | coupled process | label-only candidate | powers | dark carbon fixation in Arcobacteraceae | process | label-only candidate | https://doi.org/10.1128/msystems.00513-24 (2024) | (li2024arcobacteraceaeareubiquitous pages 1-2) | "carries out carbon fixation in the dark by coupling sulfur oxidation and denitrification" | Strong but lineage-specific; useful coupled-process edge. |
| chemolithotrophic bacterial consortium bioreactor | implementation | label-only candidate | removes | CO2 from flue gas (89.80%) | application outcome | CHEBI:16526 | https://doi.org/10.1038/s41598-024-67053-2 (2024) | (barla2024sustainablesynergisticapproach pages 1-2) | "removal efficiencies of 89.80% (CO2), 77.30% (SO2), and 80.77% (NO)" | Application edge; not organism-intrinsic mechanism. |
| chemolithotrophic bacterial consortium bioreactor | implementation | label-only candidate | removes | SO2 from flue gas (77.30%) | application outcome | CHEBI:18422 | https://doi.org/10.1038/s41598-024-67053-2 (2024) | (barla2024sustainablesynergisticapproach pages 1-2) | "removal efficiencies of 89.80% (CO2), 77.30% (SO2), and 80.77% (NO)" | Application edge. |
| chemolithotrophic bacterial consortium bioreactor | implementation | label-only candidate | removes | NO from flue gas (80.77%) | application outcome | CHEBI:16480 | https://doi.org/10.1038/s41598-024-67053-2 (2024) | (barla2024sustainablesynergisticapproach pages 1-2) | "removal efficiencies of 89.80% (CO2), 77.30% (SO2), and 80.77% (NO)" | Application edge. |
| microbiome-mediated bioleaching | application | label-only candidate | contributes to | >30% of global copper production from low-grade ores | industrial outcome | CHEBI:28694 | https://doi.org/10.3390/microorganisms12030590 (2024) | (wang2024characterizethegrowth pages 1-2) | "believed to account for over 30% of global copper production from low-grade copper ores" | Useful application statistic; secondary claim within review/introduction context. |
| chalcopyrite | mineral substrate | CHEBI:30417 | is oxidized more effectively after | bc1 complex CRISPRi perturbation | perturbation | label-only candidate | https://doi.org/10.1016/j.jbc.2024.107703 (2024) | (jung2024crisprdcas12aknockdownof pages 1-2) | "petB2 knockdown ... increased pyrite and chalcopyrite oxidation" | Bioleaching-specific engineering edge. |


*Table: This table lists curation-ready candidate causal edges for METPO:1000639, grounded in recent evidence across sulfur, nitrogen, iron, and carbon-fixation mechanisms plus selected applied implementations. It is designed to help curate a TraitMech graph while highlighting taxon specificity and uncertainty.*

### Visual evidence (recommended for curator orientation)
A pathway schematic summarizing sulfur oxidation strategies and gene modules (sox vs S4I vs rdsr) plus pH-linked ecological partitioning is available as a figure crop (twible2024phandthiosulfate media 3cab23b0).

---

## 4) Recent developments and latest research (prioritizing 2023–2024)

### 4.1 Sulfur oxidation: pathway modularity + ecological controls
A 2024 multi-year study across mine tailings impoundments highlights that **pH and thiosulfate availability** shape which sulfur-oxidation pathway dominates, linking gene module completeness (csox vs incomplete sox/rdsr vs S4I) to outcomes like **acidity generation** and **thiosulfate consumption** (twible2024phandthiosulfate pages 1-2, twible2024phandthiosulfate media 3cab23b0). This supports including environmental-factor nodes (pH, thiosulfate) as upstream causal nodes.

### 4.2 Sulfur oxidation: transport/regulation emerging as mechanistic bottleneck
Work in 2024 identifies SoxT transporters as mechanistic gatekeepers: SoxT1A mutants are sulfur oxidation-negative despite high transcription of sulfur oxidation genes, directly implicating **substrate import** as a necessary upstream cause of sulfur oxidation (li2024yeeelikebacterialsoxt pages 1-2). This is a curation-relevant advance because many TraitMech graphs historically emphasize only catalytic enzymes.

### 4.3 Chemolithotrophic carbon fixation reassessed in the ocean
A 2024 ocean study using phenylacetylene to inhibit ammonia monooxygenase reports ammonia oxidizers contribute **only 2–22%** of depth-integrated dark DIC fixation in parts of the Pacific, challenging the common assumption that nitrification dominates deep-ocean dark carbon fixation (bayer2024contributionofammonia pages 1-4). This suggests TraitMech curation should allow for **multiple energy sources** supporting dark CO2 fixation rather than nitrification alone.

### 4.4 Environmental stress (acidification) connects to CO2 fixation allocation
A 2023 Nature Communications study shows acidification decreases nitrification rates and downregulates bacterial CO2-fixation pathways while upregulating AOA 3HP/4HB fixation; it interprets this as reduced ATP production shifting energy toward maintenance (zhou2023effectsofacidification pages 6-7, zhou2023effectsofacidification pages 1-2).

---

## 5) Current applications and real-world implementations (with statistics)

### 5.1 Industrial bioreactors: combined flue gas + wastewater mitigation
A 2024 Scientific Reports bubble-column bioreactor using bacterial consortia reported:
- Biomass yield **3.66 g L−1**
- Removal efficiencies: **89.80% CO2**, **77.30% SO2**, **80.77% NO** (barla2024sustainablesynergisticapproach pages 1-2)
- Simulated flue gas composition: 10.4% CO2, 780 ppm NO, 141 ppm SO2 (barla2024sustainablesynergisticapproach pages 3-4)
- Techno-economic estimate: total capital investment **$245.74** for 288 h operation (barla2024sustainablesynergisticapproach pages 1-2)
These data support application-level edges linking chemolithotrophy-supporting communities to emissions/wastewater mitigation performance.

### 5.2 Biomining/bioleaching and acid mine drainage contexts
- A 2024 study on *A. ferrooxidans* emphasizes industrial relevance, stating microbiome-mediated bioleaching is “believed to account for **over 30%** of global copper production from low-grade copper ores” (wang2024characterizethegrowth pages 1-2). 
- A 2024 Journal of Biological Chemistry study applies CRISPRi to the *A. ferrooxidans* bc1 complex and reports that **petB2 knockdown enhanced iron oxidation** and increased **pyrite and chalcopyrite oxidation** while reducing biofilm formation and passivation (jung2024crisprdcas12aknockdownof pages 1-2). This is strong evidence for a causal link from ETC configuration → mineral oxidation performance.

### 5.3 Water treatment: rapid sand filters and chemolithotrophic functional guilds
Metagenomic profiling of groundwater rapid sand filters (2024) recovered many MAGs encoding **methane oxidation, iron/manganese oxidation, and nitrification**; iron oxidation in the anthracite layer is primarily associated with *Gallionella* encoding cluster 1 **Cyc2**, and nitrification guild composition shifts with filter age (boersma2024metagenomicanalysisof pages 1-4). This is direct evidence that chemolithotrophic pathways are operationally deployed in drinking-water treatment infrastructure.

---

## 6) Expert opinions / authoritative interpretations (from sources)

- **Acidification excludes “CO2-fertilization” of nitrifiers:** The acidification study argues that although elevated CO2 might be expected to promote chemoautotrophic growth, lowered pH excludes this beneficial effect and inhibits nitrification by shifting NH3/NH4+ equilibrium (zhou2023effectsofacidification pages 1-2).
- **Sox pathway completeness as a predictor of geochemical outcome:** The sulfur oxidation strategy study interprets that csox dominance drives acidity generation at lower pH, whereas non-csox strategies correlate with limited acidification at circumneutral pH (twible2024phandthiosulfate pages 1-2).
- **Need to avoid over-attributing dark-ocean CO2 fixation to nitrification:** The phenylacetylene inhibition approach suggests the prevailing narrative may overestimate ammonia oxidizers’ role in dark DIC fixation in some regions (bayer2024contributionofammonia pages 1-4).

---

## 7) Warnings / claims not ready for TraitMech curation

1. **Do not curate sqr as “energy-conserving sulfide oxidation” in all taxa:** In *Alcanivorax*, Sqr is reported as detoxification rather than energy conservation (chen2024adaptationmechanismsof pages 1-2). 
2. **Do not curate amoA presence as sufficient for chemolithoautotrophy:** AOA can show amoA transcripts without measurable ammonia oxidation, and some settings show bicarbonate assimilation decoupled from AOA presence (cornell2024genomeencodedmetabolicpotential pages 15-18).
3. **Community-level associations (pH ↔ pathway dominance) should be flagged as ecological/inferred edges:** pH partitioning of pathway strategies is strong but often derived from metagenomic associations rather than single-strain causal tests (twible2024phandthiosulfate pages 1-2).
4. **Preprints:** The dark-ocean contribution study is currently a preprint (bioRxiv); curate its quantitative claims with an “uncertain/preprint” flag (bayer2024contributionofammonia pages 1-4).

---

## DOI-first bibliography (with URLs and publication dates)

- **Barla RJ, Gupta S, Raghuvanshi S.** *Sustainable synergistic approach to chemolithotrophs—supported bioremediation of wastewater and flue gas.* Scientific Reports. **2024-07**. https://doi.org/10.1038/s41598-024-67053-2 (barla2024sustainablesynergisticapproach pages 1-2)
- **Beaver RC, Neufeld JD.** *Microbial ecology of the deep terrestrial subsurface.* The ISME Journal. **2024-01**. https://doi.org/10.1093/ismejo/wrae091 (beaver2024microbialecologyof pages 2-3)
- **Boersma AS, et al.** *Metagenomic analysis of age-dependent microbial dynamics in dual-media rapid sand filters treating groundwater.* bioRxiv. **2024-12**. https://doi.org/10.1101/2024.12.25.630300 (boersma2024metagenomicanalysisof pages 1-4)
- **Bayer B, et al.** *Contribution of ammonia oxidizers to inorganic carbon fixation in the dark ocean.* bioRxiv. **2024-11**. https://doi.org/10.1101/2024.11.16.623942 (bayer2024contributionofammonia pages 1-4)
- **Chen Z, et al.** *Adaptation mechanisms of Alcanivorax facilitating its predominance in marine environments.* Frontiers in Marine Science. **2024-11**. https://doi.org/10.3389/fmars.2024.1491690 (chen2024adaptationmechanismsof pages 1-2)
- **Han S, et al.** *Adaptive traits of Nitrosocosmicus clade ammonia-oxidizing archaea.* mBio. **2024-11**. https://doi.org/10.1128/mbio.02169-24 (han2024adaptivetraitsof pages 9-11)
- **Jung H, Inaba Y, Banta S.** *CRISPR/dCas12a knock-down of Acidithiobacillus ferrooxidans electron transport chain bc1 complexes enables enhanced metal sulfide bioleaching.* Journal of Biological Chemistry. **2024-09**. https://doi.org/10.1016/j.jbc.2024.107703 (jung2024crisprdcas12aknockdownof pages 1-2)
- **Li J, et al.** *YeeE-like bacterial SoxT proteins mediate sulfur import for oxidation and signal transduction.* Communications Biology. **2024-11**. https://doi.org/10.1038/s42003-024-07270-7 (li2024yeeelikebacterialsoxt pages 1-2)
- **Li J, et al.** *Arcobacteraceae are ubiquitous mixotrophic bacteria playing important roles in carbon, nitrogen, and sulfur cycling in global oceans.* mSystems. **2024-07**. https://doi.org/10.1128/msystems.00513-24 (li2024arcobacteraceaeareubiquitous pages 1-2)
- **Rudenko TS, et al.** *Mechanism of intracellular elemental sulfur oxidation in Beggiatoa leptomitoformis, where persulfide dioxygenase plays a key role.* International Journal of Molecular Sciences. **2024-10**. https://doi.org/10.3390/ijms252010962 (rudenko2024mechanismofintracellular pages 12-13)
- **Shoemaker A, et al.** *Wood–Ljungdahl pathway encoding anaerobes facilitate low-cost primary production in hypersaline sediments at Great Salt Lake, Utah.* FEMS Microbiology Ecology. **2024-07**. https://doi.org/10.1093/femsec/fiae105 (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2)
- **Twible LE, et al.** *pH and thiosulfate dependent microbial sulfur oxidation strategies across diverse environments.* Frontiers in Microbiology. **2024-07**. https://doi.org/10.3389/fmicb.2024.1426584 (twible2024phandthiosulfate pages 1-2)
- **Wang Q, et al.** *Characterize the growth and metabolism of Acidithiobacillus ferrooxidans under electroautotrophic and chemoautotrophic conditions.* Microorganisms. **2024-03**. https://doi.org/10.3390/microorganisms12030590 (wang2024characterizethegrowth pages 1-2)
- **Zhang D, et al.** *Microbe-driven elemental cycling enables microbial adaptation to deep-sea ferromanganese nodule sediment fields.* Microbiome. **2023-07**. https://doi.org/10.1186/s40168-023-01601-2 (zhang2023microbedrivenelementalcycling pages 4-6)
- **Zhou J, et al.** *Effects of acidification on nitrification and associated nitrous oxide emission in estuarine and coastal waters.* Nature Communications. **2023-03**. https://doi.org/10.1038/s41467-023-37104-9 (zhou2023effectsofacidification pages 1-2)

---

## Notes on coverage gaps vs user request
Hydrogen oxidation–specific gene modules (e.g., [NiFe]-hydrogenases) were not directly evidenced with mechanistic snippets in the retrieved excerpts, though hydrogen as an electron donor and hydrogenase enrichment in deep subsurface communities is supported (beaver2024microbialecologyof pages 2-3). Additional targeted retrieval would be needed to curate hydrogenase subunits and respiratory coupling with the same evidence density as sulfur/nitrification/iron.


References

1. (chen2024adaptationmechanismsof pages 1-2): Zhen Chen, Shizheng Xiang, Yao Lu, Qiliang Lai, Chunming Dong, Jianyang Li, Guizhen Li, and Zongze Shao. Adaptation mechanisms of alcanivorax facilitating its predominance in marine environments. Frontiers in Marine Science, Nov 2024. URL: https://doi.org/10.3389/fmars.2024.1491690, doi:10.3389/fmars.2024.1491690. This article has 4 citations.

2. (cornell2024genomeencodedmetabolicpotential pages 15-18): C Cornell. Genome-encoded metabolic potential of the nitrosocosmicus genus and related ammonia-oxidizing archaea. Unknown journal, 2024.

3. (zhou2023effectsofacidification pages 1-2): Jie Zhou, Yanling Zheng, Lijun Hou, Zhirui An, Feiyang Chen, Bolin Liu, Li Wu, Lin Qi, Hongpo Dong, Ping Han, Guoyu Yin, Xia Liang, Yi Yang, Xiaofei Li, Dengzhou Gao, Ye Li, Zhanfei Liu, Richard Bellerby, and Min Liu. Effects of acidification on nitrification and associated nitrous oxide emission in estuarine and coastal waters. Nature Communications, Mar 2023. URL: https://doi.org/10.1038/s41467-023-37104-9, doi:10.1038/s41467-023-37104-9. This article has 94 citations and is from a highest quality peer-reviewed journal.

4. (han2024adaptivetraitsof pages 9-11): Saem Han, Seongwook Kim, Christopher J. Sedlacek, Adeel Farooq, Chihong Song, Sujin Lee, Shurong Liu, Nicolas Brüggemann, Lena Rohe, Miye Kwon, Sung-Keun Rhee, and Man-Young Jung. Adaptive traits of <i>nitrosocosmicus</i> clade ammonia-oxidizing archaea. Nov 2024. URL: https://doi.org/10.1128/mbio.02169-24, doi:10.1128/mbio.02169-24. This article has 15 citations and is from a domain leading peer-reviewed journal.

5. (wang2024characterizethegrowth pages 1-2): Quansheng Wang, Haijun Long, Huiqi Wang, and Maggie C. Y. Lau Vetter. Characterize the growth and metabolism of acidithiobacillus ferrooxidans under electroautotrophic and chemoautotrophic conditions. Microorganisms, 12:590, Mar 2024. URL: https://doi.org/10.3390/microorganisms12030590, doi:10.3390/microorganisms12030590. This article has 9 citations.

6. (jung2024crisprdcas12aknockdownof pages 1-2): Heejung Jung, Yuta Inaba, and Scott Banta. Crispr/dcas12a knock-down of acidithiobacillus ferrooxidans electron transport chain bc1 complexes enables enhanced metal sulfide bioleaching. Sep 2024. URL: https://doi.org/10.1016/j.jbc.2024.107703, doi:10.1016/j.jbc.2024.107703. This article has 13 citations and is from a domain leading peer-reviewed journal.

7. (twible2024phandthiosulfate pages 1-2): Lauren E. Twible, Kelly Whaley-Martin, Lin-Xing Chen, Tara Colenbrander Nelson, James L.S. Arrey, Chad V. Jarolimek, Josh J. King, Lisa Ramilo, Helga Sonnenberg, Jillian F. Banfield, Simon C. Apte, and Lesley A. Warren. Ph and thiosulfate dependent microbial sulfur oxidation strategies across diverse environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1426584, doi:10.3389/fmicb.2024.1426584. This article has 24 citations and is from a peer-reviewed journal.

8. (li2024arcobacteraceaeareubiquitous pages 1-2): Jianyang Li, Shizheng Xiang, Yufei Li, Ruolin Cheng, Qiliang Lai, Liping Wang, Guizhen Li, Chunming Dong, and Zongze Shao. <i>arcobacteraceae</i> are ubiquitous mixotrophic bacteria playing important roles in carbon, nitrogen, and sulfur cycling in global oceans. Jul 2024. URL: https://doi.org/10.1128/msystems.00513-24, doi:10.1128/msystems.00513-24. This article has 31 citations and is from a peer-reviewed journal.

9. (beaver2024microbialecologyof pages 2-3): Rachel C Beaver and Josh D Neufeld. Microbial ecology of the deep terrestrial subsurface. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae091, doi:10.1093/ismejo/wrae091. This article has 66 citations.

10. (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2): Anna Shoemaker, Andrew Maritan, Su Cosar, Sylvia Nupp, Ana Menchaca, Thomas Jackson, Aria Dang, Bonnie K Baxter, Daniel R Colman, Eric C Dunham, and Eric S Boyd. Wood–ljungdahl pathway encoding anaerobes facilitate low-cost primary production in hypersaline sediments at great salt lake, utah. FEMS Microbiology Ecology, Jul 2024. URL: https://doi.org/10.1093/femsec/fiae105, doi:10.1093/femsec/fiae105. This article has 11 citations and is from a peer-reviewed journal.

11. (barla2024sustainablesynergisticapproach pages 7-8): Rachael J. Barla, Suresh Gupta, and Smita Raghuvanshi. Sustainable synergistic approach to chemolithotrophs—supported bioremediation of wastewater and flue gas. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-67053-2, doi:10.1038/s41598-024-67053-2. This article has 9 citations and is from a peer-reviewed journal.

12. (bayer2024contributionofammonia pages 1-4): Barbara Bayer, Katharina Kitzinger, Nicola L. Paul, Justine B. Albers, Mak A. Saito, Michael Wagner, Craig A. Carlson, and Alyson E. Santoro. Contribution of ammonia oxidizers to inorganic carbon fixation in the dark ocean. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.16.623942, doi:10.1101/2024.11.16.623942. This article has 1 citations.

13. (barla2024sustainablesynergisticapproach pages 1-2): Rachael J. Barla, Suresh Gupta, and Smita Raghuvanshi. Sustainable synergistic approach to chemolithotrophs—supported bioremediation of wastewater and flue gas. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-67053-2, doi:10.1038/s41598-024-67053-2. This article has 9 citations and is from a peer-reviewed journal.

14. (cornell2024genomeencodedmetabolicpotential pages 13-15): C Cornell. Genome-encoded metabolic potential of the nitrosocosmicus genus and related ammonia-oxidizing archaea. Unknown journal, 2024.

15. (zhou2023effectsofacidification pages 6-7): Jie Zhou, Yanling Zheng, Lijun Hou, Zhirui An, Feiyang Chen, Bolin Liu, Li Wu, Lin Qi, Hongpo Dong, Ping Han, Guoyu Yin, Xia Liang, Yi Yang, Xiaofei Li, Dengzhou Gao, Ye Li, Zhanfei Liu, Richard Bellerby, and Min Liu. Effects of acidification on nitrification and associated nitrous oxide emission in estuarine and coastal waters. Nature Communications, Mar 2023. URL: https://doi.org/10.1038/s41467-023-37104-9, doi:10.1038/s41467-023-37104-9. This article has 94 citations and is from a highest quality peer-reviewed journal.

16. (shoemaker2024wood–ljungdahlpathwayencoding pages 9-11): Anna Shoemaker, Andrew Maritan, Su Cosar, Sylvia Nupp, Ana Menchaca, Thomas Jackson, Aria Dang, Bonnie K Baxter, Daniel R Colman, Eric C Dunham, and Eric S Boyd. Wood–ljungdahl pathway encoding anaerobes facilitate low-cost primary production in hypersaline sediments at great salt lake, utah. FEMS Microbiology Ecology, Jul 2024. URL: https://doi.org/10.1093/femsec/fiae105, doi:10.1093/femsec/fiae105. This article has 11 citations and is from a peer-reviewed journal.

17. (yan2024characterizationofsulfur pages 59-63): Y Yan. Characterization of sulfur cycling in the first oil sands pilot end pit lake, base mine lake. Unknown journal, 2024.

18. (twible2024phandthiosulfate pages 5-6): Lauren E. Twible, Kelly Whaley-Martin, Lin-Xing Chen, Tara Colenbrander Nelson, James L.S. Arrey, Chad V. Jarolimek, Josh J. King, Lisa Ramilo, Helga Sonnenberg, Jillian F. Banfield, Simon C. Apte, and Lesley A. Warren. Ph and thiosulfate dependent microbial sulfur oxidation strategies across diverse environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1426584, doi:10.3389/fmicb.2024.1426584. This article has 24 citations and is from a peer-reviewed journal.

19. (rudenko2024mechanismofintracellular pages 10-12): Tatyana S. Rudenko, Liubov I. Trubitsina, Vasily V. Terentyev, Ivan V. Trubitsin, Valentin I. Borshchevskiy, Svetlana V. Tishchenko, Azat G. Gabdulkhakov, Alexey A. Leontievsky, and Margarita Yu. Grabovich. Mechanism of intracellular elemental sulfur oxidation in beggiatoa leptomitoformis, where persulfide dioxygenase plays a key role. International Journal of Molecular Sciences, 25:10962, Oct 2024. URL: https://doi.org/10.3390/ijms252010962, doi:10.3390/ijms252010962. This article has 6 citations.

20. (rudenko2024mechanismofintracellular pages 12-13): Tatyana S. Rudenko, Liubov I. Trubitsina, Vasily V. Terentyev, Ivan V. Trubitsin, Valentin I. Borshchevskiy, Svetlana V. Tishchenko, Azat G. Gabdulkhakov, Alexey A. Leontievsky, and Margarita Yu. Grabovich. Mechanism of intracellular elemental sulfur oxidation in beggiatoa leptomitoformis, where persulfide dioxygenase plays a key role. International Journal of Molecular Sciences, 25:10962, Oct 2024. URL: https://doi.org/10.3390/ijms252010962, doi:10.3390/ijms252010962. This article has 6 citations.

21. (cornell2024genomeencodedmetabolicpotential pages 86-89): C Cornell. Genome-encoded metabolic potential of the nitrosocosmicus genus and related ammonia-oxidizing archaea. Unknown journal, 2024.

22. (zhou2023effectsofacidification pages 5-6): Jie Zhou, Yanling Zheng, Lijun Hou, Zhirui An, Feiyang Chen, Bolin Liu, Li Wu, Lin Qi, Hongpo Dong, Ping Han, Guoyu Yin, Xia Liang, Yi Yang, Xiaofei Li, Dengzhou Gao, Ye Li, Zhanfei Liu, Richard Bellerby, and Min Liu. Effects of acidification on nitrification and associated nitrous oxide emission in estuarine and coastal waters. Nature Communications, Mar 2023. URL: https://doi.org/10.1038/s41467-023-37104-9, doi:10.1038/s41467-023-37104-9. This article has 94 citations and is from a highest quality peer-reviewed journal.

23. (zhang2023microbedrivenelementalcycling pages 4-6): Dechao Zhang, Xudong Li, Yuehong Wu, Xuewei Xu, Yanxia Liu, Benze Shi, Yujie Peng, Dadong Dai, Zhongli Sha, and Jinshui Zheng. Microbe-driven elemental cycling enables microbial adaptation to deep-sea ferromanganese nodule sediment fields. Microbiome, Jul 2023. URL: https://doi.org/10.1186/s40168-023-01601-2, doi:10.1186/s40168-023-01601-2. This article has 59 citations and is from a highest quality peer-reviewed journal.

24. (wang2024characterizethegrowth pages 13-15): Quansheng Wang, Haijun Long, Huiqi Wang, and Maggie C. Y. Lau Vetter. Characterize the growth and metabolism of acidithiobacillus ferrooxidans under electroautotrophic and chemoautotrophic conditions. Microorganisms, 12:590, Mar 2024. URL: https://doi.org/10.3390/microorganisms12030590, doi:10.3390/microorganisms12030590. This article has 9 citations.

25. (li2024yeeelikebacterialsoxt pages 1-2): Jingjing Li, Fabienne Göbel, Hsun Yun Hsu, Julian Nikolaus Koch, Natalie Hager, Wanda Antonia Flegler, Tomohisa Sebastian Tanabe, and Christiane Dahl. Yeee-like bacterial soxt proteins mediate sulfur import for oxidation and signal transduction. Communications Biology, Nov 2024. URL: https://doi.org/10.1038/s42003-024-07270-7, doi:10.1038/s42003-024-07270-7. This article has 7 citations and is from a peer-reviewed journal.

26. (li2024yeeelikebacterialsoxt pages 7-8): Jingjing Li, Fabienne Göbel, Hsun Yun Hsu, Julian Nikolaus Koch, Natalie Hager, Wanda Antonia Flegler, Tomohisa Sebastian Tanabe, and Christiane Dahl. Yeee-like bacterial soxt proteins mediate sulfur import for oxidation and signal transduction. Communications Biology, Nov 2024. URL: https://doi.org/10.1038/s42003-024-07270-7, doi:10.1038/s42003-024-07270-7. This article has 7 citations and is from a peer-reviewed journal.

27. (wang2024characterizethegrowth pages 22-23): Quansheng Wang, Haijun Long, Huiqi Wang, and Maggie C. Y. Lau Vetter. Characterize the growth and metabolism of acidithiobacillus ferrooxidans under electroautotrophic and chemoautotrophic conditions. Microorganisms, 12:590, Mar 2024. URL: https://doi.org/10.3390/microorganisms12030590, doi:10.3390/microorganisms12030590. This article has 9 citations.

28. (twible2024phandthiosulfate media 3cab23b0): Lauren E. Twible, Kelly Whaley-Martin, Lin-Xing Chen, Tara Colenbrander Nelson, James L.S. Arrey, Chad V. Jarolimek, Josh J. King, Lisa Ramilo, Helga Sonnenberg, Jillian F. Banfield, Simon C. Apte, and Lesley A. Warren. Ph and thiosulfate dependent microbial sulfur oxidation strategies across diverse environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1426584, doi:10.3389/fmicb.2024.1426584. This article has 24 citations and is from a peer-reviewed journal.

29. (shoemaker2024wood–ljungdahlpathwayencoding pages 11-12): Anna Shoemaker, Andrew Maritan, Su Cosar, Sylvia Nupp, Ana Menchaca, Thomas Jackson, Aria Dang, Bonnie K Baxter, Daniel R Colman, Eric C Dunham, and Eric S Boyd. Wood–ljungdahl pathway encoding anaerobes facilitate low-cost primary production in hypersaline sediments at great salt lake, utah. FEMS Microbiology Ecology, Jul 2024. URL: https://doi.org/10.1093/femsec/fiae105, doi:10.1093/femsec/fiae105. This article has 11 citations and is from a peer-reviewed journal.

30. (barla2024sustainablesynergisticapproach pages 2-3): Rachael J. Barla, Suresh Gupta, and Smita Raghuvanshi. Sustainable synergistic approach to chemolithotrophs—supported bioremediation of wastewater and flue gas. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-67053-2, doi:10.1038/s41598-024-67053-2. This article has 9 citations and is from a peer-reviewed journal.

31. (boersma2024metagenomicanalysisof pages 1-4): Alje S. Boersma, Signe Haukelidsaeter, Francesca Naletto, Caroline P. Slomp, Paul W.J.J. van der Wielen, Maartje A.H.J. van Kessel, and Sebastian Lücker. Metagenomic analysis of age-dependent microbial dynamics in dual-media rapid sand filters treating groundwater. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.25.630300, doi:10.1101/2024.12.25.630300. This article has 1 citations.

32. (li2024arcobacteraceaeareubiquitous pages 10-12): Jianyang Li, Shizheng Xiang, Yufei Li, Ruolin Cheng, Qiliang Lai, Liping Wang, Guizhen Li, Chunming Dong, and Zongze Shao. <i>arcobacteraceae</i> are ubiquitous mixotrophic bacteria playing important roles in carbon, nitrogen, and sulfur cycling in global oceans. Jul 2024. URL: https://doi.org/10.1128/msystems.00513-24, doi:10.1128/msystems.00513-24. This article has 31 citations and is from a peer-reviewed journal.

33. (barla2024sustainablesynergisticapproach pages 3-4): Rachael J. Barla, Suresh Gupta, and Smita Raghuvanshi. Sustainable synergistic approach to chemolithotrophs—supported bioremediation of wastewater and flue gas. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-67053-2, doi:10.1038/s41598-024-67053-2. This article has 9 citations and is from a peer-reviewed journal.