---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T20:01:44.127145'
end_time: '2026-06-17T20:25:10.051178'
duration_seconds: 1405.92
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: biosafety level 3
  trait_identifier: METPO:1001104
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: biosafety_level_3
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A biosafety level that can cause serious or potentially lethal disease
    through inhalation or other routes, requiring specialized containment facilities
    with controlled access, directional airflow, and strict safety protocols.
  parent_traits: METPO:1001101
  synonyms: 3, 3**
  evidence_summary: 'DOI:10.1146/annurev.micro.62.081307.162938: virulence factors
    (Virulence-factor review supports highly virulent aerosol-transmissible pathogens
    (serious or potentially lethal disease) as BSL-3 agents.)'
  causal_graph_summary: 'biosafety_level_3_serious_hazard: 3 nodes, 2 edges'
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
- **Trait label:** biosafety level 3
- **METPO identifier:** METPO:1001104
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biosafety level that can cause serious or potentially lethal disease through inhalation or other routes, requiring specialized containment facilities with controlled access, directional airflow, and strict safety protocols.
- **Parent traits:** METPO:1001101
- **Synonyms:** 3, 3**
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports highly virulent aerosol-transmissible pathogens (serious or potentially lethal disease) as BSL-3 agents.)
- **Existing causal graph summary:** biosafety_level_3_serious_hazard: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **biosafety level 3** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/biosafety_level_3.yaml`.

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
- **Trait label:** biosafety level 3
- **METPO identifier:** METPO:1001104
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biosafety level that can cause serious or potentially lethal disease through inhalation or other routes, requiring specialized containment facilities with controlled access, directional airflow, and strict safety protocols.
- **Parent traits:** METPO:1001101
- **Synonyms:** 3, 3**
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports highly virulent aerosol-transmissible pathogens (serious or potentially lethal disease) as BSL-3 agents.)
- **Existing causal graph summary:** biosafety_level_3_serious_hazard: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **biosafety level 3** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/biosafety_level_3.yaml`.

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


## Microbial Trait Causal Graph Curation Report: Biosafety Level 3 (BSL-3)

**Target trait:** biosafety level 3 (METPO:1001104; ECOLOGY; CLASS)  
**Working definition (curation-aligned):** A containment level used for work with agents that can cause serious or potentially lethal disease, especially via **inhalation/aerosol exposure**, requiring controlled access and specialized engineering controls (directional airflow/negative pressure, filtration) and strict operational practices. (bawshkhah2024thebiosafetylevel pages 2-3, gao2024frombiosafetyto pages 5-6)

### 1) Scope summary (Trait Scope)

#### 1.1 What the trait represents
BSL-3 is best treated as a **risk/containment classification trait** applied to a microorganism (or a specific work context with that microorganism) based on the combination of (i) hazard severity and (ii) exposure route likelihood, particularly inhalation. Recent sources summarize BSL-3 as appropriate for agents that “may cause serious or lethal disease primarily via inhalation” and requiring “controlled access” and “directional airflow.” (gao2024frombiosafetyto pages 5-6, gao2024frombiosafetyto pages 6-7)

Operationally, BSL-3 is also defined through the **engineering and procedural controls** that must be in place, including negative pressure and HEPA filtration, plus respiratory protection (e.g., N95/PAPR) and primary containment equipment (biosafety cabinets). (bawshkhah2024thebiosafetylevel pages 2-3, blacksell2023thebiosafetyresearchc pages 13-14)

#### 1.2 Boundary cases and distinctions from nearby traits
- **BSL-2 vs BSL-3:** A 2024 review distinguishes BSL-2 as “moderate hazards” with typical PPE and “open bench work,” while BSL-3 adds respirators (N95/PAPR), negative pressure (reported range 2.5–10 Pa), and HEPA filtration (99.97% removal for ≥0.3 µm particles). (bawshkhah2024thebiosafetylevel pages 2-3)
- **BSL-3 vs BSL-4:** BSL-4 is reserved for the most dangerous agents, often lacking vaccines/treatments and requiring maximum containment (e.g., positive-pressure suits or Class III cabinets). (bawshkhah2024thebiosafetylevel pages 2-3, gao2024frombiosafetyto pages 6-7)
- **“BSL-3 enhanced” / “BSL-3+”:** Several 2024 sources discuss “BSL-3+ / BSL-3 enhanced” as an *operational/assurance* boundary concept rather than a universally standardized level. For example, a Brazil governance assessment notes some facilities previously referred to as ‘BSL-4’ (WOAH context) are now better regarded as “BSL-3 enhanced” under BMBL framing. (mendonca2024enhancingbiosafetymanagement pages 93-95)

**Curation note:** In TraitMech, this trait is a **classification outcome**. Many candidate edges are therefore *curation-policy* (classification/requirements) rather than purely biological causation.

---

### 2) Key concepts & definitions (current understanding)

#### 2.1 Mechanistic hazard drivers that justify BSL-3 classification
Evidence from agent-focused biosafety roadmaps emphasizes that BSL-3 classification is often driven by:
- **Aerosol/inhalation transmission** and ability to aerosolize (e.g., Brucella “easily aerosolized”). (blacksell2023thebiosafetyresearchc pages 9-10)
- **Low infectious dose** via inhalation for some agents (e.g., M. tuberculosis ID50 estimated <10 bacilli; Brucella as few as 10–100 inhaled organisms). (blacksell2023thebiosafetyresearchb pages 9-10, blacksell2023thebiosafetyresearchc pages 9-10)
- **Documented laboratory-acquired infections (LAIs)** supporting higher containment requirements (e.g., Brucella with hundreds of LAIs in compiled reports). (blacksell2023thebiosafetyresearchc pages 9-10, blacksell2023thebiosafetyresearchc pages 8-9)
- **Environmental persistence** that increases exposure potential (e.g., B. anthracis endospore stability; persistence of Brucella in various matrices). (blacksell2023thebiosafetyresearchc pages 2-3, blacksell2023thebiosafetyresearchc pages 8-9)

#### 2.2 Engineering controls and verification (defining operational content)
A 2024 BSL-3 readiness review lists engineering controls including negative pressure, HEPA exhaust filtration, airlocks, and validated verification (smoke testing, HEPA integrity tests, pressure cascade verification), implying a strong “containment-as-engineering” component of the BSL-3 phenotype. (bawshkhah2024thebiosafetylevel pages 2-3)

Boundary integrity testing is a recent engineering-focused development: Ziegler & Tremblay (Applied Biosafety, 2024) recommend a two-step approach (qualitative leak finding + quantitative leakage testing) and report quantitative leakage criteria such as USDA ARS greenhouse acceptance **0.139 L/s·m² at 250 Pa**, with stricter VDI criterion **0.03620 L/s·m² at 250 Pa** for primary containment CL3 rooms, and that **55%** of typical CL3 rooms met proposed criteria. (ziegler2024boundaryintegritytesting pages 1-2, ziegler2024boundaryintegritytesting pages 7-9)

---

### 3) Candidate nodes grouped by type (ontology grounding where possible)

| Node Type | Candidate Node Label | Suggested CURIE | Evidence Source(s) |
|---|---|---|---|
| Biological Process / Hazard | Aerosol transmission / inhalation risk | GO:0140502 | (bawshkhah2024thebiosafetylevel pages 3-4, blacksell2023thebiosafetyresearchc pages 9-10, blacksell2023thebiosafetyresearchc pages 1-2) |
| Biological Process / Hazard | Environmental persistence / endospore formation | GO:0030435 | (blacksell2023thebiosafetyresearchc pages 2-3, blacksell2023thebiosafetyresearchc pages 1-2) |
| Experimental Factor / Hazard | Median infectious dose (ID50) | OBI:0001928 | (blacksell2023thebiosafetyresearchc pages 9-10, blacksell2023thebiosafetyresearchc pages 2-3) |
| Experimental Factor / Hazard | Laboratory-acquired infection (LAI) | | (blacksell2023thebiosafetyresearchc pages 9-10, blacksell2023thebiosafetyresearchc pages 8-9) |
| Environmental / Engineering Factor | Negative pressure / directional airflow | ENVO:01000845 | (bawshkhah2024thebiosafetylevel pages 2-3, ziegler2024boundaryintegritytesting pages 5-7) |
| Environmental / Engineering Factor | HEPA filtration | ENVO:01001407 | (bawshkhah2024thebiosafetylevel pages 2-3) |
| Environmental / Engineering Factor | Boundary integrity testing (leakage rate) | | (ziegler2024boundaryintegritytesting pages 9-9, ziegler2024boundaryintegritytesting pages 7-9) |
| Environmental / Engineering Factor | Biological safety cabinet (BSC) | | (bawshkhah2024thebiosafetylevel pages 2-3, blacksell2023thebiosafetyresearchc pages 13-14) |
| Experimental / Admin Factor | Respiratory protective equipment (N95/PAPR) | | (bawshkhah2024thebiosafetylevel pages 2-3) |
| Experimental / Admin Factor | Controlled access | | (bawshkhah2024thebiosafetylevel pages 2-3) |
| Experimental / Admin Factor | Biorisk management (ISO 35001) / risk assessment | | (morris2024worththerisk? pages 1-2, blacksell2023thebiosafetyresearchc pages 13-14) |
| Example Pathogen | *Mycobacterium tuberculosis* | NCBITaxon:1773 | (blacksell2023thebiosafetyresearchb pages 9-10, bawshkhah2024thebiosafetylevel pages 2-3) |
| Example Pathogen | *Bacillus anthracis* | NCBITaxon:1392 | (blacksell2023thebiosafetyresearchc pages 2-3) |
| Example Pathogen | *Brucella melitensis* | NCBITaxon:234 | (blacksell2023thebiosafetyresearchc pages 8-9) |
| Example Pathogen | *SARS-CoV-2* | NCBITaxon:2697049 | (blacksell2023thebiosafetyresearcha pages 6-8, bawshkhah2024thebiosafetylevel pages 2-3) |
| Example Pathogen | *Yersinia pestis* | NCBITaxon:632 | (bawshkhah2024thebiosafetylevel pages 2-3) |
| Example Pathogen | *Francisella tularensis* | NCBITaxon:263 | (bawshkhah2024thebiosafetylevel pages 1-2) |
| Decontamination Method | Sodium hypochlorite / chlorine | CHEBI:32018 | (blacksell2023thebiosafetyresearcha pages 6-8, blacksell2023thebiosafetyresearchc pages 6-8) |
| Decontamination Method | Ethanol | CHEBI:16236 | (blacksell2023thebiosafetyresearcha pages 6-8) |
| Decontamination Method | Heat inactivation / autoclave | | (bawshkhah2024thebiosafetylevel pages 3-4, blacksell2023thebiosafetyresearcha pages 6-8, blacksell2023thebiosafetyresearchc pages 12-13) |
| Decontamination Method | Vaporized hydrogen peroxide (VHP) | CHEBI:16240 | (blacksell2023thebiosafetyresearchc pages 12-13) |
| Decontamination Method | Chlorine dioxide (ClO2) | CHEBI:29326 | (blacksell2023thebiosafetyresearchc pages 6-8) |
| Decontamination Method | Peracetic acid | CHEBI:31252 | (blacksell2023thebiosafetyresearchc pages 6-8) |
| Decontamination Method | Glutaraldehyde | CHEBI:42981 | (blacksell2023thebiosafetyresearchc pages 6-8) |
| Decontamination Method | Formaldehyde | CHEBI:16842 | (blacksell2023thebiosafetyresearchc pages 6-8) |
| Decontamination Method | Sodium hydroxide (NaOH) | CHEBI:32145 | (blacksell2023thebiosafetyresearchc pages 12-13) |
| Decontamination Method | Ozone | CHEBI:25812 | (blacksell2023thebiosafetyresearchc pages 6-8) |


*Table: This table categorizes and proposes candidate ontology nodes relevant to Biosafety Level 3 (BSL-3) containment requirements, extracting hazards, engineering and administrative controls, example agents, and decontamination chemicals verified in the 2023-2024 literature.*

---

### 4) Evidence-backed candidate causal edges (triples)

The table below proposes edges that can be curated into a TraitMech-style causal graph. Edges explicitly linking biology → “BSL-3 classification” are marked as **curation-policy** because BSL-3 is a classification decision informed by risk assessment, not a microbial biochemical pathway.

| Edge (triple) | Edge type | Reference (DOI + URL) | Publication year/month | Supporting snippet (short quote) | Notes/uncertainty | Suggested ontology grounding |
|---|---|---|---|---|---|---|
| `Mycobacterium tuberculosis` → `transmitted_by` → `aerosol inhalation` | Mechanistic | 10.1089/apb.2022.0038 (https://doi.org/10.1089/apb.2022.0038) | 2023/09 | "inhalation of aerosols/droplets as a primary transmission route" (blacksell2023thebiosafetyresearchb pages 9-10) | High confidence | NCBITaxon:1773, GO:0140502 |
| `Mycobacterium tuberculosis` → `has_infectious_dose` → `<10 bacilli` | Mechanistic | 10.1089/apb.2022.0038 (https://doi.org/10.1089/apb.2022.0038) | 2023/09 | "human infectious dose is very low (ID50 estimated <10 bacilli)" (blacksell2023thebiosafetyresearchb pages 9-10) | High confidence | NCBITaxon:1773, OBI:0001928 |
| `Risk of aerosol transmission` → `necessitates` → `Biosafety Level 3` | Administrative | 10.64483/jmph-115 (https://doi.org/10.64483/jmph-115) | 2024/12 | "can cause severe or lethal disease by aerosol route... requires respiratory protection" (bawshkhah2024thebiosafetylevel pages 2-3, bawshkhah2024thebiosafetylevel pages 1-2) | curation-policy | GO:0140502, METPO:1001104 |
| `Biosafety Level 3` → `implemented_by` → `Negative pressure airflow` | Engineering | 10.64483/jmph-115 (https://doi.org/10.64483/jmph-115) | 2024/12 | "negative pressure (2.5 to 10 Pascals) with inward airflow" (bawshkhah2024thebiosafetylevel pages 2-3) | High confidence | METPO:1001104, ENVO:01000845 |
| `Biosafety Level 3` → `implemented_by` → `HEPA filtration` | Engineering | 10.64483/jmph-115 (https://doi.org/10.64483/jmph-115) | 2024/12 | "HEPA-filtered exhaust (eliminating 99.97% of particles ≥0.3 μm)" (bawshkhah2024thebiosafetylevel pages 2-3) | High confidence | METPO:1001104, ENVO:01001407 |
| `Brucella melitensis` → `transmitted_by` → `aerosol inhalation` | Mechanistic | 10.1089/apb.2022.0042 (https://doi.org/10.1089/apb.2022.0042) | 2023/06 | "10 to 100 aerosolized organisms are needed to cause disease" (blacksell2023thebiosafetyresearchc pages 9-10) | High confidence | NCBITaxon:234, GO:0140502 |
| `Brucella melitensis` → `causes` → `Laboratory-acquired infection` | Mechanistic | 10.1089/apb.2022.0042 (https://doi.org/10.1089/apb.2022.0042) | 2023/06 | "378 LAIs reported 1979–2015" (blacksell2023thebiosafetyresearchc pages 9-10) | High confidence | NCBITaxon:234 |
| `Bacillus anthracis` → `forms` → `Endospores` | Mechanistic | 10.1089/apb.2022.0042 (https://doi.org/10.1089/apb.2022.0042) | 2023/06 | "B. anthracis endospores are highly stable in the environment" (blacksell2023thebiosafetyresearchc pages 2-3) | High confidence | NCBITaxon:1392, GO:0030435 |
| `Vaporized hydrogen peroxide` → `inactivates` → `Brucella spp.` | Mechanistic | 10.1089/apb.2022.0042 (https://doi.org/10.1089/apb.2022.0042) | 2023/06 | "Vaporized hydrogen peroxide... inactivates B. suis on nonporous surfaces" (blacksell2023thebiosafetyresearchc pages 12-13) | High confidence | CHEBI:16240, NCBITaxon:234 |
| `Biosafety Level 3` → `verified_by` → `Boundary integrity testing` | Engineering | 10.1089/apb.2023.0017 (https://doi.org/10.1089/apb.2023.0017) | 2024/03 | "quantitative leakage testing to verify it meets minimum requirements" (ziegler2024boundaryintegritytesting pages 7-9) | curation-policy | METPO:1001104 |
| `Boundary integrity testing` → `utilizes` → `Pressure decay testing` | Engineering | 10.1089/apb.2023.0017 (https://doi.org/10.1089/apb.2023.0017) | 2024/03 | "maintain a steady negative pressure during leakage testing" (ziegler2024boundaryintegritytesting pages 9-9) | High confidence | |
| `Mobile high-containment laboratory` → `monitored_by` → `Environmental sampling` | Administrative | 10.3389/fpubh.2024.1455738 (https://doi.org/10.3389/fpubh.2024.1455738) | 2024/11 | "regular weekly environmental sampling for decontamination monitoring" (mushasha2024existingoperationalstandards pages 8-9) | curation-policy | |
| `ISO 35001 Biorisk management` → `mitigates` → `Laboratory-acquired infection` | Administrative | 10.26686/nzjhsp.v1i2.9540 (https://doi.org/10.26686/nzjhsp.v1i2.9540) | 2024/08 | "safety management systems generally improve health and safety performance" (morris2024worththerisk? pages 2-4) | curation-policy | |


*Table: Candidate causal edges proposing relationships between mechanistic biological properties and corresponding BSL-3 engineering and administrative requirements based on 2023-2024 literature.*

---

### 5) Recent developments (2023–2024) and real-world implementations

#### 5.1 Agent-specific evidence bases for biorisk assessment (2023)
The Applied Biosafety “Biosafety Research Road Map” series (2023) systematizes evidence relevant to biorisk assessments for multiple high-consequence agents, focusing on routes of inoculation/transmission, infectious dose, LAIs, containment releases, and decontamination.
- For **M. tuberculosis**, the roadmap highlights inhalation and very low infectious dose (ID50 <10), and reports associations between exposures/seroconversions and lower air exchange rates—supporting engineering control emphasis. (blacksell2023thebiosafetyresearchb pages 9-10)
- For **Brucella**, the roadmap provides direct quantitative inhalational infectious dose estimates (10–100 aerosolized organisms) and large LAI burdens compiled across decades. (blacksell2023thebiosafetyresearchc pages 9-10)
- For **SARS-CoV-2**, the roadmap emphasizes that containment and PPE selection should be activity-driven and provides quantitative inactivation findings for lysis buffers, ethanol/chlorine, heat, and UVC—supporting validated decontamination decisions in BSL-3 workflows. (blacksell2023thebiosafetyresearcha pages 6-8)

#### 5.2 Engineering assurance: quantifiable boundary integrity testing (2024)
Ziegler & Tremblay’s 2024 paper reflects a shift from subjective “sealed room” concepts to measurable leakage/porosity criteria and repeatable acceptance testing for CL3/BSL-3 rooms. (ziegler2024boundaryintegritytesting pages 1-2, ziegler2024boundaryintegritytesting pages 7-9)

#### 5.3 Modular, scalable, and mobile/field implementations (2024)
- A 2024 review describes **modular/prefabricated BSL-3** approaches intended to reduce costs by **30–50%** and speed deployment, while maintaining verification practices and redundancy (dual HVAC, monitoring alarms). (bawshkhah2024thebiosafetylevel pages 2-3)
- A 2024 scoping review of rapid response mobile laboratories (RRMLs) found 46 included studies (from 163 screened), and emphasizes that biosafety/biosecurity procedures are heavily addressed during mission execution (PPE, decontamination), with structured workstreams and QA/QMS integration; it also documents evolution to “self-reliant vehicles” with molecular diagnostics and biocontainment in 2014–16 outbreak operations. (mushasha2024existingoperationalstandards pages 1-2)

#### 5.4 Governance/management systems: ISO 35001 (2024)
A 2024 New Zealand perspective describes ISO 35001:2019 as a Plan–Do–Check–Act management-system standard for biorisk management and notes limited certification uptake (“No biocontainment laboratories operating in New Zealand” certified), emphasizing internal audits/management review needs. (morris2024worththerisk? pages 2-4)

---

### 6) Relevant statistics and data points (recent sources)

- **CL3 room leakage criteria & pass rate (engineering):** 0.139 L/s·m² at 250 Pa (ARS greenhouse criterion); stricter 0.03620 L/s·m² at 250 Pa (VDI Class 4) for primary containment CL3 rooms; **55%** of typical CL3 rooms met proposed testing criteria. (ziegler2024boundaryintegritytesting pages 1-2)
- **BSL-3 readiness engineering targets:** negative pressure **2.5–10 Pa**; HEPA filtration **99.97% removal for ≥0.3 µm particles**. (bawshkhah2024thebiosafetylevel pages 2-3)
- **Infectious dose (mechanistic risk):** M. tuberculosis ID50 **<10 bacilli**; Brucella inhalational dose **10–100 organisms**; B. anthracis inhalational human ID50 ~**8,000–10,000 spores**. (blacksell2023thebiosafetyresearchb pages 9-10, blacksell2023thebiosafetyresearchc pages 9-10, blacksell2023thebiosafetyresearchc pages 2-3)
- **Incident metrics (governance/human factors):** “**1.55 incidents per 100 hours of work**”; spills **72%** (with **98%** occurring within a BSC). (mendonca2024enhancingbiosafetymanagement pages 37-39)
- **High-containment facility counts (Brazil, governance):** ~**66** self-declared HCBLs with BSL-3 characteristics; São Paulo 23 (34.9%), Rio de Janeiro 12 (18.2%); 47.0% university-affiliated; 86.8% publicly funded; FIOCRUZ 9 (13.6%). (mendonca2024enhancingbiosafetymanagement pages 93-95)
- **Underreporting and international incident data:** estimate that **30% of zoonotic LAIs are not reported**; “16 APELS worldwide between 2000 and 2021,” mostly involving RG-3 pathogens. (mendonca2024enhancingbiosafetymanagement pages 37-39)

---

### 7) Warnings / non-curation recommendations (TraitMech hygiene)

1. **Avoid curating BSL-3 as if it were a microbial biochemical pathway.** Most links to BSL-3 are classification/requirement edges (risk assessment → containment level). Mark these as *curation-policy* (as in artifact-01). (bawshkhah2024thebiosafetylevel pages 2-3, gao2024frombiosafetyto pages 5-6)
2. **“BSL-3 enhanced/BSL-3+” lacks universal standardization.** Treat it as an operational modifier node or synonym only if your ontology supports it; otherwise keep as label-only with uncertainty. (mendonca2024enhancingbiosafetymanagement pages 93-95)
3. **Do not over-generalize decontamination efficacies across matrices/agents.** The 2023 roadmap emphasizes that disinfectant concentrations/contact times can be inconsistent and should be validated per matrix and organism. (blacksell2023thebiosafetyresearchc pages 13-14, blacksell2023thebiosafetyresearchc pages 12-13)
4. **Country-specific facility counts and incident rates may be non-comparable.** Governance reports explicitly note self-declared biosafety levels and definitional ambiguity (labs vs rooms vs complexes). (mendonca2024enhancingbiosafetymanagement pages 93-95)

---

## DOI-first bibliography (with dates and URLs)

> DOI:10.1089/apb.2022.0039 — Blacksell SD, Dhawan S, Kusumoto M, et al. Jun 2023. *The Biosafety Research Road Map: The Search for Evidence to Support Practices in the Laboratory—SARS-CoV-2*. *Applied Biosafety* 28(2):87-95. URL: https://doi.org/10.1089/apb.2022.0039 (blacksell2023thebiosafetyresearcha pages 6-8)
>
> DOI:10.1089/apb.2022.0038 — Blacksell SD, Dhawan S, Kusumoto M, et al. Sep 2023. *The Biosafety Research Road Map: The Search for Evidence to Support Practices in the Laboratory—Zoonotic Avian Influenza and Mycobacterium tuberculosis*. *Applied Biosafety* 28(3):135-151. URL: https://doi.org/10.1089/apb.2022.0038 (blacksell2023thebiosafetyresearchb pages 9-10)
>
> DOI:10.1089/apb.2022.0042 — Blacksell SD, Dhawan S, Kusumoto M, et al. Jun 2023. *The Biosafety Research Road Map: The Search for Evidence to Support Practices in the Laboratory—Bacillus anthracis and Brucella melitensis*. *Applied Biosafety* 28(2):72-86. URL: https://doi.org/10.1089/apb.2022.0042 (blacksell2023thebiosafetyresearchc pages 9-10, blacksell2023thebiosafetyresearchc pages 2-3)
>
> DOI:10.1089/apb.2023.0017 — Ziegler C, Tremblay G. Mar 2024. *Boundary Integrity Testing of Containment Level 3 (Biological Safety Level 3) Laboratories*. *Applied Biosafety* 29(1):10-18. URL: https://doi.org/10.1089/apb.2023.0017 (ziegler2024boundaryintegritytesting pages 1-2)
>
> DOI:10.3389/fpubh.2024.1455738 — Mushasha R, Jimenez AP, Dolmazon V, et al. Nov 2024. *Existing operational standards for field deployments of rapid response mobile laboratories: a scoping review*. *Frontiers in Public Health* 12. URL: https://doi.org/10.3389/fpubh.2024.1455738 (mushasha2024existingoperationalstandards pages 1-2)
>
> DOI:10.26686/nzjhsp.v1i2.9540 — Morris E. Aug 2024. *Worth the risk? ISO 35001: Biorisk management in New Zealand laboratories*. *New Zealand Journal of Health and Safety Practice* 1(2). URL: https://doi.org/10.26686/nzjhsp.v1i2.9540 (morris2024worththerisk? pages 1-2, morris2024worththerisk? pages 2-4)
>
> DOI:10.3390/laboratories1030013 — Gao W, Wu Z, Zuo K, et al. Dec 2024. *From Biosafety to National Security: The Evolution and Challenges of Biosafety Laboratories*. *Laboratories* 1(3):158-173. URL: https://doi.org/10.3390/laboratories1030013 (gao2024frombiosafetyto pages 6-7, gao2024frombiosafetyto pages 5-6)
>
> DOI:10.47328/ufvbbt.2024.220 — de Oliveira Mendonça A. 2024. *Enhancing biosafety management and governance: a comprehensive assessment of high-containment biological laboratories in Brazil*. *ArXiv / UFV repository record*. URL: https://doi.org/10.47328/ufvbbt.2024.220 (mendonca2024enhancingbiosafetymanagement pages 37-39, mendonca2024enhancingbiosafetymanagement pages 93-95)
>
> DOI:10.64483/jmph-115 — Bawshkhah MA, Alshabi MYI, Alharthi YS, et al. Dec 2024. *The Biosafety Level 3 (BSL-3) Laboratory Readiness for Emerging Pathogens: A Review Study*. *Saudi Journal of Medicine and Public Health* 1(1):392-399. URL: https://doi.org/10.64483/jmph-115 (bawshkhah2024thebiosafetylevel pages 2-3, bawshkhah2024thebiosafetylevel pages 4-6)
>
> Foundational standards note: WHO *Laboratory Biosafety Manual* 4th ed. and CDC/NIH *Biosafety in Microbiological and Biomedical Laboratories (BMBL)* 6th ed. are cited and discussed by several of the above papers as core reference frameworks, but their full texts were not directly retrieved in this evidence set. (gao2024frombiosafetyto pages 6-7, gao2024frombiosafetyto pages 9-10, mendonca2024enhancingbiosafetymanagement pages 28-31)


*Blockquote: This blockquote provides a compact DOI-first bibliography of the main 2023-2024 sources used in the BSL-3 report, including dates, journals, and URLs. It also notes the foundational WHO and BMBL standards that were referenced indirectly by retrieved papers.*


References

1. (bawshkhah2024thebiosafetylevel pages 2-3): Mohammed Ahmed Bawshkhah, Mohammad Yousef Issa Alshabi, Yazeed Saad Alharthi, Tariq Abdullah AlShamrani, Mohammed labiad Almaliki, Manar Abdulaziz Almazroua, Haifa Ayedh Alzayedi, Mohammed Mansour Ahmed Hazzazi, Mohammed Hasan Alhazemi, and Manal Abdulaziz AlManshi. The biosafety level 3 (bsl-3) laboratory readiness for emerging pathogens: a review study. Saudi Journal of Medicine and Public Health, 1:392-399, Dec 2024. URL: https://doi.org/10.64483/jmph-115, doi:10.64483/jmph-115. This article has 1 citations.

2. (gao2024frombiosafetyto pages 5-6): Wanying Gao, Zongzhen Wu, Kunlan Zuo, Qiangyu Xiang, Lu Zhang, Xiaoya Chen, Feng Tan, and Huan Liu. From biosafety to national security: the evolution and challenges of biosafety laboratories. Laboratories, 1:158-173, Dec 2024. URL: https://doi.org/10.3390/laboratories1030013, doi:10.3390/laboratories1030013. This article has 12 citations.

3. (gao2024frombiosafetyto pages 6-7): Wanying Gao, Zongzhen Wu, Kunlan Zuo, Qiangyu Xiang, Lu Zhang, Xiaoya Chen, Feng Tan, and Huan Liu. From biosafety to national security: the evolution and challenges of biosafety laboratories. Laboratories, 1:158-173, Dec 2024. URL: https://doi.org/10.3390/laboratories1030013, doi:10.3390/laboratories1030013. This article has 12 citations.

4. (blacksell2023thebiosafetyresearchc pages 13-14): Stuart D. Blacksell, Sandhya Dhawan, Marina Kusumoto, Kim Khanh Le, Kathrin Summermatter, Joseph O'Keefe, Joseph Kozlovac, Salama Suhail Almuhairi, Indrawati Sendow, Christina M. Scheel, Anthony Ahumibe, Zibusiso M. Masuku, Allan M. Bennett, Kazunobu Kojima, David R. Harper, and Keith Hamilton. The biosafety research road map: the search for evidence to support practices in the laboratory—<i>bacillus anthracis</i> and <i>brucella melitensis</i>. Jun 2023. URL: https://doi.org/10.1089/apb.2022.0042, doi:10.1089/apb.2022.0042. This article has 9 citations.

5. (mendonca2024enhancingbiosafetymanagement pages 93-95): André de Oliveira Mendonça. Enhancing biosafety management and governance: a comprehensive assessment of high-containment biological laboratories in brazil. ArXiv, 2024. URL: https://doi.org/10.47328/ufvbbt.2024.220, doi:10.47328/ufvbbt.2024.220. This article has 2 citations.

6. (blacksell2023thebiosafetyresearchc pages 9-10): Stuart D. Blacksell, Sandhya Dhawan, Marina Kusumoto, Kim Khanh Le, Kathrin Summermatter, Joseph O'Keefe, Joseph Kozlovac, Salama Suhail Almuhairi, Indrawati Sendow, Christina M. Scheel, Anthony Ahumibe, Zibusiso M. Masuku, Allan M. Bennett, Kazunobu Kojima, David R. Harper, and Keith Hamilton. The biosafety research road map: the search for evidence to support practices in the laboratory—<i>bacillus anthracis</i> and <i>brucella melitensis</i>. Jun 2023. URL: https://doi.org/10.1089/apb.2022.0042, doi:10.1089/apb.2022.0042. This article has 9 citations.

7. (blacksell2023thebiosafetyresearchb pages 9-10): Stuart D. Blacksell, Sandhya Dhawan, Marina Kusumoto, Kim Khanh Le, Kathrin Summermatter, Joseph O'Keefe, Joseph Kozlovac, Salama Suhail Almuhairi, Indrawati Sendow, Christina M. Scheel, Anthony Ahumibe, Zibusiso M. Masuku, Allan M. Bennett, Kazunobu Kojima, David R. Harper, and Keith Hamilton. The biosafety research road map: the search for evidence to support practices in the laboratory—zoonotic avian influenza and <i>mycobacterium tuberculosis</i>. Applied Biosafety, 28:135-151, Sep 2023. URL: https://doi.org/10.1089/apb.2022.0038, doi:10.1089/apb.2022.0038. This article has 6 citations.

8. (blacksell2023thebiosafetyresearchc pages 8-9): Stuart D. Blacksell, Sandhya Dhawan, Marina Kusumoto, Kim Khanh Le, Kathrin Summermatter, Joseph O'Keefe, Joseph Kozlovac, Salama Suhail Almuhairi, Indrawati Sendow, Christina M. Scheel, Anthony Ahumibe, Zibusiso M. Masuku, Allan M. Bennett, Kazunobu Kojima, David R. Harper, and Keith Hamilton. The biosafety research road map: the search for evidence to support practices in the laboratory—<i>bacillus anthracis</i> and <i>brucella melitensis</i>. Jun 2023. URL: https://doi.org/10.1089/apb.2022.0042, doi:10.1089/apb.2022.0042. This article has 9 citations.

9. (blacksell2023thebiosafetyresearchc pages 2-3): Stuart D. Blacksell, Sandhya Dhawan, Marina Kusumoto, Kim Khanh Le, Kathrin Summermatter, Joseph O'Keefe, Joseph Kozlovac, Salama Suhail Almuhairi, Indrawati Sendow, Christina M. Scheel, Anthony Ahumibe, Zibusiso M. Masuku, Allan M. Bennett, Kazunobu Kojima, David R. Harper, and Keith Hamilton. The biosafety research road map: the search for evidence to support practices in the laboratory—<i>bacillus anthracis</i> and <i>brucella melitensis</i>. Jun 2023. URL: https://doi.org/10.1089/apb.2022.0042, doi:10.1089/apb.2022.0042. This article has 9 citations.

10. (ziegler2024boundaryintegritytesting pages 1-2): Cory Ziegler and Gilles Tremblay. Boundary integrity testing of containment level 3 (biological safety level 3) laboratories. Applied Biosafety, 29:10-18, Mar 2024. URL: https://doi.org/10.1089/apb.2023.0017, doi:10.1089/apb.2023.0017. This article has 1 citations.

11. (ziegler2024boundaryintegritytesting pages 7-9): Cory Ziegler and Gilles Tremblay. Boundary integrity testing of containment level 3 (biological safety level 3) laboratories. Applied Biosafety, 29:10-18, Mar 2024. URL: https://doi.org/10.1089/apb.2023.0017, doi:10.1089/apb.2023.0017. This article has 1 citations.

12. (bawshkhah2024thebiosafetylevel pages 3-4): Mohammed Ahmed Bawshkhah, Mohammad Yousef Issa Alshabi, Yazeed Saad Alharthi, Tariq Abdullah AlShamrani, Mohammed labiad Almaliki, Manar Abdulaziz Almazroua, Haifa Ayedh Alzayedi, Mohammed Mansour Ahmed Hazzazi, Mohammed Hasan Alhazemi, and Manal Abdulaziz AlManshi. The biosafety level 3 (bsl-3) laboratory readiness for emerging pathogens: a review study. Saudi Journal of Medicine and Public Health, 1:392-399, Dec 2024. URL: https://doi.org/10.64483/jmph-115, doi:10.64483/jmph-115. This article has 1 citations.

13. (blacksell2023thebiosafetyresearchc pages 1-2): Stuart D. Blacksell, Sandhya Dhawan, Marina Kusumoto, Kim Khanh Le, Kathrin Summermatter, Joseph O'Keefe, Joseph Kozlovac, Salama Suhail Almuhairi, Indrawati Sendow, Christina M. Scheel, Anthony Ahumibe, Zibusiso M. Masuku, Allan M. Bennett, Kazunobu Kojima, David R. Harper, and Keith Hamilton. The biosafety research road map: the search for evidence to support practices in the laboratory—<i>bacillus anthracis</i> and <i>brucella melitensis</i>. Jun 2023. URL: https://doi.org/10.1089/apb.2022.0042, doi:10.1089/apb.2022.0042. This article has 9 citations.

14. (ziegler2024boundaryintegritytesting pages 5-7): Cory Ziegler and Gilles Tremblay. Boundary integrity testing of containment level 3 (biological safety level 3) laboratories. Applied Biosafety, 29:10-18, Mar 2024. URL: https://doi.org/10.1089/apb.2023.0017, doi:10.1089/apb.2023.0017. This article has 1 citations.

15. (ziegler2024boundaryintegritytesting pages 9-9): Cory Ziegler and Gilles Tremblay. Boundary integrity testing of containment level 3 (biological safety level 3) laboratories. Applied Biosafety, 29:10-18, Mar 2024. URL: https://doi.org/10.1089/apb.2023.0017, doi:10.1089/apb.2023.0017. This article has 1 citations.

16. (morris2024worththerisk? pages 1-2): Emma Morris. Worth the risk? iso 35001: biorisk management in new zealand laboratories. New Zealand Journal of Health and Safety Practice, Aug 2024. URL: https://doi.org/10.26686/nzjhsp.v1i2.9540, doi:10.26686/nzjhsp.v1i2.9540. This article has 2 citations.

17. (blacksell2023thebiosafetyresearcha pages 6-8): Stuart D. Blacksell, Sandhya Dhawan, Marina Kusumoto, Kim Khanh Le, Kathrin Summermatter, Joseph O'Keefe, Joseph Kozlovac, Salama Suhail Almuhairi, Indrawati Sendow, Christina M. Scheel, Anthony Ahumibe, Zibusiso M. Masuku, Kazunobu Kojima, David R. Harper, and Keith Hamilton. The biosafety research road map: the search for evidence to support practices in the laboratory—sars-cov-2. Applied Biosafety, 28:87-95, Jun 2023. URL: https://doi.org/10.1089/apb.2022.0039, doi:10.1089/apb.2022.0039. This article has 3 citations.

18. (bawshkhah2024thebiosafetylevel pages 1-2): Mohammed Ahmed Bawshkhah, Mohammad Yousef Issa Alshabi, Yazeed Saad Alharthi, Tariq Abdullah AlShamrani, Mohammed labiad Almaliki, Manar Abdulaziz Almazroua, Haifa Ayedh Alzayedi, Mohammed Mansour Ahmed Hazzazi, Mohammed Hasan Alhazemi, and Manal Abdulaziz AlManshi. The biosafety level 3 (bsl-3) laboratory readiness for emerging pathogens: a review study. Saudi Journal of Medicine and Public Health, 1:392-399, Dec 2024. URL: https://doi.org/10.64483/jmph-115, doi:10.64483/jmph-115. This article has 1 citations.

19. (blacksell2023thebiosafetyresearchc pages 6-8): Stuart D. Blacksell, Sandhya Dhawan, Marina Kusumoto, Kim Khanh Le, Kathrin Summermatter, Joseph O'Keefe, Joseph Kozlovac, Salama Suhail Almuhairi, Indrawati Sendow, Christina M. Scheel, Anthony Ahumibe, Zibusiso M. Masuku, Allan M. Bennett, Kazunobu Kojima, David R. Harper, and Keith Hamilton. The biosafety research road map: the search for evidence to support practices in the laboratory—<i>bacillus anthracis</i> and <i>brucella melitensis</i>. Jun 2023. URL: https://doi.org/10.1089/apb.2022.0042, doi:10.1089/apb.2022.0042. This article has 9 citations.

20. (blacksell2023thebiosafetyresearchc pages 12-13): Stuart D. Blacksell, Sandhya Dhawan, Marina Kusumoto, Kim Khanh Le, Kathrin Summermatter, Joseph O'Keefe, Joseph Kozlovac, Salama Suhail Almuhairi, Indrawati Sendow, Christina M. Scheel, Anthony Ahumibe, Zibusiso M. Masuku, Allan M. Bennett, Kazunobu Kojima, David R. Harper, and Keith Hamilton. The biosafety research road map: the search for evidence to support practices in the laboratory—<i>bacillus anthracis</i> and <i>brucella melitensis</i>. Jun 2023. URL: https://doi.org/10.1089/apb.2022.0042, doi:10.1089/apb.2022.0042. This article has 9 citations.

21. (mushasha2024existingoperationalstandards pages 8-9): Rand Mushasha, Adela Paez Jimenez, Virginie Dolmazon, Jan Baumann, Andreas Jansen, Oleg Nikolayevich Storozhenko, and Charbel El-Bcheraoui. Existing operational standards for field deployments of rapid response mobile laboratories: a scoping review. Frontiers in Public Health, Nov 2024. URL: https://doi.org/10.3389/fpubh.2024.1455738, doi:10.3389/fpubh.2024.1455738. This article has 8 citations.

22. (morris2024worththerisk? pages 2-4): Emma Morris. Worth the risk? iso 35001: biorisk management in new zealand laboratories. New Zealand Journal of Health and Safety Practice, Aug 2024. URL: https://doi.org/10.26686/nzjhsp.v1i2.9540, doi:10.26686/nzjhsp.v1i2.9540. This article has 2 citations.

23. (mushasha2024existingoperationalstandards pages 1-2): Rand Mushasha, Adela Paez Jimenez, Virginie Dolmazon, Jan Baumann, Andreas Jansen, Oleg Nikolayevich Storozhenko, and Charbel El-Bcheraoui. Existing operational standards for field deployments of rapid response mobile laboratories: a scoping review. Frontiers in Public Health, Nov 2024. URL: https://doi.org/10.3389/fpubh.2024.1455738, doi:10.3389/fpubh.2024.1455738. This article has 8 citations.

24. (mendonca2024enhancingbiosafetymanagement pages 37-39): André de Oliveira Mendonça. Enhancing biosafety management and governance: a comprehensive assessment of high-containment biological laboratories in brazil. ArXiv, 2024. URL: https://doi.org/10.47328/ufvbbt.2024.220, doi:10.47328/ufvbbt.2024.220. This article has 2 citations.

25. (bawshkhah2024thebiosafetylevel pages 4-6): Mohammed Ahmed Bawshkhah, Mohammad Yousef Issa Alshabi, Yazeed Saad Alharthi, Tariq Abdullah AlShamrani, Mohammed labiad Almaliki, Manar Abdulaziz Almazroua, Haifa Ayedh Alzayedi, Mohammed Mansour Ahmed Hazzazi, Mohammed Hasan Alhazemi, and Manal Abdulaziz AlManshi. The biosafety level 3 (bsl-3) laboratory readiness for emerging pathogens: a review study. Saudi Journal of Medicine and Public Health, 1:392-399, Dec 2024. URL: https://doi.org/10.64483/jmph-115, doi:10.64483/jmph-115. This article has 1 citations.

26. (gao2024frombiosafetyto pages 9-10): Wanying Gao, Zongzhen Wu, Kunlan Zuo, Qiangyu Xiang, Lu Zhang, Xiaoya Chen, Feng Tan, and Huan Liu. From biosafety to national security: the evolution and challenges of biosafety laboratories. Laboratories, 1:158-173, Dec 2024. URL: https://doi.org/10.3390/laboratories1030013, doi:10.3390/laboratories1030013. This article has 12 citations.

27. (mendonca2024enhancingbiosafetymanagement pages 28-31): André de Oliveira Mendonça. Enhancing biosafety management and governance: a comprehensive assessment of high-containment biological laboratories in brazil. ArXiv, 2024. URL: https://doi.org/10.47328/ufvbbt.2024.220, doi:10.47328/ufvbbt.2024.220. This article has 2 citations.