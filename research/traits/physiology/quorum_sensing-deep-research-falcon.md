---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T12:29:47.820503'
end_time: '2026-06-18T13:00:39.383808'
duration_seconds: 1851.56
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: quorum sensing
  trait_identifier: traitmech:000084
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: quorum_sensing
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell-density-dependent regulatory physiology in which cells produce,
    release, and detect diffusible autoinducer signals to coordinate gene expression
    across a population.
  parent_traits: METPO:1000059
  synonyms: autoinduction
  evidence_summary: 'DOI:10.1146/annurev.cellbio.21.012704.131001:  (Waters & Bassler
    review quorum sensing as autoinducer-mediated cell-to-cell communication coordinating
    population-wide behavior.) | DOI:10.1146/annurev.micro.55.1.165:  (Miller & Bassler
    review quorum sensing across bacteria and its regulatory logic.)'
  causal_graph_summary: 'quorum_sensing_autoinducer: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 43
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** quorum sensing
- **METPO identifier:** traitmech:000084
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-density-dependent regulatory physiology in which cells produce, release, and detect diffusible autoinducer signals to coordinate gene expression across a population.
- **Parent traits:** METPO:1000059
- **Synonyms:** autoinduction
- **Existing evidence:** DOI:10.1146/annurev.cellbio.21.012704.131001:  (Waters & Bassler review quorum sensing as autoinducer-mediated cell-to-cell communication coordinating population-wide behavior.) | DOI:10.1146/annurev.micro.55.1.165:  (Miller & Bassler review quorum sensing across bacteria and its regulatory logic.)
- **Existing causal graph summary:** quorum_sensing_autoinducer: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **quorum sensing** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/quorum_sensing.yaml`.

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
- **Trait label:** quorum sensing
- **METPO identifier:** traitmech:000084
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-density-dependent regulatory physiology in which cells produce, release, and detect diffusible autoinducer signals to coordinate gene expression across a population.
- **Parent traits:** METPO:1000059
- **Synonyms:** autoinduction
- **Existing evidence:** DOI:10.1146/annurev.cellbio.21.012704.131001:  (Waters & Bassler review quorum sensing as autoinducer-mediated cell-to-cell communication coordinating population-wide behavior.) | DOI:10.1146/annurev.micro.55.1.165:  (Miller & Bassler review quorum sensing across bacteria and its regulatory logic.)
- **Existing causal graph summary:** quorum_sensing_autoinducer: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **quorum sensing** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/quorum_sensing.yaml`.

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


## Microbial Trait Causal Graph Curation Report: Quorum Sensing (traitmech:000084)

### Scope summary (TraitMech definition alignment)
Quorum sensing (QS) is a **cell-density-dependent regulatory physiology** in which microbes **produce, release, accumulate, detect, and respond** to diffusible (or secreted) signal molecules (“autoinducers”), leading to **coordinated population-wide gene-expression changes** once a **threshold signal concentration** is reached. This “autoinduction” typically includes **positive feedback** that increases signal production upon activation. QS regulates many outputs (e.g., biofilm formation, virulence, metabolic adaptation) but the trait itself is the **signaling-and-response regulatory capacity**, not any single downstream phenotype. (sedarat2024quorumsensingin pages 1-3, juszczukkubiak2024molecularaspectsof pages 2-3)

**Boundary cases / exclusions for curation**
* Include: density/threshold-dependent autoinducer signaling circuits with defined signal production + detection + transcriptional/post-transcriptional response (e.g., LuxI/LuxR; Agr; AI‑2 phosphorelay). (li2024anengineeredescherichia pages 9-13, fang2024determinantsofmaturation pages 1-2, rajkhowa2024advancingantibioticresistantmicrobe pages 4-5)
* Exclude (as trait-defining nodes/edges): downstream outputs alone (biofilm/virulence) unless explicitly framed as QS-controlled; general “chemical signaling” not tied to population density/threshold logic; host endocrine cues unless explicitly integrated as QS inputs. (erkihun2024medicalscopeof pages 6-8, rajkhowa2024advancingantibioticresistantmicrobe pages 4-5)

### Key concepts and definitions (current understanding; 2024-focused)
* QS activation follows **signal accumulation to threshold** and detection by receptors/sensor kinases that alter gene expression. (juszczukkubiak2024molecularaspectsof pages 2-3, rajkhowa2024advancingantibioticresistantmicrobe pages 4-5)
* Major QS signal families commonly curated:
  * **AHL (AI‑1)** in many Gram-negative species (LuxI synthase; LuxR receptor/regulator). (rajkhowa2024advancingantibioticresistantmicrobe pages 4-5, juszczukkubiak2024molecularaspectsof pages 2-3)
  * **AIP peptides** in many Gram-positive species, often via **two-component systems** (histidine kinase + response regulator). (rajkhowa2024advancingantibioticresistantmicrobe pages 4-5, fang2024determinantsofmaturation pages 1-2)
  * **AI‑2** used across Gram-negative and Gram-positive bacteria, with Vibrio-style pathways involving **LuxP/LuxQ → LuxU → LuxO** phosphorelay. (rajkhowa2024advancingantibioticresistantmicrobe pages 4-5)
* Canonical assay/readout logic: the Lux system links AHL threshold sensing to **lux operon transcription and bioluminescence**, widely used as a QS reporter model. (li2024anengineeredescherichia pages 9-13, sedarat2024quorumsensingin pages 1-3)

### Recent developments and latest research (prioritizing 2023–2024)
#### 1) Mechanistic maturation of Gram-positive AIP signals (S. aureus Agr)
A 2024 primary study refined peptide maturation logic in **Staphylococcus aureus Agr**: the AIP precursor **AgrD** is processed by **two proteases**, with **AgrB** cleaving the C-terminal tail and promoting **thiolactone ring formation** (essential for signaling), and **MroQ** cleaving the N-terminal leader. The paper explicitly supports a tandem maturation process and shows **AgrB and MroQ are sufficient for AIP maturation in vitro**. (fang2024determinantsofmaturation pages 1-2)

#### 2) QS linked to oxidative-stress physiology and “priming” (S. aureus agr)
A 2024 eLife study provides an example of how QS integrates with stress defense: **agr deficiency increases endogenous ROS** and this explains increased susceptibility to lethal **H2O2**. The paper reports that **menadione pretreatment protected Δagr** during subsequent H2O2 challenge and that **sodA is required** for wild-type agr-mediated survival under H2O2 exposure. These findings motivate candidate edges linking QS → metabolic/ROS homeostasis → stress survival. (podkowik2024quorumsensingagrsystem pages 10-12, podkowik2024quorumsensingagrsystem pages 1-2)

#### 3) QS inhibition and quorum quenching (QQ) as anti-virulence/anti-biofilm strategy
Recent 2023–2024 reviews frame QS disruption as a major non-antibiotic strategy:
* “Quorum quenching” (QQ) includes **signal inactivation/degradation** (QQ enzymes) and **receptor inhibition** (QS inhibitors, QSIs). (juszczukkubiak2024molecularaspectsof pages 2-3, zhu2023innovativemicrobialdisease pages 1-2)
* A 2024 review on nanocarrier-based strategies emphasizes multi-point targeting of QS and highlights the threshold-driven cascade and feedback logic that make QS targetable. (rajkhowa2024advancingantibioticresistantmicrobe pages 4-5)

### Current applications and real-world implementations
1) **Anti-biofilm / anti-virulence therapeutics development**: QS inhibition is positioned as a way to attenuate virulence and biofilms without necessarily killing bacteria, potentially reducing selective pressure for resistance; reviews emphasize QSIs and QQ enzymes, plus adjunct modalities (nanoparticles, antibodies, probiotics, phage therapy). (juszczukkubiak2024molecularaspectsof pages 2-3)

2) **Agricultural/aquacultural biocontrol and wastewater engineering**: a 2023 review highlights QQ applications in plant/aquatic pathogen biocontrol and membrane bioreactors for wastewater treatment. (zhu2023innovativemicrobialdisease pages 1-2)

3) **Synthetic biology / biosensing platforms**: engineered LuxI/LuxR-based communities in E. coli allow tunable QS “sensing/production/degradation” modules with fluorescence/bioluminescence outputs, supporting experimental and applied biosensing or circuit design. (li2024anengineeredescherichia pages 1-5, li2024anengineeredescherichia pages 23-26)

### Relevant statistics and quantitative data (recent studies)
* Biofilm-associated antibiotic resistance can increase substantially; one 2024 review states biofilm bacteria can increase antibiotic resistance by **~1000-fold** (citing Hoiby et al.). (li2024anengineeredescherichia pages 9-13)
* 2024 hospital-environment MRSA dataset (Bangladesh; PLOS ONE):
  * **120 swabs**; **86/120 (71.67%)** S. aureus-positive.
  * Among phenotypic MRSA isolates, **56/86 (65.1%)** mecA-positive by PCR.
  * Among mecA-positive MRSA, **45/56 (80.35%)** were biofilm-forming by CVMP assay.
  * agr groups among biofilm-forming MRSA: **agr I 71.11%**, **agr III 17.78%**, **agr II 11.11%** (no agr IV). (rimi2024biofilmformationagr pages 1-2)
* AHL chemical diversity: one 2024 review states AHL side-chain lengths typically range **4–18 carbons**. (rajkhowa2024advancingantibioticresistantmicrobe pages 4-5)

### Candidate nodes for curation (grouped by type)
The following node inventory is derived from explicit mentions in 2023–2024 sources; suggested ontology grounding is included where clear.

| Node label | Type | Suggested grounding | Evidence/source (short) | Citation ID |
|---|---|---|---|---|
| acyl-homoserine lactones (AHLs; AI-1) | Signals/autoinducers | CHEBI:35222 | Primary Gram-negative QS signals; reviewed as major AI class | (juszczukkubiak2024molecularaspectsof pages 2-3, rajkhowa2024advancingantibioticresistantmicrobe pages 4-5) |
| N-(3-oxohexanoyl)-L-homoserine lactone (OHHL; 3-oxo-C6-HSL) | Signals/autoinducers | unresolved | Vibrio fischeri LuxI/LuxR model autoinducer | (li2024anengineeredescherichia pages 9-13) |
| N-(3-oxo-dodecanoyl)-L-homoserine lactone (3OC12-HSL) | Signals/autoinducers | unresolved | Pseudomonas aeruginosa LasI/LasR signal | (juszczukkubiak2024molecularaspectsof pages 2-3, erkihun2024medicalscopeof pages 6-8) |
| N-butanoyl-L-homoserine lactone (C4-HSL) | Signals/autoinducers | unresolved | Pseudomonas aeruginosa RhlI/RhlR signal | (juszczukkubiak2024molecularaspectsof pages 2-3, erkihun2024medicalscopeof pages 6-8) |
| autoinducing peptide (AIP) | Signals/autoinducers | unresolved | Gram-positive peptide autoinducer; Agr signal in S. aureus | (fang2024determinantsofmaturation pages 1-2) |
| autoinducer-2 (AI-2) | Signals/autoinducers | unresolved | Shared/inter-species QS signal in Gram-negative and Gram-positive bacteria | (sedarat2024quorumsensingin pages 1-3, rajkhowa2024advancingantibioticresistantmicrobe pages 4-5) |
| 4,5-dihydroxy-2,3-pentanedione (DPD) | Signals/autoinducers | CHEBI:17993 | AI-2 precursor listed in engineered QS system glossary | (li2024anengineeredescherichia pages 9-13) |
| diffusible signal factor (DSF; cis-11-methyl-2-dodecenoic acid) | Signals/autoinducers | unresolved | Fatty-acid signal linked to biofilm dispersion via c-di-GMP | (erkihun2024medicalscopeof pages 6-8) |
| PQS (Pseudomonas quinolone signal) | Signals/autoinducers | unresolved | Named alternative QS signal in Pseudomonas systems | (li2024anengineeredescherichia pages 9-13, hetta2024quorumsensinginhibitors pages 4-6) |
| CAI-1 | Signals/autoinducers | unresolved | Listed Vibrio autoinducer class | (li2024anengineeredescherichia pages 9-13) |
| HAI-1 | Signals/autoinducers | unresolved | Listed Vibrio autoinducer class | (li2024anengineeredescherichia pages 9-13) |
| LuxI | Synthases/processing enzymes | unresolved | Canonical AHL synthase; catalyzes OHHL/AI-1 synthesis | (li2024anengineeredescherichia pages 9-13) |
| LasI | Synthases/processing enzymes | unresolved | P. aeruginosa synthase for 3OC12-HSL | (juszczukkubiak2024molecularaspectsof pages 2-3) |
| RhlI | Synthases/processing enzymes | unresolved | P. aeruginosa synthase for C4-HSL | (juszczukkubiak2024molecularaspectsof pages 2-3) |
| LuxS | Synthases/processing enzymes | unresolved | AI-2 synthase/enzyme in LuxS/AI-2 system | (rajkhowa2024advancingantibioticresistantmicrobe pages 4-5, lawther2024—invitedreview pages 1-2) |
| AgrD | Synthases/processing enzymes | unresolved | S. aureus AIP precursor peptide | (fang2024determinantsofmaturation pages 1-2) |
| AgrB | Synthases/processing enzymes | unresolved | Cleaves AgrD C-terminus and promotes thiolactone formation | (fang2024determinantsofmaturation pages 1-2) |
| MroQ | Synthases/processing enzymes | unresolved | CAAX protease that removes AgrD N-terminal leader | (fang2024determinantsofmaturation pages 1-2) |
| AiiA lactonase | Synthases/processing enzymes | unresolved | AHL lactonase/quorum-quenching enzyme named in QS inhibition context | (li2024anengineeredescherichia pages 23-26) |
| c-di-GMP phosphodiesterase | Synthases/processing enzymes | GO:0008957 | Activated in DSF-linked dispersion pathway to degrade c-di-GMP | (erkihun2024medicalscopeof pages 6-8) |
| alginate lyase | Synthases/processing enzymes | EC:4.2.2.3 | EPS-degrading enzyme linked to biofilm detachment | (erkihun2024medicalscopeof pages 6-8) |
| LuxR | Receptors/regulators/two-component systems | unresolved | Canonical intracellular AHL-responsive transcriptional regulator | (li2024anengineeredescherichia pages 9-13) |
| LasR | Receptors/regulators/two-component systems | unresolved | P. aeruginosa AHL receptor/regulator | (juszczukkubiak2024molecularaspectsof pages 2-3, erkihun2024medicalscopeof pages 6-8) |
| RhlR | Receptors/regulators/two-component systems | unresolved | P. aeruginosa AHL receptor/regulator | (juszczukkubiak2024molecularaspectsof pages 2-3, erkihun2024medicalscopeof pages 6-8) |
| AgrC | Receptors/regulators/two-component systems | unresolved | S. aureus AIP-responsive histidine kinase | (fang2024determinantsofmaturation pages 1-2) |
| AgrA | Receptors/regulators/two-component systems | unresolved | S. aureus response regulator controlling virulence/RNA outputs | (fang2024determinantsofmaturation pages 1-2) |
| LuxP | Receptors/regulators/two-component systems | unresolved | AI-2 receptor component in Vibrio-style LuxP/LuxQ system | (rajkhowa2024advancingantibioticresistantmicrobe pages 4-5) |
| LuxQ | Receptors/regulators/two-component systems | unresolved | Sensor kinase component of AI-2 signaling | (rajkhowa2024advancingantibioticresistantmicrobe pages 4-5) |
| LuxU | Receptors/regulators/two-component systems | unresolved | Phosphotransfer protein in Vibrio AI-2 phosphorelay | (rajkhowa2024advancingantibioticresistantmicrobe pages 4-5) |
| LuxO | Receptors/regulators/two-component systems | unresolved | Regulatory protein in Vibrio AI-2 phosphorelay | (rajkhowa2024advancingantibioticresistantmicrobe pages 4-5) |
| ArcA/ArcB | Receptors/regulators/two-component systems | unresolved | Two-component system noted to repress luminescence in V. fischeri context | (li2024anengineeredescherichia pages 9-13) |
| lux box | Regulatory elements & RNAs | unresolved | Palindromic promoter element bound by LuxR-AHL complex | (juszczukkubiak2024molecularaspectsof pages 2-3, li2024anengineeredescherichia pages 9-13) |
| luxICDABEG operon | Regulatory elements & RNAs | unresolved | LuxR-activated operon driving bioluminescence | (li2024anengineeredescherichia pages 9-13) |
| RNAIII | Regulatory elements & RNAs | unresolved | Major Agr effector RNA in S. aureus | (li2024anengineeredescherichia pages 17-20, kuai2024roleofsara pages 6-9) |
| P2 promoter | Regulatory elements & RNAs | unresolved | AgrA-activated promoter driving agr operon transcription | (li2024anengineeredescherichia pages 17-20, madarova2024noveltherapeutictargeting pages 18-21) |
| P3 promoter | Regulatory elements & RNAs | unresolved | AgrA-activated promoter driving RNAIII transcription | (li2024anengineeredescherichia pages 17-20, madarova2024noveltherapeutictargeting pages 18-21) |
| quorum regulatory sRNA(s) | Regulatory elements & RNAs | unresolved | Small RNAs named in QS regulatory context | (li2024anengineeredescherichia pages 9-13, simpson2024quorumsensingin pages 25-26) |
| c-di-GMP | Second messengers | CHEBI:17968 | Second messenger degraded during DSF-linked dispersion | (erkihun2024medicalscopeof pages 6-8) |
| reactive oxygen species (ROS) | Second messengers | CHEBI:26523 | agr status affects endogenous ROS accumulation in S. aureus | (podkowik2024quorumsensingagrsystem pages 1-2, podkowik2024quorumsensingagrsystem pages 10-12) |
| bioluminescence | Phenotypic outputs | GO:0008218 | Classic LuxI/LuxR-regulated output in V. fischeri | (li2024anengineeredescherichia pages 9-13) |
| biofilm formation | Phenotypic outputs | GO:0042710 | Recurrently described QS-regulated phenotype | (sedarat2024quorumsensingin pages 1-3, juszczukkubiak2024molecularaspectsof pages 2-3) |
| biofilm dispersion/detachment | Phenotypic outputs | GO:1900236 | DSF/c-di-GMP-linked release of planktonic cells | (erkihun2024medicalscopeof pages 6-8) |
| virulence factor production | Phenotypic outputs | GO:0044003 | Central QS-regulated output across taxa | (juszczukkubiak2024molecularaspectsof pages 2-3, sedarat2024quorumsensingin pages 1-3) |
| antibiotic resistance/tolerance | Phenotypic outputs | GO:0046677 | QS associated with antibiotic tolerance/resistance phenotypes | (li2024anengineeredescherichia pages 9-13, rimi2024biofilmformationagr pages 1-2) |
| motility | Phenotypic outputs | GO:0048870 | Listed as QS-regulated physiological process | (erkihun2024medicalscopeof pages 6-8, sedarat2024quorumsensingin pages 1-3) |
| sporulation | Phenotypic outputs | GO:0043934 | Listed as QS-regulated process | (rajkhowa2024advancingantibioticresistantmicrobe pages 4-5, zhu2023innovativemicrobialdisease pages 1-2) |
| pyocyanin production | Phenotypic outputs | unresolved | Las/Rhl-regulated virulence metabolite output | (juszczukkubiak2024molecularaspectsof pages 2-3, hetta2024quorumsensinginhibitors pages 4-6) |
| rhamnolipid production | Phenotypic outputs | unresolved | QS-regulated exoproduct in Pseudomonas/Serratia contexts | (juszczukkubiak2024molecularaspectsof pages 2-3, hetta2024quorumsensinginhibitors pages 4-6) |
| high cell density | Environmental/experimental factors | ENVO:01000686 | Threshold condition for signal accumulation and QS activation | (juszczukkubiak2024molecularaspectsof pages 2-3, sedarat2024quorumsensingin pages 1-3) |
| threshold autoinducer concentration | Environmental/experimental factors | unresolved | Defining activation condition for QS | (juszczukkubiak2024molecularaspectsof pages 2-3, rajkhowa2024advancingantibioticresistantmicrobe pages 4-5) |
| nutrient limitation/starvation | Environmental/experimental factors | ENVO:01000360 | Trigger associated with DSF-linked dispersion pathway | (erkihun2024medicalscopeof pages 6-8) |
| oxygen shortage | Environmental/experimental factors | ENVO:01000949 | Trigger associated with biofilm dispersion | (erkihun2024medicalscopeof pages 6-8) |
| hydrogen peroxide (H2O2) exposure | Environmental/experimental factors | CHEBI:16240 | Oxidative-stress condition revealing agr-protective effects | (podkowik2024quorumsensingagrsystem pages 1-2) |
| menadione pretreatment | Environmental/experimental factors | CHEBI:41078 | Experimental perturbation that protected Δagr during H2O2 challenge | (podkowik2024quorumsensingagrsystem pages 10-12, podkowik2024quorumsensingagrsystem pages 12-14) |
| bioluminescence reporter | Assays/reporters | unresolved | Canonical readout of Lux QS activation | (sedarat2024quorumsensingin pages 1-3, li2024anengineeredescherichia pages 9-13) |
| fluorescent reporter strains (EGFP/EBFP2) | Assays/reporters | unresolved | Engineered E. coli QS reporter system | (li2024anengineeredescherichia pages 1-5, li2024anengineeredescherichia pages 9-13) |
| OD600 | Assays/reporters | unresolved | Growth measurement used alongside engineered QS assays | (li2024anengineeredescherichia pages 9-13) |
| fluorescence intensity (FI) | Assays/reporters | unresolved | Quantitative readout in engineered QS system | (li2024anengineeredescherichia pages 9-13) |
| Chromobacterium violaceum CV026 | Assays/reporters | NCBITaxon:243233 | Whole-cell biosensor for AI-1/AHL activity | (li2024anengineeredescherichia pages 23-26) |
| Vibrio harveyi BB170 | Assays/reporters | unresolved | Whole-cell biosensor for AI-2 activity | (li2024anengineeredescherichia pages 23-26) |
| Crystal Violet Microtiter Plate (CVMP) assay | Assays/reporters | unresolved | Biofilm quantification assay used in MRSA prevalence study | (rimi2024biofilmformationagr pages 1-2) |


*Table: This table lists candidate nodes for a TraitMech quorum sensing causal graph, grouped by biological type and annotated with suggested grounding and recent evidence sources. It is useful as a curation-ready inventory for selecting node labels and ontology mappings in `quorum_sensing.yaml`.*

### Candidate evidence-backed causal edges (triples)
The table below proposes curation-ready edges with snippet-level evidence, references, and qualifiers.

| Edge (S–P–O) | Evidence snippet (short quote) | Reference (DOI/URL, year) | Citation ID | Notes/curation qualifiers |
|---|---|---|---|---|
| LuxI — synthesizes — OHHL/3-oxo-C6-HSL | “the autoinducer N-(3-oxohexanoyl)-L-homoserine lactone (OHHL) is synthesised” | 10.3390/synbio1020010 / https://doi.org/10.3390/synbio1020010 (2024) | (li2024anengineeredescherichia pages 9-13) | Gram-negative LuxI/LuxR model; Vibrio fischeri-specific example. |
| OHHL — binds/activates — LuxR | “OHHL accumulates and binds to the transcriptional regulator LuxR, resulting in the activation of LuxR” | 10.3390/synbio1020010 / https://doi.org/10.3390/synbio1020010 (2024) | (li2024anengineeredescherichia pages 9-13) | Canonical Gram-negative QS edge; taxon/model specific but broadly representative. |
| Activated LuxR — activates transcription of — luxICDABEG operon | “The activated LuxR binds to the lux box and activates transcription of the luxICDABEG operon” | 10.3390/synbio1020010 / https://doi.org/10.3390/synbio1020010 (2024) | (li2024anengineeredescherichia pages 9-13) | Direct reporter-output edge; bioluminescence assayable. |
| LuxR–AHL complex — promotes transcription of — luxI | “AHLs together with LuxR form a LuxR–AHLs complex that recognises the ‘lux box’ of luxI to promote the luxI transcription, described explicitly as creating a positive feedback loop” | 10.3390/ijms25052655 / https://doi.org/10.3390/ijms25052655 (2024) | (juszczukkubiak2024molecularaspectsof pages 2-3) | Positive-feedback core of autoinduction; Gram-negative. |
| High cell density / threshold AI concentration — enables detection by — cognate sensor proteins | “Once the concentration of secreted AI molecules has reached a threshold level, they are detected by cognate sensor proteins” | 10.3390/ijms25052655 / https://doi.org/10.3390/ijms25052655 (2024) | (juszczukkubiak2024molecularaspectsof pages 2-3) | Generic QS trait-defining edge; broad, cross-taxa. |
| AgrB — cleaves C-terminal tail of — AgrD | “AgrB cleaves the C-terminal tail” | 10.1128/jb.00195-24 / https://doi.org/10.1128/jb.00195-24 (2024) | (fang2024determinantsofmaturation pages 1-2) | Gram-positive S. aureus Agr-specific. |
| AgrB — promotes formation of — AIP thiolactone ring | “AgrB uses active site residues H77 and C84 to cleave the C-terminal tail and to promote thiolactone ring formation, which is essential for signaling” | 10.1128/jb.00195-24 / https://doi.org/10.1128/jb.00195-24 (2024) | (fang2024determinantsofmaturation pages 1-2) | Gram-positive Agr maturation; strong mechanistic support. |
| MroQ — cleaves/removes — AgrD N-terminal Leader | “MroQ cleaves the N-terminal Leader” | 10.1128/jb.00195-24 / https://doi.org/10.1128/jb.00195-24 (2024) | (fang2024determinantsofmaturation pages 1-2) | Gram-positive Agr maturation; strong mechanistic support. |
| AgrB and MroQ — are sufficient for maturation of — AIP | “AgrB and MroQ are sufficient for AIP maturation in vitro” | 10.1128/jb.00195-24 / https://doi.org/10.1128/jb.00195-24 (2024) | (fang2024determinantsofmaturation pages 1-2) | In vitro sufficiency; curate with assay qualifier. |
| AIP — activates — AgrC histidine kinase | “AgrC, a transmembrane histidine phosphokinase that AIP activates” | 10.1128/jb.00195-24 / https://doi.org/10.1128/jb.00195-24 (2024) | (fang2024determinantsofmaturation pages 1-2) | Gram-positive Agr signaling; direct receptor edge. |
| AIP binding to AgrC — causes — AgrC autophosphorylation | “AIP binding to AgrC causes AgrC autophosphorylation” | 10.3390/synbio1020010 / https://doi.org/10.3390/synbio1020010 (2024) | (li2024anengineeredescherichia pages 17-20) | Agr cascade; model/review synthesis rather than primary biochemical paper. |
| Phosphorylated AgrA — activates transcription of — agrBDCA and RNAIII (P2/P3) | “phosphorylated AgrA activates agrBDCA, RNAIII and promoters P2/P3” | 10.3390/synbio1020010 / https://doi.org/10.3390/synbio1020010 (2024) | (li2024anengineeredescherichia pages 17-20) | Agr-specific regulatory output; taxon-specific. |
| DSF (cis-11-methyl-2-dodecenoic acid) — triggers — autophosphorylation | “DSF (cis-11-methyl-2-dodecenoic acid) triggering autophosphorylation” | 10.3390/bacteria3030008 / https://doi.org/10.3390/bacteria3030008 (2024) | (erkihun2024medicalscopeof pages 6-8) | Biofilm dispersion pathway; species context not always uniform, moderate generality. |
| Autophosphorylation — activates — c-di-GMP phosphodiesterase | “autophosphorylation that activates a c-di-GMP phosphodiesterase” | 10.3390/bacteria3030008 / https://doi.org/10.3390/bacteria3030008 (2024) | (erkihun2024medicalscopeof pages 6-8) | Dispersion mechanism; may be species/pathway-specific. |
| c-di-GMP phosphodiesterase activity — decreases — c-di-GMP | “leading to c-di-GMP degradation” | 10.3390/bacteria3030008 / https://doi.org/10.3390/bacteria3030008 (2024) | (erkihun2024medicalscopeof pages 6-8) | Second-messenger edge supporting dispersal branch. |
| c-di-GMP degradation — promotes — planktonic cell release/biofilm dispersion | “c-di-GMP degradation and release/dispersion of planktonic cells” | 10.3390/bacteria3030008 / https://doi.org/10.3390/bacteria3030008 (2024) | (erkihun2024medicalscopeof pages 6-8) | Downstream phenotype; dispersion, not core QS definition. |
| Quorum-quenching enzymes — inactivate — QS signals | “QQ enzymes that inactivate QS signals” | 10.3390/ijms25052655 / https://doi.org/10.3390/ijms25052655 (2024) | (juszczukkubiak2024molecularaspectsof pages 2-3) | Intervention edge; useful for inhibitory branch. |
| QS inhibitors (QSIs) — inhibit/disrupt — signal receptors / QS pathways | “QS inhibitors (QSIs) that chemically disrupt QS via inhibition of signal receptors” | 10.3390/ijms25052655 / https://doi.org/10.3390/ijms25052655 (2024) | (juszczukkubiak2024molecularaspectsof pages 2-3) | Intervention edge; broad class, mechanism can vary. |
| Δagr — increases — ROS accumulation | “ROS levels increased with agr deficiency” | 10.7554/eLife.89098 / https://doi.org/10.7554/eLife.89098 (2024) | (podkowik2024quorumsensingagrsystem pages 10-12) | S. aureus-specific oxidative-stress branch. |
| Increased endogenous ROS in Δagr — explains — elevated H2O2 lethality/susceptibility | “This explains the elevated lethality of peroxide in the absence of agr” | 10.7554/eLife.89098 / https://doi.org/10.7554/eLife.89098 (2024) | (podkowik2024quorumsensingagrsystem pages 10-12) | Strong phenotype edge; S. aureus-specific. |
| Wild-type agr-mediated survival during H2O2 exposure — requires — sodA | “wild-type agr-mediated survival during H2O2 exposure depends on sodA” | 10.7554/eLife.89098 / https://doi.org/10.7554/eLife.89098 (2024) | (podkowik2024quorumsensingagrsystem pages 1-2) | S. aureus-specific; oxidative-defense effector branch. |
| Menadione pretreatment — protects — Δagr from H2O2 killing | “pretreatment with menadione… ‘protected the Δagr mutant’” | 10.7554/eLife.89098 / https://doi.org/10.7554/eLife.89098 (2024) | (podkowik2024quorumsensingagrsystem pages 10-12) | Experimental/pharmacologic edge; assay-specific, not a native QS mechanism. |


*Table: This table lists candidate subject–predicate–object edges for a quorum sensing TraitMech graph, with short evidence snippets, DOI-first references, and curation qualifiers. It emphasizes core LuxI/LuxR and Agr mechanisms while also capturing dispersion, quorum quenching, and a recent agr–oxidative stress branch.*

### Visual evidence (quorum quenching targeting points)
A schematic from a 2024 Pharmaceutics review summarizes major intervention points in QS pathways (suppress synthesis; degrade signals; disrupt transport; competitively block receptor binding), consistent with the QQ/QSI categories in recent reviews. (rajkhowa2024advancingantibioticresistantmicrobe media 2c684be5)

### Expert synthesis and curation notes (authoritative interpretations)
1) **QS is best curated as a regulatory capability**, with downstream phenotypes represented as QS-controlled outputs rather than definitional components. This is consistent across recent reviews defining QS as threshold-dependent signal production/detection driving gene-expression regulation. (juszczukkubiak2024molecularaspectsof pages 2-3, sedarat2024quorumsensingin pages 1-3)
2) **Mechanistic heterogeneity matters**: QS is not one pathway; distinct signal chemistries (AHL, AIP, AI‑2) and sensor architectures (intracellular regulators vs two-component systems/phosphorelays) mean edges must be **taxon- and system-scoped** (e.g., LuxI/LuxR vs Agr vs LuxP/LuxQ→LuxU→LuxO). (rajkhowa2024advancingantibioticresistantmicrobe pages 4-5, fang2024determinantsofmaturation pages 1-2)
3) **Curation opportunity**: the 2024 AgrD maturation paper provides strong, enzyme-level causal edges (AgrB, MroQ, thiolactone requirement) appropriate for high-confidence nodes/edges in TraitMech. (fang2024determinantsofmaturation pages 1-2)
4) **Curation caution**: some quantitative claims in reviews (e.g., fold-changes of resistance in biofilms) may be secondary citations; if TraitMech requires primary evidence, curate them as “review-supported” or seek primary sources. (li2024anengineeredescherichia pages 9-13)

### Warnings (claims not yet ready for strong curation)
* **Generalizing DSF → c-di-GMP dispersion** across taxa may be overbroad; the mechanism is described in a systematic review but may be species- or pathway-specific. Curate with qualifiers (taxon/pathway uncertain) unless supported by primary DSF literature. (erkihun2024medicalscopeof pages 6-8)
* **AI‑2 as a ‘universal’ interspecies signal** is frequently asserted; however, receptor and uptake mechanisms differ widely. Curate AI‑2 edges at the level of known modules (LuxS; LuxP/LuxQ; Lsr where applicable) rather than as a universal, single mechanism. (rajkhowa2024advancingantibioticresistantmicrobe pages 4-5, lawther2024—invitedreview pages 1-2)
* **Therapeutic efficacy claims** for QS inhibitors (QSIs) and nanocarriers may be context-dependent; curate as intervention nodes/edges (mechanism-of-action) rather than clinical effectiveness unless supported by controlled clinical data (not retrieved here). (rajkhowa2024advancingantibioticresistantmicrobe pages 4-5, juszczukkubiak2024molecularaspectsof pages 2-3)

---

## DOI-first bibliography (with URLs and publication dates where available)

1. **Fang L, Cosgriff C, Alonzo F.** Determinants of maturation of the *Staphylococcus aureus* autoinducing peptide. *Journal of Bacteriology*. Published **23 Aug 2024** (issue Sep 2024). DOI: **10.1128/jb.00195-24**. URL: https://doi.org/10.1128/jb.00195-24 (fang2024determinantsofmaturation pages 1-2)

2. **Podkowik M, et al.** Quorum-sensing agr system of *Staphylococcus aureus* primes gene expression for protection from lethal oxidative stress. *eLife*. Version of record **30 Apr 2024**. DOI: **10.7554/eLife.89098**. URL: https://doi.org/10.7554/eLife.89098 (podkowik2024quorumsensingagrsystem pages 1-2, podkowik2024quorumsensingagrsystem pages 10-12)

3. **Rimi SS, et al.** Biofilm formation, agr typing and antibiotic resistance pattern in methicillin-resistant *Staphylococcus aureus* isolated from hospital environments. *PLOS ONE*. **5 Aug 2024**. DOI: **10.1371/journal.pone.0308282**. URL: https://doi.org/10.1371/journal.pone.0308282 (rimi2024biofilmformationagr pages 1-2)

4. **Juszczuk-Kubiak E.** Molecular Aspects of the Functioning of Pathogenic Bacteria Biofilm Based on Quorum Sensing (QS) Signal-Response System and Innovative Non-Antibiotic Strategies for Their Elimination. *International Journal of Molecular Sciences*. **Feb 2024**. DOI: **10.3390/ijms25052655**. URL: https://doi.org/10.3390/ijms25052655 (juszczukkubiak2024molecularaspectsof pages 2-3)

5. **Rajkhowa S, et al.** Advancing Antibiotic-Resistant Microbe Combat: Nanocarrier-Based Systems in Combination Therapy Targeting Quorum Sensing. *Pharmaceutics*. **Sep 2024**. DOI: **10.3390/pharmaceutics16091160**. URL: https://doi.org/10.3390/pharmaceutics16091160 (rajkhowa2024advancingantibioticresistantmicrobe pages 4-5, rajkhowa2024advancingantibioticresistantmicrobe media 2c684be5)

6. **Hetta HF, et al.** Quorum Sensing Inhibitors: An Alternative Strategy to Win the Battle against Multidrug-Resistant (MDR) Bacteria. *Molecules*. **Jul 2024**. DOI: **10.3390/molecules29153466**. URL: https://doi.org/10.3390/molecules29153466 (hetta2024quorumsensinginhibitors pages 2-4, hetta2024quorumsensinginhibitors pages 4-6)

7. **Erkihun M, et al.** Medical Scope of Biofilm and Quorum Sensing during Biofilm Formation: Systematic Review. *Bacteria*. **Jun 2024**. DOI: **10.3390/bacteria3030008**. URL: https://doi.org/10.3390/bacteria3030008 (erkihun2024medicalscopeof pages 6-8)

8. **Sedarat Z, Taylor-Robinson AW.** Quorum Sensing in Biofilm. In: *Recent Advances in Bacterial Biofilm Studies - Formation, Regulation, and Eradication in Human Infections*. **Feb 2024**. DOI: **10.5772/intechopen.113338**. URL: https://doi.org/10.5772/intechopen.113338 (sedarat2024quorumsensingin pages 1-3)

9. **Lawther K, et al.** Chemical signalling within the rumen microbiome (Invited Review). *Animal Bioscience*. **Feb 2024**. DOI: **10.5713/ab.23.0374**. URL: https://doi.org/10.5713/ab.23.0374 (lawther2024—invitedreview pages 1-2)

10. **Li Y, et al.** An Engineered *Escherichia coli* Community for Studying Quorum Sensing. *SynBio*. **Jul 2024**. DOI: **10.3390/synbio1020010**. URL: https://doi.org/10.3390/synbio1020010 (li2024anengineeredescherichia pages 9-13)

11. **Zhu X, et al.** Innovative microbial disease biocontrol strategies mediated by quorum quenching and their multifaceted applications: A review. *Frontiers in Plant Science*. **12 Jan 2023**. DOI: **10.3389/fpls.2022.1063393**. URL: https://doi.org/10.3389/fpls.2022.1063393 (zhu2023innovativemicrobialdisease pages 1-2)


References

1. (sedarat2024quorumsensingin pages 1-3): Zahra Sedarat and Andrew W. Taylor-Robinson. Quorum sensing in biofilm. Recent Advances in Bacterial Biofilm Studies - Formation, Regulation, and Eradication in Human Infections, Feb 2024. URL: https://doi.org/10.5772/intechopen.113338, doi:10.5772/intechopen.113338. This article has 5 citations.

2. (juszczukkubiak2024molecularaspectsof pages 2-3): Edyta Juszczuk-Kubiak. Molecular aspects of the functioning of pathogenic bacteria biofilm based on quorum sensing (qs) signal-response system and innovative non-antibiotic strategies for their elimination. International Journal of Molecular Sciences, 25:2655, Feb 2024. URL: https://doi.org/10.3390/ijms25052655, doi:10.3390/ijms25052655. This article has 139 citations.

3. (li2024anengineeredescherichia pages 9-13): Yuwei Li, Justin E. Clarke, Alex J. O’Neill, Francisco M. Goycoolea, and James Smith. An engineered escherichia coli community for studying quorum sensing. SynBio, 1:144-157, Jul 2024. URL: https://doi.org/10.3390/synbio1020010, doi:10.3390/synbio1020010. This article has 2 citations.

4. (fang2024determinantsofmaturation pages 1-2): Liwei Fang, Chance Cosgriff, and Francis Alonzo. Determinants of maturation of the <i>staphylococcus aureus</i> autoinducing peptide. Journal of Bacteriology, Sep 2024. URL: https://doi.org/10.1128/jb.00195-24, doi:10.1128/jb.00195-24. This article has 7 citations and is from a peer-reviewed journal.

5. (rajkhowa2024advancingantibioticresistantmicrobe pages 4-5): Sanchaita Rajkhowa, Safrina Zeenat Hussain, Manisha Agarwal, Alaiha Zaheen, Sami A. Al-Hussain, and Magdi E. A. Zaki. Advancing antibiotic-resistant microbe combat: nanocarrier-based systems in combination therapy targeting quorum sensing. Pharmaceutics, 16:1160, Sep 2024. URL: https://doi.org/10.3390/pharmaceutics16091160, doi:10.3390/pharmaceutics16091160. This article has 32 citations.

6. (erkihun2024medicalscopeof pages 6-8): Mulat Erkihun, Zelalem Asmare, Kirubel Endalamew, Birhanu Getie, Teklehayimanot Kiros, and Ayenew Berhan. Medical scope of biofilm and quorum sensing during biofilm formation: systematic review. Bacteria, 3:118-135, Jun 2024. URL: https://doi.org/10.3390/bacteria3030008, doi:10.3390/bacteria3030008. This article has 54 citations.

7. (podkowik2024quorumsensingagrsystem pages 10-12): Magdalena Podkowik, Andrew I Perault, Gregory Putzel, Andrew Pountain, Jisun Kim, Ashley L DuMont, Erin E Zwack, Robert J Ulrich, Theodora K Karagounis, Chunyi Zhou, Andreas F Haag, Julia Shenderovich, Gregory A Wasserman, Junbeom Kwon, John Chen, Anthony R Richardson, Jeffrey N Weiser, Carla R Nowosad, Desmond S Lun, Dane Parker, Alejandro Pironti, Xilin Zhao, Karl Drlica, Itai Yanai, Victor J Torres, and Bo Shopsin. Quorum-sensing agr system of staphylococcus aureus primes gene expression for protection from lethal oxidative stress. eLife, Apr 2024. URL: https://doi.org/10.7554/elife.89098, doi:10.7554/elife.89098. This article has 45 citations and is from a domain leading peer-reviewed journal.

8. (podkowik2024quorumsensingagrsystem pages 1-2): Magdalena Podkowik, Andrew I Perault, Gregory Putzel, Andrew Pountain, Jisun Kim, Ashley L DuMont, Erin E Zwack, Robert J Ulrich, Theodora K Karagounis, Chunyi Zhou, Andreas F Haag, Julia Shenderovich, Gregory A Wasserman, Junbeom Kwon, John Chen, Anthony R Richardson, Jeffrey N Weiser, Carla R Nowosad, Desmond S Lun, Dane Parker, Alejandro Pironti, Xilin Zhao, Karl Drlica, Itai Yanai, Victor J Torres, and Bo Shopsin. Quorum-sensing agr system of staphylococcus aureus primes gene expression for protection from lethal oxidative stress. eLife, Apr 2024. URL: https://doi.org/10.7554/elife.89098, doi:10.7554/elife.89098. This article has 45 citations and is from a domain leading peer-reviewed journal.

9. (zhu2023innovativemicrobialdisease pages 1-2): Xixian Zhu, Wen-Juan Chen, Kalpana Bhatt, Zhe Zhou, Yaohua Huang, Lian-Hui Zhang, Shaohua Chen, and Junxia Wang. Innovative microbial disease biocontrol strategies mediated by quorum quenching and their multifaceted applications: a review. Frontiers in Plant Science, Jan 2023. URL: https://doi.org/10.3389/fpls.2022.1063393, doi:10.3389/fpls.2022.1063393. This article has 89 citations.

10. (li2024anengineeredescherichia pages 1-5): Yuwei Li, Justin E. Clarke, Alex J. O’Neill, Francisco M. Goycoolea, and James Smith. An engineered escherichia coli community for studying quorum sensing. SynBio, 1:144-157, Jul 2024. URL: https://doi.org/10.3390/synbio1020010, doi:10.3390/synbio1020010. This article has 2 citations.

11. (li2024anengineeredescherichia pages 23-26): Yuwei Li, Justin E. Clarke, Alex J. O’Neill, Francisco M. Goycoolea, and James Smith. An engineered escherichia coli community for studying quorum sensing. SynBio, 1:144-157, Jul 2024. URL: https://doi.org/10.3390/synbio1020010, doi:10.3390/synbio1020010. This article has 2 citations.

12. (rimi2024biofilmformationagr pages 1-2): Sabrina Sultana Rimi, Md. Nahid Ashraf, Sanzila Hossain Sigma, Md. Tanjir Ahammed, Mahbubul Pratik Siddique, Mohammad Ali Zinnah, Md. Tanvir Rahman, and Md. Shafiqul Islam. Biofilm formation, agr typing and antibiotic resistance pattern in methicillin-resistant staphylococcus aureus isolated from hospital environments. PLOS ONE, 19:e0308282, Aug 2024. URL: https://doi.org/10.1371/journal.pone.0308282, doi:10.1371/journal.pone.0308282. This article has 32 citations and is from a peer-reviewed journal.

13. (hetta2024quorumsensinginhibitors pages 4-6): Helal F. Hetta, Yasmin N. Ramadan, Zainab I. Rashed, Ahmad A. Alharbi, Shomokh Alsharef, Tala T. Alkindy, Alanoud Alkhamali, Abdullah S. Albalawi, Basem Battah, and Matthew G. Donadu. Quorum sensing inhibitors: an alternative strategy to win the battle against multidrug-resistant (mdr) bacteria. Molecules, 29:3466, Jul 2024. URL: https://doi.org/10.3390/molecules29153466, doi:10.3390/molecules29153466. This article has 100 citations.

14. (lawther2024—invitedreview pages 1-2): Katie Lawther, Fernanda Godoy Santos, Linda B Oyama, and Sharon A Huws. — invited review — chemical signalling within the rumen microbiome. Animal Bioscience, 37:337-345, Feb 2024. URL: https://doi.org/10.5713/ab.23.0374, doi:10.5713/ab.23.0374. This article has 11 citations and is from a peer-reviewed journal.

15. (li2024anengineeredescherichia pages 17-20): Yuwei Li, Justin E. Clarke, Alex J. O’Neill, Francisco M. Goycoolea, and James Smith. An engineered escherichia coli community for studying quorum sensing. SynBio, 1:144-157, Jul 2024. URL: https://doi.org/10.3390/synbio1020010, doi:10.3390/synbio1020010. This article has 2 citations.

16. (kuai2024roleofsara pages 6-9): Yi He Kuai, Jodi Woan-Fei Law, Yong Sze Ong, Vengadesh Letchumanan, Learn-Han Lee, and Loh Teng-Hern Tan. Role of sara in staphylococcus aureus: a virulence target for therapeutic strategies. Progress In Microbes &amp; Molecular Biology, Jun 2024. URL: https://doi.org/10.36877/pmmb.a0000444, doi:10.36877/pmmb.a0000444. This article has 16 citations.

17. (madarova2024noveltherapeutictargeting pages 18-21): A Maďarová. Novel therapeutic targeting of the quorum sensing transcriptional regulation in multi-antibiotic resistant bacterium staphylococcus aureus. Unknown journal, 2024.

18. (simpson2024quorumsensingin pages 25-26): Chelsea A. Simpson, Zach R. Celentano, Nicholas W. Haas, James B. McKinlay, Carey D. Nadell, and Julia C. van Kessel. Quorum sensing in vibrio controls carbon metabolism to optimize growth in changing environmental conditions. Nov 2024. URL: https://doi.org/10.1371/journal.pbio.3002891, doi:10.1371/journal.pbio.3002891. This article has 4 citations and is from a highest quality peer-reviewed journal.

19. (podkowik2024quorumsensingagrsystem pages 12-14): Magdalena Podkowik, Andrew I Perault, Gregory Putzel, Andrew Pountain, Jisun Kim, Ashley L DuMont, Erin E Zwack, Robert J Ulrich, Theodora K Karagounis, Chunyi Zhou, Andreas F Haag, Julia Shenderovich, Gregory A Wasserman, Junbeom Kwon, John Chen, Anthony R Richardson, Jeffrey N Weiser, Carla R Nowosad, Desmond S Lun, Dane Parker, Alejandro Pironti, Xilin Zhao, Karl Drlica, Itai Yanai, Victor J Torres, and Bo Shopsin. Quorum-sensing agr system of staphylococcus aureus primes gene expression for protection from lethal oxidative stress. eLife, Apr 2024. URL: https://doi.org/10.7554/elife.89098, doi:10.7554/elife.89098. This article has 45 citations and is from a domain leading peer-reviewed journal.

20. (rajkhowa2024advancingantibioticresistantmicrobe media 2c684be5): Sanchaita Rajkhowa, Safrina Zeenat Hussain, Manisha Agarwal, Alaiha Zaheen, Sami A. Al-Hussain, and Magdi E. A. Zaki. Advancing antibiotic-resistant microbe combat: nanocarrier-based systems in combination therapy targeting quorum sensing. Pharmaceutics, 16:1160, Sep 2024. URL: https://doi.org/10.3390/pharmaceutics16091160, doi:10.3390/pharmaceutics16091160. This article has 32 citations.

21. (hetta2024quorumsensinginhibitors pages 2-4): Helal F. Hetta, Yasmin N. Ramadan, Zainab I. Rashed, Ahmad A. Alharbi, Shomokh Alsharef, Tala T. Alkindy, Alanoud Alkhamali, Abdullah S. Albalawi, Basem Battah, and Matthew G. Donadu. Quorum sensing inhibitors: an alternative strategy to win the battle against multidrug-resistant (mdr) bacteria. Molecules, 29:3466, Jul 2024. URL: https://doi.org/10.3390/molecules29153466, doi:10.3390/molecules29153466. This article has 100 citations.