---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T20:01:41.147044'
end_time: '2026-06-17T20:11:29.710444'
duration_seconds: 588.56
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: biosafety level 2
  trait_identifier: METPO:1001103
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: biosafety_level_2
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A biosafety level that poses moderate risk and is associated with human
    diseases present in the community.
  parent_traits: METPO:1001101
  synonyms: '2'
  evidence_summary: 'DOI:10.1146/annurev.micro.62.081307.162938: virulence factors
    (Virulence-factor review supports moderate-virulence community-disease pathogens
    (typically with available vaccines or therapies) as BSL-2 agents.)'
  causal_graph_summary: 'biosafety_level_2_moderate_hazard: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 36
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** biosafety level 2
- **METPO identifier:** METPO:1001103
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biosafety level that poses moderate risk and is associated with human diseases present in the community.
- **Parent traits:** METPO:1001101
- **Synonyms:** 2
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports moderate-virulence community-disease pathogens (typically with available vaccines or therapies) as BSL-2 agents.)
- **Existing causal graph summary:** biosafety_level_2_moderate_hazard: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **biosafety level 2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/biosafety_level_2.yaml`.

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
- **Trait label:** biosafety level 2
- **METPO identifier:** METPO:1001103
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biosafety level that poses moderate risk and is associated with human diseases present in the community.
- **Parent traits:** METPO:1001101
- **Synonyms:** 2
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports moderate-virulence community-disease pathogens (typically with available vaccines or therapies) as BSL-2 agents.)
- **Existing causal graph summary:** biosafety_level_2_moderate_hazard: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **biosafety level 2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/biosafety_level_2.yaml`.

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


# Research Report: Microbial Trait “Biosafety level 2” (BSL‑2) — METPO:1001103

## 0. Executive scope summary (curation-facing)
The trait **biosafety level 2 (BSL‑2)** (a.k.a. **Containment Level 2 (CL2)** or **Physical Containment 2 (PC‑2)** in some national schemes) is **not an intrinsic microbial physiology phenotype**; it is a **risk/containment classification** assigned to laboratory work with biological agents that pose **moderate hazard** and are typically aligned to **Risk Group 2 (RG2)** organisms, i.e., **“moderate individual risk, limited/low community risk”** with **effective prophylaxis or treatment generally available**. (kaufer2020laboratorybiosafetymeasures pages 3-4, blacksell2019biosafetyandbiosecurity pages 2-3, kaufer2020laboratorybiosafetymeasures pages 4-5)

In TraitMech terms, “BSL‑2” should be modeled as an **ecology/interaction-with-humans hazard-class trait** determined by (i) pathogen properties (pathogenicity, transmission mode, community spread potential, treatability), and (ii) **the activity context** (aerosol generation, culture/propagation, volume/concentration), with (iii) **controls** (BSC use, PPE, access restriction, decontamination) mediating whether work is acceptably safe at BSL‑2 vs requiring escalation to BSL‑3. (kaufer2020laboratorybiosafetymeasures pages 3-4, ta2018biosafetyandbiohazards pages 3-6, blacksell2019biosafetyandbiosecurity pages 7-8, ta2018biosafetyandbiohazards pages 6-8)

## 1. Key concepts and definitions (current understanding)

### 1.1 Core definition aligned to RG2 (“moderate risk”) 
A widely used operational definition is that **BSL‑2/PC‑2 laboratories handle microorganisms/toxins that pose a “moderate risk” to staff and the environment**, with added practices and containment relative to BSL‑1. (kaufer2020laboratorybiosafetymeasures pages 4-5, ta2018biosafetyandbiohazards pages 3-6)

Risk Group framing that underpins BSL assignment: **RG2** is defined as **“Moderate individual risk, limited community risk,”** and includes organisms that “can cause disease in a healthy host but are difficult to transmit, don’t usually cause life‑threatening illness and are readily treated or prevented.” (kaufer2020laboratorybiosafetymeasures pages 3-4)

A complementary RG2 description used in pathogen reclassification/risk-based containment discussions is that laboratory exposures may cause infection, but **“effective treatment and preventive measures are available, and the risk of spread is limited,”** and “there is usually effective prophylaxis or treatment available.” (blacksell2019biosafetyandbiosecurity pages 2-3)

### 1.2 Practical BSL‑2 control requirements (what “BSL‑2” operationally entails)
Across sources, the BSL‑2 concept is tightly coupled to **primary containment and exposure pathway control**, especially for aerosols/splashes:

* **Biological safety cabinets (BSCs)**: BSL‑2 guidance emphasizes that procedures generating aerosols/splashes should be done in **Class I/II BSCs**. (kaufer2020laboratorybiosafetymeasures pages 4-5, ta2018biosafetyandbiohazards pages 3-6)
  * Aerosol/splash-generating activities explicitly cited include **pipetting, centrifuging, grinding, blending, shaking, sonicating, and handling open containers**. (ta2018biosafetyandbiohazards pages 3-6)
* **Personal protective equipment (PPE)**: BSL‑2 requires **lab coats and gloves** and **eye protection/face protection as needed**. (kaufer2020laboratorybiosafetymeasures pages 4-5)
* **Decontamination**: Availability of an **autoclave or alternate decontamination method** and routine decontamination/contained waste handling are highlighted as key BSL‑2 elements. (kaufer2020laboratorybiosafetymeasures pages 4-5, ta2018biosafetyandbiohazards pages 3-6)
* **Administrative controls**: BSL‑2 includes **restricted access** and **additional, agent-specific training** relative to BSL‑1. (ta2018biosafetyandbiohazards pages 3-6)

### 1.3 Boundary cases: distinguish BSL‑2 from nearby traits (BSL‑1 and BSL‑3)
* **BSL‑2 vs BSL‑3**: A major boundary criterion is whether agents/procedures involve **respiratory/airborne transmission and potentially lethal infection**, which pushes containment to BSL‑3. (ta2018biosafetyandbiohazards pages 6-8, kaufer2020laboratorybiosafetymeasures pages 4-5)
* **Procedure-driven escalation**: Even for agents argued to be RG2/BSL‑2, higher containment may be required for **culture/propagation**, **necropsy/harvesting infected materials**, or **high concentration/large volume** work. (blacksell2019biosafetyandbiosecurity pages 4-5, blacksell2019biosafetyandbiosecurity pages 7-8)

## 2. Recent developments and latest research (prioritizing 2023–2024)

### 2.1 Shift toward risk-based biosafety (not “level-only” thinking)
A 2023 Applied Biosafety case study in cell/gene therapy manufacturing shows how **formal risk assessment plus cGMP contamination controls** can justify **downgrading selected BL2 elements to BL1** in a tightly controlled manufacturing context, while emphasizing that the **risk of viral contamination is not zero** and some elements should remain BL2. (godwin2023environmentalhealthand pages 1-2, godwin2023environmentalhealthand pages 2-4)

Mechanistically, this reinforces that “BSL‑2” is a **function of agent × procedure × controls**, not just the organism label.

### 2.2 2024 synthesis: updated standards landscape and governance/ethics framing
A 2024 review situates BSL systems as built on CDC/NIH and WHO frameworks and summarizes BSL‑2 as **“moderate hazard” / “moderate risk associated with human disease,”** with typical additions such as protective clothing and biohazard signage in primary health/diagnostic settings. (gao2024frombiosafetyto pages 5-6)

In parallel, 2024 bioethics/governance analysis emphasizes that BSL guidance is embedded in broader systems of **risk assessment, risk management, and oversight** (e.g., the U.S. IBC framework), and points to the **BMBL 6th edition** and **WHO Laboratory Biosafety Manual (LBM) 4th edition** as contemporary authoritative references for detailed, level-specific requirements. (resnik2024biosafetybiosecurityand pages 6-7)

### 2.3 2024 incident surveillance (real-world “BSL‑2 domain” burden)
Canadian national surveillance indicates that **most licensed facilities are RG2 (and thus CL2/BSL‑2 in practice)** and that a majority of exposure incidents involve RG2 agents:
* In Canada’s 2024 surveillance dataset, **975/1,052 (92.7%) active licences were RG2**, and implicated agents in exposure incidents were **64% RG2** (48 incidents). (tran2025surveillanceoflaboratory pages 2-4)
* Earlier annual surveillance reports show similar dominance of RG2 among exposure incidents (e.g., 2021: 61.4% RG2; 2022: 63% RG2). (thompson2022surveillanceoflaboratory pages 1-2, abalos2023surveillanceoflaboratory pages 1-2)

Although these surveillance papers are not “BSL‑2 standards,” they provide quantitative evidence that **RG2/BSL‑2 work accounts for the majority of incident burden**, making BSL‑2 controls an important real-world safety lever. (tran2025surveillanceoflaboratory pages 2-4, thompson2022surveillanceoflaboratory pages 1-2)

## 3. Current applications and real-world implementations

### 3.1 Diagnostic and research workflows: BSL‑2 with BSCs for non-propagative work
A risk-based biosafety review focused on *Orientia* spp. highlights the operational split: many jurisdictions allow **non-propagative diagnostic procedures at BSL‑2 with appropriate containment (e.g., BSC use)**, whereas **culture/propagation and high-risk manipulations require BSL‑3**. (blacksell2019biosafetyandbiosecurity pages 4-5)

### 3.2 Biobanking and routine microbiology/clinical lab operations
BSL‑2 is commonly used for handling agents/materials posing moderate hazards, including certain bacterial pathogens and **human cell lines**, with emphasis on aerosol/splash control in BSCs and standard PPE/decontamination. (ta2018biosafetyandbiohazards pages 3-6, kaufer2020laboratorybiosafetymeasures pages 4-5)

### 3.3 Manufacturing/bioprocessing: “BL2 large-scale” risk management
In large-scale cell/gene therapy manufacturing contexts, BL2 designation may be driven by the possibility of latent/adventitious human viruses in cell lines; however, intensive **traceability, testing panels, serum-free media, and closed systems** can reduce risk and support partial downgrading decisions. (godwin2023environmentalhealthand pages 1-2, godwin2023environmentalhealthand pages 2-4)

## 4. Expert opinions and analysis (authoritative sources)

### 4.1 Expert risk-assessment criteria used to determine RG2/BSL‑2
A widely cited biosafety synthesis during the SARS‑CoV‑2 period specifies that Risk Groups (and thus BSL/PC levels) are assigned based on four criteria: **(i) pathogenicity, (ii) mode/ease of transmission, (iii) host range, and (iv) availability of effective preventative measures and treatment**. (kaufer2020laboratorybiosafetymeasures pages 3-4)

These criteria align with the METPO definition emphasis on “moderate risk” and “human diseases present in the community,” but should be curated as **risk determinants**, not as microbial metabolic/physiological nodes.

### 4.2 Procedure scale and aerosolization as key escalation triggers
Risk-based containment recommendations emphasize that BSL‑2 may be acceptable for lower-risk activities in a BSC with standard PPE, but **high concentration/large volume**, or **procedures with increased aerosol risk** can require escalation (e.g., BSL‑3 secondary containment). (blacksell2019biosafetyandbiosecurity pages 7-8)

## 5. Relevant statistics and data from recent studies

### 5.1 Canada LINC surveillance: incidents are predominantly RG2 (BSL‑2 domain)
* **2016–2022 overview (published May 2024):** 928 events were reported to LINC; 361 were confirmed exposures. Most exposure incidents were rated negligible/minor; common occurrence types were sharps-related and procedure-related (23% each), and SOP-related issues were the most cited root cause (24%). 96% of affected individuals did not develop LAI and 92% received post-exposure treatment. (balbontin2024canadianlaboratoryincidents pages 1-2)
* **2024 surveillance dataset (published Dec 2025):** 1,052 active licences in 2024, 92.7% RG2; exposure incident rate 67.5 confirmed exposures per 1,000 active licences; implicated agents were 64% RG2; bacteria were 45.3% of implicated agent types. (tran2025surveillanceoflaboratory pages 2-4)

### 5.2 Exposure routes and human-factors patterns (supports emphasis on aerosol containment and SOPs)
For Canada 2021, inhalation was the predominant exposure route (52.8%) and technicians/technologists were most affected; sharps-related incidents were a leading occurrence type and “human interaction” factors were common root causes. (thompson2022surveillanceoflaboratory pages 1-2)

## 6. Candidate causal-graph entities (nodes) with ontology grounding suggestions

### 6.1 Trait node
* **biosafety level 2** — **METPO:1001103** (given)

### 6.2 Classification determinants (agent properties)
(These are typically not directly GO-groundable; treat as label nodes unless mapped to an existing ontology term.)
* **pathogenicity** (label) (kaufer2020laboratorybiosafetymeasures pages 3-4)
* **mode/ease of transmission** (label) (kaufer2020laboratorybiosafetymeasures pages 3-4)
* **host range** (label) (kaufer2020laboratorybiosafetymeasures pages 3-4)
* **availability of effective prophylaxis or treatment** (label) (kaufer2020laboratorybiosafetymeasures pages 3-4, blacksell2019biosafetyandbiosecurity pages 2-3)
* **community spread risk (limited/low)** (label) (kaufer2020laboratorybiosafetymeasures pages 3-4, blacksell2019biosafetyandbiosecurity pages 4-5)

### 6.3 Experimental/procedural factors
* **aerosol/splash-generating procedure** (label) (ta2018biosafetyandbiohazards pages 3-6)
* **pipetting / centrifugation / grinding / blending / shaking / sonication / open-container handling** (label) (ta2018biosafetyandbiohazards pages 3-6)
* **culture/propagation** (label) (blacksell2019biosafetyandbiosecurity pages 4-5)
* **necropsy / harvesting infected materials** (label) (blacksell2019biosafetyandbiosecurity pages 4-5)
* **high concentration or large volume infectious material** (label) (blacksell2019biosafetyandbiosecurity pages 7-8)

### 6.4 Engineering, PPE, and administrative controls (operational nodes)
* **biological safety cabinet (Class I/II)** (label; sometimes mappable in facility ontologies, but leave label unless stable CURIE chosen) (kaufer2020laboratorybiosafetymeasures pages 4-5, ta2018biosafetyandbiohazards pages 3-6)
* **PPE: lab coat, gloves, eye/face protection** (label) (kaufer2020laboratorybiosafetymeasures pages 4-5)
* **autoclave / waste decontamination capability** (label) (kaufer2020laboratorybiosafetymeasures pages 4-5)
* **restricted access** (label) (ta2018biosafetyandbiohazards pages 3-6)
* **agent-specific training** (label) (ta2018biosafetyandbiohazards pages 3-6)

### 6.5 Real-world incident pattern nodes (optional; likely outside “microbial mechanism” scope)
* **sharps-related incident** (label) (balbontin2024canadianlaboratoryincidents pages 1-2)
* **procedure-related incident** (label) (balbontin2024canadianlaboratoryincidents pages 1-2)
* **SOP-related root cause** (label) (balbontin2024canadianlaboratoryincidents pages 1-2)
* **human interaction/human error/workload pressure** (label) (thompson2022surveillanceoflaboratory pages 1-2)
* **inhalation exposure route** (label) (thompson2022surveillanceoflaboratory pages 1-2)

## 7. Candidate causal edges (evidence-backed triples)
The following artifact consolidates proposed edges, evidence snippets, citations, and boundary-case notes.

| Subject node (CURIE) | Predicate | Object node (CURIE) | Evidence snippet / quote | Reference | Notes |
|---|---|---|---|---|---|
| Risk group 2 pathogen / moderate individual risk, limited community risk (label; cf. RG2) | supports assignment to | biosafety level 2 / containment level 2 (METPO:1001103) | “Risk Group 2 is described as ‘Moderate individual risk, limited community risk’... The table associates RG-2 agents with BSL-2 and PC-2.” (kaufer2020laboratorybiosafetymeasures pages 3-4) | Kaufer 2020, *Laboratory biosafety measures involving SARS-CoV-2 and the classification as a risk group 3 biological agent*, doi:10.1016/j.pathol.2020.09.006, https://doi.org/10.1016/j.pathol.2020.09.006, Dec 2020 | Strong scope-defining edge; core trait boundary. Governance/classification rather than intrinsic microbial mechanism; operational. |
| pathogenicity (label) | influences selection of | biosafety level 2 / containment level 2 (METPO:1001103) | “Risk Groups are assigned based on pathogenicity, mode/ease of transmission, host range and the local availability of preventative measures and treatment.” (kaufer2020laboratorybiosafetymeasures pages 3-4) | Kaufer 2020, doi:10.1016/j.pathol.2020.09.006, https://doi.org/10.1016/j.pathol.2020.09.006, Dec 2020 | Strong but high-level; applies to risk assessment framework, not a single taxon. Operational/classification edge. |
| mode/ease of transmission (label) | influences selection of | biosafety level 2 / containment level 2 (METPO:1001103) | “Risk Groups are assigned based on pathogenicity, mode/ease of transmission...” and BSL-3 is indicated when agents are “transmissible by air and cause potentially lethal infections.” (kaufer2020laboratorybiosafetymeasures pages 3-4, kaufer2020laboratorybiosafetymeasures pages 4-5) | Kaufer 2020, doi:10.1016/j.pathol.2020.09.006, https://doi.org/10.1016/j.pathol.2020.09.006, Dec 2020 | Strong boundary edge distinguishing BSL-2 from BSL-3; airborne transmission pushes upward in containment. Operational/classification. |
| availability of effective prophylaxis or treatment (label) | supports assignment to | biosafety level 2 / containment level 2 (METPO:1001103) | RG2 organisms are “readily treated or prevented” (kaufer2020laboratorybiosafetymeasures pages 3-4); “Effective treatment and preventive measures are available, and the risk of spread is limited.” (blacksell2019biosafetyandbiosecurity pages 2-3) | Kaufer 2020, doi:10.1016/j.pathol.2020.09.006, https://doi.org/10.1016/j.pathol.2020.09.006, Dec 2020; Blacksell 2019, *Biosafety and biosecurity requirements for Orientia spp...*, doi:10.1186/s12879-019-4653-4, https://doi.org/10.1186/s12879-019-4653-4, Dec 2019 | Strong and aligns with classic RG2 framing; still classification-focused rather than mechanistic. Operational. |
| limited community spread risk (label) | supports assignment to | biosafety level 2 / containment level 2 (METPO:1001103) | RG2 is “Moderate individual risk, limited community risk” (kaufer2020laboratorybiosafetymeasures pages 3-4); Blacksell summarizes RG2 as “moderate individual risk, low community risk.” (blacksell2019biosafetyandbiosecurity pages 4-5) | Kaufer 2020, doi:10.1016/j.pathol.2020.09.006, https://doi.org/10.1016/j.pathol.2020.09.006, Dec 2020; Blacksell 2019, doi:10.1186/s12879-019-4653-4, https://doi.org/10.1186/s12879-019-4653-4, Dec 2019 | Strong trait-defining boundary. Community-risk language closely matches METPO definition. Operational/classification. |
| aerosol/splash-generating procedure (label) | necessitates use of | biological safety cabinet class I/II (label) | “all procedures where infectious or possibly infectious aerosols/splashes could be created are conducted in biological safety cabinets (BSC)” (ta2018biosafetyandbiohazards pages 3-6); BSL-2 recommends “use of a Class I or II biological safety cabinet for procedures that produce aerosols or splashes.” (kaufer2020laboratorybiosafetymeasures pages 4-5) | Ta 2018, *Biosafety and biohazards...*, doi:10.1007/978-1-4939-8935-5_19, https://doi.org/10.1007/978-1-4939-8935-5_19, Dec 2018; Kaufer 2020, doi:10.1016/j.pathol.2020.09.006, https://doi.org/10.1016/j.pathol.2020.09.006, Dec 2020 | Strong BSL-2 operational control edge. Not microbial mechanism; operational. |
| pipetting / centrifuging / grinding / blending / shaking / sonicating / handling open containers (label) | generates | infectious aerosols or splashes (label) | Ta lists aerosol-generating procedures: “pipetting, centrifuging, grinding, blending, shaking, sonicating, handling open containers” that mandate BSC use. (ta2018biosafetyandbiohazards pages 3-6) | Ta 2018, doi:10.1007/978-1-4939-8935-5_19, https://doi.org/10.1007/978-1-4939-8935-5_19, Dec 2018 | Strong assay/workflow edge supporting why BSCs are needed at BSL-2. Operational. |
| infectious aerosols or splashes (label) | increases need for | biosafety level 2 controls (METPO:1001103) | BSL-2 agents pose moderate hazards upon accidental exposure via “skin contact, inhalation, or ingestion” and aerosol/splash procedures require BSC containment. (ta2018biosafetyandbiohazards pages 3-6) | Ta 2018, doi:10.1007/978-1-4939-8935-5_19, https://doi.org/10.1007/978-1-4939-8935-5_19, Dec 2018 | Moderate-strength inferred edge: exposure route motivates controls, but source does not state assignment solely by aerosols. Operational/inferred. |
| appropriate PPE: lab coat + gloves + eye protection as needed (label) | mitigates risk in | biosafety level 2 / containment level 2 (METPO:1001103) | “Appropriate PPE (lab coats and gloves) must be worn,” with eye protection as needed in BSL-2/PC-2. (kaufer2020laboratorybiosafetymeasures pages 4-5) | Kaufer 2020, doi:10.1016/j.pathol.2020.09.006, https://doi.org/10.1016/j.pathol.2020.09.006, Dec 2020 | Strong required-control edge; operational. |
| restricted laboratory access (label) | is required for | biosafety level 2 / containment level 2 (METPO:1001103) | BSL-2 requires “restricted access” and additional agent-specific training compared with BSL-1. (ta2018biosafetyandbiohazards pages 3-6) | Ta 2018, doi:10.1007/978-1-4939-8935-5_19, https://doi.org/10.1007/978-1-4939-8935-5_19, Dec 2018 | Strong facility/practice edge; operational. |
| additional agent-specific training (label) | enables safe handling at | biosafety level 2 / containment level 2 (METPO:1001103) | BSL-2 requires “additional, agent-specific training.” (ta2018biosafetyandbiohazards pages 3-6) | Ta 2018, doi:10.1007/978-1-4939-8935-5_19, https://doi.org/10.1007/978-1-4939-8935-5_19, Dec 2018 | Strong training requirement; operational. |
| biohazard signage (label) | marks / supports compliance with | biosafety level 2 / containment level 2 (METPO:1001103) | “Biosafety Level II adds protective clothing and biohazard signs for primary health and diagnostic labs.” (gao2024frombiosafetyto pages 5-6) | Gao 2024, *From biosafety to national security...*, doi:10.3390/laboratories1030013, https://doi.org/10.3390/laboratories1030013, Dec 2024 | Moderate-strength because summarized from historical guidance; operational. |
| leakproof containers + routine decontamination + accessible autoclave (label) | reduce exposure from | infectious materials / waste (label) | BSL-2 requires “leakproof containers, decontamination...” and an “autoclave for decontamination.” (ta2018biosafetyandbiohazards pages 3-6, kaufer2020laboratorybiosafetymeasures pages 4-5) | Ta 2018, doi:10.1007/978-1-4939-8935-5_19, https://doi.org/10.1007/978-1-4939-8935-5_19, Dec 2018; Kaufer 2020, doi:10.1016/j.pathol.2020.09.006, https://doi.org/10.1016/j.pathol.2020.09.006, Dec 2020 | Strong control edge; operational. |
| human cell lines (label) | are commonly handled at | biosafety level 2 / containment level 2 (METPO:1001103) | Ta gives examples of BSL-2 materials including “human cell lines” (ta2018biosafetyandbiohazards pages 3-6); Godwin states human cell lines are handled at BL2 because of “potential for latent or adventitious human viral agents.” (godwin2023environmentalhealthand pages 1-2) | Ta 2018, doi:10.1007/978-1-4939-8935-5_19, https://doi.org/10.1007/978-1-4939-8935-5_19, Dec 2018; Godwin 2023, *Environmental health and safety offers a biosafety risk assessment...*, doi:10.1089/apb.2023.0007, https://doi.org/10.1089/apb.2023.0007, Sep 2023 | Strong application edge, but this is substrate/work-material specific rather than a general microbial mechanism. Operational/application. |
| potential latent/adventitious human viral agents (label) | motivates assignment of | human cell line work to BSL-2 (METPO:1001103) | Human cell lines are handled at BL2 “because of the potential for latent or adventitious human viral agents.” (godwin2023environmentalhealthand pages 1-2) | Godwin 2023, doi:10.1089/apb.2023.0007, https://doi.org/10.1089/apb.2023.0007, Sep 2023 | Strong for manufacturing/cell-culture context; may not generalize to all cell lines/workflows. Operational, context-specific. |
| documented cell-line origin/traceability + viral/microbial testing panels + serum-free media + closed systems (label) | lowers operational biosafety risk sufficiently to consider downgrading from | BSL-2 elements to BSL-1 elements (label) | “robust contamination controls and cGMP practices... can reduce operational biosafety risk and justify downgrading selected BL2 elements” (godwin2023environmentalhealthand pages 1-2); “the risk of viral contamination is not zero.” (godwin2023environmentalhealthand pages 2-4) | Godwin 2023, doi:10.1089/apb.2023.0007, https://doi.org/10.1089/apb.2023.0007, Sep 2023 | Important boundary case: demonstrates BSL-2 is not purely organism-intrinsic but depends on process controls and context. Uncertain outside large-scale GMP manufacturing. Operational. |
| low-risk non-propagative diagnostic work (label) | can be performed at | BSL-2 in a biological safety cabinet (METPO:1001103) | “non-propagative diagnostic work (often permitted at BSL-2 with appropriate practices/equipment such as BSC use...)” (blacksell2019biosafetyandbiosecurity pages 4-5) | Blacksell 2019, doi:10.1186/s12879-019-4653-4, https://doi.org/10.1186/s12879-019-4653-4, Dec 2019 | Moderate-strength, taxon- and procedure-specific (Orientia-focused but grounded in jurisdictional guidance). Boundary case useful for curation. Operational/specific. |
| culture / propagation / necropsy / harvesting infected materials (label) | warrants escalation to | biosafety level 3 (label) | “BSL-2 practices for non-propagative procedures but BSL-3 for culture, necropsy or harvesting of infected materials” (blacksell2019biosafetyandbiosecurity pages 4-5); high-risk activities with “high concentrations or large volumes... may require BSL-3 secondary containment.” (blacksell2019biosafetyandbiosecurity pages 7-8) | Blacksell 2019, doi:10.1186/s12879-019-4653-4, https://doi.org/10.1186/s12879-019-4653-4, Dec 2019 | Strong boundary edge showing when BSL-2 no longer suffices; organism/procedure dependent. Operational/boundary. |
| high concentration or large volume infectious material (label) | can require escalation from | biosafety level 2 to biosafety level 3 (label) | “High-risk activities involving high concentrations or large volumes... may require BSL-3 secondary containment” (blacksell2019biosafetyandbiosecurity pages 7-8) | Blacksell 2019, doi:10.1186/s12879-019-4653-4, https://doi.org/10.1186/s12879-019-4653-4, Dec 2019 | Strong but context-specific; useful as assay-scale boundary. Operational. |
| lack of person-to-person spread (label) | supports lower containment such as | biosafety level 2 (METPO:1001103) | Orientia factors arguing for lower containment include they “do not spread by person-to-person contact and are amenable to antibiotic treatment.” (blacksell2019biosafetyandbiosecurity pages 7-8) | Blacksell 2019, doi:10.1186/s12879-019-4653-4, https://doi.org/10.1186/s12879-019-4653-4, Dec 2019 | Moderate-strength, taxon-specific inference from risk-based reclassification argument. Not universally curatable without taxon context. |
| microbiology activity (label) | is frequently associated with | exposure incidents involving RG2 agents (label) | 2022: “Microbiology activities accounted for half of events (n=20; 50%).” (abalos2023surveillanceoflaboratory pages 1-2); 2021: “Microbiology activities accounted for the largest share” (n=18; 41.9%). (thompson2022surveillanceoflaboratory pages 1-2) | Abalos 2023, *Surveillance of laboratory exposures to human pathogens and toxins, Canada, 2022*, doi:10.14745/ccdr.v49i09a06, https://doi.org/10.14745/ccdr.v49i09a06, Sep 2023; Thompson 2022, *Surveillance... Canada, 2021*, doi:10.14745/ccdr.v48i10a08, https://doi.org/10.14745/ccdr.v48i10a08, Oct 2022 | Surveillance association, not mechanistic causation; useful for operational risk graph only. Operational/epidemiologic. |
| sharps-related incidents (label) | contribute to | laboratory exposure incidents in RG2-heavy settings (label) | 2022: “sharps-related and procedure-related issues (n=15 each; 24.2% each)” (abalos2023surveillanceoflaboratory pages 1-2); 2016–2022 overview: “sharps-related and procedure-related (23% each)” (balbontin2024canadianlaboratoryincidents pages 1-2) | Abalos 2023, doi:10.14745/ccdr.v49i09a06, https://doi.org/10.14745/ccdr.v49i09a06, Sep 2023; Balbontin 2024, *Canadian laboratory incidents with human pathogens and toxins...*, doi:10.14745/ccdr.v50i05a04, https://doi.org/10.14745/ccdr.v50i05a04, May 2024 | Strong surveillance pattern, but not trait-defining for microbes; better as lab-risk metadata. Operational. |
| human interaction / workload / human error (label) | contributes to | laboratory exposure incidents in RG2-heavy settings (label) | 2021: “human interaction... was the most cited root cause category (n=29; 28.2%).” (thompson2022surveillanceoflaboratory pages 1-2); 2022: “Human interaction was the leading root cause (n=20; 23.8%).” (abalos2023surveillanceoflaboratory pages 1-2) | Thompson 2022, doi:10.14745/ccdr.v48i10a08, https://doi.org/10.14745/ccdr.v48i10a08, Oct 2022; Abalos 2023, doi:10.14745/ccdr.v49i09a06, https://doi.org/10.14745/ccdr.v49i09a06, Sep 2023 | Strong incident-surveillance edge but clearly not a microbial mechanism. Operational/human-factors. |
| inhalation exposure route (label) | is common in | laboratory exposures involving RG2 pathogens (label) | 2021: “The predominant exposure route... was inhalation (n=38; 52.8%).” (thompson2022surveillanceoflaboratory pages 1-2) | Thompson 2022, doi:10.14745/ccdr.v48i10a08, https://doi.org/10.14745/ccdr.v48i10a08, Oct 2022 | Strong surveillance observation; supports importance of aerosol controls. Operational/epidemiologic. |
| RG2 pathogens (label) | account for majority of | reported Canadian laboratory exposure incidents | 2021: “human risk group 2 (RG2) pathogens (n=27; 61.4%)” (thompson2022surveillanceoflaboratory pages 1-2); 2022: “63% of incidents involved Risk Group 2 (RG2) pathogens (n=27)” (abalos2023surveillanceoflaboratory pages 1-2); 2024: “RG2 agents comprised a majority... (48, 64.0%).” (tran2025surveillanceoflaboratory pages 2-4) | Thompson 2022, doi:10.14745/ccdr.v48i10a08, https://doi.org/10.14745/ccdr.v48i10a08, Oct 2022; Abalos 2023, doi:10.14745/ccdr.v49i09a06, https://doi.org/10.14745/ccdr.v49i09a06, Sep 2023; Tran 2025, *Surveillance... Canada, 2024*, doi:10.14745/ccdr.v51i101112a04, https://doi.org/10.14745/ccdr.v51i101112a04, Dec 2025 | Strong real-world implementation/statistics edge showing practical importance of RG2/BSL-2 domain; not causal for classification itself. Operational/epidemiologic. |


*Table: This table lists candidate causal and quasi-causal edges relevant to curating the biosafety level 2 trait, combining classification criteria, laboratory controls, boundary cases, and real-world incident patterns. It is useful for separating core trait-defining edges from operational or context-specific edges that may require caution before TraitMech curation.*

## 8. Warnings / curation cautions (what should *not* be curated yet)
1. **Do not treat BSL‑2 as a microbial metabolic pathway trait.** It is a lab biosafety classification; many edges are “operational/governance.” These are still useful in TraitMech if the project explicitly models risk/containment as an ecology trait, but they are not organism-internal mechanisms. (kaufer2020laboratorybiosafetymeasures pages 3-4, kaufer2020laboratorybiosafetymeasures pages 4-5)
2. **Avoid over-generalizing taxon-specific containment arguments.** The *Orientia* reclassification argument is rich for boundaries (BSL‑2 vs BSL‑3 by procedure), but should be curated as **taxon- and procedure-scoped** edges unless additional general sources are added. (blacksell2019biosafetyandbiosecurity pages 4-5, blacksell2019biosafetyandbiosecurity pages 7-8)
3. **Incident surveillance associations are not causal microbial biology.** Root causes like SOP failures, sharps injuries, and human factors should be curated only if the graph explicitly covers lab-operations risk pathways. (balbontin2024canadianlaboratoryincidents pages 1-2, thompson2022surveillanceoflaboratory pages 1-2)
4. **Manufacturing downgrading (BL2→BL1) is context-specific.** The 2023 cGMP case demonstrates risk reduction via controls but may not generalize to academic BSL‑2 labs or to work with unknown agents. (godwin2023environmentalhealthand pages 1-2, godwin2023environmentalhealthand pages 2-4)

## 9. DOI-first bibliography (with URLs and publication dates where available)

1. **Tran EF, et al.** (Dec **2025**; surveillance year 2024). *Surveillance of laboratory exposures to human pathogens and toxins, Canada, 2024.* **DOI:** 10.14745/ccdr.v51i101112a04. URL: https://doi.org/10.14745/ccdr.v51i101112a04 (tran2025surveillanceoflaboratory pages 2-4)
2. **Balbontin N, et al.** (May **2024**). *Canadian laboratory incidents with human pathogens and toxins: An overview of reports, 2016–2022.* **DOI:** 10.14745/ccdr.v50i05a04. URL: https://doi.org/10.14745/ccdr.v50i05a04 (balbontin2024canadianlaboratoryincidents pages 1-2)
3. **Gao W, et al.** (Dec **2024**). *From Biosafety to National Security: The Evolution and Challenges of Biosafety Laboratories.* **DOI:** 10.3390/laboratories1030013. URL: https://doi.org/10.3390/laboratories1030013 (gao2024frombiosafetyto pages 5-6)
4. **Resnik DB.** (Jul **2024**). *Biosafety, biosecurity, and bioethics.* **DOI:** 10.1007/s40592-024-00204-3. URL: https://doi.org/10.1007/s40592-024-00204-3 (resnik2024biosafetybiosecurityand pages 6-7)
5. **Godwin S, et al.** (Sep **2023**). *Environmental Health and Safety Offers a Biosafety Risk Assessment for a Theoretical Model of a Gene Therapy Process Transfer from Research and Development to Large-Scale Manufacturing.* **DOI:** 10.1089/apb.2023.0007. URL: https://doi.org/10.1089/apb.2023.0007 (godwin2023environmentalhealthand pages 1-2)
6. **Abalos C, et al.** (Sep **2023**; surveillance year 2022). *Surveillance of laboratory exposures to human pathogens and toxins, Canada, 2022.* **DOI:** 10.14745/ccdr.v49i09a06. URL: https://doi.org/10.14745/ccdr.v49i09a06 (abalos2023surveillanceoflaboratory pages 1-2)
7. **Thompson E, et al.** (Oct **2022**; surveillance year 2021). *Surveillance of laboratory exposures to human pathogens and toxins, Canada, 2021.* **DOI:** 10.14745/ccdr.v48i10a08. URL: https://doi.org/10.14745/ccdr.v48i10a08 (thompson2022surveillanceoflaboratory pages 1-2)
8. **Kaufer AM, et al.** (Dec **2020**). *Laboratory biosafety measures involving SARS‑CoV‑2 and the classification as a Risk Group 3 biological agent.* **DOI:** 10.1016/j.pathol.2020.09.006. URL: https://doi.org/10.1016/j.pathol.2020.09.006 (kaufer2020laboratorybiosafetymeasures pages 3-4)
9. **Blacksell SD, et al.** (Dec **2019**). *Biosafety and biosecurity requirements for Orientia spp. diagnosis and research…* **DOI:** 10.1186/s12879-019-4653-4. URL: https://doi.org/10.1186/s12879-019-4653-4 (blacksell2019biosafetyandbiosecurity pages 4-5)
10. **Ta L, Gosa L, Nathanson DA.** (Dec **2018**). *Biosafety and Biohazards: Understanding Biosafety Levels and Meeting Safety Requirements of a Biobank.* **DOI:** 10.1007/978-1-4939-8935-5_19. URL: https://doi.org/10.1007/978-1-4939-8935-5_19 (ta2018biosafetyandbiohazards pages 3-6)


References

1. (kaufer2020laboratorybiosafetymeasures pages 3-4): Alexa M. Kaufer, Torsten Theis, Katherine A. Lau, Joanna L. Gray, and William D. Rawlinson. Laboratory biosafety measures involving sars-cov-2 and the classification as a risk group 3 biological agent. Pathology, 52:790-795, Dec 2020. URL: https://doi.org/10.1016/j.pathol.2020.09.006, doi:10.1016/j.pathol.2020.09.006. This article has 106 citations and is from a peer-reviewed journal.

2. (blacksell2019biosafetyandbiosecurity pages 2-3): Stuart D. Blacksell, Matthew T. Robinson, Paul N. Newton, Soiratchaneekorn Ruanchaimun, Jeanne Salje, Tri Wangrangsimakul, Matthew D. Wegner, Mohammad Yazid Abdad, Allan M. Bennett, Allen L. Richards, John Stenos, and Nicholas P. J. Day. Biosafety and biosecurity requirements for orientia spp. diagnosis and research: recommendations for risk-based biocontainment, work practices and the case for reclassification to risk group 2. BMC Infectious Diseases, Dec 2019. URL: https://doi.org/10.1186/s12879-019-4653-4, doi:10.1186/s12879-019-4653-4. This article has 9 citations and is from a peer-reviewed journal.

3. (kaufer2020laboratorybiosafetymeasures pages 4-5): Alexa M. Kaufer, Torsten Theis, Katherine A. Lau, Joanna L. Gray, and William D. Rawlinson. Laboratory biosafety measures involving sars-cov-2 and the classification as a risk group 3 biological agent. Pathology, 52:790-795, Dec 2020. URL: https://doi.org/10.1016/j.pathol.2020.09.006, doi:10.1016/j.pathol.2020.09.006. This article has 106 citations and is from a peer-reviewed journal.

4. (ta2018biosafetyandbiohazards pages 3-6): Lisa Ta, Laura Gosa, and David A. Nathanson. Biosafety and biohazards: understanding biosafety levels and meeting safety requirements of a biobank. Biobanking, 1897:213-225, Dec 2018. URL: https://doi.org/10.1007/978-1-4939-8935-5\_19, doi:10.1007/978-1-4939-8935-5\_19. This article has 68 citations.

5. (blacksell2019biosafetyandbiosecurity pages 7-8): Stuart D. Blacksell, Matthew T. Robinson, Paul N. Newton, Soiratchaneekorn Ruanchaimun, Jeanne Salje, Tri Wangrangsimakul, Matthew D. Wegner, Mohammad Yazid Abdad, Allan M. Bennett, Allen L. Richards, John Stenos, and Nicholas P. J. Day. Biosafety and biosecurity requirements for orientia spp. diagnosis and research: recommendations for risk-based biocontainment, work practices and the case for reclassification to risk group 2. BMC Infectious Diseases, Dec 2019. URL: https://doi.org/10.1186/s12879-019-4653-4, doi:10.1186/s12879-019-4653-4. This article has 9 citations and is from a peer-reviewed journal.

6. (ta2018biosafetyandbiohazards pages 6-8): Lisa Ta, Laura Gosa, and David A. Nathanson. Biosafety and biohazards: understanding biosafety levels and meeting safety requirements of a biobank. Biobanking, 1897:213-225, Dec 2018. URL: https://doi.org/10.1007/978-1-4939-8935-5\_19, doi:10.1007/978-1-4939-8935-5\_19. This article has 68 citations.

7. (blacksell2019biosafetyandbiosecurity pages 4-5): Stuart D. Blacksell, Matthew T. Robinson, Paul N. Newton, Soiratchaneekorn Ruanchaimun, Jeanne Salje, Tri Wangrangsimakul, Matthew D. Wegner, Mohammad Yazid Abdad, Allan M. Bennett, Allen L. Richards, John Stenos, and Nicholas P. J. Day. Biosafety and biosecurity requirements for orientia spp. diagnosis and research: recommendations for risk-based biocontainment, work practices and the case for reclassification to risk group 2. BMC Infectious Diseases, Dec 2019. URL: https://doi.org/10.1186/s12879-019-4653-4, doi:10.1186/s12879-019-4653-4. This article has 9 citations and is from a peer-reviewed journal.

8. (godwin2023environmentalhealthand pages 1-2): Simon Godwin, Shana Elkind, Timmy Carey, Kimberly DiGiandomenico, Alexa Balbo, Jemma Blocksidge, Jessica Olson, Jess Miklosko, Leo Njongmeta, Francine Preston, and Rachel Hodges. Environmental health and safety offers a biosafety risk assessment for a theoretical model of a gene therapy process transfer from research and development to large-scale manufacturing. Applied biosafety : journal of the American Biological Safety Association, 28 3:164-175, Sep 2023. URL: https://doi.org/10.1089/apb.2023.0007, doi:10.1089/apb.2023.0007. This article has 3 citations.

9. (godwin2023environmentalhealthand pages 2-4): Simon Godwin, Shana Elkind, Timmy Carey, Kimberly DiGiandomenico, Alexa Balbo, Jemma Blocksidge, Jessica Olson, Jess Miklosko, Leo Njongmeta, Francine Preston, and Rachel Hodges. Environmental health and safety offers a biosafety risk assessment for a theoretical model of a gene therapy process transfer from research and development to large-scale manufacturing. Applied biosafety : journal of the American Biological Safety Association, 28 3:164-175, Sep 2023. URL: https://doi.org/10.1089/apb.2023.0007, doi:10.1089/apb.2023.0007. This article has 3 citations.

10. (gao2024frombiosafetyto pages 5-6): Wanying Gao, Zongzhen Wu, Kunlan Zuo, Qiangyu Xiang, Lu Zhang, Xiaoya Chen, Feng Tan, and Huan Liu. From biosafety to national security: the evolution and challenges of biosafety laboratories. Laboratories, 1:158-173, Dec 2024. URL: https://doi.org/10.3390/laboratories1030013, doi:10.3390/laboratories1030013. This article has 12 citations.

11. (resnik2024biosafetybiosecurityand pages 6-7): David B. Resnik. Biosafety, biosecurity, and bioethics. Monash Bioethics Review, 42:137-167, Jul 2024. URL: https://doi.org/10.1007/s40592-024-00204-3, doi:10.1007/s40592-024-00204-3. This article has 25 citations and is from a peer-reviewed journal.

12. (tran2025surveillanceoflaboratory pages 2-4): Emily F Tran, Audrey Gauthier, Antoinette N Davis, Christine Abalos, and Samuel Bonti-Ankomah. Surveillance of laboratory exposures to human pathogens and toxins, canada, 2024. Canada Communicable Disease Report, 51:401-412, Dec 2025. URL: https://doi.org/10.14745/ccdr.v51i101112a04, doi:10.14745/ccdr.v51i101112a04. This article has 1 citations.

13. (thompson2022surveillanceoflaboratory pages 1-2): Emily Thompson, Maryem El Jaouhari, Nadine Eltayeb, Christine Abalos, Megan Striha, Rojiemiahd Edjoc, Collins Ayoo, and Samuel Bonti-Ankomah. Surveillance of laboratory exposures to human pathogens and toxins, canada, 2021. Canada Communicable Disease Report, 48:484-491, Oct 2022. URL: https://doi.org/10.14745/ccdr.v48i10a08, doi:10.14745/ccdr.v48i10a08. This article has 8 citations.

14. (abalos2023surveillanceoflaboratory pages 1-2): Christine Abalos, Audrey Gauthier, Antoinette Davis, Cailey Ellis, Nathalie Balbontin, Aryan Kapur, and Samuel Bonti-Ankomah. Surveillance of laboratory exposures to human pathogens and toxins, canada, 2022. Canada Communicable Disease Report, 49:398-405, Sep 2023. URL: https://doi.org/10.14745/ccdr.v49i09a06, doi:10.14745/ccdr.v49i09a06. This article has 6 citations.

15. (balbontin2024canadianlaboratoryincidents pages 1-2): Nathalie Balbontin, Audrey Gauthier, Christine Abalos, Antoinette Davis, and Meaghan Lister. Canadian laboratory incidents with human pathogens and toxins: an overview of reports, 2016–2022. Canada Communicable Disease Report, 50:144-152, May 2024. URL: https://doi.org/10.14745/ccdr.v50i05a04, doi:10.14745/ccdr.v50i05a04. This article has 7 citations.