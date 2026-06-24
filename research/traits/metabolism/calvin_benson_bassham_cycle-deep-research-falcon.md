---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T04:12:06.468812'
end_time: '2026-06-18T04:31:12.657055'
duration_seconds: 1146.19
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: Calvin-Benson-Bassham cycle
  trait_identifier: traitmech:000020
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: calvin_benson_bassham_cycle
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An autotrophic carbon-fixation pathway (the reductive pentose phosphate
    cycle) that fixes CO2 using ribulose-1,5-bisphosphate carboxylase/oxygenase (RuBisCO).
    It is the most widespread CO2-fixation pathway, used by plants, algae, cyanobacteria,
    and many proteobacteria.
  parent_traits: traitmech:000019
  synonyms: Calvin cycle, reductive pentose phosphate cycle
  evidence_summary: "DOI:10.1128/AEM.02473-10:  (Berg review identifies the Calvin-Benson-Bassham\
    \ (reductive pentose phosphate) cycle as the reference autotrophic pathway against\
    \ which the other five are distinguished.) | DOI:10.1146/annurev-marine-120709-142712:\
    \  (H\xFCgler & Sievert support the Calvin cycle as the most common/widespread\
    \ CO2-fixation pathway, including among marine cyanobacteria and proteobacteria.)"
  causal_graph_summary: 'cbb_rubisco_co2_fixation: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 50
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Calvin-Benson-Bassham cycle
- **METPO identifier:** traitmech:000020
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway (the reductive pentose phosphate cycle) that fixes CO2 using ribulose-1,5-bisphosphate carboxylase/oxygenase (RuBisCO). It is the most widespread CO2-fixation pathway, used by plants, algae, cyanobacteria, and many proteobacteria.
- **Parent traits:** traitmech:000019
- **Synonyms:** Calvin cycle, reductive pentose phosphate cycle
- **Existing evidence:** DOI:10.1128/AEM.02473-10:  (Berg review identifies the Calvin-Benson-Bassham (reductive pentose phosphate) cycle as the reference autotrophic pathway against which the other five are distinguished.) | DOI:10.1146/annurev-marine-120709-142712:  (Hügler & Sievert support the Calvin cycle as the most common/widespread CO2-fixation pathway, including among marine cyanobacteria and proteobacteria.)
- **Existing causal graph summary:** cbb_rubisco_co2_fixation: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **Calvin-Benson-Bassham cycle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/calvin_benson_bassham_cycle.yaml`.

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
- **Trait label:** Calvin-Benson-Bassham cycle
- **METPO identifier:** traitmech:000020
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway (the reductive pentose phosphate cycle) that fixes CO2 using ribulose-1,5-bisphosphate carboxylase/oxygenase (RuBisCO). It is the most widespread CO2-fixation pathway, used by plants, algae, cyanobacteria, and many proteobacteria.
- **Parent traits:** traitmech:000019
- **Synonyms:** Calvin cycle, reductive pentose phosphate cycle
- **Existing evidence:** DOI:10.1128/AEM.02473-10:  (Berg review identifies the Calvin-Benson-Bassham (reductive pentose phosphate) cycle as the reference autotrophic pathway against which the other five are distinguished.) | DOI:10.1146/annurev-marine-120709-142712:  (Hügler & Sievert support the Calvin cycle as the most common/widespread CO2-fixation pathway, including among marine cyanobacteria and proteobacteria.)
- **Existing causal graph summary:** cbb_rubisco_co2_fixation: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **Calvin-Benson-Bassham cycle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/calvin_benson_bassham_cycle.yaml`.

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


## Microbial Trait Causal Graph Research Report: Calvin–Benson–Bassham (CBB) Cycle (METPO: traitmech:000020)

### 1) Key concepts, definitions, and current understanding

**Trait definition (curation scope).** The *Calvin–Benson–Bassham (CBB) cycle* is an autotrophic carbon-fixation pathway whose defining biochemical feature is RuBisCO-catalyzed carboxylation of ribulose-1,5-bisphosphate (RuBP) to produce 3-phosphoglycerate (3-PGA), followed by regeneration of RuBP (requiring phosphoribulokinase, PRK) to sustain net CO2 assimilation into biomass (kurkela2024inorganiccarbonsensing pages 2-3, lucius2024theprimarycarbon pages 1-2). In cyanobacteria, the first CBB reaction occurs in **carboxysomes** (protein microcompartments) that encapsulate RuBisCO and carbonic anhydrase (CA), while downstream CBB reactions proceed in the cytoplasm after export of 3-PGA from the carboxysome (kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 2-3).

**Trait vs. nearby traits / boundary cases.**
- *Distinguish from other CO2-fixation pathways:* Recent expert syntheses explicitly enumerate multiple natural autotrophic pathways (e.g., CBB, rTCA, Wood–Ljungdahl) and emphasize that each has distinct thermodynamic and ecological constraints; thus, “autotrophy” is not equivalent to the CBB cycle (bachleitner2023thepotentialof pages 2-3).
- *CBB without obligate autotrophy:* Many microbes are mixotrophic; the curation target is the **physiological capacity for net CO2 fixation via the CBB module**, not merely the presence of RuBisCO-related genes. For TraitMech, a conservative boundary is: (i) presence of RuBisCO + RuBP regeneration capacity (e.g., PRK), and (ii) evidence of CO2-dependent growth/physiology or CCM dependence under low inorganic carbon.
- *CCM coupling as common but not mandatory:* Many microbial CBB users require a **CO2-concentrating mechanism (CCM)** to support RuBisCO under low CO2, but CBB can exist with differing degrees of CCM investment. The “DIC toolkit” concept captures this coupling (transporters + CA + carboxysomes/complexes) and clarifies why CBB organisms often encode multiple dissolved inorganic carbon (DIC) handling components (scott2024widespreaddissolvedinorganic pages 2-4, scott2024widespreaddissolvedinorganic pages 1-2).

**Assay-observed properties that operationalize the trait.**
- **Growth phenotypes in low CO2 / ambient air** that depend on CCM components (e.g., CA, bicarbonate transport, NDH complexes) provide strong evidence of functional CBB-linked carbon acquisition (kurkela2024inorganiccarbonsensing pages 1-2, wieschollek2024anewtype pages 15-17).
- **RuBisCO activity assays** and RuBP consumption can operationalize flux through the first CBB reaction; assay choice and carbon source matter substantially (faisal2024rubiscoactivityassays pages 1-2, faisal2024rubiscoactivityassays pages 4-6).

### 2) Recent developments and latest research (prioritize 2023–2024)

#### 2.1. New mechanistic regulation within carboxysomes: RuBP allosterically activates α-carboxysome CA
Pulsford et al. (2024, *Science Advances*) report that **α-carboxysome carbonic anhydrase (CsoSCA)** from *Cyanobium* is **allosterically activated by RuBP**, the RuBisCO substrate, revealing a direct metabolite-to-CCM enzyme regulatory link at the interface of carbon uptake and fixation (pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2). The associated figures provide experimental and modeled evidence for a feedback loop in which RuBP tunes CA flux and influences RuBisCO carboxylation environment inside the carboxysome (pulsford2024cyanobacterialαcarboxysomecarbonic media 5f6b944e, pulsford2024cyanobacterialαcarboxysomecarbonic media d5ca422c).

#### 2.2. Discovery of iota-carbonic anhydrase (ιCA) functioning in bacterial carboxysomes (alkaliphilic chemolithoautotrophs)
Wieschollek et al. (2024, *Applied and Environmental Microbiology*) provide genetic and biochemical evidence that an **ιCA is the carboxysomal CA** in *Thiomicrospira* sulfur chemolithoautotrophs in alkaline environments (wieschollek2024anewtype pages 1-2). Key causal findings include: (i) ιCA gene interruption eliminates detectable carboxysomal CA activity while leaving RuBisCO activity similar to wild type, and (ii) the ιCA-interrupted strain is **CO2-sensitive**, being unable to grow under ambient air (low CO2) (wieschollek2024anewtype pages 5-8, wieschollek2024anewtype pages 15-17). The work also reports measurable carboxysome-associated CA activities (e.g., ~3.1 µmol CO2 s−1 mg−1 for *T. pelophila*) and differential inhibitor/redox sensitivity, supporting mechanistic diversity in CCM implementation (wieschollek2024anewtype pages 5-8, wieschollek2024anewtype pages 12-15).

#### 2.3. Integrative models of DIC supply-to-demand: the “DIC toolkit” framing
Scott et al. (2024, *Applied and Environmental Microbiology*) synthesize the concept that CBB users commonly deploy a **DIC toolkit** comprising DIC transporters, carbonic anhydrases, CO2-active multisubunit complexes, and carboxysomes to bridge environmental DIC chemistry/flux to RuBisCO’s CO2 demand (scott2024widespreaddissolvedinorganic pages 2-4, scott2024widespreaddissolvedinorganic pages 1-2). They highlight spatial segregation as a mechanistic necessity: **non-vectoral cytosolic CA can dissipate CCM function by promoting CO2 leakage**, motivating regulatory/spatial solutions (scott2024widespreaddissolvedinorganic pages 2-4, scott2024widespreaddissolvedinorganic pages 10-13).

#### 2.4. Cyanobacterial Ci sensing and regulation continues to mature as a mechanistic layer atop CBB
Kurkela & Tyystjärvi (2024, *Physiologia Plantarum*) detail cyanobacterial CCM control involving bicarbonate transporters (SbtA, BicA, BCT1), specialized NDH-1 complexes (NDH-13/14), transcription factors (CcmR/NdhR, CyAbrB2, CmpR, RbcR), and metabolite signals (e.g., 2-phosphoglycolate, RuBP) that indicate low inorganic carbon status and tune transporter/carboxysome gene expression (kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 8-8). Their synthesis includes a strong genetic systems statement: simultaneous inactivation of multiple bicarbonate transporters and NDH complexes can prevent growth in ambient air while still allowing growth at high CO2 (kurkela2024inorganiccarbonsensing pages 1-2).

### 3) Current applications and real-world implementations

#### 3.1. CO2-to-protein production using *Cupriavidus necator* CBB-linked regulatory parts
Arhar et al. (2024, *Microbial Cell Factories*) demonstrate a real implementation of **CO2-based bioproduction** in the chemolithoautotroph *Cupriavidus necator* (formerly *Ralstonia eutropha*). They use native promoters “governing the CBB cycle” to drive heterologous enzyme (phytase, AppA) expression under autotrophic gas fermentation, reporting up to **22 U/mL** phytase activity and achieving **~8 g CDW/L** (theoretical maximum based on nitrogen input) in a 1 L fed-batch gas fermentation (arhar2024co2basedproductionof pages 1-2, arhar2024co2basedproductionof pages 7-9). They also report an approximate CO2 capture/assimilation rate (e.g., 146 mg L−1 h−1) and estimate CO2 assimilation mass in lab-scale fermentation (arhar2024co2basedproductionof pages 9-10).

#### 3.2. Expert perspective on where CBB fits among CO2-to-products routes
Bachleitner et al. (2023, *Nature Communications*) provide an authoritative comparative analysis of C1 bioprocesses. They emphasize that while some alternative CO2-fixation pathways require less ATP/reducing power, the CBB cycle can function “at very low CO2 concentrations,” aligning with the ecological success of CBB-linked CCMs (bachleitner2023thepotentialof pages 3-4). They also highlight system-level constraints for CO2-based biomanufacturing: energy needs for feedstock generation and scale-up, e.g., an estimate of **~3.40 MWh per tonne of formate** for electrochemical CO2→formate, and the challenge that large-scale fuel replacement could require substantial fractions of global electricity (bachleitner2023thepotentialof pages 3-4, bachleitner2023thepotentialof pages 4-5).

### 4) Expert opinions and analysis (authoritative sources)

**CBB is frequently paired with CCM/DIC toolkits because RuBisCO is CO2-specific and DIC speciation is pH-dependent.** Scott et al. argue that the toolkit evolved to match environmental supply (CO2/HCO3− pools, diffusion) to biochemical demand by CO2-specific carboxylases (including RuBisCO) and that uncatalyzed CO2↔HCO3− interconversion is too slow for metabolic needs, motivating transporters and CA deployment (scott2024widespreaddissolvedinorganic pages 1-2, scott2024widespreaddissolvedinorganic pages 2-4).

**Regulatory complexity is expected because CBB intermediates overlap with catabolic sugar pathways.** Lucius & Hagemann highlight that anabolic CO2 fixation and catabolic sugar-degradation share intermediates, requiring tight regulatory networks; they describe CP12 as a small protein that downregulates the CBB cycle in darkness via inhibition of PRK and GAPDH (lucius2024theprimarycarbon pages 1-2).

**CBB gene regulation is frequently under LysR-type control (CbbR).** Dangel & Tabita review CbbR as a “master regulator” of microbial CO2 fixation, including effector metabolite interactions and operon-level control (dangel2015cbbrthemaster pages 1-5). Direct mechanistic evidence from *Xanthobacter flavus* shows cbb operon transcription depends on CbbR and that NADPH increases CbbR DNA-binding affinity, linking intracellular redox/energy state to CBB gene expression (keulen2003analysisofdna pages 2-3, keulen2003analysisofdna pages 1-2).

### 5) Relevant statistics and quantitative data (recent studies)

**Carboxysome-associated CA activity (new ιCA system).** *Thiomicrospira pelophila* carboxysome preparations show CA activity on the order of **~3.1 µmol CO2 s−1 mg−1**, and disruption of ιCA eliminates detectable carboxysomal CA activity while retaining similar RuBisCO activity, consistent with a specific CA defect (wieschollek2024anewtype pages 5-8).

**Low-CO2 growth dependence.** The *T. pelophila* ιCA-135 mutant is “unable to grow under ambient air” (≈0.04% CO2), linking carboxysomal CA to growth in low CO2 environments (wieschollek2024anewtype pages 15-17, wieschollek2024anewtype pages 17-19).

**RuBisCO assay quantitative differences (CO2 vs bicarbonate supply).** Faisal et al. (2024) report RuBP consumption rates **5–7× higher** under 5% CO2 than with 20 mM NaHCO3 and a maximum measured activity of **2.13 nmol NAD+/µg Chl-a/min** in their simplified spectrophotometric assay (faisal2024rubiscoactivityassays pages 1-2). They also report an example RuBP consumption comparison (0.0159 mmol/min under 5% CO2 vs 0.0038 mmol/min with bicarbonate) and interpret the bicarbonate condition as limited by HCO3−→CO2 conversion (requiring CA) (faisal2024rubiscoactivityassays pages 4-6).

**Autotrophic CO2-to-protein bioprocess metrics.** In *C. necator* gas fermentation, Arhar et al. report up to **22.3 ± 2.4 U/mL** phytase activity and a CO2 capture rate of **146 mg L−1 h−1** (and related CO2 assimilation estimates) in lab-scale fermentation, demonstrating real-world use of CBB-linked regulation to drive protein production from CO2 (arhar2024co2basedproductionof pages 7-9, arhar2024co2basedproductionof pages 9-10).

---

## Trait scope summary (curation-oriented)

**What the trait represents.** A microbial physiological capacity for **net autotrophic CO2 assimilation** mediated by the CBB cycle (RuBisCO carboxylation + RuBP regeneration), often integrated with CCM/DIC-handling modules to ensure CO2 supply at RuBisCO.

**Key boundary cases.**
- *RuBisCO present but CBB incomplete:* RuBisCO genes without PRK/RuBP regeneration or without demonstrated net CO2 fixation are insufficient for trait assertion.
- *CCM-only traits:* CCM genes are supportive but should not substitute for evidence of CBB cycle capacity.
- *Assay context:* In vitro RuBisCO assays and gene presence can mislead if CCM architecture is disrupted (e.g., lysate CA limitation), so trait curation should prefer in vivo growth/flux evidence when possible (faisal2024rubiscoactivityassays pages 1-2).

---

## Candidate nodes (grouped by type; with ontology grounding where available)

### Pathways / modules
- Calvin–Benson–Bassham cycle (METPO:traitmech:000020)
- CO2-concentrating mechanism (CCM) (label-only candidate; closely tied to carboxysomes/transporters in cyanobacteria)
- Dissolved inorganic carbon (DIC) toolkit (label-only candidate concept) (scott2024widespreaddissolvedinorganic pages 2-4)

### Molecular functions / processes
- Carbon fixation / RuBisCO carboxylation (GO:0015977 carbon fixation; RuBisCO: GO:0016984) (kurkela2024inorganiccarbonsensing pages 2-3)
- Bicarbonate transport (GO:0015701) (kurkela2024inorganiccarbonsensing pages 2-3)

### Cellular structures
- Carboxysome (GO:0036464) (kurkela2024inorganiccarbonsensing pages 1-2)

### Genes / proteins / complexes (label-only grounding unless noted)
- RuBisCO (EC:4.1.1.39) (kurkela2024inorganiccarbonsensing pages 2-3)
- Carboxysomal carbonic anhydrase (CA; EC:4.2.1.1), including CsoSCA and ιCA (pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2, wieschollek2024anewtype pages 1-2)
- PRK (phosphoribulokinase; EC:2.7.1.19) (lucius2024theprimarycarbon pages 1-2)
- GAPDH (EC:1.2.1.12) (lucius2024theprimarycarbon pages 1-2)
- CP12 regulator protein (label-only) (lucius2024theprimarycarbon pages 1-2)
- BicA, SbtA (Na+/HCO3− symporters), BCT1/Cmp (ABC HCO3− pump) (kurkela2024inorganiccarbonsensing pages 2-3)
- NDH-13/CupA and NDH-14/CupB complexes (CO2→HCO3− conversion) (kurkela2024inorganiccarbonsensing pages 2-3)
- CbbR (LysR-type transcriptional regulator), RbcR, CcmR/NdhR, CyAbrB2, CmpR (keulen2003analysisofdna pages 2-3, kurkela2024inorganiccarbonsensing pages 6-7, kurkela2024inorganiccarbonsensing pages 6-6, kurkela2024inorganiccarbonsensing pages 8-8)

### Chemicals / metabolites
- CO2 (CHEBI:16526), HCO3− (CHEBI:17544) (scott2024widespreaddissolvedinorganic pages 1-2)
- RuBP (CHEBI:16710), 3-PGA (CHEBI:11881) (kurkela2024inorganiccarbonsensing pages 2-3)
- NADPH (CHEBI:16474) (keulen2003analysisofdna pages 1-2)
- 2-phosphoglycolate / 2-PG (CHEBI:17741) (kurkela2024inorganiccarbonsensing pages 8-8)

### Environmental / experimental factors
- Low inorganic carbon / ambient air (~0.04% CO2) vs high CO2 conditions (wieschollek2024anewtype pages 15-17, kurkela2024inorganiccarbonsensing pages 1-2)
- Alkaline pH (affecting HCO3− vs CO2 prevalence; transporter phenotypes) (kurkela2024inorganiccarbonsensing pages 2-3, scott2024widespreaddissolvedinorganic pages 7-10)
- Na+ requirement for BicA/SbtA function (≥1 mM Na+) (kurkela2024inorganiccarbonsensing pages 2-3)

---

## Candidate causal edges (evidence-backed)

The following artifact consolidates evidence-backed subject–predicate–object triples with curation notes.

| Subject node (suggested CURIE) | Predicate | Object node (suggested CURIE) | Evidence snippet | Source | DOI + URL | Notes |
|---|---|---|---|---|---|---|
| RuBisCO / ribulose-bisphosphate carboxylase oxygenase (EC:4.1.1.39; GO:0016984) | converts | RuBP (CHEBI:16710) + CO2 (CHEBI:16526) -> 3-phospho-D-glycerate / 3-PGA (CHEBI:11881) | “RubisCo… catalyses the first CBB reaction (RuBP + CO2 -> 3-PGA)” (kurkela2024inorganiccarbonsensing pages 2-3) | Kurkela 2024, *Physiologia Plantarum* | 10.1111/ppl.14140 https://doi.org/10.1111/ppl.14140 | Core defining edge for the CBB cycle in cyanobacteria; strong. |
| carboxysome (GO:0036464) | contains | RuBisCO (EC:4.1.1.39) | “carboxysomes that encapsulate RuBisCo and carbonic anhydrase” (kurkela2024inorganiccarbonsensing pages 1-2) | Kurkela 2024, *Physiologia Plantarum* | 10.1111/ppl.14140 https://doi.org/10.1111/ppl.14140 | Strong for cyanobacterial CCM-linked CBB. |
| carboxysomal carbonic anhydrase / CsoSCA (EC:4.2.1.1) | converts | HCO3- (CHEBI:17544) -> CO2 (CHEBI:16526) | “Within carboxysomes, CA… convert[s] HCO3− to CO2 to elevate luminal CO2 and promote Rubisco-catalyzed CO2 fixation” (pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2) | Pulsford 2024, *Science Advances* | 10.1126/sciadv.adk7283 https://doi.org/10.1126/sciadv.adk7283 | Strong; α-carboxysome CA in cyanobacteria. |
| HCO3- (CHEBI:17544) | diffuses_into | carboxysome (GO:0036464) | “HCO3- diffuses into it, CA supplies CO2 to RubisCo” (kurkela2024inorganiccarbonsensing pages 2-3) | Kurkela 2024, *Physiologia Plantarum* | 10.1111/ppl.14140 https://doi.org/10.1111/ppl.14140 | Strong in cyanobacteria. |
| carboxysome (GO:0036464) | concentrates | CO2 (CHEBI:16526) near RuBisCO (EC:4.1.1.39) | “carboxysomes… concentrate CO2 near Rubisco to bridge environmental DIC supply to enzymatic demand” (scott2024widespreaddissolvedinorganic pages 4-7) | Scott 2024, *Applied and Environmental Microbiology* | 10.1128/AEM.01557-23 https://doi.org/10.1128/AEM.01557-23 | Strong review-level synthesis for CBB users. |
| SbtA bicarbonate transporter (label-only candidate; GO:0015701 bicarbonate transport) | imports | HCO3- (CHEBI:17544) | “BicA and SbtA are Na+/HCO3- symporters” (kurkela2024inorganiccarbonsensing pages 2-3) | Kurkela 2024, *Physiologia Plantarum* | 10.1111/ppl.14140 https://doi.org/10.1111/ppl.14140 | Strong for cyanobacteria; Na+-dependent. |
| BicA bicarbonate transporter (label-only candidate; GO:0015701) | imports | HCO3- (CHEBI:17544) | “BicA and SbtA are Na+/HCO3- symporters” (kurkela2024inorganiccarbonsensing pages 2-3) | Kurkela 2024, *Physiologia Plantarum* | 10.1111/ppl.14140 https://doi.org/10.1111/ppl.14140 | Strong for cyanobacteria; Na+-dependent. |
| BCT1 / CmpABCD transporter (label-only candidate; GO:0015701) | imports | HCO3- (CHEBI:17544) | “BCT1 is an ABC-type high-affinity HCO3- pump encoded by the cmp operon” (kurkela2024inorganiccarbonsensing pages 2-3) | Kurkela 2024, *Physiologia Plantarum* | 10.1111/ppl.14140 https://doi.org/10.1111/ppl.14140 | Strong for cyanobacteria. |
| NDH-13 / CupA complex (label-only candidate) | converts | CO2 (CHEBI:16526) -> HCO3- (CHEBI:17544) | “specialized NDH-1 complexes (NDH-13/CupA and NDH-14/CupB) convert CO2 to cytosolic HCO3-” (kurkela2024inorganiccarbonsensing pages 2-3) | Kurkela 2024, *Physiologia Plantarum* | 10.1111/ppl.14140 https://doi.org/10.1111/ppl.14140 | Strong for cyanobacterial CCM. |
| NDH-14 / CupB complex (label-only candidate) | converts | CO2 (CHEBI:16526) -> HCO3- (CHEBI:17544) | “specialized NDH-1 complexes (NDH-13/CupA and NDH-14/CupB) convert CO2 to cytosolic HCO3-” (kurkela2024inorganiccarbonsensing pages 2-3) | Kurkela 2024, *Physiologia Plantarum* | 10.1111/ppl.14140 https://doi.org/10.1111/ppl.14140 | Strong for cyanobacterial CCM. |
| simultaneous loss of NDH complexes + bicarbonate transporters (label-only perturbation) | prevents_growth_in | ambient air / low Ci (ENVO:01000541 air) | “inactivation of two NDH complexes plus three bicarbonate transporters prevents growth in ambient air while permitting growth in high CO2” (kurkela2024inorganiccarbonsensing pages 1-2) | Kurkela 2024, *Physiologia Plantarum* | 10.1111/ppl.14140 https://doi.org/10.1111/ppl.14140 | Strong systems-level causal phenotype; cyanobacteria. |
| bicA overexpression (label-only perturbation) | increases | photosynthetic activity / glycogen production / biomass accumulation (label-only candidates) | “bicA overexpression increases photosynthetic activity, glycogen production and biomass accumulation” (kurkela2024inorganiccarbonsensing pages 2-3) | Kurkela 2024, *Physiologia Plantarum* | 10.1111/ppl.14140 https://doi.org/10.1111/ppl.14140 | Strong but physiology-specific; cyanobacteria. |
| simultaneous sbtA and bicA inactivation (label-only perturbation) | decreases | growth at alkaline pH (ENVO:09200013 alkaline water, label-only) | “simultaneous inactivation of both genes decreases growth in alkaline pH” (kurkela2024inorganiccarbonsensing pages 2-3) | Kurkela 2024, *Physiologia Plantarum* | 10.1111/ppl.14140 https://doi.org/10.1111/ppl.14140 | Strong, condition-specific phenotype. |
| CP12 (GO:0097042 CP12 protein, label-only) | inhibits | phosphoribulokinase / PRK (EC:2.7.1.19) | “Cp12 protein downregulates the CBB cycle in darkness by inhibiting phosphoribulokinase” (lucius2024theprimarycarbon pages 1-2) | Lucius 2024, *Frontiers in Plant Science* | 10.3389/fpls.2024.1417680 https://doi.org/10.3389/fpls.2024.1417680 | Strong; cyanobacteria; darkness context. |
| CP12 (label-only candidate) | inhibits | glyceraldehyde-3-phosphate dehydrogenase / GAPDH (EC:1.2.1.12) | “Cp12 protein downregulates the CBB cycle in darkness by inhibiting… glyceraldehyde 3-phosphate dehydrogenase” (lucius2024theprimarycarbon pages 1-2) | Lucius 2024, *Frontiers in Plant Science* | 10.3389/fpls.2024.1417680 https://doi.org/10.3389/fpls.2024.1417680 | Strong; cyanobacteria; darkness context. |
| RuBP (CHEBI:16710) | activates | CsoSCA / α-carboxysome carbonic anhydrase (EC:4.2.1.1) | “Cyanobium CsoSCA is allosterically activated by the Rubisco substrate ribulose-1,5-bisphosphate” (pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2) | Pulsford 2024, *Science Advances* | 10.1126/sciadv.adk7283 https://doi.org/10.1126/sciadv.adk7283 | Strong; α-cyanobacterial carboxysomes. |
| RuBP-activated CsoSCA (label-only state) | promotes | Rubisco carboxylation rate (EC:4.1.1.39) | “RuBP levels regulate CA activity to optimize the environment for carbon fixation by Rubisco” (pulsford2024cyanobacterialαcarboxysomecarbonic media 5f6b944e) | Pulsford 2024, *Science Advances* | 10.1126/sciadv.adk7283 https://doi.org/10.1126/sciadv.adk7283 | Strong but model-based reaction-diffusion evidence; note figure-derived summary. |
| RbcR transcription factor (label-only candidate) | activates_expression_of | rbcLXS operon (label-only candidate) | “RbcR… activates expression of the rbcLXS and ccmK2K1LMN operons in low Ci” (kurkela2024inorganiccarbonsensing pages 6-7) | Kurkela 2024, *Physiologia Plantarum* | 10.1111/ppl.14140 https://doi.org/10.1111/ppl.14140 | Strong; cyanobacteria; low-Ci context. |
| RbcR transcription factor (label-only candidate) | activates_expression_of | ccmK2K1LMN carboxysome shell operon (label-only candidate) | “RbcR… activates expression of the rbcLXS and ccmK2K1LMN operons in low Ci” (kurkela2024inorganiccarbonsensing pages 6-7) | Kurkela 2024, *Physiologia Plantarum* | 10.1111/ppl.14140 https://doi.org/10.1111/ppl.14140 | Strong; cyanobacteria; low-Ci context. |
| CmpR transcription factor (label-only candidate) | activates_expression_of | BCT1 / cmp operon (label-only candidate) | “2-phosphoglycolate and ribulose-1,5-bisphosphate activate transcription activator CmpR” and “activates the BCT1 transporter operon in low CO2” (kurkela2024inorganiccarbonsensing pages 8-8) | Kurkela 2024, *Physiologia Plantarum* | 10.1111/ppl.14140 https://doi.org/10.1111/ppl.14140 | Strong; cyanobacteria; low-CO2 context. |
| 2-phosphoglycolate / 2-PG (CHEBI:17741) | activates | CmpR transcription factor (label-only candidate) | “2-phosphoglycolate and ribulose-1,5-bisphosphate activate transcription activator CmpR” (kurkela2024inorganiccarbonsensing pages 8-8) | Kurkela 2024, *Physiologia Plantarum* | 10.1111/ppl.14140 https://doi.org/10.1111/ppl.14140 | Strong regulatory metabolite edge. |
| RuBP (CHEBI:16710) | activates | CmpR transcription factor (label-only candidate) | “2-phosphoglycolate and ribulose-1,5-bisphosphate activate transcription activator CmpR” (kurkela2024inorganiccarbonsensing pages 8-8) | Kurkela 2024, *Physiologia Plantarum* | 10.1111/ppl.14140 https://doi.org/10.1111/ppl.14140 | Strong regulatory metabolite edge. |
| CcmR / NdhR transcription factor (label-only candidate) | represses_or_controls | ndhF3/ndhD3/cupA operon (label-only candidate) | “the ndhF3/ndhD3/cupA operon is regulated by repressor CcmR and activator CyAbrB2” (kurkela2024inorganiccarbonsensing pages 6-6) | Kurkela 2024, *Physiologia Plantarum* | 10.1111/ppl.14140 https://doi.org/10.1111/ppl.14140 | Strong for cyanobacteria. |
| CyAbrB2 transcription factor (label-only candidate) | activates | ndhF3/ndhD3/cupA operon (label-only candidate) | “the ndhF3/ndhD3/cupA operon is regulated by repressor CcmR and activator CyAbrB2” (kurkela2024inorganiccarbonsensing pages 6-6) | Kurkela 2024, *Physiologia Plantarum* | 10.1111/ppl.14140 https://doi.org/10.1111/ppl.14140 | Strong for cyanobacteria. |
| CbbR transcriptional regulator (label-only candidate; LTTR) | activates_transcription_of | cbb operon (label-only candidate) | “CbbR, the Master Regulator for Microbial Carbon Dioxide Fixation” and “elevate expression of the cbb CO2 fixation operons” (dangel2015cbbrthemaster pages 1-5) | Dangel 2015, *Journal of Bacteriology* | 10.1128/JB.00442-15 https://doi.org/10.1128/JB.00442-15 | Strong broad review-level evidence across bacteria. |
| CbbR (label-only candidate) | required_for_expression_of | cbb operon (label-only candidate) | “cbb and gap-pgk operons are completely dependent on the… presence of the transcriptional regulator CbbR” (keulen2003analysisofdna pages 2-3) | van Keulen 2003, *Journal of Bacteriology* | 10.1128/JB.185.4.1245-1252.2003 https://doi.org/10.1128/JB.185.4.1245-1252.2003 | Strong direct evidence in *Xanthobacter flavus*. |
| CbbR (label-only candidate) | binds | cbb promoter IR1/IR2/IR3 sites (label-only candidate) | “The cbb promoter contains three CbbR binding sites (IR1, IR2, IR3)” (keulen2003analysisofdna pages 1-2) | van Keulen 2003, *Journal of Bacteriology* | 10.1128/JB.185.4.1245-1252.2003 https://doi.org/10.1128/JB.185.4.1245-1252.2003 | Strong direct DNA-binding evidence. |
| NADPH (CHEBI:16474) | increases_affinity_of | CbbR for cbb promoter (label-only candidate interaction) | “NADPH increases CbbR affinity (~3-fold)” (keulen2003analysisofdna pages 1-2) | van Keulen 2003, *Journal of Bacteriology* | 10.1128/JB.185.4.1245-1252.2003 https://doi.org/10.1128/JB.185.4.1245-1252.2003 | Strong but taxon-specific (*X. flavus*). |
| iota carbonic anhydrase / ιCA (EC:4.2.1.1; label-only class) | required_for | low-CO2 growth / ambient-air growth (label-only phenotype) | “the T. pelophila ιCA-135 mutant is ‘unable to grow under ambient air’” (wieschollek2024anewtype pages 15-17) | Wieschollek 2024, *Applied and Environmental Microbiology* | 10.1128/AEM.01075-24 https://doi.org/10.1128/AEM.01075-24 | Strong direct mutant phenotype in *Thiomicrospira pelophila*. |
| interruption of ιCA gene (label-only perturbation) | abolishes | carboxysomal CA activity (EC:4.2.1.1) | “Purified carboxysomes from an ιCA-interrupted strain… lacked detectable CA activity” (wieschollek2024anewtype pages 5-8) | Wieschollek 2024, *Applied and Environmental Microbiology* | 10.1128/AEM.01075-24 https://doi.org/10.1128/AEM.01075-24 | Strong direct enzymatic phenotype. |
| carboxysomal ιCA (EC:4.2.1.1) | enables | CO2-concentrating mechanism function (GO:0015979 photosynthesis/carbon fixation context; label-only CCM) | “prevented growth under low-CO2 conditions, indicating the enzyme is necessary for the CCM to function under CO2 limitation” (wieschollek2024anewtype pages 1-2) | Wieschollek 2024, *Applied and Environmental Microbiology* | 10.1128/AEM.01075-24 https://doi.org/10.1128/AEM.01075-24 | Strong but specific to *Thiomicrospira* α-carboxysomes. |
| T. pelophila ιCA expressed in E. coli ΔyadF ΔcynT (label-only heterologous system) | rescues | low-CO2 growth (label-only phenotype) | “restored the ability to grow in low CO2” (wieschollek2024anewtype pages 1-2) | Wieschollek 2024, *Applied and Environmental Microbiology* | 10.1128/AEM.01075-24 https://doi.org/10.1128/AEM.01075-24 | Strong complementation evidence. |
| extracellular carbonic anhydrase / eCA (EC:4.2.1.1) | facilitates | DIC transporter activity (label-only candidate) | “Extracellular CAs may ‘function to supply HCO3− or CO2 to DIC transporters,’ and ‘if coexpressed, the eCA could facilitate transporter activity’” (scott2024widespreaddissolvedinorganic pages 13-15) | Scott 2024, *Applied and Environmental Microbiology* | 10.1128/AEM.01557-23 https://doi.org/10.1128/AEM.01557-23 | uncertain; review inference from genomic/physiological synthesis. |
| cytoplasmic carbonic anhydrase / cCA (EC:4.2.1.1) | can_cause | CO2 leakage (label-only process) | “cytosolic (non-vectoral) CA activity can dissipate the CCM by causing CO2 leakage” (scott2024widespreaddissolvedinorganic pages 2-4) | Scott 2024, *Applied and Environmental Microbiology* | 10.1128/AEM.01557-23 https://doi.org/10.1128/AEM.01557-23 | Strong conceptual constraint for curation. |
| dissolved inorganic carbon transporter DAC (label-only candidate) | absent_above | pH 8.3 (PATO/label-only) | “DACs absent above pH 8.3 where CO2 is scarce” (scott2024widespreaddissolvedinorganic pages 7-10) | Scott 2024, *Applied and Environmental Microbiology* | 10.1128/AEM.01557-23 https://doi.org/10.1128/AEM.01557-23 | uncertain; comparative genomic distribution, not direct mechanism. |
| SbtA transporter (label-only candidate) | absent_below | pH 4.3 (PATO/label-only) | “SbtA absent below pH 4.3 where HCO3− is scarce” (scott2024widespreaddissolvedinorganic pages 7-10) | Scott 2024, *Applied and Environmental Microbiology* | 10.1128/AEM.01557-23 https://doi.org/10.1128/AEM.01557-23 | uncertain; comparative genomic distribution. |
| extracellular CA / eCA (EC:4.2.1.1) | absent_below_or_above | pH <5.1 or >8.3 (label-only pH ranges) | “extracellular CA absent below pH 5.1 or above pH 8.3” (scott2024widespreaddissolvedinorganic pages 7-10) | Scott 2024, *Applied and Environmental Microbiology* | 10.1128/AEM.01557-23 https://doi.org/10.1128/AEM.01557-23 | uncertain; comparative genomic distribution. |
| CBB cycle (METPO:traitmech:000020) | works_at | very low CO2 concentrations (label-only environmental condition) | “enables the CBB cycle to work at very low CO2 concentrations” (bachleitner2023thepotentialof pages 3-4) | Bachleitner 2023, *Nature Communications* | 10.1038/s41467-023-42790-6 https://doi.org/10.1038/s41467-023-42790-6 | Expert synthesis; useful high-level trait context, not a specific molecular edge. |
| cbb_chr promoter in Cupriavidus necator (label-only candidate) | drives_expression_of | heterologous AppA phytase (label-only candidate) | “native CBB-cycle promoters were tested for heterologous phytase (AppA) expression… the cbb_chr promoter in particular yielded robust AppA expression” (arhar2024co2basedproductionof pages 9-10) | Arhar 2024, *Microbial Cell Factories* | 10.1186/s12934-023-02280-2 https://doi.org/10.1186/s12934-023-02280-2 | Strong application edge; autotrophic engineering context, not native CBB mechanism. |
| CBB and hydrogenase promoters in C. necator (label-only candidates) | outperform | constitutive j5 promoter (label-only candidate) under lithoautotrophy | “native CBB and hydrogenase promoters outperformed the constitutive j5 promoter under lithoautotrophic conditions” (arhar2024co2basedproductionof pages 9-10) | Arhar 2024, *Microbial Cell Factories* | 10.1186/s12934-023-02280-2 https://doi.org/10.1186/s12934-023-02280-2 | Strong engineering evidence; context-specific. |
| 5% CO2 assay condition (label-only experimental factor) | increases | measured RuBisCO activity relative to 20 mM NaHCO3 (label-only assay readout) | “RuBP consumption rates 5–7× higher than… 20 mM NaHCO3” (faisal2024rubiscoactivityassays pages 1-2) | Faisal 2024, *Microbial Cell Factories* | 10.1186/s12934-024-02357-6 https://doi.org/10.1186/s12934-024-02357-6 | Assay-specific; do not overgeneralize biologically. |
| impaired CA activity in lysate (label-only assay factor) | limits | HCO3- -> CO2 supply to RuBisCO (label-only assay process) | “lower activity with NaHCO3 may reflect impaired carbonic anhydrase activity… limiting conversion of HCO3− to CO2” (faisal2024rubiscoactivityassays pages 1-2) | Faisal 2024, *Microbial Cell Factories* | 10.1186/s12934-024-02357-6 https://doi.org/10.1186/s12934-024-02357-6 | Assay interpretation; uncertain outside lysate context. |


*Table: This table compiles curation-ready causal edges for the microbial Calvin–Benson–Bassham cycle, spanning core pathway chemistry, CCM components, regulation, environmental constraints, and recent engineering applications. It is designed to support TraitMech node/edge selection with source-backed snippets and uncertainty notes.*

---

## Warnings / claims not ready (or requiring careful curation)

1. **Comparative-genomics distribution rules (e.g., presence/absence vs pH)** from the DIC toolkit review are useful for hypothesis generation but should be curated as *uncertain/inferred* unless supported by direct experimental tests in the taxon of interest (scott2024widespreaddissolvedinorganic pages 7-10, scott2024widespreaddissolvedinorganic pages 10-13).
2. **In vitro RuBisCO assay effects (CO2 vs bicarbonate)** quantify assay behavior and CA limitations in lysate contexts; do not curate as universal in vivo physiology without additional corroboration (faisal2024rubiscoactivityassays pages 1-2).
3. **Model-derived edges** (e.g., RuBP-regulated CA flux optimizing Rubisco fixation) are mechanistically plausible and visually supported, but should be flagged as model-supported rather than knockout-validated in vivo in a given organism (pulsford2024cyanobacterialαcarboxysomecarbonic media 5f6b944e, pulsford2024cyanobacterialαcarboxysomecarbonic media d5ca422c).

---

## DOI-first bibliography (with publication dates and URLs)

- Pulsford SB *et al.* (2024-05). *Science Advances*. “Cyanobacterial α-carboxysome carbonic anhydrase is allosterically regulated by the Rubisco substrate RuBP.” DOI:10.1126/sciadv.adk7283 https://doi.org/10.1126/sciadv.adk7283 (pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2, pulsford2024cyanobacterialαcarboxysomecarbonic media 5f6b944e, pulsford2024cyanobacterialαcarboxysomecarbonic media d5ca422c)
- Wieschollek J *et al.* (2024-09). *Applied and Environmental Microbiology*. “A new type of carboxysomal carbonic anhydrase in sulfur chemolithoautotrophs from alkaline environments.” DOI:10.1128/aem.01075-24 https://doi.org/10.1128/aem.01075-24 (wieschollek2024anewtype pages 1-2, wieschollek2024anewtype pages 5-8, wieschollek2024anewtype pages 15-17)
- Scott KM *et al.* (2024-02). *Applied and Environmental Microbiology*. “Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic Bacteria and Archaea…” DOI:10.1128/aem.01557-23 https://doi.org/10.1128/aem.01557-23 (scott2024widespreaddissolvedinorganic pages 2-4, scott2024widespreaddissolvedinorganic pages 1-2)
- Kurkela J, Tyystjärvi T (2024-01). *Physiologia Plantarum*. “Inorganic carbon sensing and signalling in cyanobacteria.” DOI:10.1111/ppl.14140 https://doi.org/10.1111/ppl.14140 (kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 2-3)
- Lucius S, Hagemann M (2024-07). *Frontiers in Plant Science*. “The primary carbon metabolism in cyanobacteria and its regulation.” DOI:10.3389/fpls.2024.1417680 https://doi.org/10.3389/fpls.2024.1417680 (lucius2024theprimarycarbon pages 1-2)
- Faisal M *et al.* (2024-03). *Microbial Cell Factories*. “RuBisCO activity assays: …” DOI:10.1186/s12934-024-02357-6 https://doi.org/10.1186/s12934-024-02357-6 (faisal2024rubiscoactivityassays pages 1-2, faisal2024rubiscoactivityassays pages 4-6)
- Arhar S *et al.* (2024-01). *Microbial Cell Factories*. “CO2-based production of phytase from highly stable expression plasmids in Cupriavidus necator H16.” DOI:10.1186/s12934-023-02280-2 https://doi.org/10.1186/s12934-023-02280-2 (arhar2024co2basedproductionof pages 1-2, arhar2024co2basedproductionof pages 7-9, arhar2024co2basedproductionof pages 9-10)
- Bachleitner S *et al.* (2023-11). *Nature Communications*. “The potential of CO2-based production cycles in biotechnology to fight the climate crisis.” DOI:10.1038/s41467-023-42790-6 https://doi.org/10.1038/s41467-023-42790-6 (bachleitner2023thepotentialof pages 3-4, bachleitner2023thepotentialof pages 4-5)
- Dangel AW, Tabita FR (2015-11). *Journal of Bacteriology*. “CbbR, the Master Regulator for Microbial Carbon Dioxide Fixation.” DOI:10.1128/jb.00442-15 https://doi.org/10.1128/jb.00442-15 (dangel2015cbbrthemaster pages 1-5)
- van Keulen G *et al.* (2003-02). *Journal of Bacteriology*. “Analysis of DNA Binding and Transcriptional Activation by the LysR-Type Transcriptional Regulator CbbR of Xanthobacter flavus.” DOI:10.1128/jb.185.4.1245-1252.2003 https://doi.org/10.1128/jb.185.4.1245-1252.2003 (keulen2003analysisofdna pages 2-3, keulen2003analysisofdna pages 1-2)


References

1. (kurkela2024inorganiccarbonsensing pages 2-3): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 15 citations and is from a peer-reviewed journal.

2. (lucius2024theprimarycarbon pages 1-2): Stefan Lucius and Martin Hagemann. The primary carbon metabolism in cyanobacteria and its regulation. Frontiers in Plant Science, Jul 2024. URL: https://doi.org/10.3389/fpls.2024.1417680, doi:10.3389/fpls.2024.1417680. This article has 88 citations.

3. (kurkela2024inorganiccarbonsensing pages 1-2): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 15 citations and is from a peer-reviewed journal.

4. (bachleitner2023thepotentialof pages 2-3): Simone Bachleitner, Özge Ata, and Diethard Mattanovich. The potential of co2-based production cycles in biotechnology to fight the climate crisis. Nature Communications, Nov 2023. URL: https://doi.org/10.1038/s41467-023-42790-6, doi:10.1038/s41467-023-42790-6. This article has 87 citations and is from a highest quality peer-reviewed journal.

5. (scott2024widespreaddissolvedinorganic pages 2-4): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

6. (scott2024widespreaddissolvedinorganic pages 1-2): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

7. (wieschollek2024anewtype pages 15-17): Jana Wieschollek, Daniella Fuller, Arin Gahramanova, Terrence Millen, Ashianna J. Mislay, Ren R. Payne, Daniel P. Walsh, YuXuan Zhao, Madilyn Carney, Jaden Cross, John Kashem, Ruchi Korde, Christine Lacy, Noah Lyons, Tori Mason, Kayla Torres-Betancourt, Tyler Trapnell, Clare L. Dennison, Dale Chaput, and Kathleen M. Scott. A new type of carboxysomal carbonic anhydrase in sulfur chemolithoautotrophs from alkaline environments. Sep 2024. URL: https://doi.org/10.1128/aem.01075-24, doi:10.1128/aem.01075-24. This article has 8 citations and is from a peer-reviewed journal.

8. (faisal2024rubiscoactivityassays pages 1-2): Muhammad Faisal, Aditya P. Sarnaik, Nandini Kannoju, Nima Hajinajaf, Muhammad Javaid Asad, Ryan W. Davis, and Arul M. Varman. Rubisco activity assays: a simplified biochemical redox approach for in vitro quantification and an rna sensor approach for in vivo monitoring. Microbial Cell Factories, Mar 2024. URL: https://doi.org/10.1186/s12934-024-02357-6, doi:10.1186/s12934-024-02357-6. This article has 5 citations and is from a peer-reviewed journal.

9. (faisal2024rubiscoactivityassays pages 4-6): Muhammad Faisal, Aditya P. Sarnaik, Nandini Kannoju, Nima Hajinajaf, Muhammad Javaid Asad, Ryan W. Davis, and Arul M. Varman. Rubisco activity assays: a simplified biochemical redox approach for in vitro quantification and an rna sensor approach for in vivo monitoring. Microbial Cell Factories, Mar 2024. URL: https://doi.org/10.1186/s12934-024-02357-6, doi:10.1186/s12934-024-02357-6. This article has 5 citations and is from a peer-reviewed journal.

10. (pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2): Sacha B. Pulsford, Megan A. Outram, Britta Förster, Timothy Rhodes, Simon J. Williams, Murray R. Badger, G. Dean Price, Colin J. Jackson, and Benedict M. Long. Cyanobacterial α-carboxysome carbonic anhydrase is allosterically regulated by the rubisco substrate rubp. Science Advances, May 2024. URL: https://doi.org/10.1126/sciadv.adk7283, doi:10.1126/sciadv.adk7283. This article has 25 citations and is from a highest quality peer-reviewed journal.

11. (pulsford2024cyanobacterialαcarboxysomecarbonic media 5f6b944e): Sacha B. Pulsford, Megan A. Outram, Britta Förster, Timothy Rhodes, Simon J. Williams, Murray R. Badger, G. Dean Price, Colin J. Jackson, and Benedict M. Long. Cyanobacterial α-carboxysome carbonic anhydrase is allosterically regulated by the rubisco substrate rubp. Science Advances, May 2024. URL: https://doi.org/10.1126/sciadv.adk7283, doi:10.1126/sciadv.adk7283. This article has 25 citations and is from a highest quality peer-reviewed journal.

12. (pulsford2024cyanobacterialαcarboxysomecarbonic media d5ca422c): Sacha B. Pulsford, Megan A. Outram, Britta Förster, Timothy Rhodes, Simon J. Williams, Murray R. Badger, G. Dean Price, Colin J. Jackson, and Benedict M. Long. Cyanobacterial α-carboxysome carbonic anhydrase is allosterically regulated by the rubisco substrate rubp. Science Advances, May 2024. URL: https://doi.org/10.1126/sciadv.adk7283, doi:10.1126/sciadv.adk7283. This article has 25 citations and is from a highest quality peer-reviewed journal.

13. (wieschollek2024anewtype pages 1-2): Jana Wieschollek, Daniella Fuller, Arin Gahramanova, Terrence Millen, Ashianna J. Mislay, Ren R. Payne, Daniel P. Walsh, YuXuan Zhao, Madilyn Carney, Jaden Cross, John Kashem, Ruchi Korde, Christine Lacy, Noah Lyons, Tori Mason, Kayla Torres-Betancourt, Tyler Trapnell, Clare L. Dennison, Dale Chaput, and Kathleen M. Scott. A new type of carboxysomal carbonic anhydrase in sulfur chemolithoautotrophs from alkaline environments. Sep 2024. URL: https://doi.org/10.1128/aem.01075-24, doi:10.1128/aem.01075-24. This article has 8 citations and is from a peer-reviewed journal.

14. (wieschollek2024anewtype pages 5-8): Jana Wieschollek, Daniella Fuller, Arin Gahramanova, Terrence Millen, Ashianna J. Mislay, Ren R. Payne, Daniel P. Walsh, YuXuan Zhao, Madilyn Carney, Jaden Cross, John Kashem, Ruchi Korde, Christine Lacy, Noah Lyons, Tori Mason, Kayla Torres-Betancourt, Tyler Trapnell, Clare L. Dennison, Dale Chaput, and Kathleen M. Scott. A new type of carboxysomal carbonic anhydrase in sulfur chemolithoautotrophs from alkaline environments. Sep 2024. URL: https://doi.org/10.1128/aem.01075-24, doi:10.1128/aem.01075-24. This article has 8 citations and is from a peer-reviewed journal.

15. (wieschollek2024anewtype pages 12-15): Jana Wieschollek, Daniella Fuller, Arin Gahramanova, Terrence Millen, Ashianna J. Mislay, Ren R. Payne, Daniel P. Walsh, YuXuan Zhao, Madilyn Carney, Jaden Cross, John Kashem, Ruchi Korde, Christine Lacy, Noah Lyons, Tori Mason, Kayla Torres-Betancourt, Tyler Trapnell, Clare L. Dennison, Dale Chaput, and Kathleen M. Scott. A new type of carboxysomal carbonic anhydrase in sulfur chemolithoautotrophs from alkaline environments. Sep 2024. URL: https://doi.org/10.1128/aem.01075-24, doi:10.1128/aem.01075-24. This article has 8 citations and is from a peer-reviewed journal.

16. (scott2024widespreaddissolvedinorganic pages 10-13): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

17. (kurkela2024inorganiccarbonsensing pages 8-8): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 15 citations and is from a peer-reviewed journal.

18. (arhar2024co2basedproductionof pages 1-2): Simon Arhar, Thomas Rauter, Holly Stolterfoht-Stock, Vera Lambauer, Regina Kratzer, Margit Winkler, Marianna Karava, Robert Kourist, and Anita Emmerstorfer-Augustin. Co2-based production of phytase from highly stable expression plasmids in cupriavidus necator h16. Microbial Cell Factories, Jan 2024. URL: https://doi.org/10.1186/s12934-023-02280-2, doi:10.1186/s12934-023-02280-2. This article has 22 citations and is from a peer-reviewed journal.

19. (arhar2024co2basedproductionof pages 7-9): Simon Arhar, Thomas Rauter, Holly Stolterfoht-Stock, Vera Lambauer, Regina Kratzer, Margit Winkler, Marianna Karava, Robert Kourist, and Anita Emmerstorfer-Augustin. Co2-based production of phytase from highly stable expression plasmids in cupriavidus necator h16. Microbial Cell Factories, Jan 2024. URL: https://doi.org/10.1186/s12934-023-02280-2, doi:10.1186/s12934-023-02280-2. This article has 22 citations and is from a peer-reviewed journal.

20. (arhar2024co2basedproductionof pages 9-10): Simon Arhar, Thomas Rauter, Holly Stolterfoht-Stock, Vera Lambauer, Regina Kratzer, Margit Winkler, Marianna Karava, Robert Kourist, and Anita Emmerstorfer-Augustin. Co2-based production of phytase from highly stable expression plasmids in cupriavidus necator h16. Microbial Cell Factories, Jan 2024. URL: https://doi.org/10.1186/s12934-023-02280-2, doi:10.1186/s12934-023-02280-2. This article has 22 citations and is from a peer-reviewed journal.

21. (bachleitner2023thepotentialof pages 3-4): Simone Bachleitner, Özge Ata, and Diethard Mattanovich. The potential of co2-based production cycles in biotechnology to fight the climate crisis. Nature Communications, Nov 2023. URL: https://doi.org/10.1038/s41467-023-42790-6, doi:10.1038/s41467-023-42790-6. This article has 87 citations and is from a highest quality peer-reviewed journal.

22. (bachleitner2023thepotentialof pages 4-5): Simone Bachleitner, Özge Ata, and Diethard Mattanovich. The potential of co2-based production cycles in biotechnology to fight the climate crisis. Nature Communications, Nov 2023. URL: https://doi.org/10.1038/s41467-023-42790-6, doi:10.1038/s41467-023-42790-6. This article has 87 citations and is from a highest quality peer-reviewed journal.

23. (dangel2015cbbrthemaster pages 1-5): Andrew W. Dangel and F. Robert Tabita. Cbbr, the master regulator for microbial carbon dioxide fixation. Journal of Bacteriology, 197:3488-3498, Nov 2015. URL: https://doi.org/10.1128/jb.00442-15, doi:10.1128/jb.00442-15. This article has 71 citations and is from a peer-reviewed journal.

24. (keulen2003analysisofdna pages 2-3): Geertje van Keulen, Anja N. J. A. Ridder, Lubbert Dijkhuizen, and Wim G. Meijer. Analysis of dna binding and transcriptional activation by the lysr-type transcriptional regulator cbbr of xanthobacter flavus. Journal of Bacteriology, 185:1245-1252, Feb 2003. URL: https://doi.org/10.1128/jb.185.4.1245-1252.2003, doi:10.1128/jb.185.4.1245-1252.2003. This article has 73 citations and is from a peer-reviewed journal.

25. (keulen2003analysisofdna pages 1-2): Geertje van Keulen, Anja N. J. A. Ridder, Lubbert Dijkhuizen, and Wim G. Meijer. Analysis of dna binding and transcriptional activation by the lysr-type transcriptional regulator cbbr of xanthobacter flavus. Journal of Bacteriology, 185:1245-1252, Feb 2003. URL: https://doi.org/10.1128/jb.185.4.1245-1252.2003, doi:10.1128/jb.185.4.1245-1252.2003. This article has 73 citations and is from a peer-reviewed journal.

26. (wieschollek2024anewtype pages 17-19): Jana Wieschollek, Daniella Fuller, Arin Gahramanova, Terrence Millen, Ashianna J. Mislay, Ren R. Payne, Daniel P. Walsh, YuXuan Zhao, Madilyn Carney, Jaden Cross, John Kashem, Ruchi Korde, Christine Lacy, Noah Lyons, Tori Mason, Kayla Torres-Betancourt, Tyler Trapnell, Clare L. Dennison, Dale Chaput, and Kathleen M. Scott. A new type of carboxysomal carbonic anhydrase in sulfur chemolithoautotrophs from alkaline environments. Sep 2024. URL: https://doi.org/10.1128/aem.01075-24, doi:10.1128/aem.01075-24. This article has 8 citations and is from a peer-reviewed journal.

27. (kurkela2024inorganiccarbonsensing pages 6-7): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 15 citations and is from a peer-reviewed journal.

28. (kurkela2024inorganiccarbonsensing pages 6-6): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 15 citations and is from a peer-reviewed journal.

29. (scott2024widespreaddissolvedinorganic pages 7-10): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

30. (scott2024widespreaddissolvedinorganic pages 4-7): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

31. (scott2024widespreaddissolvedinorganic pages 13-15): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.