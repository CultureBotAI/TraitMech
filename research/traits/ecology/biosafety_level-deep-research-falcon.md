---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T19:25:52.989544'
end_time: '2026-06-17T19:55:56.386597'
duration_seconds: 1803.4
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: biosafety level
  trait_identifier: METPO:1001101
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: biosafety_level
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A quality that categorizes biological agents according to their hazard
    level and required containment measures.
  parent_traits: METPO:1000188
  synonyms: Safety information.risk assessment.biosafety level
  evidence_summary: 'DOI:10.1146/annurev.micro.62.081307.162938: virulence factors
    (Virulence-factor review supports pathogen virulence characteristics (transmissibility,
    severity, treatability) as the biological inputs underlying biosafety-level classification.)
    | DOI:10.1038/nrmicro1592: secretion systems (Secretion-systems review supports
    effector-mediated host damage as a virulence axis informing hazard assessment.)'
  causal_graph_summary: 'biosafety_level_hazard_classification: 8 nodes, 7 edges'
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
- **Trait label:** biosafety level
- **METPO identifier:** METPO:1001101
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A quality that categorizes biological agents according to their hazard level and required containment measures.
- **Parent traits:** METPO:1000188
- **Synonyms:** Safety information.risk assessment.biosafety level
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports pathogen virulence characteristics (transmissibility, severity, treatability) as the biological inputs underlying biosafety-level classification.) | DOI:10.1038/nrmicro1592: secretion systems (Secretion-systems review supports effector-mediated host damage as a virulence axis informing hazard assessment.)
- **Existing causal graph summary:** biosafety_level_hazard_classification: 8 nodes, 7 edges

## Research Objective

Research the microbial trait **biosafety level** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/biosafety_level.yaml`.

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
- **Trait label:** biosafety level
- **METPO identifier:** METPO:1001101
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A quality that categorizes biological agents according to their hazard level and required containment measures.
- **Parent traits:** METPO:1000188
- **Synonyms:** Safety information.risk assessment.biosafety level
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports pathogen virulence characteristics (transmissibility, severity, treatability) as the biological inputs underlying biosafety-level classification.) | DOI:10.1038/nrmicro1592: secretion systems (Secretion-systems review supports effector-mediated host damage as a virulence axis informing hazard assessment.)
- **Existing causal graph summary:** biosafety_level_hazard_classification: 8 nodes, 7 edges

## Research Objective

Research the microbial trait **biosafety level** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/biosafety_level.yaml`.

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


## Curation-focused research report: Microbial trait “biosafety level” (METPO:1001101)

### 1) Scope summary (trait meaning and boundaries)

**Trait definition (operational hazard class):** A *biosafety level (BSL)* is a laboratory containment category (BSL‑1 to BSL‑4) that specifies escalating combinations of practices, engineering controls, PPE, and facility design to mitigate risk from handling biological agents. A recent review summarises the commonly used criteria: BSL‑1 covers low-risk agents unlikely to cause disease in healthy adults; BSL‑2 covers moderate-risk agents; BSL‑3 covers agents that “may cause serious or lethal diseases through inhalation”; and BSL‑4 covers “highly dangerous, life‑threatening agents often lacking vaccines or treatments” (gao2024frombiosafetyto pages 5-6, gao2024frombiosafetyto pages 6-7).

**Distinguish from nearby traits:**
- **Risk group (RG)** is *agent-centered* (hazard of the organism), whereas **BSL/containment level** is *laboratory/task-centered* (how work is conducted and contained). A high-authority review distinguishes RGs as intrinsic categories based on virulence/transmission and availability of prevention/treatment, while containment levels refer to barriers and facility/practice requirements (kimman2008evidencebasedbiosafetya pages 7-8, kimman2008evidencebasedbiosafetya pages 6-7).
- **Physical Containment / Containment Level (PC/CL)** is related terminology used in some jurisdictions (e.g., New Zealand/Australia “PC1, etc.”) rather than “BSL” (morris2024worththerisk? pages 1-2). 

**Boundary cases:** Mapping **RG → BSL/PC/CL is not automatic** because containment decisions depend on the *specific manipulations/activities* and exposure routes; formal risk assessment can upgrade/downgrade requirements for a given agent/task (forbesUnknownyearlaboratoryareas pages 137-140, kimman2008evidencebasedbiosafetya pages 6-7).

**Current understanding trend (WHO LBM4):** The WHO Laboratory Biosafety Manual 4th edition (LBM4, 2020) is widely interpreted as shifting biosafety practice toward **risk-based biorisk management**, “mov[ing] away from a prescriptive definition of biosafety levels toward a risk-based approach emphasizing core requirements and heightened control measures” (sarwar2021pakistan’sexperiencewith pages 2-3, sarwar2021pakistan’sexperiencewith pages 1-2).

### 2) Key concepts and definitions (curation-ready)

**Risk assessment inputs used to set containment:** A 2023 WHO/WOAH/Chatham House technical working group defined major evidence categories needed for biosafety decisions, including “route of inoculation/modes of transmission, infectious dose, laboratory-acquired infections, containment releases, and disinfection and decontamination strategies” (blacksell2023thebiosafetyresearch pages 1-2).

**WHO LBM4 cyclical risk assessment framing:** LBM4 is described as using a cyclical process—“gathering information, evaluating risks, developing a risk control strategy, selecting and implementing control measures, and reviewing those measures” (sarwar2021pakistan’sexperiencewith pages 1-2).

**Engineering and administrative containment concepts:** Biosafety systems are commonly presented as **primary barriers** (e.g., biosafety cabinets, PPE) and **secondary barriers** (facility design/engineering controls) (gao2024frombiosafetyto pages 3-5, kimman2008evidencebasedbiosafetya pages 7-8).

### 3) Recent developments (prioritizing 2023–2024)

**(i) 2024: Governance and national-security framing of biosafety labs.** A 2024 review connects BSLs with national regulatory and security concerns, citing current reliance on WHO LBM4, the U.S. BMBL (6th ed., 2020), and ISO 35001:2019 as key frameworks (gao2024frombiosafetyto pages 9-10).

**(ii) 2023: Evidence gaps for “evidence-based biosafety.”** The 2023 Biosafety Research Roadmap explicitly frames biosafety practice as sometimes lacking robust evidence, motivating targeted research on transmission modes, infectious dose, LAIs, releases, and decontamination effectiveness to support sustainable risk-based containment (blacksell2023thebiosafetyresearch pages 1-2).

**(iii) 2024: ISO 35001 implementation emphasis.** A 2024 perspective highlights ISO 35001’s Plan–Do–Check–Act management-system logic and emphasises **performance evaluation** (internal audits, management review) as central to biorisk management implementation (morris2024worththerisk? pages 1-2).

### 4) Current applications and real-world implementations (with statistics)

#### 4.1 Mandatory incident surveillance and licensing (Canada: LINC system)
Canada’s Human Pathogens and Toxins Act/Regulations require licenses for controlled activities with RG2–RG4 materials and mandatory reporting of incidents, operationalized through the **Laboratory Incident Notification Canada (LINC)** surveillance system (abalos2023surveillanceoflaboratory pages 1-2).

**Recent statistics (2016–2022 overview; published 2024):**
- **928 events** were submitted to LINC (2016–2022), resulting in **361 confirmed exposure incidents** and **355 confirmed non-exposure incidents** after exclusions; among exposures there were **15 suspected** and **10 confirmed** laboratory-acquired infections (LAIs) (balbontin2024canadianlaboratoryincidents pages 2-3).
- Table evidence summarizing annual counts/rates is available (Table 1 crop) (balbontin2024canadianlaboratoryincidents media 5423ea10).

**2022 surveillance (published 2023):**
- **40 confirmed exposure incident reports**; **exposure incident rate 3.8 per 100 active licences**; most incidents involved **RG2** agents (63%) and **non-security sensitive biological agents** (84%); common occurrence types were **sharps** and **procedure-related** (24.2% each) (abalos2023surveillanceoflaboratory pages 1-2).

These data operationalize the trait by linking hazard categories (risk groups) to regulated containment and monitoring infrastructure (abalos2023surveillanceoflaboratory pages 1-2, balbontin2024canadianlaboratoryincidents pages 2-3).

#### 4.2 ISO 35001 biorisk management systems in laboratories
ISO 35001 is used as a management-system standard for biorisk governance and continuous improvement; implementation discussions highlight internal auditing and management review as requirements (callihan2021considerationsforlaboratory pages 1-2, morris2024worththerisk? pages 1-2). One jurisdictional example notes that New Zealand has **no biocontainment laboratories certified to ISO 35001** yet, illustrating adoption barriers (morris2024worththerisk? pages 1-2).

#### 4.3 High-containment facility engineering (BSL-4 exemplars)
A 2025 review of high-level labs gives concrete BSL‑4 design controls (airtight seals, HEPA filtration, stable negative pressure, chemical showers, independent life-support, full-body suits) and notes deployments and planned builds (e.g., Russia planning **15 BSL-4 laboratories by 2024**) (gao2025globalsafetyand pages 14-17).

#### 4.4 Digital/AI monitoring of BSL-3 compliance (emerging implementation)
An applied AI monitoring system for BSL‑3 facilities reported (Taiwan, 2019) **22 BSL‑3 laboratories across 18 institutions**, with 12 established/repurposed for COVID‑19 work; PPE compliance detection models achieved **97.52% accuracy** (external monitoring) and the internal management system achieved **90% accuracy** (fan2025enhancingsafetywith pages 1-2). This represents an emerging “digital containment” layer augmenting traditional barriers.

### 5) Mechanistic entities relevant to a TraitMech causal graph

Because *biosafety level is a classification outcome*, the causal graph should include both (a) **organism-intrinsic hazard determinants** (virulence, toxins, secretion systems) and (b) **contextual exposure determinants** (route, infectious dose, aerosolization potential), which together drive risk-group/containment decisions (blacksell2023thebiosafetyresearch pages 1-2, kimman2008evidencebasedbiosafetya pages 7-8).

#### 5.1 Candidate nodes grouped by type

- **Operational/policy and assessment nodes:** risk group; hazard identification; risk assessment; WHO LBM4 core requirements; heightened control measures; ISO 35001 biorisk management system; SOP quality; human factors (sarwar2021pakistan’sexperiencewith pages 1-2, morris2024worththerisk? pages 1-2, balbontin2024canadianlaboratoryincidents pages 2-3).
- **Exposure and transmission nodes:** inhalation exposure; aerosol generation; route of inoculation; infectious dose; containment release; disinfection/decontamination effectiveness (blacksell2023thebiosafetyresearch pages 1-2, thompson2022surveillanceoflaboratory pages 1-2).
- **Containment structures (engineering controls):** biosafety cabinet; negative-pressure room; HEPA filtration; airlocks (gao2024frombiosafetyto pages 5-6, gao2025globalsafetyand pages 6-8).
- **Microbial virulence mechanism nodes:** type III secretion system; effector translocation; host cytoskeleton manipulation; immune signaling disruption (NF‑κB/MAPK); host cell death pathways; type VII secretion systems (coburn2007typeiiisecretion pages 2-3, bhavsar2007manipulationofhostcell pages 5-6, abdallah2007typeviisecretion—mycobacteria pages 35-37).
- **Toxin/chemical nodes:** hemolysins/enterotoxins; cereulide (CHEBI grounded) (allende2025updateofthe pages 10-11).

A structured candidate node list with example ontology grounding is provided in Artifact 01.

| Node (label) | Node type (biological process / molecular function / structure / environmental or operational factor / policy) | Example grounding (GO/CHEBI/ENVO/other CURIE if known; otherwise 'unmapped') | Rationale/definition (1 short sentence) | Key supporting source IDs |
|---|---|---|---|---|
| risk group | policy | unmapped | Agent-centered hazard class (RG1-RG4) used to summarize intrinsic risk and inform containment decisions. | (thompson2022surveillanceoflaboratory pages 1-2, gao2024frombiosafetyto pages 5-6) |
| hazard identification | environmental or operational factor | unmapped | Initial step in biorisk management that identifies relevant hazards before control selection. | (sarwar2021pakistan’sexperiencewith pages 2-3, sarwar2021pakistan’sexperiencewith pages 1-2) |
| risk assessment | environmental or operational factor | unmapped | Formal evaluation of agent, procedure, and exposure context used to choose containment measures. | (sarwar2021pakistan’sexperiencewith pages 1-2, forbesUnknownyearlaboratoryareas pages 137-140) |
| infectious dose | environmental or operational factor | unmapped | Dose needed to establish infection is a core input to biosafety risk evaluation. | (blacksell2023thebiosafetyresearch pages 1-2) |
| route of transmission | environmental or operational factor | GO:0001617 | Transmission mode strongly affects required containment and exposure controls. | (blacksell2023thebiosafetyresearch pages 1-2, forbesUnknownyearlaboratoryareas pages 137-140) |
| inhalation exposure | environmental or operational factor | CHEBI:15378 | Inhalation is a major exposure route and a key reason some agents require BSL-3 practices. | (gao2024frombiosafetyto pages 5-6, thompson2022surveillanceoflaboratory pages 1-2) |
| aerosol generation / aerosol transmissibility | environmental or operational factor | ENVO:00002005 | Aerosolizable agents increase laboratory-acquired infection risk and drive airborne containment needs. | (gao2024frombiosafetyto pages 3-5, gao2024frombiosafetyto pages 6-7) |
| laboratory-acquired infection history | environmental or operational factor | unmapped | Prior LAIs provide empirical evidence about real-world hazard and biosafety failure modes. | (blacksell2023thebiosafetyresearch pages 1-2, balbontin2024canadianlaboratoryincidents pages 2-3) |
| containment release | environmental or operational factor | unmapped | Release or escape potential is a specific biosafety assessment criterion for containment planning. | (blacksell2023thebiosafetyresearch pages 1-2, abalos2023surveillanceoflaboratory pages 1-2) |
| disinfection / decontamination strategy | environmental or operational factor | GO:0042737 | Effectiveness of decontamination is part of evidence-based biorisk management. | (blacksell2023thebiosafetyresearch pages 1-2, gao2025globalsafetyand pages 6-8) |
| primary containment (biosafety cabinet) | structure | OBI:0400103 | BSCs physically separate worker and agent and are core primary barriers in laboratory biosafety. | (callihan2021considerationsforlaboratory pages 1-2, gao2025globalsafetyand pages 6-8) |
| negative pressure room | structure | unmapped | Directional inward airflow is a secondary containment feature widely associated with BSL-3/4 labs. | (gao2024frombiosafetyto pages 5-6, gao2025globalsafetyand pages 6-8) |
| HEPA filtration | structure | unmapped | HEPA-filtered exhaust limits escape of infectious aerosols from containment spaces. | (gao2025globalsafetyand pages 6-8, abdallah2007typeviisecretion—mycobacteria pages 35-37) |
| airlock entry system | structure | unmapped | Airlocks are a maximal-containment engineering feature characteristic of BSL-4 facilities. | (gao2024frombiosafetyto pages 5-6) |
| personal protective equipment | environmental or operational factor | OBI:0002803 | PPE is a core requirement and escalates with hazard level and task risk. | (sarwar2021pakistan’sexperiencewith pages 2-3, gao2024frombiosafetyto pages 9-10) |
| standard operating procedures | environmental or operational factor | unmapped | SOP quality and compliance are major determinants of incident frequency in laboratories. | (balbontin2024canadianlaboratoryincidents pages 2-3, atchessi2021surveillanceoflaboratory pages 1-2) |
| human factors / workload pressure | environmental or operational factor | unmapped | Human interaction issues such as workload and error are leading root causes of exposure incidents. | (thompson2022surveillanceoflaboratory pages 1-2, abalos2023surveillanceoflaboratory pages 1-2) |
| availability of vaccines | environmental or operational factor | VO:0000001 | Availability of preventive measures lowers hazard severity and can influence risk-group reasoning. | (gao2024frombiosafetyto pages 6-7, kimman2008evidencebasedbiosafetya pages 6-7) |
| availability of treatments | environmental or operational factor | DRON:00000005 | Availability of effective therapy is a standard criterion in risk-group and BSL reasoning. | (gao2024frombiosafetyto pages 6-7, kimman2008evidencebasedbiosafetya pages 6-7) |
| ISO 35001 biorisk management system | policy | ISO:35001:2019 | ISO 35001 provides a management-system framework for identifying, controlling, and improving biorisk. | (callihan2021considerationsforlaboratory pages 1-2, morris2024worththerisk? pages 1-2) |
| WHO LBM4 core requirements | policy | unmapped | WHO LBM4 defines baseline biosafety requirements used across laboratory activities. | (sarwar2021pakistan’sexperiencewith pages 2-3, sarwar2021pakistan’sexperiencewith pages 1-2) |
| WHO LBM4 heightened control measures | policy | unmapped | WHO LBM4 adds heightened controls for higher-risk activities beyond core requirements. | (sarwar2021pakistan’sexperiencewith pages 2-3) |
| type III secretion system | structure | GO:0030257 | T3SS is a dedicated virulence apparatus that injects effectors into host cells and contributes to disease. | (coburn2007typeiiisecretion pages 2-3, coburn2007typeiiisecretion pages 1-2) |
| effector protein translocation | biological process | GO:0030254 | Secreted effectors alter host pathways and are direct mechanistic inputs into pathogenic potential. | (bhavsar2007manipulationofhostcell pages 5-6, angot2007exploitationofeukaryotic pages 1-2) |
| host cytoskeleton manipulation | biological process | GO:0051493 | Many T3SS effectors remodel actin and associated pathways to promote invasion and tissue damage. | (coburn2007typeiiisecretion pages 2-3, angot2007exploitationofeukaryotic pages 1-2) |
| immune evasion / NF-kB disruption | biological process | GO:0038061 | Effector-mediated blockade of immune signaling increases virulence and hazard to hosts. | (bhavsar2007manipulationofhostcell pages 5-6, angot2007exploitationofeukaryotic pages 1-2) |
| apoptosis / caspase-1 activation | biological process | GO:0097190 | Pathogen-triggered host cell death pathways are mechanistic markers of virulence severity. | (bhavsar2007manipulationofhostcell pages 5-6) |
| type VII secretion system | structure | GO:0030257 | Mycobacterial type VII secretion contributes to macrophage escape, spread, and virulence. | (abdallah2007typeviisecretion—mycobacteria pages 35-37) |
| hemolysin | molecular function | GO:0019829 | Hemolytic toxins are direct host-damaging factors relevant to pathogenic hazard classification. | (allende2025updateofthe pages 10-11) |
| enterotoxin | molecular function | GO:0050384 | Enterotoxins such as Nhe and Hbl contribute to cytotoxicity and disease severity. | (allende2025updateofthe pages 10-11) |
| cereulide | structure | CHEBI:132951 | Cereulide is a plasmid-encoded emetic toxin illustrating toxin biosynthesis as a hazard determinant. | (allende2025updateofthe pages 10-11) |


*Table: This table lists candidate nodes for a biosafety-level causal graph, spanning operational risk-assessment concepts, containment structures, and microbial virulence mechanisms. It is useful for deciding which concepts can be grounded and curated into a TraitMech-style node set.*

### 6) Candidate causal edges (triples) with evidence and curation notes

A curated set of candidate edges (with quotes and uncertainty notes) is provided in Artifact 00.

| Subject node | Predicate | Object node | Evidence snippet (quoted) | Source (DOI/URL, year) | Uncertainty/notes |
|---|---|---|---|---|---|
| hazard identification / risk assessment | guides selection of | control measures / containment measures | “hazard identification and risk assessment are central” and the WHO LBM4 describes a cyclical process of “gathering information, evaluating risks, developing a risk control strategy, selecting and implementing control measures” (sarwar2021pakistan’sexperiencewith pages 2-3, sarwar2021pakistan’sexperiencewith pages 1-2) | Sarwar & Vijayan, doi:10.1016/j.jobb.2021.09.002, 2021 | Strong support for generic biorisk-control edge; node is process-level rather than organism-intrinsic. |
| WHO LBM4 risk-based approach | shifts away from | prescriptive biosafety-level assignment | WHO LBM4 “has adopted a risk-based approach” and “moves away from a prescriptive definition of biosafety levels toward a risk-based approach emphasizing core requirements and heightened control measures” (sarwar2021pakistan’sexperiencewith pages 1-2, sarwar2021pakistan’sexperiencewith pages 2-3) | Sarwar & Vijayan, doi:10.1016/j.jobb.2021.09.002, 2021 | Strong for policy/assessment framing; should be curated as guidance context, not a microbial mechanism. |
| risk group classification (RG1–RG4) | maps to / informs | containment level / biosafety level | “risk groups (RG1–RG4)” classify hazards, and facilities working with RG2 and above require licensing; BSL categories are progressive containment categories linked to risk group/hazard classification (thompson2022surveillanceoflaboratory pages 1-2, gao2024frombiosafetyto pages 5-6) | Thompson et al., doi:10.14745/ccdr.v48i10a08, 2022; Gao et al., doi:10.3390/laboratories1030013, 2024 | Mapping is jurisdiction-dependent and not always one-to-one; curate as broad relation only. |
| transmission via inhalation / aerosol route | increases requirement for | BSL-3 containment | BSL-3 is for agents that “may cause serious or lethal diseases through inhalation” (gao2024frombiosafetyto pages 5-6, gao2024frombiosafetyto pages 6-7) | Gao et al., doi:10.3390/laboratories1030013, 2024 | Strong, canonical BSL-3 criterion; mechanism is route of exposure rather than specific gene. |
| lack of effective treatment or vaccine | supports classification at | BSL-4 containment | BSL-4 covers “highly dangerous, life-threatening agents often lacking vaccines or treatments” (gao2024frombiosafetyto pages 6-7) | Gao et al., doi:10.3390/laboratories1030013, 2024 | Strong but high-level; applies at agent/classification level, not necessarily trait of every strain. |
| route of inoculation / modes of transmission | is input to | biorisk assessment | BRM focused on “route of inoculation/modes of transmission” as one of the practical criteria used in biorisk assessment (blacksell2023thebiosafetyresearch pages 1-2) | Blacksell et al., doi:10.1089/apb.2022.0040, 2023 | Strong evidence for assessment input. |
| infectious dose | is input to | biorisk assessment | BRM identified “infectious dose” among the practical criteria used in biosafety risk assessment (blacksell2023thebiosafetyresearch pages 1-2) | Blacksell et al., doi:10.1089/apb.2022.0040, 2023 | Strong evidence for assessment input. |
| laboratory-acquired infection history | is input to | biorisk assessment | BRM listed “laboratory-acquired infections” among the criteria examined to support evidence-based biorisk management (blacksell2023thebiosafetyresearch pages 1-2) | Blacksell et al., doi:10.1089/apb.2022.0040, 2023 | Strong as evidence source/history input; indirect for any single microbe. |
| containment release history / potential | is input to | biorisk assessment | BRM included “containment releases” in its gap analysis of evidence needed for biosafety decisions (blacksell2023thebiosafetyresearch pages 1-2) | Blacksell et al., doi:10.1089/apb.2022.0040, 2023 | Strong as systems-level assessment input. |
| disinfection / decontamination strategy evidence | is input to | biorisk assessment | BRM included “disinfection/decontamination strategies” among key criteria for evidence-based biosafety decisions (blacksell2023thebiosafetyresearch pages 1-2) | Blacksell et al., doi:10.1089/apb.2022.0040, 2023 | Strong as control-measure input; not organism-intrinsic. |
| sharps-related incidents | contributes to | laboratory exposure incidents | In 2022, “sharps and procedure-related issues were the most common occurrences (n=15; 24.2% each)” among confirmed exposure incidents (abalos2023surveillanceoflaboratory pages 1-2) | Abalos et al., doi:10.14745/ccdr.v49i09a06, 2023 | Strong epidemiologic support from surveillance; edge is about incident causation, not BSL assignment. |
| human interaction / human factors | contributes to | laboratory exposure incidents | In 2021, “human interaction factors… were the most-cited root cause (29; 28.2%)”; in 2022, “Human interaction was the most common root cause” (thompson2022surveillanceoflaboratory pages 1-2, abalos2023surveillanceoflaboratory pages 1-2) | Thompson et al., doi:10.14745/ccdr.v48i10a08, 2022; Abalos et al., doi:10.14745/ccdr.v49i09a06, 2023 | Strong surveillance support; human-factor edge should likely stay outside organism-centered TraitMech core. |
| standard operating procedure issues | contributes to | laboratory exposure incidents | Across 2016–2022, “standard operating procedure-related root causes were most cited (24%)” (balbontin2024canadianlaboratoryincidents pages 2-3) | Balbontin et al., doi:10.14745/ccdr.v50i05a04, 2024 | Strong surveillance support; operational rather than microbial. |
| inhalation exposure route | accounts for substantial fraction of | laboratory exposure incidents | In 2021, “Most exposures were via inhalation (38; 52.8%)” (thompson2022surveillanceoflaboratory pages 1-2) | Thompson et al., doi:10.14745/ccdr.v48i10a08, 2022 | Strong observational support; useful for prioritizing aerosol containment logic. |
| ISO 35001 biorisk management system | enables | continual improvement in biorisk management | ISO 35001 provides a management-system approach and “emphasizes continual improvement via Plan-Do-Check-Act” (callihan2021considerationsforlaboratory pages 1-2, morris2024worththerisk? pages 1-2) | Callihan et al., doi:10.1089/apb.20.0068, 2021; Morris, doi:10.26686/nzjhsp.v1i2.9540, 2024 | Strong for governance/operations; not a biological-mechanism edge. |


*Table: This table lists candidate causal edges relevant to biosafety level classification and management, grounded in retrieved sources. It is useful for deciding which edges are suitable for curation into a TraitMech-style graph and which are better treated as contextual or operational metadata.*

### 7) Warnings / curation notes (what not to over-curate)

1. **BSL is not a microbial phenotype per se.** It is a *classification* that results from combining agent hazard with task/exposure context and available mitigations; causal graphs should therefore treat “biosafety level” as an outcome node downstream of risk assessment rather than as a direct gene-to-trait mapping (forbesUnknownyearlaboratoryareas pages 137-140, kimman2008evidencebasedbiosafetya pages 7-8).
2. **RG–BSL mappings are jurisdiction- and task-dependent.** Sources explicitly caution that risk assessment must consider manipulations/activities and worker experience; avoid hard-coding one-to-one RG→BSL edges unless scoped to a specific regulatory framework (kimman2008evidencebasedbiosafetya pages 6-7, forbesUnknownyearlaboratoryareas pages 137-140).
3. **Operational incident causes (human factors, SOP deviations, sharps) are not organism-intrinsic.** These are important for biosafety systems but should be curated separately (e.g., as facility-level modifiers) if TraitMech is intended to represent microbial mechanisms (abalos2023surveillanceoflaboratory pages 1-2, balbontin2024canadianlaboratoryincidents pages 2-3).
4. **WHO LBM4 “shift” evidence is indirect here.** We have strong secondary evidence via implementation/training literature; direct quotes from WHO LBM4 itself were not retrieved in this run, so treat the LBM4 framing node as policy-context with moderate confidence pending primary manual quotation (sarwar2021pakistan’sexperiencewith pages 2-3, sarwar2021pakistan’sexperiencewith pages 1-2).

### 8) DOI-first bibliography (with URLs and publication dates)

**Core biosafety level / biorisk frameworks and recent analyses**
- Gao W et al. *From Biosafety to National Security: The Evolution and Challenges of Biosafety Laboratories.* **Laboratories**. **2024-12**. DOI:10.3390/laboratories1030013. https://doi.org/10.3390/laboratories1030013 (gao2024frombiosafetyto pages 5-6, gao2024frombiosafetyto pages 6-7)
- Morris E. *Worth the risk? ISO 35001: Biorisk management in New Zealand laboratories.* **New Zealand Journal of Health and Safety Practice**. **2024-08**. DOI:10.26686/nzjhsp.v1i2.9540. https://doi.org/10.26686/nzjhsp.v1i2.9540 (morris2024worththerisk? pages 1-2)
- Blacksell SD et al. *The Biosafety Research Road Map: The Search for Evidence to Support Practices in Human and Veterinary Laboratories.* **Applied Biosafety**. **2023-06**. DOI:10.1089/apb.2022.0040. https://doi.org/10.1089/apb.2022.0040 (blacksell2023thebiosafetyresearch pages 1-2)

**Incident surveillance / real-world implementation (Canada)**
- Balbontin N et al. *Canadian laboratory incidents with human pathogens and toxins: An overview of reports, 2016–2022.* **Canada Communicable Disease Report**. **2024-05**. DOI:10.14745/ccdr.v50i05a04. https://doi.org/10.14745/ccdr.v50i05a04 (balbontin2024canadianlaboratoryincidents pages 2-3, balbontin2024canadianlaboratoryincidents media 5423ea10)
- Abalos C et al. *Surveillance of laboratory exposures to human pathogens and toxins, Canada, 2022.* **Canada Communicable Disease Report**. **2023-09**. DOI:10.14745/ccdr.v49i09a06. https://doi.org/10.14745/ccdr.v49i09a06 (abalos2023surveillanceoflaboratory pages 1-2)
- Thompson E et al. *Surveillance of laboratory exposures to human pathogens and toxins, Canada, 2021.* **Canada Communicable Disease Report**. **2022-10**. DOI:10.14745/ccdr.v48i10a08. https://doi.org/10.14745/ccdr.v48i10a08 (thompson2022surveillanceoflaboratory pages 1-2)

**ISO 35001 application discussion**
- Callihan DR et al. *Considerations for Laboratory Biosafety and Biosecurity During the Coronavirus Disease 2019 Pandemic: Applying the ISO 35001:2019 Standard and High-Reliability Organizations Principles.* **Applied Biosafety**. **2021-09**. DOI:10.1089/apb.20.0068. https://doi.org/10.1089/apb.20.0068 (callihan2021considerationsforlaboratory pages 1-2)

**High-containment labs and implementations**
- Gao W et al. *Global Safety and Health: The History of High-Level Biosafety Laboratories Toward Large Scientific Facilities.* **Laboratories**. **2025-01**. DOI:10.3390/laboratories2010003. https://doi.org/10.3390/laboratories2010003 (gao2025globalsafetyand pages 14-17)
- Fan Y-L et al. *Enhancing safety with an AI-empowered assessment and monitoring system for BSL-3 facilities.* **Heliyon**. **2025-01** (published online 2024). DOI:10.1016/j.heliyon.2024.e40855. https://doi.org/10.1016/j.heliyon.2024.e40855 (fan2025enhancingsafetywith pages 1-2)

**Mechanistic virulence determinants (biological inputs to hazard)**
- Coburn B et al. *Type III Secretion Systems and Disease.* **Clinical Microbiology Reviews**. **2007-10**. DOI:10.1128/cmr.00013-07. https://doi.org/10.1128/cmr.00013-07 (coburn2007typeiiisecretion pages 2-3, coburn2007typeiiisecretion pages 1-2)
- Bhavsar AP et al. *Manipulation of host-cell pathways by bacterial pathogens.* **Nature**. **2007-10**. DOI:10.1038/nature06247. https://doi.org/10.1038/nature06247 (bhavsar2007manipulationofhostcell pages 5-6)
- Angot A et al. *Exploitation of Eukaryotic Ubiquitin Signaling Pathways by Effectors Translocated by Bacterial Type III and Type IV Secretion Systems.* **PLoS Pathogens**. **2007-01**. DOI:10.1371/journal.ppat.0030003. https://doi.org/10.1371/journal.ppat.0030003 (angot2007exploitationofeukaryotic pages 1-2)
- Kimman TG et al. *Evidence-Based Biosafety: a Review of the Principles and Effectiveness of Microbiological Containment Measures.* **Clinical Microbiology Reviews**. **2008-07**. DOI:10.1128/cmr.00014-08. https://doi.org/10.1128/cmr.00014-08 (kimman2008evidencebasedbiosafetya pages 7-8, kimman2008evidencebasedbiosafetya pages 6-7)

### 9) Minimal mapping to the requested TraitMech YAML

- **Trait:** biosafety level (METPO:1001101)
- **Suggested graph interpretation:** biosafety level is an outcome of *(agent hazard determinants + exposure determinants + available controls)*, mediated by risk assessment and policy frameworks (sarwar2021pakistan’sexperiencewith pages 1-2, blacksell2023thebiosafetyresearch pages 1-2).

**Recommended curated core edges for TraitMech (highest confidence):**
- inhalation transmission risk → requires BSL-3 containment (gao2024frombiosafetyto pages 5-6, gao2024frombiosafetyto pages 6-7)
- lack of treatments/vaccines → supports BSL-4 classification (gao2024frombiosafetyto pages 6-7)
- route of transmission / infectious dose / LAI history / containment releases / decontamination efficacy → inputs to risk assessment → selection of containment controls (blacksell2023thebiosafetyresearch pages 1-2, sarwar2021pakistan’sexperiencewith pages 1-2)

**Edges to curate as “context/operations” rather than microbial mechanisms:**
- SOP or human-factor failures → exposure incidents (abalos2023surveillanceoflaboratory pages 1-2, balbontin2024canadianlaboratoryincidents pages 2-3)

**Edges to curate as “biological hazard determinants” upstream of risk group/BSL:**
- secretion systems / effector translocation / toxins → host damage/immune evasion → increased virulence/hazard potential (coburn2007typeiiisecretion pages 2-3, bhavsar2007manipulationofhostcell pages 5-6, allende2025updateofthe pages 10-11)


References

1. (gao2024frombiosafetyto pages 5-6): Wanying Gao, Zongzhen Wu, Kunlan Zuo, Qiangyu Xiang, Lu Zhang, Xiaoya Chen, Feng Tan, and Huan Liu. From biosafety to national security: the evolution and challenges of biosafety laboratories. Laboratories, 1:158-173, Dec 2024. URL: https://doi.org/10.3390/laboratories1030013, doi:10.3390/laboratories1030013. This article has 12 citations.

2. (gao2024frombiosafetyto pages 6-7): Wanying Gao, Zongzhen Wu, Kunlan Zuo, Qiangyu Xiang, Lu Zhang, Xiaoya Chen, Feng Tan, and Huan Liu. From biosafety to national security: the evolution and challenges of biosafety laboratories. Laboratories, 1:158-173, Dec 2024. URL: https://doi.org/10.3390/laboratories1030013, doi:10.3390/laboratories1030013. This article has 12 citations.

3. (kimman2008evidencebasedbiosafetya pages 7-8): Tjeerd G. Kimman, Eric Smit, and Michèl R. Klein. Evidence-based biosafety: a review of the principles and effectiveness of microbiological containment measures. Clinical Microbiology Reviews, 21:403-425, Jul 2008. URL: https://doi.org/10.1128/cmr.00014-08, doi:10.1128/cmr.00014-08. This article has 202 citations and is from a highest quality peer-reviewed journal.

4. (kimman2008evidencebasedbiosafetya pages 6-7): Tjeerd G. Kimman, Eric Smit, and Michèl R. Klein. Evidence-based biosafety: a review of the principles and effectiveness of microbiological containment measures. Clinical Microbiology Reviews, 21:403-425, Jul 2008. URL: https://doi.org/10.1128/cmr.00014-08, doi:10.1128/cmr.00014-08. This article has 202 citations and is from a highest quality peer-reviewed journal.

5. (morris2024worththerisk? pages 1-2): Emma Morris. Worth the risk? iso 35001: biorisk management in new zealand laboratories. New Zealand Journal of Health and Safety Practice, Aug 2024. URL: https://doi.org/10.26686/nzjhsp.v1i2.9540, doi:10.26686/nzjhsp.v1i2.9540. This article has 2 citations.

6. (forbesUnknownyearlaboratoryareas pages 137-140): BA Forbes. Laboratory areas. Unknown journal, Unknown year.

7. (sarwar2021pakistan’sexperiencewith pages 2-3): Samreen Sarwar and Viji Vijayan. Pakistan’s experience with risk assessment training and implementation of concepts from the 4th edition of the who laboratory biosafety manual. Journal of Biosafety and Biosecurity, 3(2):99-107, Dec 2021. URL: https://doi.org/10.1016/j.jobb.2021.09.002, doi:10.1016/j.jobb.2021.09.002. This article has 11 citations.

8. (sarwar2021pakistan’sexperiencewith pages 1-2): Samreen Sarwar and Viji Vijayan. Pakistan’s experience with risk assessment training and implementation of concepts from the 4th edition of the who laboratory biosafety manual. Journal of Biosafety and Biosecurity, 3(2):99-107, Dec 2021. URL: https://doi.org/10.1016/j.jobb.2021.09.002, doi:10.1016/j.jobb.2021.09.002. This article has 11 citations.

9. (blacksell2023thebiosafetyresearch pages 1-2): Stuart D. Blacksell, Sandhya Dhawan, Marina Kusumoto, Kim Khanh Le, Kathrin Summermatter, Joseph O'Keefe, Joseph Kozlovac, Salama Suhail Almuhairi, Indrawati Sendow, Christina M. Scheel, Anthony Ahumibe, Zibusiso M. Masuku, Allan M. Bennett, Kazunobu Kojima, David R. Harper, and Keith Hamilton. The biosafety research road map: the search for evidence to support practices in human and veterinary laboratories. Applied Biosafety, 28:64-71, Jun 2023. URL: https://doi.org/10.1089/apb.2022.0040, doi:10.1089/apb.2022.0040. This article has 32 citations.

10. (gao2024frombiosafetyto pages 3-5): Wanying Gao, Zongzhen Wu, Kunlan Zuo, Qiangyu Xiang, Lu Zhang, Xiaoya Chen, Feng Tan, and Huan Liu. From biosafety to national security: the evolution and challenges of biosafety laboratories. Laboratories, 1:158-173, Dec 2024. URL: https://doi.org/10.3390/laboratories1030013, doi:10.3390/laboratories1030013. This article has 12 citations.

11. (gao2024frombiosafetyto pages 9-10): Wanying Gao, Zongzhen Wu, Kunlan Zuo, Qiangyu Xiang, Lu Zhang, Xiaoya Chen, Feng Tan, and Huan Liu. From biosafety to national security: the evolution and challenges of biosafety laboratories. Laboratories, 1:158-173, Dec 2024. URL: https://doi.org/10.3390/laboratories1030013, doi:10.3390/laboratories1030013. This article has 12 citations.

12. (abalos2023surveillanceoflaboratory pages 1-2): Christine Abalos, Audrey Gauthier, Antoinette Davis, Cailey Ellis, Nathalie Balbontin, Aryan Kapur, and Samuel Bonti-Ankomah. Surveillance of laboratory exposures to human pathogens and toxins, canada, 2022. Canada Communicable Disease Report, 49:398-405, Sep 2023. URL: https://doi.org/10.14745/ccdr.v49i09a06, doi:10.14745/ccdr.v49i09a06. This article has 6 citations.

13. (balbontin2024canadianlaboratoryincidents pages 2-3): Nathalie Balbontin, Audrey Gauthier, Christine Abalos, Antoinette Davis, and Meaghan Lister. Canadian laboratory incidents with human pathogens and toxins: an overview of reports, 2016–2022. Canada Communicable Disease Report, 50:144-152, May 2024. URL: https://doi.org/10.14745/ccdr.v50i05a04, doi:10.14745/ccdr.v50i05a04. This article has 7 citations.

14. (balbontin2024canadianlaboratoryincidents media 5423ea10): Nathalie Balbontin, Audrey Gauthier, Christine Abalos, Antoinette Davis, and Meaghan Lister. Canadian laboratory incidents with human pathogens and toxins: an overview of reports, 2016–2022. Canada Communicable Disease Report, 50:144-152, May 2024. URL: https://doi.org/10.14745/ccdr.v50i05a04, doi:10.14745/ccdr.v50i05a04. This article has 7 citations.

15. (callihan2021considerationsforlaboratory pages 1-2): Donald R. Callihan, Marian Downing, Esmeralda Meyer, Luis Alberto Ochoa, Brian Petuch, Paul Tranchell, and David White. Considerations for laboratory biosafety and biosecurity during the coronavirus disease 2019 pandemic: applying the iso 35001:2019 standard and high-reliability organizations principles. Sep 2021. URL: https://doi.org/10.1089/apb.20.0068, doi:10.1089/apb.20.0068. This article has 24 citations.

16. (gao2025globalsafetyand pages 14-17): Wanying Gao, Zongzhen Wu, Kunlan Zuo, Qiangyu Xiang, Lu Zhang, Xiaoya Chen, Feng Tan, and Huan Liu. Global safety and health: the history of high-level biosafety laboratories toward large scientific facilities. Laboratories, 2:3, Jan 2025. URL: https://doi.org/10.3390/laboratories2010003, doi:10.3390/laboratories2010003. This article has 2 citations.

17. (fan2025enhancingsafetywith pages 1-2): Yi-Ling Fan, Ching-Han Hsu, Ju-Yu Wu, Ying-Ying Tsai, Wei J. Chen, Min-Shi Lee, Fang-Rong Hsu, and Lun-De Liao. Enhancing safety with an ai-empowered assessment and monitoring system for bsl-3 facilities. Heliyon, 11:e40855, Jan 2025. URL: https://doi.org/10.1016/j.heliyon.2024.e40855, doi:10.1016/j.heliyon.2024.e40855. This article has 6 citations.

18. (thompson2022surveillanceoflaboratory pages 1-2): Emily Thompson, Maryem El Jaouhari, Nadine Eltayeb, Christine Abalos, Megan Striha, Rojiemiahd Edjoc, Collins Ayoo, and Samuel Bonti-Ankomah. Surveillance of laboratory exposures to human pathogens and toxins, canada, 2021. Canada Communicable Disease Report, 48:484-491, Oct 2022. URL: https://doi.org/10.14745/ccdr.v48i10a08, doi:10.14745/ccdr.v48i10a08. This article has 8 citations.

19. (gao2025globalsafetyand pages 6-8): Wanying Gao, Zongzhen Wu, Kunlan Zuo, Qiangyu Xiang, Lu Zhang, Xiaoya Chen, Feng Tan, and Huan Liu. Global safety and health: the history of high-level biosafety laboratories toward large scientific facilities. Laboratories, 2:3, Jan 2025. URL: https://doi.org/10.3390/laboratories2010003, doi:10.3390/laboratories2010003. This article has 2 citations.

20. (coburn2007typeiiisecretion pages 2-3): Bryan Coburn, Inna Sekirov, and B. Brett Finlay. Type iii secretion systems and disease. Clinical Microbiology Reviews, 20:535-549, Oct 2007. URL: https://doi.org/10.1128/cmr.00013-07, doi:10.1128/cmr.00013-07. This article has 926 citations and is from a highest quality peer-reviewed journal.

21. (bhavsar2007manipulationofhostcell pages 5-6): Amit P. Bhavsar, Julian A. Guttman, and B. Brett Finlay. Manipulation of host-cell pathways by bacterial pathogens. Oct 2007. URL: https://doi.org/10.1038/nature06247, doi:10.1038/nature06247. This article has 674 citations and is from a highest quality peer-reviewed journal.

22. (abdallah2007typeviisecretion—mycobacteria pages 35-37): AM Abdallah and NC Gey van Pittius. Type vii secretion—mycobacteria show the way. Unknown journal, 2007.

23. (allende2025updateofthe pages 10-11): Ana Allende, Avelino Alvarez‐Ordóñez, Valeria Bortolaia, Sara Bover‐Cid, Alessandra De Cesare, Wietske Dohmen, Laurent Guillier, Liesbeth Jacxsens, Maarten Nauta, Lapo Mughini‐Gras, Jakob Ottoson, Luisa Peixe, Fernando Perez‐Rodriguez, Panagiotis Skandamis, Elisabetta Suffredini, Pier Sandro Cocconcelli, Pablo Salvador Fernández Escámez, Miguel Prieto Maradona, Amparo Querol, Lolke Sijtsma, Juan Evaristo Suarez, Ingvar Sundh, Angela Botteon, Barizzone Fulvio, Sandra Correia, and Lieve Herman. Update of the list of qualified presumption of safety (qps) recommended microbiological agents intentionally added to food or feed as notified to efsa 21: suitability of taxonomic units notified to efsa until september 2024. EFSA Journal, Jan 2025. URL: https://doi.org/10.2903/j.efsa.2025.9169, doi:10.2903/j.efsa.2025.9169. This article has 46 citations and is from a peer-reviewed journal.

24. (atchessi2021surveillanceoflaboratory pages 1-2): Nicole Atchessi, Megan Striha, Rojiemiahd Edjoc, Emily Thompson, Maryem El Jaouhari, and Marianne Heisz. Surveillance of laboratory exposures to human pathogens and toxins, canada 2020. Canada communicable disease report = Releve des maladies transmissibles au Canada, 47 10:422-429, Oct 2021. URL: https://doi.org/10.14745/ccdr.v47i10a04, doi:10.14745/ccdr.v47i10a04. This article has 14 citations.

25. (coburn2007typeiiisecretion pages 1-2): Bryan Coburn, Inna Sekirov, and B. Brett Finlay. Type iii secretion systems and disease. Clinical Microbiology Reviews, 20:535-549, Oct 2007. URL: https://doi.org/10.1128/cmr.00013-07, doi:10.1128/cmr.00013-07. This article has 926 citations and is from a highest quality peer-reviewed journal.

26. (angot2007exploitationofeukaryotic pages 1-2): Aurélie Angot, Annette Vergunst, Stéphane Genin, and Nemo Peeters. Exploitation of eukaryotic ubiquitin signaling pathways by effectors translocated by bacterial type iii and type iv secretion systems. PLoS Pathogens, 3:e3, Jan 2007. URL: https://doi.org/10.1371/journal.ppat.0030003, doi:10.1371/journal.ppat.0030003. This article has 217 citations and is from a highest quality peer-reviewed journal.