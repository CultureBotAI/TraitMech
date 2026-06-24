---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T22:45:33.500954'
end_time: '2026-06-17T23:07:02.812437'
duration_seconds: 1289.31
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: microaerophilic
  trait_identifier: METPO:1000604
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: microaerophilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "An oxygen preference that requires molecular oxygen (O\u2082) at concentrations\
    \ lower than atmospheric."
  parent_traits: METPO:1000601
  synonyms: Ox_microerophile, microaerophile
  evidence_summary: 'https://www.ncbi.nlm.nih.gov/books/NBK154539/: require oxygen
    to survive but require its presence in lower concentrations (Supports microaerophily
    as oxygen requirement below atmospheric concentration.) | PMID:26284041: C. jejuni
    is a microaerophilic, fastidious bacterium (Organism example: Campylobacter jejuni
    is described as microaerophilic.)'
  causal_graph_summary: 'microaerophile_low_oxygen_respiration: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** microaerophilic
- **METPO identifier:** METPO:1000604
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference that requires molecular oxygen (O₂) at concentrations lower than atmospheric.
- **Parent traits:** METPO:1000601
- **Synonyms:** Ox_microerophile, microaerophile
- **Existing evidence:** https://www.ncbi.nlm.nih.gov/books/NBK154539/: require oxygen to survive but require its presence in lower concentrations (Supports microaerophily as oxygen requirement below atmospheric concentration.) | PMID:26284041: C. jejuni is a microaerophilic, fastidious bacterium (Organism example: Campylobacter jejuni is described as microaerophilic.)
- **Existing causal graph summary:** microaerophile_low_oxygen_respiration: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **microaerophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/microaerophilic.yaml`.

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
- **Trait label:** microaerophilic
- **METPO identifier:** METPO:1000604
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference that requires molecular oxygen (O₂) at concentrations lower than atmospheric.
- **Parent traits:** METPO:1000601
- **Synonyms:** Ox_microerophile, microaerophile
- **Existing evidence:** https://www.ncbi.nlm.nih.gov/books/NBK154539/: require oxygen to survive but require its presence in lower concentrations (Supports microaerophily as oxygen requirement below atmospheric concentration.) | PMID:26284041: C. jejuni is a microaerophilic, fastidious bacterium (Organism example: Campylobacter jejuni is described as microaerophilic.)
- **Existing causal graph summary:** microaerophile_low_oxygen_respiration: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **microaerophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/microaerophilic.yaml`.

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


## Microbial trait causal graph curation report: **microaerophilic** (METPO:1000604)

### Scope summary (TraitMech curation perspective)
**Microaerophilic** denotes an **oxygen preference/requirement** in which organisms **use/require O\₂** but grow optimally at **O\₂ concentrations below atmospheric (~21%)**, and often display **growth inhibition** at atmospheric O\₂. This is an **environmental preference phenotype** commonly operationalized by growth under defined **microaerobic gas mixes** or **low dissolved oxygen (DO) windows**. A key nuance is that microaerophily is **species- and assay-dependent**, with different organisms exhibiting different DO optima and toxicity thresholds; “microaerobe” has been proposed as a more mechanistically grounded term for organisms able to respire in microoxic environments via **high-affinity terminal oxidases**. (fuduche2019anovelhighly pages 1-2, wallace2018metabolicandphysiological pages 40-45)

**Operational oxygen windows and boundary cases (examples used in literature):**
- *Magnetospira* sp. QH-2 (microaerophilic) reported optimal growth at **~2–40 µM DO**, compared with *Magnetospirillum gryphiswaldense* MSR-1 (facultative anaerobe) with a broader **0.2–210 µM DO** optimal window; water saturation at 21% O\₂ is ~284 µM at 20°C, contextualizing these microoxic ranges. (fuduche2019anovelhighly pages 1-2)
- *Campylobacter jejuni* is often cultured in “microaerobic conditions” such as **10–12% O\₂ with 5% CO\₂** (balance N\₂), and also studied under **oxygen-limited ~0.3% O\₂** in some experiments. (wallace2018metabolicandphysiological pages 40-45)
- *Helicobacter pylori* is commonly compared under **5% O\₂ (microaerobic) vs 20% O\₂ (aerobic)** conditions. (wallace2018metabolicandphysiological pages 40-45)
- *Sulfurospirillum multivorans* shows growth similar to anoxic controls at **5% O\₂** but growth cessation at **20% O\₂**, and a process-specific threshold where PCE dechlorination persists up to **~0.5% gas-phase O\₂ (~0.19 mg/mL dissolved O\₂)** but is inhibited above this level. (gadkari2018purificationofthe pages 137-141)

**Distinguishing from nearby traits (curation notes):**
- **Facultative anaerobe:** can grow with or without O\₂; may still have microoxic optima but does not *require* low O\₂ (e.g., MSR-1 has broad DO window). (fuduche2019anovelhighly pages 1-2)
- **Aerotolerant/oxygen-tolerant strains:** may survive at atmospheric O\₂ despite being categorized as microaerophilic (important boundary case; often linked to enhanced ROS defense). (delaporte2024aerotolerancyofcampylobacter pages 8-9, delaporte2024aerotolerancyofcampylobacter pages 9-11)
- **Capnophile:** CO\₂ requirement is frequently paired with microaerobic cultivation for some taxa (e.g., *Campylobacter*/*Helicobacter*), but CO\₂ preference is a distinct trait axis; microaerophily should not be conflated with CO\₂ dependence. (wallace2018metabolicandphysiological pages 40-45)

### Current mechanistic understanding (key concepts)
Microaerophily is typically enabled by a combination of:
1. **High-affinity terminal oxidases** that can reduce O\₂ at low pO\₂ (e.g., **cbb\₃-type cytochrome c oxidase**; **cytochrome bd-type quinol oxidase**). (azarkina2023interactionofterminal pages 1-2, rogers2023thephysiologyand pages 29-33)
2. **Branched respiratory chains** that allow **switching** among oxidases with different oxygen affinities/energetic efficiencies depending on O\₂ availability. A 2024 chemostat/proteomics study explicitly demonstrates oxygen-dependent abundance patterns of terminal oxidases across defined microaerobic O\₂ setpoints (0.25–4.2% O\₂). (jong2024quantitativeproteomicsreveals pages 1-2, jong2024quantitativeproteomicsreveals media 2917ae65, jong2024quantitativeproteomicsreveals media 02574e95)
3. **Oxygen/redox sensing regulatory systems** (two-component systems; Fnr/Crp-family regulators; Arc system) that transcriptionally couple environmental oxygen to expression of respiratory modules and low-oxygen survival pathways (including denitrification in facultative contexts). (freddi2023brucellaspp.are pages 1-2, mele2023oxidoreductasesandmetal pages 16-17)
4. **Reactive oxygen species (ROS) detoxification capacity** and its regulation (catalase, peroxiredoxins, SOD; regulators such as **PerR** and **CosR** in *Campylobacter*), because partially reduced oxygen species and oxygen-sensitive metalloproteins can limit growth at higher O\₂. (stoakes2024identificationofcampylobacter pages 1-2, delaporte2024aerotolerancyofcampylobacter pages 9-11, delaporte2024aerotolerancyofcampylobacter pages 8-9)

### Recent developments and latest research (prioritizing 2023–2024)

#### 1) Quantitative oxygen-dependent remodeling of respiratory chains (2024)
A 2024 *Frontiers in Microbiology* study cultivated *Caldalkalibacillus thermarum* TA2.A1 in chemostats across **0.25%–4.2% O\₂** and quantified proteomic shifts. The authors report that **cytochrome aa\₃ oxidase** abundance is highest at **4.2% O\₂**, while **cytochrome ba\₃ oxidase** is more abundant at most lower O\₂ levels but declines below **~0.42% O\₂**; other predicted oxidases were not detected proteomically, highlighting both biological regulation and technical detection limits for membrane proteins. (jong2024quantitativeproteomicsreveals pages 1-2)

The paper includes a schematic of the branched respiratory chain, depicting multiple terminal oxidases (aa\₃/ba\₃/bb\₃/bd) as alternative O\₂-reducing modules, and a figure showing respiratory complex abundance patterns versus O\₂ setpoints. (jong2024quantitativeproteomicsreveals media 2917ae65, jong2024quantitativeproteomicsreveals media 02574e95)

#### 2) Terminal oxidases as canonical low-O\₂ modules (2023)
A 2023 review in *International Journal of Molecular Sciences* emphasizes that **cbb\₃-type cytochrome c oxidases** are **common in microaerophilic Proteobacteria**, and that **bd-type quinol oxidases** are widespread in bacteria/archaea living under **low-oxygen conditions**. These are high-value generic nodes for a TraitMech causal graph because they link oxygen availability to respiratory capacity at low pO\₂. (azarkina2023interactionofterminal pages 1-2)

#### 3) Regulatory and ROS-defense mechanisms in obligate microaerophiles (2024)
For *Campylobacter jejuni* and *C. coli* (obligate microaerophiles), a 2024 *BMC Microbiology* TraDIS study summarizes that optimal growth occurs at **~2–10% O\₂**, and highlights oxygen/ROS defense regulators:
- **PerR** negatively regulates superoxide/peroxide resistance genes in an iron-dependent manner, and has overlapping regulation with **Fur**.
- **CosR** regulates antioxidants involved in superoxide and peroxide defense.
- **KatA** is highlighted as the best characterized H\₂O\₂ scavenger.
- **AhpC** is considered the predominant H\₂O\₂ scavenger at **low oxygen**; additional peroxiredoxins (Tpx, Bcp) contribute. (stoakes2024identificationofcampylobacter pages 1-2)

A 2024 comprehensive review in *Pathogens* links *Campylobacter* oxygen tolerance/aerotolerance phenotypes to regulators and enzymes:
- **PerR inactivation** increases aerotolerance and H\₂O\₂ resistance and is associated with upregulation of **katA, ahpC, rrc, trxB**.
- **CosR** controls **AhpC, SodB, Dps, Rrc, LuxS** (repressing all except AhpC per the cited summary).
- Aerotolerant strains often show increased catalase and SOD activity; katA and sodB mutants show increased oxidative sensitivity.
These provide a mechanistic “oxygen toxicity ceiling” layer that helps explain why many microaerophiles fail at atmospheric O\₂ unless ROS defenses are unusually strong. (delaporte2024aerotolerancyofcampylobacter pages 9-11, delaporte2024aerotolerancyofcampylobacter pages 8-9)

#### 4) Oxygen-sensing regulatory architectures tied to low-O\₂ respiration (2023)
In *Brucella* (classically considered strictly aerobic but shown to have nitrate-dependent anaerobic growth in atypical strains), a 2023 *Microbiology Spectrum* study links **high-affinity oxidases (cbb\₃, bd)** to oxygen depletion resistance and respiratory flexibility, and highlights oxygen/redox sensing systems including **Fnr/Crp-family regulators**, and two-component systems (**NtrYX**, **RegA/RegB**) implicated in oxygen sensing and regulation of denitrification enzymes. While *Brucella* is not an obligate microaerophile, this paper provides high-confidence regulator/pathway nodes relevant to low-O\₂ adaptation that may appear in microaerophiles and microoxic niches. (freddi2023brucellaspp.are pages 1-2)

### Current applications and real-world implementations
- **Microaerophilic cultivation technology:** A “Micro-Oxygenated Culture Device (MOCD)” was developed to enable low-cost growth of microaerophilic microorganisms, and the authors provide quantitative DO sensitivity/optimal windows for two magnetotactic bacteria (microaerophilic QH-2 vs facultative anaerobe MSR-1). This type of device operationalizes the trait for assay and bioprocess contexts and supports ontology alignment of “microaerophilic growth condition” nodes. (fuduche2019anovelhighly pages 1-2, fuduche2019anovelhighly pages 3-5)
- **Controlled microaerobic chemostats/bioreactors:** Chemostat operation at defined microaerobic O\₂ setpoints (0.25–4.2% O\₂) enables quantification of respiratory remodeling; this approach supports TraitMech edges between oxygen levels and oxidase abundance/regulation. (jong2024quantitativeproteomicsreveals pages 1-2)
- **Clinical and food microbiology:** *Campylobacter* and *Helicobacter* routine culturing uses microaerophilic atmospheres (often with CO\₂), and recent reviews emphasize the public health relevance of strains with increased aerotolerance (survival at atmospheric oxygen during transmission). Mechanistically, this connects microaerophily traits to oxidative stress defenses and biofilm physiology. (wallace2018metabolicandphysiological pages 40-45, delaporte2024aerotolerancyofcampylobacter pages 8-9)

### Candidate causal graph nodes (grouped by type)

#### Environmental / experimental factors
- **Microoxic / low oxygen environment** (candidate ENVO label; curate as “low O\₂”/“microaerobic atmosphere”). (fuduche2019anovelhighly pages 1-2)
- **Atmospheric oxygen (~21% O\₂)** as inhibitory boundary condition for many microaerophiles. (gadkari2018purificationofthe pages 137-141, alqurashi2020theroleof pages 24-28)
- Operational assay gas mixes: **5% O\₂** (H. pylori), **10–12% O\₂ + 5% CO\₂** (C. jejuni), **0.25–4.2% O\₂** (chemostat setpoints), **0.3% O\₂** (oxygen-limited). (wallace2018metabolicandphysiological pages 40-45, jong2024quantitativeproteomicsreveals pages 1-2)

#### Respiratory pathways / modules
- **Aerobic electron transport chain (ETC)**; **branched respiratory chain**. (jong2024quantitativeproteomicsreveals pages 1-2, jong2024quantitativeproteomicsreveals media 2917ae65)
- **Denitrification pathway** (facultative low-O\₂ adaptation; nitrate-dependent anaerobiosis). (freddi2023brucellaspp.are pages 1-2)

#### Terminal oxidases (key mechanistic capacity nodes)
- **cbb\₃-type cytochrome c oxidase** (high-affinity heme–copper oxidase; common in microaerophilic Proteobacteria). (azarkina2023interactionofterminal pages 1-2)
- **Cytochrome bd-type quinol oxidase** (high-affinity, non-proton pumping; widespread under low O\₂). (azarkina2023interactionofterminal pages 1-2)
- Additional oxidases in branched chains (contextual exemplars): **aa\₃**, **ba\₃**, **bb\₃**, **bd**. (jong2024quantitativeproteomicsreveals media 2917ae65, jong2024quantitativeproteomicsreveals pages 1-2)

#### Genes / regulators (oxygen sensing, redox control, ROS response)
- **fixNOQP / ccoNOQP** (cbb\₃ oxidase genes; “common microaerobic oxidase” in α-rhizobia). (rogers2023thephysiologyand pages 29-33)
- **PerR** (iron-dependent peroxide stress regulator; negative regulator of oxidative-stress genes in *Campylobacter*). (stoakes2024identificationofcampylobacter pages 1-2, delaporte2024aerotolerancyofcampylobacter pages 9-11)
- **CosR** (response regulator controlling multiple antioxidant genes in *Campylobacter*). (delaporte2024aerotolerancyofcampylobacter pages 9-11, stoakes2024identificationofcampylobacter pages 1-2)
- **Fur** (iron regulator overlapping with oxidative-stress control). (stoakes2024identificationofcampylobacter pages 1-2, delaporte2024aerotolerancyofcampylobacter pages 9-11)
- **NtrYX**, **RegA/RegB** (two-component systems implicated in oxygen sensing and denitrification regulation in *Brucella*). (freddi2023brucellaspp.are pages 1-2)

#### ROS detoxification enzymes / stress proteins
- **KatA (catalase)** (H\₂O\₂ detox). (stoakes2024identificationofcampylobacter pages 1-2, delaporte2024aerotolerancyofcampylobacter pages 8-9)
- **AhpC (alkyl hydroperoxide reductase / peroxiredoxin)** (predominant H\₂O\₂ scavenger at low oxygen in *Campylobacter*). (stoakes2024identificationofcampylobacter pages 1-2)
- **SodB (superoxide dismutase)**. (delaporte2024aerotolerancyofcampylobacter pages 8-9, delaporte2024aerotolerancyofcampylobacter pages 9-11)
- **Tpx/Bcp** (peroxiredoxins contributing to H\₂O\₂ detox). (stoakes2024identificationofcampylobacter pages 1-2)

#### Chemicals (candidate CHEBI)
- **O\₂** (CHEBI:15379).
- **Hydrogen peroxide** (CHEBI:16240). (delaporte2024aerotolerancyofcampylobacter pages 8-9)
- **Superoxide** (CHEBI:18421; verify) (implied by SOD biology and “superoxide responsive” regulators). (stoakes2024identificationofcampylobacter pages 1-2)

### Evidence-backed candidate causal edges (curation table)
The following table is designed to be directly mined into `microaerophilic.yaml` as candidate triples with curator notes.

| Edge (Subject —predicate→ Object) | Node types | Suggested ontology grounding | Evidence snippet | Source | DOI/URL | Publication date/month | Curation notes |
|---|---|---|---|---|---|---|---|
| Low oxygen environment —enables growth of→ microaerophilic bacterium | environment → trait | ENVO:low oxygen [label only]; METPO:1000604 | “microaerophile… requiring atmospheres low in O2 (less than 21%) for optimal growth” and QH-2 “grows optimally from 2.0 to 40 µM” dissolved O2 | Fuduche et al., 2019, *A Novel Highly Efficient Device for Growing Micro-Aerophilic Microorganisms* | https://doi.org/10.3389/fmicb.2019.00534 | 2019 Mar | Strong for trait definition; assay-specific to cultured magnetotactic bacteria; useful generic environment→trait edge (fuduche2019anovelhighly pages 1-2) |
| 5% O2 atmosphere —supports growth of→ microaerophilic bacterium | environment → trait | label only; METPO:1000604 | “H. pylori comparisons use microaerobic (5% O2) or aerobic (20% O2) conditions” | Wallace 2018, *Metabolic and Physiological Determinants in Listeria monocytogenes Anaerobic Virulence Regulation* | URL not available in gathered context | 2018 | Assay-operational edge; generic but derived from H. pylori experimental conditions; curate as experimental support rather than universal biological law (wallace2018metabolicandphysiological pages 40-45) |
| 10–12% O2 atmosphere —supports growth of→ Campylobacter jejuni | environment → taxon/trait | NCBITaxon:197; METPO:1000604 | “C. jejuni, ‘microaerobic conditions (5% CO2 and 10-12% O2 in N2 balance)’” | Wallace 2018, *Metabolic and Physiological Determinants in Listeria monocytogenes Anaerobic Virulence Regulation* | URL not available in gathered context | 2018 | Strong but taxon-specific assay condition for C. jejuni; helps define boundary conditions (wallace2018metabolicandphysiological pages 40-45) |
| Atmospheric oxygen (~20–21% O2) —inhibits growth of→ microaerophilic bacterium | environment → trait | label only; METPO:1000604 | microaerophiles are organisms that “cannot grow at normal atmospheric O2” and S. multivorans “20% O2 stopped growth” | Alqurashi 2020, *The Role of Flavodoxin in The Food-Borne Pathogen Campylobacter jejuni*; Gadkari et al. 2018 | URL not available; URL not available | 2020; 2018 | Strong for boundary distinction; second clause taxon-specific to S. multivorans (alqurashi2020theroleof pages 24-28, gadkari2018purificationofthe pages 137-141) |
| cbb3-type cytochrome c oxidase —enables→ respiration under low O2 | protein complex/pathway | GO:0004129; EC:7.1.1.9 [candidate]; label “cbb3-type cytochrome c oxidase” | “cbb3-type cytochrome c oxidases… are common in microaerophilic Proteobacteria” | Azarkina et al., 2023, *Interaction of Terminal Oxidases with Amphipathic Molecules* | https://doi.org/10.3390/ijms24076428 | 2023 Mar | Broad review-level support; good generic node/edge for TraitMech; not all microaerophiles use cbb3 (azarkina2023interactionofterminal pages 1-2) |
| cytochrome bd oxidase —enables→ respiration under low O2 | protein complex/pathway | GO:0008137 [quinol oxidase activity, candidate]; label “cytochrome bd ubiquinol oxidase”; EC:7.1.1.7 [candidate] | “bd-type quinol oxidases… are widespread in bacteria and archaea that live under low-oxygen conditions” | Azarkina et al., 2023, *Interaction of Terminal Oxidases with Amphipathic Molecules* | https://doi.org/10.3390/ijms24076428 | 2023 Mar | Broad review support; strong generic low-O2 respiration edge; ontology grounding may need curator verification (azarkina2023interactionofterminal pages 1-2) |
| fixNOQP/ccoNOQP (cbb3 oxidase genes) —encodes→ cbb3-type cytochrome c oxidase | gene cluster → protein complex | label “fixNOQP/ccoNOQP”; GO:0004129 | “subfamily C (cbb3-type, encoded by fixNOQP) is the common microaerobic oxidase in α-rhizobia” | Rogers 2023, *The Physiology and Symbiotic Characterisation of Paraburkholderia sprentiae WSM5005* | URL not available in gathered context | 2023 | Strong for rhizobia and related taxa; taxon-focused but mechanistically clear gene→complex edge (rogers2023thephysiologyand pages 29-33) |
| cbb3-type cytochrome c oxidase —supports→ microaerobic growth | protein complex → trait | GO:0004129; METPO:1000604 | “the common microaerobic oxidase in α-rhizobia” and “high O2 affinity” | Rogers 2023, *The Physiology and Symbiotic Characterisation of Paraburkholderia sprentiae WSM5005* | URL not available in gathered context | 2023 | Strong but taxon-anchored; good canonical edge for microaerophily graph (rogers2023thephysiologyand pages 29-33) |
| cytochrome bd oxidase —provides redundancy for→ respiration under varying O2 | protein complex → pathway/process | label “cytochrome bd ubiquinol oxidase”; GO:0019646 [aerobic electron transport chain, candidate] | “Cytochrome bd… provides redundancy in branched respiratory chains, supporting respiration… under varying O2” | Rogers 2023, *The Physiology and Symbiotic Characterisation of Paraburkholderia sprentiae WSM5005* | URL not available in gathered context | 2023 | Moderate support; phrased from rhizobial context; useful for accessory/compensatory mechanism node (rogers2023thephysiologyand pages 29-33) |
| High-affinity terminal oxidases (cbb3, bd) —increase→ respiratory flexibility during oxygen depletion | protein complexes → process | label only | “the cbb3-type cytochrome c oxidase and the cytochrome bd ubiquinol oxidase… contribute to resistance to oxygen depletion and… high respiratory flexibility” | Freddi et al., 2023, *Brucella spp. are facultative anaerobic bacteria under denitrifying conditions* | https://doi.org/10.1128/spectrum.02767-23 | 2023 Dec | Strong but in Brucella context; note Brucella are facultative anaerobes, so use for mechanism not trait identity (freddi2023brucellaspp.are pages 1-2) |
| NtrYX two-component system —regulates→ adaptation to oxygen depletion | regulatory system → process | label “NtrYX”; GO:0000156 [two-component response regulator activity, candidate] | “NtrYX and RegA/RegB… are involved in oxygen sensing and regulation… and in adaptation… to oxygen depletion” | Freddi et al., 2023, *Brucella spp. are facultative anaerobic bacteria under denitrifying conditions* | https://doi.org/10.1128/spectrum.02767-23 | 2023 Dec | Moderate support; taxon-specific to Brucella in excerpt; useful as candidate oxygen-sensing regulator node, uncertain for generic microaerophiles (freddi2023brucellaspp.are pages 1-2) |
| RegA/RegB two-component system —regulates→ denitrification enzymes under oxygen depletion | regulatory system → pathway | label “RegA/RegB”; GO:0000156 [candidate] | “RegA/RegB… involved in oxygen sensing and regulation of the denitrification enzymes” | Freddi et al., 2023, *Brucella spp. are facultative anaerobic bacteria under denitrifying conditions* | https://doi.org/10.1128/spectrum.02767-23 | 2023 Dec | Moderate; ties low-O2 sensing to respiratory pathway switching; more about facultative low-O2 adaptation than obligate microaerophily (freddi2023brucellaspp.are pages 1-2) |
| PerR —negatively regulates→ katA/ahpC/rrc/trxB oxidative stress genes | regulator → genes/pathway | label “PerR”; label “katA/ahpC/rrc/trxB” | “Inactivation of the PerR repressor increases aerotolerance and H2O2 resistance and upregulates katA, ahpC, rrc, and trxB” | Delaporte et al., 2024, *Aerotolerancy of Campylobacter spp.: A Comprehensive Review* | https://doi.org/10.3390/pathogens13100842 | 2024 Sep | Strong for Campylobacter oxidative-stress control; regulator edge is taxon-specific but central to microaerophilic oxygen sensitivity (delaporte2024aerotolerancyofcampylobacter pages 9-11) |
| PerR loss/inactivation —increases→ aerotolerance/H2O2 resistance | regulator state → phenotype | label “PerR loss-of-function”; label “aerotolerance” | “Inactivation of the PerR repressor increases aerotolerance and H2O2 resistance” | Delaporte et al., 2024, *Aerotolerancy of Campylobacter spp.: A Comprehensive Review* | https://doi.org/10.3390/pathogens13100842 | 2024 Sep | Strong phenotype edge but note it may shift away from canonical microaerophily toward aerotolerance; not a direct positive edge to microaerophilic trait (delaporte2024aerotolerancyofcampylobacter pages 9-11) |
| CosR —regulates→ AhpC/SodB/Dps/Rrc/LuxS | regulator → genes | label “CosR”; label “AhpC/SodB/Dps/Rrc/LuxS” | “CosR is a response regulator controlling AhpC, SodB, Dps, Rrc, and LuxS” | Delaporte et al., 2024, *Aerotolerancy of Campylobacter spp.: A Comprehensive Review* | https://doi.org/10.3390/pathogens13100842 | 2024 Sep | Strong Campylobacter-specific regulator edge; useful in ROS-defense branch of graph (delaporte2024aerotolerancyofcampylobacter pages 9-11) |
| CosR —represses→ SodB/Dps/Rrc/LuxS | regulator → genes | label “CosR”; label “SodB/Dps/Rrc/LuxS” | “it represses all of these except AhpC” | Delaporte et al., 2024, *Aerotolerancy of Campylobacter spp.: A Comprehensive Review* | https://doi.org/10.3390/pathogens13100842 | 2024 Sep | Strong but nuanced: AhpC is exception; consider splitting positive and negative edges in curation (delaporte2024aerotolerancyofcampylobacter pages 9-11) |
| CosR —activates→ ahpC | regulator → gene | label “CosR”; label “ahpC” | “it represses all of these except AhpC” | Delaporte et al., 2024, *Aerotolerancy of Campylobacter spp.: A Comprehensive Review* | https://doi.org/10.3390/pathogens13100842 | 2024 Sep | Moderate inference from exception wording; curator should check primary papers before hard-curating activation polarity (delaporte2024aerotolerancyofcampylobacter pages 9-11) |
| katA catalase —detoxifies→ hydrogen peroxide | gene/protein → chemical | label “katA/catalase”; CHEBI:16240 | “katA encodes catalase that prevents H2O2 accumulation” | Delaporte et al., 2024, *Aerotolerancy of Campylobacter spp.: A Comprehensive Review* | https://doi.org/10.3390/pathogens13100842 | 2024 Sep | Strong generic biochemical edge, supported in Campylobacter context (delaporte2024aerotolerancyofcampylobacter pages 8-9) |
| ahpC alkyl hydroperoxide reductase —scavenges→ H2O2 at low oxygen | gene/protein → chemical/process | label “ahpC/AhpC”; CHEBI:16240 | “AhpC is considered the predominant H2O2 scavenger at low oxygen” | Stoakes et al., 2024, *Identification of Campylobacter jejuni and Campylobacter coli genes contributing to oxidative stress response using TraDIS analysis* | https://doi.org/10.1186/s12866-024-03201-y | 2024 Feb | Strong and highly relevant to microaerophily; taxon-specific to Campylobacter but likely generalizable as ROS-defense mechanism (stoakes2024identificationofcampylobacter pages 1-2) |
| sodB superoxide dismutase —protects against→ reactive oxygen species | gene/protein → chemical class | label “sodB/SOD”; CHEBI:25520 [superoxide, candidate] | “sodB encodes superoxide dismutase (SOD); it protects against ROS” | Delaporte et al., 2024, *Aerotolerancy of Campylobacter spp.: A Comprehensive Review* | https://doi.org/10.3390/pathogens13100842 | 2024 Sep | Strong oxidative defense edge in Campylobacter; general ROS-protection role (delaporte2024aerotolerancyofcampylobacter pages 8-9) |
| Oxidative stress / high O2 exposure —induces→ AhpC | environment/process → protein | label “oxidative stress”; label “AhpC” | “AhpC strongly upregulated at 20% O2” | Gadkari et al. 2018, *Purification of the periplasmatic component of a putative quinol dehydrogenase involved in tetrachloroethene respiration in Sulfurospirillum multivorans* | URL not available in gathered context | 2018 | Strong but organism-specific; assay at 20% O2; useful for ROS-response branch, not direct cause of microaerophily (gadkari2018purificationofthe pages 137-141) |
| Oxidative stress / high O2 exposure —induces→ catalase | environment/process → protein | label “oxidative stress”; label “catalase” | “catalase detected only at 20% O2” | Gadkari et al. 2018, *Purification of the periplasmatic component of a putative quinol dehydrogenase involved in tetrachloroethene respiration in Sulfurospirillum multivorans* | URL not available in gathered context | 2018 | Strong but taxon-specific and assay-specific; good inducible-defense edge (gadkari2018purificationofthe pages 137-141) |
| 20% O2 atmosphere —stops growth of→ Sulfurospirillum multivorans | environment → taxon | NCBITaxon:844; label only | “Growth at 5% O2 resembled control… whereas 20% O2 stopped growth” | Gadkari et al. 2018, *Purification of the periplasmatic component of a putative quinol dehydrogenase involved in tetrachloroethene respiration in Sulfurospirillum multivorans* | URL not available in gathered context | 2018 | Strong taxon-specific boundary edge; useful exemplar of atmospheric O2 intolerance (gadkari2018purificationofthe pages 137-141) |
| 0.5% gas-phase O2 (≈0.19 mg/ml dissolved O2) —permits→ PCE dechlorination in S. multivorans | environment → process | label only | “Reductive dehalogenation activity was observed up to about 0.19 mg/ml dissolved O2 (…0.5% in the gas phase); above 0.5% O2 PCE dechlorination was inhibited” | Gadkari et al. 2018, *Purification of the periplasmatic component of a putative quinol dehydrogenase involved in tetrachloroethene respiration in Sulfurospirillum multivorans* | URL not available in gathered context | 2018 | Strong assay-specific threshold; more process-specific than generic growth, but informative quantitative low-O2 boundary (gadkari2018purificationofthe pages 137-141) |
| Lower O2 (vs 4.2% O2) —shifts abundance toward→ ba3 over aa3 terminal oxidase | environment → protein complexes | label “cytochrome ba3 oxidase”; label “cytochrome aa3 oxidase” | “aa3… highest at 4.2% O2” while “ba3 was more abundant at most other O2 levels” | de Jong et al., 2024, *Quantitative proteomics reveals oxygen-induced adaptations in Caldalkalibacillus thermarum TA2.A1 microaerobic chemostat cultures* | https://doi.org/10.3389/fmicb.2024.1468929 | 2024 Oct | Strong quantitative oxygen-response edge, but not direct microaerophile-defining mechanism; useful comparator/graph expansion beyond cbb3/bd (jong2024quantitativeproteomicsreveals pages 1-2, jong2024quantitativeproteomicsreveals media 2917ae65) |
| Branched respiratory chain —enables→ adaptation to fluctuating oxygen | pathway → process/trait support | GO:0022904 [respiratory electron transport chain]; label only | “branched respiratory chains enable microbes to adapt to fluctuating oxygen” | de Jong et al., 2024, *Quantitative proteomics reveals oxygen-induced adaptations in Caldalkalibacillus thermarum TA2.A1 microaerobic chemostat cultures* | https://doi.org/10.3389/fmicb.2024.1468929 | 2024 Oct | Strong general mechanistic principle; broad but useful as higher-level pathway node (jong2024quantitativeproteomicsreveals pages 1-2, jong2024quantitativeproteomicsreveals media 2917ae65) |


*Table: This table compiles candidate causal edges for curating the microbial trait microaerophilic (METPO:1000604), spanning low-oxygen environments, terminal oxidases, oxygen-sensing regulators, and ROS detox systems. It emphasizes source-backed mechanisms, suggested ontology grounding, and curation caveats such as taxon specificity and assay dependence.*

### Expert opinions / synthesis (authoritative-source analysis)
- Reviews emphasize that **terminal oxidase repertoire** (especially presence of **cbb\₃** and/or **bd**) is a canonical mechanistic basis for respiration under microoxic conditions, aligning well with microaerophily as a trait. (azarkina2023interactionofterminal pages 1-2)
- Recent experimental work supports an “**oxygen-dependent oxidase partitioning**” model where organisms modulate which terminal oxidase branches dominate depending on O\₂ (quantified in chemostats), suggesting a tractable causal link between environmental O\₂ levels and respiratory module abundance/activity. (jong2024quantitativeproteomicsreveals pages 1-2, jong2024quantitativeproteomicsreveals media 02574e95)
- In obligate microaerophiles such as *Campylobacter*, oxygen sensitivity is strongly tied to **ROS defense capacity and its transcriptional regulation** (PerR/CosR systems), providing a mechanistic rationale for why atmospheric O\₂ can be lethal while low O\₂ supports growth. (stoakes2024identificationofcampylobacter pages 1-2, delaporte2024aerotolerancyofcampylobacter pages 9-11)

### Relevant recent statistics and quantitative data
- **Microaerobic DO windows:** microaerophilic *Magnetospira* QH-2 optimum **~2–40 µM DO**, vs facultative anaerobe MSR-1 optimum **0.2–210 µM DO** (21% O\₂ saturation ~284 µM). (fuduche2019anovelhighly pages 1-2)
- **Chemostat oxygen setpoints (2024):** *C. thermarum* TA2.A1 studied across **0.25%–4.2% O\₂**, with oxidase abundance patterns changing around **~0.42% O\₂**. (jong2024quantitativeproteomicsreveals pages 1-2)
- **Campylobacter microaerophilic pO\₂:** described optimal growth at **~2–10% O\₂** (reviewed/introductory framing in 2024 TraDIS paper). (stoakes2024identificationofcampylobacter pages 1-2)
- **Threshold example (taxon/process-specific):** *S. multivorans* PCE dechlorination observed up to **~0.5% gas-phase O\₂ (~0.19 mg/mL dissolved O\₂)**; growth halted at **20% O\₂**. (gadkari2018purificationofthe pages 137-141)

### Visual evidence (mechanistic schematic)
- A branched respiratory chain schematic and oxygen-dependent proteomic abundance patterns for terminal oxidases in *C. thermarum* TA2.A1 are shown in figures retrieved from the 2024 study. These figures can support curator decisions about including “branched respiratory chain” and “terminal oxidase switching” nodes/edges. (jong2024quantitativeproteomicsreveals media 2917ae65, jong2024quantitativeproteomicsreveals media 02574e95)

### DOI-first bibliography (with URLs and publication dates where available)
1. de Jong SI, Wissink M, Yildirim K, et al. **Quantitative proteomics reveals oxygen-induced adaptations in *Caldalkalibacillus thermarum* TA2.A1 microaerobic chemostat cultures**. *Frontiers in Microbiology*. **Oct 2024**. DOI: **10.3389/fmicb.2024.1468929**. URL: https://doi.org/10.3389/fmicb.2024.1468929 (jong2024quantitativeproteomicsreveals pages 1-2)
2. Delaporte E, Karki AB, Fakhr MK. **Aerotolerancy of *Campylobacter* spp.: A Comprehensive Review**. *Pathogens*. **Sep 2024**. DOI: **10.3390/pathogens13100842**. URL: https://doi.org/10.3390/pathogens13100842 (delaporte2024aerotolerancyofcampylobacter pages 9-11, delaporte2024aerotolerancyofcampylobacter pages 8-9)
3. Stoakes E, Chen X, Kalmar L, et al. **Identification of *Campylobacter jejuni* and *Campylobacter coli* genes contributing to oxidative stress response using TraDIS analysis**. *BMC Microbiology*. **Feb 2024**. DOI: **10.1186/s12866-024-03201-y**. URL: https://doi.org/10.1186/s12866-024-03201-y (stoakes2024identificationofcampylobacter pages 1-2)
4. Freddi L, de la Garza-García JA, Al Dahouk S, et al. **Brucella spp. are facultative anaerobic bacteria under denitrifying conditions**. *Microbiology Spectrum*. **Dec 2023**. DOI: **10.1128/spectrum.02767-23**. URL: https://doi.org/10.1128/spectrum.02767-23 (freddi2023brucellaspp.are pages 1-2)
5. Azarkina NV, Borisov VB, Oleynikov IP, et al. **Interaction of Terminal Oxidases with Amphipathic Molecules**. *International Journal of Molecular Sciences*. **Mar 2023**. DOI: **10.3390/ijms24076428**. URL: https://doi.org/10.3390/ijms24076428 (azarkina2023interactionofterminal pages 1-2)
6. Fuduche M, Davidson S, Boileau C, Wu L-F, Combet-Blanc Y. **A Novel Highly Efficient Device for Growing Micro-Aerophilic Microorganisms**. *Frontiers in Microbiology*. **Mar 2019**. DOI: **10.3389/fmicb.2019.00534**. URL: https://doi.org/10.3389/fmicb.2019.00534 (fuduche2019anovelhighly pages 1-2, fuduche2019anovelhighly pages 3-5)

(Additional supporting context used for oxygen ranges/threshold exemplars: Wallace 2018 (wallace2018metabolicandphysiological pages 40-45); Gadkari 2018 (gadkari2018purificationofthe pages 137-141).)

### Warnings / “do not curate yet” flags
- **Activation vs repression polarity** for CosR→AhpC and CosR→(SodB/Dps/Rrc/LuxS) is summarized in a review; before hard-curating regulatory polarity edges, check the underlying primary experimental papers for directionality and conditions. (delaporte2024aerotolerancyofcampylobacter pages 9-11)
- Several edges are **taxon-specific** (e.g., Brucella denitrification regulation; Sulfurospirillum dechlorination thresholds) and should be tagged as **organism-/process-specific exemplars** rather than universal microaerophily mechanisms. (freddi2023brucellaspp.are pages 1-2, gadkari2018purificationofthe pages 137-141)
- Proteomics non-detection of certain terminal oxidases (bb\₃/bd) may reflect **technical limitations** rather than true absence of function under extreme low O\₂; curators may want to encode such edges with **uncertainty**. (jong2024quantitativeproteomicsreveals pages 1-2)


References

1. (fuduche2019anovelhighly pages 1-2): Maxime Fuduche, Sylvain Davidson, Céline Boileau, Long-Fei Wu, and Yannick Combet-Blanc. A novel highly efficient device for growing micro-aerophilic microorganisms. Frontiers in Microbiology, Mar 2019. URL: https://doi.org/10.3389/fmicb.2019.00534, doi:10.3389/fmicb.2019.00534. This article has 3 citations and is from a peer-reviewed journal.

2. (wallace2018metabolicandphysiological pages 40-45): NC Wallace. Metabolic and physiological determinants in listeria monocytogenes anaerobic virulence regulation. Unknown journal, 2018.

3. (gadkari2018purificationofthe pages 137-141): J Gadkari, T Schubert, and G Diekert. Purification of the periplasmatic component of a putative quinol dehydrogenase involved in tetrachloroethene respiration in sulfurospirillum multivorans. Unknown journal, 2018.

4. (delaporte2024aerotolerancyofcampylobacter pages 8-9): Elise Delaporte, Anand B. Karki, and Mohamed K. Fakhr. Aerotolerancy of campylobacter spp.: a comprehensive review. Pathogens, 13:842, Sep 2024. URL: https://doi.org/10.3390/pathogens13100842, doi:10.3390/pathogens13100842. This article has 8 citations.

5. (delaporte2024aerotolerancyofcampylobacter pages 9-11): Elise Delaporte, Anand B. Karki, and Mohamed K. Fakhr. Aerotolerancy of campylobacter spp.: a comprehensive review. Pathogens, 13:842, Sep 2024. URL: https://doi.org/10.3390/pathogens13100842, doi:10.3390/pathogens13100842. This article has 8 citations.

6. (azarkina2023interactionofterminal pages 1-2): Natalia V. Azarkina, Vitaliy B. Borisov, Ilya P. Oleynikov, Roman V. Sudakov, and Tatiana V. Vygodina. Interaction of terminal oxidases with amphipathic molecules. International Journal of Molecular Sciences, 24:6428, Mar 2023. URL: https://doi.org/10.3390/ijms24076428, doi:10.3390/ijms24076428. This article has 8 citations.

7. (rogers2023thephysiologyand pages 29-33): TH Rogers. The physiology and symbiotic characterisation of paraburkholderia sprentiae wsm5005. Unknown journal, 2023.

8. (jong2024quantitativeproteomicsreveals pages 1-2): Samuel I. de Jong, Martijn Wissink, Kadir Yildirim, Martin Pabst, Mark C. M. van Loosdrecht, and Duncan G. G. McMillan. Quantitative proteomics reveals oxygen-induced adaptations in caldalkalibacillus thermarum ta2.a1 microaerobic chemostat cultures. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1468929, doi:10.3389/fmicb.2024.1468929. This article has 4 citations and is from a peer-reviewed journal.

9. (jong2024quantitativeproteomicsreveals media 2917ae65): Samuel I. de Jong, Martijn Wissink, Kadir Yildirim, Martin Pabst, Mark C. M. van Loosdrecht, and Duncan G. G. McMillan. Quantitative proteomics reveals oxygen-induced adaptations in caldalkalibacillus thermarum ta2.a1 microaerobic chemostat cultures. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1468929, doi:10.3389/fmicb.2024.1468929. This article has 4 citations and is from a peer-reviewed journal.

10. (jong2024quantitativeproteomicsreveals media 02574e95): Samuel I. de Jong, Martijn Wissink, Kadir Yildirim, Martin Pabst, Mark C. M. van Loosdrecht, and Duncan G. G. McMillan. Quantitative proteomics reveals oxygen-induced adaptations in caldalkalibacillus thermarum ta2.a1 microaerobic chemostat cultures. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1468929, doi:10.3389/fmicb.2024.1468929. This article has 4 citations and is from a peer-reviewed journal.

11. (freddi2023brucellaspp.are pages 1-2): Luca Freddi, Jorge A. de la Garza-García, Sascha Al Dahouk, Alessandra Occhialini, and Stephan Köhler. <i>brucella</i> spp. are facultative anaerobic bacteria under denitrifying conditions. Dec 2023. URL: https://doi.org/10.1128/spectrum.02767-23, doi:10.1128/spectrum.02767-23. This article has 14 citations and is from a domain leading peer-reviewed journal.

12. (mele2023oxidoreductasesandmetal pages 16-17): Bruno Hay Mele, Maria Monticelli, Serena Leone, Deborah Bastoni, Bernardo Barosa, Martina Cascone, Flavia Migliaccio, Francesco Montemagno, Annarita Ricciardelli, Luca Tonietti, Alessandra Rotundi, Angelina Cordone, and Donato Giovannelli. Oxidoreductases and metal cofactors in the functioning of the earth. Essays in Biochemistry, 67:653-670, Aug 2023. URL: https://doi.org/10.1042/ebc20230012, doi:10.1042/ebc20230012. This article has 55 citations and is from a peer-reviewed journal.

13. (stoakes2024identificationofcampylobacter pages 1-2): Emily Stoakes, Xuanlin Chen, Lajos Kalmar, Dave J. Baker, Rhiannon Evans, Steven Rudder, and Andrew J Grant. Identification of campylobacter jejuni and campylobacter coli genes contributing to oxidative stress response using tradis analysis. BMC Microbiology, Feb 2024. URL: https://doi.org/10.1186/s12866-024-03201-y, doi:10.1186/s12866-024-03201-y. This article has 5 citations and is from a peer-reviewed journal.

14. (fuduche2019anovelhighly pages 3-5): Maxime Fuduche, Sylvain Davidson, Céline Boileau, Long-Fei Wu, and Yannick Combet-Blanc. A novel highly efficient device for growing micro-aerophilic microorganisms. Frontiers in Microbiology, Mar 2019. URL: https://doi.org/10.3389/fmicb.2019.00534, doi:10.3389/fmicb.2019.00534. This article has 3 citations and is from a peer-reviewed journal.

15. (alqurashi2020theroleof pages 24-28): A Alqurashi. The role of flavodoxin in the food-borne pathogen campylobacter jejuni. Unknown journal, 2020.